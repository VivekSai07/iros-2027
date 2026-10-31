# Gap analysis (after 5 iterations)

## Invalidated gaps — do NOT claim as novelty
- **G3 "timing/commit as a decision variable" for speech-driven manipulation** → covered by RIAP (act/wait/defer, N=30 study) and Premover (readiness gate on real SO-101).
- **"First user study with interruption"** → partially covered by SocialVLA (n=15), CMU HRI 2026 (n=18), MICoBot (18 participants), ExpressMM (n=23), Skantze & Irfan (n=39, speech-only).
- **"Speech barge-in stops a robot"** → ELLSA (sim), VITA-E (real humanoid).
- **"Acting on partial speech"** → Premover, Tufts/TUW.

## Surviving gaps (to verify further; scoop risk medium-high and rising)
- **G1 — Benchmark.** No time-anchored, speech-overlap interruption benchmark for *manipulation* with a *physical* failure taxonomy. Physical analogs of EchoChain's inertia/amnesia/displacement plus residual motion, retraction penalty, spurious halt. Metrics: repair latency, trajectory continuity, post-repair success, false-barge-in rate. "EchoChain for robots."
- **G2 — Method.** Learned mid-motion repair without stop-and-retract. Existing systems cancel (ELLSA), retract (VITA-E), or wait for atomic step boundary (Hi Robot). Candidate: chunk truncation + RTC-style inpainting on SmolVLA/ACT, driven by a cascaded streaming pipeline (streaming ASR + turn/backchannel model such as Easy Turn/VAP + small LLM for state-update parsing).
- **G4 — Validity.** No evidence that benchmark scores predict human-rated fluency (Hoffman metrics, PMQ) with naive participants on a low-cost arm. Target n≈18–39.

## Gap vs team interest
| Gap | Fit with team | Feasibility on 48 GB / 8 GB | Risk |
|---|---|---|---|
| G1 | Sim strength (Isaac/MuJoCo) + SO-101 | High (sim-first, ASR/TTS light) | Others publish benchmarks quickly |
| G2 | Imitation-learning experience | High (SmolVLA/ACT + RTC) | Gains may be small vs stop-and-replan |
| G4 | Needs participants/ethics route | Medium | Ethics approval timeline |

## H2 and A+B (summary)
- H2: consequence-prediction angle unchecked; high human-study and labeling burden.
- A+B: least collided; hardware go/no-go needed (repeatability test).

## Honest scoop-risk assessment
Many Oct 2026 arXiv papers in this exact area. If a benchmark with similar framing appears before submission, pivot to ICRA 2028 with the user-study-heavy version.

## Update 2026-10-18 — G1 re-check (see `outputs/g1-interruption-benchmark-novelty.md`)
- **G1 status: open but narrowed.** No work combines spoken interruptions + time-anchoring to motion phase + manipulation + physical repair taxonomy + human validation. Each component alone is now precedented.
- Do NOT claim: first timing-controlled switch evaluation in manipulation (Causeway 3 switch timings; LIBERO-MAX paired mid-task events; MAIL-Bench multi-stage); first manipulation interruption metrics (ARMS cross-interruption recall / foreground continuation, text); first false-stop + latency with users (SocialVLA, n=15+1); first SO-101 failure taxonomy (Yu & Qiu 2606.08881).
- Remaining differentiators: residual-motion & retraction metrics conditioned on onset; backchannel/self-correction spurious halts during manipulation; EchoChain categories as physical failure modes; phase-anchored spoken corrections; metric-validity study (G4).
- Scoop risk: **high** (Skoltech group has SocialVLA + JitterVLA; NeurIPS 2026 RTCA workshop accepted papers unchecked).
