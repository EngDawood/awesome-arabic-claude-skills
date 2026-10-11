# Awesome Arabic Claude Skills | مهارات كلود العربية 🌟

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Auto-Sync Catalog](https://github.com/EngDawood/awesome-arabic-claude-skills/actions/workflows/sync-skills.yml/badge.svg)](https://github.com/EngDawood/awesome-arabic-claude-skills/actions/workflows/sync-skills.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Language: Arabic & English](https://img.shields.io/badge/Language-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%7C%20English-blue.svg)](#)

**العربية | [English](README.en.md)**

> **قائمة مختارة ومكتبة مهارات مفتوحة المصدر لـ Claude Code ووكلاء الذكاء الاصطناعي، مخصصة للغة العربية، تعريب البرمجيات (RTL)، الترجمة المرئية، صياغة المحتوى، والمعالجة اللغوية.**  
> *A curated directory and open-source skill library for Claude Code and AI agents, specifically engineered for the Arabic language, RTL localization, subtitling, copywriting, and NLP.*

---

## الفهرس / Table of Contents
- [Awesome Arabic Claude Skills | مهارات كلود العربية 🌟](#awesome-arabic-claude-skills--مهارات-كلود-العربية-)
  - [الفهرس / Table of Contents](#الفهرس--table-of-contents)
  - [نظرة عامة / Overview](#نظرة-عامة--overview)
  - [طريقة التثبيت والاستخدام / Installation \& Usage](#طريقة-التثبيت-والاستخدام--installation--usage)
    - [1. تثبيت مهارة محددة عبر `npx skills` (Universal Skills)](#1-تثبيت-مهارة-محددة-عبر-npx-skills-universal-skills)
    - [2. التثبيت اليدوي مع Claude Code](#2-التثبيت-اليدوي-مع-claude-code)
  - [فهرس المهارات المحدث تلقائياً / Auto-Synced Skills Catalog](#فهرس-المهارات-المحدث-تلقائياً--auto-synced-skills-catalog)
  - [أوامر كلود السريعة / Claude Code Slash Commands](#أوامر-كلود-السريعة--claude-code-slash-commands)
  - [أدوات ومخدمات MCP عربية / Arabic MCP Servers \& Tools](#أدوات-ومخدمات-mcp-عربية--arabic-mcp-servers--tools)
  - [المزامنة التلقائية عبر GitHub Actions / GitHub Actions Automation](#المزامنة-التلقائية-عبر-github-actions--github-actions-automation)
  - [دليل المساهمة / Contributing](#دليل-المساهمة--contributing)
  - [الترخيص / License](#الترخيص--license)

---

## نظرة عامة / Overview

تتيح **مهارات كلود (Claude Skills)** توسيع قدرات نموذج الذكاء الاصطناعي بسياق متخصص وقواعد عمل دقيقة وتعليمات برمجية جاهزة. يهدف هذا المستودع إلى أن يكون المرجع العربي الأول لهذه المهارات، حيث يجمع بين:
1. **مهارات مدمجة (Native Built-in Skills)** جاهزة للاستخدام المباشر داخل مجلد `skills/`.
2. **فهرس متجدد (Curated Catalog & Registry)** لجميع المهارات والمستودعات ومخدمات MCP العربية في مجتمع المطورين.
3. **مزامنة تلقائية (Auto-Sync via GitHub Actions)** للتحقق من المهارات وتحديث الفهارس وسجل `skills.json` آلياً عند كل تحديث أو مساهمة.

---

## طريقة التثبيت والاستخدام / Installation & Usage

### 1. تثبيت مهارة محددة عبر `npx skills` (Universal Skills)
يمكنك تثبيت أي مهارة من هذا المستودع مباشرة في مشروعك أو على مستوى نظامك العام:
```bash
npx skills add EngDawood/awesome-arabic-claude-skills --skill arabic-subtitling
```

### 2. التثبيت اليدوي مع Claude Code
انسخ مجلد المهارة المطلوبة من `skills/` إلى مجلد مهارات كلود في مشروعك:
```bash
mkdir -p .claude/skills && cp -r /path/to/awesome-arabic-claude-skills/skills/arabic-localization-rtl .claude/skills/
```

أو أضفها إلى إعدادات كلود العامة في جهازك:
- **نظام لينكس / ماك**: `~/.claude/skills/`
- **نظام ويندوز**: `%USERPROFILE%\.gemini\config\skills\` أو `%USERPROFILE%\.claude\skills\`

---

## فهرس المهارات المحدث تلقائياً / Auto-Synced Skills Catalog

يتم تحديث هذا الجدول وسجل `skills.json` تلقائياً عبر GitHub Actions بمجرد إضافة أو تعديل أي مهارة.

<!-- SKILLS_TABLE_START -->

| المهارة (Skill) | المالك (Owner) | التصنيف (Category) | الوصف (Description) | التثبيت والاستخدام (Install / Link) |
| :--- | :--- | :--- | :--- | :--- |
| **[arabic-localization-rtl](https://github.com/EngDawood/awesome-arabic-claude-skills/tree/main/skills/arabic-localization-rtl)**<br>تعريب البرمجيات وهندسة واجهات RTL *(مدمجة / Native)* | [@EngDawood](https://github.com/EngDawood) | `Software & RTL Engineering` | Guide Arabic software localization, RTL layout adaptation, bidirectional text (BiDi) handling, Arabic typography, and pluralization. Use when building or refactoring UI components for Arabic, adapting CSS/Tailwind for RTL, handling mixed Arabic/English strings, or configuring i18next/Intl for Arabic locales (ar-SA, ar-EG, ar). | `npx skills add EngDawood/awesome-arabic-claude-skills --skill arabic-localization-rtl` |
| **[arabic-rtl-docs](https://github.com/muhmoosa/claude-arabic-docs)**<br>arabic-rtl-docs *(مزامنة من GitHub / Synced)* | [@muhmoosa](https://github.com/muhmoosa) | `General` | Produce correctly-rendered right-to-left (RTL) Microsoft Office documents — Word (.docx), PowerPoint (.pptx), and Excel (.xlsx) — for Arabic, Hebrew, Persian, Urdu, and other RTL scripts. Use this skill whenever the user asks for a document in Arabic or another RTL language, or whenever the deliverable mixes RTL prose with English/Latin tokens (IBANs, URLs, emails, numbers). It must also be used whenever you produce a docx-js / openpyxl / python-pptx output that contains any RTL text, because those libraries do NOT apply section-level bidi, table direction, or heading bidi automatically — outputs that look correct in LibreOffice can still render as LTR (cells reversed, headings left-aligned, lists flipped) when opened in Microsoft Word. Trigger on phrases like "اكتب", "خطاب", "تقرير عربي", "Arabic letter", "RTL report", "بالعربي", "اللغة العربية", "Hebrew document", "Persian", or any user message written predominantly in an RTL script. | `npx skills add muhmoosa/claude-arabic-docs` |
| **[arabic-subtitling](https://github.com/EngDawood/arabic-video-subtitles-skill/tree/main/skills/arabic-subtitling-guidelines)**<br>معايير الترجمة المرئية والتفريغ العربي (Netflix TTSG) *(مزامنة من GitHub / Synced)* | [@EngDawood](https://github.com/EngDawood) | `Media & Localization` | Guidelines and QC tooling for adding Arabic subtitles or captions to video - Arabic-to-Arabic captions (transcription, SDH) and translated subtitles (English or other language into Modern Standard Arabic). Covers Netflix Timed Text Style Guide rules (42 chars/line, 2 lines, reading speed, timing/gaps/shot changes, numbers, quotes, ellipses, diacritics, songs, forced narratives), translation strategies for cultural references, and an SRT/VTT checker script. Use this skill whenever the user wants Arabic subtitles, captions, ترجمة فيديو, ترجمة مرئية, تفريغ نصي, تسميات توضيحية, SRT/VTT/TTML files, burning captions into a video, translating a video transcript to Arabic, or reviewing/fixing existing Arabic subtitles - even if they never say "Netflix" or "style guide". | `npx skills add EngDawood/arabic-video-subtitles-skill --skill arabic-subtitling-guidelines` |
| **[ppt-master](https://github.com/EngDawood/awesome-arabic-claude-skills/tree/main/skills/ppt-master)**<br>ppt-master *(مدمجة / Native)* | [@EngDawood](https://github.com/EngDawood) | `General` | > AI-driven presentation workflow for generating editable PPTX decks and slides, reconstructing page visuals, creating reusable Brand/Style/Layout/Deck workspaces, filling native PPTX templates, and enhancing finished PPTX files. Use when the user asks to create, generate, reconstruct, regenerate, beautify, redesign, template, fill, or enhance a presentation, PPT, PPTX, slide deck, or courseware — including adding narration or animation to one — requests a presentation-authored narrated/self-running video, or mentions ppt-master. | `npx skills add EngDawood/awesome-arabic-claude-skills --skill ppt-master` |
| **[video-caption-mcp](https://github.com/EngDawood/video-caption/tree/main/skills/video-caption-mcp)**<br>video-caption-mcp *(مزامنة من GitHub / Synced)* | [@EngDawood](https://github.com/EngDawood) | `General` | This skill should be used when the user asks to "caption this video", "burn subtitles into this TikTok", "translate this reel", "add Arabic captions to this video", "subtitle this YouTube short", "change the caption font", "fix this caption line", asks how to connect to or use the video-caption MCP server, or mentions its tools by name (submit_job, job_status, get_output, cancel_job, restyle_job, fix_script). Covers connecting to the /mcp endpoint, submitting a caption job, polling it, returning the finished download link, and restyling, correcting or stopping a job. | `npx skills add EngDawood/video-caption --skill video-caption-mcp` |

<!-- SKILLS_TABLE_END -->

---

## أوامر كلود السريعة / Claude Code Slash Commands

تتضمن المهارات أوامر سريعة (Slash Commands) يمكن استدعاؤها مباشرة داخل Claude Code:

<!-- COMMANDS_TABLE_START -->

| الأمر (Slash Command) | المعاملات (Arguments) | الوصف (Description) | ملف الأمر (File) |
| :--- | :--- | :--- | :--- |
| `/check-subtitles` | `file_path` | Run automated and manual QC checks on Arabic SRT or VTT subtitle files against Netflix TTSG rules. | [`commands/check-subtitles.md`](commands/check-subtitles.md) |
| `/translate-subtitles` | `text_or_subtitles` | Translate or adapt foreign dialogue into professional Modern Standard Arabic subtitles following Netflix TTSG and ECR strategies. | [`commands/translate-subtitles.md`](commands/translate-subtitles.md) |

<!-- COMMANDS_TABLE_END -->

---

## أدوات ومخدمات MCP عربية / Arabic MCP Servers & Tools

مجموعة من مخدمات بروتوكول سياق النموذج (Model Context Protocol - MCP) والأدوات الداعمة للمحتوى والبيانات العربية:

| الأداة / المخدم | الوصف | الرابط |
| :--- | :--- | :--- |
| **Arabic Scholar MCP** | مخدم MCP للبحث الأكاديمي والتحقيق والوصول للمصادر التراثية والإسلامية | [المستودع](https://github.com/EngDawood/arabic-scholar-mcp-server) |
| **Arabic Video Subtitles Skill** | دليل معايير وقواعد الترجمة المرئية والتفريغ النصي العربي (Netflix TTSG) | [المستودع](https://github.com/EngDawood/arabic-video-subtitles-skill) |
| **Thmanyah Font Web** | حزمة وتطبيق ويب لخطوط ثمانية ودعم التيبوغرافيا العربية الحديثة | [المستودع](https://github.com/EngDawood/thmanyah-font-web) |

---

## المزامنة التلقائية عبر GitHub Actions / GitHub Actions Automation

يحتوي المستودع على منظومة متكاملة لأتمتة إضافة وتحديث المهارات:
- **فحص الترويسة والصيغة (Validation)**: التحقق من التزام كل ملف `SKILL.md` بمعايير صيغة YAML Frontmatter وعدم تجاوز الوصف لـ 1024 حرفاً ووجود معايير التفعيل.
- **تحديث سجل `skills.json`**: توليد ملف JSON مهيكل يمكن للأدوات الخارجية وواجهات السطر البرمجي (CLI) قراءته برمجياً.
- **تحديث الـ README دورياً**: حقن المهارات المدمجة والخارجية من `sources.json` مباشرة في جدول الفهرس أعلاه.
- **إضافة المهارات عبر الـ Issues والـ PRs**: عند اعتماد مساهمة، يقوم الـ Workflow بمزامنة المحتوى فوراً.

---

## دليل المساهمة / Contributing

نرحب بجميع المساهمات من المجتمع العربي والعالمي!
- لإضافة مهارة جديدة: افتح [Pull Request](CONTRIBUTING.md) أو أرسل اقتراحك عبر [نموذج المهارات](../../issues/new?template=submit_skill.yml).
- للمزيد من التفاصيل، راجع [دليل المساهمة CONTRIBUTING.md](CONTRIBUTING.md).

---

## الترخيص / License

هذا المشروع مرخص تحت رخصة **MIT**. راجع ملف [LICENSE](LICENSE) لمزيد من التفاصيل.