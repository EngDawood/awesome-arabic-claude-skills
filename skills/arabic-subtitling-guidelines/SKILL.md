---
name: arabic-subtitling-guidelines
description: Guidelines and QC tooling for adding Arabic subtitles or captions to video - Arabic-to-Arabic captions (transcription, SDH) and translated subtitles (English or other language into Modern Standard Arabic). Covers Netflix Timed Text Style Guide rules (42 chars/line, 2 lines, reading speed, timing/gaps/shot changes, numbers, quotes, ellipses, diacritics, songs, forced narratives), translation strategies for cultural references, and an SRT/VTT checker script. Use this skill whenever the user wants Arabic subtitles, captions, ترجمة فيديو, ترجمة مرئية, تفريغ نصي, تسميات توضيحية, SRT/VTT/TTML files, burning captions into a video, translating a video transcript to Arabic, or reviewing/fixing existing Arabic subtitles - even if they never say "Netflix" or "style guide".
---

# Arabic subtitling and captioning guidelines

Rules and workflow for producing Arabic subtitles that read like professional work. The baseline standard is the Netflix Timed Text Style Guide (TTSG) for Arabic, because it is the most detailed public specification. Loosen it for casual platforms; do not invent stricter rules than the source.

## Pick the mode first

| Mode | Input -> output | Extra concerns |
|---|---|---|
| **A. Arabic captions** | Arabic speech -> Arabic text (same language) | Faithful transcription, MSA vs dialect, SDH sound cues if requested |
| **B. Translated subtitles** | Other language speech -> Arabic text | Translation strategy, cultural references, condensing for reading speed |
| **C. Review / fix** | Existing SRT/VTT/TTML | Run the checker, then fix by rule |

If the user does not say, infer from the request. Ask one short question only when it changes the output: target platform (Netflix-style delivery vs YouTube/TikTok/burned-in), and whether SDH cues (sound labels, speaker IDs) are wanted.

## Workflow

1. **Get a timed source.** Use the user's transcript/SRT. If there is only audio/video, transcribe with timestamps first (word- or phrase-level). If the `video-caption-mcp` skill/server is available, it handles caption jobs and burn-in; this skill supplies the linguistic and timing rules.
2. **Segment** at clause level, never mid-phrase (see Line breaks). Aim for 1 line where possible.
3. **Translate or transcribe into Modern Standard Arabic (MSA).** For mode B, decide strategy per item using `references/translation-strategies.md`. Build a small term list (names, recurring terms) first and keep it consistent across the whole file.
4. **Apply text rules** from the cheat sheet below; details and rationale in `references/netflix-arabic-rules.md`.
5. **Time it** (in-time on first audio frame, out-time about half a second after audio if nothing follows, chain gaps, respect shot changes).
6. **Run the checker:** `python scripts/check_subtitles.py file.srt --fps 24` and fix errors. Use `--fix out.srt` for the mechanical ones, then re-check. Mechanical timing fixes do not know about audio or shot changes, so review them.
7. **Manual QC pass** with the checklist at the end. Report anything you could not verify.

## Cheat sheet (Netflix Arabic TTSG)

**Language**
- MSA only. No dialect words (the guide's examples: برجاء، يا خبر، يا ستّار). Where MSA has no equivalent, use the closest-meaning word.
- Translate place names and currencies to Arabic forms (المكسيك، أثينا، اليورو، البيزو). Never convert currency values.
- Proper/character names: transliterate, first name before last name. Nicknames: transliterate unless the meaning matters to the plot.
- Do not translate onomatopoeia ("wow", "ouch") in subtitles; do not translate fillers ("just", "really", "you know") unless they add meaning. Do not reproduce deliberate mispronunciations unless plot-relevant.
- Never censor; render profanity faithfully without adding obscenity the source lacks.
- No italics at all in Arabic.

**Layout**
- Max 42 characters per line, max 2 lines, prefer bottom-heavy two-liners, avoid a single word alone on line 2.
- Do not break a line between: verb and subject, particle and verb, adjective and noun, mudaf and mudaf ilayh, exception particle and excepted, vocative particle and vocative, preposition and its noun, number and counted noun.
- Dual speakers: hyphen + space at the start of each line, one speaker per line, each line a self-contained sentence.
- Font placeholder Arial-like sans-serif, white, size that fits 42 characters.

**Timing**
- Duration per event: min 5/6 s (20 frames at 24 fps), max 7 s.
- Reading speed: adults up to 20 chars/s, children up to 17 (SDH: 23 and 20).
- Min gap 2 frames. At 24 fps, gaps of 3-11 frames must be closed to 2; gaps are either 2 frames or >= half a second.
- In-time within 1-2 frames of first audio. If no subtitle follows, out-time about half a second after audio ends. Avoid crossing shot changes unless the dialogue crosses them.

**Punctuation and symbols**
- Ellipsis is the single character U+2026, never three dots. Use it for trailing off, interruption, pauses of 2 s or more, and a sentence interrupted by another speaker/FN (before and after the interruption). Do not put an ellipsis or dash between two subtitles when a sentence simply continues.
- No space before comma, question mark, exclamation mark. Never `?!` or `!?`. Repeat the conjunction instead of using a comma between list items (المدونون والمترجمون والمترجمون الشفويون).
- Quotes: straight double quotes, no inner spaces; one opening at the start of the quotation and one closing at its end, not per subtitle. Add kashida before the quote when ال precedes it (الـ"برونكس"). Use quotes for song titles/lyrics, transliterated names in SDH cues, and when characters read aloud.
- Hashtags/emails/websites: no Latin letters. Transliterate or use وسم/هاشتاغ; on-screen ones become "على الموقع/البريد الإلكتروني الظاهر على الشاشة".

**Numbers**
- 1-10 in words with correct gender/agreement (رجلين اثنين، خمس سيدات); above 10 in numerals; may break for space, reading speed, lists, figures of speech.
- Ordinals 1-9 in words (الموسم الأول); 10+ numerals with kashida (الـ21).
- Thousands separator comma (1,234), no comma in years (1940), decimal point with leading zero (0.5).
- Percent spelled out; currency spelled out; time on a 12-hour basis with Arabic day-part words; Gregorian month names (أغسطس not آب); metric units unless plot-relevant.

**Diacritics** only where their absence changes meaning (shadda in شابّ/شابَ, passive verbs, feminine plural nun, ya of the speaker, etc.). Tanween fatha goes on the letter before the alef for Netflix rendering reasons.

**Forced narratives (on-screen text) and foreign speech**
- Subtitle on-screen text only if plot-relevant and not already covered in dialogue; put it in straight double quotes; never mix it with dialogue in one event; time it to the on-screen text.
- Translate foreign dialogue only if the viewer was meant to understand it. For Arabic-language content, only full foreign sentences get an FN, not single words like "Hello".

**SDH** (only if requested): square brackets for sound/speaker cues, lowercase except proper nouns, indefinite form for sounds ([زقزقة عصافير]), ♪ with spaces around lyrics, higher reading-speed limits, cues in MSA even in dialect content.

## Handling conflicts and gaps in the sources

- The Arabic TTSG overrides other Netflix guides for Arabic. Where the English template guide says hyphen without space for dual speakers, Arabic says hyphen + space.
- The timing guide says 20 frames minimum and calls it "4/5 s"; 20 frames at 24 fps is 5/6 s, which matches the General Requirements. Use 5/6 s.
- Netflix delivers TTML with percentage-based positioning; SRT/VTT cannot express all of it. If the user needs Netflix delivery, say so and follow the General Requirements technical section (`references/netflix-arabic-rules.md`).
- Not verified: the Arabic transliteration/translation guideline and profanity guideline pages (linked from the Arabic TTSG) and the Netflix Glyph List could not be fetched. Tell the user these were not applied; for profanity or unusual transliteration, ask them to check those pages.

## RTL practicalities

- Save as UTF-8. Some players show a trailing period on the wrong side; prefix each line with U+200F (RLM) if needed, and test in the target player. This is general practice, not a Netflix rule.
- Subtitle editors need right-to-left mode on or punctuation will look wrong.
- For burned-in video, pick a font with full Arabic shaping support; check that diacritics do not collide between the two lines.

## QC checklist (manual)

- Meaning matches audio; no invented content; idioms and cultural references handled deliberately.
- Same term/name translated the same way throughout.
- No dialect words; register matches the source.
- Reading speed feels comfortable when watched back; no flashing gaps.
- Line breaks fall at clause boundaries; no orphan word on line 2.
- Numbers, quotes, ellipses, italics, Latin letters, brackets checked (the script covers most).

For scoring translated work (students or vendors), use the FAR model in `references/translation-strategies.md`.

## Reference files

- `references/netflix-arabic-rules.md` - full rule set: Arabic TTSG, General Requirements, Timing Guidelines, Template/pivot notes, Product Supplemental notes. Read when a case is not covered by the cheat sheet.
- `references/translation-strategies.md` - strategies for culture-bound references, common student errors, FAR quality model, based on a study of student subtitling of Wednesday. Read for mode B and for evaluating translations.
- `scripts/check_subtitles.py` - checker/fixer for SRT and VTT. Run with `--help`.
