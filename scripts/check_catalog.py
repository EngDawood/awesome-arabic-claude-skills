#!/usr/bin/env python3
"""
check_catalog.py - Offline PR checks for the skills catalog.
Never touches the network, so results depend only on the files in the PR.
"""

import json
import re
import sys

import sync_skills as m


def readme_block(content: str, start: str, end: str) -> str:
    match = re.search(rf"{re.escape(start)}(.*?){re.escape(end)}", content, re.DOTALL)
    return match.group(1).strip() if match else ""


def main() -> int:
    errors = []

    # 1. sources.json must be strict, valid JSON
    sources = []
    try:
        sources = json.loads(m.SOURCES_FILE.read_text(encoding="utf-8"))
        if not isinstance(sources, list):
            errors.append("sources.json must be a JSON array.")
            sources = []
    except Exception as e:
        errors.append(f"sources.json is not valid JSON: {e}")
    for i, item in enumerate(sources):
        if not isinstance(item, dict) or not (item.get("repo") or item.get("url")):
            errors.append(f"sources.json entry #{i + 1} needs a 'repo' (or 'url').")

    # 2. every skills/<folder>/SKILL.md must have valid frontmatter
    folders = set()
    for item in sorted(m.SKILLS_DIR.iterdir()) if m.SKILLS_DIR.exists() else []:
        if not item.is_dir():
            continue
        skill_md = item / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"skills/{item.name} has no SKILL.md.")
            continue
        folders.add(item.name)
        errors.extend(m.validate_skill(m.parse_frontmatter(skill_md), skill_md))

    # 3. skills.json must list exactly the skills and commands on disk
    try:
        registry = json.loads(m.OUTPUT_REGISTRY.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"skills.json is not valid JSON: {e}")
        registry = None

    if registry is not None:
        listed = {s["path"].split("/")[1] for s in registry.get("skills", [])}
        for name in sorted(folders - listed):
            errors.append(f"skills/{name} is missing from skills.json. Run 'python scripts/sync_skills.py'.")
        for name in sorted(listed - folders):
            errors.append(f"skills.json lists '{name}' but skills/{name} does not exist.")
        if registry.get("total_skills") != len(registry.get("skills", [])):
            errors.append("skills.json 'total_skills' does not match the number of skills.")
        if registry.get("commands") != m.collect_commands():
            errors.append("skills.json 'commands' is out of date. Run 'python scripts/sync_skills.py'.")

        # 4. README tables must match skills.json
        for readme, lang in ((m.README_FILE, "ar"), (m.README_EN_FILE, "en")):
            if not readme.exists():
                errors.append(f"{readme.name} is missing.")
                continue
            content = readme.read_text(encoding="utf-8")
            expected = {
                "skills": m.generate_markdown_table(registry.get("skills", []), lang).strip(),
                "commands": m.generate_commands_table(registry.get("commands", []), lang).strip(),
            }
            actual = {
                "skills": readme_block(content, m.TABLE_START_MARKER, m.TABLE_END_MARKER),
                "commands": readme_block(content, m.COMMANDS_START_MARKER, m.COMMANDS_END_MARKER),
            }
            for key in expected:
                if expected[key] != actual[key]:
                    errors.append(f"{readme.name} {key} table is out of sync with skills.json.")

    if errors:
        for err in errors:
            print(f"::error::{err}")
        return 1
    print(f"All checks passed ({len(folders)} skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
