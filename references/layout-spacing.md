# Layout and spacing

## Spacing

- One base unit, 4 or 8px, and multiples of it. No arbitrary 13px / 37px values.
- Proximity carries meaning: space inside a component < space between components < space between sections. Ambiguous spacing (equal gaps everywhere) is why AI pages feel flat.
- Start with too much whitespace, then remove until it reads. Adding air later never works.

## The macrostructure rule

Never ship the canned skeleton unchanged: hero > three feature cards > logo strip > pricing > FAQ > footer. Pick a structure that fits the content, and if building several pages or several projects, vary the structure between them; structural variety matters as much as visual variety.

Menu of macrostructures (pick one, commit):

1. Split-screen hero: content left, evidence right (real screenshot, real object, live demo), asymmetric widths like 7/5.
2. Editorial single column: one measure, generous margins, inline figures, section breaks by type treatment instead of boxes.
3. Sidebar-anchored: persistent left rail with identity and nav, content scrolls; suits tools and docs.
4. Full-bleed alternating: sections alternate background treatment and alignment, no two consecutive sections identical.
5. Sticky-scroll narrative: one element pins while explanation scrolls past; use once, for the thing that deserves it.
6. Grid of real content: the product's actual output as the layout (photos, entries, data), chrome kept minimal.
7. Off-grid collage: overlapping elements, rotation, depth; for playful or brutalist directions only.
8. Dense utility: toolbar, table or board, detail pane; marketing air removed on purpose.
9. Broadsheet: multi-column, hairline rules, a real measure; only when the content is genuinely editorial. Warning: this macrostructure is where placard syndrome breeds. A real newspaper carries a dateline because it is a dated issue; a landing page carrying `NO. 41` is cosplay. Take the column structure and the rules, leave the kickers, the running heads, the issue numbers and the colophon stamps.
10. One-thing page: a single centered object or claim and one action; restraint as the statement.

## Section and chrome rules

- The hero is a thesis: open with the most characteristic thing in the subject's world (a headline, an image, a live demo, an interaction). Big-number-plus-gradient-accent is the template answer; use only if truly best.
- Never the standard hero block: H1, one explanatory paragraph, then two buttons side by side with one filled and one outline. Count the CTAs before shipping. One is usually right, and the strongest heroes put the action inside the product rather than beside a description of it.
- No pill badge floating above the H1.
- No label above the H1 either. An eyebrow is a pill badge without the pill.
- Sections separate by whitespace, measure, alignment and background shift. Not by captions. A rule with a label at each end is a caption pretending to be structure.
- Vary section treatment down the page so hero, content, and CTA never feel like the same box repeated.
- Nav and footer get the same design attention as the hero. The wordmark + 4 links + button-right nav and the 4-column + social-row footer are the two most recognized AI fingerprints; change layout, density, or behavior in at least one deliberate way.
- 01/02/03 markers only when order carries information the reader needs.
- Asymmetry on purpose: one axis of the layout should break symmetry somewhere visible.

## The squint test

Shrink the rendered page to a thumbnail. You should still see: one clear focal point, distinct section rhythms, and an obvious reading order. If every section collapses into the same centered rectangle, hierarchy failed; fix structure before touching color.

## Responsive floor

Verify at 320, 375, 414, and 768px. Type scales down, measures hold, nothing overlaps, touch targets 44px+.
