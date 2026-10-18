# Plan: G1 novelty re-check — speech-interruption benchmark for manipulation

Slug: `g1-interruption-benchmark-novelty` · Date: 2026-10-18 · Owner: lead (Feynman)

## Key questions
1. Does any benchmark (sim or real) exist that evaluates **spoken interruptions overlapping robot manipulation**, anchored in time (interruption onset relative to motion phase)?
2. Does any such benchmark define a **physical failure taxonomy** (residual motion, retraction penalty, spurious halt, wrong-object commit, physical analogs of EchoChain's contextual inertia / interruption amnesia / objective displacement)?
3. Does any report metrics such as repair latency, trajectory continuity, post-repair success, false-barge-in rate?
4. Does any validate benchmark scores against human ratings?
5. Which work published 2026-06 → 2026-10-18 is the nearest competitor (scoop risk)?

## Evidence needed
- Primary abstract/full-text checks for: EchoChain, One Word Different Action (2609.05260), MAIL-Bench, RoboRecover (2609.28952), NIABench (2605.01368), ELLSA (LIBERO barge-in eval), SwitchVLA, VITA-E, RIAP, Premover (2605.12160), SocialVLA (2610.02360), Full-Duplex-Bench v1/v1.5/v2, Talking Turns (2503.01174), TurnBench (2608.25218), YAY Robot, RACER, RT-H, LIBERO-PRO, LIBERO-Plus.
- New-paper sweep: arXiv 2026-06 → now, queries on interruption / barge-in / mid-execution correction / instruction change / full-duplex VLA / embodied interruption benchmark.

## Scale decision
Narrow-but-multi-item novelty check with a fixed candidate list plus a recency sweep. Conclusions depend on precise primary-source verification of ~20 items; delegation would add verification overhead and context loss. **Decision: direct search by lead, no researcher subagents.** Citation and review done by lead (direct-mode rules). Expected 30–50 tool calls.

## Task ledger
| ID | Task | Owner | Status |
|---|---|---|---|
| T1 | Verify listed robot-side candidates (ELLSA, VITA-E, SwitchVLA, One Word, RoboRecover, MAIL-Bench, NIABench, RIAP, Premover, SocialVLA) | lead | done |
| T2 | Verify speech-side benchmarks (EchoChain, FDB v1/v1.5/v2, Talking Turns, TurnBench) | lead | done |
| T3 | Verify language-correction / perturbation suites (YAY Robot, RACER, RT-H, LIBERO-PRO, LIBERO-Plus) | lead | done |
| T4 | Recency sweep arXiv 2026-06 → 2026-10-18 (≥6 distinct queries) | lead | done |
| T5 | Coverage matrix + verdict + nearest competitor (draft) | lead | done |
| T6 | Citation pass + self-verification | lead | done (PASS WITH NOTES) |
| T7 | Deliver final + provenance | lead | done |

## Verification log
- 2026-10-18: 23 alpha/S2/OpenAlex/arXiv queries + 3 web queries run; terms in outputs/.drafts/g1-interruption-benchmark-novelty-research-direct.md.
- arXiv API id_list resolved 22 IDs (all found). MAIL-Bench resolved to 2609.35003.
- Full-text reads: MIRA, ARMS (Watch-Recall-Act), Kennington 2610.08733, One Word, RoboRecover, ELLSA, VITA-E.
- RIAP: NeurIPS abstract fetched; literature-map value "0% unsafe" found WRONG (abstract: 1.6%).
- Blocked: OpenReview RTCA (JS-rendered), ELLSA GitHub (robots, prior D-007).
- Self-review: 0 FATAL, 2 MAJOR fixed (SocialVLA recovery wording; RIAP 60.6% revisions), 2 MAJOR open (abstract-only reads; FDB human-validation cells), 4 MINOR fixed. See outputs/.drafts/g1-interruption-benchmark-novelty-verification.md.
- Project files updated: 04 (RIAP correction + new rows), 05 (G1 update), 07 (iteration 6), 08 (items 10\u201311).
- Environment note: `python3`/`python` not available in this Windows shell; edits done with Edit tool.

## Decision log
- 2026-10-18: direct mode chosen (see scale decision).
- Rule: any arXiv ID not resolved by a tool → [U]; inaccessible sources → Blocked sources section, not worked around.
