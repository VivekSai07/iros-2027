# Research notes (direct mode) — G1 novelty re-check

Date: 2026-10-18. Tools: alpha_search (alphaXiv index), feynman_science_database_search (arXiv API, Semantic Scholar, OpenAlex), alpha_ask_paper / alpha_get_paper for targeted reads.

## Exact search terms used
1. alpha_search (all): "benchmark for spoken interruptions during robot manipulation, barge-in while the robot is moving, failure taxonomy"
2. alpha_search (semantic): "full-duplex vision-language-action model speech interruption mid-execution correction"
3. alpha_search (both): "EchoChain interruption benchmark realtime voice models contextual inertia interruption amnesia objective displacement"
4. alpha_search (semantic): "robot changes instruction mid-execution benchmark, user corrects target object while arm is moving, real-time language correction evaluation"
5. alpha_search (semantic): "speech-conditioned VLA audio input interruption during manipulation embodied agent spoken command overlap"
6. alpha_search (semantic): "interruptible robot motion human-robot interaction stop halt residual motion evaluation streaming speech"
7. alpha_search (keyword): "ELLSA end-to-end full-duplex listen speak see act"
8. alpha_search (keyword): "VITA-E natural embodied interaction concurrent seeing hearing speaking acting"
9. alpha_search (keyword): "SwitchVLA execution-aware task switching vision-language-action"
10. alpha_search (keyword): "MAIL-Bench interruption benchmark"
11. alpha_search (keyword): "Premover streaming speech prefix VLA readiness gate"
12. alpha_search (semantic): "RIAP incremental intent act wait defer speech-driven manipulation unsafe commits"
13. alpha_search (keyword): "NIABench"
14. alpha_search (keyword): "Full-Duplex-Bench v2 multi-turn evaluation full-duplex spoken dialogue models interruption"
15. alpha_search (keyword): "Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities"
16. alpha_search (keyword): "LIBERO-PRO LIBERO-Plus robustness perturbation language instruction VLA benchmark"
17. alpha_search (semantic): "Yell At Your Robot language corrections RACER rich language-guided failure recovery RT-H action hierarchies"
18. alpha_search (keyword): "Talking Turns benchmarking audio foundation models turn-taking"
19. alpha_search (semantic): "voice-controlled robot arm user interrupts with new spoken command during execution, evaluate replanning latency and smoothness"
20. alpha_search (semantic): "embodied agent benchmark user interruption simulation household tasks instruction update while executing"
21. Semantic Scholar: "Full-Duplex-Bench benchmark full-duplex spoken dialogue turn-taking"; "Full-Duplex-Bench v1.5 overlap handling"; "Full-Duplex-Bench-v2 multi-turn automated examiner"; "LIBERO-Plus in-depth robustness analysis vision-language-action models"
22. OpenAlex (S2 rate-limited fallback): "LIBERO-PRO robust fair evaluation VLA beyond memorization"
23. arXiv API id lookup: 2403.12910, 2403.01823, 2510.16756, 2510.21817, 2506.03574, 2604.16456

## ID resolution (tool-confirmed)
| Item | ID | Resolved by |
|---|---|---|
| ELLSA "End-to-end Listen, Look, Speak and Act" (ICLR 2026 journal_ref) | 2510.16756 | arXiv API [V] |
| VITA-E | 2510.21817 | arXiv API [V] |
| SwitchVLA | 2506.03574 | arXiv API [V] |
| EchoChain (Labelbox) | 2604.16456 | arXiv API [V] |
| YAY Robot | 2403.12910 | arXiv API [V] |
| RT-H | 2403.01823 | arXiv API [V] |
| RACER | 2409.14674 | alphaXiv index [V metadata] |
| Full-Duplex-Bench v1 | 2503.04721 | Semantic Scholar (ASRU 2025) [V metadata] |
| Full-Duplex-Bench v1.5 | 2507.23159 | Semantic Scholar (ICASSP 2026) [V metadata] |
| Full-Duplex-Bench-v2 | 2510.07838 | Semantic Scholar (ACL 2026 short) [V metadata] |
| Full-Duplex-Bench-v3 | 2604.04847 | alphaXiv index |
| FD-Bench | 2507.19040 | Semantic Scholar |
| Talking Turns | 2503.01174 | alphaXiv index |
| TurnBench | 2608.25218 | alphaXiv index |
| LIBERO-PRO | 2510.03827 | OpenAlex |
| LIBERO-Plus | 2510.13626 | Semantic Scholar |
| Premover | 2605.12160 | alphaXiv index |
| NIABench "Assistance Without Interruption" | 2605.01368 | alphaXiv index |
| One Word, Different Action | 2609.05260 | alphaXiv index |
| RoboRecover | 2609.28952 | alphaXiv index |
| SocialVLA | 2610.02360 | alphaXiv index |
| MAIL-Bench | not resolved by name; candidate = 2609.35003 "Learning to Act under Visual Interruptions with VLA Models" (to confirm) | |
| RIAP | NOT found on arXiv/alphaXiv by any query → remains [U] beyond prior abstract read | |

## New candidates surfaced (2026-06 → 2026-10-18), to triage
- MIRA 2609.24547 (full-duplex HRI, interruptible motions, Astribot) — HIGH relevance
- Watch, Recall, Act 2609.28429 (always-on robots, concurrent embodied streams) — HIGH
- Towards an Extensible Benchmark for Spoken Dialogue with Social Robots 2610.08733 — HIGH (spoken + robot benchmark)
- Causeway 2609.30913 (instruction switching in VLA after state altered) — MED
- CIRRA 2610.08862 (instructions during ongoing execution, household) — MED
- JitterVLA 2610.13628 (replay benchmark for motion quality in VLA HRI) — MED (metric overlap: continuity)
- RASSG 2610.14659 (streaming tool execution, self-corrections invalidate launched tools) — MED (speech-side analog)
- EarlyCommit 2610.20531 (robots acting before you finish speaking, word-by-word) — MED (G3 area)
- Continue, Adapt, or Yield 2609.13117 (in-turn adaptation to overlap, speech-only) — MED
- LIBERO-MAX 2609.36518 (world changes mid-task) — LOW-MED
- LIBERO-RECOVER 2609.05178, SafeStage 2609.21223, MAGMA-Bench 2610.13534 — LOW-MED
- ELLSA 2 2610.21452 (speech+expressions+gestures) — check whether manipulation
- DuplexSLA 2605.20755 (speech-language-action, tool actions) — LOW (action = tool calls?)
- IHBench 2606.19595, When Intent Arrives Late 2610.00272, DuplexAct-Bench 2609.39446, M3-DuplexBench 2607.29125 — speech-only
- PACT-SLM contract test 2609.38232 — speech-only commit

## Deep-read findings (full text via alpha_ask_paper / alpha_get_paper)

### MIRA 2609.24547 (v2, 22 Sep 2026; IDEA + Astribot) [V full text]
- Full-duplex speech companion on Astribot S1 humanoid. Motion = co-speech gestures + discrete social behaviours (greet/listen/dance). NO object manipulation.
- Barge-in: VAD fast interruption gate, 450 ms confirmation threshold; on barge-in "active speech and joint trajectories are immediately preempted and cancelled ... safe physical halting". Bounded commitment RHPC: 15-frame (0.50 s) committed prefix.
- Metric: "Deterministic Interruption Preemption speech_started → abort_cmd_sent 466 ms" (P50). No residual-motion/continuity/false-barge-in metrics reported as a benchmark; arbiter decisions IGNORE / REPLY / INTERRUPT_AND_REPLY evaluated qualitatively on traces.
- No human-subject study ("long-term human-subject studies ... remain an important next step").
- Relevance: closest *speech-overlap + physical motion* system, but stop-only, no manipulation, not a benchmark.

### ARMS / "Watch, Recall, Act" 2609.28429 (v2, 9 Oct 2026; SJTU, CUHK, Astribot...) [V full text]
- Always-on dual-arm manipulation (Cobot Magic, real) with π0.5 backbone; language (text) guards and recall instructions arrive mid-stream. No speech audio.
- ARMS Dataset: ~200 never-reset staged streams + ~1,200 skill demos; ~150 trials per method; real-robot N = 60 per method/segment.
- Metrics: cross-interruption recall, foreground-continuation rate (FG-Res.), self-history consistency, dual-arm non-interference, overload ordering, PAUC timeliness, combined EAS. ARMS 45% EAS vs 28% SwitchVLA; human/oracle 85%.
- Table 1 axes include "Interruptible: can switch to a newly arriving instruction mid-execution".
- No physical failure taxonomy of the G1 kind (residual motion, retraction, spurious halt); timing of instruction relative to motion phase not controlled as a variable; no human validation of metrics.
- Relevance: nearest *manipulation* benchmark with interruption-survival metrics (FG-Res ≈ anti-"objective displacement"; recall across interruption ≈ anti-"amnesia"). Text, not speech.

### Kennington et al. 2610.08733 (6 Oct 2026; Boise State, Semio, Peerbots, Georgia Tech) [V full text]
- Position/sketch of a benchmark: collaborative pentomino puzzle game with Misty II; robot is instruction giver; "the goal is not to require the robot to perform complex physical manipulations". Manipulation only as a proposed extension.
- Proposed metrics: puzzles completed, time, dialogue turns, initiations, clarification requests, "among others (e.g., interruptions, barge-ins)". No data, no results. Retico framework.
- Relevance: signals the SLIVAR/SDS+HRI community wants a spoken-HRI benchmark; low current scoop risk for G1, but a likely future venue for overlap.

### One Word, Different Action 2609.05260 (4 Sep 2026; CUHK-Shenzhen, SRIBD) [V full text via alphaXiv report]
- 85 physical decision anchors (21 object-centric, 64 action-sequence); 988 atomic task families / 3,952 instances; 102 compositional families / 408 instances.
- Evaluates text LLMs (GLM-5-FP8, Qwen2.5-7B, Mistral-7B, OLMo-2-7B) on finite decision space; metrics: atomic/compositional accuracy, decision invariance/sensitivity, conditional composition success.
- Not mid-execution, no speech, no trajectory; limitation stated: "use text models and fixed decision representations rather than full VLA systems operating continuously".

### RoboRecover 2609.28952 (24 Sep 2026; Renmin U.) [V full text]
- 2,000 sim scenarios (RoboTwin + LIBERO, 1,000 each, 800/200 split). Recovery from execution-induced deviation via action-prefix replay.
- Taxonomy: Recovery Stage {Approach, Contact, Move, Place} × Deviation Type {Wrong Target, Wrong Pose, Stage Rollback, Scene Change}.
- Metric: Recovery Success Rate (RSR), Macro-9 RSR. E.g., LIBERO π0.5 64.40% RSR vs 94.17% initial-state.
- No language change, no speech, no interruption. Useful precedent for *prefix-replay* protocol and *physical deviation taxonomy*.
- Cites "Benchmarking VLA Models on SO-101: Failure and Recovery Analysis" (Yu & Qiu 2026, arXiv 2606.08881) [S — via RoboRecover reference list; not independently checked yet].

## Abstract-level verification via arXiv API (export.arxiv.org id_list) [V abstract]
- **MAIL-Bench = 2609.35003** "Learning to Act under Visual Interruptions with VLA Models" (U. Sydney, 28 Sep 2026): interruption = *camera stream loss* at multiple stages of reference trajectory; π0.5, GR00T N1.5; real AgiBot G2. No speech/language. ID now resolved (was [S]).
- **Causeway 2609.30913** (UMD/USC, 25 Sep 2026): text instruction switching "during or after" another task; "task islands"; 71 cross-object pairs, **three switch timings**, 3 VLA architectures, LIBERO-Goal; bare-switch success 3–26% → 47–65%; "rate of reaching the handoff neighborhood" +42–72 pp; real xArm. Text, no speech audio, no human validation in abstract. **Closest manipulation-side protocol with switch timing as a variable.**
- **CIRRA / CHIRP 2610.08862** (5 Oct 2026, v2 12 Oct): CHIRP = *text-based* benchmark, 120 episodes, 8 household envs; plan-level instruction reconciliation; Unitree G1 "interrupts ongoing skills at the correct moment in every trial". Plan/skill level, text.
- **JitterVLA 2610.13628** (Skoltech, 9 Oct 2026): replay benchmark for motion quality (jerk) of VLA pipelines; 838 episodes; 20 people's hand trajectories; UR3; p99 jerk 615→106 m/s^3 with interpolation. No interruption/speech; relevant as *continuity metric* precedent.
- **RASSG 2610.14659** (Beihang, 10 Oct 2026): streaming speech tool execution; self-corrections cause "stale execution whose irreversible effects persist"; stale execution rate 50.00% → 3.15% on ReCAST prospective-repair subset; also FDB-v3, Audio2Tool. Software tools, not physical. Conceptual analog of wrong-object commit / irreversibility.
- **EarlyCommit 2610.20531** (U. Copenhagen, 14 Oct 2026): word-by-word object commitment from streaming speech; threshold τ; ≥92% correct at τ=0.9; 31–35 ms/word. Pre-execution commit, not mid-motion repair. Extends G3 crowding.
- **SocialVLA 2610.02360** [V abstract re-check]: Unitree G1; 15 participants; 238 intervention-worthy episodes; 1.038 h non-intervention; false-stop episodes 100 → 57 with relevance estimation; VLA-gate-to-physical-hold 336 ms; reaction-onset-to-hold 1.021 s; verbal correction channel → continuation/restart/instruction revision. **Has a false-stop (≈ false barge-in) measure and real human reactions, but stop-centric, detector paper, not a benchmark of repair quality.**
- **Continue, Adapt, or Yield / Duplex Cue 2609.13117** (Besimple AI, 11 Sep 2026): speech-only; continue/adapt/yield taxonomy; 300 human-confirmed cues, 208 pairs; humans adapt 68.2% vs PersonaPlex 34.8% on 66 collaborative pairs. **Speech-side analog of "mid-motion repair vs stop"** — useful framing citation.
- **Yu & Qiu 2606.08881** "Benchmarking VLA Models on SO-101: Failure and Recovery Analysis" (7 Jun 2026): real SO-101; π0.5, SmolVLA, Wall-X, ACT; 4 tasks; failure taxonomy + recovery-aware metrics. No interruption/speech. Same platform & policies as team → must cite; reduces novelty of "SO-101 failure taxonomy" per se.
- **Premover 2605.12160 v2** (updated 5 Oct 2026): SO-101 with speech + online transcription; wall-clock 60.5 s → 49.7 s (−17.9%); LIBERO −8.3%.

### ELLSA 2510.16756 (v2, ICLR 2026) — barge-in evaluation details [V full text]
- Sim only (LIBERO); "has yet to be validated in real-world settings" (Limitations).
- Barge-in commands: 10 fixed phrases (App. D.1: "Stop now", "Hold on", "Pause here", "Wait a second", "Freeze for a moment", "Stop what you're doing", "Hold it right there", "Wait, not yet", "Pause the action", "Do not move"); TTS CosyVoice2-0.5B; 150 generations/command for training, 20 for test; speakers from LibriHeavy.
- Timing: speech query introduced "2–8 seconds after the initial action instruction" (random, not phase-anchored).
- Metric: success rate; interruptive command 94.3%, general question 100%, silence 100% (Table 3c); 100 episodes per suite.
- Expected behaviour = output "Action Cancelled" and stop. No residual motion, no repair/redirect, no backchannel handling ("user and assistant backchanneling remain unaddressed").

### VITA-E 2510.21817 — interactive evaluation [V full text]
- Fourier GR2 humanoid. Speech interruption 100%, task switching 93.3%, emergency stop 100%, each over 30 trials (Table 2). Voice-response latency 2.26 s (10 tests, concurrency task).
- Switching: "a retraction mechanism ... returns the robot to the initial pose by sequentially popping and executing inverse movements from a stored action stack". Future work: "smoother and more efficient transitions".
- Interruption timing in eval not reported as controlled; training data inject "Stop!" "at a random point". No user study (ablation accuracy judged by human evaluators only).

### RIAP
- Not found by alphaXiv (semantic) or Semantic Scholar queries on 2026-10-18 → no arXiv ID; details remain as previously recorded from NeurIPS listing abstract only [U for anything beyond that abstract; "8,160-trial protocol" not re-verified in this pass].

### Speech-only benchmarks (metadata verified; content per abstract)
- FDB v1 2503.04721 (ASRU 2025): pause handling, backchannel, turn-taking, interruption.
- FDB v1.5 2507.23159 (ICASSP 2026): "first fully automated benchmark ... during speech overlap"; four scenarios: user interruption, user backchannel, talking to others, background speech.
- FDB-v2 2510.07838 (ACL 2026 short): automated examiner; task families daily, correction, entity tracking, safety; Fast vs Slow pacing.
- FDB-v3 2604.04847: tool use under real-world disfluency (real human audio per abstract snippet "dataset consists entirely ...").
- FD-Bench 2507.19040 (Interspeech): LLM+TTS+ASR pipeline; user interruptions, delays.
- Talking Turns 2503.01174 (ICLR 2025): turn-taking judge trained on human-human conversations.
- TurnBench 2608.25218: multi-domain turn-taking benchmark.
- EchoChain 2604.16456: 3 failure patterns; interruptions "at a standardized point relative to assistant speech onset"; half-duplex control reduces failures by 40.2%; no model > 50%.
- Duplex Cue 2609.13117: continue/adapt/yield.
- DuplexSLA-Bench 2605.20755: pause/interrupt/backchannel + in-conversation tool calling (tools, not physical).

### Other mid-execution manipulation benchmarks (abstract) [V abstract]
- LIBERO-MAX 2609.36518: 8,000 paired cases, 8 change types (geometry, observations, appearance, clutter, paths); paired with/without mid-task event holding task, init state, seed and pre-event action sequence fixed; events reduce success 11.0–25.7 pp across 14 policies. World events, not language/speech. **Paired protocol is directly reusable for G1.**
- SafeStage 2609.21223: 97 risk scenarios; before/during/after safety; no interruption/speech.
- NIABench 2605.01368: sim benchmark for *non-intrusive* assistance (robot must avoid interrupting the human) — inverse direction of G1.
- ELLSA 2 2610.21452 (15 Oct 2026): speech + gestures/expressions; no manipulation.
- Human–VLA Communication Gap 2610.17746 (Stanford, 13 Oct 2026): natural instruction phrasing vs π0.5; not interruption.
- LIBERO-PRO 2510.03827 (OpenAlex) and LIBERO-Plus 2510.13626 (S2): pre-execution perturbations incl. language; no mid-execution events.
- YAY Robot 2403.12910, RT-H 2403.01823 (arXiv API): language corrections during execution as supervision; real hardware; not benchmarks of interruption timing. RACER 2409.14674: language-guided recovery (metadata).

## Web pass (web_search via exa; fetch_content)
Queries: "RIAP NeurIPS 2026 incremental intent act wait defer robot speech"; "benchmark spoken interruption robot manipulation 2026 barge-in VLA"; "\"interruption\" benchmark robot arm speech correction mid-motion 2026 arXiv".

- **RIAP** — https://neurips.cc/virtual/2026/poster/162424 [V abstract, fetched 2026-10-18]: "Through 8,160 simulation replays, RIAP cut unsafe commitments from 27.5% to 1.6%, anticipated user commands by an average of 1,022 ms, and corrected for 60.6% of mid-utterance human revisions ... A 30-participant study ...". Title/authors/track not shown on page.
  - **CORRECTION to 04-literature-map.md**: map says "0% unsafe commits vs 27.5%"; the abstract says **1.6%** (from 27.5%). Also "8,160 simulation replays", not "trials".
- **SafeVLA-Bench 3.0** — https://github.com/Jatshi/SafeVLA-Bench [V README, truncated]: sim (ManiSkill) "uncertainty-aware speech–vision–action robot policies"; spoken instruction *before* acting under audio SNR noise; execute/clarify/stop gate; metrics danger, coverage, success, selective success. No interruption timing, no human study found in README. LeRobot report contract mentioned. Low G1 overlap; note as speech-conditioned safety benchmark.
- **NeurIPS 2026 RTCA workshop** (Real-Time Conversational Agents; Sydney, 12 Dec 2026; submissions closed 10 Sep 2026; notification 29 Sep) — https://rtcaneurips26.github.io/ [V]: topics include "interruption handling" and "Datasets and benchmarks for interactive ... evaluation"; no accepted-paper list on site. **OpenReview group page is JavaScript-rendered → BLOCKED (not worked around).** Scoop-watch item: accepted papers may appear on arXiv before Dec 2026.

## Blocked
- OpenReview NeurIPS 2026 RTCA group page (JS-rendered; fetch failed). Not bypassed.
- ELLSA GitHub (bytedance/SALMONN, ELLSA branch) — previously ROBOTS_DISALLOWED (D-007); not re-attempted.
- Semantic Scholar one query rate-limited (429) → OpenAlex fallback used automatically (LIBERO-PRO).
- RIAP full text: no arXiv/preprint found; only NeurIPS abstract page accessible.
