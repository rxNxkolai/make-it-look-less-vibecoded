#!/usr/bin/env python3
"""Mechanical scorer for the this skill slop-test.

Covers the slop-test items that are reliably detectable from source. Items that
need a rendered screenshot or a judgement call are listed as MANUAL and scored
by hand; they are not guessed at here.

Usage:
    python score.py path/to/page.html [more.html ...]
    python score.py path/to/dir/            # walks for .html

Prints a per-file table of hit / clean / manual, then a summary line.
"""
import colorsys
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- color utils

NAMED = {
    "indigo": (75, 0, 130), "violet": (238, 130, 238), "purple": (128, 0, 128),
    "blueviolet": (138, 43, 226), "darkviolet": (148, 0, 211),
    "rebeccapurple": (102, 51, 153), "mediumpurple": (147, 112, 219),
    "slateblue": (106, 90, 205), "white": (255, 255, 255), "black": (0, 0, 0),
}
HEX_RE = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b")
RGB_RE = re.compile(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)")


def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def hue_sat(rgb):
    r, g, b = (c / 255 for c in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360, s, l


def colors_in(text):
    """Every color literal in a blob of text, as (hue, sat, light)."""
    out = []
    for m in HEX_RE.finditer(text):
        out.append(hue_sat(hex_to_rgb(m.group(0))))
    for m in RGB_RE.finditer(text):
        out.append(hue_sat(tuple(int(g) for g in m.groups())))
    for name, rgb in NAMED.items():
        if re.search(r"\b" + name + r"\b", text, re.I):
            out.append(hue_sat(rgb))
    return out


def is_violet(h, s, l):
    """Indigo / violet / purple family, saturated enough to read as a hue."""
    return 235 <= h <= 300 and s > 0.25 and 0.15 < l < 0.85


# ------------------------------------------------------------------- patterns

GRADIENT_RE = re.compile(r"(linear|radial|conic)-gradient\s*\(([^;{}]*)\)", re.I)
TW_VIOLET_RE = re.compile(
    r"\b(bg|text|from|via|to|border|ring|shadow)-(indigo|violet|purple|fuchsia)-\d{2,3}\b")
FONT_FAMILY_RE = re.compile(r"font-family\s*:\s*([^;}\n]+)", re.I)
GOOGLE_FONT_RE = re.compile(r"fonts\.googleapis\.com/css2?\?([^\"'>]+)")
DEFAULT_FACES = {"inter", "geist", "roboto", "space grotesk", "space-grotesk"}
GENERIC_FACES = {
    "sans-serif", "serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif",
    "ui-monospace", "-apple-system", "blinkmacsystemfont", "segoe ui", "helvetica",
    "helvetica neue", "arial", "cursive", "fantasy", "emoji", "math", "apple color emoji",
    "segoe ui emoji", "noto color emoji", "sans", "inherit", "initial", "unset",
}
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF✨⭐⚡]")
METRIC_RE = re.compile(
    r"(\+\s?\d{1,3}\s?%|\b\d{1,3}\s?%\s+(more|faster|increase|boost|growth|higher)"
    r"|\b\d{1,3}(,\d{3})+\+?\s+(users|customers|people|teams|developers|writers|readers|subscribers)"
    r"|\b\d+(\.\d+)?\s?[kKmM]\+?\s+(users|customers|people|teams|downloads|readers|subscribers)"
    r"|\btrusted by\b|\bjoin \d|\b\d\.\d\s?/\s?5\b|\b\d{2,3}x\b\s+(faster|better|more))", re.I)
LOREM_RE = re.compile(r"lorem ipsum|dolor sit amet|placehold(er)?\.(co|it|com)|via\.placeholder", re.I)


RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}")


def strip_print_media(text):
    """Remove @media print blocks. A white background in a print stylesheet is
    correct practice, not the untinted-#fff tell."""
    out, i = [], 0
    while True:
        m = re.search(r"@media[^{]*\bprint\b[^{]*\{", text[i:], re.I)
        if not m:
            out.append(text[i:])
            break
        start = i + m.start()
        out.append(text[i:start])
        j = i + m.end()
        depth = 1
        while j < len(text) and depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        i = j
    return "".join(out)


def style_text(text):
    """Concatenated <style> contents, print media and comments removed.

    Colour checks must read this rather than the raw file: chart series, book-spine
    swatches and other data literals inside <script> are content, not the palette,
    and counting them produces phantom 'indigo primary' hits.
    """
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", text, re.S | re.I))
    if not css.strip():
        css = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.S | re.I)
    # Comments first: a comment mentioning "@media print" would otherwise be treated
    # as a real print block and swallow live rules up to the next brace.
    css = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)
    return strip_print_media(css)


def css_rules(text):
    """[(selector, declarations)] from every <style> block, print media removed."""
    return [(m.group(1).strip(), m.group(2)) for m in RULE_RE.finditer(style_text(text))]


def sniff(text):
    """Return {item_number: (verdict, evidence)} for auto-detectable items."""
    r = {}
    low = text.lower()
    rules = css_rules(text)

    # ---- Tier 1
    css = style_text(text)
    grad_bodies = [m.group(2) for m in GRADIENT_RE.finditer(css)]
    tw_grad = re.findall(r"\bfrom-(indigo|violet|purple|fuchsia)-\d{2,3}\b", text)
    viol_grad = [g for g in grad_bodies if any(is_violet(*c) for c in colors_in(g))]
    r[1] = (bool(viol_grad or tw_grad),
            (viol_grad[0][:60] if viol_grad else (tw_grad[0] if tw_grad else "")))

    # Violet must be load-bearing: named as a brand/primary/accent token, or used
    # repeatedly in CSS. One violet swatch in a data array is content, not a palette.
    tw_hits = TW_VIOLET_RE.findall(text)
    named_viol = [m.group(1) for m in re.finditer(
        r"(--[\w-]*(?:primary|accent|brand|main)[\w-]*)\s*:\s*([^;]+)", css, re.I)
        if any(is_violet(*c) for c in colors_in(m.group(2)))]
    css_viol = [m.group(0) for m in HEX_RE.finditer(css)
                if is_violet(*hue_sat(hex_to_rgb(m.group(0))))]
    blue_2563 = "#2563eb" in css.lower()
    hit2 = bool(tw_hits or named_viol or blue_2563 or len(css_viol) >= 3)
    r[2] = (hit2, ("-".join(tw_hits[0]) if tw_hits else
                   (f"{named_viol[0]} token" if named_viol else
                    ("#2563EB" if blue_2563 else
                     (f"{len(css_viol)}x violet in CSS" if len(css_viol) >= 3 else
                      (f"{len(css_viol)}x violet (incidental)" if css_viol else ""))))))

    faces = set()
    for m in FONT_FAMILY_RE.finditer(text):
        for part in m.group(1).split(","):
            f = part.strip().strip("'\"").lower()
            if f and f not in GENERIC_FACES and not f.startswith("var("):
                faces.add(f)
    for m in GOOGLE_FONT_RE.finditer(text):
        for fam in re.findall(r"family=([^&:]+)", m.group(1)):
            faces.add(fam.replace("+", " ").strip().lower())
    real = {f for f in faces if f not in GENERIC_FACES}

    # Reworded 2026-07-26: fire when a default face is the DISPLAY voice, not only
    # when it is the sole identity. Pairing Space Grotesk display with IBM Plex body
    # still reads as stock, and the old subset test could not see that.
    def resolve(val):
        v = re.search(r"var\(\s*(--[\w-]+)", val)
        if v:
            d = re.search(re.escape(v.group(1)) + r"\s*:\s*([^;]+)", css)
            val = d.group(1) if d else val
        for part in val.split(","):
            f = part.strip().strip("'\"").lower()
            if f and f not in GENERIC_FACES and not f.startswith("var("):
                return f
        return ""

    display_face = ""
    for sel, dec in rules:
        if not re.search(r"(^|,|\s)(h1|h2)\b|\b(display|hero-title|headline|masthead|wordmark)\b", sel, re.I):
            continue
        m2 = re.search(r"font-family\s*:\s*([^;]+)", dec, re.I)
        if m2:
            f = resolve(m2.group(1))
            if f:
                display_face = f
                break
    hit3 = display_face in DEFAULT_FACES or (bool(real) and real.issubset(DEFAULT_FACES))
    r[3] = (hit3, (f"display voice = {display_face}" if display_face in DEFAULT_FACES
                   else (", ".join(sorted(real)) or "none declared")))

    metrics = [m.group(0).strip() for m in METRIC_RE.finditer(text)]
    # Fabricated testimonials: a quote attributed to a named person, usually with a
    # role. An editorial pull quote from the page's own prose has no such attribution,
    # so requiring the name+role pairing keeps legitimate pull quotes out.
    testimonials = 0
    for m in re.finditer(r"<blockquote[^>]*>(.*?)</blockquote>(.{0,400})", text, re.S | re.I):
        tail = m.group(2)
        attrib = re.search(r"<(figcaption|cite)[^>]*>(.*?)</\1>", tail, re.S | re.I) or \
            re.search(r"class=\"[^\"]*(author|attribution|byline|customer)[^\"]*\"[^>]*>(.*?)<", tail, re.S | re.I)
        if attrib and re.search(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b", re.sub(r"<[^>]+>", " ", attrib.group(0))):
            testimonials += 1
    ev = "; ".join(dict.fromkeys(metrics))[:60]
    if testimonials >= 2:
        ev = (ev + "; " if ev else "") + f"{testimonials} attributed testimonials"
    r[7] = (bool(metrics or testimonials >= 2), ev)

    # ---- Tier 2
    clip = re.search(r"background-clip\s*:\s*text|\bbg-clip-text\b", text, re.I)
    r[8] = (bool(clip and grad_bodies), "gradient + background-clip:text" if clip and grad_bodies else "")

    blob = re.search(r"filter\s*:\s*blur\(\s*(\d{2,})px|\bblur-(2xl|3xl)\b", text, re.I)
    r[9] = (bool(blob and (grad_bodies or tw_grad)), "large blur + gradient" if blob and (grad_bodies or tw_grad) else "")

    # The rule is "1px gray border on every CARD". Form inputs need a border for
    # affordance, and grid/table cell rules are structure, so neither counts.
    CARDISH = re.compile(r"\b(card|panel|tile|feature|widget|module|box)\b", re.I)
    gray_borders = []
    for sel, dec in rules:
        if not CARDISH.search(sel):
            continue
        for m in re.finditer(r"(?<!-)\bborder\s*:\s*1px\s+solid\s+([^;]+)", dec, re.I):
            cols = colors_in(m.group(1))
            if cols and all(s < 0.25 for (h, s, l) in cols):
                gray_borders.append(sel.strip()[:30])
    # Reported, never auto-failed. "On every card" is a property of the RENDER: one
    # `.panel` rule can paint 17 boxes, so a source-side count cannot see it, and
    # keying on selector names produces false negatives. Scored by hand instead.
    r[10] = (False, f"{len(gray_borders)} card-ish rules w/ 1px gray border (see manual 10)")

    lstrip = []
    for sel, dec in rules:
        for m in re.finditer(r"border-left\s*:\s*(\d+)px\s+solid\s+([^;]+)", dec, re.I):
            if int(m.group(1)) >= 3 and any(s > 0.3 for (h, s, l) in colors_in(m.group(2))):
                lstrip.append(f"{sel.strip()[:24]} {m.group(1)}px")
    r[11] = (bool(lstrip), lstrip[0] if lstrip else "")

    r[12] = ("rounded-2xl shadow-lg p-6" in low, "verbatim string" if "rounded-2xl shadow-lg p-6" in low else "")

    # Blur and sticky must live in the SAME rule, not merely both appear in the file.
    glassy = [sel for sel, dec in rules
              if re.search(r"backdrop-filter\s*:[^;]*blur", dec, re.I)
              and re.search(r"position\s*:\s*(sticky|fixed)", dec, re.I)]
    tw_glassy = re.search(r"class=\"[^\"]*\b(sticky|fixed)\b[^\"]*\bbackdrop-blur", text, re.I)
    r[14] = (bool(glassy or tw_glassy), (glassy[0][:44] if glassy else ("tailwind sticky+backdrop-blur" if tw_glassy else "")))

    anim_bg = re.search(r"@keyframes[^{]*\{[^}]*background-position", text, re.I | re.S)
    # A glow is a large-radius shadow in a saturated hue. Neutral/black shadows at any
    # radius are ordinary elevation, so require real saturation AND real blur.
    glow = []
    for sel, dec in rules:
        for m in re.finditer(r"box-shadow\s*:\s*([^;]+)", dec, re.I):
            val = m.group(1)
            blur = [int(b) for b in re.findall(r"(\d{2,})px", val)]
            alphas = [float(a) for a in re.findall(r"rgba\([^)]*?,\s*([01]?\.?\d+)\s*\)", val)]
            # A tinted low-alpha shadow is ordinary elevation. Neon glow is a bright,
            # highly saturated, substantially opaque halo.
            if alphas and max(alphas) < 0.4:
                continue
            if blur and max(blur) >= 20 and any(s > 0.6 and l > 0.45 for (h, s, l) in colors_in(val)):
                glow.append(f"{sel.strip()[:30]}: {val.strip()[:40]}")
    r[16] = (bool(anim_bg or glow),
             "animated gradient bg" if anim_bg else (glow[0] if glow else ""))

    body_txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
    emo = EMOJI_RE.findall(body_txt)
    # Case-sensitive: the tell is an all-caps LIVE chip, not the word "live" in prose
    # ("live search", "live region") which is ordinary UI vocabulary.
    live = re.search(r">\s*(LIVE|Live)\s*<", text)
    r[17] = (len(emo) >= 3 or bool(live),
             (f"{len(emo)} emoji" if emo else "") + (" + LIVE badge" if live else ""))

    g3 = re.findall(r"grid-template-columns\s*:\s*repeat\(\s*3\b|\bgrid-cols-3\b|"
                    r"grid-template-columns\s*:\s*(?:1fr\s+){2}1fr\b", text, re.I)
    r[19] = (bool(g3), f"{len(g3)} three-column grid rule(s)")

    arrows = re.findall(r"[↑▲⬆]|\btrending[_-]?up\b", text, re.I)
    r[20] = (len(arrows) >= 3, f"{len(arrows)} up-arrow/trend marks")

    # A reveal rule must exist (opacity:0 + translateY in one block), its class must
    # be applied broadly, and an observer must drive it. IntersectionObserver alone is
    # not evidence: it is just as often scroll-spy or lazy-loading.
    reveal_sel = [sel for sel, dec in rules
                  if re.search(r"opacity\s*:\s*0\b", dec)
                  and re.search(r"transform\s*:[^;]*translateY", dec, re.I)]
    n_reveal = 0
    for sel in reveal_sel:
        for cls in re.findall(r"\.([A-Za-z0-9_-]+)", sel):
            n_reveal = max(n_reveal, len(re.findall(r"class=\"[^\"]*\b" + re.escape(cls) + r"\b", text)))
    io = "intersectionobserver" in low
    r[24] = (bool(io and n_reveal >= 5), f"{n_reveal} elements on an observer-driven fade-up" if n_reveal else "")

    bounce = re.search(r":hover[^{]*\{[^}]*(animation[^;}]*bounce|cubic-bezier\([^)]*1\.[5-9])", text, re.I)
    r[25] = (bool(bounce), "bounce easing on hover" if bounce else "")

    # ---- Tier 3
    radii, n_radius_rules = set(), 0
    for sel, dec in rules:
        for m in re.finditer(r"border-radius\s*:\s*([^;]+)", dec, re.I):
            v = m.group(1).strip().lower()
            if v.startswith("var(") or re.search(r"\b(999+|9999)px|\b50%|\bfull\b", v):
                continue  # tokenised, or a deliberate pill/circle
            radii.add(v)
            n_radius_rules += 1
    r[29] = (len(radii) == 1 and n_radius_rules >= 5,
             f"one radius ({next(iter(radii))}) on {n_radius_rules} rules" if len(radii) == 1 and n_radius_rules >= 5
             else f"{len(radii)} distinct non-pill radii")

    # Only the page canvas counts, and only outside @media print.
    pure = []
    for sel, dec in rules:
        if not re.search(r"(^|,)\s*(html|body|:root)\s*(,|$)", sel, re.I):
            continue
        m = re.search(r"background(?:-color)?\s*:\s*(#fff{1,3}\b|#ffffff\b|white\b|#000\b|#000000\b|black\b)", dec, re.I)
        if m:
            pure.append(f"{sel.strip()[:24]} -> {m.group(1)}")
    r[30] = (bool(pure), pure[0] if pure else "")

    hues = [h for (h, s, l) in colors_in(css) if s > 0.2 and 0.1 < l < 0.9]
    buckets = {int(h // 30) for h in hues}
    r[31] = (len(buckets) >= 6, f"{len(buckets)} distinct hue buckets")

    r[33] = (bool(LOREM_RE.search(text)), LOREM_RE.search(text).group(0) if LOREM_RE.search(text) else "")

    # ---- Placard syndrome (new in v0.2 rules)
    # Small tracked all-caps labels used to annotate sections. One or two can be
    # editorial; a page full of them reads as an infographic with captions rather
    # than a website. Calibrated against a hand-checked page (3 eyebrows / 22 labels).
    label_classes = set()
    for sel, dec in rules:
        if re.search(r"text-transform\s*:\s*uppercase", dec, re.I):
            for cls in re.findall(r"\.([A-Za-z0-9_-]+)", sel):
                label_classes.add(cls)
    # Count elements that ARE labels, not every use of an uppercase utility class.
    # An uppercase class on a wrapper whose children are prose or code (API pane
    # headers, section descriptions) is not a placard; only a short leaf label is.
    label_uses = 0
    for cls in label_classes:
        for m in re.finditer(r"<(\w+)[^>]*class=\"[^\"]*\b" + re.escape(cls) +
                             r"\b[^\"]*\"[^>]*>(.*?)</\1>", text, re.S | re.I):
            inner = m.group(2)
            if re.search(r"<(p|div|section|ul|ol|table|pre|h[1-6])\b", inner, re.I):
                continue                      # wrapper, not a label
            txt = re.sub(r"<[^>]+>", " ", inner)
            txt = re.sub(r"&[a-z#0-9]+;", " ", txt).strip()
            if 2 <= len(txt) <= 48 and not re.search(r"[.;{}()/]|\b(GET|POST|PUT|DELETE)\b", txt):
                label_uses += 1
    # eyebrow = one of those labels immediately followed by a heading
    eyebrow = 0
    if label_classes:
        pat = r"class=\"[^\"]*\b(?:" + "|".join(re.escape(c) for c in label_classes) + \
              r")\b[^\"]*\"[^>]*>[^<]{2,48}</\w+>\s*(?:<[^>]+>\s*)?<h[1-4]\b"
        eyebrow = len(re.findall(pat, text, re.I))
    # The v0.2 rule is zero eyebrows above headings and at most one tracked label,
    # so a single confirmed eyebrow is a violation. Label budget kept at 12 rather
    # than 1 because the source-side count still cannot separate every functional
    # label (table headers, axis ticks) from decorative ones; the render is the
    # authority there. Erring loose on labels, strict on eyebrows.
    r[44] = (eyebrow >= 1 or label_uses >= 12,
             f"{eyebrow} eyebrow-above-heading, {label_uses} all-caps label uses")

    # Hero formula: H1, a real explanatory paragraph, then a primary/secondary CTA pair.
    # Guards learned from false positives: install-command tabs (npm/pnpm) and toolbar
    # controls both match a naive "h1 + p + two links" pattern, so require the
    # paragraph to be actual prose and the two CTAs to be a differentiated pair.
    hero, hero_ev = None, ""
    m = re.search(r"<h1\b[^>]*>(.*?)</h1>\s*(?:<[^>]+>\s*)*?<p\b[^>]*>(.*?)</p>\s*"
                  r"(?:<div[^>]*>\s*)?((?:<a\b[^>]*>.*?</a>\s*|<button\b[^>]*>.*?</button>\s*){2})"
                  r"(?!\s*(?:<a\b|<button\b))", text, re.S | re.I)
    if m:
        para = re.sub(r"<[^>]+>", " ", m.group(2))
        para = re.sub(r"&[a-z]+;", " ", para).strip()
        ctas = re.findall(r"<(?:a|button)\b([^>]*)>(.*?)</(?:a|button)>", m.group(3), re.S | re.I)
        cls = [re.search(r"class=\"([^\"]*)\"", a or "") for a, _ in ctas]
        cls = [c.group(1) if c else "" for c in cls]
        labels = [re.sub(r"<[^>]+>", " ", b).strip() for _, b in ctas]
        tabbish = re.compile(r"\b(tab|seg|toggle|chip|filter|preset)\b", re.I)
        pkg = {"npm", "pnpm", "yarn", "bun", "deno", "cdn", "pip"}
        if (len(para) >= 40                                   # real prose, not a hint bar
                and len(cls) == 2 and cls[0] != cls[1]        # differentiated pair
                and not any(tabbish.search(c) for c in cls)   # not a segmented control
                and not any(l.lower() in pkg for l in labels)):
            hero = m
            hero_ev = f"H1 + paragraph + CTA pair ({' / '.join(labels)[:40]})"
    r[45] = (bool(hero), hero_ev)

    # ---- Copy gate / quality floor
    ems = body_txt.count("—")
    r[36] = (ems > 1, f"{ems} em dashes")

    focus = re.search(r":focus-visible", text, re.I)
    r[39] = (not focus, "no :focus-visible rule" if not focus else "focus-visible present")

    r[43] = ("prefers-reduced-motion" not in low, "no prefers-reduced-motion" if "prefers-reduced-motion" not in low else "honored")

    return r


# NOTE: these numbers are stable INTERNAL ids, not slop-test.md line numbers. The
# checklist was renumbered on 2026-07-26 when items were retiered; keeping these fixed
# means the figures already published in RESULTS.md stay valid. Tier labels below track
# the current tiering.
LABELS = {
    1: "T2 purple/indigo gradient (demoted)", 2: "T2 indigo/#2563EB primary (demoted)",
    3: "T1 default face as display voice", 7: "T1 invented metric/social proof",
    8: "T2 gradient text", 9: "T2 gradient blob behind hero",
    10: "T2 1px gray border on cards", 11: "T2 colored left-border strip",
    12: "T2 verbatim rounded-2xl shadow-lg p-6", 14: "T2 glassy sticky nav",
    16: "T2 neon glow / animated gradient", 17: "T2 emoji icons / LIVE dot",
    19: "T2 reflex 3-column grid", 20: "T2 up-arrow stat banner",
    24: "T2 universal fade-up on scroll", 25: "T2 bounce on hover",
    29: "T3 uniform radius everywhere", 30: "T3 pure #fff/#000 background",
    31: "T3 no dominant hue", 33: "T3 lorem ipsum / placeholder art",
    36: "CG em dashes > 1", 39: "QF no visible focus ring",
    43: "QF prefers-reduced-motion ignored",
    44: "T1 placard syndrome (eyebrows/labels)", 45: "T1 hero formula H1+para+2 CTAs",
}
# Items 1 and 2 demoted to Tier 2 on 2026-07-26: zero hits across seven unguided
# baselines, but still occasionally present in deployed AI-builder output.
TIER1 = {3, 7, 44, 45}
MANUAL = {4: "exactly 3 feature cards in a row", 5: "canned skeleton unchanged",
          6: "pill badge over H1", 10: "1px gray border on every card (count in render)",
          13: "cards nested in cards",
          15: "dark mode with no product reason", 18: "giant centered icon above heading",
          21: "gradient 'Most popular' pill", 22: "unmodified wordmark+4links+button nav",
          23: "unmodified 4-col + social footer", 26: "w700 tight-track as only hierarchy",
          27: "serif-italic accent in all-sans page", 28: "all-caps/mono labels everywhere",
          32: "3D blob / fake browser chrome", 34: "check_words.py clean",
          35: "buttons named for what happens", 37: "not-X-but-Y / rule of three",
          38: "squint test", 40: "empty/loading/error designed",
          41: "contrast measured", 42: "checked at 320/375/768"}


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    files = []
    for a in argv:
        p = Path(a)
        files.extend(sorted(p.rglob("*.html")) if p.is_dir() else [p])

    grand = {}
    for f in files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        res = sniff(text)
        hits = [k for k, (v, _) in res.items() if v]
        t1 = [k for k in hits if k in TIER1]
        print(f"\n{'=' * 74}\n{f}\n{'=' * 74}")
        for k in sorted(res):
            v, ev = res[k]
            mark = "HIT " if v else "ok  "
            print(f"  {mark} {k:>2}. {LABELS[k]:<42} {ev}")
        print(f"  -> auto hits: {len(hits)}  (Tier 1: {len(t1)} {sorted(t1)})")
        grand[str(f)] = (len(hits), len(t1), hits)

    print(f"\n{'=' * 74}\nSUMMARY (auto-detectable items only)\n{'=' * 74}")
    for k, (n, t1, hits) in grand.items():
        print(f"  {n:>2} hits / {t1} Tier-1   {k}")
    print(f"\n{len(MANUAL)} further items need eyes on the rendered page:")
    for k in sorted(MANUAL):
        print(f"  {k:>2}. {MANUAL[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
