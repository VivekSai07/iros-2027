# Provenance: G2 mid-motion repair novelty re-check

- **Date:** 2026-10-18
- **Rounds:** 1 (4 parallel researcher passes A-D, lead synthesis, 1 verifier pass); the Feynman run hit an Anthropic rate limit (HTTP 429) before its deliver step, so final delivery was done manually.
- **Sources consulted / accepted:** 43 arXiv IDs checked against the arXiv API (all resolve to the named paper, v1 dates match); LeRobot docs/commit 146d847 (2026-10-16) checked by curl + grep.
- **Sources rejected / unavailable:** ChunkFlow and FASTER project pages (404); FASTER PDF over 20 MB (HTML used). No robots/paywall blocks; ELLSA GitHub not re-fetched (D-007).
- **Verification:** PASS WITH NOTES. 10/10 high-stakes claims supported; 5 wording corrections applied on delivery (FutureRTC 3 real tasks; ReSteer 33% baseline is teleop-fine-tuned, zero-shot 7%; SwitchVLA code "not stated"; SwitchVLA canonical-start-pose is a training-target construction; MIRA 466 ms is dispatch of the abort command, not physical stop).
- **Open notes:** Premover v2 appendix not fully read; ReSteer/piR2/FutureRTC/DiscreteRTC code status [S]/[U]; minimal SO-101 experiment is planned, not run.
- **Plan:** outputs/.plans/g2-midmotion-repair-novelty.md
- **Research files:** outputs/.drafts/g2-midmotion-repair-novelty-research-{A,B,C,D}.md, -draft.md, -verification.md
