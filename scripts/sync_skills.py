#!/usr/bin/env python3
"""
sync_skills.py - Auto-sync Arabic Claude Skills catalog and registry.
Validates SKILL.md frontmatter, merges local skills with sources.json,
writes skills.json registry, and updates the README.md table.
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
SOURCES_FILE = ROOT_DIR / "sources.json"
OUTPUT_REGISTRY = ROOT_DIR / "skills.json"
README_FILE = ROOT_DIR / "README.md"

TABLE_START_MARKER = "<!-- SKILLS_TABLE_START -->"
TABLE_END_MARKER = "<!-- SKILLS_TABLE_END -->"


def parse_frontmatter(file_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file without external dependencies."""
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}

    frontmatter_text = match.group(1)
    data = {}
    current_key = None

    for line in frontmatter_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if (val.startswith('"') and val.endswith('"')) or (
                val.startswith("'") and val.endswith("'")
            ):
                val = val[1:-1]
            data[key] = val
            current_key = key
        elif current_key:
            # Multi-line string continuation
            data[current_key] += " " + line

    return data


def validate_skill(skill: dict, file_path: Path) -> list:
    """Validate skill against Claude Code & Universal Skill standards."""
    errors = []
    name = skill.get("name")
    desc = skill.get("description")

    if not name:
        errors.append(f"Missing 'name' in frontmatter: {file_path}")
    elif not re.match(r"^[a-z0-9-]+$", name):
        errors.append(
            f"Invalid 'name' format '{name}' in {file_path}. Must use lowercase letters, numbers, and hyphens."
        )

    if not desc:
        errors.append(f"Missing 'description' in frontmatter: {file_path}")
    elif len(desc) > 1024:
        errors.append(
            f"Description for '{name}' exceeds 1024 characters ({len(desc)} chars)."
        )

    return errors


def collect_native_skills() -> tuple[list, list]:
    """Scan the skills/ directory for native SKILL.md files."""
    skills = []
    validation_errors = []

    if not SKILLS_DIR.exists():
        return skills, validation_errors

    for item in sorted(SKILLS_DIR.iterdir()):
        if item.is_dir():
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                fm = parse_frontmatter(skill_md)
                errs = validate_skill(fm, skill_md)
                if errs:
                    validation_errors.extend(errs)
                    continue

                name = fm.get("name", item.name)
                title_ar = fm.get("title_ar", name)
                category = fm.get("category", "General")
                desc = fm.get("description", "")

                skills.append(
                    {
                        "id": name,
                        "name": name,
                        "title_ar": title_ar,
                        "category": category,
                        "type": "native",
                        "description": desc,
                        "path": f"skills/{item.name}/SKILL.md",
                        "url": f"https://github.com/EngDawood/awesome-arabic-claude-skills/tree/main/skills/{item.name}",
                        "install_cmd": f"npx skills add EngDawood/awesome-arabic-claude-skills --skill {name}",
                    }
                )

    return skills, validation_errors


def collect_external_sources() -> list:
    """Load external curated skills from sources.json."""
    if not SOURCES_FILE.exists():
        return []

    try:
        with open(SOURCES_FILE, "r", encoding="utf-8") as f:
            sources = json.load(f)
            return [
                {
                    "id": item.get("name", "external-skill"),
                    "name": item.get("name", ""),
                    "title_ar": item.get("title_ar", item.get("name", "")),
                    "category": item.get("category", "External"),
                    "type": "external",
                    "description": item.get("description", ""),
                    "url": item.get("url", ""),
                    "install_cmd": item.get("install_cmd", f"npx skills add {item.get('name')}"),
                }
                for item in sources
            ]
    except Exception as e:
        print(f"Warning: Failed to parse sources.json: {e}", file=sys.stderr)
        return []


def generate_markdown_table(skills: list) -> str:
    """Generate a clean GitHub-Flavored Markdown table for README.md."""
    lines = [
        "| المهارة (Skill) | التصنيف (Category) | الوصف (Description) | التثبيت والاستخدام (Install / Link) |",
        "| :--- | :--- | :--- | :--- |",
    ]

    for s in skills:
        badge = "*(مدمجة / Native)*" if s["type"] == "native" else "*(خارجية / External)*"
        name_cell = f"**[{s['name']}]({s['url']})**<br>{s['title_ar']} {badge}"
        cat_cell = f"`{s['category']}`"
        desc_cell = s["description"]
        cmd_cell = f"`{s['install_cmd']}`" if s.get("install_cmd") else f"[عرض المستودع]({s['url']})"
        lines.append(f"| {name_cell} | {cat_cell} | {desc_cell} | {cmd_cell} |")

    return "\n".join(lines)


def update_readme(table_markdown: str):
    """Replace content between markers in README.md."""
    if not README_FILE.exists():
        return

    content = README_FILE.read_text(encoding="utf-8")
    pattern = rf"({re.escape(TABLE_START_MARKER)})(.*?)({re.escape(TABLE_END_MARKER)})"

    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(
            pattern,
            f"\\1\n\n{table_markdown}\n\n\\3",
            content,
            flags=re.DOTALL,
        )
        README_FILE.write_text(new_content, encoding="utf-8")
        print("Updated README.md skills catalog table.")
    else:
        print("Markers not found in README.md; skipping table injection.")


def main():
    print("Starting Arabic Claude Skills auto-sync...")

    native_skills, errors = collect_native_skills()
    if errors:
        print("Validation errors encountered:")
        for err in errors:
            print(f" - {err}", file=sys.stderr)
        sys.exit(1)

    external_skills = collect_external_sources()
    all_skills = native_skills + external_skills

    print(
        f"Found {len(native_skills)} native skills and {len(external_skills)} external skills. Total: {len(all_skills)}"
    )

    # 1. Output skills.json
    registry_data = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "name": "awesome-arabic-claude-skills",
        "description": "Curated directory and registry of Arabic skills for Claude Code and AI agents",
        "total_skills": len(all_skills),
        "native_skills_count": len(native_skills),
        "external_skills_count": len(external_skills),
        "skills": all_skills,
    }

    with open(OUTPUT_REGISTRY, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, ensure_ascii=False, indent=2)
    print(f"Generated {OUTPUT_REGISTRY.relative_to(ROOT_DIR)}")

    # 2. Update README table
    table_md = generate_markdown_table(all_skills)
    update_readme(table_md)

    print("Auto-sync completed successfully!")


if __name__ == "__main__":
    main()
