# DESIGN.md - token lock

Filled before any UI code. After the lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** Half Past Six, a neighbourhood bakery at 412 Ash Street. Four bakes a day, sells until it runs out.
- **Audience:** People who live within a ten minute walk and want bread today, not a brand story.
- **The page's single job:** Answer "is there sourdough left right now, and if not, when is the next one out?"
- **Direction:** Dense utility. A live bake board, the way a kitchen or a station concourse would build it. Marketing air removed on purpose.
- **Why not the obvious one:** Warm organic is the reflex answer for a bakery and it is also the measured 2026 default (cream paper + serif display + terracotta). Every bakery page on the internet is that page. This bakery's actual daily problem is timing and stock, so the page is a board, not a placard.
- **The one deliberate risk:** A dark ground for a bakery. Justified, not reflexive: the object being imitated is a lit status board, and the shop's work happens between 21:00 and 07:00. Dark is the board's native form. Two sections invert to paper so the page is not uniformly dark.
- **Signature element:** The oven timeline. A 06:00-16:30 track with four bake notches and a marker that sits at the real current time and moves as you sit there. The board below is filtered by it.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | Bricolage Grotesque (variable, opsz + wght) | 200, 400, 500, 800 | Wordmark, H1, section headings, big time numerals. 200 against 800 carries the hierarchy. Characterful grotesque, not a default. |
| Utility / data | IBM Plex Mono | 400, 500, 600 | Board rows, times, prices, counts, hours table, rail. Tabular figures by construction. |

- Scale: base 16px, ratio x1.25 (dense/app). 13px permitted for table data only.
- Measure: 60-72ch on the two prose blocks; everything else is tabular and sets its own width.
- Display tracking: -0.02em at large sizes. Deliberately not 72px/-1.8px.
- 24-hour time everywhere. It is a work schedule, so it reads as one.

## Color

Three hues. Dominant dark ground, light bone neutral, one saffron accent. Semantic red is a separate group used only for form validation.

```css
:root {
  /* dominant ~60% - cool charcoal, oklch(0.21 0.006 220) */
  --ground:      #16191B;
  --ground-2:    #1D2124;   /* raised rows, rail */
  --ground-3:    #2A2F33;   /* hairlines on dark */

  /* neutral ~30% - cool bone, oklch(0.91 0.006 150) */
  --paper:       #E3E6E0;
  --paper-2:     #D5D9D2;   /* inverted-section hairlines, input fields */
  --ink:         #16191B;   /* = ground, reused on paper */
  --bone:        #E3E6E0;   /* = paper, reused on dark */
  --bone-muted:  #9BA29B;   /* 6.76:1 on ground */
  --bone-faint:  #6B726D;   /* sold-out, non-text only */

  /* accent ~10% - saffron, oklch(0.84 0.15 88) */
  --accent:      #F4C430;   /* 10.75:1 on ground */
  --accent-deep: #C79A18;   /* press/hover shade on paper */

  /* semantic, separate group, validation only */
  --error:       #E5484D;   /* 4.51:1 on ground, never used alone without text */
}
```

Measured contrast: bone on ground 14.01:1. Accent on ground 10.75:1. Muted on ground 6.76:1. Ink on paper 14.01:1. Ink on accent 10.75:1.

**Hard rule from the measurement:** accent on paper is 1.38:1. On the light sections the accent may only appear as a *fill* with ink on top, never as text or a hairline. Checked before building because accent-on-dominant is the pair that usually fails.

Split: ground ~60% / paper ~30% / accent ~10%.

## Space, shape, depth

- Base unit: 8px, 4px half-step. No arbitrary values.
- Radius scale (3 values): `0` for the board and all surfaces, `3px` for inputs, buttons and chips, `999px` for the status dot only. Nothing is `rounded-2xl`.
- **Shadow policy: none.** Zero shadows on the page. Separation is carried by whitespace, a 3-5% background-lightness shift, and hairlines. Hairlines appear only between peer rows in a list or table, never around a section.
- No box wraps a section. No card contains another card.

## Motion budget (max 2 moments)

1. **Page load:** the board rows stagger in, opacity 0 to 1 and translateY(6px) to 0, 40ms apart, 320ms each, once. Not scroll-triggered, not applied to anything else on the page.
2. **Interaction family:** one shared 180ms transform/opacity response on the time chips, the hold buttons, and the timeline marker's travel. Same duration, same curve, so it reads as one system rather than scattered effects.

Easing: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1)`.
`prefers-reduced-motion: reduce` path: rows appear instantly, marker jumps without transition, all transitions removed. Real no-motion path, not a shortened one.

No ambient loops. The clock ticks because it is live data, not decoration; the status dot does not pulse.

## Macrostructure

**#8 Dense utility**, alternating ground and paper so no two consecutive sections share a treatment:

1. Status rail (dark) - live clock, open/closed, next bake. A status bar carrying data, not a wordmark-plus-four-links-plus-button nav. No button in it at all.
2. Board (dark) - H1 sentence, oven timeline, time chips, the live table. Zero hero CTAs; the only actions are inside the board rows.
3. The bake (paper) - asymmetric 5/7, short prose at measure on the left, weekly list on the right. Hairline rows, no cards.
4. Standing order (dark) - asymmetric, accent fill block, a real form with all 8 states.
5. Visit (paper) - address block plus tabular hours, then three plain facts.
6. Footer (dark) - one dense strip, different density from the rail: it carries tomorrow's first bake instead of a live clock. Not a four-column link grid.

Squint test target: the amber timeline marker and the H1 are the single focal point; sections alternate light/dark so the thumbnail shows five distinct bands, not five identical centered boxes.

## Copy rules for this page

- No invented proof. No customer counts, no ratings, no testimonials, no press logos. Prices, times, addresses and stock counts are the page's content, not claims about its popularity.
- Plain verbs. No "craft", "curated", "artisan", "made with love", "elevate".
- Button vocabulary survives the flow: "Hold one" produces "Held until 14:12". "Start the standing order" produces "Standing order started".
- Errors give direction, not mood.
- Phone numbers use the 555 range so nothing resolves to a real business.
