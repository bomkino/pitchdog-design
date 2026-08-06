# pitch.dog Brand Foundation

## Contents

- Governing character
- Typography
- Surface and tactility
- Cards and objects
- Controls and navigation
- Internal product adapter
- Brand completion checks

## Governing character

Create work that feels exact but alive, warm but unsentimental, witty but unshowy, generous but not vague, tactile but contemporary, politically aware through material choices, and confident enough to stop.

Use the brand foundation as a starting authority. Give each subject a distinct answer.

## Typography

### Canonical editorial stack

- **Neco:** display, major headlines, project titles, brief pull quotes.
- **Erode:** body, introductions, sustained explanation, editorial actions.
- **Geist Mono:** eyebrows, folios, metadata, status, measurements, credits, utility language.
- **Geist Sans:** dense controls, tables, and small UI body where a functional product needs it.

Obtain Neco and Erode from their official Fontshare family pages. Obtain Geist from [Vercel's official distribution](https://vercel.com/font) or Google Fonts where its reduced glyph/features set is sufficient. Verify the current licence and weights before implementation. Never bundle font files in this skill.

If a family is unavailable, use a disclosed temporary fallback and do not claim complete brand fidelity:

```css
--pd-font-display: "Neco", "Iowan Old Style", "Palatino Linotype", Georgia, serif;
--pd-font-body: "Erode", "Iowan Old Style", "Palatino Linotype", Georgia, serif;
--pd-font-ui: "Geist Sans", Inter, system-ui, sans-serif;
--pd-font-mono: "Geist Mono", "SFMono-Regular", Menlo, Consolas, monospace;
```

### Starting type scale

Treat values as optical starting points. `1rem = 16px`.

| Role | Wide | Desktop | Tablet | Phone | Leading |
| --- | ---: | ---: | ---: | ---: | ---: |
| Display XL | 7.5rem | 6rem | 4.5rem | 3rem | 0.90–0.98em |
| Display / H1 | 5.5rem | 4.5rem | 3.5rem | 2.625rem | 0.94–1.02em |
| H2 | 4rem | 3.25rem | 2.5rem | 2rem | 0.98–1.08em |
| H3 | 2.25rem | 2rem | 1.75rem | 1.5rem | 1.05–1.18em |
| Intro | 1.5rem | 1.375rem | 1.25rem | 1.125rem | 1.30–1.45em |
| Body | 1.125rem | 1.125rem | 1.0625rem | 1rem | 1.48–1.62em |
| Small | 0.9375rem | 0.9375rem | 0.875rem | 0.875rem | 1.40–1.55em |
| Eyebrow / Utility | 0.8125rem | 0.8125rem | 0.75rem | 0.75rem | 1.25–1.40em |

Starting tracking:

- Neco display: `-0.01em` to `-0.035em`, tighter as scale grows.
- Erode body: `-0.005em` to `0.01em` after legibility review.
- Geist Mono utility: `0.03em` to `0.08em`; uppercase only when it aids orientation.

Keep sustained body measure near 55–70 characters. Break display lines where thought turns. Do not center every short headline or use all-caps eyebrows as decoration.

## Surface and tactility

Aim for a contemporary studio whose digital work retains evidence of handling.

Use:

- hard or nearly hard edges;
- fine rules and visible boundaries;
- crop, overlap, occlusion, and controlled stacks;
- registration details tied to use;
- real project residue;
- tiny contact shadows only where surfaces meet;
- native proof ratios.

Avoid global glass, universal soft shadows, scrapbook texture, moving grain, fake tape, random rotation, tears, stains, and distressed nostalgia.

Default radius is `0–4px`; proof frames use `0–2px` unless project shape says otherwise. Irregularity must explain hierarchy or handling.

## Cards and objects

A boundary must represent a real object, relationship, or action. Possible families:

- **Proof Frame:** deck page, film frame, website, treatment, product media.
- **Story Card:** one state in a causal transformation.
- **Offer Object:** service, engagement, or scope shape.
- **Index Row:** archive, navigation, FAQ, pricing, or programme status.
- **Testimonial Note:** exact words and attribution; quote length sets measure.
- **Status Row:** open, paused, active, complete, unavailable.
- **Utility Control:** menu, close, previous, next, copy, download.

Do not default to icon, heading, and paragraph inside an equal rounded tile. Share behavior; keep narrative compositions authored.

## Controls

Use a small family:

1. **Ink Block:** primary commitment action.
2. **Editorial Link:** lower-intensity action without a container.
3. **Index Row:** full-width navigation or disclosure.
4. **Utility Control:** compact mechanical action.

Defaults:

- rectangular or nearly rectangular;
- 48–56px high for primary touch controls;
- 44px minimum usable target, 48px preferred;
- visible focus and immediate registered press;
- restrained arrow movement only when directional;
- decorative layers with `pointer-events: none`.

No default pills, magnetic chase, liquid fills, glowing gradients, endless arrows, or wobble.

## Navigation

Favor an editorial shell over a floating SaaS capsule.

- Keep direct routes direct.
- Separate a parent link from its disclosure control.
- Use one content source across breakpoints.
- Implement collision detection, safe pointer travel, Escape, focus return, and touch alternatives for desktop menus.
- Use an authored full-screen contents view on phone rather than miniature desktop dropdowns.
- Keep useful paths visible; do not make navigation spectacular at the cost of clarity.

## Internal product adapter

Keep Brand Mode but change density and type balance:

- make task and output the protagonist;
- use familiar controls, compact tables/forms/status, search, recovery, and undo;
- reserve Neco for product identity or rare voiced moments;
- use Geist Sans/Mono for dense operation;
- use brand colour as paper, ink, focus, and semantic status—not atmosphere;
- remove marketing-page scroll theatre.

“Anti-SaaS” never licenses an unfamiliar or inefficient tool.

## Brand completion checks

- Load exact colour, spacing, and grid files.
- Confirm lawful font availability and actual loaded families.
- Preserve client/project proof without tinting.
- Check sRGB fallback and intended contrast.
- Verify phone, tablet, desktop, and wide behavior.
- Verify static, reduced-motion, empty, loading, error, and success states.
- Inspect rendered output before claiming checked.
