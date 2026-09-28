---
description: Run automated and manual QC checks on Arabic SRT or VTT subtitle files against Netflix TTSG rules.
argument: file_path
---

Validate the provided Arabic subtitle file ($ARGUMENTS) against the Arabic Subtitling Guidelines:

1. **Automated Inspection**:
   - If a file path is provided, run `python skills/arabic-subtitling-guidelines/scripts/check_subtitles.py "$ARGUMENTS" --fps 24`.
   - If the user provided subtitle text directly in the chat, parse and evaluate it against:
     - Line length ($\le$ 42 characters per line).
     - Line count ($\le$ 2 lines per event).
     - Event duration (5/6 second minimum, 7 seconds maximum).
     - Reading speed ($\le$ 20 characters per second for adults, 17 for children).
     - Unicode ellipsis (`…` `U+2026`) instead of three dots (`...`).
     - Arabic punctuation spacing (no space before `،`, `؟`, `!`).
     - Proper quotes (`"..."`) with kashida for definite article (`الـ"..."`).
     - Zero italics (`<i>` / `<em>` are strictly forbidden in Arabic).

2. **Linguistic & Style Verification**:
   - Check that the register is strict Modern Standard Arabic (MSA / الفصحى).
   - Flag any dialectal vocabulary (e.g., `برجاء`, `يا خبر`, `يا ستّار`).
   - Flag ill-timed line breaks (splits across verb-subject, mudaf/mudaf ilayh, or preposition-noun).
   - Check numbers (1–10 written in words; 11+ in numerals; ordinals with kashida `الـ21`).

3. **Report & Fixes**:
   - Present a concise report grouped by: Critical Errors, Warnings, and Suggested Mechanical Fixes.
   - If requested, generate the fixed subtitle file using `--fix`.
