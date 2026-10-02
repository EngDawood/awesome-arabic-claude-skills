#!/usr/bin/env python3
"""
sync_skills.py - Auto-sync Arabic Claude Skills catalog, registry, and commands.
Pulls synced skills and commands from upstream GitHub repositories,
validates SKILL.md frontmatter, writes skills.json registry, and updates README.md tables.
"""

import io
import json
import os
import re
import sys
import tarfile
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
COMMANDS_DIR = ROOT_DIR / "commands"
SOURCES_FILE = ROOT_DIR / "sources.json"
OUTPUT_REGISTRY = ROOT_DIR / "skills.json"
README_FILE = ROOT_DIR / "README.md"

TABLE_START_MARKER = "<!-- SKILLS_TABLE_START -->"
TABLE_END_MARKER = "<!-- SKILLS_TABLE_END -->"
COMMANDS_START_MARKER = "<!-- COMMANDS_TABLE_START -->"
COMMANDS_END_MARKER = "<!-- COMMANDS_TABLE_END -->"


def parse_frontmatter_text(content: str) -> dict:
    """Extract YAML frontmatter from markdown content without external dependencies."""
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
            data[current_key] += " " + line

    return data


def parse_frontmatter(file_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file without external dependencies."""
    content = file_path.read_text(encoding="utf-8")
    return parse_frontmatter_text(content)


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


def extract_tar_folder(tar: tarfile.TarFile, root_prefix: str, source_rel: str, dest_dir: Path) -> int:
    """Extract a subfolder from tar archive into destination directory."""
    full_source = (
        f"{root_prefix}/{source_rel.strip('/')}".rstrip("/")
        if source_rel.strip("/")
        else root_prefix
    )
    dest_dir.mkdir(parents=True, exist_ok=True)
    synced_count = 0

    for member in tar.getmembers():
        if member.name == full_source or member.name.startswith(full_source + "/"):
            rel_subpath = member.name[len(full_source) :].lstrip("/")
            if not rel_subpath:
                continue

            target_file = dest_dir / rel_subpath
            if member.isdir():
                target_file.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target_file.parent.mkdir(parents=True, exist_ok=True)
                fileobj = tar.extractfile(member)
                if fileobj:
                    target_file.write_bytes(fileobj.read())
                    synced_count += 1

    return synced_count


def sync_external_repositories(sources: list) -> dict:
    """Sync skills and commands from upstream GitHub repositories.
    Supports:
    - Smart format: {"repo": "owner/repo", "dir": "skills/"}
    - Specific skill: {"repo": "owner/repo", "dir": "skills/my-skill"}
    - Explicit format: {"repo": "...", "source_path": "...", "target_path": "..."}
    Returns a dict mapping folder name in skills/ to metadata.
    """
    synced_meta = {}

    for item in sources:
        raw_repo = item.get("repo") or item.get("url") or ""
        if not raw_repo:
            continue

        raw_repo = re.sub(r"^https?://github\.com/", "", raw_repo).strip("/")
        repo_match = re.match(r"^([^/]+/[^/]+)(?:/tree/([^/]+)(?:/(.*))?)?", raw_repo)
        if repo_match:
            repo = repo_match.group(1)
            branch = item.get("branch") or repo_match.group(2) or "main"
            url_subpath = repo_match.group(3) or ""
        else:
            repo = raw_repo
            branch = item.get("branch", "main")
            url_subpath = ""

        dir_spec = item.get("dir")
        if dir_spec is None:
            dir_spec = item.get("source_path", url_subpath)

        dir_spec_str = dir_spec.strip() if dir_spec else ""
        is_directory_mode = dir_spec_str.endswith("/") or dir_spec_str == "skills"

        print(f"Syncing from GitHub: {repo}@{branch} (dir: '{dir_spec_str}')...")
        archive_url = f"https://github.com/{repo}/archive/refs/heads/{branch}.tar.gz"

        try:
            req = urllib.request.Request(
                archive_url, headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status != 200:
                    print(
                        f"Warning: HTTP {resp.status} fetching {archive_url}",
                        file=sys.stderr,
                    )
                    continue

                data = io.BytesIO(resp.read())
                with tarfile.open(fileobj=data, mode="r:gz") as tar:
                    members = tar.getmembers()
                    root_prefix = members[0].name.split("/")[0] if members else ""
                    if not root_prefix:
                        continue

                    # 1. Discover all SKILL.md files in the tarball
                    all_skill_files = []
                    for m in members:
                        if m.isfile() and (m.name == f"{root_prefix}/SKILL.md" or m.name.endswith("/SKILL.md")):
                            rel_skill = m.name[len(root_prefix) :].lstrip("/")
                            all_skill_files.append((m, rel_skill))

                    clean_dir_spec = dir_spec_str.strip("/")

                    skills_to_extract = []
                    for member, rel_skill in all_skill_files:
                        skill_folder_rel = str(Path(rel_skill).parent).replace("\\", "/")
                        if skill_folder_rel == ".":
                            skill_folder_rel = ""

                        matches = False
                        if not clean_dir_spec:
                            if skill_folder_rel == "":
                                matches = True
                            elif not any(r == "SKILL.md" for _, r in all_skill_files):
                                matches = True
                        elif is_directory_mode:
                            if skill_folder_rel == clean_dir_spec or skill_folder_rel.startswith(clean_dir_spec + "/"):
                                matches = True
                        else:
                            if skill_folder_rel == clean_dir_spec:
                                matches = True

                        if matches:
                            skills_to_extract.append((member, skill_folder_rel))

                    # Fallback if no SKILL.md found by pattern but dir_spec was given
                    if not skills_to_extract and clean_dir_spec:
                        skills_to_extract.append((None, clean_dir_spec))

                    # 2. Extract each matched skill
                    for skill_md_member, source_rel in skills_to_extract:
                        fm = {}
                        if skill_md_member:
                            f = tar.extractfile(skill_md_member)
                            if f:
                                fm = parse_frontmatter_text(f.read().decode("utf-8", errors="replace"))

                        if len(skills_to_extract) == 1 and item.get("name"):
                            skill_name = item.get("name")
                        else:
                            skill_name = fm.get("name") or Path(source_rel).name or repo.split("/")[1]

                        skill_name = re.sub(r"[^a-z0-9-]", "-", skill_name.lower()).strip("-")

                        if len(skills_to_extract) == 1 and item.get("target_path"):
                            target_rel = item.get("target_path")
                        else:
                            target_rel = f"skills/{skill_name}"

                        dest_skill_dir = ROOT_DIR / target_rel
                        count = extract_tar_folder(tar, root_prefix, source_rel, dest_skill_dir)
                        print(f" - Synced skill '{skill_name}' ({count} files) to {target_rel}")

                        skill_url = item.get("url") or (
                            f"https://github.com/{repo}"
                            if not source_rel
                            else f"https://github.com/{repo}/tree/{branch}/{source_rel}"
                        )
                        install_cmd = item.get("install_cmd") or (
                            f"npx skills add {repo}"
                            if not source_rel
                            else f"npx skills add {repo} --skill {skill_name}"
                        )

                        folder_target_name = Path(target_rel).name
                        synced_meta[folder_target_name] = {
                            "name": skill_name,
                            "title_ar": item.get("title_ar") or fm.get("title_ar", skill_name),
                            "category": item.get("category") or fm.get("category", "General"),
                            "type": item.get("type", "synced"),
                            "upstream_repo": repo,
                            "description": fm.get("description", ""),
                            "url": skill_url,
                            "install_cmd": install_cmd,
                            "target_path": target_rel,
                        }

                    # 3. Sync commands if present in repo
                    commands_source = item.get("commands_source", "commands").strip("/")
                    commands_target = item.get("commands_target", "commands").strip("/")
                    has_commands = any(
                        m.name.startswith(f"{root_prefix}/{commands_source}/") for m in members
                    )
                    if has_commands and commands_target:
                        dest_cmd_dir = ROOT_DIR / commands_target
                        cmd_count = extract_tar_folder(tar, root_prefix, commands_source, dest_cmd_dir)
                        if cmd_count > 0:
                            print(f" - Synced {cmd_count} command files to {commands_target}")

        except Exception as e:
            print(
                f"Warning: Failed to sync from GitHub {repo} ({e}). Preserving local files.",
                file=sys.stderr,
            )

    return synced_meta


def load_sources() -> list:
    """Load configuration from sources.json, tolerating trailing commas and comments."""
    if not SOURCES_FILE.exists():
        return []
    try:
        content = SOURCES_FILE.read_text(encoding="utf-8")
        # Strip single-line comments
        content = re.sub(r"^\s*//.*$", "", content, flags=re.MULTILINE)
        # Strip trailing commas in objects and arrays
        content = re.sub(r",\s*([\]}])", r"\1", content)
        return json.loads(content)
    except Exception as e:
        print(f"Warning: Failed to load sources.json: {e}", file=sys.stderr)
        return []


def collect_native_skills(sources: list, synced_meta: dict = None) -> tuple[list, list]:
    """Scan the skills/ directory for native SKILL.md files."""
    skills = []
    validation_errors = []

    if synced_meta is None:
        synced_meta = {}

    sources_map = {}
    for s in sources:
        target_path = s.get("target_path") or (f"skills/{s.get('name')}" if s.get("name") else None)
        if target_path:
            norm_target = Path(target_path).name
            sources_map[norm_target] = s

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

                folder_name = item.name
                is_synced = (folder_name in synced_meta) or (folder_name in sources_map)
                source_info = synced_meta.get(folder_name) or sources_map.get(folder_name, {})

                name = source_info.get("name") or folder_name
                title_ar = source_info.get("title_ar") or fm.get("title_ar", name)
                category = source_info.get("category") or fm.get("category", "General")
                desc = fm.get("description", "") or source_info.get("description", "")
                skill_type = source_info.get("type", "synced" if is_synced else "native")
                upstream_repo = source_info.get("upstream_repo") or source_info.get("repo")
                url = (
                    source_info.get("url")
                    if is_synced and source_info.get("url")
                    else f"https://github.com/EngDawood/awesome-arabic-claude-skills/tree/main/skills/{folder_name}"
                )
                install_cmd = (
                    source_info.get("install_cmd")
                    if is_synced and source_info.get("install_cmd")
                    else f"npx skills add EngDawood/awesome-arabic-claude-skills --skill {name}"
                )

                skills.append(
                    {
                        "id": name,
                        "name": name,
                        "title_ar": title_ar,
                        "category": category,
                        "type": skill_type,
                        "upstream_repo": upstream_repo,
                        "description": desc,
                        "path": f"skills/{folder_name}/SKILL.md",
                        "url": url,
                        "install_cmd": install_cmd,
                    }
                )

    return skills, validation_errors


def collect_commands() -> list:
    """Scan commands/ directory for Claude Code slash commands."""
    commands = []
    if not COMMANDS_DIR.exists():
        return commands

    for item in sorted(COMMANDS_DIR.iterdir()):
        if item.is_file() and item.suffix == ".md":
            fm = parse_frontmatter(item)
            cmd_name = f"/{item.stem}"
            desc = fm.get("description", "")
            arg = fm.get("argument", "")
            commands.append(
                {
                    "command": cmd_name,
                    "description": desc,
                    "argument": arg,
                    "path": f"commands/{item.name}",
                }
            )
    return commands


def generate_markdown_table(skills: list) -> str:
    """Generate a clean GitHub-Flavored Markdown table for skills."""
    lines = [
        "| المهارة (Skill) | التصنيف (Category) | الوصف (Description) | التثبيت والاستخدام (Install / Link) |",
        "| :--- | :--- | :--- | :--- |",
    ]

    for s in skills:
        if s["type"] == "synced":
            badge = f"*(مزامنة من GitHub / Synced)*"
        elif s["type"] == "native":
            badge = "*(مدمجة / Native)*"
        else:
            badge = "*(خارجية / External)*"

        name_cell = f"**[{s['name']}]({s['url']})**<br>{s['title_ar']} {badge}"
        cat_cell = f"`{s['category']}`"
        desc_cell = s["description"]
        cmd_cell = (
            f"`{s['install_cmd']}`"
            if s.get("install_cmd")
            else f"[عرض المستودع]({s['url']})"
        )
        lines.append(f"| {name_cell} | {cat_cell} | {desc_cell} | {cmd_cell} |")

    return "\n".join(lines)


def generate_commands_table(commands: list) -> str:
    """Generate a markdown table for Claude Code slash commands."""
    if not commands:
        return "*لا توجد أوامر مخصصة حالياً.*"

    lines = [
        "| الأمر (Slash Command) | المعاملات (Arguments) | الوصف (Description) | ملف الأمر (File) |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for c in commands:
        cmd_cell = f"`{c['command']}`"
        arg_cell = f"`{c['argument']}`" if c.get("argument") else "—"
        desc_cell = c["description"]
        file_cell = f"[`{c['path']}`]({c['path']})"
        lines.append(f"| {cmd_cell} | {arg_cell} | {desc_cell} | {file_cell} |")
    return "\n".join(lines)


def update_readme(skills_table_md: str, commands_table_md: str):
    """Replace content between markers in README.md."""
    if not README_FILE.exists():
        return

    content = README_FILE.read_text(encoding="utf-8")

    # Update skills table
    skills_pattern = (
        rf"({re.escape(TABLE_START_MARKER)})(.*?)({re.escape(TABLE_END_MARKER)})"
    )
    if re.search(skills_pattern, content, re.DOTALL):
        content = re.sub(
            skills_pattern,
            f"\\1\n\n{skills_table_md}\n\n\\3",
            content,
            flags=re.DOTALL,
        )

    # Update commands table if markers present
    cmd_pattern = (
        rf"({re.escape(COMMANDS_START_MARKER)})(.*?)({re.escape(COMMANDS_END_MARKER)})"
    )
    if re.search(cmd_pattern, content, re.DOTALL):
        content = re.sub(
            cmd_pattern,
            f"\\1\n\n{commands_table_md}\n\n\\3",
            content,
            flags=re.DOTALL,
        )

    README_FILE.write_text(content, encoding="utf-8")
    print("Updated README.md tables.")


def main():
    print("Starting Arabic Claude Skills auto-sync...")

    sources = load_sources()

    # 1. Sync external GitHub repos (skills + commands)
    synced_meta = sync_external_repositories(sources)

    # 2. Collect skills
    native_skills, errors = collect_native_skills(sources, synced_meta)
    if errors:
        print("Validation errors encountered:")
        for err in errors:
            print(f" - {err}", file=sys.stderr)
        sys.exit(1)

    # 3. Collect commands
    commands = collect_commands()

    print(
        f"Found {len(native_skills)} skills and {len(commands)} commands."
    )

    # 4. Output skills.json registry
    registry_data = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "name": "awesome-arabic-claude-skills",
        "description": "Curated directory and registry of Arabic skills and commands for Claude Code and AI agents",
        "total_skills": len(native_skills),
        "total_commands": len(commands),
        "skills": native_skills,
        "commands": commands,
    }

    with open(OUTPUT_REGISTRY, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, ensure_ascii=False, indent=2)
    print(f"Generated {OUTPUT_REGISTRY.relative_to(ROOT_DIR)}")

    # 5. Update README tables
    skills_table_md = generate_markdown_table(native_skills)
    commands_table_md = generate_commands_table(commands)
    update_readme(skills_table_md, commands_table_md)

    print("Auto-sync completed successfully!")


if __name__ == "__main__":
    main()
