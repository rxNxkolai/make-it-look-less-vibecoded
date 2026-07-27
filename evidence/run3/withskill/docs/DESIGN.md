# DESIGN.md - token lock

Filled 2026-07-27, before any UI code. After the lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** `sinew`, an open source JavaScript library. A reactive core: signals, computed
  values, effects. Documentation homepage.
- **Audience:** working JS developers evaluating whether to adopt it. They have seen twenty
  signals libraries. They want to know what it does differently and how big it is, in that order.
- **The page's single job:** make a developer understand the dependency graph well enough to
  trust it, without leaving the page.
- **Direction:** Industrial mono, in a **drafting-instrument** register. Plotter paper, printed
  grid, engraved hairlines, one signal colour. Not a black terminal, and deliberately not Dense
  Utility: this is a library that has to be *wanted*, not an internal dashboard.
- **The one deliberate risk:** the accent colour is emitted by the runtime. It is physically
  unusable as text (1.07:1 on paper) so it can only ever appear as a highlighter mark, and the
  only thing that paints marks is the library recomputing. A quiet page turns yellow exactly
  when work happens. Second half of the risk: the source listing at the bottom is the source
  executing at the top, evaluated verbatim from the same element.
- **Signature element:** the live dependency graph where **an edge physically unhooks itself**.
  Flip the unit switch and the `celsius -> reading` edge detaches, because the computed stopped
  reading it. Then write to `celsius` and the recompute counter stays at zero.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Martian Mono | 300, 700 (var wght; wdth 87.5) | wordmark, H1, section headings, big figures. Wide engineered mono, reads as instrument panel |
| Body | Public Sans | 400, 600 (var) | prose, table cells, controls. Humanist grotesque, institutional not fashionable |
| Utility | Spline Sans Mono | 400, 600 (var) | code, values, node labels, counters. Carries data only, never decoration |

Fallbacks are real: `ui-monospace, "Cascadia Mono", Consolas, monospace` and
`system-ui, "Segoe UI", sans-serif`. The page must survive with no network.

- Scale: base 16px, ratio x1.25 -> 12.8 / 14 / 16 / 20 / 25 / 31.25 / 39
- Display H1: `clamp(3.25rem, 10.5vw, 6.75rem)`, tracking `-0.045em`. Fluid on purpose so it
  never lands on 72px / -1.8px, which is `text-7xl tracking-tight` and a Tailwind fingerprint.
- Measure: 62-72ch body
- Italics used for terms on first mention, not bold.

## Color (CSS variables)

```css
:root {
  /* dominant ~60% - drafting film, cool green-grey */
  --paper:      #E4E7DE;
  --paper-2:    #EEF0E9;   /* raised panel */
  --paper-3:    #D3D8CB;   /* recessed, grid ground */

  /* neutral ~30% - ink with a green cast, never pure black */
  --ink:        #131A15;
  --ink-2:      #3B463D;
  --ink-3:      #5C665E;   /* 4.77:1 on paper, AA body */
  --ink-4:      #A9B1A9;   /* hairlines and printed grid ONLY, never text, never a
                              meaningful boundary. 1.76:1, decorative by contract */

  /* accent ~10% - the mark. Fill only. 1.07:1 on paper, so it cannot be text */
  --signal:      #E4E62E;
  --signal-deep: #5E6000;  /* 5.33:1 on paper. Strokes and accent text when legibility is needed */

  /* semantic, kept out of the brand palette */
  --alert:      #A82810;   /* 5.64:1 on paper. Thrown errors in the scratch pad, nothing else */
}
```

Measured contrast (WCAG 2.1, computed not eyeballed):
ink/paper 14.15 · ink-2/paper 7.88 · ink-3/paper 4.77 · ink/paper-3 12.18 ·
ink/signal 13.20 · signal-deep/paper 5.33 · alert/paper 5.64 ·
rail text #D8DCD2 on #131A15 12.72 · rail dim #949C92 on rail 6.26 · signal on rail 13.20.

Split: paper family ~60% / ink family ~30% / signal ~10% and only in bursts.

## Space, shape, depth

- Base unit: 8px, 4px half-step. Section rhythm 96px desktop / 56px mobile.
- Radius scale: **0** everywhere, **2px** on inline value chips. Two values, and square
  buttons are the point. (9 of 9 measured builder pages had zero square CTAs.)
- Shadow policy: **none**. Depth comes from material instead:
  1. fractal-noise grain over the whole page at 0.05, multiply
  2. printed 8px / 64px grid inside the graph panel
  3. engraved hairlines: 1px `--ink-4` with a 1px `--paper-2` highlight below

## Motion budget (max 2 moments)

1. **Arrival.** On load the dependency graph builds itself in topological order. `mode` leads at
   0ms, its edges draw by stroke-dashoffset, the computed layer stamps in at +200ms, the join at
   +380ms, the effect last at +520ms. 640ms total, 60ms stagger, nodes scale from 0.86 with a 6px
   rise. Nothing on the page is hidden waiting for script: if JS never runs, the graph is already
   drawn in its initial state.
2. **Consequence.** A write repaints. Every node whose function actually ran gets the highlighter
   swept across it, staggered 60ms apart in true recompute order, then fading over 900ms. The
   rail counter takes the same mark. This is the only place the accent exists.

Everything else is a state flip, not a moment: 140ms in, 100ms out (0.71x).

Easing: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1)` for arrival and panels,
`--ease-flip: cubic-bezier(0.2, 0, 0, 1)` for hover and focus. No `linear`, no bare `ease`.

`prefers-reduced-motion`: genuine no-motion path. The graph is complete at frame one, marks
appear and vanish as instant state changes with a 700ms hold, no sweep, no dash, no travel.

## Macrostructure

**Sidebar-anchored** (menu item 3). A persistent ink rail carries identity, the install line,
scroll-spy nav, and a live runtime readout that counts real recomputes; the paper column scrolls
past it. Chosen because docs are navigated, not read start to finish, and because the 260px /
rest split is the page's asymmetry: nothing on this page is centred.

The rail is not a wordmark-plus-four-links bar. It is dark against paper, vertical, and it does
work: the bottom third is instrumentation reading from the live graph, so the nav has a pulse.

Section rhythm, deliberately varied so no two consecutive blocks are the same box:
hero (paper, type as image) -> graph panel (recessed paper-3, printed grid) -> API table (paper,
hairline rows) -> install strip (thin, paper-2) -> scratch pad (raised paper-2 with a live pane)
-> measured batch panel (narrow, paper) -> source listing (ink slab, gutter numbers) -> footer
(paper, one dense provenance line).

## Honesty rules for this page

Every figure is computed at runtime or it does not ship. Line count and character count are
measured from the source element. Node and edge counts are read from `node.deps`. Recompute
counts come from instrumented user functions, not from estimates. The batch comparison runs both
paths and prints what actually happened. There are no downloads, stars, benchmarks against other
libraries, adopter logos, or bundle-size claims anywhere on the page.
