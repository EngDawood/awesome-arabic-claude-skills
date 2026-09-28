#!/usr/bin/env python3
"""
add_skill_from_issue.py - Parse a GitHub Issue submission and register it into sources.json
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT_DIR / "sources.json"


def extract_field(body: str, field_header: str) -> str:
    """Extract a field from GitHub Issue Form Markdown body."""
    pattern = rf"###\s+{re.escape(field_header)}\s*\n\s*(.*?)(?=\n###|\Z)"
    match = re.search(pattern, body, re.DOTALL)
    if match:
        val = match.group(1).strip()
        return val if val != "_No response_" else ""
    return ""


def main():
    issue_body = os.environ.get("ISSUE_BODY", "")
    if not issue_body:
        print("Error: ISSUE_BODY environment variable is empty.", file=sys.stderr)
        sys.exit(1)

    name = extract_field(issue_body, "Skill Name (اسم المهارة بالإنجليزية)")
    title_ar = extract_field(issue_body, "Skill Title in Arabic (عنوان المهارة بالعربية)")
    category = extract_field(issue_body, "Category (التصنيف)")
    url = extract_field(issue_body, "Repository / Skill URL (رابط المستودع أو المهارة)")
    description = extract_field(issue_body, "Description (الوصف)")
    install_cmd = extract_field(issue_body, "Install Command (أمر التثبيت الاختياري)")

    if not name or not url:
        print("Error: Required fields 'Skill Name' or 'URL' missing from issue body.", file=sys.stderr)
        sys.exit(1)

    # Sanitize name
    name = re.sub(r"[^a-z0-9-]", "-", name.lower()).strip("-")

    sources = []
    if SOURCES_FILE.exists():
        try:
            with open(SOURCES_FILE, "r", encoding="utf-8") as f:
                sources = json.load(f)
        except Exception:
            sources = []

    # Check for duplicates
    for s in sources:
        if s.get("name") == name or s.get("url") == url:
            print(f"Skill '{name}' or URL '{url}' is already in sources.json. Updating entry.")
            s["title_ar"] = title_ar or s.get("title_ar", name)
            s["category"] = category or s.get("category", "Community")
            s["description"] = description or s.get("description", "")
            s["url"] = url
            if install_cmd:
                s["install_cmd"] = install_cmd
            break
    else:
        new_entry = {
            "name": name,
            "title_ar": title_ar or name,
            "category": category or "Community",
            "description": description or "",
            "url": url,
            "install_cmd": install_cmd or f"npx skills add {url.replace('https://github.com/', '')}",
        }
        sources.append(new_entry)
        print(f"Added new skill '{name}' to sources.json.")

    with open(SOURCES_FILE, "w", encoding="utf-8") as f:
        json.dump(sources, f, ensure_ascii=False, indent=2)

    print("sources.json successfully updated.")


if __name__ == "__main__":
    main()
