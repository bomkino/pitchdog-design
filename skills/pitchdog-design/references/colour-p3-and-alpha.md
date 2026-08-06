# Colour: Display-P3, sRGB, and alpha

## Contents

- Model
- Opaque tokens
- Semantic alpha
- Behaviour
- Verification

## Model

Treat three axes separately:

```text
Theme: System / Light / Dark
Scene: Neutral / Powder / Lilac / Mint / Blush / Project / Ink Room
Signal: None / Vermilion / Cobalt / Project
```

Use only states the artifact needs. Colour behaves as paper, ink, signal, project material, or narrative state—not ambient digital lighting.

## Opaque tokens

### Light and shared

| Token | Display-P3 | sRGB fallback | Role |
| --- | --- | --- | --- |
| `Paper/Neutral` | `color(display-p3 0.964 0.961 0.972)` | `#F6F5F8` | main cool paper |
| `Paper/Powder` | `color(display-p3 0.900 0.925 0.957)` | `#E4ECF5` | process and technical calm |
| `Paper/Lilac` | `color(display-p3 0.950 0.920 0.975)` | `#F2EBF8` | reflection, invitation, humour |
| `Paper/Mint` | `color(display-p3 0.918 0.946 0.910)` | `#EAF1E8` | useful or communal state |
| `Paper/Blush` | `color(display-p3 0.990 0.900 0.925)` | `#FDE9EE` | authorship and human warmth |
| `Sheet` | `color(display-p3 0.992 0.988 0.982)` | `#FDFCFB` | proof page or sheet |
| `Ink` | `color(display-p3 0.055 0.054 0.060)` | `#0E0E0F` | primary light-mode ink |
| `MutedInk` | `color(display-p3 0.37 0.38 0.41)` | `#5F6169` | supporting facts |

### Dark

| Token | Display-P3 | sRGB fallback | Role |
| --- | --- | --- | --- |
| `InkRoom` | `color(display-p3 0.044 0.047 0.054)` | `#0B0C0E` | main dark ground |
| `BlueBlack` | `color(display-p3 0.050 0.061 0.080)` | `#0C1015` | cool technical dark |
| `PanelDark` | `color(display-p3 0.083 0.085 0.097)` | `#151619` | dark sheet or panel |
| `Dark/Lilac` | `color(display-p3 0.065 0.050 0.082)` | `#110D15` | reflective dark state |
| `Dark/Mint` | `color(display-p3 0.043 0.070 0.058)` | `#0B120F` | useful dark state |
| `Dark/Blush` | `color(display-p3 0.090 0.050 0.058)` | `#170D0F` | human dark state |
| `LightInk` | `color(display-p3 0.945 0.941 0.931)` | `#F1F0ED` | primary dark-mode ink |
| `MutedLightInk` | `color(display-p3 0.65 0.655 0.69)` | `#A6A7AF` | supporting dark facts |

### Signals

| Token | Display-P3 | sRGB fallback | Role |
| --- | --- | --- | --- |
| `Signal/Vermilion` | `color(display-p3 0.88 0.32 0.21)` | `#F34325` | warm editorial punctuation |
| `Signal/Cobalt` | `color(display-p3 0.13 0.31 0.80)` | `#0450D4` | cool editorial punctuation |
| `Signal/CobaltDark` | `color(display-p3 0.55 0.66 0.95)` | `#85A9F8` | cobalt over dark fields |

Use one signal family at a time unless two distinct meanings require both. Verify contrast before using signal colour for text.

## Semantic alpha

Apply alpha in the colour value while keeping layer opacity at 100%. Whole-layer opacity fades content and children.

```text
Ink/A04  Ink/A08  Ink/A12  Ink/A14  Ink/A16  Ink/A24  Ink/A40  Ink/A64
LightInk/A04  LightInk/A08  LightInk/A12  LightInk/A16
LightInk/A24  LightInk/A40  LightInk/A64
Vermilion/A12  Vermilion/A24  Vermilion/A40
Cobalt/A12  Cobalt/A24  Cobalt/A40
Sheet/A88  Sheet/A96
InkRoom/A40  InkRoom/A64  InkRoom/A80  InkRoom/A88  InkRoom/A96
```

Aliases:

| Alias | Light | Dark |
| --- | --- | --- |
| `Surface/Quiet` | `Ink/A04` | `LightInk/A04` |
| `Surface/Hover` | `Ink/A08` | `LightInk/A08` |
| `Surface/Selected` | `Ink/A12` | `LightInk/A16` |
| `Surface/Pressed` | `Ink/A16` | `LightInk/A24` |
| `Rule/Subtle` | `Ink/A14` | `LightInk/A16` |
| `Rule/Strong` | `Ink/A24` | `LightInk/A24` |
| `Scrim/Soft` | `InkRoom/A40` | `InkRoom/A40` |
| `Scrim/Strong` | `InkRoom/A64` | `InkRoom/A64` |
| `Scrim/Maximum` | `InkRoom/A80` | `InkRoom/A80` |

## Behaviour

- Let project colour change the room around proof; never tint unapproved proof.
- Use discrete editorial cuts, short crossfades, or one field covering another.
- Treat dark mode as an authored ink room, not automatic inversion.
- Keep the system mostly monochrome; use signals as punctuation.
- Never animate grain or cycle through a rainbow.
- Do not make every section a new scene colour.
- Ask “why here?” for every colour change.

## Verification

1. Grayscale: hierarchy and story survive.
2. sRGB: every P3 colour has a useful fallback.
3. Contrast: text, icons, controls, focus, and status meet the target.
4. Proof: surrounding colour does not compete with owner-supplied work.
5. Alpha: child content stays opaque.
6. Dark mode: proof, focus, errors, and muted text remain deliberate.
