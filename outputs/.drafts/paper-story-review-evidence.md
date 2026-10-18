# Evidence notes — paper-story review

Inspected: `06-paper-story.md`, `05-gap-analysis.md`, `10-research-map-and-implementation.md`, `outputs/g1-interruption-benchmark-novelty.md`, `outputs/g2-midmotion-repair-novelty.md`; grep only: `outputs/g4-fluency-metrics-validity.md`, `02-iros-2027-constraints.md`.
Primary check (2026-10-18): arXiv export API `id_list=2610.02360,2609.30913` (SocialVLA and Causeway abstracts).

Flag convention: [V] = verified from a primary source, either by me in this pass (marked "this pass") or by the evidence report (inherited); [S] = secondary; [U] = unverified.

## Claims in the artifact (quoted)
- N2: "Current systems stop (ELLSA), retract (VITA-E), wait for step boundaries (Hi Robot), or only act early on partial speech (Premover, RIAP). None measure or optimise what happens *physically* when speech overlaps motion."
- N3/C3: "evidence that the benchmark predicts human-rated fluency"; "Human study (n≈18–39, within-subject) showing correlation of benchmark metrics with Hoffman fluency metrics and PMQ/SUS."
- C1: "Interruption-in-manipulation benchmark (sim + real SO-101), failure taxonomy, metrics (...)".
- C2: "Mid-motion repair via chunk truncation + inpainting-style continuation (RTC) on SmolVLA/ACT ... runs on commodity GPUs."
- Baselines: "stop-and-replan (LeRobot async), step-boundary wait (Hi Robot-style), retract-and-restart (VITA-E-style), ELLSA only if code is released".
- Speech: "voice-cloned TTS users in sim (EchoChain protocol)".
- Risk: "Scoop (medium-high)".
- "Best-paper potential depends on ..."

## Contradicting / qualifying evidence
1. SocialVLA 2610.02360 [V this pass, abstract]: physical Unitree G1, 15 participants. "VLA-gate-to-physical-hold latency is 336 ms, and reaction-onset-to-hold latency is 1.021 s"; "Relevance estimation reduces false-stop episodes from 100 to 57"; "a separate speech channel captures verbal corrections for participant-directed continuation, restart, or instruction revision." → contradicts N2 "None measure ... physically".
2. MIRA 2609.24547: speech-onset → abort-command 466 ms P50 (gestures, not manipulation) [V inherited, G1/G2].
3. Causeway 2609.30913 [V this pass, abstract]: "71 cross-object pairs, three switch timings, and three VLA architectures"; "bare-switch success from 3-26% to 47-65%"; real xArm. Text instructions, no retract → the story's prior-work taxonomy is incomplete.
4. SwitchVLA 2506.03574, ReSteer 2603.17300: learned text-instruction switching without retract [V inherited; ReSteer via alphaXiv report]. G2 §1: "The broad G2 claim ... is no longer open."
5. G2 §5 surviving wedge: speech-overlap trigger + prefix-aware in-flight retargeting + SmolVLA/SO-101 + continuity evaluation, all four required [inference].
6. G2 §3c [V inherited, code]: ACT "No language input; no RTC". Legacy `async_inference` was retired on main and replaced by `set_task()`, which is stop-based ("Expect a stop during this transition").
7. G2 §5 risks: πR² reports RTC prefix bias toward continuing recent motion [V inherited]. Causeway reports "task islands": instruction influence drops near contact [V inherited].
8. G2 §6 baselines B1–B8, including B2 bare switch, B3 truncate+fresh chunk without RTC, and B6 ReSteer-style fine-tune.
9. G4: Hoffman (2019) |r| ≤ 0.123 between objective metrics and the subjective composite. H-IDLE correlates *positively* [V inherited]. A per-participant correlation needs n≈543; a trial-level design reaches power 0.98 at N=24 × 8 trials with within-r=0.3 (simulation, `experiments/g4-fluency-metrics-validity/power_results.txt`; not re-run by me). PMQ was validated for non-embodied speech interfaces [V inherited]. Song 2607.00530: n=24, spoken commands on a low-cost arm [V inherited].
10. G1 §4 "do not claim" list: first timing in manipulation; first interruption benchmark in manipulation; first false-stop + latency with users; first SO-101 failure taxonomy (Yu & Qiu 2606.08881); first speech barge-in.
11. G1/05: scoop risk **high**, from 11 adjacent papers dated 2026-09-21 to 2026-10-14. The story still says "medium-high".
12. 10 §4: "Planned repo layout (proposal; nothing built yet)". No sim scenes, metrics, or results exist.
13. 02: deadline 1 Mar 2027 [V inherited]. 10 §5 Gantt: ethics + human study must fit 2026-11-01 → 2027-02-12.
14. The EchoChain "voice-cloned TTS" protocol is not described in G1, which records only an injection "at a standardized point relative to assistant speech onset". → [U].
15. Commodity GPU claim: SmolVLA ~99 ms on RTX 4090 [V inherited, G2]. The latency of the full ASR+turn+LLM cascade is not measured anywhere → [U].

## Reported metrics/results in artifact
None. The artifact states no numbers except the participant range. C3 is phrased as a finding ("showing correlation") that does not exist yet.
