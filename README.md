# pitch.dog Design

An open Agent Skill for making design useful, specific, warm, exact, and alive—without turning every subject into the same house style.

Version 2 replaces the old token-heavy draft with a governed process:

- **Brand Mode:** pitch.dog authority, real proof, authored composition, and medium-specific craft.
- **Mindset Mode:** the same standard of judgment in service of somebody else's identity.
- **Typography:** resolved from the canonical [pitch.dog Type System](https://github.com/bomkino/pitchdog-type-system), verified and pinned per artifact; no copied font truth.
- **Digital:** Light and Dark are both authored, System is the initial default, and Phosphor is the Brand/unbranded icon family; accepted external icon authority stays intact.
- **Material:** tactility comes from real art, edges, crop, overlap, contact, marks, and evidence. Additive grain and noise are forbidden.
- **Website language:** quiet field, loud work, one strange little thing in each authored scene—relationships, not a homepage template.

The governing rule: **design with a spine, not a uniform.**

[![License: 0BSD](https://img.shields.io/badge/license-0BSD-111111.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/bomkino/pitchdog-design)](https://skills.sh/bomkino/pitchdog-design)

## Install in Codex or another compatible agent

Codex:

    npx skills add bomkino/pitchdog-design --skill pitchdog-design -g -a codex -y

Every agent supported by the skills CLI:

    npx skills add bomkino/pitchdog-design --skill pitchdog-design -g -a '*' -y

Update later:

    npx skills update pitchdog-design -g -y

Review community skills before installation. The distributed skill is deliberately text-only: no executable code, remote tool declaration, secret, telemetry, font binary, or image asset.

## Install the exact v2.0.0 archive

Codex, pinned to the release tag:

    npx skills add https://github.com/bomkino/pitchdog-design/tree/v2.0.0 --skill pitchdog-design -g -a codex -y

ChatGPT desktop:

1. Download [pitchdog-design.skill](https://github.com/bomkino/pitchdog-design/releases/download/v2.0.0/pitchdog-design.skill).
2. Open it with ChatGPT and complete its scan/install flow.

ChatGPT web/mobile:

1. Download [pitchdog-design.zip](https://github.com/bomkino/pitchdog-design/releases/download/v2.0.0/pitchdog-design.zip).
2. Open **Plugins → Skills → Create → Upload from your computer**.
3. Choose the archive and complete the scan/install flow.

Availability and upload permissions vary by product and workspace. Check OpenAI's current [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) guidance before installation.

The .skill and .zip assets contain the same deterministic bytes; only the filename differs for native desktop handling.

## Use

    Use $pitchdog-design to art-direct this pitch.dog landing page.

    Use $pitchdog-design in Mindset Mode for this client. Preserve its bright palette, type, and icon system.

    Use $pitchdog-design to review this drawer interaction. Diagnose only; do not change code.

The skill supports websites and Framer, products and internal tools, decks, documents, identities, print, invitations, social and video assets, motion contracts, design-system work, and artifact review.

## What lives where

- skills/pitchdog-design/SKILL.md — operating spine and branch router.
- skills/pitchdog-design/brand-profiles/pitchdog.yaml — machine-readable profile and authority locators.
- skills/pitchdog-design/references/ — branch-only design knowledge.
- skills/pitchdog-design/evals/evals.json — realistic behavioural cases; specifications are not execution claims.
- scripts/validate-skill.py — structural, privacy, authority, and package-boundary checks.
- scripts/package-skill.py — deterministic archive builder.
- docs/source-resolution.md — research authority and conflict decisions.
- docs/evaluation-report.md — evidence actually run for the current release.

## Validate and package

    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements-dev.txt
    .venv/bin/python scripts/validate-skill.py
    .venv/bin/python scripts/package-skill.py --output dist/pitchdog-design.zip

Structural validation cannot certify taste, accessibility conformance, browser behaviour, or owner acceptance. Those require the real artifact and are reported separately.

## Licence and boundaries

Repository and packaged-skill prose are released under [0BSD](LICENSE). The canonical type-system repository, third-party fonts, Phosphor Icons, marks, linked services, and source references retain their own terms. No font or third-party skill file is redistributed here.

See [NOTICE.md](NOTICE.md), [SECURITY.md](SECURITY.md), and [CONTRIBUTING.md](CONTRIBUTING.md).
