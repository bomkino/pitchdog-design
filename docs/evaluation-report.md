# Evaluation report

Date: 2026-09-03
Release candidate: v2.0.0

## Objective verdict

The v2 source and package hold as a design-decision system. The skill routes pitch.dog and external-brand work differently, defers typography to its governed repository, requires authored Light and Dark states with System default, governs Phosphor without erasing external icon authority, prohibits additive grain, and preserves composition outside the component kit.

This verdict covers source structure, package integrity, and fresh decision-behaviour probes. It does not certify the taste, accessibility, performance, rendering, or owner acceptance of a future design artifact.

## Structural and package evidence

| Check | Result | Evidence |
| --- | --- | --- |
| OpenAI `quick_validate.py` | Pass | Valid skill name, frontmatter, description, and structure |
| Repository validator | Pass | Exact 27-file allowlist; UTF-8/text-only and no-symlink boundary; ten live profile references; 15 eval specifications; 110-line entrypoint |
| Local-link and privacy scan | Pass | Local Markdown links resolve; no user path, mounted-volume path, or local file URL in published text source |
| `skills` CLI discovery | Pass | Local repository exposes one installable skill: `pitchdog-design` |
| Package determinism | Pass | `.zip` and `.skill` are byte-identical at SHA-256 `ef5276f0f47983beefaa4fee2cd59d496a2a3d57ebda7b38fa08746ddd0aadd9` |
| Package round-trip | Pass | 27 archive entries; extracted skill byte-matches source and passes OpenAI validation |
| Diff hygiene | Pass | `git diff --check` reports no whitespace error |

The repository validator is a structural boundary check. Phrase sentinels and consistency assertions guard known regressions; they do not prove semantic quality or behaviour by themselves.

## Fresh behavioural evaluation

Independent forward runs exercised all 15 case specifications. Each run had an expected profile, required decisions, forbidden outcomes, and a named failure. The first pass was allowed to fail.

The eight Brand Mode cases initially met all 35 required decisions and 29 of 30 forbidden-outcome checks. The real miss was destructive icon semantics: an accessible name alone still allowed an icon-only destructive action. The final contract now requires visible text or an equally explicit adjacent confirmation for destructive, irreversible, permission-changing, and privacy-sensitive actions.

Seven Mindset, proof, system, review, and print cases then exposed four authority seams: external Phosphor fallback was not explicitly provisional; theme rules could overrule external values without recording inference; Light/Dark language leaked into print; and one near-term component use could be promoted as a reusable second use. Fixtureless review and component prompts also needed to reward an evidence hold instead of inviting invented findings.

After repair, focused reruns passed the affected cases and adjacent regressions:

- Brand editorial scenes retain one primary event; dense tools use task and state hierarchy instead.
- Accepted external typography, colour, material, and icon authority remains intact.
- Missing external theme modes and icon direction are explicitly provisional until owner acceptance.
- Reusable extraction requires two representative real uses; a near-term use permits only a local pilot.
- Physical work resolves colour through its production profile and proof, not interface themes.
- Missing artifacts produce a named evidence hold, not fabricated critique.
- All no-grain, immutable-type-pin, System-theme, authored-phone, and static-first-motion guards remained intact.

These are reasoning probes against supplied case facts, not built or rendered artifacts. Counts describe adherence to the eval specification; they are not a taste score.

## Whole-artifact criticism and repairs

A separate source critic held the candidate until the following material defects were repaired:

- global production typography, palette, and motion values were removed or made project-provisional;
- the always-loaded profile was reduced from a duplicated 263-line brand kit to a 115-line authority router;
- theme selection and effective theme were separated, including native `color-scheme` behaviour;
- external material language was protected while the owner-wide no-additive-grain rule remained universal;
- the design-system gate was aligned everywhere to two observed real uses;
- evidence states now separate edited, built, rendered, checked, installed, deployed, published, live, and accepted;
- package validation changed from an extension blacklist to an exact allowlist with UTF-8 verification;
- exact private research fingerprints and inventory counts were moved to a private receipt.

The final source reread found no remaining priority 1–3 source defect.

## Publication and installation evidence

| State | Result | Evidence |
| --- | --- | --- |
| Release source committed and pushed | Pass | Commit `16594f65b85fc67d2fd081405bffc733dc547342` reached `origin/main` |
| Hosted CI | Pass | GitHub Actions run `33679728465` validated and rebuilt the exact release-source commit |
| Immutable tag | Pass | Annotated `v2.0.0` tag dereferences to the release-source commit |
| GitHub Release | Pass | Public, non-draft, non-prerelease release with `.zip`, `.skill`, and both checksum manifests |
| Public asset readback | Pass | Four assets downloaded anew; both manifests, archive CRC, 27-entry allowlist, source diff, and OpenAI validation passed |
| Active Codex installation | Pass | Exact `v2.0.0` GitHub source installed; 27 installed files byte-match release source and public extraction |
| Install provenance | Pass | Skills lock records repository `bomkino/pitchdog-design`, ref `v2.0.0`, path `skills/pitchdog-design/SKILL.md`, and folder hash `202811c23df47c0f837f2e6b1c463dc8546ceb3b` |
| Recovery | Pass | Previous installed skill and pre-update lock were copied to a private backup outside the repository before replacement |

GitHub source, release assets, and the active install are verified states. No design artifact was created by this release, so rendered-artifact quality and owner acceptance remain deliberately unclaimed.
