#!/usr/bin/env python3
"""Validate the portable pitchdog-design Agent Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install requirements-dev.txt.", file=sys.stderr)
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "pitchdog-design"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


required_files = {
    "SKILL.md",
    "LICENSE",
    "NOTICE.md",
    "agents/openai.yaml",
    "brand-profiles/pitchdog.yaml",
    "evals/evals.json",
    "references/actual-goal-and-soul.md",
    "references/profile-routing.md",
    "references/pitchdog-brand-foundation.md",
    "references/typography-authority.md",
    "references/digital-theme-and-icons.md",
    "references/design-system-governance.md",
    "references/website-design-language.md",
    "references/colour-and-material.md",
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
}

for relative in sorted(required_files):
    require((SKILL / relative).is_file(), f"missing required file: {relative}")

actual_files = {
    path.relative_to(SKILL).as_posix()
    for path in SKILL.rglob("*")
    if path.is_file() or path.is_symlink()
}
for relative in sorted(actual_files - required_files):
    ERRORS.append(f"unapproved package file: {relative}")
for relative in sorted(required_files - actual_files):
    ERRORS.append(f"required file absent from package set: {relative}")

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
        require(
            isinstance(name, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None,
            "invalid skill name",
        )
        require(
            isinstance(description, str) and 120 <= len(description) <= 1024,
            "description must explain scope and triggers in 120-1024 characters",
        )
        require("$pitchdog-design" in str(description), "description must include explicit invocation")
        for trigger in ("pitch.dog", "external", "review", "system"):
            require(trigger.lower() in str(description).lower(), f"description lacks trigger branch: {trigger}")

require(len(skill_text.splitlines()) < 500, "SKILL.md must remain under 500 lines")
require(SKILL.name == "pitchdog-design", "skill folder must match frontmatter name")

markdown_files = [
    path
    for path in ROOT.rglob("*.md")
    if ".git" not in path.parts and "dist" not in path.parts and ".venv" not in path.parts
]
link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in markdown_files:
    text = markdown.read_text(encoding="utf-8")
    for target in link_pattern.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        resolved = (markdown.parent / unquote(target)).resolve()
        require(resolved.exists(), f"broken local link in {markdown.relative_to(ROOT)}: {target}")

private_path_patterns = {
    "/" + "Users/": "macOS user path",
    "/" + "Volumes/": "mounted-volume path",
    "file" + "://": "local file URL",
}
for path in ROOT.rglob("*"):
    if (
        not path.is_file()
        or ".git" in path.parts
        or "dist" in path.parts
        or ".venv" in path.parts
    ):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    if path.resolve() != Path(__file__).resolve():
        placeholder_pattern = re.compile(r"\[(?:TO" + r"DO|TB" + r"D)\]|\bTB" + r"D\b", re.IGNORECASE)
        require(placeholder_pattern.search(text) is None, f"placeholder marker in {path.relative_to(ROOT)}")
    for pattern, label in private_path_patterns.items():
        require(pattern not in text, f"{label} in {path.relative_to(ROOT)}")

openai = yaml.safe_load((SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8"))
interface = openai.get("interface", {}) if isinstance(openai, dict) else {}
require(interface.get("display_name") == "pitch.dog Design", "openai display_name mismatch")
short_description = interface.get("short_description", "")
require(25 <= len(short_description) <= 64, "openai short_description must be 25-64 characters")
require("$pitchdog-design" in interface.get("default_prompt", ""), "openai default_prompt must mention $pitchdog-design")

profile_path = SKILL / "brand-profiles" / "pitchdog.yaml"
profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
require(profile.get("profile", {}).get("version") == "2.0.0", "profile version must be 2.0.0")
require(
    profile.get("typography", {}).get("authority_repository") == "https://github.com/bomkino/pitchdog-type-system",
    "typography authority repository mismatch",
)
require(
    profile.get("digital", {}).get("theme", {}).get("choices") == ["system", "light", "dark"],
    "theme choices must be system, light, dark",
)
require(profile.get("digital", {}).get("theme", {}).get("default") == "system", "theme default must be system")
require(profile.get("digital", {}).get("icons", {}).get("family") == "Phosphor Icons", "icon family must be Phosphor Icons")
require(
    profile.get("digital", {}).get("icons", {}).get("minimum_target_css_px", 0) >= 44,
    "minimum icon-control target must be at least 44 CSS px",
)
require(
    profile.get("digital", {}).get("icons", {}).get("destructive_action", "").startswith("never-icon-alone"),
    "destructive actions must never rely on an icon alone",
)
require(
    profile.get("design_language", {}).get("governing_sentence") == "Quiet field. Loud work. One strange little thing.",
    "website design-language sentence mismatch",
)
require(
    profile.get("design_language", {}).get("cadence", {}).get("scope")
    == "authored editorial scenes, not dense task surfaces",
    "editorial scene cadence must not govern dense task surfaces",
)

def profile_references(value: object, prefix: str = "") -> list[tuple[str, object]]:
    found: list[tuple[str, object]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            dotted = f"{prefix}.{key}" if prefix else str(key)
            if str(key).endswith("_reference"):
                found.append((dotted, child))
            found.extend(profile_references(child, dotted))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(profile_references(child, f"{prefix}[{index}]"))
    return found


references = profile_references(profile)
require(len(references) == 10, "profile must expose exactly ten branch authority references")
for dotted, target in references:
    require(isinstance(target, str), f"invalid profile reference: {dotted}")
    if isinstance(target, str):
        require((profile_path.parent / target).resolve().is_file(), f"broken profile reference {dotted}: {target}")

package_text = "\n".join(
    path.read_text(encoding="utf-8")
    for path in SKILL.rglob("*")
    if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json"}
)
for stale in ("Neco", "Erode", "Geist Mono", "Geist Sans", "color(display-p3", "v13.1.0"):
    require(stale not in package_text, f"stale or duplicated typography/colour authority in skill: {stale}")

material_text = (SKILL / "references" / "colour-and-material.md").read_text(encoding="utf-8")
for guard in ("Never add grain", "SVG turbulence", "Preserve texture already intrinsic to approved source art"):
    require(guard in material_text, f"material boundary missing: {guard}")

type_text = (SKILL / "references" / "typography-authority.md").read_text(encoding="utf-8")
for guard in (
    "bomkino/pitchdog-type-system",
    "Cross-check that version",
    "matching Git tag",
    "Do not resolve through `main`",
    "Record the resolved tag and commit",
):
    require(guard in type_text, f"typography resolver missing: {guard}")

digital_text = (SKILL / "references" / "digital-theme-and-icons.md").read_text(encoding="utf-8")
for guard in (
    "`System` — the initial default",
    "prefers-color-scheme",
    "currentColor",
    "@phosphor-icons/react",
    "Interactive controls use the active resolved icon family",
    "provisional system choice until owner acceptance",
    "an icon and accessible name alone are insufficient",
):
    require(guard in digital_text, f"digital contract missing: {guard}")
require("Interactive icon controls use Phosphor" not in digital_text, "external icon authority is contradicted")

external_text = (SKILL / "references" / "external-brand-adapter.md").read_text(encoding="utf-8")
for guard in (
    "label the derived state provisional until owner acceptance",
    "Phosphor is a provisional system choice until owner acceptance",
):
    require(guard in external_text, f"external-brand authority boundary missing: {guard}")

system_text = (SKILL / "references" / "design-system-governance.md").read_text(encoding="utf-8")
require("two representative real uses" in system_text, "component extraction must require two real uses")

motion_text = (SKILL / "references" / "motion-and-interaction.md").read_text(encoding="utf-8")
for forbidden in ("Brand starting values", "--pd-ease-", "--pd-spatial-panel"):
    require(forbidden not in motion_text, f"ungoverned global motion token: {forbidden}")

evals = json.loads((SKILL / "evals" / "evals.json").read_text(encoding="utf-8"))
cases = evals.get("cases", [])
required_eval_ids = {
    "brand-website-v12-language",
    "existing-type-pin",
    "type-authority-conflict",
    "light-dark-system-contract",
    "phosphor-icon-governance",
    "external-brand-no-contamination",
    "no-additive-texture",
    "phone-authorship",
    "review-diagnose-only",
}
ids = [case.get("id") for case in cases]
require(required_eval_ids.issubset(set(ids)), "eval suite lacks a required discriminating case")
require(len(ids) == len(set(ids)), "eval IDs must be unique")
for case in cases:
    case_id = case.get("id", "<missing>")
    for field in ("id", "prompt", "expected_profile", "must", "must_not", "failure_caught"):
        require(bool(case.get(field)), f"eval {case_id} lacks {field}")
    require("$pitchdog-design" in str(case.get("prompt", "")), f"eval {case_id} must invoke the skill")
    require(isinstance(case.get("must"), list), f"eval {case_id} must field must be a list")
    require(isinstance(case.get("must_not"), list), f"eval {case_id} must_not field must be a list")

for path in SKILL.rglob("*"):
    require(not path.is_symlink(), f"symlink not allowed in portable skill: {path.relative_to(SKILL)}")
    if path.is_file():
        data = path.read_bytes()
        require(b"\0" not in data, f"NUL byte in text-only package file: {path.relative_to(SKILL)}")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            ERRORS.append(f"non-UTF-8 file in text-only package: {path.relative_to(SKILL)}")

require(not (SKILL / "scripts").exists(), "published skill must remain text-only")
require((ROOT / "LICENSE").read_bytes() == (SKILL / "LICENSE").read_bytes(), "root and skill licences must match")
package_size = sum(path.stat().st_size for path in SKILL.rglob("*") if path.is_file())
require(package_size < 1_000_000, "skill package must stay below 1 MB")

if ERRORS:
    print("FAIL")
    for error in ERRORS:
        print(f"- {error}")
    raise SystemExit(1)

print(
    f"PASS: {len(required_files)} required files, {len(cases)} discriminating eval specifications, "
    f"{len(markdown_files)} Markdown files, {len(skill_text.splitlines())} SKILL.md lines"
)
