# Typography authority

Typography for pitch.dog Brand Mode is governed solely by [`bomkino/pitchdog-type-system`](https://github.com/bomkino/pitchdog-type-system). This skill routes to that authority; it does not mirror font families, token values, scales, measures, wrapping rules, CSS, or binaries.

## Resolve the source

For an existing artifact, preserve its immutable tag or commit until a migration is explicitly requested. A type-system change can reflow a finished layout.

For new Brand Mode work:

1. Read the repository root and identify the release declared current.
2. Cross-check that version in `package.json` and `tokens/pitchdog.system.tokens.json`.
3. Verify that a matching Git tag exists and resolve the tag to its commit.
4. If those authorities disagree, keep typography unresolved and name the conflict. Do not choose the newest-looking value.
5. Record the resolved tag and commit in the project or handover, then pin the consuming artifact to that immutable source.

Do not resolve through `main` or GitHub’s “latest release” shortcut. Either can differ from the governed tag. Never hotlink repository font URLs or expose credentials in browser code.

## Read only the branch you need

At the resolved tag or commit, start with the canonical tokens and then load only the relevant contract:

- `tokens/pitchdog.system.tokens.json` — semantic roles and anchors;
- `docs/SPECIFICATION.md` — role behaviour across website, interface, social, and video;
- `docs/WEB-TEXT-WRAPPING.md` — web wrapping and reading measure;
- `docs/USING-IN-PROJECTS.md` — package, submodule, native, and design-tool consumption;
- `docs/KNOWN-FONT-DETAILS.md` — native or static compatibility caveats;
- `docs/ARROWS.md` — typographic arrow roles.

Components consume semantic roles. Do not invent convenient family names, weights, postures, widths, sizes, leading, tracking, or wrapping rules in downstream code.

## Consume, do not transcribe

Use the package exports or copied governed distribution described by `docs/USING-IN-PROJECTS.md`. Keep split CSS layers in their documented dependency order. Variable fonts are authoritative unless the resolved source explicitly says otherwise.

For design tools or native work, use the documented handoff from a full checkout. Do not package fonts inside this design skill, mix variable and static versions of one family, or patch source metadata downstream.

Mindset Mode follows the external brand’s accepted typography. Do not import the pitch.dog type system merely because this skill is active.

## Verify the result

- Record the pinned tag and resolved commit.
- Confirm the production build emits the assets required by that pinned version and has no font request failures.
- Inspect loaded, blocked, fallback, italic/posture, weight, zoom, and text-spacing states where relevant.
- Test real copy at the target widths; a token is not visual proof.
- Keep source resolved, dependency pinned, built, rendered, installed, deployed, live, and accepted as separate claims.

If the authority is inaccessible, ask for an approved checkout or export. A disclosed unresolved state is better than a plausible substitute.
