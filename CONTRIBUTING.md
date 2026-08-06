# Contributing

Contributions are welcome when they make the skill more truthful, portable, useful, accessible, or resistant to samey output.

## Before changing the skill

- Open an issue for a material new direction.
- Keep pitch.dog Brand Mode separate from external-brand Mindset Mode.
- Preserve accepted facts, credits, and source provenance.
- Prefer principles, decision rules, and counterexamples over fixed compositions.
- Do not add font binaries, secrets, telemetry, remote code, or undocumented dependencies.
- Do not copy proprietary course material or third-party skill text.

## Make the change

- Keep `SKILL.md` operational and under 500 lines.
- Put detail in a directly linked reference.
- Add or update an adversarial eval for every behavior change.
- Use imperative language and exact evidence boundaries.
- Keep the skill text-only unless deterministic code is necessary and fully reviewable.

## Validate

```bash
python3 -m venv .venv
.venv/bin/python -m pip install PyYAML==6.0.2
.venv/bin/python scripts/validate-skill.py
.venv/bin/python scripts/package-skill.py --output dist/pitchdog-design.zip
```

Inspect the resulting zip before opening a pull request.

## Licence of contributions

By contributing, you agree that your contribution is distributed under this repository's 0BSD licence.
