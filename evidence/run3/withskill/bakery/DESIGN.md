# DESIGN.md - token lock

Wilder Street Bakehouse landing page. Filled before any UI code. After this lock: no new
hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** Wilder Street Bakehouse, a single-site neighbourhood bakery on a corner.
- **Audience:** people who live or walk within about ten minutes. Not tourists, not
  wholesale buyers. Someone standing in their kitchen at 8:40am deciding whether to put
  shoes on.
- **The page's single job:** get one person to walk over **today**, before the thing they
  want is gone.
- **Direction:** **Playful analog**, executed as a two-ink Risograph shop poster.
  Chunky grotesk display, real saturated ink, rotation, overlap, visible print texture.
  - *Why not Warm organic:* that is the nearest neighbour and it is exactly where the
    2026 default palette lives (cream `#F4F1EA` + serif + terracotta). Same warmth,
    different material story, so the page reads as printed rather than as tasteful.
  - *Why not Dense utility:* SKILL.md flags it as the lazy answer and names a bakery as
    the specific case where it was wrong. A shop has a mood. This one gets to have it.
- **The one deliberate risk:** the palette and the ground. Almost every bakery page is
  pale, beige and daylit. This one is mostly **deep federal blue** with **sunflower**
  ink, because the actual bakery day starts at 3am in the dark and the only warm light
  in the room is the oven. The page opens in that dark, moves onto blush paper stock for
  the open hours, and returns to ink for closing. Loud ink on a food page is the bet.
- **Signature element:** **The Bake Board.** A live shelf, driven by the visitor's own
  clock against the published bake schedule. Every item is proving, in the oven with a
  real countdown, just out and cooling, on the shelf, or gone for today. A printed time
  tape above it can be dragged to scrub the whole day from 5:00 to 16:30, and every row,
  countdown and drawn shelf recomputes as you drag.
  - Describable tomorrow as: *"the bakery page where you drag the time and watch the
    bread sell out."*

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Bricolage Grotesque | 200, 500, 800 | Variable (opsz, wdth, wght). Ink-trapped, slightly wonky, reads printed rather than screen. Not on any ban list. Hierarchy comes from the 200/800 jump, not from 700 everywhere. |
| Body | Newsreader | 300, 400, 600 + italic | Variable serif with real texture and a true italic. Grotesk-display over serif-body inverts the usual arrangement and keeps the page out of the serif-display default zone. |
| Utility | Courier Prime | 400, 700 | Carries data only: clock, countdowns, bake times, prices, ticket stub. Typewriter voice matches the order-slip idiom. Never decorative. |

- Scale: base 17px, ratio x1.333 (editorial). 17 / 22.7 / 30.2 / 40.3 / 53.7 / 71.6 / 95.4.
- All display sizes set with `clamp()` in `rem`, tracking in `em`. The Tailwind fingerprint
  pair (72px with -1.8px tracking) never appears.
- Measure: 62-70ch on body prose.
- Italics used for real reasons (the starter's name, asides), not as a decorative accent word.

## Color (measured, not eyeballed)

Three hues only. Blue is dominant, blush stock is the tinted neutral, sunflower is the
accent. `--crust` is a shade of sunflower, not a fourth hue.

```css
:root {
  --ink:       #16225E; /* federal blue, dominant: type, all line work, 2 grounds */
  --ink-2:     #2E3E86; /* tint: rules, "proving" state, footer type texture */
  --ink-mute:  #454F8F; /* tint: muted text on stock          5.96:1 */
  --ink-soft:  #9AA3D0; /* tint: muted text on ink            5.98:1 */

  --stock:     #F5E0D3; /* blush riso stock, neutral                  */
  --stock-2:   #EBD0BF; /* panel shift, 1.15:1 vs stock (~5% lightness) */

  --sun:       #FFB511; /* sunflower ink, accent              8.33:1 on ink */
  --sun-pale:  #FFD983; /* tint                              10.88:1 on ink */
  --crust:     #BC6C15; /* shade of sun, drawn fills   3.11:1 on stock / 3.72:1 on ink */
}
```

Measured pairs (WCAG, computed not estimated):

| Pair | Ratio | Use |
|---|---|---|
| ink on stock | 11.57:1 | all body text on paper sections |
| stock on ink | 11.57:1 | all body text on dark sections |
| sun on ink | 8.33:1 | accent text, status chips, focus ring on ink |
| ink on sun | 8.33:1 | text on the sunflower section |
| ink-mute on stock | 5.96:1 | secondary text on paper |
| ink-soft on ink | 5.98:1 | secondary text on dark |
| crust on stock / on ink | 3.11 / 3.72:1 | drawn fills only, clears the 3:1 non-text bar on both grounds |

**Hard rule from the measurement:** sunflower on blush stock is **1.39:1**. Sunflower is
never text, never a line, and never a focus ring on a stock ground. It is a ground there,
with ink on top. The focus ring swaps per section: ink on stock, sunflower on ink.

Split across the page: blue family ~60% (both grounds plus every stroke), blush ~30%,
sunflower ~10%.

## Space, shape, depth

- Base unit: 8px, 4px half-step. No arbitrary values.
- Radius scale (3 values): `0` default, `3px` chips and inputs, `999px` on drawn dots only.
  Hard edges are the point; this is a printed poster.
- **Shadow policy: none.** No `box-shadow` anywhere on the page. Depth is carried by the
  print idiom instead: a 3px sunflower **misregistration ghost** behind the display type,
  plus overlap and slight rotation in the collage section. That is the analog answer to
  elevation and it keeps every card out of the soft-shadow default.

## Texture and material (the richness floor, not decoration)

1. Paper grain: inline `feTurbulence` as a data URI, `multiply` on stock, `screen` on ink.
2. Halftone dot field: repeating radial-gradient, used in the oven glow and behind the board.
3. Misregistration: sunflower ghost offset 3px/2px behind the H1 and the footer wordmark only.

Drawn imagery, all inline SVG, all with consistent 2px ink stroke: the oven with its deck
and three loaves, seven bakery goods (boule, seeded rolls, croissant, cardamom bun, rye
tin, focaccia, baguette), the depleting shelf, the day-stage diagram, a flour sack,
a balance, a banneton spiral, and a drawn street map of the corner.

## Motion budget (max 2 moments)

1. **Arrival: the ovens come on.** Once, on load. The drawn oven leads, its glow rises,
   then the board's rows follow in reading order at 60ms stagger, 8px travel.
   520ms total, `--ease-out`. Nothing else on the page animates in.
2. **Consequence: the board ticks.** When the time tape moves or a minute passes, the
   affected row's status chip cross-fades (140ms) and its shelf items redraw. Only the
   rows that actually changed move. Exits run at 0.7x (98ms).

Easing: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);` and
`--ease-snap: cubic-bezier(0.2, 0, 0, 1);` for state flips. Never `linear`, never bare `ease`.
Only `transform` and `opacity` are animated. No scroll-triggered fade-up anywhere.

`prefers-reduced-motion`: genuine no-motion path. The entrance is removed entirely (content
renders in final position), chip changes become instant, the tape stops easing. Layout does
not depend on motion to be legible.

**Progressive enhancement:** every element is visible in CSS by default. The entrance is
opt-in via a `.js` class set by an inline script, so the page never renders blank if
scripting fails. A `<noscript>` path shows the schedule as a plain table.

## Macrostructure

**Off-grid collage** (menu item 7, the one reserved for playful directions), with the bake
board inside it as a **grid of real content** (menu item 6).

Section rhythm, alternating ground so no two consecutive sections read the same:

| # | Section | Ground | Treatment |
|---|---|---|---|
| 1 | Masthead | ink | Not a link rail. Mark, name, and the live open/closed state. Two anchors. A slim solid ink strip pins after the hero carrying the live status. No blur, no glass. |
| 2 | Hero | ink | H1 is the name of the thing, nothing under it. Drawn oven overlapping to the right. One clock-derived status line. **One** CTA, a stamped chip, not a filled/outline pair. |
| 3 | Bake board | stock | The live object. Draggable time tape, seven rows, drawn depleting shelves. Sample-day honesty note stated once, plainly. |
| 4 | How the day runs | ink | An explanatory diagram: overlapping stage bars from 03:00 to 16:30 on the same scale as the tape, so the two rhyme. Teaches why things come out when they do. |
| 5 | Flour, starter, people | stock | Off-grid collage. Overlapping rotated drawings, plain prose, short measure. |
| 6 | Standing order | sun | The one form. Produces a drawn ticket stub. All 8 states real. |
| 7 | Visit | ink | Hours table with today derived from the clock, drawn street map of the corner. |
| 8 | Footer | ink | Single band. Wordmark set enormous as type-as-image. Closing countdown. Not 4-column + social row. |

Asymmetry: the hero splits 7/5 with the oven bleeding past the right margin, the board's
tape is offset left of the row grid, and section 5 sits on a deliberately broken grid.

## Honesty rules for this page

- No founding year, no issue number, no location stamp, no `EST.` anything.
- No invented metrics: no loaf counts sold, no customer numbers, no ratings, no testimonials.
- Every number on screen derives from the clock or the published schedule: current time,
  countdowns, out-at times, usually-gone-by times, opening hours, prices.
- The board's sample-day nature is stated once, plainly, in place. Not as a stamp over the top.
- The reservation form writes to the visitor's own browser and says so. No fake network
  call, and therefore no fake loading bar, per the motion rule that a loading animation
  must reflect real progress or not exist.
