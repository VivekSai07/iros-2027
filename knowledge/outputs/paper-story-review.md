# Review: `06-paper-story.md` ("Say It Mid-Motion"), skeptical IROS reviewer view

Reviewed 2026-10-18. Evidence: `05-gap-analysis.md`, `10-research-map-and-implementation.md`, `outputs/g1-interruption-benchmark-novelty.md` (G1), `outputs/g2-midmotion-repair-novelty.md` (G2, partial delivery), and grep checks of G4 and `02-iros-2027-constraints.md`. Notes are in `outputs/.drafts/paper-story-review-evidence.md`.

Flags: [V] = verified from a primary source. "this pass" means I checked it myself; otherwise the flag is inherited from the evidence reports and I did not re-check it. [S] = secondary. [U] = unverified.

## Summary Assessment
The story describes a plausible, well-motivated three-part paper: a benchmark, a method, and a validity study. **But it is out of date with respect to the project's own evidence.** G1, G2 and G4 were completed after the story was written and narrowed every contribution. The story absorbed none of those changes:
- Its prior-work claim is now false.
- C2 states a broad novelty that G2 marks as closed.
- C3 promises a result that G4 shows is underpowered as designed and rests on weak-validity metrics.
- The baselines are all "stop-type" strawmen.

It needs a rewrite before the team decision (due around 24 Oct).

## Strengths
- The problem is real, and the SO-101 + LeRobot stack makes the work reproducible on low-cost hardware.
- The three-way structure is coherent, and the Risks section uses each part as a hedge for the others.
- The interruption types include **backchannel (should NOT interrupt)** and **self-correction**. G1 §3 finds that spurious halts on backchannels during manipulation are measured nowhere. This is one of the few remaining differentiators [inference from G1].

## Critical Issues
1. **The central motivating claim is contradicted by the project's own evidence.** Narrative §2 says: "None measure or optimise what happens *physically* when speech overlaps motion."
   - SocialVLA (2610.02360) runs real Unitree G1 manipulation with 15 participants. It reports "VLA-gate-to-physical-hold latency is 336 ms, and reaction-onset-to-hold latency is 1.021 s" and false-stop episodes falling 100→57 [V, abstract checked this pass].
   - MIRA reports speech-onset→abort latency of 466 ms [V].
   - G1 names SocialVLA the **nearest competitor**, yet the story never mentions it.
   - The prior-work list (ELLSA, VITA-E, Hi Robot, Premover, RIAP) also omits non-retract switching: SwitchVLA, ReSteer, and Causeway. Causeway uses "three switch timings" across 71 pairs and three VLAs [V, abstract checked this pass].
   - **Fix:** restate the claim as G1 §4 does. The novelty is the *conjunction*: spoken × phase-anchored × manipulation × physical repair taxonomy × validated metrics.
2. **C2 claims a novelty that G2 marks as closed.** "Mid-motion repair via chunk truncation + inpainting (RTC)" reads as the broad claim. G2 §1 says "The broad G2 claim … is no longer open", because SwitchVLA, ReSteer and Causeway repair text switches without retracting [V]. The surviving wedge requires all four of these together (G2 §5) [inference]:
   - a speech-overlap trigger;
   - a latency-bounded committed prefix;
   - SmolVLA on SO-101;
   - continuity metrics.

   C2 must name that wedge. It must also state the core technical risk: RTC's prefix biases toward the *old* intent (πR²), and steerability fades near contact (the "task islands" effect from Causeway) [V]. The story presents the method as if neither risk exists.
3. **C3 is worded as a finding, and the planned design cannot deliver it.** "showing correlation of benchmark metrics with Hoffman fluency metrics" has three problems:
   - (a) There are no data yet.
   - (b) Hoffman's objective metrics correlate only weakly with perceived fluency (|r| ≤ 0.123, and H-IDLE correlates *positively*) [V via G4]. "Correlation with Hoffman metrics" therefore validates against a weak proxy, not against human-rated fluency. That contradicts Narrative §3 ("predicts human-rated fluency").
   - (c) A per-participant correlation at n≈18–39 is underpowered. G4's calculation puts the requirement at n≈543 for Hoffman-sized effects; a trial-level mixed model is needed (G4 §6; simulation not re-run by me).

   Song et al. 2607.00530 already ran an n=24 spoken-command study on a low-cost arm [V via G4]. Cite it and scope C3 to *interruption* metrics.

## Major Issues
4. **The baselines are strawmen.** All three named baselines stop, wait, or retract. A reviewer will ask why the method is not compared with a switch that does not stop. G2 §6 lists the minimum set:
   - B2: bare switch;
   - B3: truncate + fresh chunk, no RTC (needed to isolate the contribution of RTC);
   - B6: ReSteer-style switch-data fine-tune.

   Without B3, gains cannot be attributed to the inpainting. Also, "LeRobot async" is stale: the legacy stack was retired on main, and the stop path is now `set_task()` ("Expect a stop during this transition") [V via G2 code read].
5. **"SmolVLA/ACT" is internally inconsistent.** LeRobot's ACT has no language input and no RTC [V via G2 §3c]. Instruction-triggered repair is therefore SmolVLA-only. ACT can serve at most as a checkpoint-switch or motion-quality baseline.
6. **The metrics are not operationalised.**
   - "Repair latency" has no defined onset: speech onset, the semantic disambiguation point ("…the *left* bowl"), or end of utterance? For self-corrections this choice decides the result.
   - "Trajectory continuity" and "false-barge-in rate" have no definition or denominator.
   - Onsets should be state-based (approach/grasp/transport/place), as in 10 §4.
   - No control separates speech-pipeline failure from task-island failure; 10 §4 proposes a bare-text-switch reference for this.
7. **Benchmark protocol precedent is not acknowledged.** The paired with/without-interruption design and the timing grid come from Causeway and LIBERO-MAX. G1 §5 says to "borrow their protocol rather than claim it". ARMS (text-based interruption-recall metrics) and Yu & Qiu 2606.08881 (an SO-101 failure taxonomy with SmolVLA/ACT) also need positioning, because C1 says "failure taxonomy" on SO-101 without qualification [V via G1].
8. **Scoop risk is understated.** The story says "medium-high"; 05 and G1 say **high**, based on 11 adjacent papers dated 2026-09-21 to 2026-10-14 and a Skoltech group with both SocialVLA and JitterVLA [V dates via G1; the group-merge risk is inference]. The story should carry the G1 differentiators: residual motion and retraction conditioned on onset, backchannel spurious halts, phase-anchored spoken corrections, and validity.
9. **Safety and semantics of "cancel".** A no-hold method still needs a guaranteed stop for "cancel" and safety words. The story lists "cancel" but never states a hold fallback.

## Minor Issues
- "runs on commodity GPUs" is unmeasured. SmolVLA alone is ~99 ms on an RTX 4090 [V via G2], but the latency of the full ASR + turn-model + LLM cascade is [U]. Mark it as a planned measurement.
- "voice-cloned TTS (EchoChain protocol)": G1 records only EchoChain's injection point, not voice cloning [U].
- PMQ was validated for non-embodied speech interfaces [V via G4]; on an arm it is exploratory. SUS measures usability, not fluency.
- "Best-paper potential" is unsupported; remove it.
- The story has no trial counts, scene list, statistics plan, or sim platform choice; 10 §4 has more detail than the story itself.

## Reproducibility and Verification
- **Data/code: not run.** 10 §4 says "nothing built yet". There is no benchmark, metric code, sim scene, or result. Every quantitative outcome is `TODO: run experiment`.
- **Checked this pass:** SocialVLA and Causeway abstracts via the arXiv export API (both claims used above match).
- **Inherited, not re-checked:** G2 LeRobot code facts; G4 correlations and power simulation. G2 is a partial delivery with no provenance sidecar.
- **Verification: BLOCKED** (inherited): NeurIPS 2026 RTCA accepted papers, RIAP full text, ELLSA repository. These are evidence gaps, not weaknesses of the story, but they leave C1's novelty provisional.

## Inline Annotations
| Location | Text | Annotation |
|---|---|---|
| Narrative 2 | "None measure or optimise … physically" | False as written (SocialVLA, MIRA). Replace with the conjunction claim. **Critical.** |
| Narrative 2 | stop/retract/wait/act-early list | Add switch-without-retract (SwitchVLA, ReSteer, Causeway) and SocialVLA's hold-then-revise. |
| C1 | "failure taxonomy" | Qualify: interruption-specific physical taxonomy; cite EchoChain, RoboRecover, Yu & Qiu, ARMS. |
| C2 | "on SmolVLA/ACT" | SmolVLA only for language-triggered repair. |
| C2 | "chunk truncation + RTC" | Name the wedge (latency-bounded committed prefix, `keep` ablation) and the prefix-bias risk. |
| C3 | "showing correlation" | Present it as a hypothesis; use a trial-level design; use human ratings as the criterion, not Hoffman metrics. |
| Experiments | "LeRobot async" | Replace with `set_task` hold-and-refresh; add B2, B3, B6. |

## Recommendation
**Major revision of the story before the direction decision.** The core idea survives in narrowed form [inference from G1/G2/G4]. As currently framed it would face a likely reject at IROS on novelty and baselines.

Minimum rewrite:
1. Conjunction-based C1.
2. Wedge-specific C2 with B2/B3/B6.
3. C3 as a hypothesis with a trial-level design and human-rating criteria.
4. Positioning against SocialVLA, Causeway/LIBERO-MAX, SwitchVLA/ReSteer, ARMS, Yu & Qiu and Song.
5. Scoop risk raised to high.

## Sources
- SocialVLA (2026) — https://arxiv.org/abs/2610.02360 [V this pass]
- Causeway (2026) — https://arxiv.org/abs/2609.30913 [V this pass]
- Inherited from G1/G2/G4, arXiv IDs: 2609.24547 (MIRA), 2506.03574 (SwitchVLA), 2603.17300 (ReSteer), 2609.36518 (LIBERO-MAX), 2609.28429 (ARMS), 2606.08881 (Yu & Qiu), 2607.26055 (πR²), 2607.00530 (Song), 2604.16456 (EchoChain); https://github.com/huggingface/lerobot
- Local: the artifact, 05, 10, G1, G2, G4, and `outputs/.drafts/paper-story-review-evidence.md`
