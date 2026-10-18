# Literature map (H1 focus)

Status flags: [V] verified from primary page/abstract in this research; [S] secondary only; [U] unverified. Paywalled IEEE/ACM versions were seen via abstracts/preprints only.

## 1. Full-duplex / interruption-aware manipulation
| Paper | Key findings | Limits | Status |
|---|---|---|---|
| **ELLSA** (SALMONN, ByteDance) | SA-MoE: Llama-3.1-8B speech expert + UniVLA/Emu3 action expert; 1 s time blocks; LIBERO sim only; barge-in = "Action Cancelled"+stop for 10 fixed TTS phrases, 94.3% interruptive-command success; 854 ms per-block latency | No backchannel handling; no real-robot validation; heavy (~2×8B); code release unverified (GitHub ROBOTS_DISALLOWED → user check) | [V] paper, [U] code |
| **VITA-E** | Dual Active/Standby VLA; tokens [ACT]/[HALT]/[END]/[RES]; Fourier GR2 humanoid; speech interruption 100%, task switching 93.3%, e-stop 100% (30 trials); voice latency 2.26 s | Switching *retracts to initial pose* via stored inverse movements; humanoid data; 7B VLM + GR00T; future work lists real-time feedback & smoother transitions. Code: github VITA-MLLM/VITA-E | [V] |
| **EchoChain** | Benchmark of 200 interrupted conversations; failure taxonomy: contextual inertia, interruption amnesia, objective displacement; no model >50% (Grok 48.5, GPT-realtime 45.0, Nova 26.5, Gemini 16.5); planner-simulator + voice-cloned TTS users | Speech-only; no physical consequences | [V] |
| **SwitchVLA** | Execution-aware *text* task switching; sim + real | Text, not speech overlap | [V] |
| Hi Robot | VLM rerun on correction; waits for atomic step | No mid-motion repair | [V] |
| YAY Robot, RT-H, RACER | Language corrections as supervision/recovery | Offline/step-level | [S] |
| CoRe (2608.14822) | Inference-time recovery | — | [S] |
| VLA-Feedback (2609.21022) | Intra-chunk feedback denoising | Not speech | [S] |
| **RTC** (2506.07339) | Real-Time Chunking: inpainting-based async execution for any flow/diffusion policy | Not tied to speech | [V] |
| LeRobot/SmolVLA async stack | policy_server/robot_client | Baseline infrastructure | [V] |

## 2. Incremental / streaming HRI
| Paper | Findings | Limits |
|---|---|---|
| Tufts/TU Wien IROS 2025 | Incremental CCG parser + BoundMPC online planning, 7-DoF real robot; 6-type constraint taxonomy (manner/target/object/action/safety/sequential) | Hand-built grammar, known objects, no vision, no human study [V] |
| Kennington/Lison/Schlangen survey (2501.00953) | Timing as decision variable, non-monotonicity, action on partial input; little incremental DM research | Survey [V] |
| **Premover** (2605.12160) | Frozen VLA acts on streaming speech prefix with readiness gate; real SO-101 + π0.5; 86.0% vs 81.0%; 17.9% wall-clock reduction | Explicitly does not handle corrections after execution begins [V] |
| **RIAP** (NeurIPS 2026 listing 162424) | Act/wait/defer via incremental intent belief + state-dependent costs; 8,160 *simulation replays*; unsafe commitments 27.5% → **1.6%** (corrected 2026-10-18; earlier entry said 0%); anticipates commands by 1,022 ms; corrects 60.6% of mid-utterance revisions; N=30 human study | No arXiv/preprint found; title/authors not on page; details beyond abstract [U] [V abstract, re-fetched 2026-10-18] | **UPDATE 2026-10-18 (full text read, `inputs/riap-notes.md`):** NeurIPS 2026 *workshop* paper; replay is synthetic (no speech audio, no physics, no humans); N=30 study is a browser mobile-base ratings study comparing system bundles; no code; WAIT cannot brake motion in progress. Not a G1/G2 competitor. [V]
| Loth et al. 2018 | Error cost & commitment in early speech hypotheses | Older [S] |
| ExpressMM (2604.05320) | Turtlebot-4 + SO-101; GPT-5.2 planner + π0.5; plan-level replan; n=23 audience Likert | Plan-level only [V] |
| SocialVLA (2610.02360) | Unitree G1; 15 participants; reaction-based stop, 336 ms gate-to-hold, 1.021 s onset-to-hold; verbal correction channel | Humanoid; stop-centric [V] |
| CMU bidirectional pHRI (HRI 2026) | n=18 older adults; speech-adjusted physical assistance | Paywalled; abstract only [V abstract] |
| MICoBot (2508.05535) | Mixed-initiative dialog; physical trials with 18 participants | Dialog-level [V] |
| One Word, Different Action (2609.05260) | Real-robot benchmark for instruction change | Text instruction change [V] |
| RoboRecover (2609.28952), MAIL-Bench (2609.35003) | Recovery from execution deviations (Stage × Deviation incl. Wrong Target); MAIL-Bench = camera-loss "interruptions" | No language/speech [V] (2026-10-18) |

_2026-10-18 G1 re-check additions (details + matrix in `outputs/g1-interruption-benchmark-novelty.md`):_ Causeway 2609.30913 (text switch, 3 switch timings) [V abs]; LIBERO-MAX 2609.36518 (paired mid-task events) [V abs]; ARMS/Watch-Recall-Act 2609.28429 (text, real dual-arm, cross-interruption recall, FG-continuation) [V]; MIRA 2609.24547 (speech barge-in halts co-speech gestures, 466 ms; no manipulation) [V]; JitterVLA 2610.13628 (motion-quality replay) [V abs]; RASSG 2610.14659 (stale tool execution under speech self-corrections) [V abs]; EarlyCommit 2610.20531 [V abs]; Duplex Cue 2609.13117 (continue/adapt/yield) [V abs]; Kennington et al. 2610.08733 (spoken-HRI benchmark proposal) [V]; Yu & Qiu 2606.08881 (SO-101 VLA failure/recovery benchmark incl. SmolVLA, ACT) [V abs]; CIRRA/CHIRP 2610.08862 [V abs]; SafeVLA-Bench (GitHub) [V README]. |

## 3. Turn-taking & speech stack
Easy Turn (2509.23938; open model + 1,145 h dataset; states complete/incomplete/backchannel/wait); Talking Turns (2503.01174, ICLR 2025); TurnBench (2608.25218; causal commit timestamps under FPR budget); Skantze & Irfan HRI 2025 (TurnGPT+VAP, n=39 within-subject, Furhat); DuplexPO (2607.07148); DuplexCascade (2603.09180); DuplexOmni (2606.09186); Full-Duplex-Bench v1/v1.5/v2; FD-Bench; FLEXI; VoxMind (2604.15710, spoken tool use); RoboEgo (2506.01934); DyaPlex (2606.03874). Streaming ASR (faster-whisper) + TTS (XTTS-v2) as used in Premover. [V/S mixed — see bibliography]

## 4. HRI evaluation methodology
Hoffman fluency metrics (human idle time, robot idle time, concurrent activity, functional delay; MAD-TN adds concurrent inactivity/resource delay) — original paper seen only via citing papers [S]. Questionnaires: PMQ, Almere, SUS. Typical user-study N: 12–39. PACT sim-human protocol and Clarification Utility = Acc/(1+AskRate). EchoChain voice-clone protocol.

## 5. H2 prior art & position paper
PACT (2605.24350), Event-Driven Proactive Assistive Manipulation (2603.23950), NIABench (2605.01368), Attentive Support, Baraglia et al., AURA, LIT (2406.13787), HOI4ABOT, GUIDER, Smart Help. Karcini et al. 2026 (2606.06556): four missing pillars — physical data engine/autolabelling, task-preserving retargeting, physics-grounded world models for consequence prediction, self-improving deployment loops (human corrections). Related: π*0.6 RECAP.

## 6. A+B related
NeuralActuator (2607.11734), FACTR 2, InsertAnything (0.02 mm clearance sim-trained), RL-100, Agia thesis, Newton 1.0 GA (VBD cables/cloth/rubber, iMPM granular, MuJoCo Warp, Isaac Lab 3.0 backend). SO-101 specs secondary-source.
