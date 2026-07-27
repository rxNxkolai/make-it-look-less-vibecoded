# Interaction and live objects

The strongest generative rule this project produced, and it came out of the evidence
rather than out of taste.

## Show the working thing

Across the pages in `../evidence/`, the with-skill builds that read least like generated
output all did the same structural thing: **the page contains the product's core object,
working, rather than a description of it.**

| Page | What the hero actually is |
|---|---|
| Habit tracker | A live 365-square year sheet. Click a square, the counts recompute. |
| Bakery | A bake board driven by the real clock. Items move from "in 6h" to "cooling" to "sold out" as time passes. |
| E-commerce | A brushable revenue tape. Drag the window, every figure below follows. |
| Docs | A real reactive implementation, about 100 lines, with a dependency graph that lights up in recompute order. |
| Settings | A signal chain across the top. Change any control and the chain redraws. |

And on 8 measured handmade sites, the same instinct: Linear argues by displaying app
surface, not by stacking claim cards.

This is not a demo bolted onto a marketing page. The distinction that matters:

- A **screenshot** says "trust me, it looks like this".
- A **mockup** says "imagine it looks like this".
- A **live object** says "here, use it" and cannot lie, because it is the thing.

Build the third one. It is usually less code than the fake version, because you write
the logic once instead of hand-faking every state.

## What makes it real rather than a toy

- **It computes.** Every number on screen derives from the object's actual state. The
  moment you hardcode "82%" next to a grid that would compute 57%, you have invented a
  metric, which is a Tier-1 fail.
- **It has a today.** Seeded, deterministic data beats random. Random data reshuffles on
  reload and destroys trust; a fixed seed with real structure (weekly rhythm, seasonality,
  a genuine outage in July) reads as a real account.
- **It is honest about being sample data.** Label it once, plainly, somewhere permanent.
  Not as a disclaimer stamped over the top.
- **It survives interaction.** Every state a user can reach must be designed, including
  the empty one. If the empty state is unreachable because the sample data is too tidy,
  change the data so it can happen.

## Direct manipulation over controls

Given a choice between a control that sets a value and an object the user can grab,
choose the object.

- A brushable tape beats a date-range dropdown.
- Clicking the grid square beats a "mark today" button.
- Dragging the EQ band beats a numeric input.

The control is easier to build and always available as a fallback for accessibility, but
the manipulable object is what makes a page feel made rather than assembled.

## Keyboard is not optional, and it is a design surface

A live object that only works with a mouse is half-built.

- A grid of hundreds of cells gets **one** tab stop with roving focus, not 365 tab stops.
  Arrows move, Enter or Space acts, Home and End jump.
- Every custom control has a real semantic role, `aria-pressed` or `aria-current` where
  applicable, and a visible focus ring that lands somewhere legible. Check the ring
  against the element *and* the background; a ring that vanishes on one of the two is
  the most common miss.
- Shortcuts are shown, not hidden. If `/` focuses search, say so in the field.

## Micro-interaction, with restraint

The motion budget is two moments and this is where the second one usually goes: the
moment of consequence, when the user's action changes the object.

- Acknowledge the input on the element that received it, immediately, under 180ms.
- Change one property, not four.
- Never animate the thing the user is currently pointing at out from under them.
- Optimistic updates need a real rollback path, not a hope.

## The eight states, applied to objects

`states-access.md` covers the per-element states. A live object also needs:

- **First run.** What it looks like with no history at all.
- **Partial.** Some data, not enough for the full view.
- **Stale.** Data exists but is old, and the interface says so.
- **Failed refresh.** The last good state stays on screen; the failure is announced
  beside it, not instead of it.

Blanking a working view because a refresh failed is the most common way a good object
becomes a bad one.

## The test

Open the page and try to break the main object. If nothing you click changes anything,
you built a picture. If something changes but the numbers around it do not, you built a
lie. Both are worse than a static page that is honest about being static.
