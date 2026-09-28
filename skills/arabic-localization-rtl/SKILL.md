---
name: arabic-localization-rtl
description: Guide Arabic software localization, RTL layout adaptation, bidirectional text (BiDi) handling, Arabic typography, and pluralization. Use when building or refactoring UI components for Arabic, adapting CSS/Tailwind for RTL, handling mixed Arabic/English strings, or configuring i18next/Intl for Arabic locales (ar-SA, ar-EG, ar).
category: Software & RTL Engineering
title_ar: تعريب البرمجيات وهندسة واجهات RTL
---

# Arabic Localization & RTL Engineering Skill (تعريب البرمجيات وهندسة RTL)

## Quick Start (البداية السريعة)

When adapting frontends (React, Vue, Svelte, HTML/CSS) for Arabic:
1. **HTML Root**: Always set `<html lang="ar" dir="rtl">`.
2. **CSS Logical Properties**: Replace directional properties with logical ones:
   - `margin-left` / `margin-right` $\to$ `margin-inline-start` / `margin-inline-end`
   - `padding-left` / `padding-right` $\to$ `padding-inline-start` / `padding-inline-end`
   - `left` / `right` $\to$ `inset-inline-start` / `inset-inline-end`
   - `text-align: left` $\to$ `text-align: start`
3. **Tailwind CSS**: Use `ms-`, `me-`, `ps-`, `pe-`, `start-`, `end-` instead of `ml-`, `mr-`, etc.

---

## Bidirectional (BiDi) & Mixed Text Rules (معالجة النصوص ثنائية الاتجاه)

### 1. Punctuation Jumping & Weak Characters
When Arabic text ends with numbers, code snippets, or English words followed by punctuation, neutral characters (like periods or parentheses) often flip incorrectly:
- **Solution**: Use the Right-to-Left Mark (RLM: `&rlm;` or `\u200F`) after Latin text or numbers at the end of an Arabic sentence.
- **Example**: `تم حفظ الملف File.txt بنجاح.` $\to$ place RLM after the dot if the file name causes the dot to jump.

### 2. Isolated LTR Fragments
Wrap LTR entities (emails, code tokens, URLs, phone numbers) in `<bdi>` or `dir="ltr"`:
```html
<span dir="ltr">+966 50 123 4567</span>
<code><bdi>npm install</bdi></code>
```

---

## Arabic Typography & Font Metrics (الخطوط والطباعة الرقمية)

- **Line Height**: Arabic scripts require ~20–30% larger `line-height` than Latin fonts due to vertical diacritics and tall ascenders/descenders (e.g. `leading-relaxed` or `line-height: 1.6 - 1.8`).
- **Recommended Web Fonts**:
  - Sans-serif / Modern UI: *IBM Plex Sans Arabic*, *Tajawal*, *Readex Pro*, *Alexandria*.
  - Editorial / Classical: *Amiri*, *Noto Naskh Arabic*.
- **Font Pairing**: Avoid mixing generic fallback system fonts that misalign baseline heights.

---

## Arabic Pluralization (قواعد الجمع الست في العربية)

Arabic has 6 plural forms supported by Unicode CLDR and `Intl.PluralRules` (`ar`):
1. **Zero (صفر)**: 0 عناصر
2. **One (واحد / مفرد)**: عنصر واحد
3. **Two (اثنان / مثنى)**: عنصران
4. **Few (قليل / جمع قلة 3-10)**: 3-10 عناصر
5. **Many (كثير 11-99)**: 11-99 عنصراً
6. **Other (مئة ومضاعفاتها وغيرها)**: 100 عنصر

Ensure your i18n dictionary (e.g., `i18next`, `next-intl`) provides keys for `_zero`, `_one`, `_two`, `_few`, `_many`, and `_other` rather than naive English single/plural logic.
