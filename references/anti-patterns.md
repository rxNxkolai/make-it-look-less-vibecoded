# Anti-patterns: the catalog of AI-UI tells

Tier 1 = named on every platform surveyed; any single hit fails the slop test.
Tier 2 = widely documented; more than one hit fails.
Tier 3 = concrete, newer, fewer sources; treat as strong smell.

A tier-marked pattern used deliberately, with a written reason tied to the brief, may pass. Used by default, it never does.

## Color and gradients

- [T1] Purple-to-blue / indigo-to-violet gradients anywhere; "vibecode purple" lavender.
- [T1] `bg-indigo-500` / `bg-indigo-600` / `blue-600` (`#2563EB`) as the unexamined primary.
- [T2] Gradient text on hero headings, big numbers, or anything "needing visual interest".
- [T2] Purple or violet gradient orbs / blobs floating behind the hero.
- [T2] Neon-on-dark (cyan/violet) accents with glowing borders.
- [T2] Untouched shadcn gray plus Tailwind blue as the entire palette.
- [T3] Timid, evenly distributed palettes with no dominant hue and no real accent.
- [T3] Pure `#ffffff` / `#000000` backgrounds with no warm or cool tint.

## Cards, borders, containers

- [T1] The rounded bordered card grid as the default container for everything.
  *(9 of 9 AI-builder pages, the only universal in that sample: 32, 4, 6, 33, 10, 13,
  13, 3 and 24 cards per page. Even a plain-text essay page had 10. Meanwhile 0 of 8
  handmade sites boxed their sections, though all 8 had item-level boxes. The rule
  that separates them: **a border marks one of several like things in a grid, never a
  container around a section.** If a box holds a section rather than a peer, delete
  the box.)*
- [T2] Flat 1px gray border on every card.
- [T2] Colored 3-4px left-border strip as decoration (as reliable a tell as em dashes are in text).
- [T2] The verbatim `rounded-2xl shadow-lg p-6` shadcn default card.
- [T3] Cardocalypse: everything boxed, cards inside cards, three container levels deep.
- [T3] One hard box-shadow at 0.1 opacity on everything.
- [T3] Uniform border radius (say, 24px) on every element regardless of size.

## Typography

- [T1] Inter / Roboto / Arial / Open Sans / Lato / Poppins / Space Grotesk / Geist as the sole identity.
- [T3] Weight 700 headlines with tight tracking as the only hierarchy move (the weight is the giveaway, more than the font).
- [T3] Font-size-only hierarchy; no weight or scale strategy.
- [T3] One serif-italic "accent word" dropped into an otherwise all-sans page (Space Grotesk + Instrument Serif is the cliche pairing).
- [T3] Monospace used decoratively for "hacker vibe" rather than to carry data. All-caps section labels moved to Tier 1, see "Chrome, labels, and captions" below.
- [T3] No variable fonts; bold-only emphasis with italics never used.

## Chrome, labels, and captions (placard syndrome)

The single most reliable 2026 tell. The page annotates itself: every section gets a
small tracked all-caps label, every block gets a caption, the header carries a
dateline. It reads as an infographic or a slide deck with placards, not a website.
Real publications and real products do not label their own sections; the reader can
see it is a section.

Evidence level is marked per item, because this section mixes externally corroborated
tells with signals originating in our own testing. Both are real; only some are
independently documented, and the difference should not be blurred.

- [T1] Placard syndrome overall: more than one all-caps tracked micro-label on the
  whole page. Budget is one, and zero is usually right.
  *(THE STRONGEST TELL IN THE WHOLE CATALOG, on three independent bodies of evidence.
  Present on 8 of 9 real AI-builder pages, 106 label instances total, median 8 per
  page. Present on 0 of 8 handmade sites, which is as clean a separation as this
  catalog contains. Named by 3 public slop catalogs. And it is the tell that survives
  taste: the single most design-directed page in the AI sample had stripped every
  pill, gradient, gradient-text and CTA pair, and still shipped 8 tracked caps labels.
  Pills and gradients go first. Labels and rounded cards are what remain.)*
- [T1] An eyebrow / kicker above a heading (`ALSO ON THE DESK`, `ON THE DAY YOU MISS`,
  `THE WHOLE INTERACTION`). If the heading needs a label above it to make sense, fix
  the heading.
  *(CORROBORATED, 3 independent public catalogs: "Repeating tiny uppercase tracked
  labels above headings", impeccable.style/slop; "Eyebrow Chrome", solodesign.cc
  2026-06-06; "All-caps headings and section labels", developersdigest.tech 2026-04)*
- [T2] Section header built as label + long horizontal rule + right-aligned second
  label (`The Desk ------- THIS WEEK'S ESSAY`, `HABIT SHEET ------- 2026 SHEET`).
  *(EDITORIAL-DIRECTION ARTIFACT, not a general tell. Measured 0 of 9 AI-builder
  pages and 0 of 8 handmade sites. It showed up only in our own generated pages,
  i.e. a chat model pushed toward a broadsheet look. Demoted from T1 on that
  evidence. Still banned, because it is what the direction table was producing.)*
- [T2] Fabricated masthead metadata: issue numbers (`NO. 41`), datelines on a page
  that is not an issue, `EST. 2014`, `WRITTEN IN LEITH · MOST THURSDAYS SINCE 2019`.
  Invented provenance, the same failure as invented metrics.
  *(EDITORIAL-DIRECTION ARTIFACT. 0 of 9 AI-builder pages, 0 of 8 handmade sites,
  absent from every public slop catalog. Note the sharpest datapoint: The Guardian
  and The New Yorker genuinely have volume and issue numbers in print and put zero
  of them on the page. Demoted from T1, still banned.)*
- [T2] Credential strips under the dek (`NO ADS, NO TRACKING · SINCE 2019`). *(own)*
- [T2] Captions under pull quotes labelling what the quote is
  (`THE ONE RULE NOTCH IS BUILT ON`). *(own)*
- [T2] Footer meta row: wordmark, link list, and a date range or location stamp
  (`2019-2026 · WRITTEN IN LEITH`). *(own)*
- [T3] Small tracked all-caps used for any non-data label. Column headers in a real
  table and axis labels on a real chart are fine; they carry data, not decoration.

Test: delete every label on the page. If nothing is harder to understand, they were
decoration. Ship it deleted.

## The hero formula

- [T1] H1, then one explanatory paragraph, then exactly two buttons side by side, one
  filled and one outline/ghost. Present on 7 of 12 pages in the v0.1 test, in both arms.
  Alternatives: one action and no second button; the product itself as the hero with
  the action inside it; a live object; navigation instead of CTAs; no hero at all.
  *(PARTIAL corroboration, and worth knowing which half. The surrounding block is
  well documented: oversized centered hero headline, badge above the H1, vague
  aspirational copy, all named by 3 public catalogs. The filled-plus-outline button
  PAIR is not listed as an AI tell anywhere checked; it is documented mainly by
  how-to guides teaching it as the standard recipe, which is arguably worse. Ghost
  secondary buttons are criticised on conversion grounds, not AI grounds.)*
- [T1] **One word or the final phrase of the H1 wrapped in a `<span>` and given an
  accent colour or a gradient.** ("Start building.", "Data-Driven", "3 seconds.")
  *(6 of 9 AI-builder pages, and 6 of 6 of the marketing landing pages among them.
  This is the highest-frequency hero tell measured and it was missing from v0.1
  entirely.)* If one phrase deserves emphasis, carry it with size, weight, position or
  the line break, not by recolouring a word.
- [T2] H1 at 72px with -1.8px letter-spacing. That exact pair is Tailwind
  `text-7xl tracking-tight` and appeared on 4 of 9 pages, the most reproducible
  numeric fingerprint in the sample. Other recurring computed giveaways:
  `border-radius: 3.35544e+07px` (`rounded-full`), `rgb(37,99,235)` (`blue-600`),
  `rgb(17,24,39)` (`gray-900`).
- [T2] Hero paragraph that restates the H1 in longer words.
- [T2] The filled-plus-outline CTA pair anywhere, not only in the hero.
  *(4 of 9 builder pages ran exactly 2 hero CTAs in the filled/outline shape;
  0 of 8 handmade sites did. Handmade hero CTA count is 0 or 1.)*
- [T2] Every CTA with a rounded radius. 9 of 9 builder pages had zero square-cornered
  CTAs. A square button is now genuinely unusual, which makes it available.

## Layout and structure

- [T1] Centered hero with a small pill badge floating directly above the H1.
- [T1] Exactly three feature cards in a row: icon on top, title, two lines of blurb.
- [T1] The canned skeleton shipped unchanged: hero > 3 cards > logo strip > pricing > FAQ > footer.
- [T2] Reflex `grid-cols-3`; bento grid reached for by default.
- [T2] Numbered 1-2-3 "how it works" step rows; horizontal stat banners with little green up-arrows.
- [T2] Hero metric layout: big number, small label, gradient accent line on the left.
- [T2] Standard nav (wordmark + 4-5 inline links + button right) and standard footer (4 link columns + social row + tiny copyright) with zero variation.
- [T3] Fully symmetric layouts; no asymmetry, no intentional negative space.
- [T3] Gradient "Most popular" pill on the middle pricing plan.
- [T3] Sidebar navigation with emoji icons.

## Dark mode and effects

- [T2] Permanent dark mode as the default reflex.
- [T2] Glassmorphism / frosted glass on everything; `backdrop-blur-md` sticky translucent nav.
- [T2] Animated accent-glow or animated gradient backgrounds.

## Imagery and icons

- [T2] Emoji as icons or in UI copy; sparkle and rocket emoji; "green dot LIVE" badges.
- [T2] One huge rounded icon (usually Lucide) centered above a heading.
- [T3] Floating 3D abstract blobs; faceless 3D humans holding glowing orbs; plastic-smooth illustration.
- [T3] Generic stock ("diverse team at a laptop"); placeholder images shipped as final.
- [T3] Re-drawn fake browser chrome, phone frames, or code-window mockups.

## Motion

- [T2] The same fade-in on every element; fade-up-on-scroll as the universal entrance.
- [T2] Bounce on every hover; scattered micro-interactions instead of one orchestrated moment.
- [T3] Hover states that do nothing, or that fade/hide the element being hovered.
- [T3] Buttons that snap with no easing; decorative spinners.

## Copy and content

- [T1] Fabricated metrics and testimonials ("+47% conversion", "trusted by 50,000+ teams", "10x faster").
- [T2] Fake logo bars; lorem ipsum in a deliverable; "Welcome to [Product]" / "Revolutionize your workflow" heroes.
- [T2] Overused AI vocabulary in copy (see banned-words.md).
- [T3] Em dashes in every sentence; "not X, but Y" constructions; rule-of-three adjective triplets.
- [T3] Missing empty / loading / error / focus states; contrast that fails measurement.

## Calibration note: the default has moved (measured 2026-07-25)

The Tailwind-era tells above (indigo gradient, Inter at 700, `#2563EB` primary) did
not appear once across three unguided baseline pages built by a current
top-tier model. Do not assume they are still the default. They may still surface on
enterprise/fintech briefs, which were not tested.

What the unguided model actually produced, on a blog, a habit-tracker landing page
and an analytics dashboard, with no styling guidance at all:

| | Paper | Accent | Display face |
|---|---|---|---|
| blog | `#f5f2ea` | `#a8412a` rust | Fraunces |
| habit tracker | `#F4F1E9` | `#C0451C` ember | Fraunces |
| dashboard | `#F3F1EA` | `#A5801F` gold | Instrument Sans |

Same warm cream within a few hex points, across three unrelated briefs. **Warm cream
plus a high-contrast serif plus a terracotta/rust accent is the 2026 default.** It is
this decade's indigo gradient. It looks tasteful, which is exactly why it is harder to
notice and more important to name.

Two related clusters that also read as defaults: near-black with one acid-green or
vermilion accent, and broadsheet-with-hairline-rules. All are legitimate when the
brief asks for them. Reaching for them unprompted is the same convergence in better
clothes.

Independently corroborated. Two public slop catalogs name the same palette without
reference to this test: "the amber-and-cream wash that signals 'tasteful AI startup'"
(solodesign.cc, 2026-06-06) and "Cream / beige palette" (impeccable.style/slop). A
third source describing AI-generated *slide decks* names "cream backgrounds, italic
serif flourishes, and colored bars next to every text box" (plusai.com), which is the
same three tells this catalog lists for web. That convergence is worth noticing: the
generated-web default has drifted into presentation-deck language.

### There are two different defaults, and which one you get depends on the tool

This matters, because a rule tuned to the wrong population is dead weight.

**Chat-model default** (Claude/GPT-class, asked in prose for a page): warm cream, a
serif display face, a rust accent. Measured on our own baselines, 3 of 3.

**Builder-platform default** (Lovable, Bolt, Replit): the opposite. Measured across 9
real deployed pages, **zero serif typefaces of any kind**, zero cream, zero
terracotta. Instead: near-black on white, Tailwind `blue-600`, magenta, deep navy,
sci-fi cyan. Plus a hard Tailwind numeric fingerprint, an H1 at exactly **72px with
-1.8px letter-spacing** (`text-7xl tracking-tight`) on 4 of 9, and CTA radii that are
never square on 9 of 9.

What both populations share, and therefore what the rules should weight most: tracked
all-caps micro-labels (8/9 builders, all our own pages) and rounded bordered card
grids (9/9 builders). Those two are the real cross-tool constants.

Also recalibrate downward, on measurement: the pill badge above the H1 appeared on
only **2 of 9** builder pages, glassmorphism on **1 of 9**, blockquote testimonial
walls on **1 of 9**, emoji icons in hero copy on **0 of 9**, and full
indigo-to-violet gradient saturation on only **2 of 9**. Several of the loudest tropes
in the public discourse are now the rarest things in the sample.

Practical consequence: if the palette is drifting toward cream paper with a rust
accent and you did not choose that from the brief, you have landed on the default.
Pick again. Cool greys, true neutrals, deep greens, blues and genuinely saturated
grounds are all under-used by comparison.

## Honest counter-argument

Keep these in view; a rule set that cannot state its own weaknesses is marketing.

- **The sameness predates AI.** Component libraries (shadcn, daisyUI) and platform
  guidelines produced convergent UI well before LLM codegen. Attributing all of it to
  models is one causal step too far.
- **Indigo is Tailwind's doing, not the model's.** `bg-indigo-500` was the framework's
  demo default years before codegen, and propagated through tutorials into training
  data. The model learned it; it did not invent it.
- **Boring is sometimes correct.** Predictable pricing cards and familiar layouts have
  real utility value for buyers scanning quickly. Distinctiveness is not free, and
  "generic" is a valid deliberate choice for some briefs.
- **The one published audit of 100 vibe-coded sites (dev.to, 2025-08-06) reported only
  technical defects**, missing OpenGraph tags, missing alt text, heading-level jumps,
  default favicons, stale copyright years. It found zero visual patterns. The
  "vibecoded look" discourse and the "vibecoded audit" discourse are measuring
  different things, and only the former is what this skill addresses.
