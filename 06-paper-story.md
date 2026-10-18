# Paper story v2 (working draft, H1: benchmark + method + validity)

Supersedes `06-paper-story.md` per `outputs/paper-story-review.md`. Flags [V]/[S]/[U] carried from evidence reports. **Nothing built or run: every outcome is `TODO: run experiment`.**

**Working title:** "Say It Mid-Motion: Benchmarking and Repairing Spoken Corrections During Manipulation on a Low-Cost Arm"

## Novelty claim (conjunction only)
Each ingredient has precedent [V, G1; G4]: spoken barge-in (ELLSA, VITA-E, SocialVLA), switch timing (Causeway, LIBERO-MAX), interruption metrics (ARMS), an SO-101 failure taxonomy (Yu & Qiu), spoken-command studies on low-cost arms (Song).

Our claim is only the **conjunction** of five properties:
1. **spoken** corrections,
2. **anchored to the motion phase**,
3. of ongoing **manipulation**,
4. scored with an interruption-specific **physical repair taxonomy** (residual motion, retraction, spurious halt, wrong-object commit, inertia/amnesia/displacement),
5. whose metrics are **validated against per-episode human ratings**.

We found no work that has all five [inference over G1's matrix; the search was not exhaustive]. We make no "first" claim about any single ingredient.

## Narrative
1. People correct collaborators while they act ("not that one, the left bowl").
2. Published systems take one of four approaches [V per system; the grouping is our synthesis, CMP §2]:
   - **Halt:** ELLSA, SocialVLA, MIRA, and LeRobot `set_task` when a request is in flight. These measure stops: SocialVLA reports gate→hold 336 ms and onset→hold 1.021 s; MIRA reports speech→abort command 466 ms [V].
   - **Retract:** VITA-E.
   - **Redirect from text only:** SwitchVLA, ReSteer, Causeway; Hi Robot re-plans immediately at the command level.
   - **Anticipate partial speech:** Premover, RIAP, EarlyCommit.

   None of them scores the physical quality of the repair while speech overlaps motion.
3. We contribute a phase-anchored benchmark with a physical repair taxonomy, a narrow SmolVLA/SO-101 repair method, and a test of whether its metrics predict human ratings.

## Positioning

| Work | Has | Lacks relative to us | Flag |
|---|---|---|---|
| SocialVLA 2610.02360 | Audio reactions and stop phrases; real G1 manipulation; hold latency; false stops; 15+1 participants | Not a benchmark; corrections only logged after the hold; no repair metric, phase control, or ratings | [V full text] |
| Causeway 2609.30913 | 3 switch timings; 71 pairs × 3 VLAs; Reach / Fin\|R; task islands | Text only; no overlap, motion-quality metrics, humans, or code | [V full text] |
| LIBERO-MAX 2609.36518 | Paired with/without mid-task events | No language events; sim only | [V abstract] |
| SwitchVLA 2506.03574 / ReSteer 2603.17300 | Learned switching from intermediate states without returning home | Text only; no continuity metric | [V] / [V report] |
| ARMS 2609.28429 | Cross-interruption recall and foreground continuation on a real robot | Text only; no phase control; no residual or retraction metric | [V] |
| Yu & Qiu 2606.08881 | SO-101 failure taxonomy with SmolVLA and ACT | Not interruption-specific | [V abstract] |
| Song 2607.00530 | n=24; spoken commands on a low-cost arm | No interruptions; no metric↔rating analysis | [V] |
| MIRA 2609.24547 | Streaming barge-in; bounded 0.5 s commitment | Gestures, not manipulation; latency only to command dispatch | [V] |
| RIAP (NeurIPS 2026) | Act/wait/defer on partial speech; N=30; unsafe commits 27.5%→1.6% | Physics and speech details unknown | [V abstract]; rest [U] |
| Premover 2605.12160 | Acts on streaming speech on a real SO-101 | Excludes corrections after motion starts | [V] |

**Borrowed, not claimed:** Causeway's timing grid, success relative to solo ρ_B, Reach / Fin|R and object strata; LIBERO-MAX's paired with/without design (absent from Causeway [V]; attribution is inference pending a full-text read); SocialVLA's hold criterion and latency decomposition.

## Contributions
- **C1 — Benchmark** (sim first, then real SO-101).
  - Interruption types: target change, constraint, speed/manner, cancel, self-correction, and backchannel (which should *not* interrupt).
  - Each is delivered at a state-defined onset and scored with the taxonomy and metrics below.
  - Distinctive measurements [G1 §3, inference]: residual-motion and retraction metrics conditioned on onset, and spurious halts on backchannels or self-corrections during manipulation. Neither is measured in surveyed work.
- **C2 — Speech-triggered, prefix-aware in-flight retargeting on SmolVLA/SO-101.**
  - All four parts are needed together [G2 §5, inference]:
    1. speech that overlaps motion triggers it;
    2. there is no hold or retract;
    3. the queued chunk is truncated to a latency-bounded committed prefix (keep k ≈ remaining inference steps) and re-denoised under the new instruction, with RTC guidance over that prefix only;
    4. it is evaluated with continuity metrics.
  - **Core risks, measured rather than assumed:**
    - *Prefix bias:* in-flight actions pull RTC toward the *old* intent [V, πR² 2607.26055].
    - *Task islands:* the instruction's effect on actions drops 1–2 orders of magnitude before contact [V, Causeway].
  - Ablation grid: keep k × schedule {ZEROS, LINEAR, EXP} × β {5, 10} × Jacobian {identity, VJP}.
  - **LeRobot `main`@146d847 gaps** [V code, RTC audit]: (1) identity Jacobian, not VJP (open PR #4945; may weaken seam continuity [U]); (2) β 10 vs paper 5; (3) LINEAR vs paper EXP schedule; (4) `execution_horizon` 10 is the guided-region length, and d above it leaves the first executed action unguided; (5) `set_task` holds on SO-101 if a request is in flight; (6) no per-request guidance profile; (7) no immediate re-request on task change in RTC mode. Effort: 3–5 dev-days + 2–4 for VJP [U].
- **C3 — hypothesis, not a finding.**
  - *H3:* one pre-specified trial-level benchmark metric predicts per-episode human fluency ratings beyond what condition labels explain.
  - Criterion: human ratings, not Hoffman's objective metrics, which correlate weakly with perceived fluency (|r| ≤ 0.123; H-IDLE positive) [V via G4] and stay exploratory. Scoped to *interruption* metrics, unlike Song.

## Research questions
- **RQ1:** Which taxonomy failures does each baseline produce, broken down by onset phase and utterance type?
- **RQ2:** Does C2 improve continuity and reduce retraction compared with B1–B3 and B6, without lowering post-repair success? Can we separate speech-pipeline failure from task-island failure?
- **RQ3:** Does H3 hold?

## Experiments

**Baselines** [G2 §6; RTC audit §4]

| ID | Behaviour | Flag |
|---|---|---|
| B1 | Hold-and-refresh with LeRobot `set_task`. This replaces the retired "LeRobot async" baseline | [V code] |
| B2 | Bare switch: queued old-task actions are kept | [V] |
| B3 | Truncate + fresh chunk without RTC; isolates the inpainting | [V] |
| B4 | Retract-to-home, then restart (VITA-E style) | [V] |
| B5 | Wait for the step boundary (Hi Robot / CIRRA style) | [V] |
| B6 | Fine-tune SmolVLA on ReSteer-style switch data; serves as both baseline and ablation | [V report] |

Optional: B7, a Causeway-style write. **All repair claims are SmolVLA-only.** LeRobot's ACT has no language input and no RTC [V code], so ACT appears only as B8, a reference for checkpoint switching and motion quality.

**State-based onsets.**
- The utterance fires when the arm reaches approach, grasp, transport or place. Phases are defined by hand–object distance and gripper state, not step count, because accessibility follows state [V, Causeway; thresholds TODO].
- We log three timestamps: speech onset $t_s$, the semantic disambiguation point $t_d$ (the first word that fixes the new goal, found by forced alignment), and utterance end $t_e$.

**Controls.**
- **Bare text switch:** the transcript is injected at $t_d$ from the same state. This isolates speech-pipeline failure.
- **State-placement reference:** task B is started from the switch state. This isolates task-island inaccessibility.
- **‖Δa‖ probe:** checks for the Causeway "gate" on SmolVLA.
- **Paired runs:** every scenario is also run without the interruption.

**Metrics** (our design choices; inference)
- **Repair latency:** $L_x = t_{\text{redirect}} - t_x$ for $x \in \{s,d,e\}$. $t_{\text{redirect}}$ is the first tick after which the end-effector distance to the new goal decreases for ≥ $W$ ms ($W$: TODO).
  - **Primary: $L_d$.** For self-corrections, $t_s$ comes before the robot has the information it needs.
- **Continuity:** $J=\max_{t\in[t_s,t_s+T]}\lVert\dddot q\rVert$, normalised by the paired uninterrupted run. We also report the seam jump $\lVert\ddot q(t^+_{\text{seam}})-\ddot q(t^-_{\text{seam}})\rVert$ ($T$: TODO).
- **Retraction:** $R=\int_{t_s}^{t_{\text{done}}}\max\big(0,\tfrac{d}{dt}\lVert x_{ee}-g_B\rVert\big)\,dt$.
- **Residual motion** (cancel/stop): end-effector path length from $t_s$ until a SocialVLA-style hold criterion is met (SO-101 thresholds: TODO). Onset→hold latency is reported as median, p95 and max.
- **Post-repair success:** measured relative to $\rho_B$ and split into Reach and Fin|R.
- **False-barge-in rate:**
  - Numerator: should-not-interrupt episodes (backchannel, off-target speech) with a spurious halt (velocity below hold threshold ≥ $H$ ms, absent in the paired run; $H$: TODO) or a goal change.
  - Denominator: **all should-not-interrupt episodes**. Also false stops per motion-hour (SocialVLA-comparable).

**Cancel and safety words bypass repair.**
- A keyword/VAD gate issues LeRobot's planned hold directly. SO-101 supports position hold [V code].
- This mirrors the separate fast-stop paths in VITA-E, MIRA and SocialVLA [V].
- Cancel is scored only on residual motion and hold latency. A hardware e-stop and human supervision are always in place.

**Speech.** TTS cloned only from consenting voice actors, as EchoChain did [V via G4], used as input only, never for ratings; plus real speakers. Streaming ASR → turn model → small-LLM cascade latency: **TODO: measure** (SmolVLA alone ~99 ms on RTX 4090 [V via G2]).

**Scale.**
- Scenes: two objects, two bowls, pick-place [10 §4].
- Simulator: MuJoCo or Isaac (TODO).
- Pairs, initial states and trials per cell: TODO. Causeway used 8 states × 3 rollouts.
- The LeRobot commit is pinned.

**Human study (C3)** [G4 §8]
- **Participants and conditions:** N=24 (minimum 20), within-subject. Conditions B1, B4, B5 and C2 in a balanced Latin square.
- **Episodes:** k=8 per condition. Onset phase varies *within* each condition.
- **Criterion:** a per-episode 7-point item adapted from Hoffman's direct-fluency subscale. Exact wording: TODO.
- **Model:** `rating ~ primary_metric + condition + (1 + primary_metric | participant)`, preregistered.
- **Power** (G4; random intercepts only, so optimistic):
  - beyond-condition power at r=0.2 falls from ≈0.97 to ≈0.37 as the condition's share of metric variance rises from 50% to 90%;
  - a between-participant r=0.3 needs n=85.
  - A pilot (n=4–6) must estimate within-condition variance before N is fixed.
- **Exploratory measures:** Hoffman objective metrics and PMQ (validated only for non-embodied interfaces). SUS (usability, not fluency) is optional.
- **Ethics:** the route is still unknown (Q8). Voice is biometric data under GDPR [V via G4].

## Why it can stand out
A reusable low-cost benchmark compared against LeRobot's shipped stop path; failure modes no surveyed work measures; validity tested, not asserted. Value depends on clean C1 and an honest C3 result either way.

## Risks and fallbacks
- **Scoop risk: HIGH.**
  - 11 adjacent papers appeared between 2026-09-21 and 2026-10-14 [V dates, G1].
  - The Skoltech group has published both SocialVLA and JitterVLA; a merged follow-up is plausible [inference].
  - We cannot check the RTCA workshop papers or RIAP's full text (blocked).
  - LeRobot lists "buffered motion" as a priority, and PR #4108 adds flush-based voice task switching [V].
  - Re-check novelty weekly.
- **Prefix bias or task islands erase C2's gains.** Reframe as a systematic study: C1 + C3, with C2 reported as a negative or ablation result.
- **C2 is not reliable on hardware by mid-January 2027.** IROS then gets the benchmark plus a pilot, and the full study moves to ICRA 2028 (~16 Aug 2027 [S, 10 §3]).
- **H3 fails.** Report it as a finding [S, G4 §9].
- **Ethics delay.** Start the approval route now. The worst case leaves ~2–4 weeks for data collection [G4 §7, inference].
- **LeRobot drift.** Keep our changes small, flagged and pinned.

## Sources
- SocialVLA https://arxiv.org/abs/2610.02360
- Causeway https://arxiv.org/abs/2609.30913
- LIBERO-MAX https://arxiv.org/abs/2609.36518
- SwitchVLA https://arxiv.org/abs/2506.03574
- ReSteer https://arxiv.org/abs/2603.17300
- ARMS https://arxiv.org/abs/2609.28429
- Yu & Qiu https://arxiv.org/abs/2606.08881
- Song https://arxiv.org/abs/2607.00530
- MIRA https://arxiv.org/abs/2609.24547
- RIAP https://neurips.cc/virtual/2026/poster/162424
- Premover https://arxiv.org/abs/2605.12160
- ELLSA https://arxiv.org/abs/2510.16756
- VITA-E https://arxiv.org/abs/2510.21817
- Hi Robot https://arxiv.org/abs/2502.19417
- EarlyCommit https://arxiv.org/abs/2610.20531
- πR² https://arxiv.org/abs/2607.26055
- RTC https://arxiv.org/abs/2506.07339
- EchoChain https://arxiv.org/abs/2604.16456
- JitterVLA https://arxiv.org/abs/2610.13628
- Hoffman 2019 https://doi.org/10.1109/THMS.2019.2904558
- LeRobot https://github.com/huggingface/lerobot (146d847)
- LeRobot PRs https://github.com/huggingface/lerobot/pull/4945, https://github.com/huggingface/lerobot/pull/4108
- Local: G1, G2, G4, CMP, RTC audit, Causeway/SocialVLA summaries, 05, 10
