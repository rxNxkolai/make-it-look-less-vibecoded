# DESIGN.md - token lock

Fill before writing any UI code. After the lock: no new hues, fonts, radii, shadows, or motion mid-build.

## Brief

- **Subject:** Nell Farraday, a writer publishing long reporting about night work. Personal blog homepage.
- **Audience:** Readers who already like long-form nonfiction and arrive from a link, a newsletter, or another writer's blogroll. They are here to read something and to find out whether there is more worth reading.
- **The page's single job:** Get one essay started and make the back catalogue feel like a real body of work, not a feed.
- **Direction:** Editorial print, pushed to **broadsheet** register. Newsprint paper, hairline column rules, kickers and datelines, a drop cap, a corrections notice. The brief did not name a look; the content is genuinely editorial, which is the one condition under which layout-spacing.md permits the broadsheet macrostructure.
- **The one deliberate risk:** A real newspaper grid instead of a page of sections. A 7/5 asymmetric lede with a live vertical column rule between the well and the rail, section heads set *into* the horizontal rules rather than above them, and a marginalia rail where years and note numbers hang outside the text column on a single vertical axis. Risky because it is fragile at small widths, so the rail folds into inline labels below 900px and the column rule is removed rather than squeezed.
- **Signature element:** The marginalia rail plus rules-with-text-set-in. Every section head is a hairline that a word interrupts. Nothing on this page is in a box.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Fraunces (variable, opsz + wght + ital) | 300, 400, 500, 900 | Nameplate at 900, headlines at 400, standfirst and pull quotes at 300 italic. The 300-against-900 spread on one screen is the hierarchy move, not tight-tracked 700. |
| Body | Source Serif 4 (variable, opsz + wght + ital) | 400, 600 + italic | Essay text, rail entries, colophon. Optical sizing on. |
| Utility | Archivo | 500, 600 | Kickers, datelines, folio lines, section tags, index dates. Uppercase, +0.1em tracking, tabular numerals in the index only. |

- Scale: base **17px**, ratio **x1.333** (editorial). 12 / 14 / 17 / 21 / 28 / 38 / 52, nameplate `clamp(46px, 12.5vw, 128px)`.
- Measure: 62-72ch in the well, 34-40ch in the rail.
- Real typographic detail: proper quotes, tabular numerals in the index, hanging drop cap, italics used for titles and voice rather than bold.

## Color (CSS variables)

```css
:root {
  /* dominant ~60%  - warm newsprint */
  --paper:        #F4EFE6;
  --paper-deep:   #EAE3D6;   /* shade, alternating band */
  --paper-lift:   #FBF8F2;   /* tint, the one raised surface */

  /* neutral ~30%   - warm ink, and every rule is this at alpha */
  --ink:          #1C1A17;
  --ink-2:        #5A5248;   /* secondary text        6.70:1 on paper */
  --ink-3:        #6E6659;   /* muted labels          4.94:1 on paper */
  --ink-on-dark:  #B8AE9F;   /* muted on ink          7.84:1 on ink   */
  --rule:         rgba(28, 26, 23, 0.16);
  --rule-strong:  rgba(28, 26, 23, 0.38);
  --rule-dark:    rgba(244, 239, 230, 0.22);

  /* accent ~10%    - printer's vermilion, one hue, two lightnesses */
  --accent:       #A93B1E;   /* on paper              5.50:1 */
  --accent-lift:  #E2724E;   /* on ink                5.52:1 */
}
```

Split: paper ~60% / ink ~30% / vermilion ~10%. No fourth hue. Every rule, divider, and tint is ink or paper at alpha, so the page holds three hues total. Semantic colors are not needed: the only state feedback is on one form, and it reuses `--accent` for error and `--ink` for success, which is the honest editorial reading (a correction is printed in red, a receipt is printed in black).

## Space, shape, depth

- Base unit: **8px**, 4px half-step. Section rhythm 96 / 64 / 32 / 16 / 8.
- Radius scale (2 values): **0** everywhere; **2px** on form controls only. Newsprint has no rounded corners.
- Shadow policy: **none**. Separation is whitespace first, then a 3-5% paper-lightness shift, then a hairline rule. No elevation anywhere on the page.

## Motion budget (max 2 moments)

1. **Nameplate settling on load.** Five elements only (rule, nameplate, standfirst, meta, section strip), staggered 70ms, 620ms, `transform: translateY(14px)` + `opacity`.
2. **Index row marker.** On hover or keyboard focus of an index row, a 3px vermilion bar wipes out from the left margin (`transform: scaleX`, 180ms) and the row background lifts to `--paper-lift`. Nothing moves, nothing fades away.

Form states change color and text only. No scroll-triggered animation of any kind.

Easing tokens: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);` `--ease-quick: cubic-bezier(0.4, 0, 0.2, 1);`
`prefers-reduced-motion` path: yes, real no-motion path (elements start at final position, marker appears without transition).

## Macrostructure

**Broadsheet** (menu item 9). Fits because the content genuinely is editorial: one lede essay, a rail of shorter items, an archive that wants to be an index, and a colophon. Section order deliberately breaks the canned skeleton:

1. **Nameplate** - folio bar, name at 900, standfirst at 300 italic, section strip set on a rule (not wordmark + 4 links + button).
2. **The Desk** - 7/5 asymmetric lede: drop cap essay in the well, a live vertical column rule, a rail carrying two short notes and a correction.
3. **The Index** - full-width ruled archive. Years hang in the left margin; rows are date / title / section / length with tabular figures. No cards.
4. **The Notebook** - full-bleed ink band, two-column text flow, small type. Inverts the page so no two consecutive sections read the same.
5. **Colophon** - a real colophon as a `<dl>`, two columns, including what the page is set in.
6. **The Post** - one form, asymmetric, all eight states designed.
7. **Imprint** - single ruled line plus a printer's bar. Not a four-column link farm.
