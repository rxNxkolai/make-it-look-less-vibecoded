<!-- Name the ARCHITECTURE before the values. Filling in three hues and two fonts
     without choosing a structure is how 14 pages came out as ink on paper with an
     accent. See the palette and type architecture menus in SKILL.md. -->

Palette architecture: ______  (60/30/10 | two-ink | mono+1 | polychrome | achromatic | night | analogous earth | clash)
Type architecture:    ______  (display+body | one superfamily | three roles | type-as-image | system stack)

# DESIGN.md - token lock

Fill before writing any UI code. After the lock: no new hues, fonts, radii, shadows, or motion mid-build. Change this file first if something truly must change, and say why.

## Brief

- Subject:
- Audience:
- The page's single job:
- Direction (one from SKILL.md table, or the brief's own words):
- The one deliberate risk:
- Signature element (the one thing this page will be remembered by):

## Type

| Role | Family | Weights used | Notes |
|---|---|---|---|
| Display | | | |
| Body | | | |
| Utility (optional) | | | |

- Scale: base 16px, ratio x1.25 (app) / x1.333 (editorial)
- Measure: 60-80ch body

## Color (CSS variables, OKLCH preferred)

```css
:root {
  --dominant: ;
  --neutral: ;
  --accent: ;
  /* tints/shades derived from the three above only */
  --success: ; --warning: ; --error: ; --info: ;
}
```

Split: dominant ~60% / neutral ~30% / accent ~10%.

## Space, shape, depth

- Base unit: 8px (4px half-step)
- Radius scale (max 3 values):
- Shadow policy (none / one soft level / layered, pick one):

## Motion budget (max 2 moments)

1.
2.

Easing tokens: `--ease-out: cubic-bezier(0.22, 1, 0.36, 1);`
`prefers-reduced-motion` path: yes.

## Macrostructure

Chosen structure (from layout-spacing.md menu) and why it fits the content:
