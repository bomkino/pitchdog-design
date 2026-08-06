#!/usr/bin/env python3
"""Deterministically validate the pitchdog-design Agent Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install PyYAML==6.0.2.", file=sys.stderr)
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "pitchdog-design"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


required_files = [
    "SKILL.md",
    "LICENSE",
    "NOTICE.md",
    "agents/openai.yaml",
    "brand-profiles/pitchdog.yaml",
    "evals/evals.json",
    "references/actual-goal-and-soul.md",
    "references/profile-routing.md",
    "references/pitchdog-brand-foundation.md",
    "references/colour-p3-and-alpha.md",
    "references/spacing-grid-and-sizing.md",
    "references/web-framer-and-responsive.md",
    "references/motion-and-interaction.md",
    "references/responsive-accessibility-performance.md",
    "references/external-brand-adapter.md",
    "references/non-web-adapters.md",
    "references/anti-patterns.md",
    "references/artifact-review.md",
    "references/examples-and-calibration.md",
    "templates/design-brief.md",
    "templates/brand-profile.yaml",
    "templates/motion-contract.md",
    "templates/artifact-review.md",
]

for relative in required_files:
    require((SKILL / relative).is_file(), f"missing required file: {relative}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
require(frontmatter_match is not None, "SKILL.md must start with YAML frontmatter")

if frontmatter_match:
    metadata = yaml.safe_load(frontmatter_match.group(1))
    require(isinstance(metadata, dict), "SKILL.md frontmatter must be a mapping")
    if isinstance(metadata, dict):
        require(set(metadata) == {"name", "description"}, "SKILL.md frontmatter must contain only name and description")
        name = metadata.get("name")
        description = metadata.get("description")
        require(name == "pitchdog-design", "frontmatter name must be pitchdog-design")
        require(isinstance(name, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None, "invalid skill name")
        require(isinstance(description, str) and 120 <= len(description) <= 1024, "description must be informative and 120–1024 characters")
        require("$pitchdog-design" in description, "description must include explicit invocation")

require(len(skill_text.splitlines()) < 500, "SKILL.md must remain under 500 lines")
require(SKILL.name == "pitchdog-design", "skill folder must match frontmatter name")

markdown_files = list(SKILL.rglob("*.md")) + [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "NOTICE.md"]
link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in markdown_files:
    text = markdown.read_text(encoding="utf-8")
    for target in link_pattern.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        resolved = (markdown.parent / unquote(target)).resolve()
        require(resolved.exists(), f"broken local link in {markdown.relative_to(ROOT)}: {target}")

for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "NOTICE.md", *SKILL.rglob("*")]:
    if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".json"}:
        continue
    text = path.read_text(encoding="utf-8")
    require(re.search(r"\[(?:TODO|TBD)\]|\bTBD\b", text, re.IGNORECASE) is None, f"placeholder marker in {path.relative_to(ROOT)}")
    require("/Users/" not in text, f"private absolute path in {path.relative_to(ROOT)}")

openai = yaml.safe_load((SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8"))
interface = openai.get("interface", {}) if isinstance(openai, dict) else {}
require(interface.get("display_name") == "pitch.dog Design", "openai display_name mismatch")
short_description = interface.get("short_description", "")
require(25 <= len(short_description) <= 64, "openai short_description must be 25–64 characters")
require("$pitchdog-design" in interface.get("default_prompt", ""), "openai default_prompt must mention $pitchdog-design")

profile = yaml.safe_load((SKILL / "brand-profiles" / "pitchdog.yaml").read_text(encoding="utf-8"))
opaque = profile.get("colour", {}).get("opaque", {})
required_colours = {
    "paper_neutral", "paper_powder", "paper_lilac", "paper_mint", "paper_blush",
    "sheet", "ink", "muted_ink", "ink_room", "blue_black", "panel_dark",
    "dark_lilac", "dark_mint", "dark_blush", "light_ink", "muted_light_ink",
    "signal_vermilion", "signal_cobalt", "signal_cobalt_dark",
}
require(set(opaque) == required_colours, "canonical opaque colour set is incomplete or changed")
for name, token in opaque.items():
    require(isinstance(token, dict), f"colour {name} must be a mapping")
    if isinstance(token, dict):
        require(re.fullmatch(r"color\(display-p3(?:\s+\d+(?:\.\d+)?){3}\)", str(token.get("p3", ""))) is not None, f"invalid P3 value for {name}")
        require(re.fullmatch(r"#[0-9A-F]{6}", str(token.get("srgb", ""))) is not None, f"invalid sRGB fallback for {name}")

evals = json.loads((SKILL / "evals" / "evals.json").read_text(encoding="utf-8"))
cases = evals.get("cases", [])
require(len(cases) >= 24, "eval suite must contain at least 24 cases")
ids = [case.get("id") for case in cases]
require(len(ids) == len(set(ids)), "eval IDs must be unique")
for case in cases:
    for field in ("id", "prompt", "expected_profile", "must", "must_not", "failure_caught"):
        require(bool(case.get(field)), f"eval {case.get('id', '<missing>')} lacks {field}")

for path in SKILL.rglob("*"):
    require(not path.is_symlink(), f"symlink not allowed in portable skill: {path.relative_to(SKILL)}")
    if path.is_file():
        require(path.suffix.lower() not in {".ttf", ".otf", ".woff", ".woff2", ".eot", ".exe", ".dylib", ".so"}, f"forbidden binary: {path.relative_to(SKILL)}")

require(not (SKILL / "scripts").exists(), "published skill must remain text-only")
require((ROOT / "LICENSE").read_bytes() == (SKILL / "LICENSE").read_bytes(), "root and skill licences must match")
require(sum(path.stat().st_size for path in SKILL.rglob("*") if path.is_file()) < 1_000_000, "skill package must stay below 1 MB")

if ERRORS:
    print("FAIL")
    for error in ERRORS:
        print(f"- {error}")
    raise SystemExit(1)

print(f"PASS: {len(required_files)} required files, {len(cases)} evals, {len(opaque)} colour pairs, {len(skill_text.splitlines())} SKILL.md lines")
