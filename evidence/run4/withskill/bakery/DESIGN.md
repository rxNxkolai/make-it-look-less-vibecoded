# DESIGN.md - token lock

Pennyloaf Bakehouse, 14 Marlowe Street. Locked before any markup. No new hues, fonts,
radii, shadows or motion moments after this point.

## Brief

- Subject: a single-oven neighbourhood bakery. Nine things, one two-deck oven, sold out
  by mid afternoon.
- Audience: people who live within a ten minute walk and want to know whether the thing
  they want is still on the shelf.
- The page's single job: get someone to walk down before the thing they want is gone.
- Direction: **Playful analog**. A bakery's own production board and printed paper bag,
  made into a page. Chunky grotesque display, real colour, offset print blocks, stamps,
  drawn goods, paper grain.
  - Why not the austerity family: this brief is appetite, warmth and craft with a baker
    at the centre of it. Dense utility / Industrial mono / Swiss minimal / Brutalist would
    keep the gate clean and produce a datasheet for bread. Rejected on those grounds.
  - Why not Warm organic as written: cream paper plus a rust accent is the 2026 default
    palette and the brief did not ask for it. Kept the warmth, moved the ground to a real
    butter yellow and the accent to jam berry.
- The one deliberate risk: the ground is a saturated butter yellow across the whole page,
  not an off-white. A page that is genuinely yellow is a commitment that can go wrong.
  Held together by the enamel blue ink and the printed-offset treatment.
- Signature element: **the day rail**. A draggable handle across 04:30 to 16:00 that sets
  the whole page's clock. Drag it and the shelf fills, empties and gets stamped. The oven
  diagram's "now" line moves with it. Every count on the page follows.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Bricolage Grotesque (variable) | 200, 500, 800 | wdth axis pulled to 100 on the big display. 200 against 800 carries the hierarchy, not size alone. Not on the banned display list. |
| Body | Fraunces (variable, SOFT + WONK axes) | 300, 400, 500, 600 | Serif as body under a grotesque display inverts the usual arrangement on purpose. SOFT raised for warmth. |
| Utility | Chivo Mono | 400, 600 | Times, counts, prices, the hours table. Carries data only, never decorative. |

- Scale: base 17px, ratio x1.333 (editorial). 17 / 22.7 / 30.2 / 40.3 / 53.7 / 71.6 / 95.4
- Measure: 62-70ch on body prose.
- Display tracking: -0.02em at large sizes. Never 72px with -1.8px tracking.

## Color

```css
:root {
  /* dominant ~60%: butter, the paper */
  --butter-05: #FCF6E4;
  --butter-10: #F7E9C4;   /* page ground */
  --butter-20: #EFD9A2;
  --butter-30: #E3C77F;

  /* neutral ~30%: enamel blue, the ink */
  --ink:    #17263D;
  --ink-70: #41546F;
  --ink-40: #8A9BB0;      /* hairlines only, never text */
  --deep:   #0F1E36;      /* full-bleed bands */

  /* accent ~10%: jam berry */
  --berry:      #B3125A;
  --berry-soft: #EFB9CF;  /* accent on the deep bands */
  --berry-deep: #7C0B3E;  /* pressed states */

  /* semantic, kept out of the brand three */
  --fresh: #2F6B3F;       /* on the shelf now */
}
```

Split: butter ~60% / ink ~30% / berry ~10%.
Measured contrast on butter-10 ground: ink 14.9:1, ink-70 6.3:1, berry 5.5:1, fresh 5.3:1.
On deep: butter-10 15.7:1, berry-soft 9.9:1.

## Space, shape, depth

- Base unit: 8px, 4px half step. Section rhythm 96 / 128 / 160.
- Radius scale, three values only: `--r-1: 2px` (paper cut edges), `--r-2: 14px` (bag
  corners, cards), `--r-3: 999px` (stamps, dots, the rail handle).
- Shadow policy: **none**. Depth comes from hard offset colour blocks, an ink or berry
  plate sitting 5px behind the element like a misregistered two-plate print, implemented
  as a zero-blur `box-shadow`. No blurred drop shadow anywhere on the page. The one blur
  on the whole page is the berry ink blot spreading under the stamp, which is the
  material response.
- Texture: SVG feTurbulence grain multiplied over the whole page at 0.05, plus a 6px
  halftone dot field on the deep blue bands.

## Motion budget (2 signature moments)

1. **The board sets.** On load: the rail's ink line draws left to right from its own left
   edge (520ms), the now-handle drops in and leads at 260ms, then the shelf items rise
   and fade in reading order on a 55ms stagger. Total about 700ms.
2. **The stamp soaks.** When a scrub pushes an item to zero, a berry SOLD OUT stamp
   presses on: scale 1.3 to 1, rough displaced edge, with a blurred berry ring spreading
   out behind it and fading. This is also the page's **material response**: ink hitting
   paper and spreading, not a rectangle changing colour.

Functional motion is uncapped and required: every link, item, stepper, chip, handle and
button gets hover, focus-visible and active feedback at 120-180ms. Exits run at 0.7x
their enter.

Easing tokens: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);`
`--ease-snap: cubic-bezier(0.2, 0, 0, 1);`
`prefers-reduced-motion`: genuine no-motion path. Arrival skipped entirely, stamp appears
instantly, rail still drags.

## The live object

The page is built around one object, not a picture of one.

- `BAKES`: ten bakes across nine goods, each with a deck, an in time, an out time, a
  cooling time and a quantity. This is the bakery's real day. The baguettes bake twice.
- `demand(m)`: a fixed weighting curve, 1.9x through the 07:30 school run, 1.5x at lunch,
  0.5x after 13:30. No randomness, so the day is identical on every reload.
- Everything else is derived: what is proving, what is in the oven, what is cooling, how
  many are left, when a thing sold out, when it comes back, the header sentence, the
  section heading, the order pad total, the collection time, the starter's rise, the
  progress edge under the header, the now-line on the oven diagram.
- Honest about the model: stated once, plainly, under the shelf. The counts are a model
  of the day's bake sheet, not a till feed.
- Reachable states all designed: before opening (nothing out), first thing out, the rush,
  the restock, sold out, counter closed, and the empty order pad.

## Macrostructure

**Grid of real content** (menu item 6) as the spine: the shelf itself is the layout, in a
six column grid with 4/3/2 span variation so no row repeats, and the order pad as a
sticky paper pad in a narrower right column. Around it, **full-bleed alternating**
(menu item 4): butter, then a deep blue band for the rail and again for the oven decks,
then butter again at a different measure and alignment for the method prose. No two
consecutive sections take the same treatment, and no section is put in a box.

Nav is not wordmark-plus-four-links-plus-button: it is a status strip carrying the live
clock sentence, two links, and a berry progress edge along its bottom that fills with the
proportion of the day's bake already sold.
Footer is one wide band, not four columns with a social row.

The hero carries the H1 alone in a 7-column, with zero buttons. The drawn loaf and its
caption sit in the 5-column beside it, right-aligned. The shop's facts live in the rail
note rather than in an explanatory paragraph under the headline.

## Imagery (rung 2 and rung 3)

- Nine goods drawn as inline SVG, one consistent 3px ink stroke, butter fills, berry
  scoring. Recognisable at 120px.
- The oven deck diagram, generated from `BAKES`, showing how the two decks share slots
  and why the baguettes can only come back at 11:10.
- The starter jar, its level bound to hours since the last feed.
- A drawn plan of the Marlowe Street corner: the door, the bike rack, the bus stop.
- Paper grain and halftone as real texture.
