# Contributing

Contributions are welcome when they make the skill more truthful, useful, accessible, portable, or resistant to samey output.

## Before changing behaviour

- Start with an observed user need or named failure, not catalogue completeness.
- Keep pitch.dog Brand Mode separate from external-brand Mindset Mode.
- Preserve accepted facts, credits, rights, and source provenance.
- Keep one source of truth. Point to canonical dependencies instead of copying them into prose.
- Prefer decision rules, completion criteria, and counterexamples over fixed compositions.
- Do not add font binaries, private assets, secrets, telemetry, remote code, or undocumented dependencies.
- Do not copy proprietary course material or third-party skill text.

## Shape the skill

- Put the universal operating spine in SKILL.md and branch-only detail in a directly linked reference.
- Co-locate one concept's rule, definition, and caveats.
- Make each process step end in a checkable criterion.
- Prune duplicated and no-op sentences without deleting useful design knowledge for brevity.
- Update a realistic behavioural case when a change alters behaviour.
- Keep objective structural checks separate from qualitative design judgment.

## Validate

    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements-dev.txt
    .venv/bin/python scripts/validate-skill.py
    .venv/bin/python scripts/package-skill.py --output dist/pitchdog-design.zip

Inspect the archive, run the affected behavioural cases with a fresh agent, and record only evidence that was actually produced.

## Licence of contributions

By contributing, you agree that your contribution is distributed under this repository's 0BSD licence.
