---
name: arabic-subtitling
description: Guide Arabic video subtitling, closed captioning, line-balancing, and formatting adhering to international standards (Netflix Arabic TTSG). Use when creating, translating, formatting, reviewing, or fixing Arabic subtitles, SRT/VTT files, or when user mentions Arabic captions, subtitling guidelines, or video caption timing.
category: Media & Localization
title_ar: معايير الترجمة المرئية والتفريغ العربي
---

# Arabic Subtitling Guidelines Skill (مهارة الترجمة المرئية والتفريغ العربي)

## Quick Start (البداية السريعة)

Apply professional Arabic subtitling standards to subtitle blocks:
- **Maximum Line Length**: 32–37 characters per line (Netflix standard: max 37 CPL).
- **Line Count**: Maximum 2 lines per subtitle event.
- **Reading Speed**: Target 12–15 characters per second (CPS) for Arabic; absolute max 17 CPS.
- **Duration**: Minimum 5/6 of a second (approx 20 frames); maximum 7 seconds per subtitle event.
- **Punctuation Position**: Always maintain proper right-to-left punctuation (periods, commas, question marks). Do NOT manually invert punctuation marks; ensure proper Unicode RTL embedding (`\u200F` or `\u202B`) if rendering engines flip them.

---

## Core Rules & Conventions (القواعد والمعايير الأساسية)

### 1. Line Breaks & Syntactic Balance (توزيع الأسطر والتوازن النحوي)
Never split connected syntactic units across lines:
- **Do NOT split**:
  - المضاف والمضاف إليه (e.g., keep `رئيس / مجلس الإدارة` together if possible).
  - الفعل والفاعل المباشر أو المفعول به القصير.
  - الصفة والموصوف (e.g., `مشروع / ضخم`).
  - حرف الجر واسمه المجرور (e.g., `في / المدينة`).
  - أحرف العطف والربط: لا تترك حرف العطف منفصلاً في نهاية السطر.

### 2. Numbers & Numerals (الأرقام والتواريخ)
- Spell out numbers from zero to ten (صفر إلى عشرة) in Arabic prose.
- Use numerals (11+) for quantities above ten unless stylistic context requires words.
- Use Eastern Arabic numerals (`١، ٢، ٣`) or Western Arabic (`1, 2, 3`) consistently depending on project specs (modern streaming platforms prefer Western Arabic numerals: `1, 2, 3`).

### 3. Punctuation & Formatting (علامات الترقيم)
- Use Arabic question mark `؟` and Arabic comma `،` and Arabic semicolon `؛`.
- Avoid exclamation marks unless genuine yelling or extreme urgency is expressed.
- Dialogue from two speakers in one event uses a leading dash with a space:
  ```
  - مرحباً، كيف حالك؟
  - بخير، شكراً لك.
  ```

---

## Workflow: Subtitle Review & Optimization (خطوات مراجعة وتحسين ملف الترجمة)

1. **Calculate CPL (Characters Per Line)**: Ensure no line exceeds 37 characters.
2. **Calculate CPS (Characters Per Second)**:
   $$\text{CPS} = \frac{\text{Length of Text (chars)}}{\text{Duration (seconds)}}$$
   If $\text{CPS} > 16$, condense or rephrase the Arabic sentence without losing meaning.
3. **Check Bidirectional / RTL Leaks**: Ensure trailing periods or question marks don't jump to the right/left improperly due to mixed Latin/Arabic text. Wrap English names or acronyms cleanly.
