# DESIGN.md - token lock

Product: **Notch**, a habit tracker.
Filled before any UI code. After this lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** Notch, a habit tracker whose entire interaction is marking one square per day.
- **Audience:** people who have quit three habit apps already. They do not want a coach, a streak flame, or a score. They want a record they can look at.
- **The page's single job:** convince the visitor that the daily action takes two seconds and the sheet it produces is worth keeping.
- **Direction:** printed almanac wall chart. Not a magazine spread and not a broadsheet: the reference object is a year planner taped above a desk, with a rubber stamp next to it. Ruled, square-cornered, ink on cool paper stock, one stamp colour.
- **The one deliberate risk:** the hero is not a pitch or a screenshot. It is the product's core object, a working 365-square year sheet, rendered live in the page and clickable. The marketing page runs the app's actual interaction, and there is no scroll animation anywhere on the page to compensate.
- **Signature element:** the 2026 sheet. Seven rows, fifty-three columns, vermilion stamps on slate paper, keyboard-navigable with arrow keys.

## Type

Two families, three roles. Archivo is variable on the `wdth` axis, so display and utility are the same family at different widths. Hierarchy comes from width and weight and case, not size alone.

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Archivo (variable, `wdth` 125) | 500, 800 | Expanded width for poster lettering. Tracking -0.02em at large sizes. Fallback: Helvetica Neue, Arial. |
| Body | Source Serif 4 (variable, `opsz`) | 300, 400, 600, 400 italic | Real italics for the pull quote and for terms. Fallback: Iowan Old Style, Georgia. |
| Utility | Archivo (variable, `wdth` 100) | 500, 600 | Labels, dates, table headers, numerals. `tabular-nums` everywhere numbers line up. |

- Scale: base 16px, ratio x1.333 (editorial): 16 / 21.3 / 28.4 / 37.9 / 50.5 / 67.3 / 89.7. Display sizes use `clamp()` between two steps.
- Measure: 62-70ch for body prose.
- Rejected on purpose: Inter, Geist, Space Grotesk, Playfair, Instrument Serif.

## Color (hex locked, OKLCH intent noted)

Three hues: cool slate paper (dominant), cold ink (neutral), vermilion (accent). Everything else is a tint or shade of those three.

```css
:root {
  /* dominant ~60% - cool slate paper, oklch(0.93 0.006 220) */
  --paper:       #E7EBEC;
  --paper-lift:  #F2F5F5;   /* raised panel, +3% lightness */
  --paper-band:  #DCE2E3;   /* banded section, -4% lightness */

  /* neutral ~30% - cold ink, oklch(0.27 0.02 235) */
  --ink:         #1B2A33;
  --ink-mid:     #3E525C;   /* secondary text, 6.4:1 on paper */
  --ink-soft:    #7C8E96;   /* hairlines and 3:1 UI parts only, never body */

  /* accent ~10% - stamp vermilion, oklch(0.585 0.20 32) */
  --mark:        #D6431B;   /* marks, rules, large numerals. 3.7:1 on paper */
  --mark-deep:   #A5300F;   /* small accent text and button fill. 5.8:1 on paper */

  /* semantic, kept out of the brand palette */
  --ok:   #1F6B4A;
  --warn: #8A6A00;
  --err:  #B3261E;
  --info: #24606E;
}
```

Split: paper ~60%, ink ~30% (two full-bleed ink bands plus all type), vermilion ~10% (stamps, rules, numerals).

Why this is not the cream-plus-terracotta default the reference warns about: the paper is cool (hue 220, blue-grey), not warm cream #F4F1EA; the ink is a cold navy-slate, not a warm near-black; the accent is a high-chroma printer's vermilion, not muted clay #D97757. The system reads cold paper with one hot stamp, not warm-on-warm.

Measured contrast: ink/paper 12.9:1. ink-mid/paper 6.4:1. mark-deep/paper 5.8:1. mark/paper 3.7:1 (large text and UI parts only). paper/ink-band 12.9:1. paper-lift on mark-deep 7.0:1. Focus ring ink on mark 3.3:1.

## Space, shape, depth

- Base unit: 8px, half-step 4px. Section rhythm 96px desktop / 56px mobile. Nothing inside a component exceeds 32px.
- Radius scale (3 values max): `--r0: 0` (default, everything), `--r1: 1px` (grid cells), `--r2: 3px` (buttons and inputs). Print is square; radius is nearly absent on purpose.
- Shadow policy: **none**. Separation is whitespace first, then a 3-5% paper lightness shift, then a 1px `--ink-soft` hairline rule. No elevation anywhere on the page.

## Motion budget (max 2 moments)

1. **Page load, once:** the year sheet stamps in. Cells go from `scale(0.6)`/`opacity 0` to rest, staggered left to right by column, 420ms plus a capped stagger. Nothing else on the page animates on load, and nothing at all animates on scroll.
2. **The stamp:** clicking any day square scales it 0.82 to 1 and fills it, 150ms. This is the product's primary interaction, so it gets the second budget slot.

Easing: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1)`, `--ease-snap: cubic-bezier(0.34, 1.2, 0.64, 1)` for the stamp only.
`prefers-reduced-motion: reduce`: sheet renders already filled with zero stagger, stamp becomes an instant state change, all transitions drop to 0ms.

## Macrostructure

**Grid of real content** (menu item 6), with full-bleed alternating bands (item 4) for section rhythm.

Why it fits: the product's output is a grid of days, so the grid is the layout rather than an illustration of it. The hero renders the real object at full bleed; every later section is another view of the same grid at a different scale (a week strip, four month sheets). Marketing chrome is kept to the two ink bands.

Section order and treatment, no two adjacent sections alike:

| # | Section | Treatment |
|---|---|---|
| 1 | Masthead | two-line print header, hairline rules, date stamp right, links on the second line. Not sticky, not glassy, no button in the nav. |
| 2 | Hero | headline block left at 60% width, full-bleed year sheet beneath, bleeding past the right margin |
| 3 | Try it | raised `--paper-lift` panel, label column left, 3x7 week strip right |
| 4 | What it does | full-width ledger rows, hairline rules, label column + prose column |
| 5 | The missed day | full-bleed **ink band**, narrow measure, serif italic pull quote |
| 6 | Sample sheets | `--paper-band`, four real month grids, borderless, hairline top rule each |
| 7 | Price | `--paper-band`, two rows, price set huge in expanded Archivo with tabular figures. No cards, no popular badge, no third tier. |
| 8 | Questions | paper, two-column print Q&A with hanging labels, native `<details>` |
| 9 | Start | full-bleed **ink band**, huge wordmark, email form carrying error and success states |
| 10 | Colophon | one run-in paragraph with inline links, no columns, no social row |

Nav and footer variations, stated: the masthead puts the date where a CTA button usually sits and drops the links to a second line under a rule. The footer is a single colophon paragraph naming the typefaces, not a four-column link farm.
