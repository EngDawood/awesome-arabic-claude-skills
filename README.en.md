# Awesome Arabic Claude Skills 🌟

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Auto-Sync Catalog](https://github.com/EngDawood/awesome-arabic-claude-skills/actions/workflows/sync-skills.yml/badge.svg)](https://github.com/EngDawood/awesome-arabic-claude-skills/actions/workflows/sync-skills.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**English | [العربية](README.md)**

> A curated directory and open-source skill library for Claude Code and AI agents, built for the Arabic language: RTL localization, subtitling, and NLP.

---

## Table of Contents
- [Overview](#overview)
- [Installation & Usage](#installation--usage)
- [Auto-Synced Skills Catalog](#auto-synced-skills-catalog)
- [Claude Code Slash Commands](#claude-code-slash-commands)
- [Arabic MCP Servers & Tools](#arabic-mcp-servers--tools)
- [GitHub Actions Automation](#github-actions-automation)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Claude Skills** extend an AI model with specialized context and working rules. This repository provides:
1. **Native skills** ready to use from the `skills/` folder.
2. **A curated catalog and registry** of Arabic skills, repositories, and MCP servers from the community.
3. **Auto-sync via GitHub Actions** that validates skills and keeps the catalogs and the `skills.json` registry up to date.

---

## Installation & Usage

### 1. Install a specific skill with `npx skills`
You can install any skill from this repository into your project or system-wide:
```bash
npx skills add EngDawood/awesome-arabic-claude-skills --skill arabic-subtitling
```

### 2. Manual install with Claude Code
Copy the skill folder you need from `skills/` into your project's Claude skills folder:
```bash
mkdir -p .claude/skills && cp -r /path/to/awesome-arabic-claude-skills/skills/arabic-localization-rtl .claude/skills/
```

Or add it to your global Claude settings:
- **Linux / macOS**: `~/.claude/skills/`
- **Windows**: `%USERPROFILE%\.claude\skills\`

---

## Auto-Synced Skills Catalog

This table and the `skills.json` registry are updated automatically by GitHub Actions whenever a skill is added or changed.

<!-- SKILLS_TABLE_START -->

| Skill | Owner | Category | Description | Install / Link |
| :--- | :--- | :--- | :--- | :--- |
| **[arabic-localization-rtl](https://github.com/EngDawood/awesome-arabic-claude-skills/tree/main/skills/arabic-localization-rtl)**<br>تعريب البرمجيات وهندسة واجهات RTL *(Native)* | [@EngDawood](https://github.com/EngDawood) | `Software & RTL Engineering` | Guide Arabic software localization, RTL layout adaptation, bidirectional text (BiDi) handling, Arabic typography, and pluralization. Use when building or refactoring UI components for Arabic, adapting CSS/Tailwind for RTL, handling mixed Arabic/English strings, or configuring i18next/Intl for Arabic locales (ar-SA, ar-EG, ar). | `npx skills add EngDawood/awesome-arabic-claude-skills --skill arabic-localization-rtl` |
| **[arabic-rtl-docs](https://github.com/muhmoosa/claude-arabic-docs)**<br>*(Synced from GitHub)* | [@muhmoosa](https://github.com/muhmoosa) | `General` | Produce correctly-rendered right-to-left (RTL) Microsoft Office documents — Word (.docx), PowerPoint (.pptx), and Excel (.xlsx) — for Arabic, Hebrew, Persian, Urdu, and other RTL scripts. Use this skill whenever the user asks for a document in Arabic or another RTL language, or whenever the deliverable mixes RTL prose with English/Latin tokens (IBANs, URLs, emails, numbers). It must also be used whenever you produce a docx-js / openpyxl / python-pptx output that contains any RTL text, because those libraries do NOT apply section-level bidi, table direction, or heading bidi automatically — outputs that look correct in LibreOffice can still render as LTR (cells reversed, headings left-aligned, lists flipped) when opened in Microsoft Word. Trigger on phrases like "اكتب", "خطاب", "تقرير عربي", "Arabic letter", "RTL report", "بالعربي", "اللغة العربية", "Hebrew document", "Persian", or any user message written predominantly in an RTL script. | `npx skills add muhmoosa/claude-arabic-docs` |
| **[arabic-subtitling](https://github.com/EngDawood/arabic-video-subtitles-skill/tree/main/skills/arabic-subtitling-guidelines)**<br>معايير الترجمة المرئية والتفريغ العربي (Netflix TTSG) *(Synced from GitHub)* | [@EngDawood](https://github.com/EngDawood) | `Media & Localization` | Guidelines and QC tooling for adding Arabic subtitles or captions to video - Arabic-to-Arabic captions (transcription, SDH) and translated subtitles (English or other language into Modern Standard Arabic). Covers Netflix Timed Text Style Guide rules (42 chars/line, 2 lines, reading speed, timing/gaps/shot changes, numbers, quotes, ellipses, diacritics, songs, forced narratives), translation strategies for cultural references, and an SRT/VTT checker script. Use this skill whenever the user wants Arabic subtitles, captions, ترجمة فيديو, ترجمة مرئية, تفريغ نصي, تسميات توضيحية, SRT/VTT/TTML files, burning captions into a video, translating a video transcript to Arabic, or reviewing/fixing existing Arabic subtitles - even if they never say "Netflix" or "style guide". | `npx skills add EngDawood/arabic-video-subtitles-skill --skill arabic-subtitling-guidelines` |
| **[video-caption-mcp](https://github.com/EngDawood/video-caption/tree/main/skills/video-caption-mcp)**<br>*(Synced from GitHub)* | [@EngDawood](https://github.com/EngDawood) | `General` | This skill should be used when the user asks to "caption this video", "burn subtitles into this TikTok", "translate this reel", "add Arabic captions to this video", "subtitle this YouTube short", "change the caption font", "fix this caption line", asks how to connect to or use the video-caption MCP server, or mentions its tools by name (submit_job, job_status, get_output, cancel_job, restyle_job, fix_script). Covers connecting to the /mcp endpoint, submitting a caption job, polling it, returning the finished download link, and restyling, correcting or stopping a job. | `npx skills add EngDawood/video-caption --skill video-caption-mcp` |

<!-- SKILLS_TABLE_END -->

---

## Claude Code Slash Commands

Skills include slash commands you can call directly inside Claude Code:

<!-- COMMANDS_TABLE_START -->

| Slash Command | Arguments | Description | File |
| :--- | :--- | :--- | :--- |
| `/check-subtitles` | `file_path` | Run automated and manual QC checks on Arabic SRT or VTT subtitle files against Netflix TTSG rules. | [`commands/check-subtitles.md`](commands/check-subtitles.md) |
| `/translate-subtitles` | `text_or_subtitles` | Translate or adapt foreign dialogue into professional Modern Standard Arabic subtitles following Netflix TTSG and ECR strategies. | [`commands/translate-subtitles.md`](commands/translate-subtitles.md) |

<!-- COMMANDS_TABLE_END -->

---

## Arabic MCP Servers & Tools

Model Context Protocol (MCP) servers and tools that support Arabic content and research.

| Tool / Server | Description | Link |
| :--- | :--- | :--- |
| **Arabic Scholar MCP** | MCP server for academic research, textual verification, and access to heritage and Islamic sources | [Repository](https://github.com/EngDawood/arabic-scholar-mcp-server) |
| **Arabic Video Subtitles Skill** | Standards and rules for Arabic subtitling and transcription (Netflix TTSG) | [Repository](https://github.com/EngDawood/arabic-video-subtitles-skill) |
| **Thmanyah Font Web** | Web package for the Thmanyah fonts and modern Arabic typography | [Repository](https://github.com/EngDawood/thmanyah-font-web) |

---

## GitHub Actions Automation

The repository has a full automation setup for adding and updating skills:
- **Validation**: checks that every `SKILL.md` has valid YAML frontmatter, a description of at most 1024 characters, and trigger criteria.
- **`skills.json` registry**: generates a structured JSON file that external tools and CLIs can read.
- **README updates**: injects native and external skills from `sources.json` into the catalog table above. Both `README.md` and `README.en.md` are generated from the same data.
- **Adding skills via Issues and PRs**: once a contribution is approved, the workflow syncs its content right away.

---

## Contributing

Contributions from the Arabic and global community are welcome.
- To add a new skill, open a [Pull Request](CONTRIBUTING.md) or send your suggestion with the [skill form](../../issues/new?template=submit_skill.yml).
- For details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This project is licensed under the **MIT** license. See [LICENSE](LICENSE) for details.
