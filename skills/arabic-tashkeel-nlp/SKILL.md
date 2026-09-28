---
name: arabic-tashkeel-nlp
description: Guide Arabic diacritization (Tashkeel/Harakat), grammatical inflection (I'rab), and Arabic NLP preprocessing (normalization, lemmatization, root extraction). Use when adding diacritics to Arabic text, preparing text for Arabic Text-to-Speech (TTS), fixing grammatical mistakes, or processing Arabic strings in NLP and search pipelines.
category: Language & NLP
title_ar: التشكيل والتدقيق اللغوي ومعالجة النصوص العربية (NLP)
---

# Arabic Tashkeel & NLP Skill (التشكيل الدقيق ومعالجة النصوص العربية)

## Quick Start (البداية السريعة)

Provide context-aware Arabic diacritization and linguistic preprocessing:
1. **Full Diacritization (تشكيل كامل)**: Used for Quranic text, poetry, children's literature, and Text-to-Speech (TTS) phonetization. Every consonant receives Fatha, Damma, Kasra, Sukun, or Shaddah with Harakah.
2. **Partial / Disambiguation Diacritization (تشكيل بنيوي / فك اللبس)**: Used for modern publishing and journalism. Only place vowels on ambiguous words where context alone might not suffice (e.g., `عُلِمَ` vs `عَلِمَ`, `مُدَرِّس` vs `مَدْرَسَة`).
3. **End-of-word Inflection (أواخر الكلم - الإعراب)**: Determine case endings (حركات الإعراب: رفع، نصب، جر، جزم) based on syntactic roles in the sentence.

---

## Core Diacritics Rules (قواعد وضوابط التشكيل)

### 1. Shaddah + Harakah Ordering (ترتيب الشدة مع الحركات)
- In standard Unicode: The base letter is followed by the Shaddah (`\u0651`), then the vowel (`\u064E` Fatha, `\u064F` Damma, `\u0650` Kasra).
- Never separate a Shaddah from its consonant with a space or Tatweel.

### 2. Hamzat & Alif Rules (همزة الوصل والقطع والألف المتطرفة)
- **همزة القطع**: تظهر وتُنطق وتُكتب فوق أو تحت الألف (`أَ / أُ / إِ`).
- **همزة الوصل**: في الأسماء العشرة ومصادر وأفعال الخماسي والسداسي وأمر الثلاثي وأل التعريف (`ا`). لا يُوضع عليها همزة.
- **الألف اللينة المتطرفة**: تُرسم ياءً غير منقوطة (`ى`) إذا كان أصلها ياءً أو زادت الكلمة عن ثلاثة أحرف (مثل: `مستشفى`)، وتُرسم ألفاً ممدودة (`ا`) إذا كان أصلها واواً (مثل: `دعا - يدعو`).

---

## Arabic NLP Text Preprocessing (معالجة النصوص لمحركات البحث والذكاء الاصطناعي)

### 1. Normalization Matrix (توحيد الأحرف للبحث والتصنيف)
When building search indices, embedding pipelines, or classifiers:
- Normalize Alef variants: `[أ إ آ]` $\to$ `ا`
- Normalize Yaa / Alef Maksura: `ى` $\to$ `ي` (only if semantic distinction is not critical)
- Normalize Taa Marbuta: `ة` $\to$ `ه` (for search queries)
- Strip Tatweel/Kashida: remove `ـ` (`\u0640`)
- Strip Tashkeel regex: `[\u064B-\u0652\u0670]`

### 2. Text-to-Speech (TTS) Tuning
For Arabic speech synthesis models (ElevenLabs, Azure Arabic, Bark):
- Always place explicit Tanween and Sukun.
- Ensure solar/lunar Lam (اللام الشمسية والقمرية) has proper Shaddah after solar letters (e.g. `الشَّمْس`).
- Avoid silent Alifs causing mispronunciation: explicitly diacritize hamzat al-wasl or elisions.
