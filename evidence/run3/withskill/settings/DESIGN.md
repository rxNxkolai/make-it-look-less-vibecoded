# DESIGN.md - token lock

Filled 2026-07-27, before any UI code. After the lock: no new hues, fonts, radii, shadows or motion moments.

## Brief

- **Subject:** Settings for **Tungsten**, a music streaming app. Desktop and mobile web, the same view.
- **Audience:** the listener who has opinions about crossfade length and knows which of their outputs is the good one. Not an engineer, but someone who will drag an EQ band until it sounds right rather than pick a preset.
- **The page's single job:** let someone change an audio setting and **hear the difference immediately**, without leaving the page or playing a real track.
- **Direction:** **Industrial mono**, built as a listening console rather than a terminal. Mono type carries every number (Hz, dB, kbps, GB, ms, LUFS), a grotesque carries the human sentences, and the ground is a deep petrol dark lit by one amber. Data-dense, exposed structure, no marketing air.
- **The one deliberate risk:** the page **makes sound**. It generates a two-bar loop in the browser with Web Audio and runs it through the actual settings. The equaliser is five real BiquadFilters, mono is a real channel sum, balance is a real StereoPanner, loudness is a real gain. Nothing here is a picture of a control. If a setting cannot be heard, it is honest about being state only.
- **Signature element:** the **response curve**, drawn from the same biquad coefficients the player uses, with five handles you drag directly on it. Behind it, a live spectrum drawn from a real AnalyserNode. Move a handle, the curve redraws, the spectrum tilts, and the sound changes under your hand.

### Why not the obvious answers

- **Not a rail of sections with values in it.** That is the standard settings-page answer and the earlier build of this brief already did it. The persistent surface here is a **monitor**, not a nav: what you are about to hear, permanently on screen while you change what makes it.
- **Not cream paper, serif display and a rust accent.** That is the measured 2026 default. This goes deep petrol, warm bone, one amber.
- **Not indigo, not near-black-plus-acid-green, not glass.** Named defaults, all of them.
- **Dark is a product decision, not a reflex.** A spectrum and a level meter are unreadable on paper white, and this app is used at night with the lights down. Light ships as a real, working choice in Appearance, and the page is contrast-measured in both.
- **No hero, no display headline.** This is a view inside an app. The h1 is the word `Settings` at 20px, in the header line, next to the account.

## Type

Two families, three roles. Both from Google Fonts, both variable.

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display / wordmark | Bricolage Grotesque | 200, 500, 800 | Character comes from the width and optical-size axes, not from bolding. Wordmark at 800 with `wdth` 78 (condensed), section headings at 500, the monitor figure's unit label at 200. The 200-against-800 span is the whole hierarchy strategy. |
| Body / UI | Bricolage Grotesque | 400, 500 | Row names 500, descriptions 400 at 15px, capped at 62ch. |
| Data | IBM Plex Mono | 400, 500 | Every number and unit on the page: Hz, dB, kbps, GB, ms, LUFS, seconds, and the shortcut hints. Never decorative. Tabular by default. |

- Scale: base 16px → **11 / 13 / 14 / 15 / 16 / 20 / 40** as actually rendered.
- **The one large figure, added during the build.** The scale above ran 11 to 20 and stopped, which left the page with no focal point and left this document's own "200 against 800" claim unbuilt. The monitor now opens on the bitrate you will actually get, at 40px in mono 300 with the unit at 200. That is a 2.7x jump over the 15px body, it changes when the output or the quality changes, and it is derived rather than typed. It is the answer to the only question the page exists to settle. Not a hero metric: no gradient, no accent rule beside it, and it lives inside an instrument, not above a call to action.
- Italics used where they belong: the `Custom` equaliser state, and the name of a preset inside a sentence.
- Fallback stacks are real, not `sans-serif` alone, so the page still reads offline.

## Color (CSS variables)

Three hues total. Petrol (dominant, ~60% of surface), bone (neutral, ~30%), amber (accent, ~10%). Semantic red is a separate group and never used as brand colour.

```css
[data-theme="console"] {
  /* dominant ~60% : petrol */
  --ground-00: #101A1D;   /* page ground */
  --ground-10: #162327;   /* header deck, monitor pane */
  --ground-20: #1E2F34;   /* wells, slider tracks, recessed */
  --ground-30: #2A4148;   /* hairlines, borders, spectrum bars */
  --ground-40: #3E6F78;   /* lifted petrol, spectrum fill, 3.12:1 */

  /* neutral ~30% : bone */
  --ink-00: #EDE8DC;      /* primary text, 14.50:1 on ground-00 */
  --ink-20: #9AA8A6;      /* secondary text, 7.20:1 on ground-00 */
  --ink-30: #6E807F;      /* disabled, 4.26:1 on ground-00 */

  /* accent ~10% : amber */
  --signal:    #F2A93B;   /* 8.87:1 on ground-00 */
  --signal-lo: #C4861F;   /* pressed / dimmed amber */
  --on-signal: #101A1D;   /* text on an amber fill, 8.87:1 */

  /* semantic, separate group */
  --alarm: #F2705E;       /* 6.16:1 on ground-00 */
}

[data-theme="daylight"] {
  --ground-00: #DDE4E3;
  --ground-10: #E8EDEB;
  --ground-20: #CFD8D7;
  --ground-30: #AFBDBB;
  --ground-40: #7C9296;
  --ink-00: #10201F;      /* 13.30:1 on ground-00 */
  --ink-20: #46595A;      /* 6.51:1 */
  --ink-30: #6E8080;      /* 3.71:1, disabled only */
  --signal:    #7A4E03;   /* 5.52:1 on ground-00 */
  --signal-lo: #5C3A02;
  --on-signal: #F4F1E9;
  --alarm: #A32217;       /* 6.09:1 */
}
```

Every pair above was calculated with the WCAG relative-luminance formula, not eyeballed, then re-measured off the rendered page in both themes. Lowest ratio used for body text in either theme is 5.58:1. `--ink-30` is used only for disabled text and non-essential units, where 3:1 is the bar.

### One token changed during the build, and why

`--ground-40` moved from `#3E6F78` to `#43757F` (console) and from `#7C9296` to `#6B8286` (daylight). Measuring the rendered page showed `--ground-30` sitting at 1.64:1, and it was doing two different jobs: separating rows, and drawing the edge that tells you where a button, a select, a switch or a slider track begins. The first job is decorative separation and 1.64:1 is fine for it. The second is WCAG 1.4.11, which wants 3:1, and it was failing.

So the two jobs were split. Row hairlines, pane dividers and plot gridlines stay on `--ground-30`. Every edge that identifies a control moved to `--ground-40`, which was nudged until it cleared 3:1 against both the page and the monitor pane in both themes. Measured after the change: component edges land between **3.15:1 and 4.34:1**. Hover moved to `--ink-30` so it still reads as a change. No new hue: this is a lightness step inside the petrol already in the palette, which is what the three-hue rule allows.

No third accent. The spectrum, the meter fill and the storage bar all use tints of petrol and amber, which is why the palette holds at 3 hues while carrying four different data graphics.

## Space, shape, depth

- Base unit: 8px, 4px half-step. Row padding 14/20. Section gap 44. Monitor pane 380px.
- Radius scale, 3 values, no others: `0` (every surface and every button, deliberately square, because 9 of 9 measured AI-builder pages had zero square CTAs and that makes square available), `3px` (inputs, chips, wells, slider thumbs), `999px` (the switch capsule only, because a switch is physically a capsule).
- **Shadow policy: none.** Not one, anywhere. Depth comes from four petrol lightness steps, hairlines at `--ground-30`, and the grille texture. The undo bar reads as floating because of a hairline and a lightness step, not a blur.

## Texture and imagery

Rung 1 and rung 2 of the imagery ladder, plus rung 4.

- **The real thing:** a live spectrum from a real AnalyserNode, and a real level meter reading peak and RMS in dBFS off the time-domain buffer.
- **The real thing, drawn:** the frequency-response curve, computed from the Audio EQ Cookbook coefficients that Web Audio itself specifies, so the drawing and the sound come from one set of numbers.
- **A diagram that teaches:** the crossfade figure, two gain envelopes drawn at the actual crossfade length. At 0s it draws a butt cut, which is the correct picture of zero.
- **Texture:** a horizontal grille on the header deck (repeating gradient, 4px pitch, like a speaker fret) and a fine `feTurbulence` grain over the deck and the monitor pane at 4.5% opacity. Both inline, no network, no image files.
- Icons: two glyphs on the whole page, a play triangle and a stop square, both inside the transport button where they replace text rather than decorate it. No icon set. No emoji.

## Motion budget (max 2 moments)

1. **Arrival.** The response curve draws from flat to its stored shape over 420ms, leading; the ten control sections follow in a 55ms stagger in reading order. One element leads, the rest follow it.
2. **Consequence.** When a control changes what you would hear, the matching line of the monitor readout flips to amber and settles back: 160ms in, 112ms out, which is the 0.7x exit rule.

Hover, focus and small state flips run at 140ms `--ease-flip` as ordinary state feedback per the timing table; they are not moments and nothing else on the page animates. No scroll animation of any kind. No spinners: the devices refresh shows a sized skeleton, and the skeleton is only as wide as the content it stands in for.

```css
--ease-out: cubic-bezier(0.22, 1, 0.36, 1);
--ease-flip: cubic-bezier(0.2, 0, 0, 1);
```

`prefers-reduced-motion` gets a genuine no-motion path: no curve sweep, no stagger, no translate on the undo bar, instant state changes. The in-app **Reduce motion** switch sets the same flag, so the control is real rather than decorative.

**The arrival animation is not allowed to lie.** It starts the curve flat, which is a shape the equaliser may not be in, and `requestAnimationFrame` does not run in a background tab or a pane that is not compositing. Caught during verification: the curve stayed flat and all five handles sat at 0 dB while the stored equaliser was late night. The sweep now carries a hard timeout backstop, gives up the moment the page is hidden, and never runs at all if the page loads hidden. A settings page drawing the wrong state is worse than one drawing the right state without ceremony.

## Macrostructure

**#1 split-screen, asymmetric,** with the evidence side made permanent. Controls left at `minmax(0,1fr)`, monitor right at 380px, the monitor sticky so it never leaves while you scroll the settings that feed it.

Deliberate breaks from the default version of that shape:

- **The right side is not a summary, it is an instrument.** It plays, it measures, it can be dragged. Changing a control on the left is answered on the right within one frame.
- **No footer.** The page ends on the last setting row, the way an app view does. The bottom edge belongs to the undo bar, which exists only when there is something to undo.
- **No save button.** Changes apply the moment you make them, and the one-step undo is the safety net. A settings page that batches changes cannot let you hear them.
- Header is app chrome, not marketing nav: back to library, wordmark, view title, a filter field bound to `/`, transport, account. Not wordmark plus four links plus a button on the right.

Asymmetry: 380px of lit instrument against a wide field of rows; the left column is left-weighted with controls hard against a right edge; nothing on the page is centred except the dB readouts inside the meter.

Below 1040px the monitor moves above the controls and stops being sticky, because a sticky instrument would eat half a phone screen. The bottom status bar carries the consequence feedback instead: it already names what changed. Below 620px the segmented controls become full-width option lists, because four bitrate options cannot hold a 44px target on one line at 320px, and every control the thumb reaches goes to 44px.

Verified at 376px: no horizontal overflow, segments stacked, monitor first, canvas tracking its own box, and the only sub-44px targets left are the 40px curve handles, which are a pointer affordance with a 44px native slider beside them for every band.

## Section rhythm (so no two read alike at thumbnail size)

1. Deck, full-bleed, grille texture, dark band
2. Jump strip, thin, sticky, horizontal
3. Output, plain rows plus a select and a centred-zero balance slider
4. Sound quality, three segmented banks with mono bitrates
5. Equaliser, preset chips plus five labelled slider rows
6. Playback, a slider with a drawn figure beside it
7. Downloads, a storage bar plus a removable album list
8. Notifications, a real two-column matrix table
9. Devices, list rows with a skeleton and a live error row
10. Privacy, rows ending in a two-step destructive action
11. Appearance, segmented controls that actually re-theme the page
12. Account, rows ending in a bordered danger block

## Sample data, stated once

The loop, the six downloaded albums, the five devices and the account line are stand-ins, labelled plainly on the page. Every figure shown is computed from them: the storage bar is the sum of the album sizes against the reserve you set, the applied gain is the gain node's real value, the sample rate is the audio context's real rate. Nothing is hardcoded next to something that would compute differently.

## States shipped

All eight on every interactive element. Screen-level states designed rather than left over: monitor stopped, devices loading skeleton, device unreachable with the list still on screen beside the failure, downloads emptied, reserve exceeded, filter with no matches, quality option disabled with the reason given, history cleared confirmation.

## Slop test

Run against the rendered page. Result recorded as a block comment at the top of the stylesheet in `index.html`.
