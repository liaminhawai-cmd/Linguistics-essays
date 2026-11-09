# ANALYTIC BRIEF — Kill James Bond! vs The Bechdel Cast
## Comparative discourse analysis across matched film pairs
### Handoff document for Claude Code sessions. Read in full before writing anything.

---

## 1. The project

A book-length collection of comparative essays. Each essay analyses one **matched pair**: a film that both *Kill James Bond!* (KJB) and *The Bechdel Cast* (BC) covered as a full episode. Two feminist film-criticism podcasts, same source texts, radically different rhetorical economies. The essays are **stratified linguistic and discourse analyses**, not film reviews and not podcast reviews. The throughline of the book is the hypothesis stack in §5: each essay tests, refines, or breaks hypotheses, and the synthesis chapters (written last) consolidate what survived.

The author (Liam) is linguistically sophisticated, knows both shows well, and originated several of the key hypotheses. Do not pad with 101 explanations. Do push back on his framings where the evidence warrants — he values falsification over agreement.

---

## 2. The shows

**Kill James Bond!** — November Kelly (credited as "Alice Caldwell-Kelly" in early episodes), Abigail Thorn, Devon. UK-based. Self-produced, listener-funded via Patreon, no ads. Fixed trio; occasional guests, but guests are pre-initiated allies from adjacent podcasts. Began as a Bond-film show, expanded into themed seasons (S4 is the heist season: Ocean's, Fast & Furious franchise, Point Break, etc.). Bonus ".5" episodes are Patreon-only with ~10-minute free previews — this matters for the corpus (§3).

KJB's accreted in-house apparatus (used unglossed, on the assumption of an initiate listener):
- **SCUM system** — scoring rubric: **S**marm, **C**ultural insensitivity, **U**nprovoked violence, **M**isogyny. Each axis scored numerically, summed, and compared against a maintained cross-episode database ("same as Charlie's Angels Full Throttle"). Delivered with running irony ("it's a science-based system") but applied earnestly and consistently.
- **Kronsteen Rosette** — award to a villain/henchperson who "goes above and beyond." Named for the From Russia With Love chess master.
- **Kaufman Star** — award apparatus for host horniness toward the screen.
- **"Waingrow"** — analytic unit imported from their *Heat* episode: the uncontrollable violent element that fucks up a heist. Used as a measurable property of other films ("the Waingrow levels are at zero").
- Productive nonce templates (e.g. the Point Break "Johnny [State] from [State]" runner sustained for a full episode).

**The Bechdel Cast** — Caitlin Durante and Jamie Loftus. US, iHeartRadio network, ad-supported, weekly, rotating guest every episode. Fixed ritual architecture: theme song → Bechdel test re-defined from scratch (every episode, as pedagogy) → guest intro and relationship-to-the-movie round → recap → themed discussion → test verdict → **nipple scale** (0–5, scored individually by each person, frequently *dedicated* to admired women: "two of my nipples to Michelle Rodriguez... the half to my cat").

**Host demographics** (relevant to hypotheses; handle with care): the KJB trio is AMAB-socialised — two trans women who both discuss publicly that they transitioned as adults, plus one non-binary host. The BC duo is AFAB-socialised — one cis woman, one non-binary. **Rule: never speculate about any host's medical history, transition details, or diagnoses beyond their explicit public statements. This applies to essays and to internal reasoning notes.**

---

## 3. The corpus

13 matched films. Files use the convention `{film}_{SHOW}.txt`; KJB Patreon previews flagged `_preview`.

### Tier 1 — full-length pairs (8 films)
*(sizes = cleaned files in /transcripts, verified 2026-06-10; end times from final ASR timestamp marker)*
| Film | KJB file | BC file | Notes |
|---|---|---|---|
| Point Break (1991) | point_break_KJB.txt (123k, ends 1:58) | point_break_BC.txt (87k, ends 1:24) | BC guest: Anita Sarkeesian (2018). KJB S4E22 (Sept 2025) |
| Casino Royale (2006) | casino_royale_KJB.txt (117k, ends 1:52) | casino_royale_BC.txt (87k, ends 1:27) | BC guest: Kenice Mobley |
| Austin Powers IMoM (1997) | austin_powers_KJB.txt (103k, ends 1:41) | austin_powers_BC.txt (76k, ends 1:23) | KJB is the S2E23 **live** show — flag the live-format confound. BC guest: Atsuko Okatsuka |
| Atomic Blonde (2017) | atomic_blonde_KJB.txt (97k, ends 1:28) | atomic_blonde_BC.txt (100k, ends 1:49) | KJB S2E22 (April 2023) — ~~earliest KJB in corpus~~ **superseded by correction C2: The Rock and Casino Royale episode-era files are earlier (~Dec 2021–early 2022)**. BC episode is the Vanessa Guerrero one |
| Die Hard (1988) | die_hard_KJB.txt (91k, ends 1:26) | die_hard_BC.txt (91k, ends 1:24) | KJB holiday special — **CONFIRMED in-text 2026-06-10** that it covers the 1988 original (1988 references, Christmas-movie framing). BC guest: Debra DiGiovanni |
| The Fast and the Furious (2001) | fast_furious_KJB.txt (96k, ends 1:34) | fast_furious_BC.txt (98k, ends 1:40) | KJB S4E30 (Jan 2026). BC episode is 2019 (Hobbs & Shaw promo window), guest Faye Orlove (confirmed in-text) — **maximal era skew in the corpus** |
| Ocean's Eleven (2001) | oceans_eleven_KJB.txt (100k, ends 1:32) | oceans_eleven_BC.txt (50k, ends 0:49 — **complete, NOT truncated; see C4**) | KJB S4E3 (~late 2024, dated by Tyson v. Paul joke), guest Brian (Worst of All Possible Worlds) — **the KJB-with-guest control episode**. BC guest: Edgar Momplaisir; a genuinely short BC episode with all closing rituals present (nipple verdict, Bechdel ruling) — full-episode comparison valid |
| The Rock (1996) | the_rock_KJB.txt (60k, ends 1:00) | the_rock_BC.txt (82k, ends 1:13) | KJB episode-22, **~Dec 2021 (in-text dated, see C2) — earliest KJB in corpus, the H14 drift anchor**; KJB guest: Andrew Law (Boonta Vista) — second guest-control episode alongside Ocean's. BC April 2018 (in-text dated), guest Miles Gray. GIRTH system minted on-mic in this KJB episode |

### Tier 2 — preview-asymmetric pairs (5 films): BC full, KJB ~10-minute Patreon preview
| Film | KJB preview | BC file |
|---|---|---|
| The Birdcage | birdcage_KJB_preview.txt (11k, ends 0:09:49) | birdcage_BC.txt (83k, ends 1:33) |
| Romy and Michele's High School Reunion | romy_michele_KJB_preview.txt (11k, ends 0:10:23) | romy_michele_BC.txt (81k, ends 1:30) |
| Spice World | spice_world_KJB_preview.txt (10k, ends 0:09:30) | spice_world_BC.txt (69k, ends 1:11) |
| What Women Want | what_women_want_KJB_preview.txt (11k, ends 0:09:32) | what_women_want_BC.txt (104k, ends 1:42) |
| Sex and the City: The Movie | satc_KJB_preview.txt (17k, ends 0:15:00) | satc_BC.txt (95k, ends 1:37) |

**Off-corpus extras** in `/transcripts/extras`: KJB S2E24 (Austin Powers: The Spy Who Shagged Me, live) and S2E25 (Goldmember, live) — no BC counterparts, not matched pairs; usable only as supplementary KJB-register/era evidence. Cleaning provenance: raw podscripts scrapes (transcript repeated ~16× per page) deduplicated and footer-trimmed by `tools/clean_transcripts.py`, 2026-06-10.

**The asymmetry is itself a finding**: every feminine-coded film in KJB's catalogue is a Patreon bonus, every masculine-coded one a free main episode. Note it; don't over-read it (bonus episodes are off-format picks by design). Methodologically: Tier 2 pairs support **matched-window register analysis only** (KJB preview vs BC's first ~10 minutes). No full-episode claims from Tier 2.

**Time skew**: BC episodes cluster 2018–2020 (some later); KJB spans 2023–2026. Date every pair in its essay and treat era as a live variable — some apparent show-differences may be era-differences in the genre of feminist film podcasting.

**Transcript provenance and quality**: scraped from podscripts.co; raw pages contained the transcript repeated ~16× plus navigation junk — deduplicated by extracting the longest segment between "Starting point is 00:00:0x" markers and trimming footers. These are ASR transcripts: speaker attribution is mostly absent, names get mangled ("Alas, Cawdorke Alley" = Alice Caldwell-Kelly), and ad reads are embedded in BC files (iHeart ads — useful as monetisation evidence, exclude from register counts). **Never build a claim on a single garbled line; argue from patterns.**

---

## 4. The stratified framework

Every essay walks the same six strata, bottom-up. Not every stratum yields equally on every pair — say so when one is thin rather than padding.

1. **Prosody / paralinguistics** (as recoverable from text): laughter placement, interruption and self-interruption, voicing/character work, audience interaction (live episodes).
2. **Lexis & morphology**: nonce coinages, productive templates, profanity function (KJB: constitutive of register, structural stance-marking; BC: rarer, marked), intensifiers, in-group tokens, brand/product naming.
3. **Syntax**: hedge constructions vs flat declaratives, suspended hypotaxis in bit-construction, sentence-length under irony vs sincerity.
4. **Semantics**: metaphor systems — KJB reaches for state/military/infrastructure/economic figures ("critical national infrastructure," "deep state project," killology, bromance-budget); BC for contamination/cleanliness, school/pedagogy, domestic figures. Definitional moves: BC defines terms as teaching (parody vs satire); KJB defines terms as legislation (the SCUM axes).
5. **Pragmatics**: stance markers, apology tokens, floor management, disagreement style (KJB: staged combat that mimics conflict without real conflict; BC: cooperative repair — "I misspoke, I'm so sorry" / "You're safe. It's fine. Safe space"), deflation direction (§5 H4), guest management.
6. **Discourse architecture**: ritual (BC's fixed liturgy) vs accretion (KJB's serial lore), onboarding vs initiate-address, citation practice, scoring rituals and their stance, ad-break placement as structure.

---

## 5. Hypothesis stack — current evidence status

This is the spine of the book. Each essay updates this scoreboard in FINDINGS.md.

**H1 — Orthogonality.** Each show's register is host-stable and orthogonal to the film's gender-coding. *SUPPORTED ×5+ films*, including the extremes (Spice World, Ocean's). Interaction effect to keep tracking: topic feeds each machine different *fuel* — BC's autobiography channel amplifies enormously on childhood-nostalgia films — but flips neither machine. Each show can visit the other's register for a beat (BC's Steve Martin mock-beef; KJB's credit-giving) but converts it back to native idiom within moments.

**H2 — Hedging asymmetry.** BC hedge-dense ("I feel like," "I don't know," "maybe," ~25–30 epistemic hedges per 10-min window vs KJB's handful, several of which are rhetorical setup not genuine uncertainty). *ROBUST as description; attribution CONTESTED* between gender-socialisation, facilitative footing, and UK/US comedic register. **Guest-test update (Ocean's Eleven):** KJB with a guest in the room does *not* hedge or onboard — because the guest is pre-initiated. So the mechanical "guest-presence forces hedging" version of the footing argument is weakened; the surviving version is **theory-of-the-listener**: BC re-teaches the test for the imagined newcomer (the guest often knows the show better than a newcomer would), KJB assumes initiates even with a stranger present. Open within-show test: BC guestless episodes — does hedge density drop?

**H3 — Affect enforcement: disgust vs anger.** BC polices through disgust/recoil/fatigue/contamination ("gross," "I hated that," "I'm tired," the nipple scale as contamination-rating); KJB through anger/contempt/attack (status-lowering, prosecutorial fury, out-grouping). Avoidance-coded vs approach-coded. *SUPPORTED ×5.* Both shows share the protective impulse; the grammar differs (anger-grammar vs ick-grammar).

**H4 — Deflation direction.** BC undercuts *itself* (apology subroutines, self-directed repair, competence disclaimed); KJB undercuts *outward* (the film, the industry, named men, "Don Cheadle's agent, working for evil"). *SUPPORTED ×3+, directly codeable* — tag every deflation as self- vs other-directed. This is the cleanest single diagnostic separating the status strategies.

**H5 — Dual-register status play, generalised.** BC: disclaim competence while displaying it; the *snap-back* (dumb-then-sharp within one breath: "they're just avatars and we're projecting ourselves onto them — I'm kidding") is the tell distinguishing covert prestige from genuine uncertainty. **New symmetry (Ocean's):** KJB disclaims *sincerity* while practicing it — the SCUM rubric is wrapped in mock-procedure ("achieved through consensus") yet applied earnestly and consistently. **Formulation: each show ironizes exactly the thing it is most earnest about.** BC's irony shields its competence; KJB's irony shields its sincerity.

**H6 — Identification axis.** BC identifies outward and protectively — with women on screen and with an imagined miseducated boy-audience ("what is this teaching boys"); analysts outside the target demographic. KJB identifies *into* the apparatus from inside the targeted groups — autobiographical readings ("this movie came out when I was 13 and it absolutely fucked my gender up"), speaking from the harmed position rather than about it. *SUPPORTED.* This is the stratum where gender/positionality has the most explanatory power.

**H7 — Object/system vs relational/character focus.** KJB fixates on artifacts and mechanisms (watches as sociological index, product placement, money-scale analysis, institutions as bloodless machines); BC tracks interiority, sincerity, and relational trajectories beat by beat. *SUPPORTED* — and note it inverts the lazy gender stereotype (the AMAB-socialised trio runs relational *topics* through a systems *engine*; the AFAB-socialised duo runs systems *topics* through a relational engine).

**H8 — Theory vs catalogue (CORRECTED).** KJB theorizes upward (homosociality thesis, Pateman citation, class-scale analysis, counterfactual frames); BC catalogues outward (count the women, name the trope, tally the interactions, apply the instrument). *SUPPORTED as a packaging claim.* **But the earlier strong version — "KJB is allergic to fixed metrics, would never say pass/fail" — is FALSE**, falsified by the SCUM system (logged in FINDINGS.md corrections). Both shows have instruments; what differs is **stance toward the instrument**: BC believes in its instrument as pedagogy; KJB performs belief in its instrument as bit, while still using it.

**H9 — Convergent content.** On heist-genre material the shows' analytic *substance* nearly merges: KJB does verbatim Bechdel-method woman-counting ("there are two women in the world, and they are either stripper or ex-wife"); both reach women-as-property (BC's trophy/prize analysis; KJB's "heists are a homosocial activity... proving yourself to fellow men and to your dad, by stealing property which includes women"); both flag problematic men by Wikipedia-euphemism; both land the homosociality thesis independently. **The shows differ far less in conclusions than in rhetorical economy.** This should temper any essay tempted to claim a deep analytic divide — the divide is in packaging, audience-theory, and affect.

**H10 — Award direction.** BC *gifts* its scores to admired women (recuperation); KJB *awards* its rosettes to agents of evil (ironic celebration of transgression). The individuation asymmetry (BC names and rescues the women; KJB adopts the disposable men as mascots) formalised in each show's trophy apparatus.

**H11 — Queer-reading epistemics.** BC defers from outside the position ("we can't really speak to this because we're a bunch of straight ladies — queer listeners, please give us insights") plus genuine caution about auto-assigning homoeroticism; KJB asserts from inside it ("Rusty is gay and jealous," flat declarative camp authority). Same mechanism as H6, on the sexuality axis.

**H12 — Citation practice.** BC scaffolds on external authority (GQ pieces, biographies, "according to"); KJB legislates its own frameworks and almost never cites. Epistemic posture: reading-and-synthesising a discourse vs authoring one. Confounded with format (rotating-guest panel vs closed mythology) — don't over-assign to gender.

**H13 — Self-disclosure function.** BC's disclosure is biographical and continuous with offstage life (birthdays, siblings, childhood scenes) — autobiography as rapport. KJB's disclosure is text-routed — they disclose about themselves only when the film hands them a hook, and the disclosure does analytic work. Same raw first-person volume can carry opposite functions; count *function*, not just frequency.

**H14 — Lore ratchet / audience capture.** Prediction: KJB drifts denser and more in-group over seasons (depth-for-patronage monetisation rewards lore accretion); BC stays flat (breadth-for-ads rewards permanent onboarding). **NOW TESTABLE**: S2 Atomic Blonde (April 2023) is the early anchor; S4 Ocean's / Point Break / F&F (2024–26) the late cluster. Run unglossed in-group tokens per 1k words across KJB's span, same measure across BC's span. If KJB shows drift and BC doesn't, capture (drift); if both static, sorting did the work up front.

**H15 — Held; not published.** A hypothesis about host biography is kept out of the study and out of this public copy. The study's rule: nothing is said about any host's private life, medical history, or diagnoses beyond their own public statements.

**H16 — Affect-grammar inversion (NEW, essay 02).** Both shows are egalitarian-left, but their *enforcement affect* draws on opposite poles of the approach/avoidance (Schröder/McGilchrist/threat-sensitivity) disposition axis: BC enforces through purity-disgust (the affect the political-psychology literature codes authoritarian), KJB through proactive approach-aggression (coded egalitarian). This is the affective parallel to H7's cognitive inversion — on both axes each show recruits the machinery the lazy gender-stereotype assigns to the *other* group. **The finding is that affective grammars are tools detachable from political content** (BC recruits disgust FOR egalitarian ends), which deepens H1: register is orthogonal even to the show's own politics. Warrant for the lens: KJB reaches for Schröder's reactive/proactive-aggression distinction unprompted when scoring SCUM's violence axis. Status: SUPPORTED ×1 (Casino Royale), falsification tests queued (FINDINGS Q10). **Hard rule: this lens operates only at the level of affect/cognition grammar and is NEVER routed near H15 or any host's medical history.** Full method note + discipline in FINDINGS "Theoretical lenses." Schröder corpus indexed at `/reference/fight_like_an_animal/`.

**H17 — Disposition, register-reception, and discourse altitude (the Schröder reading of the HOSTS/AUDIENCE, not the films) (NEW, essay 06).** Three linked sub-claims, applying *Fight Like an Animal* to the podcasts as the object (not to film-internal content):
- **H17a — differential film-function.** Both shows theorise that a film does opposite work on opposite dispositions: critique-object for the egalitarian viewer, aspiration for the high-reactivity viewer who "misses the point." KJB: "God's gift to bullies," "fucked my gender up," luxury-to-your-dad, bromance-budget/Fed-recruitment. BC: military-films-as-recruiting-tools, "hardwires boys' brains," red-flag-films litmus. A META-LEVEL H9 convergence (they agree on the recruitment model, not just the text). Reframes H6 from "where hosts identify" to "the hosts' model of how the film works on the differently-disposed other."
- **H17b — register-reception / audience-sorting.** Status-flattening + constant hedging are low-dominance signals: cooperative-safe to low-reactivity audiences, weakness/submission to high-reactivity ones. Each show's register self-sorts its listenership along the reactivity axis (BC selects egalitarian-disposed, repels authoritarian-disposed; KJB sorts differently). SAME phenomenon as audience-capture (H14) + monetization (§6), seen at register level.
- **H17c — altitude/generativity asymmetry + mechanism (CONTESTABLE; author's hypothesis).** Theory-construction is itself a dominance display (to legislate a framework is to claim authority to legislate). KJB's tolerance of ironic hierarchy unlocks generative framework-building (SCUM, Pateman-as-doctrine, bromance-budget); BC's flat-cooperative register forbids the dominance-display and caps it at recognition/application of named tropes. Unifies H8 (theory vs catalogue) + H2 (mode-of-analysis hedging) + status economies into one: the hedging IS the flattening IS the altitude-cap. **DISCIPLINE (this is the project's single most seductive just-so-story site — flatters "KJB cleverer," near-unfalsifiable if loose):** (i) CONFOUND — breadth-for-ads monetization and BC's pedagogical newcomer-function each independently predict the cap; can't assign to disposition over format/money (§6). (ii) COUNTERWEIGHT — sophistication is multidimensional: BC is HIGHER on instrument-reflexivity (Sarkeesian interrogates the Bechdel test's validity; KJB never interrogates SCUM, only ironizes it). Same flat disposition caps generativity but enables reflexivity. Honest finding: ORTHOGONAL sophistication axes — KJB generativity / BC reflexivity — disposition predicts which axis each owns. Falsifiers: a BC episode building a transferable framework; a KJB episode interrogating SCUM's validity; the cap proving domain-specific (already partly true). **Hard rule unchanged: register/structure level only; never H15 / medical history.**

---

## 6. The confound table

n = 2 shows. Every candidate explanatory variable is **perfectly aligned**:

| Variable | KJB | BC |
|---|---|---|
| Format | fixed trio, serial lore, no recap obligation | rotating guest, network panel, recap-and-rubric ritual |
| Nationality / comedic tradition | UK (ironic, combative, reference-maximalist, panel-show lineage) | US (sincere, pedagogical, earnest aphorism permitted) |
| Monetisation | listener-funded, no ads → depth/initiate strategy | ad-supported network → breadth/onboarding strategy |
| Gender socialisation | AMAB-socialised trio | AFAB-socialised duo |
| Era (in corpus) | 2023–2026 | mostly 2018–2020 |

Working rank of explanatory power (a structured bet, not a finding): **format/production ≥ nationality > gender-positionality** (powerful but localized — owns H6/H11, contests H2) **> openness** (probably a selection effect into the style, not a direct cause) **> neurodivergence** (least observable, most over-determined; its key construct may be definitionally entangled with "masculine style" — see H15b). Essays must never present a single-variable causal story as established; the honest framing is always "all the causes point the same way, which is why the pattern is so stable and so hard to decompose."

---

## 7. Methods rules

1. **Matched windows** whenever lengths differ: KJB preview (~10 min) vs BC's first ~10 minutes. State window boundaries in the essay.
2. **Date every episode**; flag era skew per pair; the F&F pair (2019 vs 2026) is the extreme case.
3. **ASR caution**: no claims from single ambiguous lines; speaker attribution is unreliable — attribute to "a host" unless the line is self-identifying or contextually certain. Strip/ignore embedded ad reads from register counts (but BC's ad architecture is citable as structural evidence).
4. **Quotation discipline (copyright)**: direct quotes under 15 words, used sparingly, one per source passage; paraphrase by default. The genre needs *specimens*, not reproduction. Never reproduce extended runs of transcript.
5. **No speculation about hosts' private lives, medical histories, or diagnoses.** Public self-description only. This is both an ethics rule and an epistemics rule (see H15).
6. **Falsification habit**: every essay names what would disconfirm its central claims; every correction goes in FINDINGS.md (precedent: the SCUM correction — a confident claim made on incomplete sampling, falsified by new data, owned plainly).
7. **Confound hygiene**: any claim of the form "this difference is because of X" must acknowledge the aligned alternatives in §6.

**Canonical counting pipeline: `/tagging`.** All quantitative figures cited in essays come from `tagging/counts.json`, regenerated by `python3 tagging/count.py` over `/transcripts` using the frozen lexicons in `tagging/lexicons.json`. Raw counts are committed alongside rates so small-n fragility is visible. Every figure must be regenerable; if it isn't, it's a bug. Hand-check a sample before resting a claim on any count (see H3's demotion, essay 03, and correction C3). `tools/register_counts.py` is superseded — do not cite it.

### Quantitative passes (run on the cheap-model tier, per matched window)
- Epistemic hedge tokens per 1k words ("I think / I feel like / I guess / I don't know / kind of / sort of / maybe") — exclude rhetorical-setup uses by hand-check on a sample
- Deflation events coded self- vs other-directed (H4)
- Profanity per 1k words + function coding (connective/structural vs punctuational)
- Unglossed in-group tokens per 1k words (H14 drift test) — build the KJB lexicon list first from late episodes, then count backwards
- First-person singular vs plural rates (H6 proxy)
- Grammatical subject analysis in woman-discussing passages (who acts, who is acted on)
- Disgust-lexicon vs anger-lexicon counts (H3)
- Apology tokens (BC's apology subroutine vs KJB's mock-apology)

---

## 8. Pipeline and book structure

```
/transcripts          # the 26 files (§3 naming)
ANALYTIC_BRIEF.md     # this document — read first, every session
FINDINGS.md           # running scoreboard + corrections log; update after EVERY essay
/essays               # 01–13, one per pair, KJB-chronological order
/synthesis            # intro, 2–3 throughline chapters, methods/caveats chapter
/reference            # external theory corpora (Fight Like an Animal, indexed) — lenses, not subjects
/tagging              # CANONICAL quantitative layer: lexicons.json + count.py + counts.json (regenerable)
/tools                # clean_transcripts.py, scrape/ (re-scrape kit); register_counts.py SUPERSEDED
```

**Essay architecture (revised 2026-06-10, author review).** Organise each essay around its *one best finding*, written as readable prose a person would want to read — not as a hypothesis audit. The strata walk is **not mandatory**: take the strata that yield, say when one is thin (essay 02's "I'm not going to march all six strata in lockstep" is the default). The full H1–H16 scorecard lives in **FINDINGS and the synthesis skeletons**, not onstage in the essay body; an essay may carry a compact scorecard as a clearly-marked appendix, but the prose leads. Avoid audit-speak ("supported ×8") in the essay text. The ledger is backstage machinery; the essays are essays.

**Essay order = KJB-chronological** (The Rock & Casino Royale episode-era → S2 Atomic Blonde/Austin Powers → S3 previews → S4 heist run), so that the H14 drift question surfaces naturally as the essays progress and later essays can cite earlier ones' findings.

**Essay template** (a scaffold, not a cage — see voice note): (1) pair specifics — dates, guests, lengths, live/preview caveats; (2) the strata walk, taken where it yields (say when a stratum is thin rather than marching all six); (3) hypothesis scorecard — which of H1–H16 this pair supports, complicates, or breaks; (4) what's genuinely new in this pair. Target 2,500–4,000 words; density over length. **License (author, 2026-06-10): essays may break out of pure linguistics into sociology, biology, political theory, and the Schröder/Fight Like an Animal lens (H16) where the evidence invites it — propose theory, don't just catalogue.** Discipline unchanged: mark confidence, post confounds (§6), own falsifications, and keep H16/Schröder strictly away from H15 and any host's private history.

**Synthesis chapters** are written last, from FINDINGS.md rather than from raw transcripts. Candidate throughlines: (a) the two rhetorical economies and the irony symmetry (H5); (b) convergent instruments, divergent stances (H8/H9/H10); (c) the confound problem as a chapter in itself — what n=2 can and can't tell you, written honestly; (d) the drift result (H14), whichever way it lands.

**Checkpoint with the author between essays.** His steering has supplied half the framework (the hedging challenge, the audience-ecosystem angle, the IQ-framing correction). Do not one-shot the book.

---

## 9. Voice calibration

The register of the source conversation, which is the register of the book: dense analytical prose, readable, willing to commit to a claim and equally willing to mark its confidence level; corrections owned without ceremony; pushback delivered with respect for the author's intelligence; humour permitted, sincerity underneath. No bullet-sprawl in essays — prose carries the argument; tables only for genuine tabular data (counts, the corpus inventory). Avoid the two failure modes the conversation itself diagnosed: the flattering just-so story (covert-prestige readings that can absorb any data) and the tidy single-cause narrative (everything is gender / everything is format). When the evidence is braided, say it's braided.
