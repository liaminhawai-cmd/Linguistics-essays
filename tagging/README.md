# /tagging — auditable quantitative layer

**Every numeric figure cited in `/essays` is regenerable from here.** If a number
in an essay can't be reproduced by running the script below, it's a bug — report it.

## Files
- `lexicons.json` — the exact token lists for each metric, plus the ad-strip
  markers and timestamp regex. Edit metrics **here**, never in code. Glosses
  document construct caveats and deliberate exclusions (e.g. "I mean" out of
  hedges, "creepy" out of disgust) with the reason.
- `count.py` — reads `lexicons.json`, runs it over `/transcripts`, writes
  `counts.json`. Strips ASR timestamp markers and (BC only) dynamically-inserted
  iHeart ad sentences before counting.
- `counts.json` — per-episode output: `words_after_strip`, `ad_words_stripped`,
  and for each metric **`raw` count and `per_1k` rate**. Raw counts are committed
  so small-n fragility is visible: a "12–0" dissociation is a whole-episode total
  from a compact lexicon — suggestive, not proof.

## Regenerate
The transcripts are kept in a private repository, so this only runs where you have them in a `transcripts/` folder next to `tagging/`. `counts.json` is the committed output.
```
python3 tagging/count.py              # rewrite counts.json for all 26 transcripts
python3 tagging/count.py casino       # print just the matching files to stdout
```

## Discipline (learned the hard way — see FINDINGS C3)
1. **Stand this up before citing figures, not after.** The first ad-hoc script
   had a case-sensitivity bug that undercounted sentence-initial "My"/"Me" and
   manufactured a spurious first-person "inversion" in the Casino Royale essay.
2. **Lexicon choice moves the numbers.** Including "creepy"/"cringe" in disgust
   lifts KJB's Casino Royale count 3→8 and erodes the H3 dissociation. The lists
   are frozen to the brief §7 tokens (hedges) and to recoil-at-the-object terms
   (disgust); changing them is a methodological decision, logged.
3. **These are crude regex passes over ASR text.** They are directional evidence.
   Hand-check a sample before resting a claim on any count — this is why H3 was
   demoted from a lexical to a hand-coded functional claim (essay 03).
4. **Report raw alongside rate**, always, so the reader can see the n.

`/tools/superseded/register_counts.py` is the superseded ad-hoc script, kept only for
provenance; do not cite its output. `tagging/count.py` is canonical.

## The extended in-joke test
`ingroup_extended.py` → `ingroup_extended.json`. Runs the in-joke word list (original and a spelling-calibrated version) over the 23 full KJB episodes in broadcast order, including those in `transcripts/kjb_unpaired/`, and reports where the scoring segment starts, density inside and outside it, whether SCUM is spelled out, and which wording of the third axis is recited. Behind essay 11. Kept separate from `counts.json`, which covers only the matched pairs.
