# doc-to-word-rtl

> A Claude skill that turns a Claude Doc into a Word file ready to hand in: Arabic docs come out right-to-left in a Saudi thesis style, English docs in APA 7. Arabic version: [README.md](./README.md)

## Why

Claude Docs can export to `.docx`, but that export carries no right-to-left settings. Arabic paragraphs come out left-aligned and tables read from the wrong side, so every Arabic chapter needs manual reformatting in Word. This skill replaces that export with two small scripts that build the file in the right direction and the right style from the start.

## What it does

Give Claude a Claude Doc link and ask for Word. The skill:

1. Reads the doc and exports each tab as markdown.
2. Picks the script for the doc's language.
3. Builds the `.docx`.
4. Renders a body page, a table page and a list page to check the layout.
5. Delivers the file named after the doc title.

If something goes wrong along the way, it names the cause, proposes a fix to the skill itself, and applies it only after you approve and confirm the new output.

## Installation

### Claude Code / any agent that supports `skills`

```bash
npx skills add EngDawood/awesome-arabic-claude-skills --skill doc-to-word-rtl
```

### Claude Code plugin

```
/plugin marketplace add EngDawood/awesome-arabic-claude-skills
/plugin install doc-to-word-rtl@awesome-arabic-claude-skills
```

### Manual

Copy this folder into `.claude/skills/` (project) or `~/.claude/skills/` (user).

Requires Python 3 with `python-docx` (`pip install python-docx`). LibreOffice and `pdftoppm` are used only for the visual check.

## Usage

```
Convert this to Word: https://claude.ai/artifact/XXXX
```
```
حوّل هذا المستند إلى ورد بخط 14 وتباعد 1.5: https://claude.ai/artifact/XXXX
```

The scripts also run on their own, on any markdown file:

```bash
python3 scripts/md_to_docx_rtl.py chapter.md chapter.docx
python3 scripts/md_to_docx_en.py paper.md paper.docx --paper a4
```

## House styles

### Arabic: `md_to_docx_rtl.py`

| Element | Default |
|---|---|
| Page | A4, 2.54 cm margins, centered page number |
| Body | Traditional Arabic 16, justified, line spacing 1.08 |
| Headings | `#` 22, `##` 18, `###` 16, bold. Centered when they open with المحور / الفصل / المراجع, right-aligned otherwise |
| Tables | Right-to-left columns, 14 pt, grey header row repeated on every page, rows never split |
| Captions | `جدول (n): ...` bold and centered, kept with its table |
| Lists | Each numbered list restarts at 1 |
| References | Hanging indent 0.635 cm |
| Pictures and charts | Centered, at most the text width, caption below |

Options: `--ar-font`, `--en-font`, `--size`, `--table-size`, `--color`, `--line`, `--margins`, `--paper a4|letter`, `--keep-byline`, `--dir rtl|ltr|auto`.

### English: `md_to_docx_en.py` (APA 7)

| Element | Default |
|---|---|
| Page | US Letter, 2.54 cm margins, page number top right |
| Body | Times New Roman 12, double-spaced, first-line indent 1.27 cm |
| Headings | `#` title; `##` to `#####` map to APA levels 1 to 4 |
| Tables | `Table n` bold, title italic below; horizontal rules only |
| Notes | `Note.` in italics under the table |
| References | New page, hanging indent 1.27 cm |

Options: `--font`, `--size`, `--table-size`, `--line`, `--margins`, `--paper a4|letter`, `--keep-byline`.

## Limits

- Images and charts are carried over: the skill fetches each picture from the doc and screenshots each chart, then places them with their captions. Comments are not carried over.
- A chart arrives in Word as a static picture, not an editable chart.
- Footnotes become plain text.
- The visual check runs in LibreOffice, which may not have Traditional Arabic; it judges layout, not typeface.

## Files

```
doc-to-word-rtl/
├── SKILL.md                     steps and house-style tables for Claude
├── README.md / README.en.md
└── scripts/
    ├── md_to_docx_rtl.py        Arabic, right-to-left
    └── md_to_docx_en.py         English, APA 7
```
