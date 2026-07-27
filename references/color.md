# Color

## Process

1. Design in grayscale first. Get hierarchy working with spacing, size, and weight alone; if the page reads in gray, color becomes seasoning instead of a crutch.
2. Cap the palette at 3 hues: one dominant (~60% of surface), one neutral (~30%), one sharp accent (~10%). Extend with tints and shades of those hues, never new ones.
3. Tint the neutrals. Pure `#ffffff` and `#000000` are flat; shift "white" and "black" a few points warm or cool toward the dominant hue for depth.
4. Keep semantic colors (success, warning, error, info) as a separate token group, out of the brand palette.
5. Lock everything as CSS variables in DESIGN.md before building. OKLCH preferred (perceptually even tints/shades); hex acceptable.

## Bans, and why

- `bg-indigo-*`, `bg-violet-*`, purple-to-blue gradients: the single most recognized AI fingerprint, inherited from years of indigo-500 defaults in the training data.
- `#2563EB` (Tailwind `blue-600`) and `#5E6AD2`-adjacent "Magic Blue" as the unexamined primary: the second-generation defaults.
- Gradient text, gradient blobs, animated gradient backgrounds, neon glow on dark.
- Evenly split palettes with no dominant hue: timidity reads as no decision.
- The "tasteful defaults": cream `#F4F1EA` + terracotta `#D97757`, and near-black + acid green. Fine when the brief asks; convergence when it doesn't.

A hard trick that works: in Tailwind projects, REPLACE the `colors` object in the config instead of extending it, so `bg-indigo-600` fails the build. Forcing the failure is the point.

## Contrast targets

Measure, never eyeball. WCAG AA minimum everywhere (4.5:1 body, 3:1 large text and UI parts). On dark themes prefer APCA: Lc 75+ for body, 45+ for large text, 30+ for non-text. Check the accent-on-dominant combination first; it fails most often.

## Example token sets (starting points, not answers)

Editorial print:
```
--ink: oklch(0.24 0.02 60);      /* warm near-black */
--paper: oklch(0.97 0.01 85);    /* warm off-white */
--accent: oklch(0.55 0.19 25);   /* deep brick red */
```

Industrial mono:
```
--ink: oklch(0.92 0.01 140);     /* pale green-gray text */
--ground: oklch(0.2 0.01 140);   /* deep gray-green */
--accent: oklch(0.85 0.21 130);  /* signal green, sparse */
```

Warm organic:
```
--ink: oklch(0.3 0.04 40);
--ground: oklch(0.95 0.02 70);
--accent: oklch(0.62 0.13 150);  /* leaf */
```

Derive 3-4 tints/shades per hue with OKLCH lightness steps; that is the whole system.
