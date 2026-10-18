# Plan — Source comparison: how systems handle an instruction arriving while the arm moves

Slug: `midmotion-instruction-handling-strategies` · Date: 2026-10-18 · Final artifact: `outputs/midmotion-instruction-handling-strategies-comparison.md`

## Question
When a spoken or text instruction arrives while a robot arm is already moving, what does each existing system do physically, how does it continue/repair, how fast, on what backbone/hardware, and is it reusable for SmolVLA/ACT on SO-101 (8 GB / 48 GB GPUs)?

## Sources (12 systems, grouped by strategy)
| Strategy | System | ID |
|---|---|---|
| Stop | ELLSA | arXiv 2510.16756 |
| Retract-to-home then switch | VITA-E | arXiv 2510.21817 |
| Wait for atomic step boundary | Hi Robot | arXiv 2502.19417 |
| Switch with timing awareness | SwitchVLA | arXiv 2506.03574 |
| Switch with timing awareness | Causeway | arXiv 2609.30913 |
| Act early on streaming speech | Premover | arXiv 2605.12160 |
| Act early on streaming speech | RIAP | NeurIPS 2026 poster 162424 (no arXiv found) |
| Act early on streaming speech | EarlyCommit | arXiv 2610.20531 |
| Reaction-triggered hold | SocialVLA | arXiv 2610.02360 |
| Arbiter preemption | MIRA | arXiv 2609.24547 |
| Chunk-level async execution | RTC | arXiv 2506.07339 |
| Chunk-level async execution | LeRobot async inference | github.com/huggingface/lerobot + SmolVLA 2506.01844 |

## Dimensions
1. Trigger modality (text / TTS speech / live speech / paralinguistic / observation)
2. Physical behaviour at the moment of interruption
3. Repair / continuation mechanism
4. Latency numbers (as stated)
5. Policy backbone and size
6. Real vs sim (robot)
7. Human study (N)
8. Code / weights released
9. GPU fit: 8 GB vs 48 GB (stated, or inferred from params — inferred marked [U])
10. Applicability to SmolVLA / ACT on SO-101 (inference, marked as such)
Plus required evidence matrix columns: source, key claim, evidence type, caveats, confidence.

## Reuse
Existing verified notes: `outputs/g1-interruption-benchmark-novelty.md`, `outputs/.drafts/g1-...-research-direct.md`, `notes/g2-midmotion-repair-novelty-lead-notes.md`, `outputs/.drafts/g2-...-research-A.md`. Researchers fill missing cells only (backbone size, code/weights, GPU, latency, Hi Robot, SwitchVLA, Causeway, Premover, EarlyCommit, SocialVLA, RTC, LeRobot async).

## Execution
- 3 parallel `researcher` subagents (R1: ELLSA, VITA-E, Hi Robot, SwitchVLA; R2: Causeway, Premover, RIAP, EarlyCommit, SocialVLA, MIRA; R3: RTC + LeRobot async code + SmolVLA/ACT memory footprint). Drafts in `outputs/.drafts/midmotion-instruction-handling-strategies-R{1,2,3}.md`.
- Lead synthesizes draft; `verifier` checks flags/URLs and adds inline citations.
- Output structure: summary → Mermaid taxonomy → dimension matrix (11 cols) → evidence matrix (source/key claim/evidence type/caveats/confidence) → latency table → agreement / disagreement / uncertainty → SO-101 implications → open questions → Blocked sources → Sources.

## Rules
[V]/[S]/[U] on every claim. Blocked sources listed, not worked around (ELLSA GitHub is ROBOTS_DISALLOWED per D-007; RIAP full text unavailable). Write only under outputs/.

## Task ledger
| # | Task | Status |
|---|---|---|
| T1 | Read 00-README + g1 output + prior drafts | done |
| T2 | Plan written | done |
| T3 | Researchers R1–R3 | pending |
| T4 | Draft | pending |
| T5 | Verifier pass | pending |
| T6 | Final artifact + check on disk | pending |

## Verification log
- 2026-10-18: R1/R2/R3 drafts on disk (outputs/.drafts/midmotion-instruction-handling-strategies-R{1,2,3}.md).
- 2026-10-18 lead spot-checks: Hi Robot 2502.19417 §4.2 confirms "high-level inference is triggered immediately" on intervention (contradicts "wait for atomic step" framing, which comes from VITA-E/SwitchVLA related-work); SwitchVLA Tables 1/3/11 numbers match R1; LeRobot main remote_inference/README.md confirms task versioning, "planned wait" on in-flight retarget, ACT "temporal ensembling disabled", SmolVLA guided RTC.
- T3 done. T4 drafting.
- 2026-10-18 (resumed after HTTP 429): T4 draft on disk. T5 verification by lead: 13/13 arXiv IDs and 12/12 URLs resolve; 11 cells spot-checked; 0 FATAL / 3 MAJOR / 9 MINOR, all fixed → `-verification.md`, `-revised.md`. T6: final written to `outputs/midmotion-instruction-handling-strategies.md` (COMPLETE) + `.provenance.md`. Ledger T3–T6: done.
