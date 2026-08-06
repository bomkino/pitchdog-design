# Source resolution

Date: 2026-08-06

## Inputs inspected

| Input | SHA-256 | Use |
| --- | --- | --- |
| `PITCHDOG_DESIGN_SKILL_CANONICAL_SOURCE.md` v2.0 | `03f402ae070875ee2c46f4d24e134a57d230f4d814e92480fdee94754fad4995` | Canonical profile routing, fonts, refined colour/dark tokens, and build requirements |
| `pitchdog-designed-by-us-skill-source.md` v1.0 | `bcef26fb643c6d2d59ef1992cb57e1239ad1a27e194ee2247493dae217ec7485` | Actual Goal lens, design constitution, cross-medium depth, quality gates, and anti-overcook rules |
| `pitchdog-brand-profile.yaml` v1.0 | `27388d619d9e0594933abad19e0b579ca20e92175d04efc8a25351720d3a5b06` | Earlier machine-readable profile and exact historical comparison |
| `apple-design/SKILL.md` | `11840b24a11d7f94f39c6aaab074750ae4e4de4ef54ee4b1dd97e16ebd485e61` | Fluid-interface principles, gesture physics, spatial continuity, access |
| `emil-design-eng/SKILL.md` | `433b5a239cda18e0576e4e558532e7e53512e21fafe5b85db4894c28ec399b72` | Motion decision discipline, UI timing, component craft, review format |
| `skill-creator/SKILL.md` | `da44c88f6b3845a8fa8c60792ec9a722110a55a9793c279757b48fefb11f819c` | OpenAI-compatible structure, progressive disclosure, metadata, validation |

The v1 source package also included its authoring prompt, README, and completed audit; all were inspected before synthesis.

## Authority decision

v2.0 labels itself canonical and requests the final `pitchdog-design` name. It therefore governs canonical pitch.dog type and colour values.

The material conflict was typography:

- v1.0 truth-gated family names and treated Neco, Erode, and Geist as historical candidates.
- v2.0 explicitly promotes Neco, Erode, Geist Mono, and the dense-interface Geist Sans adapter to canonical defaults.

Resolution: use v2.0 families, retain lawful-source verification, include disclosed fallbacks, distribute no font binaries, and never claim full fidelity after substitution.

Where P3 values differed slightly, v2.0 values govern. v2.0 also supplies the extended dark palette, `Ink/A14`, and denser semantic aliases.

## Composite decisions

| Tension | Resolution |
| --- | --- |
| CSS transition versus spring | Use exact-property CSS/WAAPI for predetermined state; velocity-aware springs for gesture-driven, momentum-carrying interruption. |
| Keyframes versus interruption | Allow self-contained predetermined sequences; forbid them for direct manipulation. |
| Expressive motion versus frequency | Remove motion from high-frequency keyboard actions; expand only rare, purposeful moments. |
| Apple influence versus imitation | Transfer response, causality, continuity, agency, and restraint; reject Apple surface grammar. |
| Emil detail versus pitch.dog motion ceiling | Keep component craft and debugging discipline inside pitch.dog's zero-bounce, one-dominant-sequence ceiling. |
| Brand recognizability versus client authorship | Separate Brand Mode from Mindset Mode and evaluate leakage adversarially. |
| Comprehensive authority versus context cost | Keep `SKILL.md` lean and route to directly linked references. |

## Originality and third-party boundary

The published skill is a new synthesis. It does not redistribute the Apple or Emil skill files, proprietary course material, or font files. Interaction guidance is rewritten and reconciled against pitch.dog's own rules. Public primary sources are acknowledged in `NOTICE.md`.

0BSD covers repository material only. Third-party fonts, marks, services, and linked works retain their own terms.
