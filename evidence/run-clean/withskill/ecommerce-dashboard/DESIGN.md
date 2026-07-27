# DESIGN.md - token lock

Filled before any UI code. After the lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** Analytics console for Thicket Seed Co., a two-person heirloom seed shop that ships from a garage. Sample dataset, 2026-01-27 to 2026-07-25.
- **Audience:** The owner-operator. She opens this between packing orders, on a laptop, and wants to know what to do in the next hour: what to reorder, what to ship, whether the fall-planting bump has started.
- **The page's single job:** Let her pick a window of days and see exactly what happened in it, down to the order row.
- **Direction:** Dense utility. Tool-first, compact spacing, keyboard-visible, zero marketing air. A seed shop's console should feel like a ledger and a packing bench, not a pitch deck.
- **The one deliberate risk:** The primary date control is not a dropdown. It is a **brushable revenue tape** running full-bleed across the top: one bar per day for the whole dataset, drag to select, and every number on the page follows it. Risky because a drag-to-brush control is less discoverable than a select; justified because the seasonality *is* the story for a seed shop, so the shape of the year should be the control, not hidden behind a menu.
- **Signature element:** That tape. Nothing else on the page competes with it for size.

Secondary risk, stated: 13px type in tables. Dense utility calls for it and the quick-picks in typography.md allow 13-14px for data tables. Prose and controls stay at 15-16px, and coarse-pointer devices get 44px rows.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Archivo (variable, `wdth` 62-125) | 700, 800 | Used at **width 112-125%** for the wordmark and the two big numbers only. Hierarchy comes from the width axis, not from weight 700 alone. |
| Body / UI | Archivo (variable) | 350, 400, 500, 600 | Width 100% for controls and prose, **width 86-88%** for table headers and section labels. Italic 400 for annotations. |
| Utility | IBM Plex Mono | 400, 500, 600 + italic 400 | Every number, SKU, order id, date, and delta. Tabular figures throughout. Never used decoratively for headings. |

- Scale: base 16px, ratio x1.25. 10 / 11 / 12 / 13 / 15 / 16 / 19 / 24 / 40px.
- Measure: prose capped at 62ch.
- Width axis replaces the usual weight-700 move: section labels are semi-condensed 88%, display is expanded 118%. Both live in one family, so the page reads as one voice at three widths.

## Color (CSS variables)

```css
:root {
  /* dominant: green-cast ink and paper, one hue family, ~85% of surface */
  --paper:    #F1F2EC;   /* sage-tinted off-white, never #fff */
  --paper-2:  #E8EAE2;   /* panel inset */
  --paper-3:  #DDE0D6;   /* track / deeper inset */
  --ink:      #1B211C;   /* green-black, never #000 */
  --ink-2:    #3D453D;

  /* neutral: warm gray, chrome only */
  --muted:    #5E645A;   /* secondary text */
  --rule:     #C9CDC0;   /* hairline separators */
  --edge:     #868C7F;   /* control borders, measured 3.07:1 */

  /* accent: madder red, ~4% of surface. Attention and focus only. */
  --accent:   #A62B24;
  --accent-tint: #F2DCD9;

  /* semantics, kept out of the brand palette */
  --ok:       #2E6B3E;   /* rising delta, tape bars in window */
  --tape-dim: #6E9370;   /* tape bars outside window */
  --warn:     #8A5A0B;   /* low stock */
  --warn-tint:#F1E4C6;
}
```

Split: dominant (paper + ink, one hue family) ~86%, neutral gray chrome ~10%, madder accent ~4%.

Two decisions worth naming:

1. **Falling numbers are gray, not red.** For a seasonal seed shop, a down week in July is information, not an alarm. Red is reserved for things that need a human today: a stock-out, an order sitting unfulfilled, the focus ring. Most dashboards spend their red on the calendar; this one spends it on the packing bench.
2. **Selection inverts instead of tinting.** A selected row fills with ink and flips its text to paper. No accent wash, no left-border strip.

Measured contrast on `--paper`: ink 14.6:1 - ink-2 8.8:1 - muted 5.4:1 - accent 6.2:1 - ok 5.7:1 - warn 5.3:1 - edge 3.1:1 - tape-dim 3.1:1. Focus ring on inverted rows switches to `--paper` (14.6:1) because madder-on-ink measures 2.3:1 and would fail.

## Space, shape, depth

- Base unit: 8px, 4px half-step. Table row rhythm 28px.
- Radius scale, three values only: `2px` (chips, inputs, bars), `4px` (panels), `9px` (tape handle caps).
- **Shadow policy: none.** Separation is whitespace first, then a 3-5% background-lightness step (`--paper` to `--paper-2`), then a hairline. Nothing on this page floats.

## Motion budget (max 2 moments)

1. **Window change.** When the tape selection commits, dependent panels settle with one 160ms opacity step. Bars recolor with a 120ms fill transition. That is the whole thing.
2. **Detail arrives.** Picking a row brings the detail pane in with a staggered 180ms rise (`translateY(5px)` plus opacity, 45ms apart per block).

   *Changed during the build, and why:* moment 2 was going to be an ink wipe across the selected row. A pseudo-element on a `<tr>` gets wrapped in an anonymous table cell by Chrome, which shifts every real cell one column right, so the wipe cannot be built that way without breaking the table. Row selection is now instant, which is the better answer for a dense tool anyway, and the moment moved to the panel that actually changes.

No scroll-triggered animation anywhere. No hover bounce. Easing token: `--ease: cubic-bezier(0.22, 1, 0.36, 1)`.
`prefers-reduced-motion: reduce` sets all durations to 0 and removes the wipe transform.

## Macrostructure

**#8, Dense utility:** command bar / full-bleed tape / metric rail / three-column shell (nav rail 196px, fluid work area, 336px detail pane) / status bar.

Why it fits: the content is a working ledger, and the operator needs range control, a working surface, and a detail read at the same time without navigating. The asymmetry is deliberate and visible: rail and pane are different widths, and the tape breaks out of the three-column grid to run full-bleed across the top, which is what marks it as the control for everything below.

Below 900px the rail becomes a horizontal tab strip and the pane moves under the work area. Below 640px the tape aggregates from days to weeks, because a 2px bar is not a control.
