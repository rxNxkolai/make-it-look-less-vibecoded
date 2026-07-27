#!/usr/bin/env python3
"""Extract each page's type + palette fingerprint straight from the source.

Exists so the convergence question is answered from parsed tokens rather than from
what each agent claimed about its own work. Prints a comparison table.

Usage: python fingerprint.py dirA/ dirB/ ...
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from score import HEX_RE, colors_in, hex_to_rgb, hue_sat, style_text  # noqa: E402

GENERIC = {
    "sans-serif", "serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif",
    "ui-monospace", "-apple-system", "blinkmacsystemfont", "segoe ui", "helvetica",
    "helvetica neue", "arial", "georgia", "cursive", "inherit", "initial", "unset",
    "apple color emoji", "segoe ui emoji", "noto color emoji", "sans", "iowan old style",
    "hoefler text", "times new roman", "times", "courier new", "menlo", "monaco",
    "consolas", "liberation mono", "segoe ui variable", "cambria", "charter",
}


def fonts(text):
    """Families actually requested from Google Fonts, in declaration order."""
    out = []
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?([^\"'>]+)", text):
        for fam in re.findall(r"family=([^&:]+)", m.group(1)):
            f = fam.replace("+", " ").strip()
            if f.lower() not in GENERIC and f not in out:
                out.append(f)
    if not out:  # no CDN: fall back to declared families
        for m in re.finditer(r"font-family\s*:\s*([^;}\n]+)", style_text(text), re.I):
            for part in m.group(1).split(","):
                f = part.strip().strip("'\"")
                if f.lower() not in GENERIC and not f.startswith("var(") and f not in out:
                    out.append(f)
    return out


def page_bg(text):
    """The canvas colour: html/body/:root background, else the lightest token."""
    css = style_text(text)
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        sel, dec = m.group(1).strip(), m.group(2)
        if not re.search(r"(^|,)\s*(html|body)\s*(,|\{|$)", sel, re.I):
            continue
        b = re.search(r"background(?:-color)?\s*:\s*([^;]+)", dec, re.I)
        if b:
            hx = HEX_RE.search(b.group(1))
            if hx:
                return hx.group(0)
            var = re.search(r"var\(\s*(--[\w-]+)", b.group(1))
            if var:
                v = re.search(re.escape(var.group(1)) + r"\s*:\s*([^;]+)", css)
                if v and HEX_RE.search(v.group(1)):
                    return HEX_RE.search(v.group(1)).group(0)
    # Fallback: a token named paper/bg/surface/canvas, else the lightest declared hex.
    for m in re.finditer(r"(--[\w-]*(?:paper|bg|background|surface|canvas)[\w-]*)\s*:\s*([^;]+)", css, re.I):
        hx = HEX_RE.search(m.group(2))
        if hx and hue_sat(hex_to_rgb(hx.group(0)))[2] > 0.75:
            return hx.group(0)
    lights = [m.group(0) for m in HEX_RE.finditer(css) if hue_sat(hex_to_rgb(m.group(0)))[2] > 0.85]
    return lights[0] if lights else "?"


def accent(text):
    """The token named accent/primary/brand, if the page declares one."""
    css = style_text(text)
    for m in re.finditer(r"(--[\w-]*(?:accent|primary|brand)[\w-]*)\s*:\s*([^;]+)", css, re.I):
        hx = HEX_RE.search(m.group(2))
        if hx:
            return f"{hx.group(0)}"
    # Fallback: the most saturated mid-lightness token the page declares, which is
    # what an accent is regardless of what the author called the variable.
    best, best_s = "?", 0.0
    for m in re.finditer(r"--[\w-]+\s*:\s*(#[0-9a-fA-F]{3,6})\b", css):
        h, s, l = hue_sat(hex_to_rgb(m.group(1)))
        if s > best_s and 0.2 < l < 0.75:
            best, best_s = m.group(1), s
    return best if best_s > 0.3 else "?"


def describe(hx):
    if not hx or hx == "?":
        return ""
    h, s, l = hue_sat(hex_to_rgb(hx))
    if s < 0.08:
        return "neutral"
    name = ("red" if h < 15 or h >= 345 else "orange" if h < 45 else "yellow" if h < 70
            else "green" if h < 165 else "teal" if h < 200 else "blue" if h < 250
            else "violet" if h < 290 else "magenta" if h < 345 else "red")
    return f"h{int(h)} {name}"


def main(argv):
    rows = []
    for a in argv:
        p = Path(a)
        for f in (sorted(p.rglob("index.html")) if p.is_dir() else [p]):
            t = f.read_text(encoding="utf-8", errors="ignore")
            bg, ac = page_bg(t), accent(t)
            rows.append((str(f.parent).replace("\\", "/"), fonts(t)[:3], bg, describe(bg), ac, describe(ac)))

    w = max((len(r[0]) for r in rows), default=10)
    print(f"{'page'.ljust(w)}  {'paper':<9} {'':<11} {'accent':<9} {'':<12} fonts")
    print("-" * (w + 60))
    for name, fs, bg, bgd, ac, acd in rows:
        print(f"{name.ljust(w)}  {bg:<9} {bgd:<11} {ac:<9} {acd:<12} {', '.join(fs)}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
