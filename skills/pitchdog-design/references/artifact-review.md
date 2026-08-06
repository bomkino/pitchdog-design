# Artifact review

## Required output

1. **Objective verdict:** whether the artifact does its real job.
2. **What works:** concrete evidence, not compliments.
3. **Proxy-compliant failures:** polished choices that hide a weaker outcome.
4. **Consequential unknowns:** missing truth, assets, permissions, browser/device evidence, or user research.
5. **Ranked repairs:** smallest changes, highest impact first.
6. **Evidence boundary:** checks performed and not performed.

For UI code review, put every actionable change in one Markdown table:

| Before | After | Why |
| --- | --- | --- |
| Exact current code or behavior | Exact proposed code or behavior | User consequence and design reason |

Distinguish functional failure, brand-system failure, and taste. Do not redesign merely because another taste is possible.

## Core tests

### Unfamiliar-reader

Can a new person explain what this is, why it matters, and what to do next?

### Proof

How quickly does real evidence arrive? Does it support the nearby claim? Is it large enough to inspect?

### Grayscale

Does hierarchy survive without colour?

### Silhouette

Blur or zoom out. Is the composition a field of equal cards and generic zones?

### Texture-off

Remove grain, scans, tape, shadows, and residue. Does material logic remain?

### Container-off

Would removing a card improve hierarchy or meaning?

### Motion-off

Is the static artifact excellent? Does reduced motion preserve content, order, and state?

### Reverse-motion

Interrupt and reverse every interactive transition. Does it continue from the visible value, retain control, and restore state?

### Phone-authorship

Does phone edit priority, density, proof, and interaction—or merely stack desktop?

### 4K

Does proof gain authority while sustained reading stays controlled?

### Brand Mode

Are canonical type, colour, spacing, sizing, surface, motion, and responsive rules used semantically rather than ceremonially?

### Mindset Mode

Does the target remain itself with no pitch.dog surface leakage?

### Identity swap

Could another studio replace the logo and publish this unchanged?

### Authorship

Does the subject still sound and look like itself? Are collaborators and sources credited?

### Actual Goal stress

Reverse a style preference while keeping audience, content, and constraints stable. Do integrity-critical choices remain tied to outcome?

### Last pass

Check copy, names, pronouns, titles, figures, URLs, credits, crops, contrast, permissions, focus, loading, empty/error/success states, file hygiene, and handover.

## Review boundaries

- A source review proves source behavior, not rendering.
- A screenshot proves one visual state, not interaction or access.
- A green build proves compilation, not audience outcome.
- A deployment URL proves hosting, not correctness.
- An automated accessibility scan finds classes of issues, not conformance.
- Only an owner accepts consequential creative work.

Name exact surface, viewport, input method, date, and version when evidence can drift.

## Repair rule

Fix the highest-consequence failure first. Re-run only affected tests plus one regression pass. Stop when further changes are taste churn.
