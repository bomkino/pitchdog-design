# Digital theme and icons

This contract applies to every new digital system created with this skill. Brand Mode uses pitch.dog authority. Mindset Mode preserves the external brand’s accepted visual values and icon family. The product contract still requires System, Light, and Dark; when an external authority lacks one of those modes, derive it provisionally from that authority, label it provisional, and require owner acceptance before calling it brand truth. If an accepted authority explicitly forbids a required mode, preserve the conflict and ask rather than silently overriding either rule. Reviewing or surgically refining an existing single-mode artifact does not silently authorize a theme-system expansion—name the missing state and scope it honestly.

## Light, Dark, System

Every new digital artifact ships three theme choices:

- `System` — the initial default; follows the operating-system preference;
- `Light` — an explicit user override;
- `Dark` — an explicit user override.

Resolve System through `prefers-color-scheme`. Persist an explicit Light or Dark choice, and provide a clear route back to System. Resolve the effective theme before first paint where the platform permits so the opening frame does not flash the wrong room. Set `color-scheme` to the effective `light` or `dark` value when an explicit override is active; use `light dark` only for a System-capable baseline so native controls do not contradict the selected room.

Keep selected theme separate from effective theme:

- selected is `system`, `light`, or `dark`;
- effective is the rendered Light or Dark result;
- an operating-system change updates effective only while selected remains System;
- resetting to System removes the stored override rather than storing the current effective value;
- unavailable or invalid storage falls back to System without blocking render.

Light and Dark are two authored environments, not one palette inverted. Use the same semantic roles in both—ground, surface, raised surface, primary and muted text, boundary, signal, focus, success, warning, danger, and proof frame—but choose each value and contrast relationship deliberately. Project colour may change the climate without tinting or overpowering approved work.

Verify both explicit modes, first-load System, a live operating-system change while System is active, persistence, reset to System, keyboard control, visible focus, forced colours where relevant, reduced motion, and all loading/error/empty/success states. Theme choice must not hide content, change meaning, or become an animation showcase.

## Phosphor Icons

Use [Phosphor Icons](https://phosphoricons.com/) as the sole default interface icon family in Brand Mode and in new unbranded systems. In Mindset Mode, preserve an accepted external icon family. When none exists, use Phosphor as a provisional system choice until owner acceptance. Select the official adapter for the stack:

- React: [`@phosphor-icons/react`](https://github.com/phosphor-icons/react);
- framework-neutral SVG assets and catalogue: [`@phosphor-icons/core`](https://github.com/phosphor-icons/core);
- webfont: [`@phosphor-icons/web`](https://github.com/phosphor-icons/web).

Pin versions in the consuming project’s lockfile. With React or core SVG assets, import only the icons and weights used. With the webfont adapter, load only required weight files; when per-icon payload control matters, prefer core SVG assets instead of shipping a whole catalogue. Do not load every weight for convenience.

Govern the family as language:

- choose the most literal familiar symbol for the action;
- use `regular` as the ordinary starting weight, then change weight for hierarchy or state—not variety;
- reserve `fill` for a genuine selected or committed state;
- use `currentColor` so semantic colour and theme states remain aligned;
- keep optical size, stroke weight, and alignment coherent within a control group;
- pair an icon with text when its meaning is not immediate;
- give icon-only controls an accessible action name and at least a 44 × 44 CSS px target;
- require explicit visible text or an equally explicit adjacent confirmation for destructive, irreversible, permission-changing, or privacy-sensitive actions; an icon and accessible name alone are insufficient;
- hide a redundant decorative icon from assistive technology;
- do not communicate status through icon shape or colour alone;
- mirror only when direction truly follows reading direction.

Typographic arrows inside copy may follow the pinned type-system arrow contract. Interactive controls use the active resolved icon family—Phosphor in Brand Mode and the unbranded default; the accepted external family in Mindset Mode. Do not mix icon families, emoji, hand-drawn stand-ins, or arbitrary SVG styles inside one interface.

For material treatment, obey the single governing boundary in [colour and material](colour-and-material.md).
