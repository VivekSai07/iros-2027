# Verification pass (lead self-review, direct mode) — g1-interruption-benchmark-novelty

Date: 2026-10-18. Reviewed: `outputs/.drafts/g1-interruption-benchmark-novelty-cited.md` → fixes written to `...-revised.md`.

## Checks performed
1. Every arXiv ID in the matrix resolved by a tool: 22 via arXiv export API (id_list, all found), the rest via alphaXiv index / Semantic Scholar / OpenAlex (source noted per entry in Sources). No ID left unresolved; RIAP has no arXiv ID and is cited to its NeurIPS page.
2. Every numeric claim traced to the research notes (`...-research-direct.md`), which quote abstract/full text: ELLSA 94.3% / 10 phrases / 2–8 s; VITA-E 100/93.3/100% over 30 trials, 2.26 s; MIRA 466 ms, 450 ms gate, 0.50 s prefix; SocialVLA 15 participants, 100→57 false stops, 336 ms, 1.021 s; RIAP 8,160 replays, 27.5%→1.6%, 1,022 ms, 60.6%, N=30; Causeway 71 pairs, 3 timings, 3–26%→47–65%; LIBERO-MAX 8,000 pairs, 11.0–25.7 pp; ARMS 45% vs 28%, 85% oracle; RoboRecover 2,000 scenarios; JitterVLA 615→106 m/s^3; RASSG 50.00%→3.15%; Duplex Cue 68.2% vs 34.8%.
3. Date claim "eleven papers between 2026-09-21 and 2026-10-14" checked against publishedAt / arXiv published fields recorded in notes.
4. Cross-checked status flags: abstract-only rows marked [V abstract]; inferences labelled "Inference".
5. URL reachability: arXiv abs URLs returned by arXiv API; neurips.cc, github.com/Jatshi, rtcaneurips26.github.io fetched successfully; OpenReview failed (listed as Blocked).

## Findings
### FATAL
- None remaining.

### MAJOR (fixed in revised)
- M1: SocialVLA characterised as "stops instead of repairing" / "evaluates holding, not repair". Abstract states a speech channel captures verbal corrections "for participant-directed continuation, restart, or instruction revision". Softened in exec summary, matrix row and reading note.
- M2: RIAP row omitted "corrected for 60.6% of mid-utterance human revisions", which is relevant to repair. Added.

### MAJOR (not fixable in this pass → Open Questions)
- M3: Verdict depends on abstract-level reading of SocialVLA, Causeway, RIAP. Full text not read for these (RIAP unavailable). Listed in §7 Open questions and §8 Next steps.
- M4: Human-validation cells for FDB/Talking Turns/TurnBench are "?" — does not affect verdict (no manipulation) but matrix is incomplete there.

### MINOR (fixed)
- m1: ELLSA 5.7% described as "failed-to-stop"; causes not broken down in paper → reworded.
- m2: MIRA "does not measure post-command motion" → "not in sections read".
- m3: JitterVLA human column changed to ✗ (human trajectories are inputs, not ratings).
- m4: "ten papers in six weeks" corrected to "eleven between 2026-09-21 and 2026-10-14".

### MINOR (accepted)
- Talking Turns/TurnBench content cells rely on prior notes [S].
- MIRA/ARMS dates from alphaXiv publishedAt (arXiv v2 stamps 22 Sep / 9 Oct).

## Side finding (affects repo files)
- `04-literature-map.md` RIAP row says "0% unsafe commits vs 27.5%"; primary abstract says 27.5% → 1.6% over 8,160 simulation replays. Needs correction.

Verification: PASS WITH NOTES (M3, M4 open; blocked sources listed).
