---
description: Translate or adapt foreign dialogue into professional Modern Standard Arabic subtitles following Netflix TTSG and ECR strategies.
argument: text_or_subtitles
---

Translate the input dialogue or timed subtitle events ($ARGUMENTS) into professional Arabic subtitles following the rules in `skills/arabic-subtitling-guidelines/SKILL.md`:

1. **Language & Register**:
   - Translate strictly into **Modern Standard Arabic (MSA / الفصحى)**.
   - Avoid colloquialisms, regional slang, or dialect words.
   - Never censor; faithfully match original dramatic or comedic register without adding unneeded obscenity.
   - Never apply italics (`<i>`).

2. **Cultural References (ECRs)**:
   - Apply appropriate adaptation strategies from `skills/arabic-subtitling-guidelines/references/translation-strategies.md` (Specification, Generalization, Retention in quotes, Official Equivalents).
   - Acronyms: Translate established ones (CIA -> `الوكالة المركزية للاستخبارات`), transliterate familiar phonetic ones (OPEC -> `أوبك`).

3. **Layout & Segmentation**:
   - Limit lines to **42 characters maximum** (including punctuation and spaces).
   - Maximum **2 lines** per subtitle event; prefer single lines or bottom-heavy two-liners.
   - Never break a line between: verb and subject, mudaf and mudaf ilayh, noun and adjective, preposition and noun, or number and counted noun.
   - Never leave a single orphan word on line 2.

4. **Dual Speakers**:
   - Use hyphen + space (`- `) on each line if two speakers are speaking in the same event.

5. **Output**:
   - Output formatted SRT or clean two-line subtitle events ready for video synchronization.
