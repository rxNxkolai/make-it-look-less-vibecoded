# DESIGN.md, logo mark

Locked 2026-07-27. No new hues, radii or shapes after this point.

## Direction

**Swiss minimal.** Audience: developers scanning a GitHub repo. Job: say "this is
measured, not vibes" in one glance at 16px.

Deliberate risk: the mark is a diagram of the thesis rather than a symbol. A uniform
grid stands for the statistical centre models sample from; one unit has left it. If it
reads as a chart instead of a logo, that is the point.

Explicitly not Editorial print and not Warm organic. Both are flagged in
`references/anti-patterns.md` as sitting on or beside the 2026 default, and a project
about avoiding defaults cannot ship one on its own cover.

## Tokens

| Role | Value | Notes |
|---|---|---|
| Ink, dominant | `#16191B` | cool-tinted near-black, never `#000` |
| Ink on dark | `#E6EAEC` | the light-theme inversion |
| Neutral | `#5C666B` | cool grey, the settled units |
| Accent | `#C4187A` | magenta, the escaped unit, roughly 8% of the mark |

Accent reasoning: magenta is outside every cluster the catalog flags. Not indigo or
violet, not rust or terracotta, not acid-green-on-near-black, not neon cyan. It is also
the hue that appeared least across the 20 measured pages, which is the point of picking
it. Contrast measured below, not eyeballed.

## Geometry

- 4 by 4 grid, 24px units on a 12px gutter, 0 radius. Square corners are deliberate:
  9 of 9 measured AI-builder pages had zero square-cornered CTAs, so hard corners are
  now the unusual choice.
- One unit displaced up and right, clear of the grid, in accent.
- No gradient, no shadow, no glow, no blur, no rounded anything.
- Two colours plus the escaped unit. No third hue.

## Motion budget

Zero. A static mark. Nothing animates.

## Measured contrast

| Tone | vs white | vs GitHub dark `#0d1117` |
|---|---|---|
| grey `#5C666B` | 5.89 | 3.22 |
| magenta `#C4187A` | 5.59 | 3.39 |

## Amendment, recorded per the lock rule

The lock originally called for an ink tone that swapped by `prefers-color-scheme`, plus
separate light and dark files. Measuring killed that: both chosen tones already clear
3:1 against white *and* against GitHub dark, so the swap was solving a problem that did
not exist. Dropped. The mark is now a single file with no theme logic, which is fewer
moving parts and cannot desynchronise.

No hue was added. The `#16191B` ink and `#E6EAEC` inversion in the table above are
retained only as documentation of what was considered and why it was cut.

Semantic bonus that fell out of it: the settled units are muted grey and the escaped
unit is the only saturated thing in the mark. The colour hierarchy now says the same
thing as the geometry.

## Deliverables

- `mark.svg`, transparent, no theme logic, correct on any background
- `favicon.svg`, same geometry reduced to 2 by 2 so it survives 16px
- `mark.png`, transparent raster at 512px for contexts that will not take SVG

---

## Wordmark, added 2026-07-27

`wordmark.svg` and `wordmark.png`: the word set in a 5 by 9 pixel font drawn as
squares, with a block cursor.

Same reasoning as the mark. No typeface is referenced, so it renders identically
in every context and cannot silently fall back to something else. It also keeps the
square unit as the shared element between the two assets: the mark is a grid of them,
the wordmark is letterforms built from them.

| Tone | vs white | vs GitHub dark |
|---|---|---|
| letters `#6E797E` | 4.47 | 4.23 |
| cursor `#C4187A` | 5.59 | 3.39 |

The letter tone was chosen as the balance point where both readings are near-equal,
so one file serves both themes. Third candidate tested of four; the others leaned too
far to one theme.
