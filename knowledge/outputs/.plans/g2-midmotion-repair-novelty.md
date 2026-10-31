# Plan — G2 novelty re-check (mid-motion repair without stop-and-retract)

Slug: `g2-midmotion-repair-novelty` · Date: 2026-10-18 · Not a lab/author corpus review (topic review).

## Key questions
1. Does any published method repair/update an in-flight action chunk (VLA/ACT/flow/diffusion) in response to a NEW language/speech instruction while the arm moves?
2. For RTC (2506.07339) and 2026 descendants (FutureRTC, DiscreteRTC, Barrier-Constrained Guidance, pi-R2, Reactive Real-Time Flow Policies, RAVEL, ChunkFlow, FASTER, Reflex, Action-Prior Denoising): what is repaired, trigger, real/sim, code, speech-overlap coverage.
3. Instruction/task switching VLAs (SwitchVLA, VITA-E, Hi Robot, One Word Different Action): same table.
4. LeRobot async inference (policy_server/robot_client): what it does on instruction change.
5. Which run on SmolVLA / ACT.
6. Scoop sweep 2026-06 → 2026-10.

## Sources
alpha_search (semantic+keyword), alpha_get_paper/ask_paper for primary abstracts, feynman_science_database_search (arxiv ID lookup), alpha_read_code for LeRobot repo.

## Task ledger
| # | Task | Status |
|---|---|---|
| T1 | Read project context files | done |
| T2 | RTC + descendants lookup | lead did RTC, piR2, FutureRTC, DiscreteRTC (notes/g2-midmotion-repair-novelty-lead-notes.md); rest -> researcher A |
| T3 | Instruction-switching VLAs | researcher B |
| T4 | LeRobot async stack code check | researcher D |
| T5 | Open scoop sweep 2026-06+ | lead ran 10 alpha_search queries; researcher C extends |
| T6 | Draft synthesis | pending |
| T7 | Verifier pass (citations/URLs) | pending |
| T8 | Reviewer pass | pending |
| T9 | Final + provenance | pending |

## Verification log
(appended as checks run)
- 2026-10-18: alpha_search confirmed IDs for all named descendants: FutureRTC 2607.24008, DiscreteRTC 2604.25050, Barrier 2610.14997, piR2 2607.26055, Reactive RT Flow 2609.36540, RAVEL 2609.34170, ChunkFlow 2607.12992, FASTER 2603.19199, Reflex 2607.14695, Action-Prior Denoising 2605.25537, SwitchVLA 2506.03574, VITA-E 2510.21817, Hi Robot 2502.19417, One Word 2609.05260.
- New candidate threats surfaced by lead search: Causeway 2609.30913, CIRRA 2610.08862, Watch-Recall-Act 2609.28429, MIRA 2609.24547, ELLSA 2 2610.21452, TempoBridge 2610.09451, ActionSplice 2609.08230.
- Workflow f0053dee launched (researchers A-D).
