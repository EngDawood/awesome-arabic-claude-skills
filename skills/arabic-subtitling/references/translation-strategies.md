# Arabic Subtitling Translation Strategies & The FAR Quality Model
### Reference Guide for Interlingual Subtitling, Cultural Adaptation & Quality Assessment

This document outlines strategies for translating audiovisual dialogue into Modern Standard Arabic (MSA), handling culture-bound references (CBRs/ECRs), applying condensation techniques, and evaluating subtitle quality using the **FAR Model** (Pedersen, 2017).

---

## 1. Extralinguistic Cultural References (ECRs / CBRs)

Audiovisual dialogue frequently features culture-bound references (food, institutions, historical figures, pop culture, educational systems) that lack direct equivalents in the target culture. Following **Jan Pedersen’s (2005, 2017) ECR taxonomy**, subtitlers apply six primary strategies adapted for Arabic:

| Strategy | Definition | Arabic Subtitling Example | Context & Rationale |
| :--- | :--- | :--- | :--- |
| **1. Official Equivalent (المكافئ الرسمي)** | Established standard translation in dictionaries or official institutions. | *Supreme Court* &rarr; `المحكمة العليا`<br>*White House* &rarr; `البيت الأبيض` | Standard institutional vocabulary understood universally across the Arab world. |
| **2. Retention (الإبقاء / النقل الصوتي)** | Transliterating the source term phonetically, often placed in quotes if novel. | *Hogwarts* &rarr; `"هوغوورتس"`<br>*Halloween* &rarr; `"الهالوين"` | Preserves fictional universe names or widely recognized global phenomena. |
| **3. Specification / Explicitation (التخصيص والتوضيح)** | Adding a hypernym or clarifying classifier to aid immediate comprehension. | *Walgreens* &rarr; `صيدلية "والغرينز"`<br>*Smithsonian* &rarr; `متحف "سميثسونيان"` | Viewers have only seconds on screen; adding `متحف` or `صيدلية` clarifies the entity without pausing. |
| **4. Generalization (التعميم)** | Replacing a culture-specific term with its broader superordinate category. | *Twinkie* &rarr; `كعكة محلاة`<br>*Ivy League* &rarr; `جامعات النخبة` | Used when the specific brand is immaterial to the narrative and characters are simply snacking. |
| **5. Cultural Substitution (الاستبدال الثقافي)** | Replacing the source cultural item with a recognizable target-culture equivalent. | *straight A's* &rarr; `درجات ممتازة` (rather than literal `ألفات مستقيمة`) | Ensures natural idiomatic comprehension while avoiding over-localizing into regional dialect. |
| **6. Omission (الحذف)** | Omitting the reference when space/reading speed is constrained and context is visually self-evident. | *Let's stop at 7-Eleven on 5th Street.* &rarr; `فلنتوقف عند المتجر.` | Used when time limits force condensation and visual cues show the storefront clearly. |

---

## 2. Arabic Condensation & Syntactic Strategies

Subtitlers face severe space (42 characters/line) and time (20 CPS) constraints. Because spoken English often contains wordy verbal phrases, discourse markers, and pronouns, Arabic subtitlers use concise syntactic alternatives:

### A. Verbal Nouns (المصادر) vs. Relative Clauses
- **Source**: *After he had finished speaking to his brother...*
- **Literal/Wordy**: `بعد أن انتهى من التحدث مع أخيه...` (32 chars)
- **Concise (المصدر)**: `بعد حديثه مع أخيه...` (18 chars)
- *Saves 14 characters while elevating the literary register of the subtitle.*

### B. Active vs. Passive Voice
- While English frequently uses the passive voice, classical and modern standard Arabic favor the active voice or concise passive without agent:
  - English: *The suspect was arrested by the federal agents.*
  - Wordy/Awkward Calque: `تم اعتقال المشتبه به من قبل العملاء الفيدراليين.` (51 chars)
  - Natural Arabic (Active): `اعتقل العملاء الفيدراليون المشتبه به.` (36 chars)

### C. Pruning Discourse Fillers & Phatic Markers
- Spoken dialogue is laden with conversational fillers: *you know*, *well*, *I mean*, *actually*, *like*, *to be honest*.
- **Rule**: Unless a filler serves characterization (e.g., illustrating hesitation, deceit, or stuttering), omit it in subtitles:
  - *Well, actually, I don't really know.* &rarr; `لا أعلم في الحقيقة.`

### D. Eliminating Clunky Calques
- Avoid overusing synthetic constructions borrowed from English:
  - Avoid: `قام بزيارة` &rarr; Use: `زار`
  - Avoid: `قام بالاتصال به` &rarr; Use: `اتصل به`
  - Avoid: `السيارة الخاصة به` &rarr; Use: `سيارته`
  - Avoid: `بشأن هذا الأمر` &rarr; Use: `عن هذا الأمر` or `فيه`

---

## 3. Common Subtitling Errors & Student Pitfalls

In academic evaluations of student subtitlers (e.g., Pedersen 2017; studies on contemporary drama like *Wednesday*), the most recurrent errors are:

1. **Ill-Timed Line Splits (كسر الأسطر غير النحوي)**:
   - Splitting between a preposition and noun or adjective and noun forces the viewer's eye to process incomplete syntactic units.
2. **Orphan Words (الكلمة المعلقة)**:
   - Placing a single word (e.g., `دائمًا.`) on the second line destroys visual balance.
3. **BiDi & Punctuation Flip (انعكاس علامات الترقيم)**:
   - Using Western commas (`,`) and question marks (`?`) instead of Arabic (`،` and `؟`).
   - Ending lines with a period without checking whether the player flips it to the right-hand margin.
4. **Incorrect Arabic Number Inflections (أخطاء تمييز ومخالفة العدد)**:
   - Writing `خمسة نساء` instead of `خمس نساء`, or `عشرة أيام` vs `عشر سنوات`.
5. **False Friends & Literal Idiom Calquing**:
   - Translating *cold feet* as `أقدام باردة` instead of `تردد` or `تراجع في اللحظة الأخيرة`.

---

## 4. The FAR Subtitling Quality Assessment Model (Pedersen, 2017)

The **FAR Model** is an objective, error-based metric designed specifically for evaluating **interlingual subtitles**. It assesses subtitles across three independent dimensions:

```
                      ┌──────────────────────────────────────┐
                      │            FAR MODEL                 │
                      └──────────────────┬───────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│   FUNCTIONAL     │           │  ACCEPTABILITY   │           │   READABILITY    │
│   EQUIVALENCE    │           │                  │           │                  │
├──────────────────┤           ├──────────────────┤           ├──────────────────┤
│ • Semantic       │           │ • Grammar        │           │ • Line Length    │
│ • Stylistic      │           │ • Spelling/Hamza │           │ • Reading Speed  │
│                  │           │ • Idiomaticity   │           │ • Segmentation   │
│                  │           │                  │           │ • Punctuation    │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

### Pillar 1: Functional Equivalence (F)
Measures how accurately the subtitle renders the original speaker's meaning and aesthetic effect.

| Error Subcategory | Severity | Penalty Points | Description & Criteria |
| :--- | :--- | :--- | :--- |
| **Semantic Error** | **Minor** | **0.5** | Nuance or secondary meaning is slightly altered or softened, but core plot comprehension remains unimpaired. |
| | **Standard** | **1.0** | Subtitle misrepresents part of the dialogue, leading to a misleading or distorted statement. |
| | **Serious** | **2.0** | Total mistranslation. Meaning is inverted, unintelligible, or contradicts the visual narrative. |
| **Stylistic Error** | **Minor** | **0.5** | Slight mismatch in formality (e.g., overly formal phrasing in a casual conversation). |
| | **Standard** | **1.0** | Severe tonal clash (e.g., archaic Quranic phrasing in modern slang, or vulgarity where none was present). |

### Pillar 2: Acceptability (A)
Measures adherence to the grammatical, lexical, and stylistic norms of the target language (Modern Standard Arabic).

| Error Subcategory | Severity | Penalty Points | Description & Criteria |
| :--- | :--- | :--- | :--- |
| **Grammar** | **Minor** | **0.25** | Minor agreement flaw (e.g., feminine/masculine mismatch on a distant demonstrative). |
| | **Standard** | **0.5** | Noticeable grammatical breakdown (e.g., wrong dual/plural conjugation, violation of number rules *العدد والمعدود*). |
| | **Serious** | **1.0** | Syntactic breakdown rendering the sentence grammatically broken or unparseable. |
| **Spelling / Orthography** | **Minor** | **0.25** | Minor typo that does not form an erroneous real word; missing dot on `ة` vs `ه`. |
| | **Standard** | **0.5** | Blatant misspelling, incorrect *hamza* (*همزة الوصل وهمزة القطع*), or tanween on an illegal letter. |
| **Idiomaticity** | **Minor** | **0.25** | Unnatural or stiff Arabic collocation that sounds translated. |
| | **Standard** | **0.5** | Unacceptable calque (*ترجمة حرفية ركيكة*) that violates Arabic phrasing conventions. |

### Pillar 3: Readability (R)
Measures whether the subtitles can be comfortably read in a fluid, non-intrusive manner within the technical audiovisual constraints.

| Error Subcategory | Severity | Penalty Points | Description & Criteria |
| :--- | :--- | :--- | :--- |
| **Line Length** | **Minor** | **0.25** | 43–44 characters per line (slight overflow). |
| | **Standard** | **0.5** | $\ge$ 45 characters per line, or $\ge$ 3 lines on screen. |
| **Reading Speed** | **Standard** | **0.5** | 21–23 CPS (uncomfortably fast for dialogue). |
| | **Serious** | **1.0** | $\ge$ 24 CPS (virtually impossible for average viewers to read). |
| **Line Segmentation** | **Minor** | **0.25** | Awkward visual balance (top-heavy two-liner). |
| | **Standard** | **0.5** | Grammatically split constituent (e.g., split between verb and subject or mudaf/mudaf ilayh) or single orphan word on line 2. |
| **Punctuation & Layout** | **Minor** | **0.25** | Using ASCII `...` instead of Unicode `…`; minor space before comma. |
| | **Standard** | **0.5** | Inverted punctuation mark on wrong side due to BiDi bug; double punctuation (`؟!`). |
| **Spotting & Shot Cuts** | **Minor** | **0.25** | Subtitle straddles a shot change by 1–2 frames unnecessarily. |
| | **Standard** | **0.5** | Glaring desynchronization ($\ge$ 1 second early or late) or flash gap (< 2 frames). |

---

## 5. Scoring & Quality Threshold Calculation

To benchmark subtitling work across translators or student cohorts, calculate the **Normalized Error Score**:

$$\text{Error Score per 100 Subtitles} = \left( \frac{\text{Total Penalty Points}}{\text{Total Number of Subtitle Events}} \right) \times 100$$

### Quality Threshold Benchmarks:
- **$\le 5.0$ Penalty Points / 100 Events**: **Professional / Broadcast Quality (Pass)**.
- **$5.1 - 10.0$ Penalty Points / 100 Events**: **Acceptable with Minor Revisions**.
- **$10.1 - 15.0$ Penalty Points / 100 Events**: **Borderline / Requires Significant QC Overhaul**.
- **$> 15.0$ Penalty Points / 100 Events**: **Unacceptable / Fail (Re-translation required)**.
