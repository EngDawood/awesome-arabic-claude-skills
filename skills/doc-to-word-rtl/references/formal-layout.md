# Formal layout: cover page, table of contents, APA references

Read this when the user wants a formal Arabic Word report ("docx فورمال", "غلاف + فهرس", "تقرير وورد رسمي", a university assignment with a cover page) and the thesis house style of `md_to_docx_rtl.py` is not enough. The script has no cover, no table of contents, and no APA reference list for Arabic docs. Build the file with docx-js (`npm i docx`) from the doc's blocks, and apply the rules below. Each rule was learned from a render that came out wrong.

## 1. Ask first, with defaults

Ask once, before building: font and size, and which front matter to include. Suggest these defaults, do not assume them:

- Cover page + table of contents + body.
- Times New Roman 12, A4, 1-inch margins, line spacing 340 (about 1.4).
- Page numbers in the footer, restarting at 1 on the first page after the cover and contents.

Cover fields the user has not given (university, college, student name, ID, course, instructor, date) stay as `[اسم الجامعة]`-style placeholders. Never invent them. List the placeholders in the delivery message.

## 2. Direction (bidi): the mistakes that cost the most time

Word and LibreOffice reorder mixed Arabic and Latin text by their own rules. These fixes held in both.

- Arabic text goes in runs with `rightToLeft: true`. Latin, digits, signs and percentages go in separate runs without it. Split each paragraph with a token regex: an optional sign, then Latin letters or digits joined by `. , % + - _ '`, optionally continued by single-space-separated tokens.
- Do not wrap signed numbers in LRE, PDF, LRI or LRM characters. Tested: `+7.04%` rendered as `(7.04%+)`. Separate non-rtl runs are the fix.
- A table cell that starts with a sign or a Latin letter (`+2.10%`, `-0.92`, `stc`) gets an LTR paragraph. In an RTL paragraph it shows as `0.92+`.
- Tickers and codes shaped like `7010.SR` display as `SR.7010` after Arabic text. Prefix the token with one LRM (`‎`) when it matches `^\d[\d.,]*\.[A-Za-z]`. This is the only place LRM is used.
- Tables use `visuallyRightToLeft: true` and explicit column widths that sum to the text width (9026 DXA on A4 with 1-inch margins).
- Captions: `الجدول (n)` above a table, `الشكل (n)` below a figure.

## 3. Spacing and pagination

- Set `lineRule: AUTO` explicitly on every paragraph that has a `line` value. Without it, images and formulas render as clipped slivers.
- Heading 1 starts a new page (`pageBreakBefore`).
- Tables of 9 rows or fewer: `keepNext` on every row so a table never splits across pages.
- An orphan page holding one or two lines is a defect. Fixes in the order that worked: line spacing 360 to 340, table cell top/bottom margins 50 to 30, a slightly smaller last chart.
- After each build, render and count pages, then view every page (see section 6).

## 4. Table of contents that is not empty

A TOC field with no cached entries opens blank until the reader updates fields. Fill it at build time.

1. Build the docx with the TOC placeholder (a `w:sdt` containing the field) and convert it to PDF with LibreOffice.
2. Find each heading's page with `pdftotext -f N -l N`. Match with exact equality on normalized lines, never `endswith` or substring: the heading "4. مقارنة مستويات العائد" matched the wrong page that way. Normalize by dropping bidi marks, keeping only Arabic letters, and folding `ا أ إ آ ل ى ي ئ ء ة ه`.
3. Rewrite the content of the `w:sdtContent` as TOC1/TOC2 paragraphs, one field chain across them: `fldChar begin`, `instrText ' TOC \h \o "1-2" '`, `fldChar separate`, the entries, `fldChar end` in the last paragraph.
4. Each entry paragraph has `<w:bidi/>` and a tab stop `w:val="right" w:leader="dot" w:pos="<text width>"`. With `left` the page number wraps to the next line.
5. Page label = PDF page minus the number of unnumbered front pages (cover and contents), because numbering restarts at 1 in the body section.
6. Remove `w:dirty` so Word does not prompt on open. Re-zip, convert again, and confirm the page count did not change.

The page numbers come from LibreOffice's layout. Tell the user: if Word paginates differently, right-click the contents and choose Update Field.

## 5. Charts, formulas, references

- Arabic text in matplotlib is not shaped. Draw charts as SVG, render them to PNG with Chromium (Playwright, `deviceScaleFactor: 2`), and embed the PNG. Use axis fonts of 16 px or more on a viewBox about 780 px wide, and leave room under the lowest value label so it does not touch the x axis.
- A formula with Latin symbols only can be a matplotlib mathtext PNG (`mathtext.fontset: stix`). Keep it as an image.
- APA 7 reference list on a page of its own, heading "المراجع" (or "References" in an English report):
  - English entries are LTR paragraphs, hanging indent 720 DXA, sorted alphabetically.
  - Same author and year: add `a`, `b`, `c` after the year (`2026a`). No date: `n.d.-a`, `n.d.-b`.
  - Pages whose content changes (prices, quotes, market data) get "Retrieved Month D, YYYY, from URL". Do not invent a retrieval date: use the date the page was actually read, or the build date, and tell the user which.
  - A lecture or course material the user has not described stays a bracketed placeholder entry; the user fills it in.
  - Make URLs clickable.
- The body usually has no in-text citations. Offer to add `(Author, year)` citations; do not add them unasked.

## 6. Verify before delivering

Done when all of these hold on the rendered PDF:

- Page count is what you expect and no page holds only one or two lines.
- No table is split across pages, no figure is clipped, no caption is separated from its table or figure.
- Every TOC page number matches the page where the heading actually appears.
- Signed numbers, percentages and tickers read correctly in tables and prose, and no word is reversed.
- The docx passes validation (`validate.py` from the docx skill, or open and re-save in LibreOffice).
- The delivery message names every placeholder still in the file, every assumed date, and the Update Field note from section 4.
