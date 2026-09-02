# Design-system governance

Use this branch when the deliverable is a reusable system, token layer, component library, pattern, or migration. A system should make safe, expressive work easier; it should not turn authored compositions into inventory.

## Layer the authority

1. **External authorities:** accepted brand sources, the resolved typography system, platform standards, rights, and protected material.
2. **Semantic foundations:** theme roles, space relationships, boundaries, focus, motion qualities, density, layers, and state language.
3. **Primitives:** text-role adapters, icons, controls, inputs, layout, proof frames, and feedback.
4. **Components and patterns:** repeated jobs with shared state, data, access, or interaction behaviour.
5. **Authored compositions:** page arguments, campaign ideas, proof sequences, jokes, and one-off choreography. Keep these outside the reusable core.

A lower layer consumes the authority above it. It does not copy and rename it. In Brand Mode, reference the pinned pitch.dog type system instead of creating a second typography source.

## Start from use

Before adding a token or component, recover:

- the real user or production need;
- two representative real uses; a verified near-term second use may justify a local pilot, not reusable extraction;
- the failure caused by leaving it local;
- the authority it centralizes;
- the states, media, themes, inputs, and content extremes it must survive;
- the owner and migration cost.

Prototype inside the real artifact first. Extract only after the shared contract is visible.

## Acceptance bar

A system addition must be:

- useful: solves a demonstrated repeated need;
- distinct: not an alias for an existing primitive;
- usable: has clear content, interaction, and recovery behaviour;
- coherent: consumes existing semantic foundations;
- adaptable: survives the contexts it claims to support;
- evidenced: inspected in representative artifacts, not only a catalogue page.

If one criterion fails, keep the solution local or repair the existing primitive.

## Token discipline

Name tokens by role and relationship, not current appearance. Prefer surface, text-muted, focus, danger, cluster-gap, or chapter-space over lavender-200, tiny-grey, or homepage-gap.

Keep raw values at the foundation edge. Components consume semantic roles. Do not encode one composition as a global spacing or colour token.

For every new digital system, provide complete Light and Dark values behind the same semantic roles, with System as the initial theme state. Follow [digital theme and icons](digital-theme-and-icons.md).

## Component contract

Document:

- job and when not to use it;
- anatomy and content limits;
- variants that represent meaning, not aesthetic choice;
- default, hover, focus, active, selected, disabled, loading, empty, error, success, and permission states as relevant;
- keyboard, touch, pointer, assistive-technology, and reduced-motion behaviour;
- Light, Dark, and forced-colour behaviour;
- responsive and container behaviour;
- source authority, version, owner, and migration notes;
- real examples and known limits.

A catalogue rendering is evidence of availability, not usability.

## Change discipline

Classify each change:

- **patch:** repairs implementation without changing the contract;
- **minor:** adds a backwards-compatible role, state, or component;
- **major:** changes meaning, metrics, API, behaviour, or an existing role in a way that can alter artifacts.

Pin external authorities. Record the resolved ref and commit. Deprecate before removal where consumers exist. Provide a migration path and inspect at least one real consumer before calling a migration safe.

Do not silently upgrade typography, rename semantic roles for tidiness, or alter every composition to prove adoption.

## Keep soul outside the kit

The system owns reliability: type authority, theme semantics, icons, focus, states, access, responsive behaviour, and repeatable mechanics.

The artifact owns point of view: its proof, primary event, strange little thing, chapter grammar, crop, joke, and emotional pace.

If every page is easy to recognize as the same template, the system has consumed the work. Move narrative decisions back to the artifact.

## Evidence

Report separately:

- source and schema validation;
- catalogue rendering;
- representative consumer rendering;
- keyboard, assistive-technology, zoom, theme, device, and motion checks;
- migration readback;
- owner acceptance.

Stop when the system centralizes real authority, reduces repeated error, and leaves compositions freer—not when the catalogue looks full.
