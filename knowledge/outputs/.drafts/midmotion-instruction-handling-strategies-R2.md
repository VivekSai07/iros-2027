# Mid-motion instruction handling — six systems (R2)

Date: 2026-10-18. Tags: [V] I read it in the primary text (alphaXiv full text from `feynman alpha get`, or the official page); [S] secondary; [U] my inference or unverified. Numbers are quoted as the sources state them.

## Summary table

| System | (a) Trigger → model input | (b) Physical act at interruption | (c) Repair | (d) Latency (as stated) | (e) Backbone / head | (f) Real / sim | (g) Human study | (h) Code / weights |
|---|---|---|---|---|---|---|---|---|
| Causeway [1] | Text instruction ℓB swapped in during or after task A [V] | Switch immediately. A gradient "write" in the action stream steers the robot to a re-entry pose [V] | Engagement → return → dwell → handoff back to the frozen VLA [V] | Per-chunk 102/75/128 → 253/187/362 ms on A100-80GB [V] | π0.5, OpenVLA-OFT, GR00T N1.5 (frozen) [V] | LIBERO-Goal/Object; real xArm 6 [V] | None [V] | No link in paper [V] |
| Premover [2] | TTS speech → faster-whisper streaming ASR → text prefix tokens [V] | Starts moving early. Uses the shared action prefix while later words are still arriving [V] | Replans every chunk as the prefix grows. Does **not** handle corrections [V] | Heads add 0.232 ms over a 65.84 ms forward; wall-clock 60.5 → 49.7 s [V] | Frozen π0.5 / GR00T-N1.7 + 2.36M-param heads [V] | SO-101 (π0.5); LIBERO, VLA-Arena [V] | None (WPM rate taken from prior data) [V] | No link found [V] |
| RIAP [3] | Partial speech (abstract-level only) [V-abstract] | ACT / WAIT / DEFER decision [V-abstract] | "corrected for 60.6% of mid-utterance human revisions" [V-abstract] | "anticipated user commands by an average of 1,022 ms" [V-abstract] | Unknown | "8,160 simulation replays" [V-abstract] | N=30, subjective UX [V-abstract] | Unknown |
| EarlyCommit [4] | Speech (TTS/recording) → faster-whisper small.en → words → text classifier [V] | Commits to an object once calibrated p ≥ τ, then reaches. "A commit is final" [V] | None. Asks "which one" if nothing commits by the last word [V] | 31–35 ms/word median, 38–41 ms p95 on RTX 3060 laptop / Colab T4 [V] | Laya, a 421M-param ModernBERT-large classifier (no action policy) [V] | Kinematic 2-link arm demo only; "no physical robot" [V] | None [V] | Anonymised supplementary material, Apache 2.0; no public URL [V] |
| SocialVLA [5] | Live human reactions: paralinguistic audio (wav2vec2 emotion logits + ExtraTrees), face/video, Vosk stop phrases [V] | **Hold**. One pause command to the running VLA [V] | Post-hold Vosk transcript of the correction is logged. A human then resumes, restarts or revises the instruction [V] | Detector→fusion 47.9 ms median; gate→physical hold 336 ms; reaction onset→hold 1.021 s [V] | GR00T policy on Unitree G1 (external gateway, policy-agnostic) [V] | Real Unitree G1 [V] | 15 participants + 1 prospective [V] | No link in paper [V] |
| MIRA [6] | Live speech: Silero VAD fast gate + streaming ASR → LLM arbiter [V] | **Stop/cancel** after the committed 0.50 s prefix. Abort fires on 450 ms of sustained speech [V] | IGNORE → continue the interrupted response from saved context; INTERRUPT_AND_REPLY → new response [V] | speech_started→abort_cmd_sent 466 ms (P50) [V] | ROSCO DiT (d=256, 8 blocks) co-speech motion; LLM unnamed [V] | Real Astribot S1 humanoid (gestures, not manipulation) [V] | No formal study; production trace of 199 sessions / 559 decisions [V] | Homepage only, no code link [V] |

---

## 1. Causeway (arXiv 2609.30913) [1]

- **(a)** A text instruction switch: the policy "begins task A and permanently receives instruction ℓB at an intermediate or terminal state" [V].
- **(b)** The switch takes effect immediately. A bare switch often fails: success "collapses as the robot approaches the object… due to policy stalling or continuing toward the source object" [V]. Causeway's write "starts at the instruction switch. If the hand holds oA ≠ oB, only the gripper channel is active until the hand opens…; otherwise, the position and orientation channels engage immediately" [V]. So the robot releases or retracts toward a re-entry pose, and the frozen VLA decodes every action.
- **Three switch timings:**
  - Sim: "step 30 (approach), step 60 (object held in 58–61% of trials), or post-completion" [V].
  - Real: "mid-approach, at pre-grasp, or post-completion (5 trials/cell)" [V].
- **(c) Repair:** the method backpropagates through the frozen decoder toward a demonstration-derived re-entry pose T*. Thresholds are γ = 0.3 rad, Nγ = 20, Nd = 15 steps. The write disengages after the dwell, or once the gripper closes on a grasp inside the neighborhood. It "issues no motor commands" [V].
- **Results:**
  - Sim: bare-switch success "3–26% to 47–65%" over 71 pairs × 3 timings × 3 VLAs [V].
  - Real xArm 6, pooled bare → ours: "42.9 100 / 14.3 94.3 / 17.1 82.9" (approach / pre-grasp / after A) [V].
- **(d) Latency:** "On one A100-80GB, per-chunk latency rises 2.5–2.8× (102/75/128 → 253/187/362 ms; replanning 4.0/5.3/2.8 Hz; +≤4.3 GiB peak) on OFT/π0.5/GR00T, active only during re-entry" [V].
- **(e) Backbones:** π0.5, OpenVLA-OFT and GR00T N1.5. The real robot uses π0.5 "fine-tuned on 30 teleoperated demonstrations per task and frozen" [V]. Parameter counts are not stated in the text I read.
- **(g)** No human study [V].
- **(h)** No code or weights link found in the paper [V].
- **(i)** A100-80GB [V]. It needs a backward pass through the decoder (+≤4.3 GiB). With π0.5 it plausibly needs the 48 GB card. With SmolVLA (450M), 8 GB is plausible [U].
- **(j) Applicability [U]:**
  - The idea of a state-directed gradient on the action-stream representation is backbone-agnostic in principle, but needs per-architecture calibration (stated limitation) [V].
  - SmolVLA's flow-matching action expert is analogous to π0.5's.
  - ACT (CVAE decoder) would need its own definition of the "write" location.
  - Demo-derived re-entry poses are portable.
- **(k) Key claim:** a training-free, inference-time fix makes a new instruction reachable from "task islands". **Caveat:** it "depends on task-relative coordinates (ξ) and demonstration coverage… requiring per-architecture calibration" [V].

## 2. Premover (arXiv 2605.12160) [2]

- **(a)** "TTS-generated speech with ASR transcripts". The stack is XTTS-v2 + faster-whisper large-v3 (sim replay), and faster-whisper v1.2.1 streaming on the robot [V]. The text prefix goes into a frozen VLA. Speech is synthetic TTS, not live humans [V].
- **(b)** Premover starts moving early, before the instruction finishes. Once the readiness gate fires, "the robot begins acting from the default action chunk A(0) before the complete instruction arrives" [V]. If later actions depend on missing words, it uses "consensus-guided execution… executes only the initial actions shared across these chunks" [V].
- **(c) Repair:** it replans per chunk with the latest prefix. It explicitly does **not** handle corrections: "We do not consider corrections or changes to previously specified targets or destinations after execution has begun" [V].
- **(d) Latency:**
  - The projection heads "added 0.232 ms per inference step on LIBERO over an average backbone forward time of 65.84 ms" [V].
  - SO-101 wall-clock "60.5 to 49.7 s" (−17.9%) on single-object tasks. Success is 86.0% vs 81.0% for Full-prompt, over 20 trials per task and method [V].
  - Disambiguation tasks: "88.2 to 76.7 s", score 71.7% vs 57.5% [V].
  - LIBERO at speaking rate: "8.17 to 7.49 seconds" [V].
- **(e) Backbone:** frozen π0.5 and GR00T-N1.7. The heads hold "2.36M parameters in total". Resume horizons are T_resume = 6 for π0.5 and 10 for GR00T [V].
- **(f)** Real SO-101 with π0.5, 50 teleop demos per task. Sim: LIBERO and VLA-Arena [V].
- **(g)** No user study [V].
- **(h)** No code URL in the text [V].
- **(i)** Training and evaluation ran on "8 NVIDIA H200 GPUs with 141 GB"; each set of heads was trained on one GPU [V]. π0.5 inference on 8 GB is tight or unlikely. On 48 GB it is fine [U].
- **(j) Applicability [U]:** this is the most directly relevant work, since it uses the same robot (SO-101). The readiness gate and focus map are trained on backbone features, so moving to SmolVLA means retraining the heads on SmolVLA's VLM features. ACT has no language input, so it does not apply.
- **(k) Key claim:** overlapping speech delivery with execution cuts wall-clock time without losing success. **Caveat:** the intended task is assumed fixed, and speech is TTS rather than live human.

## 3. RIAP — NeurIPS 2026 poster 162424 [3] (abstract-level only)

The full title is "Risk-Aware Incremental Action Policy for Physical Commitment from Partial Speech" [V]. I re-searched alphaXiv (by title) and Semantic Scholar once each. I found no arXiv or full text. Semantic Scholar was rate-limited (429) and returned 0 hits.

From the abstract [V]:
- It "decouples these decisions by weighing real-time intent confidence against action- and state-dependent safety costs". It picks between "ACT, WAIT, or DEFER".
- "Through 8,160 simulation replays, RIAP cut unsafe commitments from 27.5% to 1.6%, anticipated user commands by an average of 1,022 ms, and corrected for 60.6% of mid-utterance human revisions".
- "A 30-participant study… superior perceived user experience".

Backbone, robot, latency hardware, code and GPU are all unknown. Fields (b)(c)(e)(h)(i) are **not verifiable**. **Applicability [U]:** the ACT/WAIT/DEFER gate sits above the policy and is likely policy-agnostic. Unlike Premover and EarlyCommit, it is the one system here that claims to handle revisions mid-utterance.

## 4. EarlyCommit (arXiv 2610.20531) [4]

- **(a)** Speech (TTS or a recorded file "streamed as if live") → faster-whisper small.en, which "re-transcribes the audio received so far every 0.3 s". A word is "released only when two consecutive transcripts agree" (LocalAgreement) [V]. The judge is a text model. The main evaluation feeds text directly, "without speech recognition" [V].
- **(b)** It commits word by word: "commits to arg max… at the first t ≥ 2 with max p̃ ≥ τ… A commit is final. If the instruction ends without a commit the robot asks which object is meant" [V]. A commit returns an object ID and position to the caller's grasp controller [V].
- **(c)** No repair. "a commit is never revised" [V].
- **(d) Latency:** "31–35 ms per word at the median and 38–41 ms at the 95th percentile" on a laptop RTX 3060 and a Colab T4 [V].
- **Accuracy:** at τ = 0.9 it "is right at least 92% of the time when it commits". Its commits "save 0.79–1.06 s per instruction", with time saved computed at 0.3 s per word [V].
- **(e)** Laya, a "421M-parameter text classifier built on the ModernBERT-large encoder", with temperature calibration (T = 5.29 shown in Fig. 1). It produces no actions [V].
- **(f)/(g)** "no user study and no physical robot". There is a kinematic 2-link demo [V].
- **(h)** "Code, result files and demo videos are provided as anonymised supplementary material… released under Apache 2.0" [V]. I found no public URL, so I did not check a repo. The paper cites a Laya model card at huggingface.co/convaiinnovations/laya [S, not opened].
- **(i)** Fine-tuned on one A100; inference was shown on RTX 3060 laptop / T4 [V]. It fits 8 GB [U, strongly supported].
- **(j) Applicability [U]:** fully policy-agnostic, as an object-selection front end. For SmolVLA, its output could be turned into a templated instruction. ACT has no language input, so it would need a per-object policy or a goal-conditioned variant.
- **(k) Key claim:** calibrated early commitment beats keyword matching on unseen words, at 1.6 to 2 times as many correct commits. **Caveat:** templated vocabulary, no robot, irreversible commits.

## 5. SocialVLA (arXiv 2610.02360) [5]

- **(a)** Live human reactions (participants), entering through three channels [V]:
  - paralinguistic audio: Aniemore wav2vec2 emotion logits over causal 320-ms windows, fed to ExtraTrees fast (≤0.4 s) and context (≤2.0 s) heads;
  - visual reaction recognition plus a robot-relevance head;
  - Vosk lexical stop phrases.
  The fusion is "asynchronous first-event": the first authorized event triggers [V].
- **(b) Hold:** "the gasp-vla-gate sends one pause command to the running VLA and places it in a hold state… The robot remains paused until the participant explicitly requests continuation" [V].
- **(c) Repair:** "a separate Vosk logging session records unrestricted verbal correction… it cannot resume the robot, clear the hold state, or issue motion commands". The participant may "resume execution from the held state, adjust the workspace and restart the action, or provide a revised instruction" [V]. Each correction is stored with the active VLA action or chunk for later data curation. Retraining is out of scope [V].
- **(d) Latency (Table II, live):**
  - Detector→fusion 0.048 s median (n = 22).
  - Fusion→gate 0.001 s.
  - "VLA gate → physical hold (n = 24) 0.336 0.681 1.559".
  - "Reaction onset → physical hold (n = 14) 1.021 1.569 1.576".
  "most end-to-end delay occurs before detector emission and during physical robot deceleration" [V].
- **Detection:** offline recall 54.6% / precision 69.5%. In the prospective run on a 16th participant, recall was 59.5% and precision 91.7% [V].
- **(e)** "physical Unitree G1 humanoid controlled by GR00T-WholeBodyControl and a GR00T policy trained for a pick-and-place task" [V].
- **(g)** 15 participants: 238 intervention-worthy episodes and 1.038 h of non-intervention behavior, plus 1 prospective participant [V].
- **(h)** No code link in the paper [V].
- **(i)** GPU not stated [V]. The perception stack (wav2vec2 + trees + Vosk) is likely under 8 GB [U].
- **(j) Applicability [U]:** it is explicitly "policy-agnostic". It needs only a pause/hold interface, which SmolVLA and ACT on SO-101 can expose via LeRobot's control loop. It could be dropped in directly.
- **(k) Key claim:** human reactions become a sub-second-transport hold signal. **Caveat:** reaction onset to hold is about 1 s, recall is around 55–60%, and the system "is not a certified safety system".

## 6. MIRA (arXiv 2609.24547) [6]

- **(a)** Live user speech. A Silero VAD "Fast Interruption Gate" sends audio incrementally to ASR; the provider is not named. Once ASR finalizes, the Deliberative Turn Arbiter runs: rules plus a "non-streaming language-model query" using transcript, vocal affect and dialogue history [V].
- **(b) Stop/cancel:** "If the segment reaches the configured 450 ms interruption-confirmation threshold while playback is active… it marks the current response as aborted, clears pending TTS output, sends a TTS-stop control message, and terminates the ongoing robot motion" [V]. Under RHPC, "only 15 frames (0.50 s) are committed at a time… the active motion session can be terminated after the currently committed segment" [V]. Physical preemption does not wait for the arbiter [V].
- **(c) Repair, by arbiter decision ∈ {IGNORE, REPLY, INTERRUPT_AND_REPLY}:**
  - **IGNORE after an early abort:** "the controller can use the saved assistant context to generate a continuation of the previous response". In Case A, a bystander false alarm was followed by a seamless continuation [V].
  - **INTERRUPT_AND_REPLY:** generates a replacement response [V].
- **(d) Latency (P50, Table 3):**
  - "speech_started → abort_cmd_sent 466 ms".
  - ASR endpointing 10.0 ms; LLM TTFT 1.62 s.
  - ROSCO chunk 195 ms (RTF 0.390).
  - First motion 2.36 s [V].
  - Hardware for these numbers is not stated in the text I read [V].
- **(e) Motion model:** ROSCO is a prefix-conditioned DiT (d = 256, eight blocks, four heads, DDPM). It predicts a 50-frame window, commits 15 frames, and uses a 10-frame prefix, at 30 fps [V]. The LLM, TTS and ASR models are not named in the sections I read [V].
- **(f)** Real Astribot S1 humanoid, co-speech gestures and social behaviors. No object manipulation [V].
- **(g)** No formal user study. There is a production trace: 199 sessions, 559 decisions (302 REPLY / 88 INTERRUPT_AND_REPLY / 169 IGNORE) [V].
- **(h)** The homepage gagajian.github.io/MIRA has no code or weights link [V].
- **(i)** GPU not stated. ROSCO is small and likely under 8 GB; the LLM is presumably remote or separate [U].
- **(j) Applicability [U]:** fully policy-agnostic, since it is an orchestration layer:
  - the fast VAD gate;
  - the arbiter's three-way decision;
  - the "bounded commitment" idea.
  The bounded-commitment idea maps directly onto SmolVLA/ACT chunking: cap the executed chunk prefix (e.g., `n_action_steps`) so an abort loses ≤0.5 s. The co-speech motion model itself is irrelevant to manipulation.
- **(k) Key claim:** a dual-timescale design stops fast via VAD and decides slowly via the LLM, with a bounded 0.5 s motion commitment. **Caveat:** gestures, not manipulation, and the 466 ms is measured to command dispatch, not to physical stop.

## Cross-system observations [U unless cited]

- **The interruption response falls on a spectrum:**
  - hold/stop: SocialVLA [5], MIRA [6];
  - immediate switch with steered re-entry: Causeway [1];
  - early start on a prefix: Premover [2], EarlyCommit [4], RIAP [3].
  Only RIAP (abstract) and Causeway (instruction switch) address **revision after motion starts**. Premover and EarlyCommit explicitly exclude it [2][4].
- **Latency is measured to different endpoints, so the numbers are not comparable:**
  - MIRA: to abort dispatch.
  - SocialVLA: to physical hold, including deceleration.
  - Causeway: per-chunk compute.
- **For SO-101 + SmolVLA/ACT, the cheapest policy-agnostic pieces** are a SocialVLA/MIRA-style hold gate, MIRA's bounded chunk commitment, and an EarlyCommit-style calibrated text gate. Premover-style readiness heads and Causeway's gradient write need backbone-specific work.

## Coverage status
- **Done, full text read via alphaXiv:** Causeway, Premover, EarlyCommit, SocialVLA, MIRA.
- **Abstract only:** RIAP, after one alpha search and one S2 search, plus a web search.
- **Not found** in the text I read: parameter counts for Causeway's backbones, MIRA's GPU/LLM, SocialVLA's GPU.
- **alpha code (read_code):** not run. None of the six papers gives a GitHub URL for its own code (MIRA's only GitHub link is to silero-vad).

## Blocked sources
- RIAP full text: none publicly located; the NeurIPS virtual page shows the abstract only.
- EarlyCommit code: anonymised supplement, no public URL.
- (ELLSA bytedance/SALMONN is known ROBOTS_DISALLOWED; not relevant here and not retried.)

## Sources
1. Wang et al., "Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies," arXiv 2609.30913 — https://arxiv.org/abs/2609.30913
2. Park, Jeong, Gong, "Premover: Fast VLA Control via Early Execution During Instruction Delivery," arXiv 2605.12160 — https://arxiv.org/abs/2605.12160
3. "Risk-Aware Incremental Action Policy for Physical Commitment from Partial Speech" (RIAP), NeurIPS 2026 poster — https://neurips.cc/virtual/2026/poster/162424
4. Khan, "EarlyCommit: Calibrated Word-by-Word Commitment for Robots Acting Before You Finish Speaking," arXiv 2610.20531 — https://arxiv.org/abs/2610.20531
5. Konstantinova et al., "SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation," arXiv 2610.02360 — https://arxiv.org/abs/2610.02360
6. Lin et al., "MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions," arXiv 2609.24547 — https://arxiv.org/abs/2609.24547 ; homepage https://gagajian.github.io/MIRA/
