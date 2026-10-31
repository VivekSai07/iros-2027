# Provenance: G1 novelty re-check — speech-interruption benchmark for manipulation with physical failure taxonomy

- **Date:** 2026-10-18
- **Rounds:** 2 (round 1: alphaXiv/S2/OpenAlex/arXiv sweep + targeted full-text reads; round 2: web pass for RIAP, workshop scoop-watch, GitHub benchmarks)
- **Sources consulted:** ~70 search-result records across 23 paper-index queries and 3 web queries; 41 sources examined at abstract level or deeper (34 arXiv papers listed in Sources + RIAP NeurIPS page + SafeVLA-Bench README + RTCA site; plus screened-out results such as IHBench, DuplexAct-Bench, M3-DuplexBench, VGBench, MEMOBench, Human–VLA Communication Gap).
- **Sources accepted:** 34 arXiv works + 3 web pages (see Sources in outputs/g1-interruption-benchmark-novelty.md). Full text read: ELLSA, VITA-E, MIRA, ARMS, RoboRecover, One Word Different Action, Kennington et al.
- **Sources rejected / not used:** speech-only benchmarks without interruption-during-action relevance (IHBench 2606.19595, DuplexAct-Bench 2609.39446, M3-DuplexBench 2607.29125, When Intent Arrives Late 2610.00272, MultiPartyTurnBench 2610.20172) — screened by title/abstract snippet only; unrelated "barge" keyword hits (tugboat-barge).
- **Blocked:** OpenReview NeurIPS 2026 RTCA group page (JS-rendered); ELLSA GitHub (ROBOTS_DISALLOWED, prior D-007, not re-attempted); RIAP full text (no preprint found); SafeVLA-Bench docs beyond truncated README.
- **Verification:** PASS WITH NOTES — no FATAL issues; open MAJOR items: SocialVLA/Causeway/RIAP read at abstract level only; human-validation cells for FDB/Talking Turns/TurnBench unknown.
- **Plan:** outputs/.plans/g1-interruption-benchmark-novelty.md
- **Research files:** outputs/.drafts/g1-interruption-benchmark-novelty-research-direct.md, outputs/.drafts/g1-interruption-benchmark-novelty-draft.md, outputs/.drafts/g1-interruption-benchmark-novelty-cited.md, outputs/.drafts/g1-interruption-benchmark-novelty-revised.md, outputs/.drafts/g1-interruption-benchmark-novelty-verification.md
