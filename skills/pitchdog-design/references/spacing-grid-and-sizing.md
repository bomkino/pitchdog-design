# Spacing, grid, and sizing

## Atomic scale

Use a 4px base and an 8px dominant rhythm. Approved starting tokens:

```text
4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 80 · 96 · 128 · 160 · 192 · 256
```

Do not treat every multiple of four as a token. Use optical exceptions only when content or font metrics prove the need.

## Relationship defaults

| Relationship | Typical range |
| --- | ---: |
| Eyebrow to headline | 12–16px |
| Headline to body | 20–32px |
| Body to action | 24–32px |
| Proof to caption | 8–12px |
| Related items | 16–32px |
| Modules within one section | 48–80px |
| Ordinary section transition | 96–160px |
| Major chapter transition | 160–256px |

Use these as relationships, not mandatory padding values.

## Authored canvases

| Canvas | Width | Columns | Margin | Gutter |
| --- | ---: | ---: | ---: | ---: |
| Wide | 1600px | 12 | 64px | 32px |
| Desktop | 1200px | 12 | 48px | 24px |
| Tablet | 810px | 8 | 32px | 20px |
| Phone | 390px | 4 | 20px | 12px |

Review at 360, 390, 600, 768, 810, 834, 1024, 1200, 1366, 1440, 1600, 1920, 2560, and 3840px. Add a new breakpoint only when a real failure proves the existing fluid composition insufficient.

## Four spatial layers

1. **Viewport Scene:** full-width ground, colour, clipping, chapter state.
2. **Wide Proof Canvas:** large media and project proof; often `92%` width with a `2560–3200px` cap according to page.
3. **Editorial Core:** structured relationships; commonly capped near `1760px`.
4. **Reading Measure:** sustained text; optically near `680–760px`.

At 4K, proof and relationships grow. Body measure does not.

## Density modes

- **Compact:** forms, tables, terms, metadata, FAQ, status, pricing details.
- **Standard:** services, process, testimonials, ordinary chapters.
- **Chapter:** proof, major argument, colour takeover, large composition.
- **Scene:** a deliberate viewport or sticky state that earns its footprint.

Vary top and bottom rhythm. Tight spaces join; large spaces divide.

## Grid breaking

Allow an object to break the grid only while retaining an anchor: a line, edge, caption, column, or explicit relationship.

Useful breaks include proof reaching an edge, a title crossing a media boundary, a sheet entering off-grid then resolving, or true marginalia.

Avoid random offsets, unexplained negative margins, inconsistent page edges, and universal full bleed.

## Sizing principles

- Use scale causally: importance, immersion, project authority, or task criticality.
- Give one object authority instead of six equal objects.
- Keep touch targets at least 44px; prefer 48px.
- Preserve native media ratios unless art direction explicitly crops.
- Let a testimonial or note determine its measure; do not truncate to fit a system.
- Use full bleed selectively. If everything bleeds, nothing does.
