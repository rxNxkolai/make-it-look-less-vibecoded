# DESIGN.md - token lock

Locked 2026-07-26, before any markup. No new hues, fonts, radii, shadows or motion moments after this point.

## Brief

- **Subject:** Weir, a B2B payments API. Businesses move money to other businesses over bank rails and cards, and get a double-entry ledger back from the same call.
- **Audience:** the senior backend engineer who will be paged when a payment goes missing, plus the finance lead who has to close the books on what that engineer built.
- **The page's single job:** make that engineer believe they can reconcile to the cent, then hand them a sandbox key.
- **Direction:** Dense utility. Tool-first, compact spacing, tables over prose, keyboard path visible, marketing air removed on purpose.
- **Why this direction:** this buyer reads the API reference before the headline. A payments page that opens with claims instead of data is asking to be closed. Dense utility also walks between the two measured defaults: it is not the 2026 cream/serif/rust chat-model default, and it is not the Tailwind fintech default of blue-600 on white with rounded cards. Fintech was flagged in the skill as untested, so both traps get named and avoided explicitly.
- **The one deliberate risk:** there is no marketing hero. The H1 sits alone with no supporting paragraph, and the only primary action on the page lives inside the product surface, in the console toolbar, not beside a description of it. A landing page with no explanatory paragraph under the H1 is a real risk; it is the right one here because the console immediately below explains more than a paragraph could.
- **Signature element:** a reconciliation ledger whose debit and credit columns actually sum to the same number, with a difference row that reads 0.00. Every figure on the page is arithmetically checkable by the reader. That is the product's whole argument, rendered rather than claimed.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Archivo (variable, wght + wdth) | 250, 400, 600, 700, 800 | H1 at weight 250 and width 108 for a wide engineered look. The extreme low weight against 700 UI chrome carries the hierarchy, not size alone. |
| Body / UI | Archivo | 400, 500, 600 | Same family, normal width. |
| Utility | IBM Plex Mono | 400, 500, 600 | Carries data only: ids, account paths, amounts, JSON, rail names, table column headers. Never decorative. |

- Scale: base 16px, ratio x1.25. 12 / 13 / 14 / 16 / 20 / 25 / 28 / 36-56 (H1 fluid).
- Body measure capped at 68ch. Data tables run wider by design.
- `font-variant-numeric: tabular-nums` on every figure so columns align.
- Explicitly avoided: Inter, Geist, Roboto, Space Grotesk as identity; weight-700-tight-tracking as the only hierarchy move; the 72px / -1.8px Tailwind fingerprint (H1 tops out at 56px with -0.018em).

## Color (CSS variables)

```css
:root {
  /* dominant ~60%: cool slate-green paper */
  --paper:      #EEF0EE;
  --paper-2:    #E4E8E5;   /* section background shift, ~4% lightness */
  --paper-3:    #DADFDB;   /* table head, footer rows, skeletons */
  --rule:       #C6CDC8;   /* hairline, used only for table structure */

  /* neutral ~30%: ink */
  --ink:        #16211E;   /* 14.43:1 on paper */
  --ink-2:      #3D4B46;   /* 8.00:1 */
  --ink-3:      #5A6763;   /* 5.17:1 */

  /* accent ~10%: stamp */
  --stamp:      #0B5D4E;   /* 6.82:1 on paper, 6.82:1 paper-on-stamp */
  --stamp-2:    #0A4A3E;   /* pressed */
  --stamp-tint: #D6E3DE;   /* selected row fill, ink on it 12.41:1 */

  /* semantic, deliberately a separate group from the brand palette */
  --pending:    #8A5A00;   /* 5.18:1 */
  --failed:     #9E2B20;   /* 6.50:1 */

  /* code pane, one dark surface only */
  --pane:       #16211E;
  --pane-ink:   #C8D2CD;   /* 10.67:1 on pane */
  --pane-dim:   #7E8D87;   /* 4.76:1 */
  --pane-key:   #9FB8AF;   /* 7.75:1 */
  --pane-str:   #6FC7AC;   /* 8.22:1 */
  --pane-num:   #D8B26A;   /* 8.28:1 */
}
```

Split: paper family ~60%, ink ~30%, stamp ~10%.

One rule the palette enforces: **settled money gets no colour at all.** In a ledger the normal state is the boring state, so `settled` renders in plain ink and only the exceptions (`pending`, `held`, `failed`, `returned`) spend semantic colour. That also keeps green free to be the brand stamp without colliding with a "success" reading.

Explicitly avoided: indigo, violet, purple-to-blue gradients, `#2563EB`, gradient text, gradient blobs, neon-on-dark, cream `#F4F1EA` + serif + terracotta, near-black + acid green, untinted `#fff` / `#000`.

## Space, shape, depth

- Base unit 8px, half-step 4px. Section padding 56-88px, which is deliberately tighter than a marketing page.
- Radius scale, 3 values: `0` for buttons, panels, table cells and inputs; `2px` for chips and the segmented control; `3px` for the code panes. Square CTAs are the point, 9 of 9 measured AI pages had zero of them.
- Shadow policy: **none.** Separation comes from whitespace, then a 4% background lightness shift, then a 1px hairline used only where it marks real table structure. No section is boxed. Boxes only ever mark one of several peer rows.

## Motion budget (max 2 moments)

1. **Page load, once:** the console's payment rows stagger in on `transform` + `opacity`, 26ms apart, 460ms total, `--ease-out`. Runs one time, never re-triggers on scroll.
2. **Row selection:** picking a payment fills the row and cross-fades the detail pane on `opacity`, 180ms.

Everything else is colour-only state feedback at 140ms, which is state, not animation.

Easing tokens: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);`
`prefers-reduced-motion: reduce` path: yes, genuine. Stagger removed, cross-fade removed, all durations to 0.01ms.

Banned and absent: fade-up-on-scroll, bounce on hover, shimmer skeletons, decorative spinners, infinite ambient motion.

## Macrostructure

Primary structure is **#8 Dense utility** (toolbar, table, detail pane), with the hero borrowing **#1 split-screen** at an asymmetric 5/7 so the console gets the larger share.

Section rhythm down the page, chosen so no two neighbours read alike at thumbnail size:

1. Two-row console chrome. Not wordmark + 4 links + button: row one is identity plus API version plus an environment toggle, row two is a scrolling tab strip with a scroll-spy underline. No CTA in the nav.
2. Hero: H1 alone at 5 columns with a mono index of API resources beneath it, live console at 7 columns. One CTA, inside the console toolbar.
3. Lifecycle: a thin full-width state rail plus a transitions table. 01-06 markers are used because a state machine's order is information the reader needs.
4. Send a payment: two dark code panes side by side with language tabs. Highest value contrast on the page.
5. When it breaks: light, dense failure table plus one real 409 error body. The honest section, and where the designed error state lives.
6. Reconcile: full-bleed ledger on the `--paper-2` shift, widest measure on the page, with the difference row that reads 0.00.
7. Rails: dense reference table of public rail properties.
8. Pricing: a table, not cards. No "most popular" pill.
9. Footer: a reference index of resource paths, not four link columns and a social row.

Designed non-happy states, all reachable: **empty** (filter the console to nothing), **loading** (recompute the ledger balances, static skeleton sized to the real numbers), **error** (the 409 body in section 5).
