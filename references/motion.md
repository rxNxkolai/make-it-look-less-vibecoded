# Motion

Bans alone produce dead pages. This file is the positive half: what the two allowed
moments should actually be, and how to build them so they read as craft rather than
decoration.

## Two budgets, not one. This is the part that gets misread.

Measured 2026-07-27: two pages built under the earlier wording shipped **exactly two
`@keyframes` each** and nothing else. The rule said "at most 2 moments" and was read as
"animate at most 2 things", which strips an interface of every response it owes the
user. That is the wrong failure and it makes pages feel dead.

There are two separate budgets and only the first is capped.

**Signature moments: at most 2, named in DESIGN.md.** These are the orchestrated,
staged, someone-designed-this events. Spend them on the moment of arrival (what the page
does once, on load) and the moment of consequence (what happens when the user does the
thing the page is for). If you cannot name both in a sentence you have transitions, not
motion design.

**Functional motion: uncapped, and required.** Every interactive element owes the user a
response. Hovers, focus rings, pressed states, disclosure, tab changes, value updates,
row selection, loading, validation, drag feedback, the number that ticks when the data
behind it changes. None of these count against the budget. A page with 40 well-tuned
transitions and 2 signature moments is correct. A page with 2 keyframes and no hover
feedback is broken, not restrained.

The distinction: a signature moment is something the user *notices*. Functional motion
is something they would only notice if it were missing.

**A third thing worth having: material response.** Interfaces that feel made tend to
have one place where the material behaves like a real thing. Ink that soaks rather than
appears. A card that has weight when dragged. A meter that overshoots and settles like a
needle. Type that sets after a beat. Pick one, tie it to the direction, and make it the
thing someone would describe afterwards.

## Choreography, not effects

The difference between designed motion and default motion is whether elements move
*in relation to each other*.

- **Stagger with intent.** 40 to 80ms between siblings. Below 40 reads as simultaneous,
  above 120 reads as slow. Stagger in reading order, never in DOM order if they differ.
- **Anchor the motion.** Things should enter from where they came from, not from a
  generic 20px below. A panel opened by a button should expand from that button's edge.
  `transform-origin` is the most under-used property in AI output.
- **One thing leads.** In a staged entrance, the focal element arrives first and the
  supporting cast follows. Everything arriving at once is the same as nothing arriving.
- **Distance scales with size.** A large element moving 20px looks broken; a small one
  moving 60px looks thrown. Roughly 4 to 8% of the element's own dimension.

## Timing

| Kind | Duration | Curve |
|---|---|---|
| Hover, focus, small state flips | 120-180ms | `cubic-bezier(0.2, 0, 0, 1)` |
| Panels, drawers, disclosure | 200-320ms | `cubic-bezier(0.22, 1, 0.36, 1)` |
| Staged page entrance | 400-700ms total | ease-out family, never ease-in-out |
| Exit | 0.7x the enter duration | faster out than in, always |

Exits are the tell that separates careful from careless. Almost all generated UI uses
the same duration both ways. Real interfaces leave faster than they arrive, because a
user dismissing something has already moved on.

Never `linear` for anything a human looks at. Never bare `ease`, which is a browser
default and reads like one.

## Springs

Use a spring only where something is being *manipulated directly*: a dragged handle, a
sheet the user pulled, a toggle they flipped. Springs on a page-load fade are noise.

If you reach for a spring, mass and damping do the work, not overshoot. Overshoot above
about 1.05 reads as bounce, which is banned as a default for good reason: it makes every
element feel like the same rubber toy.

## Scroll

The universal fade-up-on-scroll is banned. What is allowed, and good:

- **Scroll-linked, not scroll-triggered.** Tie a property to scroll *position* so the
  user is scrubbing it, rather than firing a one-shot animation when an element crosses
  a threshold. Scrubbing feels like control; triggering feels like a slideshow.
- **One pinned sequence, maximum, for the thing that deserves explaining.** If nothing on
  the page needs explaining in steps, do not pin anything.
- **Parallax only with real depth logic.** Layers must move in a consistent relationship
  or the eye reads it as jitter.

If content is hidden at `opacity: 0` awaiting an observer, it must be visible when
scripting fails, when the tab is backgrounded, and when the page loads at an anchor.
Three of the generated pages in `../evidence/` shipped with this bug and rendered blank.

## Performance and honesty

- Animate `transform` and `opacity` only. Never `width`, `height`, `top`, `margin`,
  `padding`: they force layout on every frame.
- `will-change` on the element about to move, removed after. Left on permanently it
  costs memory and can make things worse.
- A loading animation must reflect real progress or not exist. A fake progress bar that
  always takes 1.5 seconds is a lie told in motion.

## prefers-reduced-motion

A genuine no-motion path, not shortened durations. Replace movement with an instant
state change; keep opacity fades under 200ms if you keep anything at all. Parallax,
pinning and scrub effects switch off entirely, and the layout must still make sense
without them, which means it cannot depend on motion to be legible.
