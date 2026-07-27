# DESIGN.md - token lock

Filled before writing any UI code. After the lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** `wick` 0.7.2, an open source reactive primitives library for JavaScript (signals, computeds, effects). Documentation homepage / overview page.
- **Audience:** working JS developers evaluating the library in the first 60 seconds, plus existing users landing here to look up an API.
- **The page's single job:** let a developer understand what fine-grained reactivity actually does, then find the exact API they need, without leaving this page.
- **Direction:** **Dense utility.** Tool-first, compact spacing, keyboard-visible, zero marketing air. Chosen because a docs homepage is a tool, not a campaign. Explicitly not Editorial print and not Warm organic, both of which sit on or next to the 2026 default.
- **The one deliberate risk:** there is no marketing hero at all. No pitch paragraph, no CTA pair, no feature cards. The top of the page is the H1 (the package name, set in the code face), one spec line, the install command, and then immediately a working build of the library running in front of you. If a reader wants persuasion they have to get it from watching the thing execute.
- **Signature element:** **the live dependency graph.** A real SVG graph of five reactive nodes wired to the actual library implementation shipped in the page. Change a source, watch invalidation propagate node by node, with honest instrumented counters for computed runs and effect runs. Toggling `batch()` visibly changes the effect count. The wordmark's underline lights on each propagation, so the identity mark is wired to the demo.

## Type

Pairing: **IBM Plex Mono + IBM Plex Sans** ("industrial, systems" from the sanctioned list). Chosen because half this page is code, and Plex Mono is the one mono with enough personality to carry the wordmark while still being an honest code face.

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | IBM Plex Mono | 600 | H1 is the package name set in the code face: what you type in the import statement is the logo. Also carries signatures and the wordmark. |
| Body | IBM Plex Sans | 300, 400, 500, 400 italic | Section headings at 500 (never 700-tight). Italic used for real typesetting: terms on first mention, the caveat notes, "no" states. |
| Utility | IBM Plex Mono | 400, 500 | Code, signatures, versions, byte counts, keyboard hints, all numeric data with `tabular-nums`. |

- Scale: base 16px, ratio x1.25 (app): 13 / 16 / 20 / 25 / 31 / 39 / 49
- H1: `clamp(2.4375rem, 5.5vw, 3.0625rem)`, tracking -0.03em. Deliberately not 72px / -1.8px.
- Measure: 68ch body, 100ch for code
- Hierarchy axes in use: face switch (mono vs sans), weight (300 vs 600), size (3x display-to-body), case (sentence case everywhere), color (4 ink steps). Never size alone.
- Mono is never decorative: every mono run is code, an identifier, a byte count, a version, or a keyboard key.

## Color (CSS variables)

Three hues. Dominant is the pale sage paper, neutral is the graphite-teal ink, accent is magenta. Magenta chosen specifically to avoid both flagged defaults: it is not indigo/violet, and it is not the acid-green-on-near-black pair.

```css
:root {
  /* dominant ~60%: pale sage paper */
  --paper:      #ECEEE8;
  --paper-hi:   #F5F6F1;
  --paper-lo:   #E2E5DC;
  --rule:       #CDD2C6;
  --rule-soft:  #DDE1D6;

  /* neutral ~30%: graphite-teal */
  --ink:        #121C20;  /* primary text, and the ground of the dark block */
  --ink-2:      #24343A;
  --ink-3:      #3E5257;
  --ink-4:      #556467;  /* secondary text on paper, 5.28:1 */
  --ink-5:      #8C9895;  /* secondary text on the dark ground, 5.86:1 */

  /* accent ~10%: magenta */
  --accent:     #C1146F;  /* on paper, 5.02:1 */
  --accent-hot: #F03D9B;  /* on ink ground, 4.86:1 */
  --accent-wash:#F7E2ED;  /* tint, row highlight only */

  /* semantic, separate group, error only */
  --error:      #8E1F2B;  /* on paper, 7.55:1 */
}
```

Success confirmations reuse `--accent` rather than adding a green. Warning and info are not needed on this page and are not declared.

Split: paper ~60% / graphite ~30% / magenta ~10%.

## Space, shape, depth

- Base unit: 8px, 4px half-step. No arbitrary values.
- Radius scale (3 values): `0` (rules, table cells, code blocks), `2px` (inputs, chips, buttons), `5px` (the graph panel, the drawer). No `rounded-2xl`. No uniform radius.
- Shadow policy: **none**, with exactly one declared exception. Separation is by whitespace first, then a 3 to 5% background-lightness shift (`--paper` / `--paper-hi` / `--paper-lo`), then hairline rules between peer rows. The single exception is `--shadow-drawer` on the mobile navigation drawer, where the layer genuinely floats over content.
- Borders mark peers only (table rows, API entries, nav items). No box is drawn around a section.

## Motion budget (max 2 moments)

1. **Propagation.** When a source signal is written, each downstream node that actually recomputes flashes the accent and lifts 1px, staged in dependency order; the value chip re-ticks; the wordmark underline lights. 420ms, `transform` and `opacity` only. This is the page's whole argument, animated.
2. **Interaction states.** 140ms on hover / focus / active for nav rows, buttons, inputs, tabs. `transform` and `opacity` only.

Nothing else animates. No scroll-triggered reveals anywhere on the page.

Easing tokens: `--ease: cubic-bezier(0.22, 1, 0.36, 1);` `--fast: 140ms;` `--flash: 420ms;`

`prefers-reduced-motion` path: yes, genuine. Values still update instantly and counters still tick, but flashes become an instantaneous color swap with no transition and no transform, and all state transitions drop to 0ms.

## Macrostructure

**#3, sidebar-anchored.** Persistent left rail carrying identity, a working filter input, and the page's own table of contents with scroll-spy; content scrolls in the main column.

It fits because a docs homepage genuinely is a rail plus a document, and because the rail lets the page be long without ever being lost. It also kills two fingerprints for free: there is no top wordmark-plus-four-links-plus-button navigation bar, and the footer is a docs pager plus one dense meta line rather than a four-column social block.

Section rhythm down the page, so no two neighbours read as the same box:

| Block | Treatment |
|---|---|
| Opening | paper, wide left-aligned, H1 + spec line + install |
| Live graph | full-bleed `--ink` ground, inverted, the only dark block |
| Install / First signal | paper, narrow measure, numbered steps |
| Core API | paper, hairline-separated entries, two-column params grids |
| Patterns | paper, code-dominant, one live async widget |
| What's in the bundle | `--paper-lo` sunk, horizontal stacked bar + data table |
| Interop / Upgrading / Changelog | paper, tables and terse lists |
| Pager + meta | `--ink` strip, single dense line |

## Copy rules for this page

Technical register, present tense, plain verbs. No adjective triplets, no "not just X but Y", no "-ing" tailing clauses, no em dashes. Zero comparative or persuasion metrics: the only numbers on the page are the library's own byte composition (internally consistent, sums to 1.4 kB) and the counters the demo actually measures at runtime. No testimonials, no logo wall, no star count, no user count.
