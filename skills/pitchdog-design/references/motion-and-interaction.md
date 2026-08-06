# Motion and interaction

## Contents

- Motion decision
- Technology selection
- Timing and easing
- Direct manipulation
- Momentum and springs
- Spatial behavior
- Component details
- Material and multimodal feedback
- Access and performance
- Review protocol

## Motion decision

Ask in order:

1. **How often is this seen?**
   - hundreds of times daily or keyboard-driven: no motion;
   - frequent navigation/control: instant or drastically reduced;
   - occasional modal, drawer, toast, or state change: standard motion;
   - rare onboarding or expressive moment: delight is allowed if it stays skippable.
2. **What does it do?** Require feedback, explanation, spatial continuity, causal storytelling, or protection from a jarring change.
3. **What happens when interrupted?** If no coherent answer exists, simplify.
4. **What is the reduced-motion equivalent?** Preserve meaning without vestibular travel.

For scroll storytelling, complete: “As the visitor scrolls, X becomes Y, revealing Z.” If Z is the site's ability to animate, remove it.

## Technology selection

Choose by behavior, not fashion:

- **CSS transition:** predetermined state change with exact properties, such as opacity, colour, or a small transform. Prefer for frequently retargeted ordinary UI; never use `transition: all`.
- **`@starting-style`:** progressive-enhancement entry for a newly rendered element when browser support is acceptable.
- **WAAPI:** programmatic, cancellable predetermined motion with browser scheduling and no library requirement.
- **Spring runtime:** direct manipulation, drag release, velocity handoff, or an interaction that must be grabbed and reversed mid-flight.
- **No animation:** keyboard commands, high-frequency actions, weak devices under load, or any case where motion delays the result.

CSS keyframes suit self-contained predetermined sequences. Do not use them for gesture-driven state that must inherit current velocity.

Do not assume a library shorthand is compositor-only. Profile actual frames. Prefer `transform` and `opacity`; use `clip-path` only after target-browser testing. Avoid animating layout properties inside tight interaction loops.

## Timing and easing

Brand starting values:

| Interaction | Timing |
| --- | ---: |
| Pointer-down / press feedback | 80–120ms |
| Hover / focus | 140–180ms |
| Form or status change | 120–200ms |
| Passive reveal | 180–260ms |
| Semantic group stagger | 0–60ms |
| Menu, disclosure, panel | 300–400ms |
| Scroll-state settle | 200–320ms |

Keep ordinary UI below 500ms and usually below 300ms. Long timing is allowed when the user is deliberately holding or scrubbing, never while the system is merely responding.

Easing selection:

- entering or exiting: strong ease-out;
- moving or morphing on screen: ease-in-out;
- hover or colour: `ease` or a tuned ease-out;
- constant progress: linear;
- direct gesture: no easing while held; track 1:1.

Useful CSS curves:

```css
:root {
  --pd-ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --pd-ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --pd-ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

Never use `ease-in` for an ordinary UI entrance; delayed response feels broken.

## Direct manipulation

- Respond on pointer-down; commit on pointer-up.
- Let content follow the pointer 1:1 after a small direction threshold near 10px.
- Preserve the offset where the object was grabbed; do not snap its center to the pointer.
- Use Pointer Events and `setPointerCapture()` so tracking survives leaving bounds.
- Ignore additional touch points after a drag begins.
- Track a short position/time history to estimate release velocity.
- Detect plausible gestures in parallel, then cancel losers when intent becomes clear.
- Keep input enabled during motion.

Allow a tap to cancel when the pointer leaves its padded target and recover when it returns. Provide roughly 10px hysteresis where the platform allows.

## Momentum and springs

Default to zero bounce. Add a small under-damped response only when a physical gesture supplied momentum.

Starting spring qualities:

| Use | Damping ratio | Response |
| --- | ---: | ---: |
| Reposition | 1.0 | 0.4s |
| Rotation after gesture | 0.8 | 0.4s |
| Drawer or sheet release | 0.8 | 0.3s |

Treat response as a behavior parameter, not fixed duration.

### Interruption

Start from the live presentation value, not the previous target. Retarget the running spring and carry velocity through reversal. For 2D motion, use independent X and Y springs.

### Velocity handoff

Pass release velocity to the spring in the units its API expects. If an API expects relative velocity:

```text
relativeVelocity = gestureVelocity / (target - current)
```

Guard zero or near-zero remaining distance.

### Momentum projection

Choose a destination from projected momentum, then animate to it with release velocity:

```js
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}

const projected = current + project(releaseVelocity);
const target = nearestSnapPoint(projected);
```

Use a lower rate such as `0.99` for a shorter projection. Validate with real device input rather than copying a number blindly.

### Soft boundaries

Continue responding past a bound with increasing resistance:

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) /
    (dimension + constant * Math.abs(overshoot));
}
```

Hard stops feel frozen; endless free travel feels broken.

## Spatial behavior

- Open from a visible source and return along the same path.
- Set popover transform origin from its trigger; keep centered modals centered.
- Preserve current position and velocity during reversal.
- Telegraph the likely final state in intermediate frames.
- Finish a sticky terminal state before releasing the section.
- Let fast scroll skip animation but land in the correct logical state.
- Never queue stale scroll states.

## Component details

### Pressable elements

Register the press immediately. A subtle `scale(0.97)` can work for a physically sized button; a ruled row may instead use colour, inset, or registration shift. Do not force scale on every control.

### Entrances

Do not enter from `scale(0)`. Begin near the final form, commonly `scale(0.95–0.98)` plus opacity. The object should not appear from mathematical nothing.

### Tooltips

Delay the first tooltip enough to avoid accidental activation. Once one is open, let adjacent tooltips appear instantly and without a repeated entrance animation.

### Lists

Use 30–80ms semantic stagger only for decorative entry. Never block interaction until stagger completes. Coordinate opacity with height/position by inspecting frames; no universal formula replaces tuning.

### Hold-to-confirm

Make the deliberate hold linear and visible; make cancellation/release fast. Keep an accessible non-hold alternative where motor or input constraints require it.

### Crossfades

If two shapes read as overlapping objects, a tiny synchronized blur may bridge them. Use sparingly and profile Safari; blur is not a substitute for correct structure.

## Material and multimodal feedback

Use translucent material only when it communicates a floating functional layer. Match blur, opacity, edge, and shadow to surface size. Never stack low-contrast translucent layers until text disappears.

For sound and haptics:

- **Causality:** fire on the actual commit, snap, success, or error.
- **Harmony:** align visual, sound, and haptic on the same perceived frame.
- **Utility:** reserve them for meaningful events; repetition destroys signal.

## Access and performance

### Reduced motion

Replace travel, pinning, parallax, large scale, and bounce with direct state changes or 120–200ms opacity. Preserve content order, state, and orientation.

### Reduced transparency

Raise surface opacity or use a solid field; remove backdrop blur.

### Increased contrast

Use near-solid fields, clear boundaries, and stronger focus. Do not rely on vibrancy.

Gate hover behavior:

```css
@media (hover: hover) and (pointer: fine) {
  .control:hover { /* hover-only enhancement */ }
}
```

Avoid full-viewport looping backgrounds, slow oscillations, large brightness changes, animated blur fog, and media walls. Test on an ordinary phone while the page is loading.

## Review protocol

1. Use slowly.
2. Reverse before completion.
3. Trigger again while moving.
4. Test pointer, keyboard, and touch.
5. Inspect in slow motion or frame by frame.
6. Test reduced motion and transparency.
7. Test under CPU/network pressure on a mid-range device.
8. Check origin, current-value continuity, end state, and focus.
9. State what the motion clarified.

If the answer is only “it feels premium,” remove or simplify it.
