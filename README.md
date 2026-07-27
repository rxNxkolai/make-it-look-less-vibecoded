<img src="assets/wordmark.png" alt="unslop" width="300">

An open-source design skill that stops AI coding tools from producing the default "vibe-coded" look.

It also answers to the sentence you would actually type:

```
make it look less vibecoded
```

Most lists of AI design tells are three years out of date. This one was rebuilt from measurement in July 2026, and the headline finding is that **the default moved**. Across ten unguided baseline pages built by a current top-tier model, the famous tells (indigo gradient, `#2563EB` primary, Inter as the identity) fired **zero times**. What fired instead:

- **Placard syndrome.** Small tracked all-caps labels annotating every section: eyebrows above headings, rule-plus-label section headers, invented datelines. Present on 8 of 9 deployed AI-builder pages measured, and on **0 of 8** handmade sites (Linear, Panic, Basecamp, Things, Pentagram, The Guardian, The New Yorker, basement.studio). It is what makes a generated page read as an infographic instead of a website.
- **The hero formula.** H1, one explanatory paragraph, then exactly two buttons, one filled and one outline. 0 of 8 handmade sites do this.
- **The tasteful palette.** Warm cream paper, a high-contrast serif, a rust accent. It looks considered, which is why it is harder to catch than an indigo gradient.
- **The rounded bordered card grid**, on 9 of 9 AI-builder pages, the only universal in that sample.

A closed version of this idea (sybau.md, claimed at 814k characters, folded into a paid product) made the rounds in July 2026 and was never published. This is the open take, built on citable sources, measured against real output, and sized so models actually follow it.

## Why the slop happens

Models sample the statistical center of their training data. Years of indigo-500 defaults, shadcn examples and identical SaaS templates put that center in one place, and Tailwind's own creator has publicly joked about his role in it. But the center is not fixed: as models retrain on newer, more design-aware data, it drifts toward whatever currently reads as tasteful. That is why this skill is date-stamped and re-measured rather than written once.

Size is the other half. The IFScale benchmark (arXiv:2507.11538) found the best models manage only 68% instruction accuracy at 500 simultaneous instructions, with **a measured bias toward earlier instructions**. So it keeps a short always-loaded core, orders its rules by how often each tell actually fires, and moves the big catalogs into reference files that load on demand.

## It is not only a list of bans

A rule set made entirely of prohibitions produces dead pages, so half of this is about
what to build instead.

**Build the working thing, not a picture of it.** The single strongest move, and it came
out of the measurements rather than out of taste. The generated pages that read least
like generated pages all did the same structural thing: they put the product's core
object on the page, working. A clickable 365-square year grid. A bakery board driven by
the real clock, moving items from "in 6h" to "cooling" to "sold out". A brushable revenue
tape where dragging the window updates every figure below it. A documentation page
shipping a real 100-line implementation of the library, with a dependency graph that
lights up in recompute order.

A screenshot asks to be trusted. A mockup asks to be imagined. A live object just works,
and it is usually less code than faking every state by hand. It also makes invented
metrics impossible: if the number derives from the object, it cannot be a lie.

**Motion, spent deliberately.** Two moments per page, named upfront: the moment of
arrival and the moment of consequence. Choreography over effects, stagger in reading
order, movement anchored to where it came from, exits at 0.7x the enter duration.
Scroll-linked scrubbing rather than scroll-triggered one-shots.

**Imagery, in order of preference.** The real thing, then the real thing drawn in CSS and
SVG, then a diagram that teaches something, then texture, then type as the image, then
nothing. Whitespace is a finished state, not an unfinished one.

## What's inside

```
unslop/
├── SKILL.md                    # core rules + workflow (always loaded when triggered)
├── references/
│   ├── anti-patterns.md        # tiered catalog of the tells, with what was measured
│   ├── interaction.md          # building the live object, direct manipulation, keyboard
│   ├── imagery.md              # what to put on the page instead of stock art
│   ├── motion.md               # the two moments, choreography, timing, scroll
│   ├── typography.md           # pairings, weights, scale
│   ├── color.md                # palette process, tokens, contrast targets
│   ├── layout-spacing.md       # macrostructure menu, spacing, squint test
│   ├── states-access.md        # the 8 states, empty/loading/error, contrast targets
│   ├── banned-words.md         # ~250 words and phrases to avoid in copy
│   └── slop-test.md            # 53-gate binary check run before delivering
├── scripts/
│   └── check_words.py          # deterministic banned-word scanner (CI-friendly)
├── assets/                     # the mark, and the DESIGN.md it was built against
└── templates/
    └── DESIGN.md               # token-lock template copied into each project
```

## Install

Claude Code:

```bash
git clone https://github.com/rxNxkolai/unslop ~/.claude/skills/unslop
```

Cursor / other tools: point your rules at `SKILL.md`, or paste its Core rules section into your project rules file. The reference files work as plain context documents anywhere.

## Use

Build UI as usual; the skill triggers on frontend work. The flow it enforces: pick a direction, lock tokens in DESIGN.md, build against the core rules, then gate with `references/slop-test.md` and:

```bash
python scripts/check_words.py src/
```

## Evidence

Rules earn their place here or leave. Every tier assignment traces to a measurement,
and the full record with per-page numbers is in `evidence/RESULTS.md`.

Twenty pages, one isolated agent each, same prompts and same constraints in both arms:

| Arm | Auto-detected hits | Tier-1 |
|---|---|---|
| baseline, no skill (10 pages) | 34 | 13 |
| with skill, built under v0.1 (3 pages) | 3 | 3 |
| **with skill, built under v0.2 (4 pages)** | **2** | **0** |

The v0.1 to v0.2 change is the useful part, because it shows a rule working. v0.1 pages
passed the gate while covered in all-caps labels, because the checklist had them at
Tier 3. After promoting them to Tier 1, the same measurement on fresh prompts went from
63 labels on a single page to **zero across the entire arm**. All three v0.2 agents
independently cited the same calibration note as their reason for avoiding the default.

Reproduce it: run three vague prompts with and without the skill, score with
`evidence/score.py`, and gate on the rendered screenshot rather than the source.
Disable any other design linter first; a competing one contaminated our first run and
silently fixed this skill's own rules inside the control group.

### Things that did not survive contact with evidence

Published because a rule set that only reports its wins is marketing.

- Indigo gradient and indigo primary, **demoted from Tier 1**: zero hits in ten baselines.
- Rule-plus-label section headers and invented mastheads, **demoted**: 0 of 9 AI-builder
  pages, 0 of 8 handmade sites. They turned out to be artifacts of this skill's own
  "editorial print" direction, not general tells.
- The direction table does not by itself produce diversity. Under v0.1 all three
  with-skill pages independently converged on the same typeface and a red accent.
- The scorer in `evidence/` was corrected eight times during the study, every time
  because a hand-read of the page disagreed with it. Detectors that cannot be measured
  honestly from source are marked as requiring a rendered check instead of guessed at.

## Versioning

The tells drift as models retrain. Lists are date-stamped; when a new default font or palette becomes the fingerprint, edit the reference file, bump the version, and note it in the changelog.

## Credits and sources

- Anthropic's frontend-design skill and frontend-aesthetics cookbook (process and calibration ideas)
- Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup) and berenslab/llm-excess-vocab (word lists)
- Nutlope/hallmark (progressive-disclosure architecture and gate-battery idea)
- Refactoring UI by Adam Wathan and Steve Schoger (spacing, hierarchy, color principles)
- Community writeups on dev.to, Hacker News and design blogs documenting the tells

### Cited research, with what each one actually shows

Every citation below was verified against the source on 2026-07-26. Two of them are
framing rather than evidence, and that distinction is kept explicit on purpose.

`check_words.py` reports three hits in this table ("frontier", "Nexus", "Landscape").
All three sit inside a verbatim quotation, a journal name and a paper title. Justified
and kept, per the skill's own rule that a flagged item may stand with a stated reason.
Altering a citation to satisfy a copy linter would be the worse error.

| Work | What it is | What it actually establishes |
|---|---|---|
| Shin, Gao, Pang, Lee, Reinecke, Tseng, "Interrogating Design Homogenization in Web Vibe Coding" (arXiv:2603.13036, 13 Mar 2026) | **Position/framework paper, cs.HC** | Characterises the vibe-coding lifecycle and proposes "productive friction". **No measurements, no participants, no sample size.** Cite for the argument, never as evidence homogenization was measured. |
| Jaroslawicz, Whiting, Shah, Maamari, "How Many Instructions Can LLMs Follow at Once?" (arXiv:2507.11538, 15 Jul 2025) | Benchmark, 20 models | "Even the best frontier models only achieve 68% accuracy at the max density of 500 instructions." Reports **3 distinct degradation patterns and a bias toward earlier instructions**, so degradation is selective, not uniform. This is why rule order in SKILL.md is load-bearing. |
| Wenger and Kenett, "Large language models are homogeneously creative" (PNAS Nexus 5(3), pgag042, Mar 2026) | **Peer reviewed**, 102 humans vs 22 LLMs | LLM output is measurably less variable than human output on divergent-thinking tasks (AUT 0.459 vs 0.699, effect size 1.8). |
| Anderson, Shah, Kreminski, "Homogenization Effects of Large Language Models on Human Creative Ideation" (ACM C&C 2024, DOI 10.1145/3635636.3656204) | **Peer reviewed**, N=36 | Users produced less semantically distinct ideas with ChatGPT than with an alternative tool. |
| Sourati et al., "The Shrinking Landscape of Linguistic Diversity in the Age of Large Language Models" (arXiv:2502.11266) | Large observational + experimental | Post-ChatGPT variance decline across 318k Reddit stories, 380k news articles, 80k papers. |

**Known gap, stated plainly:** no published study measures visual or structural
convergence across independently generated *websites*. The work above covers ideation,
prose and token diversity. The A/B in `evidence/` was run because that gap exists,
not to replicate someone else's result.

On sybau.md: its contents were never published, and the figures quoted for it
(814,300 characters, 220 banned words, 11 months) are the author's own claims, not
verified facts. Stated here as claims, which is how they should be repeated.

## License

MIT
