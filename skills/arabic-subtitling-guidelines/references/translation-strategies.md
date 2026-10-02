# Translation strategies for culture-bound references (English -> Arabic subtitling)

Based on: Mirza, Tarhini & El-Ahmar, "Arabic Subtitling of Cultural References in Netflix's Wednesday: A Case Study at the Islamic University of Lebanon" (student corpus study). Use this to choose a deliberate strategy per cultural reference, and to QC/grade existing translations. Pair with the Netflix rules in `netflix-arabic-rules.md` for the mechanical side (chars/line, timing, punctuation).

## Strategy inventory (pick one per reference, and say why)

1. **Retention** — keep the source term as-is or transliterated with no further explanation. Best for globally recognized terms. Least intrusive, but can confuse a viewer with no source-culture background if overused.
2. **Specification** — add a clarifying detail the source left implicit, so the Arabic audience doesn't miss the point. Good for references that are opaque without context.
3. **Direct translation** — literal rendering, word for word or close to it. Works when the source and target cultures share the concept.
4. **Generalization** — replace a specific cultural item with a broader, more universal term. Useful when the specific item has no Arabic cultural footprint, but it flattens nuance — avoid using it as a default fallback.
5. **Substitution** — replace with a different, culturally familiar equivalent that serves the same narrative function. The most-used strategy in the study (22.86% of extracts); effective for idioms and culture-bound humor, but can drift from the source if overused.
6. **Omission** — drop the reference entirely. Last resort: only when the reference is untranslatable, non-plot-pertinent, and would cost more reading-speed budget than it's worth.
7. **Official/established equivalent** — use a standardized, previously published Arabic translation (official titles, brand names, religious/historical terms). Was the least-used strategy in the study (5%) — check for one before assuming it doesn't exist; official equivalents raise consistency and credibility.
8. **Equivalence** — functional match with a different surface form but the same effect (closest to substitution but driven by effect/register rather than imagery).
9. **Modulation** — shift in point of view, voice, or category (e.g. active -> passive, abstract -> concrete) to make the sentence land naturally in Arabic.
10. **Adaptation/simplification** — loosen or simplify to increase clarity, usually under reading-speed or character-count pressure.
11. **Borrowing** — import the term with no change, relying on established crossover usage (the study's example: keeping "zombies").

### Choosing a strategy
- Prefer official/established equivalent first if one exists and is widely recognized.
- Prefer substitution or specification over generalization when the reference matters to the joke, plot, or characterization — generalization was linked in the study to loss of nuance and richness.
- Use retention/borrowing for terms the target audience already knows globally (brand names, globally diffused pop-culture terms).
- Use omission sparingly and only as dictated by space/time, not convenience.
- Keep one strategy per term consistent across the whole asset — switching strategies for the same recurring reference reads as careless.

## Common failure patterns to avoid (from the study's error analysis)

- **Misreading unfamiliar references** — idioms, fictional character names, or culturally loaded phrases (the study's examples: "Scooby gang", "pilgrim", "emotional Morse code") get mistranslated or dropped when the translator doesn't recognize the source. Research the reference before choosing a strategy; don't guess from the literal words.
- **Flattening idioms/metaphors with no Arabic equivalent** (e.g. "heebie-jeebies", "mansplaining") into an over-general phrase that loses the original's register or humor. Consider substitution with an Arabic idiom of similar weight before defaulting to a flat paraphrase.
- **Reactive strategy switching under character-limit pressure** — picking whatever strategy fits the space rather than the one that best preserves meaning. Decide the strategy first, then edit for length within it.
- **Inconsistent strategy choice for the same type of reference** across one asset, with no clear rationale — undermines viewer trust and tone.
- **Treating subtitling as prose translation** — ignoring line-break, timing, and reading-speed mechanics is itself a source of acceptability and readability errors (see Netflix rules), not just a technical afterthought.

## FAR model — quality scoring (Pedersen's model, as applied in the study)

Use this to grade or self-check a batch of subtitles. Three top-level error categories; log each instance against a Minor/Standard/Serious scale where applicable.

### Functional equivalence
- Does the subtitle preserve the communicative function and semantic content of the source? Idioms and metaphors are the highest-risk spot — the study found frequent minor/standard/serious semantic errors concentrated here. For each subtitle, ask: would an Arabic-only viewer get the same information and tone a source-language viewer gets?

### Acceptability (target-language correctness and naturalness)
- Grammar errors (minor and serious)
- Spelling errors
- Idiomaticity errors (minor and standard) — translated text that is grammatically correct but doesn't read as natural Arabic
- These disrupt natural flow even when the meaning is technically preserved — fix for native-reader naturalness, not just correctness.

### Readability (mechanical/technical)
- Excessive line length (the most frequent readability issue in the study — directly tied to the 42-char/line limit)
- Punctuation errors
- These are usually catchable mechanically — run `scripts/check_subtitles.py` before a manual pass.

### Using FAR for review
1. Go subtitle by subtitle; tag each error found under Functional / Acceptability / Readability, with a severity (minor/standard/serious) where the category supports it.
2. Prioritize fixing Functional errors first (they change meaning), then Acceptability (they damage naturalness), then Readability (mechanical, often fixable by the script).
3. For a vendor/student quality report, tally error counts and rates per category like the study's Table 2, and call out which specific reference types (idioms, culture-bound names, metaphors) are driving the errors — that's more actionable than an aggregate score.
