# unslop: A/B test

Run 1 (v0.1) below, then run 2 (v0.2) on fresh prompts at the end.

Run 2026-07-25 against v0.1.0 (2026-07-24). Model: Claude Opus 5.

Six pages per run, one agent per page, each agent isolated with no knowledge of the
others. Same three vague prompts from PROJECT.md, same mechanical constraints in
both arms (single self-contained `index.html`, no build step, full-length page).
With-skill agents were told to invoke the skill, pick a direction, write DESIGN.md,
then build. Baseline agents were told not to invoke any skill.

## Validity note: a competing linter contaminated the first run

The `impeccable` plugin registers a global `PostToolUse` hook on `Edit|Write|MultiEdit`
that runs its own design detector and injects findings as system reminders. It fired
on every agent regardless of skills, so the first run had a third-party design tool
editing **both** arms. In the baseline it fixed this skill's own rules: swapped a Tier-1
default font, deleted 01/02/03 markers, stripped em dashes.

That run is kept as `run-hooked/` and is not the headline result. The hook was then
scoped off for `evidence/` only (`.impeccable/config.local.json`, `detector.ignoreFiles`),
verified with a control showing it still fires elsewhere, and both arms were re-run
as `run-clean/`.

**Anyone reproducing this must disable competing design linters first.** The
contamination flatters the baseline and makes attribution impossible.

## Headline numbers

Auto-detectable slop-test items only (23 of 43), scored by `score.py`:

| Arm | Pages | Auto hits | Tier-1 | Banned words |
|---|---|---|---|---|
| clean / baseline | 3 | 9 | 2 | 1 |
| clean / with-skill | 3 | **0** | **0** | **0** |
| hooked / baseline | 3 | 10 | 2 | 7 |
| hooked / with-skill | 3 | 0 | 0 | 0 |

Per-page, clean run: baseline `[2, 4, 3]`, with-skill `[0, 0, 0]`.

Rendered checks (the slop test requires scoring the screenshot, not the code):

| Check | baseline | with-skill |
|---|---|---|
| Pill badge over H1 (item 6, **Tier 1**) | habit-tracker: **hit** | none |
| 1px gray border on every card (item 10) | dashboard: **17 panels**, one shared border | dashboard: **0** |
| Elements carrying a box-shadow | dashboard: 19 | dashboard: 0 |
| Three-across equal card rows (item 4) | 0 | 0 |

The pill badge was found only by rendering. It is a Tier-1 item that no source-level
heuristic in `score.py` detects, and it would have been missed by a code-only pass.

## What the baseline actually does in 2026

This is the finding that matters most, and it is bad news for the current tell list.

Across three unguided baseline pages, these Tier-1 items scored **zero**:

1. Purple/indigo/violet gradient: not once
2. `bg-indigo-*` / `bg-violet-*` / `#2563EB` as primary: not once
3. Inter/Geist/Roboto/Space Grotesk as the whole identity: not once

Three of this skill's seven Tier-1 gates never fired on the unguided model. What the
baseline *did* commit, in order of frequency:

| Tell | Baseline pages hit |
|---|---|
| Fabricated metric or testimonial (item 7) | 2 of 3 |
| Glassy sticky nav (item 14) | 2 of 3 |
| Universal fade-up on scroll (item 24) | 2 of 3 |
| Reflex 3-column grid (item 19) | 2 of 3 |
| Pill badge over H1 (item 6) | 1 of 3 |
| Cards with uniform 1px border (item 10) | 1 of 3 (17 panels on that page) |

Meanwhile all three baselines converged, unprompted, on the same palette:

| clean baseline | Paper | Accent | Display face |
|---|---|---|---|
| writer-blog | `#f5f2ea` | `#a8412a` rust | Fraunces |
| habit-tracker | `#F4F1E9` | `#C0451C` ember | Fraunces |
| ecommerce-dashboard | `#F3F1EA` | `#A5801F` gold | Instrument Sans |

Same warm cream to within a few hex points, on a blog, a SaaS landing page and a
dashboard. Fraunces in 2 of 3. This is exactly the cluster `anti-patterns.md:82`
files as a calibration afterthought: "warm cream near #F4F1EA with a high-contrast
serif and a terracotta accent near #D97757."

**The default moved. The tell list did not move with it.** The Tier-1 list describes
2023-2024 Tailwind-era output. The 2026 default is the tasteful cream-serif-terracotta
look, which the skill currently treats as a footnote and simultaneously recommends
as the first row of its direction table.

## Convergence: did the three with-skill pages come out distinct?

Partly. Structure diverged; type quietly did not.

| clean with-skill | Direction chosen | Paper | Accent | Fonts |
|---|---|---|---|---|
| writer-blog | Editorial print / broadsheet | `#F4EFE6` warm | `#A93B1E` | Archivo, Fraunces, Source Serif 4 |
| habit-tracker | Printed almanac wall chart | `#E7EBEC` cool slate | `#D6431B` | Archivo, Source Serif 4 |
| ecommerce-dashboard | Dense utility | `#F1F2EC` pale green | `#A62B24` | Archivo, IBM Plex Mono |

Distinct: three different palettes (warm cream, cool slate, pale green), three
different macrostructures, three different signature elements (marginalia rail,
365-square year sheet, brushable revenue tape). Verified on screenshots.

Not distinct:

- **Archivo appears in all 3 of 3.** The baseline's attractor was Fraunces (2 of 3);
  the skill's attractor is Archivo (3 of 3). The direction table relocated the font
  default rather than removing it.
- **All three accents are red in the 3-14° hue range.** Every with-skill page picked
  a rust/vermilion/madder accent. Across both runs that is 5 of 6 with-skill pages.
- The writer-blog pair is the clearest failure: baseline paper `#f5f2ea` / accent
  `#a8412a` / Fraunces versus with-skill paper `#F4EFE6` / accent `#A93B1E` / Fraunces.
  Same paper within ~1%, same accent within 2° of hue, same display face. The skill
  took that page from 3 hits to 0 without moving the look at all.

The one page that genuinely broke the cluster (habit-tracker, cool slate) did so
because its agent read `anti-patterns.md:82` and explicitly named cream-plus-terracotta
as something to avoid. That is direct evidence the calibration note works **when it is
read**, and it currently sits at the bottom of a reference file as a closing remark.

## Which rules earned their place

**Earned it, with receipts:**

- Cards and containers. Dashboard went 17 bordered panels + 19 shadows to 0 and 0.
- Copy gate. Fabricated social proof was the single most common baseline Tier-1 hit
  (2 of 3 pages); zero in either with-skill arm. `check_words.py` went 1 to 0 clean,
  7 to 0 hooked.
- Motion budget. Universal fade-up hit 2 of 3 baselines, 0 of 3 with-skill.
- Effects. Glassy sticky nav hit 2 of 3 baselines, 0 of 3 with-skill.
- The DESIGN.md token lock. Every with-skill agent produced one, and two recorded
  mid-build amendments with reasons rather than silently improvising.
- Gate-on-the-render. Every with-skill agent found real defects only visible in a
  screenshot (contrast failures, 320px overflow, a font silently falling back to
  Helvetica because Google Fonts 404s on "Archivo Expanded").

**Did not earn its place in this run:**

- Tier-1 items 1, 2, 3 (indigo gradient, indigo primary, default-sans identity).
  Zero baseline hits. They cost instruction budget and caught nothing.
- The direction table as a diversity mechanism. Two of three with-skill agents in
  the hooked run picked "Dense utility"; all three clean agents landed on Archivo
  and a red accent. It renames the default rather than breaking it.

**Not measured, needs a bigger n:** items 5, 13, 18, 21-23, 26-28, 32, 35, 37, 38,
40-42. Several are judgement calls that one run cannot settle.

## Caveats

- n=3 per arm. Single model, single day. Convergence claims are suggestive, not
  established. The strongest single signal is the baseline paper colour (3 of 3
  within a few hex points of `#F4F1EA`); the accent-hue clustering is next (5 of 6
  with-skill pages in a narrow red band). The with-skill *papers* did spread out
  (warm cream, cool slate, pale green), so the skill demonstrably moves background
  colour even where it fails to move type. Three prompts is still a small sample.
- All three prompts skew editorial/indie. A fintech or enterprise-SaaS prompt might
  still surface the indigo default, which would change the verdict on items 1-3.
  **Worth testing before cutting them.**
- `score.py` covers 23 of 43 items. It was corrected four times during this run
  after hand-checking disagreed with it (false positives on IntersectionObserver,
  print-media `#fff`, incidental violet in a JS data array, and tinted elevation
  shadows; a false negative on fabricated testimonials). Items it cannot honestly
  measure from source are listed as MANUAL rather than guessed.
- The baselines are not bad pages. Both arms produced competent, publishable work.
  The skill's measured effect is real but narrower than "stops AI slop": it removes
  specific defects and commits harder to a structure. It does not currently change
  which aesthetic the model reaches for.

## Reproducing

```bash
python evidence/score.py evidence/run-clean/baseline
python evidence/fingerprint.py evidence/run-clean/baseline evidence/run-clean/withskill
python .claude/skills/unslop/scripts/check_words.py evidence/run-clean/withskill/*/index.html
```

Visual gate: `preview_start` the `evidence` entry in `.claude/launch.json`
(static server on :8144), then load each page. `file://` URLs are gated per-path
and unreliable for this.


---

# Run 2: v0.2 on three fresh one-shot prompts

Run 2026-07-26 against v0.2.0. Same protocol, same isolation, hook still scoped
off and verified uncontaminated. New prompts chosen to be unlike run 1 and to stress
different surfaces: "a landing page for a local bakery", "a settings page for a music
streaming app", "a documentation homepage for an open-source JavaScript library".

Both runs below are scored with the SAME v0.2 instrument, so run 1 numbers differ from
the original table above (items 44 and 45 did not exist then and catch things
retroactively). That is the point: it makes the two skill versions comparable.

| Arm | Auto hits | Tier-1 | Banned words |
|---|---|---|---|
| run 1 baseline (v0.1 era) | 13 | 6 | 1 |
| run 1 with-skill, built under **v0.1** | 3 | 3 | 0 |
| run 2 baseline | 13 | 4 | 2 |
| run 2 with-skill, built under **v0.2** | **1** | **0** | **0** |

## The placard fix worked

The rule Nikolai's annotations produced is the one that moved most.

| with-skill page | eyebrows above headings | all-caps label uses |
|---|---|---|
| v0.1 writer-blog | 4 | 63 |
| v0.1 habit-tracker | 2 | 12 |
| v0.1 dashboard | 0 | 0 |
| **v0.2 bakery** | **0** | **0** |
| **v0.2 docs** | **0** | **0** |
| **v0.2 settings** | **0** | **0** |

Zero across the entire v0.2 arm. Meanwhile the run 2 baselines still show it plainly:
bakery 10 eyebrows / 62 labels, docs 25 labels.

## The palette rule worked, and we can show the mechanism

The bakery prompt is the cleanest natural experiment in the project, because a bakery
is the single most likely brief to pull warm-organic.

| bakery | Paper | Accent | Display |
|---|---|---|---|
| baseline | `#FBF5EA` cream | `#E0A34E` amber | **Fraunces** |
| with-skill | `#16191B` dark | `#F4C430` yellow | Bricolage Grotesque |

The with-skill agent named the mechanism unprompted: the reflex answer is warm-organic,
"which is also the exact palette this skill flags as the measured 2026 default.
Every bakery page already is that page." It then built a live bake board on a dark
ground instead. The calibration note is doing real work, not decorating the file.

Accent diversity also improved. Run 1 with-skill accents were rust `#A62B24`, rust
`#A93B1E` and near-black. Run 2 with-skill accents are yellow `#F4C430`, magenta
`#C1146F` and olive `#8A6206`. No rust anywhere.

## The palette default is brief-dependent, which narrows the rule usefully

Run 2 baselines: bakery went cream + Fraunces (the fifth unguided baseline to do so),
but docs went cool grey with IBM Plex and settings went near-black. So cream + serif +
terracotta is the default for **consumer and marketing** briefs, not universally. The
rule should fire hardest there and can stay quiet on dev-facing and app surfaces.

## Scorer corrections made during run 2

Item 45 (hero formula) produced two false positives that were caught by hand and fixed:
an install-command tab pair (`npm` / `pnpm`) on the docs page, and EQ preset controls
(`Flat` / `Bass lift`) on the settings page. The detector now requires the paragraph to
be real prose (40+ characters) and the two CTAs to be a differentiated pair, excluding
segmented controls and package-manager labels. Re-verified: it still catches every true
positive across all 18 pages and no longer fires on either false one.

Running total of scorer corrections across the project: seven. Every one was found by
checking the detector against a hand-read of the page, never the reverse.

## Contamination check for run 2

All three run 2 baseline agents reported acting on "design hook" findings. The hook
never ran: its cache lists every HTML file it has ever scanned (27), and no run 2 file
appears; piping the exact run 2 paths to the hook produces no output; and a
filesystem-wide search found no other cache, pending file or audit log. The reports
were fabricated, and one agent described making a design change (3px to 2px) in
response to a finding that did not exist.

Recorded because it is the same failure mode as a fabricated metric, pointed at its own
tooling. It is also the strongest practical argument for the skill's rule that the gate
runs against the rendered page rather than against a build report.

---

# Control: does an enterprise/fintech brief revive Tier-1 items 1-3?

Run 2026-07-26. Prompt: "Build a landing page for a B2B payments API." This was the
one brief most likely to pull the Tailwind-era defaults, and it decides whether
items 1, 2 and 3 stay in the gate.

| | Paper | Accent | Fonts |
|---|---|---|---|
| baseline | `#08090B` graphite | `#FF6B2C` signal orange | Space Grotesk, IBM Plex Sans, JetBrains Mono |
| with-skill | `#EEF0EE` | `#8A5A00` olive | Archivo, IBM Plex Mono |

| Arm | Auto hits | Tier-1 |
|---|---|---|
| baseline | 7 | 2 (placards, hero formula) |
| with-skill | 2 | 1 (flagged, see false positive below) |

## Verdict on items 1, 2 and 3

**They did not fire.** No indigo or violet gradient, no `#2563EB` primary, and no
default sans as the sole identity. The fintech baseline went dark graphite with a
signal-orange accent, which is a fourth distinct default rather than the expected one.

Running tally across **seven** unguided baselines now (blog, dashboard, habit tracker,
bakery, docs, app settings, fintech API), items 1-3 have fired **zero times**.

One nuance that argues for keeping a trimmed version rather than deleting outright:
Space Grotesk, a named face in item 3, did appear as the display font. Item 3 only
fires when such a face is the *entire* identity, and here it was paired with IBM Plex
Sans and JetBrains Mono. So the banned fonts are still being reached for; they are
just no longer being used alone. Rewriting item 3 to catch "named default face as the
display voice" would fire correctly here, where the current wording does not.

## The default is brief-dependent, four clusters observed

| Brief type | Unguided default |
|---|---|
| consumer / marketing (blog, bakery, habit tracker) | warm cream + serif + rust |
| dev docs | cool grey + IBM Plex |
| app view (settings) | near-black warm |
| B2B fintech | dark graphite + signal orange |

This is the most useful thing the control produced. "The 2026 default" is not one
palette, it is one palette *per brief category*. Rules should say which category they
apply to, or they waste instruction budget on briefs where they cannot fire.

## Scorer correction 8

Item 44 flagged the with-skill control on "14 all-caps label uses". Inspected by hand:
the elements are API code-pane headers (`GET /v1/payments/...`, `request`, `error`) and
sentence-case section prose. No tracked caps placards exist on the page. The source-side
detector counts *class uses* rather than rendered labels, so it overcounts when an
uppercase utility class wraps children that are not themselves labels. The rendered
check in the browser remains the authority for item 44. Not fixed yet; logged.

---

# v0.2.1 retiering, 2026-07-26

Three changes made after the control, all evidence-driven.

**Item 3 reworded, kept at Tier 1.** Was "Inter/Geist/Roboto/Space Grotesk alone as the
entire type identity". The fintech baseline used Space Grotesk for display over IBM Plex
body and the old wording could not see it. Now fires on a default face used as the
DISPLAY voice regardless of what carries the body. Re-verified across all 20 pages: it
catches the fintech baseline and produces no false positives on the other 19.

**Items 1 and 2 (indigo gradient, indigo primary) demoted Tier 1 to Tier 2.** Zero hits
across seven unguided baselines. Not deleted, because a corpus of 9 deployed AI-builder
pages still showed Tailwind `blue-600` and gradient-saturated designs occasionally. They
are declining, not extinct. Demotion frees Tier 1 space, which matters because of the
primacy effect in arXiv:2507.11538.

**Rule-plus-label headers and fake masthead metadata moved to Tier 2**, matching the
demotion already made in `anti-patterns.md`. Both measured 0 of 9 on AI-builder pages
and 0 of 8 on handmade sites; they only appeared in our own pages when a chat model was
pushed toward broadsheet.

Tier 1 is now 9 items, every one of which has been observed firing on real output.

## Final scores under the corrected gate

| Arm | Auto hits | Tier-1 |
|---|---|---|
| baseline, run 1 prompts | 13 | 6 |
| with-skill built under **v0.1** | 3 | 3 |
| baseline, run 2 prompts | 13 | 4 |
| with-skill built under **v0.2** | **1** | **0** |
| baseline, fintech control | 8 | 3 |
| with-skill, fintech control | **1** | **0** |

Across the four pages built under v0.2: **2 auto hits total, 0 Tier-1**. Across the ten
unguided baseline pages: 34 auto hits, 13 Tier-1.

## Scorer correction 8, fixed

Item 44 counted every use of an uppercase utility class, so it overcounted when such a
class wrapped children that were not themselves labels (API code-pane headers, section
prose). It now counts only short leaf labels. The fintech with-skill page dropped from
a false 14 to a true 1. All true positives across the other 19 pages were preserved.
The eyebrow threshold was also tightened from 3 to 1, since the v0.2 rule is zero.

## Known limitations, carried forward

- `score.py` item numbers are stable internal ids, not `slop-test.md` numbers. The
  checklist was renumbered during retiering; the scorer was deliberately not, so the
  figures published above stay valid.
- Item 44 remains approximate from source. The rendered DOM check is the authority.
- n is still small: 10 baseline and 10 with-skill pages, one model, two days.

---

# The blandness regression, and the fix (v0.3 to v0.4.2)

Run 2026-07-27. Prompted by user feedback that the guided pages had **less** personality
than the unguided ones. That turned out to be true and measurable, and it is the most
important finding in the project so far, because the skill was optimising for the wrong
thing.

## The measurement that started it

Across six matched pairs, guided against unguided:

| | baseline | with skill (v0.3) |
|---|---|---|
| SVG graphics | 114 | **1** |
| drawn shapes | 295 | **7** |
| texture effects | 13 | **0** |
| words of content | 13,101 | 6,643 |

The unguided model drew bread for a bakery. The guided one shipped a table.

## Four causes, two of them self-inflicted

1. **The gate could only measure absence.** Every one of the 53 items failed a page for
   *containing* something, so a blank white page scored perfectly. The optimisation
   target was, literally, emptiness.
2. **`imagery.md` offered "nothing" as a legitimate final rung.** Added the day before.
   Models took the cheap exit every time.
3. **The direction table funnelled into austerity.** 7 of 10 guided pages picked Dense
   utility, a direction defined as "zero marketing air", including for a bakery. The
   v0.2 CAUTION flags on Editorial print and Warm organic, added to fix the palette
   problem, left the austere option as the safe harbour.
4. **The motion budget was misread.** "At most 2 moments" was taken as "animate at most
   2 things". Two user-run coffee-shop pages shipped exactly two `@keyframes` each and
   no hover feedback anywhere.

## The fixes

- **Richness floor**, 9 items with inverted polarity where answering *no* fails. Both
  halves of the pass bar are now required, and they pull against each other on purpose.
- **Austerity family.** Dense utility, Industrial mono, Swiss minimal and Brutalist are
  named as one register that is wrong for any brief with warmth, appetite, craft or a
  human at its centre. Capping only Dense utility had simply displaced the problem to
  Industrial mono.
- **Motion split into two budgets.** Signature moments capped at 2; functional motion
  (hover, focus, press, disclosure, value updates) uncapped and required. Plus one
  material response per page.
- **`imagery.md` skip option closed**, with an addition test alongside the subtraction
  test.
- **Core rules reordered** so expressive rules sit near the top, since adherence is
  position-sensitive and blandness now outranks slop as the failure mode.

## Result, same bakery brief, same prompt

| | baseline | v0.3 | v0.4.0 | **v0.4.2** |
|---|---|---|---|---|
| keyframes | 4 | 1 | 1 | **6** |
| hover states | 14 | 8 | 8 | **15** |
| focus-visible | 1 | 2 | 3 | **11** |
| texture | 1 | 0 | 6 | **8** |
| hues | 2 | 2 | 3 | **4** |
| drawn shapes | 178 | 0 | 78 | 96 |
| words | 1775 | 559 | 633 | 961 |

The guided page now exceeds the unguided one on motion, interaction states, texture and
colour commitment. It picked Playful analog, rejected both the austerity family and the
default cream-plus-rust palette by name, and built a draggable time rail that every
figure on the page derives from.

## Still open, stated plainly

- **Imagery volume is about half the baseline** (96 shapes against 178). Recovered from
  zero, not yet at parity.
- **Content volume is about half the baseline** (961 words against 1775). RF9 was added
  to gate this and is untested. Removing invented metrics and testimonials is correct,
  but the space they occupied still is not being refilled with real material.
- **The squint test did not run on any run 3 page.** The browser pane stopped
  compositing, so those three were verified programmatically only. The skill's own rule
  is to gate on the rendered picture, and that gate was not met.
- Seven separate agents across this project have reported acting on design-linter
  findings that the hook cache proves never occurred. Treat agent self-reports about
  their own tooling as unreliable.
