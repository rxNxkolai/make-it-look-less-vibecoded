# Slop test (final gate)

Run against the RENDERED page (screenshot), then the code, then the copy. Every item is yes/no.

**Pass bar, both halves required.** Zero Tier-1 hits and at most 2 total hits, with any
kept hit carrying a one-line written justification tied to the brief. AND every Richness
floor item answered yes. The two halves pull against each other on purpose: the tiers
stop a page being generic, the richness floor stops it being empty. Passing only the
tiers is how you ship a correct, dead page.

## Tier 1 (any hit = fail)

1. Inter/Geist/Roboto/Space Grotesk/Plus Jakarta as the DISPLAY voice, whether or not
   another face carries the body? (reworded 2026-07-26: the old "alone as the entire
   identity" wording missed a fintech baseline that used Space Grotesk for display
   over IBM Plex body, which is the pattern that actually reads as generic)
2. Exactly three feature cards in a row (icon, title, blurb)?
3. Canned skeleton shipped unchanged (hero > cards > logos > pricing > FAQ > footer)?
4. Pill badge floating above the H1?
5. Any invented metric, testimonial, user count, or logo wall?
6. More than ONE small tracked all-caps label on the whole page? (count them)
7. Any eyebrow/kicker label sitting above a heading?
8. Hero = H1 + one paragraph + exactly two buttons (one filled, one outline)?
9. Warm cream paper + serif display + rust/terracotta accent, arrived at without the
   brief asking for it? (the 2026 default, see `anti-patterns.md` calibration note)

## Tier 2 (more than one hit = fail)

Also demoted 2026-07-26, for consistency with `anti-patterns.md`: both measured
0 of 9 on deployed AI-builder pages and 0 of 8 on handmade sites. They appeared
only in our own generated pages when a chat model was pushed toward broadsheet,
so they are editorial-direction artifacts rather than general tells.

10. Any section header built as label + rule + right-aligned second label?
11. Any invented masthead metadata: issue number, dateline, `EST. 2014`, location or
   frequency stamp, on something that is not a real dated issue?

Demoted from Tier 1 on 2026-07-26. Across seven unguided baselines (blog,
dashboard, habit tracker, bakery, docs, app settings, B2B fintech) neither fired
even once. They are kept because a corpus of 9 deployed AI-builder pages still
showed Tailwind blue-600 and gradient-saturated designs occasionally, so the
patterns are declining rather than extinct. They no longer occupy Tier 1, where
the primacy effect (arXiv:2507.11538) makes position expensive.

12. Purple/indigo/violet gradient anywhere?
13. `bg-indigo-*`, `bg-violet-*`, or `#2563EB` as primary?

14. Gradient text on any heading or number?
15. Gradient blob/orb behind the hero?
16. Flat 1px gray border on every card?
17. Colored left-border strip as decoration?
18. Verbatim `rounded-2xl shadow-lg p-6` anywhere?
19. Cards nested inside cards?
20. `backdrop-blur-md` (or any glassy) sticky nav?
21. Dark mode with no product reason?
22. Neon glow or animated gradient background?
23. Emoji as icons, sparkles, rockets, or a "LIVE" dot badge?
24. Giant centered icon above a heading?
25. Reflex `grid-cols-3` or default bento grid?
26. Stat banner with green up-arrows / numbered 1-2-3 step row with no real sequence?
27. Gradient "Most popular" pricing pill?
28. Wordmark + 4 links + button-right nav, unmodified?
29. Four-column + social-row footer, unmodified?
30. Fade-up-on-scroll on everything / identical fade-in on every element?
31. Bounce on hover anywhere?

32. More than two motion moments on the page, or the same transition applied to everything?
33. Exit animations the same duration as their enter (should be about 0.7x)?
34. Any image, icon or graphic that could be removed with no loss of meaning?
35. A number, streak or total on screen that does not derive from the live object's real state?

## Tier 3 (smells; fix unless justified)

36. Weight-700 tight-tracked headline as the only hierarchy?
37. Serif-italic accent word in an all-sans page?
38. Decorative monospace (mono not carrying data)? All-caps labels are Tier 1, item 8.
39. Uniform radius on every element?
40. Pure #fff or #000 background, untinted?
41. Palette with no dominant hue?
42. Any 3D blob, faceless 3D person, or fake browser chrome?
43. Lorem ipsum or placeholder imagery in the deliverable?

## Richness floor (answer NO to any of these and the page fails)

Every other item on this list fails a page for *containing* something. These fail it for
*lacking* something, and they exist because the earlier version of this checklist could
be passed perfectly by a blank white page. Measured 2026-07-27: pages built under that
version shipped 1 SVG graphic between six of them, against 114 in the unguided baselines.

RF1. Is there any drawn, photographic or generated imagery on the page at all?
RF2. Is there a signature element a reader could describe from memory tomorrow?
RF3. Does the palette commit to something, rather than being ink on paper with one accent?
RF4. Is there texture, material or depth anywhere: grain, pattern, a real surface?
RF5. Does the direction match the brief's register? If the subject has warmth, appetite,
     humour, craft or a human at its centre, the austerity family (Dense utility,
     Industrial mono, Swiss minimal, Brutalist) is the wrong answer no matter how clean
     it keeps the gate. Two coffee-shop builds landed on "roaster's log book" and
     "technical datasheet". Both failed here.
RF6. If you described this page in one sentence without saying layout, spacing,
     typography or clean, would the sentence contain anything?
RF7. Does every interactive element respond visibly to hover, focus and press? Motion on
     only the two signature moments is not restraint, it is an interface that ignores the
     user. Functional motion is uncapped and expected.
RF8. Is there one material response somewhere, a place where something behaves like a
     real substance rather than a rectangle changing colour?
RF9. Is the palette architecture named, and is it something other than ink-on-paper-plus-
     an-accent? That one structure appeared on 14 of 14 pages this skill produced.
RF10. Is the type architecture named, and does it avoid the faces this skill has already
     overused (Archivo, Bricolage Grotesque, IBM Plex, Source Serif 4, Fraunces, Chivo
     Mono) unless the brief genuinely calls for one?
RF11. Does the page carry enough substance to be worth reading, not just worth looking at?
     Measured 2026-07-27, guided pages ran to roughly a third of the content of unguided
     ones on the same brief, and it got worse with each revision: a documentation
     homepage fell from 4,346 words to 1,108. Craft was being traded for substance.
     Removing invented metrics, testimonials and logo walls is correct, but the space
     they occupied has to be refilled with real material: actual API surface, actual
     process, actual answers. An empty page that is beautifully drawn is still empty.

A page that fails these is not restrained, it is unfinished. Fix by adding, not by
removing more.


## Copy gate

44. `scripts/check_words.py` run on all copy, zero unjustified hits?
45. Buttons named for what happens; action names consistent through the flow?
46. Em dashes: more than one per screen of copy?
47. Any "not X, but Y", rule-of-three triplet, or "-ing" tailing clause?

## Quality floor

48. Squint test passed (focal point + section rhythm at thumbnail size)?
49. All 8 interactive states present; focus ring visible?
50. Empty/loading/error screens designed?
51. Contrast measured and passing?
52. Checked at 320 / 375 / 768px?
53. `prefers-reduced-motion` honored?

Record the result as a short block comment at the top of the main stylesheet or page: date, hits, justifications.
