# Netflix Arabic Timed Text Style Guide & Specifications
### Comprehensive Reference Manual (incorporating December 2025 Updates)

This document is the definitive technical and linguistic reference for Arabic timed text (subtitling and SDH), consolidating:
1. **Netflix Arabic Timed Text Style Guide** (including all **December 2025** updates)
2. **Timed Text Style Guide: General Requirements**
3. **Timed Text Style Guide: Subtitle Timing Guidelines**
4. **Timed Text Style Guide: Subtitle Templates & Pivot Workflows**
5. **Timed Text Style Guide: Product Supplemental & Marketing Assets**

---

## 1. Linguistic & Translation Guidelines (December 2025 Updates)

### Modern Standard Arabic (MSA / الفصحى)
- Subtitles must be rendered exclusively in **Modern Standard Arabic (MSA)**.
- Dialectal vocabulary, regional slang, or colloquial Egyptian/Levantine/Gulf phrasing (such as `برجاء`, `يا خبر`, `يا ستّار`, `إيش`, `شو`, `عشان`) are strictly forbidden, even when translating colloquial source dialogue.
- When an exact MSA equivalent does not exist, subtitlers must choose the closest standard Arabic term that preserves semantic accuracy and tone.

### Translation vs. Transliteration (Updated Dec 2025)
- **Primary Rule**: Always prioritize clarity, semantic fidelity, and natural phrasing. Always research and utilize a well-established Arabic equivalent where one exists.
- **Transliteration with Double Quotes**:
  - If a foreign term lacks an established Arabic equivalent, is ambiguous, or is rarely used in Arabic, transliterate the term and enclose it in straight double quotation marks: `"..."` (e.g., `"بودكاست"` when unfamiliar, `"سكيت بورد"`).
- **Integrated Loanwords (Dropping Quotes)**:
  - If a transliterated foreign term has been widely integrated into everyday Arabic usage, quotation marks may be omitted **if the term can be pluralized using standard Arabic plural patterns** (e.g., `راديو` and `راديوهات`, `كمبيوتر` and `كمبيوترات`, `تلفزيون` and `تلفزيونات`).
- **Geographical Entities & Currencies**:
  - Use standard Arabic exonyms and names: `المكسيك` (Mexico), `أثينا` (Athens), `اليورو` (Euro), `البيزو` (Peso).
  - **Never** perform mathematical currency conversions (e.g., do not convert 50 USD into local currency). Maintain the original numerical amount and translate the currency name.
- **Proper Names & Character Names**:
  - Transliterate personal names phonetically matching the target pronunciation (First name followed by Last name).
  - Character nicknames: Transliterate phonetically unless the literal meaning is a plot point or character attribute directly relevant to narrative comprehension.

### Acronyms & Abbreviations (Updated Dec 2025)
- **Acronyms with Known Arabic Equivalents**:
  - Translate the acronym into its established Arabic title or abbreviation if widely recognized:
    - *CIA* &rarr; `الوكالة المركزية للاستخبارات` (or `الاستخبارات المركزية`)
    - *UN* &rarr; `الأمم المتحدة`
    - *WHO* &rarr; `منظمة الصحة العالمية`
- **Acronyms Used Phonetically**:
  - If an acronym is commonly recognized without translation and is spoken as a single word or recognized as-is, transliterate it phonetically:
    - *OPEC* &rarr; `أوبك`
    - *UNICEF* &rarr; `يونيسف`
    - *NATO* &rarr; `الناتو`
    - *FBI* &rarr; `إف بي آي` (if phonetic recognition exceeds the translated phrase)
- **Standard Abbreviations & SI Measurement Units**:
  - Standard Arabic abbreviations for time and measurement are permissible when space is constrained:
    - `ص` for a.m. (`صباحًا`)
    - `م` for p.m. (`مساءً`)
    - `ملم` for millimeters (`مليمتر`)
    - `سم` for centimeters (`سنتيمتر`)
    - `م` or `أمتار` for meters
    - `كم` for kilometers (`كيلومتر`)
    - `كغ` or `كغم` for kilograms (`كيلوغرام`)
  - **Crucial Formatting Rule**: Insert a non-breaking space between the number and the unit abbreviation (e.g., `5 كغ`, `10 سم`).
  - **No Periods**: In accordance with the International System of Units (SI) and Netflix TTSG, **never** append a period to measurement unit abbreviations (write `5 كغ`, **not** `5 كغ.`).

### Profanity & Censorship
- **Zero Censorship**: Never censor, bleep, or euphemize foul language or sensitive dialogue.
- Match the severity, register, and comedic/dramatic tone of the source text.
- Do not introduce obscenities or vulgarities that are absent in the source audio.

### Treatment of Italics
- **Strict Prohibition**: The Arabic writing system does not support or recognize italics. Never use `<i>` or `<em>` tags in Arabic subtitles under any circumstance.

---

## 2. Layout, Line Treatment & Typography

### Screen Layout Specifications
- **Characters Per Row (CPR)**: Maximum **42 characters per line** (inclusive of punctuation and spaces).
- **Line Count**: Maximum **2 lines** per subtitle event. Single-line subtitles are preferred whenever possible.
- **Visual Balance (Pyramid / Bottom-Heavy)**:
  - When two lines are required, prefer a bottom-heavy shape where Line 2 is longer than Line 1.
  - Never leave an **orphan word** (a single isolated word) on Line 2.

### Syntactic Line Breaking Constraints
Never break a line across grammatical constituents. A line break must never separate:
1. **Verb and Subject** (الفعل والفاعل)
2. **Preposition and Governed Noun** (حرف الجر والاسم المجرور)
3. **Annexation / Genitive Construct** (المضاف والمضاف إليه)
4. **Noun and Adjective** (الاسم وموصوفه)
5. **Subordinating Particle and Verb** (أدوات النصب والجزم وفعلها)
6. **Numeral and Counted Noun** (العدد والمعدود)
7. **Vocative Particle and Vocative Noun** (حرف النداء والمنادى)
8. **Exception Particle and Excepted Word** (أداة الاستثناء والمستثنى)

### Dual Speakers (Dialogue Events)
- When two different characters speak within the same subtitle event:
  - Each character must occupy a separate line (maximum 2 lines total).
  - Each line begins with a hyphen followed by a space: `- `.
  - Each line must represent a complete, syntactically independent sentence or utterance.

### Punctuation & Kashida Placement
- **Ellipsis**:
  - Always use the dedicated single Unicode character `…` (`U+2026`). Never write three ASCII dots (`...`).
  - Use ellipses for trailing off thoughts, pauses exceeding 2 seconds, or interrupted speech.
  - When speech is interrupted by another speaker or a Forced Narrative and subsequently resumed, place an ellipsis at the end of the first subtitle and at the beginning of the continuation subtitle.
  - Do **not** use an ellipsis when a standard sentence naturally spans across two consecutive subtitles without an audible pause.
- **Punctuation Spacing**:
  - Cliticize commas (`،`), periods (`.`), question marks (`؟`), and exclamation marks (`!`) directly to the preceding word without spaces.
  - **No Double Punctuation**: Combinations like `؟!`, `!?`, or `!!` are forbidden. Choose the punctuation mark that matches the dominant tone.
  - In Arabic syndetic coordination, repeat the conjunction `و` without preceding commas instead of using European-style comma lists:
    - Correct: `الرجال والنساء والأطفال`
    - Incorrect: `الرجال، النساء، والأطفال`
- **Quotation Marks**:
  - Use straight double quotes: `"..."`.
  - Prefixing with the Definite Article (`الـ`): When quoting a word that has the Arabic definite article prefixed, connect the article to the quotation mark with a **kashida** (tatweel `U+0640`):
    - Example: `الـ"برونكس"`
  - Quote book titles, films, songs, quoted dialogue, and transliterated names inside SDH descriptors.

---

## 3. Numbers, Dates & Measurements

- **Numbers 1 to 10**: Must be written in full words, observing Arabic gender agreement rules (*مخالفة العدد للمعدود*):
  - `ثلاثة رجال` / `ثلاث نساء`
  - `رجل واحد` / `امرأة واحدة`
  - `رجلان اثنان` / `امرأتان اثنتان`
- **Numbers 11 and Above**: Write in numerals (`11`, `45`, `1,250`), unless starting a sentence or used in fixed idioms.
- **Ordinals**:
  - 1st through 9th: Write in words (`الموسم الأول`, `المركز الثالث`).
  - 10th and above: Write using digits prefixed with the definite article and kashida: `الـ10`, `الـ21`, `الـ100`.
- **Formatting Conventions**:
  - Thousands separator: Comma (`,`) &rarr; `10,000`.
  - Decimal point: Dot (`.`) with a leading zero if under 1 &rarr; `0.75`.
  - Percentages: Write the word out in Arabic: `بالمئة` or `في المئة` (e.g., `25 بالمئة`).
  - Time: 12-hour system followed by daylight markers (`صباحًا`, `مساءً`, or abbreviations `ص`, `م`).
  - Gregorian Months: Use standard MSA Gregorian names (`يناير`, `فبراير`, `مارس`, `أبريل`, `مايو`, `يونيو`, `يوليو`, `أغسطس`, `سبتمبر`, `أكتوبر`, `نوفمبر`, `ديسمبر`). Avoid Levantine/Mesopotamian month variants (`آب`, `كانون`) unless local context specifically demands it.

---

## 4. Subtitle Timing Guidelines & Synchronization

### Duration Boundaries
- **Minimum Duration**: **5/6 second** (approx. 20 frames at 24 fps, or 21 frames at 25 fps, or 25 frames at 29.97 fps).
- **Maximum Duration**: **7 seconds** per event.

### Reading Speed Limits
- **Adult Programs**: Up to **20 Characters Per Second (CPS)**.
- **Children's Programs**: Up to **17 Characters Per Second (CPS)**.
- **SDH (Subtitles for Deaf and Hard of Hearing)**:
  - Adults: Up to **23 CPS**.
  - Children: Up to **20 CPS**.

### Shot Changes & Chaining Rules
- **Shot Changes**:
  - If dialogue begins within 1 to 2 frames after a shot change, snap the subtitle in-time directly to the shot change.
  - Subtitles must not cross a shot change unless dialogue continuously spans across the cut.
  - If dialogue finishes before a shot change, end the subtitle at least 2 frames before the cut.
- **Inter-Subtitle Gaps (Chaining)**:
  - **Minimum Gap**: **2 frames** between consecutive subtitles to allow the eye to register a new subtitle.
  - **Forbidden Gap Range**: At 24 fps, gaps between 3 and 11 frames cause visual blinking/fluttering. Such gaps **must be closed (chained) to exactly 2 frames**.
  - If dialogue pause is 1/2 second or longer ($\ge$ 12 frames at 24 fps), maintain the natural gap.

---

## 5. Forced Narratives (FN) & Foreign Speech

- **Definition**: Subtitles for on-screen text, signs, letters, text messages, and foreign dialogue that are crucial for comprehension.
- **Plot Relevance**: Subtitle only content that the original audience was meant to understand and that is not already conveyed in spoken dialogue.
- **Formatting**:
  - Enclose on-screen text translations in straight quotation marks: `"منطقة محظورة"`.
  - **Never** combine on-screen text and spoken dialogue in the same event.
  - Time the Forced Narrative precisely to the appearance and disappearance of the on-screen graphic.
- **Foreign Language Utterances**:
  - In Arabic-language productions, full sentences in foreign languages (English, French, etc.) receive an FN subtitle if meant to be understood.
  - Common foreign interjections or single words (`Hello`, `Merci`, `Bye`) should **not** receive an FN subtitle.

---

## 6. Subtitles for the Deaf and Hard of Hearing (SDH)

### Language Consistency (Updated Dec 2025)
- **Strict MSA Requirement**: All SDH identifiers, speaker labels, and sound descriptions **must be rendered exclusively in Modern Standard Arabic**, even when transcribing colloquial/dialectal video content.
- Never write SDH identifiers in dialect.

### Sound Effects & Ambient Audio
- Enclose all sound descriptors in square brackets: `[...]`.
- Use the **indefinite grammatical form** for sound descriptions:
  - `[زقزقة عصافير]` (not `[الزقزقة]`)
  - `[صوت طلق ناري]`
  - `[صوت بوق سيارة بعيد]`
  - `[ضحك]`
- For off-screen dialogue, specify the speaker in brackets if identification is necessary: `[أحمد عبر الهاتف]`.

### Music & Song Lyrics
- Bracket music with musical notes (`♪`) surrounded by a single space on each side:
  - `♪ كلمات الأغنية بالعربية ♪`
- If music is purely instrumental, describe the genre or mood in square brackets:
  - `[موسيقى هادئة]`
  - `[موسيقى روك صاخبة]`

---

## 7. Subtitle Templates & Pivot Workflows

- **English Pivot Template**:
  - For non-English productions (e.g., Korean, Japanese, Spanish), downstream translators translate from an English pivot template.
  - Timing and event segmentation in the template should generally be respected to maintain global subtitle synchronization across languages.
- **Adjusting Timing**:
  - When Arabic grammatical structures or reading speed limits necessitate more space, translators may merge two short template events or split a dense event, provided shot change and duration rules are respected.
- **Key Names and Places (KNP)**:
  - Maintain a strict Key Names/Places glossary across episodes to ensure consistent transliteration of character names, fictitious entities, and pronouns/registers.

---

## 8. Product Supplemental & Marketing Assets

For trailers, social teasers, promo clips, and bonus content:
- **Audio Alignment Priority**: Subtitles must align tightly with audio rhythm, tone, and punchy pacing.
- **Reading Speed Flexibility**: Social media and fast-paced promotional trailers allow higher reading speeds (exceeding 20 CPS where justified) to keep taglines, comedic timing, and iconic slogans verbatim.
- **Preservation of Key Moments**: Never over-condense marketing hooks, jokes, or emotional payoffs for the sake of strict character counts.
