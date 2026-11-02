---
name: doc-to-word-rtl
description: Exports a Claude Doc (claude.ai artifact link) to a Word .docx, Arabic docs in a right-to-left Saudi thesis house style and English docs in APA 7. Use when asked to turn a Claude Doc into Word, docx, ملف وورد or تحويل المستند إلى ورد.
category: Documents & Academic Writing
title_ar: تحويل مستندات Claude إلى ورد (عربي RTL و APA)
---

# Claude Doc → Word

Turn a Claude Doc into a .docx that opens in Word already in its **house style**. Two scripts in this skill's `scripts/` folder, one per language; each is the single source of truth for its house style, and its options override it when a client's template differs:

- Arabic doc → `md_to_docx_rtl.py` (right-to-left paragraphs and tables, Traditional Arabic, thesis spacing)
- English doc → `md_to_docx_en.py` (APA 7 student paper)

The doc's language is the one most of its prose is written in; the client's instructions win when they name a style.

Build the final file with the script. The connector's own `docx` export carries no bidi settings, so its Arabic tables and paragraphs come out mirrored.

## Steps

1. **Locate.** Call Claude Docs `read` with `ref: {object: "project", id: <doc id>}`. For a short `claude.ai/artifact/...` link, `Artifact` read it first to get the doc id. Done when you hold the doc id and the file id of every tab.
2. **Export.** For each tab, call Claude Docs `export` with `format: "markdown"`. Large results are saved to a JSON file and the tool message names its path: that path is the script input as is. Small inline results: write `{"data":{"bytes_b64":"<the value>"}}` to `<scratch>/<tab>.json`. Done when every tab has an input file on disk.
3. **Pictures.** The export's `notes` list each dropped construct; images become `&#91;image: <alt>\]` lines and charts or other widgets become `&#91;embedded content: <caption>\]`. When the notes report any, fetch every one, in document order:
   - Read the tab with `payload: {"projection": "outline"}`. Each picture is a `<media blob='blob/<id>' alt='…'/>`, each chart an `<embed ref='node/<id>' caption='…'/>`. A `<gap>` inside a list or table hides its blocks; read that block with `{"kind": "view", "parentId": "<its id>"}` when the outline shows fewer pictures than the notes count.
   - Picture: `read` `ref: {object: "blob", id: "<id>"}` gives its `asset`; then `Artifact` read with the doc's link and `path: "<asset>"` saves the file and prints its path.
   - Chart: `read` `ref: {object: "node", id: "<id>"}`, `engine: "widget"`, `payload: {"kind": "screenshot"}` saves a PNG and prints its path.
   - Write `<scratch>/images.json` as a list of `{"alt": "<alt or caption>", "path": "<file>"}` in the order they appear.
   Done when the list holds one entry per dropped picture and chart.
4. **Pick the script.** `<base dir>/scripts/<script>`, where `<base dir>` is the "Base directory for this skill" line shown when this skill loads and `<script>` is the one for the doc's language. Run it in place (`pip install python-docx --break-system-packages` if the import fails). Done when `python3 <base dir>/scripts/<script> -h` prints usage.
5. **Convert.** `python3 <base dir>/scripts/<script> <input> "<doc title>.docx" [--images <scratch>/images.json] [options]`, passing an option for every client-template value that differs from the house style. Done when the script prints `OK -> ...` and `images: N embedded, 0 missing` for every tab; `direction: LTR` from the Arabic script on an Arabic doc means the script is damaged: stop and tell the user.
6. **Verify.** `soffice --headless --convert-to pdf`, then `pdftoppm -r 60 -png` and view a body page, a table page, a numbered-list page, and a page with a picture when there is one. Done when every page viewed passes every check:
   - layout matches the house-style table for the doc's language (Arabic: first table column on the right, grey header row; English: rules only above, below the header and at the bottom of tables);
   - headings placed per the house style (right-aligned Arabic headings sit on the right edge);
   - each picture centered within the margins, its caption under it;
   - each numbered list starts at 1;
   - no box glyphs or reversed words.
   The render box usually lacks Traditional Arabic and substitutes a fallback face; judge layout, not typeface.
7. **Deliver.** SendUserFile, file named after the doc title. Name anything still missing (comments, a picture that could not be fetched) so the user can add it by hand.
8. **Lesson.** Every run that hit a defect (a failed step, a wrong render, a user correction to the output) ends with a lesson for this skill. Done when each defect is either fixed in the skill's source or the user declined the fix:
   - Name the defect and its root cause in one line each, then propose the smallest change that prevents it: the script, the house-style table, or a step here.
   - Make the change only after the user approves the proposal.
   - Apply it in a working copy of this skill, rerun steps 5 and 6 on the same doc, and send the user the new .docx.
   - Once the user confirms the new output is correct, write the change into the skill's source, `EngDawood/claude-doc-to-docx-arabic`: a pull request that bumps `version` in `.claude-plugin/plugin.json`. For a copy installed in Claude (claude.ai / Cowork) as a `.plugin` file, also repackage it with the `cowork-plugin` skill (customize mode).
   - A defect the user declines stays as it is; keep the deliverable from step 7.

## Arabic house style (`md_to_docx_rtl.py`)

Taken from a hand-formatted Saudi master's thesis chapter.

| Element | Style | Option |
|---|---|---|
| Page | A4, margins 2.54 cm, centered page number | `--paper`, `--margins` |
| Body | Traditional Arabic 16, colour 0D0D0D, justified, line 1.08, 8 pt after | `--ar-font`, `--en-font`, `--size`, `--color`, `--line` |
| `#` | 22 bold, centered; Title style, so it stays out of the table of contents | derives from `--size` |
| `##` | 18 bold | derives from `--size` |
| `###` | 16 bold | derives from `--size` |
| Heading alignment | centered when it opens with المحور / الفصل / مراجع / المراجع; right otherwise (أولاً، 1.، خلاصة) | `CENTER_H_RE` in script |
| Caption `جدول (n): …` | 16 bold centered, kept with the table | |
| Table | full width, 14 pt, header bold on E7E6E6 repeated each page, rows unsplit, cells vertically centered, text right, numbers centered | `--table-size` |
| After a table | 10 pt space before the next paragraph | |
| Lists | 16 pt, 4 pt after, every numbered list restarts at 1 | |
| References (under a heading with المراجع / References) | right-aligned, hanging indent 0.635 cm | |
| English-only paragraph | left-to-right, same font | |
| Pictures and charts | centered, scaled to the text width (at most 18 cm tall); a chart's caption under it | `--images` |
| Right-aligned text | no `jc` set, so Word aligns it to the start (right) of the RTL line; `jc="right"` would land on the left | |
| `date · @name` line under the title | removed | `--keep-byline` |
| `---` | page break | |

## English house style (`md_to_docx_en.py`, APA 7)

| Element | Style | Option |
|---|---|---|
| Page | US Letter, margins 2.54 cm, page number top right | `--paper`, `--margins` |
| Body | Times New Roman 12, double-spaced, left-aligned, first line indented 1.27 cm, no space between paragraphs | `--font`, `--size`, `--line` |
| `#` | paper title, bold centered; Title style, so it stays out of the table of contents | |
| `##` | APA Level 1, bold centered | |
| `###` | Level 2, bold flush left | |
| `####` | Level 3, bold italic flush left | |
| `#####` | Level 4, bold indented | |
| `Table n: Title` | "Table n" bold on its own line, title italic on the next | |
| Table | horizontal rules only (top, under header, bottom), header row repeats, rows unsplit | `--table-size` |
| `Note.` line after a table | "Note." italic, then the text | |
| Lists | double-spaced, every numbered list restarts at 1 | |
| `References` heading | starts a new page; entries hanging indent 1.27 cm | |
| Pictures and charts | centered, scaled to the text width (at most 18 cm tall); a chart's caption under it | `--images` |
| `date · @name` line under the title | removed | `--keep-byline` |
