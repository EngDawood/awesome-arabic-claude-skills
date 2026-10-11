#!/usr/bin/env python3
"""
add_source.py - Add or update one upstream skill entry in sources.json.
Inputs come from environment variables: REPO (required), DIR, NAME, TITLE_AR, CATEGORY.
"""

import json
import os
import re
import sys
from pathlib import Path

SOURCES_FILE = Path(__file__).resolve().parent.parent / "sources.json"

REPO_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+(/tree/[A-Za-z0-9._-]+(/[A-Za-z0-9._/-]*)?)?$")
DIR_RE = re.compile(r"^[A-Za-z0-9._/-]*$")


def main() -> int:
    repo = re.sub(r"^https?://github\.com/", "", os.environ.get("REPO", "").strip()).strip("/")
    repo = re.sub(r"\.git$", "", repo)
    dir_ = os.environ.get("DIR", "").strip()

    if not REPO_RE.match(repo):
        print(f"Error: '{repo}' is not a valid GitHub repo (use owner/repo).", file=sys.stderr)
        return 1
    if not DIR_RE.match(dir_) or ".." in dir_.split("/"):
        print(f"Error: invalid dir '{dir_}'.", file=sys.stderr)
        return 1

    entry = {"repo": repo}
    if dir_:
        entry["dir"] = dir_
    for key, env in (("name", "NAME"), ("title_ar", "TITLE_AR"), ("category", "CATEGORY")):
        value = os.environ.get(env, "").strip()
        if value:
            entry[key] = value

    sources = json.loads(SOURCES_FILE.read_text(encoding="utf-8")) if SOURCES_FILE.exists() else []

    for existing in sources:
        if existing.get("repo") == repo and existing.get("dir", "") == dir_:
            existing.update(entry)
            print(f"Updated existing entry for {repo} {dir_}".strip())
            break
    else:
        sources.append(entry)
        print(f"Added {repo} {dir_}".strip())

    SOURCES_FILE.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
