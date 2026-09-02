# Responsive, accessibility, and performance

## Responsive authorship

Author priority, sequence, interaction, and density for each relevant context. Preserve the argument, not desktop geometry.

At minimum, inspect the smallest supported phone, a representative phone, one intermediate/tablet width, ordinary desktop, and the widest real display. Add a width at each observed layout failure. Also inspect portrait and landscape when supported, text expansion, 200% zoom, and 400% reflow.

Change order, proof scale, crop, sticky behavior, or control model when the device demands it. Do not use breakpoint count as proof of responsive authorship.

## Accessibility

Target WCAG 2.2 AA where applicable; never claim conformance until the finished artifact is evaluated.

Require:

- semantic structure and meaningful order;
- complete keyboard path;
- persistent visible focus;
- useful names, labels, and instructions;
- inline errors that preserve work and explain recovery;
- announced status changes;
- sufficient text and non-text contrast;
- status not encoded by colour, motion, or sound alone;
- meaningful icons with sufficient non-text contrast and no icon-only ambiguity;
- reduced-motion and reduced-transparency alternatives;
- 200% zoom and 400% reflow without lost content or horizontal page scroll, except genuinely two-dimensional content that requires both axes; contain that exception locally with an operable labelled scroll region rather than making the page scroll sideways;
- adequate touch targets and spacing;
- text alternatives for meaningful visual output;
- captions/transcripts where media requires them;
- no hover-only or gesture-only path.

Accessibility can override aesthetic preference. Treat that as design doing its job.

## Performance

- Render critical content without waiting for scroll or spectacle.
- Use responsive images and verify source resolution.
- Lazy-load only content that can arrive late.
- Play only visible media; prefer manual play for testimony and feedback.
- Prefer transform and opacity in hot animation paths.
- Avoid heavy animated blur, shadows, WebGL foundations, site-wide smooth scrolling, and unnecessary third-party embeds.
- Reserve `will-change` for imminent motion; remove it afterward where practical.
- Test code components separately.
- Test Light, Dark, first-load System, explicit overrides, and reset-to-System without duplicating content or hiding focus.
- Inspect layout shift, long tasks, console errors, broken links, and network failure.
- Test on a mid-range phone and ordinary connection, not only a powerful desktop.

## State completeness

Design and verify:

- loading;
- empty;
- partial;
- error;
- offline or unavailable where relevant;
- success;
- permission denied;
- stale data;
- interrupted/reversed motion;
- reduced motion and contrast.

Use language that states what happened, what remains safe, and how to recover.

## Evidence language

Say exactly what was checked and where. A source file, screenshot, green test, preview URL, or deployment receipt proves only its own layer.

Do not promote “built” to “accessible,” “installed,” “deployed,” “published,” “live,” or “accepted” without corresponding evidence.
