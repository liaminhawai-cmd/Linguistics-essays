#!/usr/bin/env python3
"""Extended in-joke test (FINDINGS Q17): does KJB's private vocabulary get denser over time?

    python3 tagging/ingroup_extended.py            # writes tagging/ingroup_extended.json, prints the table
    python3 tagging/ingroup_extended.py --contexts # also prints every 'scum' hit outside the scoring segment

Runs two instruments over the 23 full KJB episodes in broadcast order:
  original   - the ingroup_kjb list in lexicons.json, unchanged (comparable with essay 08)
  calibrated - the same vocabulary with every spelling variant found in either captioning
               source (the first 8 episodes are podscripts.co ASR, the later 15 are
               YouTube-style captions, and they spell the invented words differently)

Also reports, per episode:
  - where the scoring segment starts, and density inside vs outside it. The start is the first
    time, in the last 40% of the episode, that the hosts introduce the scoring system
    ("science-based system", "called the scum system" and close variants). NOTE: the first
    version of this detector looked for the word "smarm" and failed, because YouTube captions
    mangle it ("smum", "smoo", "sm"). It was repaired after the first run, i.e. after seeing
    the data; the prediction it serves was registered before.
  - whether SCUM is glossed: the hosts say what the letters stand for ("scum system ... stands
    for" within 30 words, or "scum system for smarm", or three of the four axis names within
    80 words)
  - which wording of the third axis is recited: "unprovoked" (original) or "unnecessary"
    (the amendment enacted in the Blues Brothers episode)

Word counts exclude timestamps, '>>' speaker ticks and [bracketed] caption tags.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEX = json.loads((ROOT / "tagging" / "lexicons.json").read_text())

# Broadcast order. Dates for the first 8 are from FINDINGS; the rest are consecutive season-4 episodes.
EPISODES = [
    ("ep22 The Rock", "transcripts/the_rock_KJB.txt", "podscripts"),
    ("ep24 Casino Royale", "transcripts/casino_royale_KJB.txt", "podscripts"),
    ("Die Hard (Dec 2022)", "transcripts/die_hard_KJB.txt", "podscripts"),
    ("S2E22 Atomic Blonde", "transcripts/atomic_blonde_KJB.txt", "podscripts"),
    ("S2E23 Austin Powers (live)", "transcripts/austin_powers_KJB.txt", "podscripts"),
    ("S4E3 Ocean's Eleven", "transcripts/oceans_eleven_KJB.txt", "podscripts"),
    ("S4E22 Point Break", "transcripts/point_break_KJB.txt", "podscripts"),
    ("S4E30 Fast and the Furious", "transcripts/fast_furious_KJB.txt", "podscripts"),
    ("S4E34 Fast Five", "transcripts/kjb_unpaired/s4e34_fast_five_KJB.txt", "youtube"),
    ("S4E36 Furious 7", "transcripts/kjb_unpaired/s4e36_furious_7_KJB.txt", "youtube"),
    ("S4E37 Fate of the Furious", "transcripts/kjb_unpaired/s4e37_fate_of_the_furious_KJB.txt", "youtube"),
    ("S4E38 Hobbs & Shaw", "transcripts/kjb_unpaired/s4e38_fast_and_furious_presents_hobbs_and_shaw_KJB.txt", "youtube"),
    ("S4E39 F9", "transcripts/kjb_unpaired/s4e39_f9_the_fast_saga_KJB.txt", "youtube"),
    ("S4E40 Fast X", "transcripts/kjb_unpaired/s4e40_fast_x_KJB.txt", "youtube"),
    ("S4E41 Blue Collar", "transcripts/kjb_unpaired/s4e41_blue_collar_KJB.txt", "youtube"),
    ("S4E42 Baby Driver", "transcripts/kjb_unpaired/s4e42_baby_driver_KJB.txt", "youtube"),
    ("S4E43 The Blues Brothers", "transcripts/kjb_unpaired/s4e43_the_blues_brothers_KJB.txt", "youtube"),
    ("S4E44 Pelham 123 (1974)", "transcripts/kjb_unpaired/s4e44_the_taking_of_pelham_123_KJB.txt", "youtube"),
    ("S4E46 Entrapment", "transcripts/kjb_unpaired/s4e46_entrapment_KJB.txt", "youtube"),
    ("S4E47 Reservoir Dogs", "transcripts/kjb_unpaired/s4e47_reservoir_dogs_KJB.txt", "youtube"),
    ("S4E48 Point Blank", "transcripts/kjb_unpaired/s4e48_point_blank_KJB.txt", "youtube"),
    ("S4E49 Jackie Brown", "transcripts/kjb_unpaired/s4e49_jackie_brown_KJB.txt", "youtube"),
    ("S4E50 Layer Cake", "transcripts/kjb_unpaired/s4e50_layer_cake_KJB.txt", "youtube"),
]

ORIGINAL = re.compile(
    r"\b(?:" + "|".join(sorted((re.escape(t) for t in LEX["metrics"]["ingroup_kjb"]["tokens"]), key=len, reverse=True)) + r")\b",
    re.I)

# One pattern per piece of apparatus, with the variants seen in either source.
CALIBRATED = {
    "SCUM": r"\bscum\b",
    "Kronsteen": r"\b[ck]ronst\w+|\bcronting\b",
    "Rosette": r"\brosettes?\b",
    "Kaufman": r"\bkaufman\b",
    "Goodnight Cross": r"\bgood ?night cross\b",
    "Waingrow": r"\bwaingro\w*|\bwangro\w*",
    "GIRTH": r"\bgirth\b",
    "science-based": r"\bscience[- ]based\b",
    "homosocial": r"\bhomo ?social\w*",
}
CAL = {k: re.compile(v, re.I) for k, v in CALIBRATED.items()}
AXES = [r"\bsm[au]r?m\w*|\bsmum\b|\bsmoo\b", r"\bcultural(?:ly)? (?:and |in)sensitiv\w+|\bcultural incentitivity", r"\bun(?:provoked|necessary) violence", r"\bmisogyn\w+"]
SCORING_INTRO = re.compile(r"science[- ]based system|scientific system|objective system|call(?:ed)? the scum system|thing based system", re.I)
GLOSS = re.compile(r"scum system\W+(?:\S+\W+){0,30}?stands? for|scum system\W*(?:stands )?for sm", re.I)
TIMESTAMP = re.compile(LEX["timestamp_marker"])


def clean(text):
    text = TIMESTAMP.sub(" ", text)
    text = re.sub(r"\[[^\]]{0,40}\]", " ", text)  # [music], [laughter], bleeps
    return re.sub(r">>", " ", text)


def word_index(text):
    """Word start offsets, so character positions can be turned into word positions."""
    return [m.start() for m in re.finditer(r"\S+", text)]


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def analyse(label, rel, source):
    text = clean((ROOT / rel).read_text(encoding="utf-8", errors="replace"))
    starts = word_index(text)
    n = len(starts)

    def wpos(char):  # word position of a character offset
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if starts[mid] <= char:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

    orig = len(ORIGINAL.findall(text))
    hits = {k: [wpos(m.start()) for m in rx.finditer(text)] for k, rx in CAL.items()}
    all_hits = sorted(p for v in hits.values() for p in v)

    # scoring segment: first introduction of the scoring system in the last 40% of the episode
    intro = [wpos(m.start()) for m in SCORING_INTRO.finditer(text)]
    late = [p for p in intro if p >= 0.60 * n]
    seg = late[0] if late else None
    inside = [p for p in all_hits if seg is not None and p >= seg]
    outside = [p for p in all_hits if seg is None or p < seg]
    out_words = seg if seg is not None else n
    in_words = n - seg if seg is not None else 0

    # gloss: the letters are spelled out
    axis_pos = [[wpos(m.start()) for m in re.finditer(a, text, re.I)] for a in AXES]
    glossed = bool(GLOSS.search(text))
    if not glossed:
        for p in sorted(q for a in axis_pos for q in a):
            if sum(any(p <= q < p + 80 for q in a) for a in axis_pos) >= 3:
                glossed = True
                break
    third_axis = dict(unprovoked=len(re.findall(r"\bunprovoked violence", text, re.I)),
                      unnecessary=len(re.findall(r"\bunnecessary violence", text, re.I)))

    return dict(
        episode=label, file=rel, source=source, words=n,
        original_raw=orig, original_per_1k=round(1000 * orig / n, 2),
        calibrated_raw=len(all_hits), calibrated_per_1k=round(1000 * len(all_hits) / n, 2),
        by_term={k: len(v) for k, v in hits.items() if v},
        distinct_terms=sum(1 for v in hits.values() if v),
        scoring_starts_at_pct=round(100 * seg / n) if seg is not None else None,
        inside_raw=len(inside), inside_per_1k=round(1000 * len(inside) / in_words, 2) if in_words else None,
        outside_raw=len(outside), outside_per_1k=round(1000 * len(outside) / out_words, 2) if out_words else None,
        scum_glossed=glossed, third_axis=third_axis,
        axis_mentions=[len(a) for a in axis_pos],
    )


def main():
    rows = [analyse(*e) for e in EPISODES]
    order = list(range(1, len(rows) + 1))
    old, new = rows[:8], rows[8:]
    mean = lambda rs, k: round(sum(r[k] for r in rs) / len(rs), 2)
    summary = dict(
        n=len(rows),
        spearman_order_vs_original=round(spearman(order, [r["original_per_1k"] for r in rows]), 3),
        spearman_order_vs_calibrated=round(spearman(order, [r["calibrated_per_1k"] for r in rows]), 3),
        spearman_order_vs_outside_scoring=round(spearman(order, [r["outside_per_1k"] for r in rows]), 3),
        spearman_new15_only_calibrated=round(spearman(order[8:], [r["calibrated_per_1k"] for r in new]), 3),
        mean_original_first8=mean(old, "original_per_1k"), mean_original_new15=mean(new, "original_per_1k"),
        mean_calibrated_first8=mean(old, "calibrated_per_1k"), mean_calibrated_new15=mean(new, "calibrated_per_1k"),
        mean_outside_first8=mean(old, "outside_per_1k"), mean_outside_new15=mean(new, "outside_per_1k"),
        range_calibrated_first8=[min(r["calibrated_per_1k"] for r in old), max(r["calibrated_per_1k"] for r in old)],
        range_calibrated_new15=[min(r["calibrated_per_1k"] for r in new), max(r["calibrated_per_1k"] for r in new)],
        glossed_first8=sum(r["scum_glossed"] for r in old), glossed_new15=sum(r["scum_glossed"] for r in new),
        share_of_tokens_inside_scoring=round(sum(r["inside_raw"] for r in rows) / max(sum(r["calibrated_raw"] for r in rows), 1), 2),
        episodes_with_scoring_segment_found=sum(r["scoring_starts_at_pct"] is not None for r in rows),
        mean_distinct_terms_first8=mean(old, "distinct_terms"), mean_distinct_terms_new15=mean(new, "distinct_terms"),
        threshold_for_n23=0.41,
    )
    (ROOT / "tagging" / "ingroup_extended.json").write_text(json.dumps(dict(summary=summary, episodes=rows), indent=1) + "\n")

    print(f"{'episode':30}{'src':5}{'words':>7}{'orig/1k':>8}{'cal/1k':>7}{'raw':>4}{'terms':>6}{'score@':>7}{'in/1k':>7}{'out/1k':>7} gloss 3rd-axis")
    for r in rows:
        print(f"{r['episode']:30}{r['source'][:4]:5}{r['words']:>7}{r['original_per_1k']:>8}{r['calibrated_per_1k']:>7}{r['calibrated_raw']:>4}"
              f"{r['distinct_terms']:>6}{str(r['scoring_starts_at_pct'])+'%':>7}{str(r['inside_per_1k']):>7}{str(r['outside_per_1k']):>7} {'yes' if r['scum_glossed'] else 'no':4} {'unprov' if r['third_axis']['unprovoked'] else ''}{'/' if r['third_axis']['unprovoked'] and r['third_axis']['unnecessary'] else ''}{'UNNEC' if r['third_axis']['unnecessary'] else ''}")
    print()
    for k, v in summary.items():
        print(f"{k}: {v}")

    if "--contexts" in sys.argv:
        print("\n'scum' outside the scoring segment (is it the apparatus or the ordinary word?):")
        for label, rel, _ in EPISODES:
            text = clean((ROOT / rel).read_text(encoding="utf-8", errors="replace"))
            words = text.split()
            n = len(words)
            starts = word_index(text)
            late = [m.start() for m in SCORING_INTRO.finditer(text)]
            late = [sum(1 for s in starts if s <= c) for c in late]
            late = [i for i in late if i >= 0.60 * n]
            seg = late[0] if late else n
            for i, w in enumerate(words[:seg]):
                if re.fullmatch(r"\W*scum\W*", w, re.I):
                    print(f"  {label:28} {' '.join(words[max(0, i - 7):i + 6])}")


if __name__ == "__main__":
    main()
