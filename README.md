# pitch.dog Design

An open Agent Skill for making design useful, specific, warm, exact, and alive—without turning every project into the same house style.

It works in two profiles:

- **Brand Mode:** canonical pitch.dog type roles, Display-P3 and sRGB colour, spacing, grid, surfaces, motion, responsive behavior, and finishing standard.
- **Mindset Mode:** pitch.dog's judgment, proof discipline, rhythm, care, and artifact review in service of somebody else's identity.

The governing rule: **design with a spine, not a uniform.**

[![License: 0BSD](https://img.shields.io/badge/license-0BSD-111111.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/bomkino/pitchdog-design)](https://skills.sh/bomkino/pitchdog-design)

## Install in Codex or another compatible agent

Codex:

```bash
npx skills add bomkino/pitchdog-design --skill pitchdog-design -g -a codex -y
```

Every agent supported by the `skills` CLI:

```bash
npx skills add bomkino/pitchdog-design --skill pitchdog-design -g -a '*' -y
```

Update later:

```bash
npx skills update pitchdog-design -g -y
```

Review community skills before installation. This repository is deliberately text-only inside the skill: no executable code, remote tool dependency, secret, tracking script, or font binary.

## Install in ChatGPT and Work

1. Download [`pitchdog-design.zip`](https://github.com/bomkino/pitchdog-design/releases/latest/download/pitchdog-design.zip).
2. In ChatGPT, open **Plugins → Skills → Create → Upload from your computer**.
3. Choose the zip and complete ChatGPT's scan/install flow.
4. Install separately on ChatGPT desktop and web/mobile. Personal Skills do not currently sync automatically between those surfaces.
5. If workspace permissions allow, use the skill's `•••` menu → **Share** to publish it to selected people or the workspace library.

See OpenAI's current [Skills in ChatGPT](https://help.openai.com/en/articles/20001066) guide for plan and admin requirements.

## Use

Invoke explicitly:

```text
Use $pitchdog-design to art-direct this pitch.dog landing page.
```

```text
Use $pitchdog-design in Mindset Mode for this client. Keep its bright palette and sans-serif identity.
```

```text
Use $pitchdog-design to review this drawer interaction. Diagnose only; do not change code.
```

Supported work includes web and Framer, products and internal tools, decks, documents, identities, print, invitations, social assets, motion contracts, design systems, and artifact audits.

## What it refuses

- pitch.dog surface leaking into client work;
- Apple, Awwwards, or “premium” cosplay;
- cards, empty space, paper texture, or motion used as proof of quality;
- fake portfolio work or invented facts;
- inaccessible reference mimicry;
- rebuilding strong work when a surgical repair is enough;
- confusing built, rendered, checked, accepted, and published.

## Repository

```text
skills/pitchdog-design/
├── SKILL.md
├── agents/openai.yaml
├── brand-profiles/pitchdog.yaml
├── references/
├── templates/
└── evals/evals.json
```

The installed skill uses progressive disclosure: routing stays lean; detailed brand, motion, medium, and review guidance loads only when needed.

## Validate and package

```bash
python3 -m venv .venv
.venv/bin/python -m pip install PyYAML==6.0.2
.venv/bin/python scripts/validate-skill.py
.venv/bin/python scripts/package-skill.py --output dist/pitchdog-design.zip
```

The package script produces a deterministic zip with one top-level `pitchdog-design/` folder, ready for ChatGPT upload.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Add principles and counterexamples when they improve judgment. Do not add fixed page recipes that make unrelated work converge.

## Licence

[0BSD](LICENSE). Use it, change it, fork it, sell work made with it, remove attribution, teach from it. No permission ceremony.

Voluntary acknowledgement is lovely but never required. Third-party fonts, marks, services, and linked works keep their own terms; see [NOTICE.md](NOTICE.md).
