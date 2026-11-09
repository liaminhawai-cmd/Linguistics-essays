# Synthesis IV — Methods, instruments, and caveats

This chapter is the project's conscience. It exists because the strongest claims in the book (Chapters II and III) are exactly the kind that a motivated reader could manufacture out of a transcript corpus by selective quotation and a flattering theory, and the only thing separating this study from that failure mode is the discipline recorded here. The brief that governs the work warns, in Schröder's words, against "attending to a small subset of salient variables at the expense of complexity," and against the "flattering just-so story." Those are not decorative cautions. They are the standard every chapter is held to, and this chapter documents the machinery that enforces it.

## The corpus and its shape

The corpus is matched film pairs — films covered by *both* Kill James Bond and The Bechdel Cast — analysed in KJB-chronological order. Eight pairs are full-length on both sides and carry the hypothesis stack; a ninth, composite chapter (essay 09) handles five further pairs where KJB exists only as ten-minute Patreon previews against BC full episodes, and is restricted by construction to matched-window register analysis with no full-episode claims. The transcripts are machine ASR (Whisper-class), which has two consequences the methods must respect: speaker attribution inside a multi-host show is unreliable (so intra-show idiolect work was attempted and parked — see below), and verbatim quotation must be handled carefully because the ASR garbles lines. Quotation discipline throughout is strict: direct quotes are kept under fifteen words, used sparingly, one per source passage, with paraphrase as the default.

## The confound, restated as a method

The central methodological fact is n=2 with total confound alignment: format, nationality, monetisation, gender-socialisation, and era of recording all covary across the two shows (Chapter I). This is not a limitation to be mitigated; it is a boundary on what can be claimed, and the method is to *respect the boundary explicitly* rather than write around it. No single-cause attribution is ever made. Where a difference is striking, the move is to name the whole confound stack that predicts it and to decline to pick a winner. The two natural experiments in the archive (the live/studio perturbations of each show) are the only places a single variable — audience presence — is isolated cleanly, and they are treated as the load-bearing causal evidence precisely *because* they are the only places the confound briefly comes apart.

## The auditable counting pipeline

The highest-priority methodological commitment, and the one that most distinguishes this study from an impressionistic reading, is that **every quantitative figure in every essay is regenerable.** The `/tagging` directory holds the instrument: frozen token lexicons (`lexicons.json`), a canonical counter (`count.py`) that reads them, strips timestamps and the dynamically-inserted iHeart ads from BC files, and emits per-episode raw counts and per-thousand-word rates to `counts.json`. Any figure cited in the book can be reproduced by running `python3 tagging/count.py`. Three principles govern its use:

1. **Raw counts sit beside rates**, so small-n fragility is always visible. A rate computed over a short window or a thin token-count is not allowed to hide its own instability.
2. **The lexicons are frozen and their exclusions documented.** The disgust lexicon deliberately excludes "creepy" and "cringe" (descriptive, not recoil); "I mean" is excluded from hedges. These choices are recorded in the lexicon glosses *with* the worked example of what including them would do (including "creepy"/"cringe" lifts KJB's Casino Royale disgust from 3 to 8 and erodes the H3 dissociation) — so the reader can see exactly which judgement calls the figures depend on.
3. **Counts are interrogated, not believed.** This is the single most important methodological theme in the book, and it earned its place by nearly causing two errors in opposite directions (below).

## Function, not lexical shadow

The unit of analysis is the *function* of an utterance, never the lexical token that shadows it. This principle was forced by two near-misses that point in opposite directions, which is why it is trustworthy rather than convenient. In the Ocean's studio test (essay 04), ten apology tokens that a raw counter reads as repair *all* hand-code as something else — rhetorical softening, mock-apology to the listener, in-character voicing — so that the raw count alone would have *falsified* a true hypothesis (H4). In the Austin Powers case (essay 03), over-trusting a lexical disgust/anger dissociation that *failed to replicate* nearly preserved a claim that needed demoting, and H3 was correctly demoted to a hand-coded functional claim. One error would have rejected a truth; the other would have kept a falsehood. The lexicons exist to *locate* candidate phenomena; the verdict always rests on hand-coding what the located utterance is doing.

A boundary the third-pole test (essay 10) made vivid: **lexicons do not transfer across media.** The frozen speech lexicons scored *zero* disgust on the most purity-saturated text in the entire project (a Christian content review built on "perversion" and "fouling their minds"), because written prose carries affect in moral content-vocabulary rather than the spoken recoil tokens the lexicons were built from; and the pool's one profanity "hit" was a writer *quoting* a slur to condemn it. Cross-medium rate comparisons (prose vs speech, or bleeped auto-captions vs clean ASR) are therefore never made — within-medium comparison plus hand-coding of function is the rule, and the third-pole counts live in their own file (`third_pole/third_pole_counts.py`) precisely so they can never be mistaken for corpus rates.

## Corrections as method, not embarrassment

The corrections log (in FINDINGS) is kept as a first-class methodological artefact, because the *pattern* of the errors is itself a finding about how to do this work. Four corrections, four lessons:

- **C1** (the SCUM rubric falsifies a pre-corpus claim that KJB is "allergic to a fixed metric"): confident structural claims about a show require sampling across its eras, not a memorable clip.
- **C2** (The Rock dated from in-text evidence to ~2021, overturning the brief's claim that Atomic Blonde was the earliest KJB): date every episode from in-text evidence before using it in an era argument — and never date an episode by its embedded ads, since BC's iHeart ads are inserted at scrape time and postdate the content by years.
- **C3** (a case-sensitivity bug in an early ad-hoc counter manufactured a spurious first-person "inversion" in the Casino Royale essay): stand up the auditable pipeline *before* citing figures, not after. The corrected near-tie actually *sharpened* the underlying point (count function, not frequency).
- **C4** (a BC file wrongly inferred truncated from its end-timestamp turned out complete): check the actual ending for the ritual markers; do not infer truncation from a timestamp.

The through-line is that every correction came from checking a confident claim against primary evidence, and three of the four overturned something the project had taken on trust. The corrections are logged in full and the affected figures were repaired against the canonical counts; nothing is quietly amended.

## Pre-registration

Where a claim was vulnerable to confirmation bias — most acutely the Point Break status-inversion prediction, because a pre-corpus analysis of that film was already on record — the prediction was *written down before the transcripts were read* (FINDINGS, Q15) and reported against its registered text with no post-hoc editing. That prediction was largely *falsified*, and the falsification produced the sharper finding (BC runs flat peer-collaboration, not a deference economy — Chapter III). Pre-registration is kept in the method toolkit precisely because its value showed up as a *wrong* prediction that the discipline forbade quietly revising into a right one.

## The Schröder lens — use discipline

The *Fight Like an Animal* corpus is used as a **generative lens, not a subject**: it supplies a disposition axis (approach/egalitarian versus avoidance/authoritarian; reactive versus proactive aggression; purity-disgust as the authoritarian affective signature) that names patterns in the data without claiming to *cause* them. The discipline around it is explicit and non-negotiable:

- The warrant for importing it at all is that *both shows reach for its distinctions unprompted* (KJB scoring SCUM's violence axis on the reactive/proactive split; BC's folk reactive-aggression theory). The lens is licensed by the data, not imposed on it.
- It is **never causal**. The affect-grammar inversion (BC enforces through the authoritarian-coded pole) explicitly does *not* make BC authoritarian; the finding is that affective grammars are *detachable* from political content.
- The Schröder source transcripts are themselves machine-ASR, so the lens is *paraphrased*, never quote-mined from garbled lines.
- And the absolute boundary: **the lens is never routed near H15 / anyone's medical history**, in the essays or in the reasoning behind them. The disposition axis is applied to register and discourse structure only.

## The H15 prohibition

The hardest rule in the project, stated once more because it governs everything: there is no speculation about any host's medical history, transition details, or diagnoses beyond their explicit public statements — in the essays, in the synthesis, or in internal reasoning. H15 is held, never asserted. Positionality (Chapter III) is analysed only at the level of stated public position and identification vector. Where an analysis seems to want to reach past that line, the line is the answer: it stops.

## Era as a live variable

Era is never assumed neutral. The KJB recordings span roughly 2021–2026 and the BC recordings roughly 2017–2020, and the era gap on a given pair runs from a few years to seven (F&F). The method treats era as a genuine threat to every cross-show comparison — and then *tests* it rather than assuming it away. The decisive result (Chapter II) is that the convergence holds across the maximal seven-year gap, which licenses the conclusion that era is a live variable that *fails to break* the convergence rather than one that *manufactures* it. That conclusion is only available because era was treated as a threat first.

## What the method cannot do, stated plainly

It cannot decompose the confound: no single cause of the two economies can be isolated from n=2. It cannot do intra-show idiolect analysis: ASR attribution is too poor, and the attempt (essay 03, the live show where voices are most differentiated) established only that live format differentiates *roles* — drop-operator, lecturer, notes-holder — better than it differentiates *individuals*. It cannot extend the preview pairs to full-episode convergence claims. And it cannot turn the altitude hypothesis (H17c) into a settled finding, because that claim is over-determined by three aligned causes; the method's honest output there is orthogonal axes and open falsifiers, not a verdict. Naming these limits is not hedging. It is the same commitment that keeps the rest of the book's claims worth the paper: the study says exactly as much as two podcasts can support, and stops there.
