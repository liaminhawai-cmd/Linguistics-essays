#!/usr/bin/env python3
"""Auditable register counts for the KJB-vs-BC corpus.

Single source of truth for every quantitative figure cited in /essays.
Reads lexicons from tagging/lexicons.json, runs them over /transcripts,
and writes tagging/counts.json with RAW counts (not just rates) so
small-n fragility is visible. Every essay figure must be regenerable by:

    python3 tagging/count.py            # all transcripts -> tagging/counts.json
    python3 tagging/count.py the_rock   # filter by substring, print to stdout

Method (ANALYTIC_BRIEF.md §7): strip ASR timestamp markers and dynamically
-inserted BC ads, lowercase, whole-word regex alternation per lexicon.
Counts are crude — directional evidence, hand-check before resting a claim.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEX = json.loads((ROOT / "tagging" / "lexicons.json").read_text())
TRANSCRIPTS = ROOT / "transcripts"
OUT = ROOT / "tagging" / "counts.json"

TIMESTAMP = re.compile(LEX["timestamp_marker"])
AD_MARKERS = LEX["ad_strip"]["markers"]


def strip_ads(text: str) -> tuple[str, int]:
    """Remove sentences containing any ad-campaign marker. Returns (clean, n_words_removed)."""
    before = len(text.split())
    # split into sentence-ish chunks and drop any chunk carrying a marker
    chunks = re.split(r"(?<=[.!?])\s+", text)
    kept = [c for c in chunks if not any(m.lower() in c.lower() for m in AD_MARKERS)]
    clean = " ".join(kept)
    return clean, before - len(clean.split())


def compile_metric(tokens: list[str]) -> re.Pattern:
    # longest-first so multiword tokens match before their substrings
    parts = sorted((re.escape(t) for t in tokens), key=len, reverse=True)
    return re.compile(r"\b(?:" + "|".join(parts) + r")\b", re.IGNORECASE)


METRICS = {name: compile_metric(spec["tokens"]) for name, spec in LEX["metrics"].items()}


def analyze(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    detimed = TIMESTAMP.sub(" ", raw)
    is_bc = "_BC" in path.name
    clean, ad_words = (strip_ads(detimed) if is_bc else (detimed, 0))
    words = len(clean.split())
    metrics = {}
    for name, rx in METRICS.items():
        hits = rx.findall(clean)
        n = len(hits)
        metrics[name] = {
            "raw": n,
            "per_1k": round(1000 * n / words, 2) if words else 0.0,
        }
    return {
        "file": path.name,
        "words_after_strip": words,
        "ad_words_stripped": ad_words,
        "metrics": metrics,
    }


def main() -> None:
    filt = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(TRANSCRIPTS.glob("*.txt"))
    if filt:
        files = [f for f in files if filt in f.name]
    results = {f.name: analyze(f) for f in files}
    if filt:
        for name, r in results.items():
            print(f"\n=== {name} — {r['words_after_strip']:,} words (ads stripped: {r['ad_words_stripped']}) ===")
            for m, v in r["metrics"].items():
                print(f"  {m:24} raw={v['raw']:>4}  {v['per_1k']:>6}/1k")
    else:
        OUT.write_text(json.dumps(results, indent=2) + "\n")
        print(f"Wrote {OUT.relative_to(ROOT)} ({len(results)} transcripts)")


if __name__ == "__main__":
    main()
