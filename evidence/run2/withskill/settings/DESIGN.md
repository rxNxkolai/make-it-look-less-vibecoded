# DESIGN.md - token lock

Filled 2026-07-26, before any UI code. After the lock: no new hues, fonts, radii, shadows, or motion.

## Brief

- **Subject:** Settings for Tremolo, a music streaming app (desktop + mobile web).
- **Audience:** people who care how their music sounds. The listener who owns headphones worth configuring, keeps 40GB downloaded for the subway, and has an opinion about crossfade length.
- **The page's single job:** let someone change one audio setting and see, without leaving the row, what it does to the sound they are about to get.
- **Direction:** **Dense utility**, executed as an audio control surface. Tool-first, compact spacing, keyboard-visible, zero marketing air. The reference is studio hardware, a mixing desk faceplate: dark cheek on the left, light aluminium panel, silkscreened labels, real faders, a signal path printed across the top.
- **The one deliberate risk:** the settings do not sit in a list, they sit in a **signal chain**. A live readout strip across the top of the panel shows source, codec, EQ, level, crossfade and output as one path, and every control on the page writes into it. If a setting does not change the sound, it is not in the chain. That is a real constraint on the design and it drives the whole layout.
- **Signature element:** that signal chain strip, plus the 6-band EQ built as actual vertical faders with dB readouts rather than a picture of an EQ.

### Why not the obvious answers

- **Not dark by reflex.** Every music app ships dark, so dark is the default answer here and defaults are what this is trying to avoid. Light aluminium is also the honest call: settings is the one screen in a music app where legibility beats ambience. Dark ships as a real user choice in Appearance, and it actually works.
- **Not cream + serif + rust.** That is the measured 2026 default. This goes cool zinc + grotesk/mono + signal green instead.
- **No marketing surfaces.** No hero, no feature cards, no footer link columns. This is a view inside an app. Views do not have display headlines.

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display / UI | Archivo (variable) | 200, 400, 500, 600, 800 | Weight contrast carries hierarchy: 200 on the big chain numbers against 800 on the wordmark. Width axis stays at default except the wordmark, set expanded. |
| Utility / data | Azeret Mono | 300, 400, 500 | Every number on the page: kbps, dB, LUFS, GB, seconds, codec names, shortcut keys. Never decorative, always carrying a value. |

- Scale: base 16px, ratio x1.25 → 12 / 13 / 15 / 16 / 20 / 25 / 32
- Row titles 16px, descriptions 15px, mono data 13px, mono micro 12px (data only, inside meters and tables)
- Measure: descriptions capped at 62ch
- Italics used for the one place they belong: the "custom" EQ state and inline value names in helper text.

## Color (CSS variables)

Three hues. Panel = zinc with a faint green cast (dominant). Ink = graphite with the same cast (neutral). Signal = deep green (accent). Semantic reds/ambers are a separate group, out of the brand palette.

```css
:root {
  /* dominant ~60% : panel */
  --panel-00: #E7E9E4;  /* page ground */
  --panel-10: #DCDFD9;  /* raised row / rail-on-light */
  --panel-20: #CDD1CA;  /* recessed groove, fader slot */
  --panel-30: #B9BEB6;  /* hairline strong */

  /* neutral ~30% : ink */
  --ink-00: #1C211E;    /* primary text, and the left rail ground */
  --ink-10: #3A423D;
  --ink-20: #545E58;    /* secondary text, 5.44:1 on panel-00 */
  --ink-30: #6E7872;    /* disabled text, 3.70:1 on panel-00 */
  --rail-dim: #8E968F;  /* secondary text on the dark rail, 5.37:1 */

  /* accent ~10% : signal */
  --signal:      #0E6B4F;  /* 5.25:1 on panel-00, white on it 6.49:1 */
  --signal-lift: #128A66;  /* hover */
  --signal-dark: #48C495;  /* the same hue lifted for use on ink-00, 7.47:1 */
  --signal-wash: #CFE0D8;  /* tint, fills and track-active only, never text */

  /* semantic, separate group */
  --peak:  #B4231E;   /* clip / destructive, 5.30:1 on panel-00 */
  --warn:  #8A6206;
}
```

Dark theme (`[data-theme="dark"]`) inverts panel and ink within the same three hues, no new ones:
`--panel-00:#1C211E --panel-10:#232926 --panel-20:#2C332F --panel-30:#3A423D --ink-00:#E7E9E4 --ink-20:#A7AFA9 --ink-30:#7A837D --signal:#48C495 --peak:#F2665E`

Every pair above was calculated, not eyeballed. Lowest ratio used for body text is 5.25:1.

## Space, shape, depth

- Base unit: 8px, 4px half-step. Row padding 12/16. Section gap 40. Rail width 264px.
- Radius scale, 3 values total: `0` (default, including every button, which is deliberately square), `2px` (inputs, chips, fader slots), `999px` (switch capsule only, because a switch is physically a capsule).
- Shadow policy: **none**, with one exception stated up front. Depth comes from panel lightness steps and hairlines. The only shadow on the page is a single soft upward one on the docked save bar, because it floats over content and needs to read as above it.

## Motion budget (max 2 moments)

1. **Save bar dock.** When there are unsaved changes the bar translates up from the bottom edge, 220ms, `--ease-out`. Reverses on save or discard. `transform` + `opacity` only.
2. **Chain acknowledgment.** When a control writes to the signal chain, that one node in the chain lifts to `--signal-wash` and fades back, 200ms. It confirms the write and nothing else.

No scroll animation of any kind. No hover bounce. No spinners: loading states are text plus a sized skeleton.

Easing token: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);`
`prefers-reduced-motion`: honored, and the in-app "Reduce motion" setting sets the same flag so the control is real.

## Macrostructure

**#3 sidebar-anchored crossed with #8 dense utility.** Persistent left rail, scrolling panel, no marketing air.

Two deliberate breaks from the default version of that shape:

- **The rail carries state, not just labels.** Each section entry shows its own current key value in mono on the right, so the nav doubles as a summary readout: `Audio quality → 320 AAC`, `Downloads → 12.4 GB`. Changing a setting changes the nav. It also holds the filter box, which is the fastest path to any row and is bound to `/`.
- **No footer.** The bottom edge belongs to the save bar, which exists only when there is something to save. The page ends on the last setting row, the way an app view does.

Asymmetry: dark 264px rail against a wide light panel, and the panel's own content is left-weighted (label column reads long, control column sits right against a hard right edge). Nothing on the page is centered except the fader dB readouts.

## Section rhythm (so no two read the same at thumbnail)

1. Signal chain strip, full-bleed dark band
2. Playback, plain rows
3. Audio quality, rows + segmented selectors + the fader block
4. Downloads, rows + a horizontal usage meter
5. Library, rows + removable chip list
6. Notifications, a real matrix table
7. Devices, list rows with a refresh that skeletons
8. Account, rows ending in a destructive zone
9. Appearance, rows + the theme selector

## States shipped

All 8 on every control. Screen-level states designed, not left over: devices loading skeleton, empty devices, empty hidden-artist list, empty filter result, cache cleared, save error with a named cause and a fix.

## Responsive decisions (made during build, recorded here)

- **Below 900px** the rail stops being a rail. It becomes a horizontally scrolling strip of section tabs across the top, each still carrying its value underneath the name. The strip scrolls rather than wraps, so the order of sections stays readable.
- **Below 620px** the segmented controls stop being segments. Four options with bitrate figures cannot sit on one line at 320px without either shrinking below a 44px target or scrolling under a clipped focus ring, so they become a full-width option list, name left, bitrate right in mono. Same control, same states, different shape.
- **The signal chain scrolls, it never wraps.** Each node sizes to its own value and the strip scrolls sideways. A wrapped audio path stops being a path.
- Verified at 320, 375, 768 and 1440. No horizontal page scroll at any of them.

## Slop test

Run against the rendered page on 2026-07-26. Zero Tier 1, zero Tier 2, zero Tier 3 hits. Full record, including the two deliberate exceptions and every measured contrast pair, is the block comment at the top of the stylesheet in `index.html`.
