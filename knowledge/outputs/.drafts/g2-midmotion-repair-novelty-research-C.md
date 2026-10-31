# G2 scoop-risk sweep (research-C): learned mid-motion repair of an in-flight action chunk triggered by overlapping speech, on a low-cost arm

Date of sweep: 2026-10-18. Window prioritized: 2026-06 onward.
Claim being protected (TARGET): *"learned mid-motion repair of an in-flight action chunk (VLA/ACT/flow/diffusion) triggered by overlapping speech, without stop-and-retract, on a low-cost arm."*

Flags: **[V]** = verified from primary text (arXiv API abstract record and/or full paper text pulled with `feynman alpha ask/get`); **[S]** = secondary (blog, thesis snippet, search-result summary); **[U]** = unverified.
I confirmed every arXiv ID below with the arXiv API (`export.arxiv.org/api/query?id_list=...`) unless it is marked [U].

Method notes (read these first):
- `feynman alpha ask <id> <question>` gave back the paper's full text (about 36–40 KB each) and no synthesized answer. I worked from that primary text by keyword-grepping for affiliations, robot, policy, trigger, stop/hold, and code URL. Some long papers may be cut off at the end, so appendix details could be missing (see Coverage Status).
- Numbers below are quoted exactly as the source states them.

---

## Part 1: the ten assigned papers

| # | Title (short) | arXiv ID / date (v1) | Org | What is repaired | Trigger | Mid-motion? | Real / sim | Base policy | Code / page | Closeness |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs (VLA-Feedback) | 2609.21022, 2026-09-17 [V] | UT Austin; U. Central Florida [V] | Each action of a diffusion chunk is corrected by a kept "final denoising step" using the latest observation [V] | Visual observation (moving objects/scene) [V] | Yes, per-action correction before execution, no rerun of the full VLA [V] | Sim (LIBERO + dynamic sim) and real Franka Emika Panda [V] | GR00T (frozen ~3B planner) + ~1.19M-param trainable feedback module [V] | https://vla-feedback.github.io [V] | **Partial**: learned in-flight chunk correction, but visual trigger, no speech, Franka |
| 2 | React When You Need To: Event-Triggered Asynchronous Inference for VLA Policies | 2609.22587, 2026-09-18 [V] | Technical University of Munich (+MBZUAI per alphaXiv listing [S]) [V] | Inference gap adapted; on an event it runs early inference and "smoothly transitions to the updated action chunk" (blend) [V] | Visual scene-change event estimator (VLA vision encoder) [V] | Yes, blends in a new chunk during execution [V] | Real Franka Emika Panda, static + dynamic settings [V] | π0.5 fine-tuned with LoRA [V] | https://react-when-you-need-to.github.io/ ; "code will be made publicly available upon acceptance" [V] | **Partial**: mid-chunk switch, but triggered by vision, no language/speech, Franka |
| 3 | MIRA: Real-Time Full-Duplex HRI for Embodied Companions | 2609.24547, 2026-09-21 (v2 09-22) [V] | International Digital Economy Academy; Astribot [V] | Co-speech gesture motion (ROSCO prefix-conditioned diffusion); RHPC commits only "the leading 15 frames (500 ms) of each 50-frame prediction horizon" [V] | Streaming user speech; VAD-based barge-in gate, 450 ms confirmation threshold [V] | **No repair**: barge-in → abort/"safe physical halting"; "speech_started → abort_cmd_sent 466 ms" [V] | Real Astribot S1 humanoid [V] | ROSCO (own diffusion motion model), not a manipulation VLA [V] | https://gagajian.github.io/MIRA/ [V] | **Partial**: speech barge-in during motion, but stop/abort, gestures not manipulation, humanoid |
| 4 | Full-Duplex Interaction with Speech, Expressions and Gestures (ELLSA 2) | 2610.21452, 2026-10-15 [V] | Tsinghua University; ByteDance [V] | Streaming gesture/expression generation alongside full-duplex dialogue [V] | Speech (full-duplex) [V] | N/A: no manipulation action chunks [V] | Avatar/gesture generation, no robot manipulation found in text [V] | ELLSA 2 chunk-wise synthesizer (no VLA) [V] | https://github.com/bytedance/SALMONN/tree/ELLSA2 [V] | **None** |
| 5 | End-to-end Listen, Look, Speak and Act (ELLSA) | 2510.16756, 2025-10-19 (v2 2026-04-20; ICLR 2026) [V] | Tsinghua University; ByteDance [V] | None. "Action barge-in": on an interruptive command ELLSA "is expected to respond with 'Action Cancelled' and immediately stop the action" [V] | Spoken interruptive command during execution [V] | **No**, it stops (cancel) and does not repair [V] | Sim only (LIBERO suites); no real-robot experiments found in text [V] | SA-MoE; action expert = Emu3-Base with FAST action tokenizer (autoregressive) [V] | https://github.com/bytedance/SALMONN/tree/ELLSA [V] | **Partial**: speech overlaps with acting, but cancel-and-stop, sim only. Interruptive-command success 96%/96%/89%/96% on SPATIAL/OBJECT/GOAL/LONG (Table 13) [V] |
| 6 | DREAM-Chunk: Reactive Action Chunking with Latent World Model | 2606.18589, 2026-06-17 [V] | Purdue University; Stanford University [V] | During execution, picks actions from whichever of N sampled candidate chunks has a latent prediction that best matches the observed rollout [V] | Observation vs. latent-world-model mismatch (stochastic dynamics, hardware error, perturbation) [V] | Yes, test-time reactive selection during long-horizon chunk execution [V] | Kinetix sim + real **SO-101** (3 tasks) and Franka (1 task) [V] | **SmolVLA fine-tuned on SO-101**; π0.5 on Franka; N = 10 candidates on SO-101 [V] | https://wenxichen2746.github.io/DREAM-Chunk/ [V] | **Partial (hardware/policy overlap)**: same arm + SmolVLA + in-flight chunk switching, but no language/speech trigger, and candidates share the original instruction |
| 7 | When to Switch: Reliable Action-Chunk Extension for VLAs (RACE) | 2610.05719, 2026-10-05 [V] | KAIST; GIST; NVIDIA; POSTECH [V] | Not a repair: predicts subskill-transition timing so longer chunks stay reliable [V] | None (internal one-step denoising pass) [V] | N/A; cuts stop-and-go idle time "by about 5x" [V] | Sim benchmarks (e.g., VLABench) + real AgileX PiPER 6-DoF arm [V] | π0.5; also GR00T-N1.6 [V]; which backbone ran on the real robot not confirmed [U] | https://github.com/Seonghoon-Yu/RACE-VLA [V] | **None**, apart from the "no stop-and-go" framing |
| 8 | ActionSplice: In-Flight Action Editing for Interactive World Models | 2609.08230, 2026-09-08 (v2 09-26) [V] | Texas A&M University [V] | Interrupted *video world-model* solver state; CST_T "preserves the temporal prefix at the intervention step and corrects only the suffix" [V] | Action-condition change during sampling [V] | Yes, mid-sampling, but of generated video, not robot motion [V] | Video WMs (minWM–Wan Action2V, HY-WM1.5); no robot [V] | Frozen world model + lightweight corrector [V] | https://pardistaghavi.github.io/actionsplice-website/ [V] | **Partial (conceptual analogue only)**: "in-flight" edit with prefix kept and suffix corrected; not robotics, not speech |
| 9 | SocialVLA: Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery | 2610.02360, 2026-10-01 [V] | Skolkovo Institute of Science and Technology (+MWS per alphaXiv [S]) [V] | Not repaired in-flight: a VLA **hold**, then participant-directed continuation, restart, or instruction revision for "a subsequent VLA action" [V] | Paralinguistic audio, facial reaction, explicit stop phrases, plus a separate speech channel (Vosk) [V] | **No**: "The robot remains paused until the participant explicitly requests continuation" [V] | Real Unitree G1 humanoid; 15 participants + prospective 16th [V] | GR00T policy + GR00T-WholeBodyControl [V] | None found in text [U] | **Partial**: speech/vocal-triggered interruption of a real VLA, but stop-first; VLA-gate-to-physical-hold 336 ms, reaction-onset-to-hold 1.021 s [V] |
| 10 | Premover: Fast VLA Control via Early Execution During Instruction Delivery | 2605.12160, 2026-05-12 (v2 2026-10-05) [V] | UNIST [V] | Starts executing on a streaming instruction prefix; "updates its action prediction as the streaming prefix grows" [V] | Streaming speech → online ASR transcript prefix (sim: XTTS-v2 + faster-whisper large-v3; real: "TTS-ASR streaming pipeline") [V] | Acts *while the user speaks*, but for an ambiguous prefix "the robot remains still and waits for the next word" [V]; no handling of a contradicting correction found [U] | Real **SO-101** + sim (LIBERO, VLA-Arena) [V] | Frozen **π0.5** on SO-101; π0.5 and GR00T-N1.7 in sim. SmolVLA is only cited, not evaluated [V] | No code URL found in text [V-negative] | **Strong-partial**: same arm, speech overlapping motion, chunked VLA. Not a repair of an in-flight chunk after a correction. SO-101: wall-clock 60.5 s → 49.7 s (−17.9%), success 86.0% vs 81.0% [V] |

### Part 1 findings (with refs)
- None of the ten papers does **speech-triggered repair of an in-flight chunk without stopping** [1–10]. Two split along the target claim:
  - Repair without speech: VLA-Feedback [1], React-When [2], DREAM-Chunk [6] all correct mid-chunk from *visual/observation* signals.
  - Speech without repair: MIRA [3], ELLSA [5], SocialVLA [9] all use speech/vocal barge-in to **stop / abort / hold**.
- The only papers on the **same hardware** (SO-101) are DREAM-Chunk [6] (SmolVLA, no language trigger) and Premover [10] (π0.5, speech overlaps with motion only for the *initial* instruction).
- ActionSplice [8] is the clearest *mechanistic* analogue: keep the prefix, correct the suffix when the conditioning changes mid-sampling. But it works on video world models, not robot policies.

---

## Part 2: additional alphaXiv sweep

### Exact queries run (`feynman alpha search --mode <mode> "<q>"`); 17 queries total
1. semantic: "speech interruption during robot manipulation, repairing the in-flight action chunk without stopping"
2. keyword: "barge-in VLA"
3. semantic: "instruction change during execution flow matching guidance action chunk inpainting new language"
4. semantic: "full-duplex vision-language-action model robot arm listens while acting"
5. semantic: "language correction mid-trajectory diffusion policy real-time steering"
6. keyword: "interruptible VLA"
7. semantic: "streaming ASR vision-language-action real-time spoken command robot"
8. keyword: "SO-101 speech"
9. semantic: "user changes their mind mid-motion, robot redirects to a new target object without retracting, VLA"
10. semantic: "real-time chunking language instruction switch mid-chunk VLA task switching"
11. keyword: "SwitchVLA task switching"
12. semantic: "low-cost robot arm voice correction while moving, LeRobot SmolVLA ACT"
13. semantic: "verbal correction while the robot arm is moving, VLA updates trajectory on the fly from spoken feedback"
14. keyword: "speech-conditioned VLA interruption"
15. semantic: "incremental speech understanding robot manipulation revise action when user's sentence continues or contradicts"
16. keyword: "in-flight action chunk"
17. semantic: "real-time chunking inpainting with changed language prompt, prefix-conditioned replanning toward a new goal"

Plus one `web_search` (exa) over 3 grey-literature queries on SO-101 / LeRobot voice interruption.

Keyword queries "barge-in VLA" and "interruptible VLA" returned only generic VLA-adaptation papers, with no barge-in/interruption manipulation work, so no exact-term collision. "SO-101 speech" returned a single hit (2606.08881), which is a benchmark with no speech component.

### Plausibly relevant hits (2026-06 onward, plus key earlier anchors)

| # | Paper | arXiv ID / date | One-line relevance | Closeness |
|---|---|---|---|---|
| 11 | Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies (UMD; USC) | 2609.30913, 2026-09-25 [V] | New *text* instruction issued "during or after" execution; training-free gradient "state-directed write" makes the frozen VLA decode a return motion to a demonstration-supported re-entry pose. Real xArm 6 + π0.5 (fine-tuned, frozen), "re-routing a held bowl from plate to shelf without put-down or re-grasp". LIBERO-Goal bare-switch 3–26% → 47–65% [V] | **Strong-partial** (closest) |
| 12 | Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams (ARMS; SJTU, CUHK, Nanjing U., Astribot, Juxi; CoRL 2026) | 2609.28429, 2026-09-23 [V] | π0.5 streaming dual-arm policy; "Interruptible: can switch to a newly arriving instruction mid-execution", and runs inserted action "on a free arm without halting the foreground". Combined task 45% vs 28% [V]. Speech not mentioned in text read [U] | Partial |
| 13 | EarlyCommit: Calibrated Word-by-Word Commitment for Robots Acting Before You Finish Speaking (U. Copenhagen) | 2610.20531, 2026-10-14 [V] | Word-by-word streaming-ASR object commitment. Self-stated: "There is no user study and no physical robot ... a commit is never revised" [V] | Partial (speech-incremental only; no motion, no repair) |
| 14 | Training-Free Action Correction for VLA Model Failures via Language Feedback (CorrectVLA; CMU) | 2608.29967, 2026-08-30 [V] | A single task-level language correction → additive action-magnitude adjustment, applied across rollouts; xArm7 [V] | Partial (language-triggered, but offline per-task, not mid-motion, not speech) |
| 15 | RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input (SJTU et al.) | 2610.10534, 2026-10-07 [V] | Traces, points, and coarse directional instructions → action drafts refined through DP/π0.5/FastWAM noise space [V] | Partial (steering mechanism; no speech; mid-motion not verified [U]) |
| 16 | Atomic Motion Coordinate for Language-Steerable and Force-Responsive Manipulation | 2609.15012, 2026-09-14 (v3 10-06) [V] | Language atoms injected into a π0.5-style action expert; contact history "regenerate[s] only the unexecuted horizon suffix" [V] | Partial (suffix regeneration is force-triggered; language steering is per-prompt, not speech overlap) |
| 17 | ReEnvision: Future-Guided Selective Action Repair (HKUST-GZ, Daimon, NJU) | 2610.17977, 2026-10-13 [V] | "selective repair of only the affected actions within a cached action chunk", driven by execution feedback [V] | Partial (in-chunk repair; no language/speech) |
| 18 | Predict in Chunks, Revise in Spans (CMAP) | 2610.14864, 2026-10-10 [V] | Uncertainty-guided span regeneration inside a chunk, keeping predictions outside the span [V] | Partial (mechanism only) |
| 19 | π R²: Reactive Real-time Flow Policies (CMU) | 2607.26055, 2026-07-28 [V] | Treats "in-flight actions as inpainting conditioning"; GR00T-N1.7 on xArm6+XHand, ~25 Hz [V] | Partial (mechanism; proprioception/vision trigger) |
| 20 | REACT: Rolling Denoising and Dual Decoupling (SJTU et al.; CoRL 2026 Spotlight) | 2610.12007, 2026-10-08 [V] | Persistent staggered-timestep action buffer refined with the latest observation [V] | Partial (mechanism; no language trigger) |
| 21 | Barrier-Constrained Guidance for Real-time Asynchronous VLA Execution (FreeBar; CoRL 2026) | 2610.14997, 2026-10-10 [V] | Training-free CBF-style consistency between consecutive chunks [V] | None–partial (chunk continuity only) |
| 22 | VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon (ZJU, DAMO) | 2607.01804, 2026-07-02 (date from alphaXiv listing [S]; ID not checked via arXiv API [U]) | Visual-deviation-triggered truncation + gradient-guided replanning; evaluated on π0.5, SmolVLA, X-VLA [S, from exa page text] | Partial (truncate-and-replan; visual trigger) |
| 23 | Acting While Understanding: Asynchronous Semantic-Action Decoupling | 2606.15285, 2026-06-13 [V] | Slow semantic conditions updated asynchronously while a fast action module keeps acting; π0.5/UniVLA [V] | Partial (architecture that could carry a new instruction mid-motion; not evaluated for that [U]) |
| 24 | CIRRA: Continual Instruction Reconciliation with Ongoing Execution (UGA, Northeastern, EmbodyX) | 2610.08862, 2026-10-05 [V] | LLM task-level schedule merge; interruptibility modes {immediate, safe point, uninterruptible}; `immediate` → active subtask "paused immediately and resumed"; Unitree G1 [V] | Partial (symbolic task level, pause-based) |
| 25 | Listen Before Act: ListenVLA | 2610.16313, 2026-10-12 [V] | Audio-conditioned GR00T N1.7 for *environmental* sounds (LIBERO-Audio) [V] | None–partial (audio is not user speech) |
| 26 | Benchmarking VLA Models on SO-101: Failure and Recovery Analysis (Hiroshima U.) | 2606.08881, 2026-06-07 [V] | π0.5, SmolVLA, Wall-X, ACT on SO-101 with recovery-aware metrics [V] | None (useful baseline citation) |
| 27 | DyaPlex: Full-Duplex Speech-Motion Model (NVIDIA, HKUST) | 2606.03874, 2026-06-02 [V] | Full-duplex speech + human motion generation; no robot manipulation [V] | None |
| 28 | DuplexSLA (StepFun et al.) | 2605.20755, 2026-05-20 (v2 06-11) [V] | Full-duplex speech + textual tool-call/action channel; interruption handled in backbone; no robot control found [V] | None–partial |
| 29 | SwitchVLA (BIHR), anchor/prior art | 2506.03574, 2025-06-04 [V] | Execution-aware task switching when "new instructions arrive during ongoing execution"; sim + real [V] | Partial (pre-window prior art; text instruction) |
| 30 | VITA-E (NJU, Tencent YouTu, …), anchor/prior art | 2510.21817, 2025-10-21 [V] | Active/Standby dual VLA; "emergency stops and speech interruptions" on a humanoid [V] | Partial (pre-window; stop/switch, humanoid) |

Grey literature (web, [S]):
- AY-Robots blog, "Voice Control for Robot Arms: Whisper in Front of a Policy". It explicitly advises: "If you want mid-episode interruption, implement it as a stop signal, not as a re-prompt" [S]. This documents current SO-arm practice as stop-based.
- Seeed Studio wiki: SO-ARM10x voice controller, wake word → Whisper → LLM → preset poses [S].
- NTU DR-NTU thesis "Interactive robotic arm manipulation through multimodal human feedback": SO-101 + SmolVLA. After a YOLO-detected failure, voice/text intent is classified as "restart" or "exit" [S]. This is post-failure and not mid-motion.
- GitHub a-yankovs/PatchWork (hackathon): SO-101 + ACT, failure detection then patch-and-retry [S].

---

## The 3 closest threats, and exactly what each does NOT do

1. **Causeway, 2609.30913 (2026-09-25)** [V]. Closest on *mid-execution instruction switching with redirect of a held object on a real arm*.
   - Trigger is not speech: it is a *text instruction switch* at fixed steps τ ∈ {30, 60, done}. Its text has no mention of speech/voice/audio (0 keyword hits).
   - Not learned: it is a "training-free inference-time intervention", a gradient write through the frozen decoder that needs per-architecture calibration.
   - It does not keep the in-flight chunk: it steers toward a "demonstration-supported re-entry pose" via a "return motion". That is close to the retract-to-re-entry pattern the target claim excludes, though the closed-gripper branch can re-route a held bowl without put-down.
   - Not a low-cost arm: it uses an xArm 6.
   - No SmolVLA or ACT: it uses π0.5, OpenVLA-OFT, and GR00T N1.5.
2. **Premover, 2605.12160 (v2 2026-10-05)** [V]. Closest on *hardware + speech overlapping motion*: SO-101, streaming ASR, chunked VLA, acting while the user speaks.
   - No correction of an in-flight chunk: the speech is the *initial* instruction still being delivered, and no new or contradicting utterance arrives mid-motion.
   - When the prefix is ambiguous it waits ("remains still and waits for the next word") instead of repairing.
   - Frozen π0.5, not SmolVLA/ACT. The backbone stays frozen; only a lightweight focus-map/readiness module is learned.
   - No code URL found.
3. **SocialVLA, 2610.02360 (2026-10-01)** [V]. Closest on *real-world speech/vocal-triggered interruption of a running VLA, followed by verbal instruction revision*.
   - It is stop-first: hold latency 336 ms; "The robot remains paused until the participant explicitly requests continuation".
   - The revised instruction applies only to "a subsequent VLA action", so there is no in-flight chunk repair.
   - No learned motion repair: policy retraining is stated to be "outside the scope of this work".
   - Not a low-cost arm: Unitree G1 humanoid with a GR00T policy.

Runners-up:
- DREAM-Chunk 2606.18589: SO-101 + SmolVLA in-flight chunk switching, but **no language/speech trigger**.
- ELLSA 2510.16756: speech "action barge-in" that **stops** the action, sim only (LIBERO).
- ARMS 2609.28429: real-robot mid-execution instruction switching via a *free second arm*, dual-arm π0.5. Speech not shown [U].

**Bottom line (inference):** as of 2026-10-18, I found no paper in the alphaXiv index or arXiv records checked that combines all four elements:
- (a) a learned repair of the in-flight chunk,
- (b) triggered by overlapping user speech,
- (c) with no stop/hold/retract,
- (d) on a low-cost arm.

Each element appears in some paper, but no paper has all four together. The density of Sept–Oct 2026 work (Causeway, ARMS, SocialVLA, Premover v2, EarlyCommit) means scoop risk is **elevated and rising**.

---

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|---|---|---|---|---|
| 1 | VLA-Feedback (2609.21022) | https://arxiv.org/abs/2609.21022 | Final denoising step kept as visual feedback interface; GR00T; Franka | primary | high |
| 2 | React When You Need To (2609.22587) | https://arxiv.org/abs/2609.22587 | Event-triggered early inference + chunk blending; π0.5 LoRA; Franka | primary | high |
| 3 | MIRA (2609.24547) | https://arxiv.org/abs/2609.24547 | VAD barge-in → abort; 466 ms; Astribot S1 | primary | high |
| 4 | ELLSA 2 (2610.21452) | https://arxiv.org/abs/2610.21452 | Gestures/expressions; no manipulation | primary | high |
| 5 | ELLSA (2510.16756) | https://arxiv.org/abs/2510.16756 | Action barge-in = "Action Cancelled" + stop; LIBERO | primary | high |
| 6 | DREAM-Chunk (2606.18589) | https://arxiv.org/abs/2606.18589 | SmolVLA on SO-101; candidate-chunk selection via latent WM | primary | high |
| 7 | RACE (2610.05719) | https://arxiv.org/abs/2610.05719 | Chunk extension; PiPER; ~5x idle reduction | primary | high |
| 8 | ActionSplice (2609.08230) | https://arxiv.org/abs/2609.08230 | Prefix-preserving suffix correction in video WMs | primary | high |
| 9 | SocialVLA (2610.02360) | https://arxiv.org/abs/2610.02360 | Hold then participant-directed revision; G1; GR00T | primary | high |
| 10 | Premover (2605.12160) | https://arxiv.org/abs/2605.12160 | SO-101 + π0.5 + streaming ASR; acts during instruction delivery | primary | high |
| 11 | Causeway (2609.30913) | https://arxiv.org/abs/2609.30913 | Training-free mid-execution instruction switching; xArm 6; π0.5 | primary | high |
| 12 | ARMS (2609.28429) | https://arxiv.org/abs/2609.28429 | Interruptible + concurrent dual-arm π0.5 | primary | medium (modality [U]) |
| 13 | EarlyCommit (2610.20531) | https://arxiv.org/abs/2610.20531 | Word-by-word commitment; no physical robot; commit never revised | primary | high |
| 14 | CorrectVLA (2608.29967) | https://arxiv.org/abs/2608.29967 | Task-level language correction → action magnitude offsets | primary (abstract) | medium |
| 15 | RoboPrompt (2610.10534) | https://arxiv.org/abs/2610.10534 | Sparse-input noise-space steering | primary (abstract) | medium |
| 16 | Atomic Motion Coordinate (2609.15012) | https://arxiv.org/abs/2609.15012 | Language atoms; suffix-only regeneration on contact | primary (abstract + alpha report) | medium |
| 17 | ReEnvision (2610.17977) | https://arxiv.org/abs/2610.17977 | Selective repair inside cached chunk | primary (abstract) | medium |
| 18 | CMAP (2610.14864) | https://arxiv.org/abs/2610.14864 | Span regeneration inside chunk | primary (abstract) | medium |
| 19 | π R² (2607.26055) | https://arxiv.org/abs/2607.26055 | In-flight actions as inpainting conditioning | primary (abstract) | medium |
| 20 | REACT (2610.12007) | https://arxiv.org/abs/2610.12007 | Rolling denoising buffer | primary (abstract) | medium |
| 21 | FreeBar (2610.14997) | https://arxiv.org/abs/2610.14997 | Barrier-guided chunk consistency | primary (abstract) | medium |
| 22 | VLA-Corrector (2607.01804) | https://www.alphaxiv.org/abs/2607.01804 | Visual-trigger truncate + replan; SmolVLA evaluated | secondary (search page text) | low–medium |
| 23 | Acting While Understanding (2606.15285) | https://arxiv.org/abs/2606.15285 | Async semantic/action decoupling | primary (abstract) | medium |
| 24 | CIRRA (2610.08862) | https://arxiv.org/abs/2610.08862 | Interruptibility modes; pause-resume; G1 | primary | high |
| 25 | ListenVLA (2610.16313) | https://arxiv.org/abs/2610.16313 | Environmental-audio-conditioned GR00T | primary (abstract) | medium |
| 26 | SO-101 VLA benchmark (2606.08881) | https://arxiv.org/abs/2606.08881 | π0.5/SmolVLA/Wall-X/ACT on SO-101 | primary (abstract) | medium |
| 27 | DyaPlex (2606.03874) | https://arxiv.org/abs/2606.03874 | Full-duplex speech-motion; no robot | primary (abstract) | medium |
| 28 | DuplexSLA (2605.20755) | https://arxiv.org/abs/2605.20755 | Full-duplex speech + action/tool channel | primary (abstract) | medium |
| 29 | SwitchVLA (2506.03574) | https://arxiv.org/abs/2506.03574 | Mid-execution task switching (prior art) | primary (abstract) | medium |
| 30 | VITA-E (2510.21817) | https://arxiv.org/abs/2510.21817 | Speech interruptions/emergency stop, humanoid (prior art) | primary (abstract) | medium |
| 31 | AY-Robots blog | https://www.ay-robots.com/blog/en/voice-and-natural-language-control-for-arms | Recommends stop-signal, not re-prompt, for mid-episode interruption | secondary | low |
| 32 | NTU thesis (DR-NTU) | https://hdl.handle.net/10356/215147 | SO-101 + SmolVLA; post-failure voice restart/exit | secondary (snippet) | low |
| 33 | Seeed Studio wiki | https://wiki.seeedstudio.com/respeaker_flex_soarm/ | SO-ARM voice controller with preset poses | secondary | low |
| 34 | PatchWork repo | https://github.com/a-yankovs/tinyVLA-debugger | SO-101 + ACT failure-patch-retry (hackathon) | secondary | low |

## Sources
1. Ji, Zhou, Sentis, Seo — Catch Me If You Can (VLA-Feedback) — https://arxiv.org/abs/2609.21022
2. Wu, Li, Hou, Chen, Knoll — React When You Need To — https://arxiv.org/abs/2609.22587
3. Lin et al. — MIRA — https://arxiv.org/abs/2609.24547
4. Wang et al. — ELLSA 2: Full-Duplex Interaction with Speech, Expressions and Gestures — https://arxiv.org/abs/2610.21452
5. Wang et al. — End-to-end Listen, Look, Speak and Act (ELLSA) — https://arxiv.org/abs/2510.16756
6. Chen et al. — DREAM-Chunk — https://arxiv.org/abs/2606.18589
7. Yu et al. — When to Switch (RACE) — https://arxiv.org/abs/2610.05719
8. Taghavi et al. — ActionSplice — https://arxiv.org/abs/2609.08230
9. Konstantinova et al. — SocialVLA — https://arxiv.org/abs/2610.02360
10. Park, Jeong, Gong — Premover — https://arxiv.org/abs/2605.12160
11. Wang et al. (Manocha) — Causeway — https://arxiv.org/abs/2609.30913
12. Yi et al. — Watch, Recall, Act (ARMS) — https://arxiv.org/abs/2609.28429
13. Khan — EarlyCommit — https://arxiv.org/abs/2610.20531
14. Kwon et al. — CorrectVLA — https://arxiv.org/abs/2608.29967
15. Zou et al. — RoboPrompt — https://arxiv.org/abs/2610.10534
16. Zhai et al. — Atomic Motion Coordinate — https://arxiv.org/abs/2609.15012
17. Zeng et al. — ReEnvision — https://arxiv.org/abs/2610.17977
18. Wang et al. — Predict in Chunks, Revise in Spans (CMAP) — https://arxiv.org/abs/2610.14864
19. Park, Tulsiani — π R² — https://arxiv.org/abs/2607.26055
20. Xiong et al. — REACT — https://arxiv.org/abs/2610.12007
21. Yu et al. — FreeBar — https://arxiv.org/abs/2610.14997
22. VLA-Corrector (ZJU/DAMO) — https://www.alphaxiv.org/abs/2607.01804 (code per page text: https://github.com/ZJU-OmniAI/vla-corrector [S])
23. Yan et al. — Acting While Understanding — https://arxiv.org/abs/2606.15285
24. Zhang et al. — CIRRA — https://arxiv.org/abs/2610.08862
25. Fan et al. — ListenVLA — https://arxiv.org/abs/2610.16313
26. Yu, Qiu — Benchmarking VLA Models on SO-101 — https://arxiv.org/abs/2606.08881
27. Nagano et al. — DyaPlex — https://arxiv.org/abs/2606.03874
28. Zhang et al. — DuplexSLA — https://arxiv.org/abs/2605.20755
29. Li et al. — SwitchVLA — https://arxiv.org/abs/2506.03574
30. Liu et al. — VITA-E — https://arxiv.org/abs/2510.21817
31. AY-Robots — Voice Control for Robot Arms — https://www.ay-robots.com/blog/en/voice-and-natural-language-control-for-arms
32. NTU DR-NTU — Interactive robotic arm manipulation through multimodal human feedback — https://hdl.handle.net/10356/215147
33. Seeed Studio — reSpeaker + SO-ARM10x voice — https://wiki.seeedstudio.com/respeaker_flex_soarm/
34. a-yankovs — PatchWork — https://github.com/a-yankovs/tinyVLA-debugger

## Blocked sources
- None encountered. No robots.txt, paywall, or login blocks were hit. The anonymous ListenVLA code link (anonymous.4open.science) was not fetched.

## Coverage Status
- **Part 1: done.** All 10 IDs were confirmed via the arXiv API. Full text was pulled for all 10 via `feynman alpha ask`, which returned paper text rather than a model answer. Fields were extracted by keyword search of that text.
- **Part 2: done.** 17 alphaXiv queries were run (≥8 required), mixing semantic and keyword modes, plus one 3-query web sweep. Full text was read for Causeway, ARMS, EarlyCommit, CIRRA, and Atomic Motion Coordinate (alpha report). Everything else is from arXiv abstracts only.
- **Uncertain / needs follow-up:**
  - RACE: which backbone ran on the real PiPER.
  - ARMS: whether interruptions are spoken or text.
  - Premover: behavior when a later word contradicts an already-executing prefix. Not found in the text read. Appendix truncation possible.
  - SocialVLA and Premover: code availability.
  - VLA-Corrector 2607.01804: ID/date not confirmed via the arXiv API.
  - RoboPrompt: whether steering is applied mid-motion.
- **Not checked:**
  - Non-arXiv venues (CoRL/IROS/ICRA 2026 proceedings, OpenReview) beyond what arXiv mirrors.
  - Chinese-language preprints.
  - Industry demos (e.g., Physical Intelligence or Figure blogs) of verbal mid-motion corrections.
