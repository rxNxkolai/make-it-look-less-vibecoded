---
name: unslop
description: Anti-AI-slop design rules for web UI. Use whenever building, styling, restyling, reviewing, or auditing any frontend - landing pages, marketing sites, dashboards, apps, portfolios, or single components - in HTML/CSS/Tailwind/React/Next.js or any web stack. Trigger on "make it look less vibecoded", "less vibecoded", "it looks vibecoded", "make it look good", "design this", "build me a website", "make it not look AI generated", "it looks AI generated", "make it look handmade", or any mention of slop, generic, or template. Replaces default AI output (all-caps eyebrow labels above every heading, the H1-paragraph-two-buttons hero, invented mastheads and metrics, warm-cream-plus-serif-plus-terracotta palettes, indigo gradients, Inter-700, three rounded feature cards, glassmorphism, emoji icons, 240+ overused words) with deliberate, distinctive design. Use it if a page reads like a slide deck or infographic rather than a website.
license: MIT
metadata:
  version: 0.5.0 (2026-07-27)
---

# unslop

LLMs sample the statistical center of their training data. For web UI that center is one page, and it has moved. It is no longer mainly Inter at 700 over an indigo gradient. Measured 2026-07-25, the current center is a *tasteful* page: warm cream paper, a high-contrast serif, a rust accent, a small tracked all-caps label above every section, and a hero of headline plus one paragraph plus two buttons. It looks considered, which is exactly why it is harder to catch. The older tells (indigo gradient, pill badge over the H1, three feature cards, glassy nav) still appear and are still banned, but they are no longer what a current model reaches for unprompted.

Every rule here exists to push output off that center. These are frequency bans, not taste laws: a banned pattern used deliberately, for a stated reason that fits the brief, can pass review. Used by default, it fails.

## Workflow (in order)

**1. Pick a direction before writing any code.** "Clean and modern" is not a direction; that phrase IS the default. Choose one and say it out loud with the audience and the page's single job ("editorial print, for coffee nerds, job: make one blend feel collectible"). Take one deliberate aesthetic risk you can justify.

| Direction | Feels like |
|---|---|
| Editorial print | magazine spreads, serif display, hairline rules, generous measure. Watch for placard syndrome here, but do not avoid the direction: it is expressive and that is worth having |
| Swiss minimal | grid discipline, huge type, one accent, lots of air |
| Brutalist | raw HTML energy, hard edges, system fonts used on purpose |
| Industrial mono | terminal, mono type, data-dense, exposed structure |
| Warm organic | cream papers, soft ink colors, hand-drawn or photographic texture. Cream plus rust alone is the 2026 default palette, so carry this with real texture and drawn imagery and shift the accent off rust |
| Retro-web | early-internet motifs, borders, bitmap or slab type |
| Dense utility | tool-first, compact spacing, keyboard-visible, zero marketing air. CAUTION: 7 of 10 pages built under earlier versions of this skill picked this one, including a bakery. It is the direction where the bans cost nothing, which makes it the lazy answer. Only correct for a genuine tool, an internal surface or a dashboard. Never for a shop, a person, a product launch or anything with a mood |
| Playful analog | stickers, rotation, chunky type, real color |

If the brief already names a look, the brief wins, always.

**Match the direction to the brief's register, not to whichever is easiest to keep
clean.** Four of these are an austerity family: Dense utility, Industrial mono, Swiss
minimal and Brutalist. They share a register, they are where the ban list costs nothing,
and they are therefore the lazy answer. Capping one only moves the problem: measured
2026-07-27, flagging Dense utility pushed two consecutive coffee-shop builds into
Industrial mono instead, arriving at a "roaster's log book" and a "technical datasheet"
with zero images, zero texture and one colour between them.

So the test is the subject, not the row. **If the brief has warmth, appetite, humour,
craft, physical presence or a human at the centre of it, the austerity family is wrong**,
however clean it would keep the gate. A bakery, a coffee roaster, a musician, a bookshop,
a restaurant, a game, a person's own site: none of these are tools. Pick a direction that
can carry the subject and then do the harder work of keeping it off the defaults.

Reserve the austerity family for what it is for: dashboards, settings, developer tools,
internal surfaces, admin. Things where the data genuinely is the content.

**2. Lock tokens in DESIGN.md.** Copy `templates/DESIGN.md` into the project and fill it: 2 typefaces with roles and weights, 3 hues (dominant / neutral / accent) as CSS variables, one spacing unit, a radius scale, a shadow policy, a motion budget of at most 2 moments. After the lock, no new hues, fonts, or radii mid-build. Improvising tokens mid-render is how slop creeps back in.

**3. Build against the core rules below.** Before working in an area, read its reference file (table at the bottom). Do not load all references upfront; load the one you need.

**4. Gate before delivering.** Render the result and look at the screenshot, not the code. Run the squint test (shrink to thumbnail: if every section is the same centered box, hierarchy failed). Then run `references/slop-test.md` top to bottom, including the Richness floor, and `scripts/check_words.py` on all copy. Fix, re-gate, then ship.

## Core rules

**Subtraction is not design. Read this before the bans.** Every rule below removes
something. Removal alone produces a page that breaks no rules and says nothing, and that
failure is just as real as slop, only quieter. Measured 2026-07-27 across six matched
pairs: pages built under the earlier version of this file carried **1 SVG graphic
between them against 114** in the unguided baselines, **7 drawn shapes against 295**, and
**zero** texture effects against 13. The unguided model drew bread for a bakery. The
guided one shipped a table.

So the bans are a floor, not a goal. A page must also *contain* something: drawn or
photographic imagery, a real texture, a colour that commits, a signature element a
person could describe afterwards. If the honest summary of your page is "type, rules and
whitespace", you have not made a restrained design, you have made an empty one. When a
ban removes a device, replace it with a better version of that device rather than with
absence.

**Labels and chrome.** The page must not annotate itself. The banned thing is a specific *treatment*: small, all-caps, letter-spaced, stacked above a heading. Measured on 8 handmade sites (Linear, Panic, Basecamp, Things, Pentagram, The Guardian, The New Yorker, basement.studio) it appears **zero times**. Labeling a section is fine; The Guardian labels all 14 of its blocks. It sets them at 20px, sentence case, zero tracking, as real `<h2>` elements that name a place you can click into. **The label IS the heading.** The tell is saying the same thing twice at two type sizes.

So: if a block has both a kicker and a heading, delete one, and set the survivor at heading size in sentence case with no tracking. Also out: section headers built as label-plus-rule-plus-right-aligned-label, invented masthead metadata (issue numbers, datelines, `EST. 2014`, "written in X since Y"), captions labelling a pull quote, footer meta rows stamping a date range or location. `<hr>` appeared on 0 of 8 handmade sites; it is effectively extinct, so a horizontal rule is almost never the answer. Test: delete every label on the page; if nothing got harder to understand, ship it deleted. This is the most reliable current tell and it is what makes generated pages read as an infographic or a slide deck instead of a website.

**The hero.** Never H1 plus one explanatory paragraph plus two buttons, one filled and one outline. Zero of 8 handmade sites do this. What they do instead, measured: the H1 is either just the name of the thing (Things → "Things", Pentagram → "Pentagram") or one complete sentence that finishes the argument with no supporting paragraph under it (Basecamp, 93 characters, zero nearby paragraphs). **Hero CTA count is 0 or 1, never a filled/outline pair.** Panic and Things ship zero. And the hero shows the thing rather than describing it: Linear argues by displaying product surface, not by stacking claim cards. If a second button is genuinely needed it must not be a mirrored outline twin of the first.

**Build the working thing, not a picture of it.** The strongest single move available. Put the product's core object on the page, live: a clickable year grid, a bake board driven by the real clock, a brushable date range, a working 100-line implementation of the library being documented. Every figure on screen must derive from that object's actual state, because a hardcoded number next to a live grid is an invented metric. Use a fixed seed so the data is stable across reloads, label it as sample data once and plainly, and make sure every reachable state including empty is designed. A screenshot asks to be trusted, a mockup asks to be imagined, a live object just works. Prefer direct manipulation to a control that sets a value: dragging the tape beats a date dropdown. Details: `references/interaction.md`.

**Imagery.** Work down this list and stop at the first the brief supports: the real thing, the real thing drawn in CSS and SVG, a diagram that teaches something, texture, type as the image, nothing. Whitespace is a finished state. Inline SVG is the default medium because it themes with `currentColor`, never 404s, and can be made *of* the data. No emoji as icons, no giant centred icon above a heading, one icon set at text size or none. Cover every image on the page: if it communicates the same without them, they were decoration. Details: `references/imagery.md`.

**Motion.** Two separate budgets, and only the first is capped. **Signature moments: at most 2**, named upfront, spent on the moment of arrival and the moment of consequence. **Functional motion: uncapped and required**: hovers, focus, pressed states, disclosure, tab changes, value updates, loading, validation, drag feedback. These do not count against the budget. Measured 2026-07-27, two pages read the old wording as "animate at most 2 things" and shipped exactly two keyframes with no hover feedback anywhere, which is broken rather than restrained. A signature moment is something the user notices; functional motion is something they would only notice missing. Also give the page one **material response**, a place where something behaves like a real substance: ink soaking, weight when dragged, a needle settling. Choreograph rather than apply effects: stagger 40-80ms in reading order, anchor movement via `transform-origin`, let one element lead, exits at 0.7x the enter duration. Animate `transform` and `opacity`. Prefer scroll-linked scrubbing over scroll-triggered one-shots. Never a universal fade-up, never bounce as a default, never animate the element under the pointer away. `prefers-reduced-motion` gets a genuine no-motion path. Details: `references/motion.md`.

**Copy.** Real content, honest claims, plain verbs. Zero invented metrics, testimonials, or logo walls; a made-up "+47% conversion" is an automatic fail. Buttons say what happens ("Save changes", never "Submit"), and an action keeps its name through the whole flow. Run `scripts/check_words.py`; the full list lives in `references/banned-words.md`. For prose beyond UI copy, the stop-slop and humanizer skills (if installed) take over.

**Cards and containers.** Default to borderless. The rounded bordered card grid is the one universal in AI output: 9 of 9 measured builder pages, up to 33 cards on a single page. The rule that separates handmade from generated is precise: **a border marks one of several like things in a grid, never a container around a section.** 0 of 8 handmade sites boxed a section; all 8 had item-level boxes. If a box holds a section rather than a peer, delete the box. Separate content in this order and stop as soon as it reads: whitespace, then a 3-5% background-lightness shift, then soft elevation. Never a flat 1px gray border on every card, a decorative colored left strip, the verbatim `rounded-2xl shadow-lg p-6` string, or cards nested inside cards.

**Layout.** Never ship the canned skeleton unchanged (hero, three feature cards, logo strip, pricing, FAQ, footer), a pill badge over the H1, or reflex `grid-cols-3`. Pick a macrostructure from `references/layout-spacing.md`, vary section treatment down the page, and use real asymmetry.

**Color.** **Pick a palette architecture first, then fill it.** Prescribing one structure produced 14 pages that were all ink on paper plus an accent: measured 2026-07-27, `--ink` appeared 71 times and `--paper` 44 across the set, and 9 of 14 lock files literally stated "three hues" because this rule used to demand it. Different hex values, identical skeleton. Choose one and say which:

| Architecture | What it is |
|---|---|
| Dominant 60/30/10 | one hue, a tinted neutral, one sharp accent. The old default, still valid, no longer automatic |
| Two-ink | exactly two inks that overprint and mix, riso or screenprint logic, no neutral at all |
| Monochrome plus one | a single hue through its whole value range, one foreign accent that never blends |
| Polychrome | four to six saturated hues held together by equal value, poster or textile logic |
| Achromatic | true greys carrying everything, colour only inside imagery or data |
| Night | a dark ground that is a real hue rather than near-black, lit by two temperatures |
| Analogous earth | neighbouring hues with no accent, separation by value and texture only |
| Clash | two hues that fight on purpose, held apart by area and a hard edge |

Whichever you pick: design in grayscale first so spacing and size carry hierarchy, extend with tints and shades rather than new hues, and measure contrast. Never `bg-indigo-*`, purple-to-blue gradients, `#2563EB` unexamined, gradient text, gradient blobs, pure `#fff`/`#000` untinted. And never warm cream paper with a serif display and a rust accent, the measured 2026 default. Details: `references/color.md`.

**Typography.** **Pick a type architecture, not just two fonts.** "A display face plus a body face" is one option that got treated as the only one. Choose: display-plus-body; a single superfamily worked hard across widths and weights; three roles (display, body, data); type as the image, where one enormous setting carries the page and everything else is small; or a system stack used deliberately. Hierarchy comes from weight contrast (200 against 800 beats 400 against 700) and one modular scale. Italics exist.

**Faces this skill has overused are now defaults too.** Measured across its own output: Archivo 6 times, IBM Plex Mono 5, Bricolage Grotesque 5, Source Serif 4 four, Fraunces 3, Chivo Mono 3. Treat that list exactly like Inter: reaching for one without a reason tied to the brief is the same failure, one generation later. Go and find a face that fits the subject.

Never Inter, Geist, Roboto, Space Grotesk or Plus Jakarta as the display voice even with a characterful body face. Never wrap one word of the H1 in a span and recolour it, the highest-frequency hero tell measured. Avoid 72px at -1.8px tracking, a Tailwind fingerprint. Details: `references/typography.md`.

**Effects.** No glassmorphism by default, no `backdrop-blur-md` sticky nav, no neon glow, no animated gradient backgrounds. Dark mode only when the product calls for it, never as a reflex.

**Icons and imagery.** No emoji as icons. No sparkles or rockets. No single giant centered icon above a heading. No floating 3D blobs or faceless 3D people. No re-drawn fake browser chrome. One consistent icon set at text size, or none at all.

**States and access.** Every interactive element gets 8 states: default, hover, focus-visible, active, disabled, loading, error, success. Visible focus ring at 3:1 contrast minimum. Empty, loading, and error screens are designed, not left over. Contrast is measured, not eyeballed (targets in `references/states-access.md`). Verify at 320, 375, and 768px.

## Reference files

| File | Read when |
|---|---|
| `references/anti-patterns.md` | auditing an existing UI, or unsure whether something is a tell |
| `references/banned-words.md` | writing any UI or marketing copy |
| `references/typography.md` | choosing fonts or setting the type scale |
| `references/color.md` | building the palette |
| `references/layout-spacing.md` | picking page structure, grids, spacing |
| `references/motion.md` | animation: the two moments, choreography, timing, scroll |
| `references/imagery.md` | what to put on the page instead of stock art or 3D blobs |
| `references/interaction.md` | building the live object, direct manipulation, keyboard |
| `references/states-access.md` | the 8 states, empty/loading/error screens, contrast targets |
| `references/slop-test.md` | the final gate, every time, before delivering |

## Versioning note

The tells drift as models retrain. This file is stamped v0.5.0 (2026-07-27); when a new default font or palette becomes the fingerprint, update the reference lists and bump the version rather than treating today's list as permanent truth.

v0.2.0 changed things on evidence, not taste. An A/B test over 12 generated pages found that the Tailwind-era Tier-1 tells (indigo gradient, indigo primary, Inter-as-identity) never fired on an unguided current model, while placard syndrome hit 9 of 12 pages and the standard hero block hit 7 of 12, in both arms. Labels, hero shape and the cream-serif-terracotta palette were promoted to Tier 1 on that basis. Items 1-3 are kept pending a test on enterprise and fintech briefs, which have not been run. Results in `evidence/RESULTS.md`.
