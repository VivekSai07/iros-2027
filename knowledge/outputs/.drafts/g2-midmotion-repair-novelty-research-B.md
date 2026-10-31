# G2 — Mid-motion repair upon a new instruction: novelty check (research-B)

Date: 2026-10-18. Researcher subagent. Scope: 10 assigned papers only.

**Question:** Does any method *repair an in-flight motion / action chunk* of a VLA/ACT/flow/diffusion policy when a NEW language or speech instruction arrives *while the arm is moving*, without stop-and-retract?

**Tags:** [V] = verified from primary full text (pulled via `feynman alpha get --full-text <id>`, i.e. the alphaXiv extracted paper text); [S] = secondary (project page or other paper describing it); [U] = unverified / not stated / inferred.
All 10 arXiv IDs were confirmed through the arXiv API (`feynman_science_database_search`, `arxiv_get_papers`): titles, dates and authors match. So every ID below is [V].

## Blocked sources
- None. No source was blocked by robots.txt, a paywall or a login. Note: the Hi Robot page (pi.website) and the SwitchVLA, TempoBridge and CorrectVLA project pages had no code links in their static HTML. That means code is absent from the page, not that access was blocked.

---

## Evidence table

| # | Source | URL | Key claim (for this question) | Type | Confidence |
|---|---|---|---|---|---|
| 1 | SwitchVLA (2506.03574) | https://arxiv.org/abs/2506.03574 | Switching happens mid-execution and is learned. It uses forward/rollback/advance modes and is applied at chunk granularity. "Advance" interpolates in joint space toward the new task's canonical start pose. Text only | primary | high |
| 2 | VITA-E (2510.21817) | https://arxiv.org/abs/2510.21817 | Speech-triggered action switching preempts the active model. The robot then **retracts to initial pose** by replaying inverse actions | primary | high |
| 3 | Hi Robot (2502.19417) | https://arxiv.org/abs/2502.19417 | Spoken interjection (Whisper ASR) immediately re-triggers the high-level VLM. The low-level π0 receives a new command. Handling of the in-flight chunk is not described | primary | high |
| 4 | One Word, Different Action (2609.05260) | https://arxiv.org/abs/2609.05260 | Static text-LLM decision benchmark on fixed physical anchors. No execution-time switching | primary | high |
| 5 | Causeway (2609.30913) | https://arxiv.org/abs/2609.30913 | Training-free representation write that makes the frozen VLA decode a return motion to a task-B re-entry pose. Real xArm6 and π0.5. Switches at approach, pre-grasp, and post-completion | primary | high |
| 6 | CIRRA (2610.08862) | https://arxiv.org/abs/2610.08862 | LLM plan reconciliation. Interruption happens only at skill-level boundaries set by an interruptibility mode (immediate / safe point / uninterruptible). Paused skill goes to standby | primary | high |
| 7 | Watch, Recall, Act / ARMS (2609.28429) | https://arxiv.org/abs/2609.28429 | New demands run concurrently on a *free arm* instead of switching. A "hard interrupt" ablation is worse | primary | high |
| 8 | TempoBridge (2610.09451) | https://arxiv.org/abs/2610.09451 | Tempo cue is read "once per instruction" at episode start. The phase router switches FAST/SLOW inside one fixed instruction. No new instruction mid-run | primary | high |
| 9 | CorrectVLA (2608.29967) | https://arxiv.org/abs/2608.29967 | Correction is given after observing the complete rollout and reused across re-executions. Not online | primary | high |
| 10 | RoboPrompt (2610.10534) | https://arxiv.org/abs/2610.10534 | Sparse sketch/point/coarse-direction prompts are issued during execution. They are blended across replanning chunks via progressive biased denoising (PBD) and noise-augmented flow reversal steering (NA-FRS). No speech; not task switching | primary | high |
| 11 | VITA-E code (from homepage) | https://github.com/Tencent/VITA/tree/VITA-E | Code branch linked from the project homepage; HTTP 200 | primary (repo) | medium |
| 12 | RoboPrompt code (from website) | https://github.com/yanwen-zou/Roboprompt | Repo linked from the project website; HTTP 200 | primary (repo) | medium |

---

## Per-paper findings

### 1. SwitchVLA: Execution-Aware Task Switching for VLA Models — 2506.03574 [V]
- **Date / org:** 2025-06-04. Beijing Innovation Center of Humanoid Robotics (x-humanoid.com) [V] [1].
- **(1) Physical behaviour on a new instruction.** The policy predicts a behaviour mode. Quote [V] [1]: "forward (b_t = 0) continues standard execution, rollback (b_t = 1) undoes previous actions upon detecting an intent mismatch while in contact, and advance (b_t = 2) transitions to a new subtask when the instruction updates and no physical interaction is present."
  - Training target for advance [V]: "Interpolate linearly in joint space between the current action a_t and a canonical start pose a_normal_0, defined as the mean of initial trajectories for instruction l_cur."
  - Timing [V]: "After each action chunk is executed, the model updates l_pre ← l_cur … New instructions can be issued at any timestep, upon which the model re-evaluates b_t and dynamically adjusts behavior."
  - Classification: replan from the current state with a learned mode. Rollback = reverse actions while in contact. Advance = move toward the *new task's* start pose, which is a retract-like behaviour to a canonical pose, not a blend. The switch takes effect at the next chunk/inference step. There is no in-chunk blending. Actions are smoothed with ACT-style temporal ensembling: "predict 100 future actions (chunk size) and use first 30 actions for temporal ensembling" [V].
- **(2) Trigger:** text instruction pair (l_pre, l_cur). No speech mentioned [V, by absence in full text]. The switch is truly mid-motion. Evaluation issues it "early (pre-contact), mid (in-contact), and late (post-action)" [V].
- **(3) Platform:** simulation (LIBERO-Goal) and real hardware: "two dual-armed Franka Emika Panda robot workstations", 15 Hz [V].
- **(4) Base policy:** built on Florence-2 with a flow-matching "Conditional Execution Expert" outputting action chunks [V]. No real-time chunking (RTC). Baselines are π0, OpenVLA-OFT, **MT-ACT**, and Diffusion Policy. SmolVLA is not used [V].
- **(5) Code:** not stated in the paper. The project page https://switchvla.github.io has no code link in its static HTML [V, checked].
- **(6) Metrics [V]:**
  - LIBERO-Goal success, No/Early/Mid/Late switch: SwitchVLA 93.0 / 93.5 / 50.9 / 68.7; π0 92.3 / 40.7 / 8.3 / 10.2; OpenVLA-OFT 98.0 / 40.6 / 11.1 / 13.0.
  - Real WS1, No/Early/Mid/Late: SwitchVLA 95.9 / 99.3 / 95.1 / 75.0; MT-ACT 56.3 / 0.0 / 0.0 / 4.9; π0 97.9 / 50.1 / 0.0 / 32.0.
  - Real WS2: SwitchVLA 100.0 / 95.1 / 96.5 / 94.4.
  - Long sequence, real: 95.6 (A→B) down to 54.2 (A→…→F). Baselines all 0.0.
  - No latency metric and no quantitative smoothness metric. "Interaction naturalness" is shown qualitatively, plus a failure-cause breakdown (object drop, position error, execution halt, instruction ignore).
- **(7) Speech-overlap mid-motion repair?** No. It is text-only, the instruction is assumed to be complete when it arrives, and it uses a large Franka setup. It is the closest *learned* mid-motion switcher, but "advance" heads toward a canonical start pose.

### 2. VITA-E: Concurrent Seeing, Hearing, Speaking, and Acting — 2510.21817 [V]
- **Date / org:** 2025-10-21. Nanjing University, Tencent Youtu Lab, CASIA, Fourier Intelligence [V] [2].
- **(1) Physical behaviour on a new instruction:** stop plus **retract to initial pose**. Quote [V] [2]: "The Standby Model then preempts the Active Model, halting its execution of Task A. … To ensure safety during this transition, a retraction mechanism is employed, which returns the robot to the initial pose by sequentially popping and executing inverse movements from a stored action stack." The limitations section confirms it [V]: "while our current task-switching relies on a safe retraction to a neutral state, we plan to explore methods for achieving smoother and more efficient transitions between tasks."
- **(2) Trigger:** user speech.
  - [V]: the system can "listen to user speech" while acting.
  - The VLM is a fine-tuned VITA-1.5 [V], an interruptible full-duplex voice model.
  - Whether audio goes in end-to-end or through ASR is **not explicit** in the VITA-E text [U]. The paper formalises the input as "a natural language instruction from the user L_user_t" [V].
  - The switch command arrives mid-motion, but the response is halt and retract, not repair.
- **(3) Platform:** real Fourier GR2 humanoid with a head-mounted RealSense D455. LIBERO is used for basic manipulation only [V].
- **(4) Base policy:** dual-system. The VLM is VITA-1.5 and the action expert is the GR00T Diffusion Transformer; it outputs action chunks [V]. No RTC. SmolVLA, π0, GR00T and Diffusion Policy appear only as manipulation baselines (Fig. 6), not as switching baselines [V].
- **(5) Code:** https://github.com/Tencent/VITA/tree/VITA-E, linked from the homepage https://lxysl.github.io/VITA-E/ (HTTP 200) [V-link; contents not inspected].
- **(6) Metrics [V], 30 trials each:** Speech Interruption SR 100%, Task Switching SR 93.3%, Emergency Stop SR 100%. Average voice-response latency 2.26 s over ten tests. No motion-switch latency and no smoothness metric.
- **(7) Speech-overlap mid-motion repair?** Partially. It covers speech arriving *during* motion and concurrent speak-while-act. But the action switch is preempt → retract → restart, which is exactly the stop-and-retract baseline. The paper itself names smoother transitions as future work [V].

### 3. Hi Robot: Hierarchical VLA for open-ended instruction following — 2502.19417 [V]
- **Date / org:** 2025-02-26 (v2 2025-07-15, ICML 2025). Physical Intelligence, with Stanford and UC Berkeley affiliations [V] [3].
- **(1) Physical behaviour:** replan from the current state at the *subtask-command* level. Quote [V]: "The user can intervene at any point during policy execution … When the system receives a user intervention, the high-level inference is triggered immediately to recompute ℓ̂_t." Otherwise high-level inference reruns "either when one second has elapsed, or when a new interaction with the user takes place."
  - The low-level π0 simply receives the new low-level command. The paper does **not** describe what happens to the in-flight chunk: no blending or inpainting is described, and no stop/retract is described either [U for chunk handling].
  - After an interjection is fulfilled, the user "can signal to the robot that it may switch back to the previous command" [V].
- **(2) Trigger:** "text commands or spoken language (which is then transcribed into text)" [V]. ASR is "Whisper large-v2" running locally on audio from a "consumer-grade lavalier microphone". TTS uses the Cartesia API (spelled "Cartetia" in the paper) [V]. Interjections arrive during execution. The switch is at the language-command level, so it takes effect at the next low-level inference [inferred].
- **(3) Platform:** real robots — UR5e single arm, bimanual ARX, and Mobile ARX (Mobile ALOHA-based) [V].
- **(4) Base policy:** PaliGemma-3B-based high-level VLM and a π0 low-level policy with flow-matching action chunks [V]. Uses action chunking ("With action chunking … control robots at 50 Hz"). No RTC is mentioned [V by absence]. No SmolVLA or ACT model is used.
- **(5) Code:** not stated in the paper. No code link on the pi.website page [V, checked HTML].
- **(6) Metrics:**
  - Instruction Accuracy and Task Progress are reported only in bar charts. Text claim [V]: "Hi Robot averages over 40% higher instruction accuracy than GPT-4o".
  - No switch-latency or smoothness metric.
  - Component latency [V]: low-level per-step total 73 ms on-board / 86 ms off-board + WiFi (RTX 4090). High-level single decoding step 47 ms prefill + 13.2 ms decode.
- **(7) Speech-overlap mid-motion repair?** No. Speech is handled by ASR on a finished utterance, and the switch acts on the next command. There is no repair of the current chunk and no handling of partial or overlapping speech [inferred from what is described].

### 4. One Word, Different Action: real-robot benchmark — 2609.05260 [V]
- **Date / org:** 2026-09-04 (v2 2026-09-13). CUHK-Shenzhen and Shenzhen Research Institute of Big Data [V] [4].
- **(1) Physical behaviour:** not applicable. It is an offline decision benchmark. Instances are built on "85 physical decision anchors" "collected and verified with a real robot", and models output "a machine-readable executable decision" [V]. Nothing executes, so there is no mid-execution change.
- **(2) Trigger:** text only. The evaluated models are text LLMs: GLM-5-FP8, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, OLMo-2-1124-7B-Instruct [V].
- **(3) Platform:** real-robot-derived anchors; the evaluation itself is offline [V]. The robot model is not identified in the text [U].
- **(4) Base policy:** none (LLMs). No chunking, no ACT, no SmolVLA [V].
- **(5) Code:** not stated [V by absence].
- **(6) Metrics [V], Table III (Atomic / Composite / Cond. Comp. / Invariance / Sensitivity):**
  - GLM-5-FP8: 0.994 / 0.949 / 0.818 / 0.961 / 0.843
  - Qwen2.5-7B: 0.844 / 0.645 / 1.000 / 0.657 / 0.471
  - Mistral-7B: 0.978 / 0.836 / 0.610 / 0.755 / 0.696
  - OLMo-2-7B: 0.878 / 0.828 / 0.929 / 0.814 / 0.667
  - No switching latency or smoothness metric.
- **(7)** No. It is relevant only as a *metric idea*: decision invariance vs. sensitivity to wording changes.

### 5. Causeway: Restoring Task Accessibility for Instruction Switching — 2609.30913 [V]
- **Date / org:** 2026-09-25. University of Maryland, College Park, and University of Southern California [V] [5].
- **(1) Physical behaviour:** replan from the current state via a policy-decoded **return motion to a demonstration-supported re-entry pose for task B**, then hand off. This is not home and not a stop.
  - Quote [V]: "The write starts at the instruction switch. If the hand holds o_A ≠ o_B, only the gripper channel is active until the hand opens beyond ḡ; otherwise, the position and orientation channels engage immediately."
  - Quote [V]: "every action, during re-entry and after handoff, is decoded by the frozen policy."
  - For same-object pairs it can re-route a held object "without put-down or re-grasp" [V].
  - Classification: a partial retract toward a task-B re-entry neighbourhood, carried out by the policy itself, with no external controller.
- **(2) Trigger:** text instruction ℓ_B, issued at three timings — sim at step 30 (approach), step 60, and post-completion; real robot "mid-approach, at pre-grasp, or post-completion" [V]. It is truly mid-motion. No speech [V by absence].
- **(3) Platform:** sim (LIBERO-Goal, LIBERO-Object) and a real xArm 6 with π0.5 fine-tuned on 30 demos per task [V].
- **(4) Base policies:** OpenVLA-OFT (parallel decoding), π0.5 (flow matching), GR00T N1.5 (diffusion), all with action chunks [V]. No RTC, no ACT, no SmolVLA [V by absence].
- **(5) Code:** not stated; there are no URLs in the text [V by absence].
- **(6) Metrics [V]:**
  - Sim bare-switch → Causeway success: π0.5 26.0% → 61.6%, OpenVLA-OFT 3.4% → 64.5%, GR00T 9.9% → 47.5%.
  - Reaching the handoff neighbourhood: +42–72 pp.
  - Real xArm pooled, bare → ours: approach 42.9 → 100, pre-grasp 14.3 → 94.3, after A 17.1 → 82.9 (5 trials/cell).
  - Cost: per-chunk latency rises 2.5–2.8× (102/75/128 → 253/187/362 ms; replanning 4.0/5.3/2.8 Hz) on an A100.
  - No smoothness metric.
- **(7)** No speech. The return-motion repair is real, but it re-routes to a re-entry pose rather than blending the in-flight chunk. It needs gradients through the policy and per-architecture calibration [V: "requiring per-architecture calibration"].

### 6. CIRRA: Continual Instruction Reconciliation — 2610.08862 [V]
- **Date / org:** 2026-10-05 (v2 2026-10-12). University of Georgia, Northeastern University, EmbodyX Inc. [V] [6].
- **(1) Physical behaviour:** **wait for a step/subtask boundary**, chosen by an interruptibility mode.
  - Quote [V]: "If ι = immediate, it may be paused immediately and resumed after the inserted subtasks are completed. If ι = safe point, integration is delayed until the next safe execution boundary. If ι = uninterruptible, the active subtask must finish before the revised sequence can take effect."
  - Quote [V]: "A paused skill switches its policy to standby mode … and later resumes from the current observation."
  - Classification: pause/standby or wait for boundary. No motion repair.
- **(2) Trigger:** text utterance u_t. CHIRP is "text-based" [V]. No speech/ASR mentioned [V by absence]. On the real robot the instruction can arrive "during navigation, at the onset of a grasp, or mid-manipulation" [V], but it acts only at the boundary.
- **(3) Platform:** CHIRP text benchmark (120 episodes) and a real Unitree G1 humanoid [V].
- **(4) Base policy:** Qwen3-VL-8B planner. Skills are eight policies "fine-tuned from ImageWAM … on 50 demonstrations" [V]. Chunking and RTC are not discussed [U]. SmolVLA appears only in the reference list [V].
- **(5) Code:** the text says benchmark stages are "all shipped with the code", but no URL is given [V; URL not stated].
- **(6) Metrics [V]:**
  - CHIRP: 74.2% decision agreement, +30 pp over the strongest replanning baseline.
  - Real G1: DA 95.6%, TA 95.8%, EA 95.6% (+18.4, +26.6, +32.0 over ITP).
  - Interruption compliance 100% vs. baselines "at most 51.6%".
  - No latency or smoothness metric.
- **(7)** No. It is task-planning-level preemption only.

### 7. Watch, Recall, Act: Always-On Robots (ARMS) — 2609.28429 [V]
- **Date / org:** 2026-09-23 (v2 2026-10-09; CoRL 2026). Shanghai Jiao Tong University, CUHK, Nanjing University, Astribot, Juxi Tech [V] [7].
- **(1) Physical behaviour:** **continue the foreground task and run the inserted action concurrently on the other arm**, not a switch. Quote [V] (Table 1 definition): "Concurrent: runs the inserted action on a free arm without halting the foreground."
  - The ablation "hard interrupt (no async concurrency)" drops foreground continuation 76 → 41 and non-interference 78 → 38 [V].
  - Single-arm in-flight chunk repair is not addressed [inferred].
- **(2) Trigger:** language instructions and visual "guards" (standing conditions fired by a perception gate) [V]. No speech [V by absence]. It is mid-task, but handled through context injection into π0.5 rather than motion repair.
- **(3) Platform:** real AgileX Cobot Magic dual-arm robot plus the ARMS Dataset [V].
- **(4) Base policy:** a single π0.5 backbone with three asynchronous modules [V]. RTC (Black et al.) is cited in related work only [V]; whether it is used is not stated [U]. No ACT or SmolVLA.
- **(5) Code:** "We will publicly release ARMS Dataset and the construction code" — no URL [V].
- **(6) Metrics [V]:**
  - EAS 45 vs. 28 for the best baseline (SwitchVLA re-implementation: Recall 15, FG-Res 58, EAS 28).
  - Real: Watch+concurrency success / FG-resume 65 / 70 vs. 20 / 28.
  - Median trigger-to-decision latency "under 200 ms".
  - No smoothness metric.
- **(7)** No speech and no chunk repair. It is a different strategy: add parallelism with a second arm instead of repairing the motion.

### 8. TempoBridge: Language-Guided Tempo Control — 2610.09451 [V]
- **Date / org:** 2026-10-07. KAIST [V] [8].
- **(1) Physical behaviour:** no new instruction mid-execution. The tempo is parsed "Once per instruction" (Fig. 2 label, [V]). A causal phase router "permits only a single forward transition from Event 1 to Event 2" inside one compound instruction (e.g., "Quickly pick up … and slowly place …") [V]. A gain scales translation of each chunk: "The robot executes the first M ≤ H actions of the modulated chunk, receives a new observation, and replans" [V]. This is modulation inside an instruction fixed from the start.
- **(2) Trigger:** text. The change is planned at the phase boundary, not a new user command [V].
- **(3) Platform:** LIBERO sim and a real xArm6 [V].
- **(4) Base policy:** frozen π0.5, chunked. No RTC, ACT or SmolVLA [V by absence].
- **(5) Code:** not stated. The project page https://lysees.github.io/tempobridge-page/ has no code link in its static HTML [V checked].
- **(6) Metrics [V]:**
  - Tempo Success Rate 52.6% → 89.7% (canonical).
  - Task success 92.9% vs. 93.6% baseline.
  - Real: 60/67 (89.6%) vs. baseline 60/66 (90.9%).
  - Table V: Readout Accuracy 97.5% / 78.4%, Balanced Phase Agreement 89.7% / 90.4%, median FAST-to-SLOW speed ratio 1.58× / 1.52× (canonical / unseen).
- **(7)** No. It is relevant only because a scalar "how" modifier (speed) could be one class of mid-motion correction.

### 9. Training-Free Action Correction via Language Feedback (CorrectVLA) — 2608.29967 [V]
- **Date / org:** 2026-08-30. Carnegie Mellon University [V] [9].
- **(1) Physical behaviour:** **offline, between episodes**. Quote [V]: "A human reviewer can identify the critical error region and provide sparse corrections … after observing the complete rollout." Also [V]: "Feedback is provided once at the task level and reused across all rollouts without per-episode intervention." Additive biases follow a piecewise-linear envelope over a time window (e.g., "down little 2.0–2.3s"), and the corrected rollout is re-executed [V].
- **(2) Trigger:** text, parsed by an LLM. Between episodes, not mid-motion [V].
- **(3) Platform:** LIBERO-90 sim and a real UFactory xArm7 [V].
- **(4) Base policy:** OpenVLA-OFT and π0.5 (`lerobot/pi05_libero_finetuned`; real robot uses π0.5-DROID) [V]. No RTC, ACT or SmolVLA.
- **(5) Code:** not stated. The project page https://correctvla.github.io has no code link in its static HTML [V checked].
- **(6) Metrics [V]:**
  - Real: 2/20 (10%) → 19/20 (95%).
  - Sim in-distribution recovery rate 65/139 (46.8%); OOD recovery 33/328 (10.1%).
  - No switching latency or smoothness metric.
- **(7)** No. The correction is not online and does not overlap the motion.

### 10. RoboPrompt: Policy Steering with Sparse Human Input — 2610.10534 [V]
- **Date / org:** 2026-10-07. Shanghai Jiao Tong University, Shanghai Innovation Institute, Noematrix Ltd. [V] [10].
- **(1) Physical behaviour:** **continue and blend** across replanning chunks.
  - Quote [V]: "Let m denote the replanning chunk index after a prompt is issued … the first chunk follows the human input strongly, while later chunks gradually reintroduce the base policy prior."
  - NA-FRS gives "a smoother, near-linear action transition across denoising levels" [V].
  - Whether the robot pauses while the user draws is not stated [U].
- **(2) Trigger:** drawn traces or points on the camera image, plus "global action prompts … given as text inputs appended to the task instruction" (coarse directions) [V]. No speech [V by absence]. Steering happens during execution, but it targets motion corrections within the task, not new task instructions.
- **(3) Platform:** real Flexiv Rizon4 with a Robotiq 2F-85 gripper [V].
- **(4) Base policies:** Diffusion Policy, π0.5, FastWAM (diffusion / flow, chunked) [V]. No RTC (it builds on Flow Reversal Steering). No ACT or SmolVLA.
- **(5) Code:** https://github.com/yanwen-zou/Roboprompt, linked from the project site (HTTP 200) [V-link; contents not inspected].
- **(6) Metrics [V]:**
  - Prompt alignment "above 95% across all three policies".
  - DAgger: +15.5% average success for π0.5 across three tasks and +21.3% across three policies on Insert Bread.
  - Interventions down 44.0% (2.86 → 1.60) and 81.9% (2.60 → 0.47).
  - No latency number in what was read [U].
- **(7)** Partial on the *mechanism*: it blends a new human intent into ongoing chunked flow/diffusion generation without stopping. But it has no speech, no task switching, and a high-end arm.

---

## Synthesis — which papers perform mid-motion repair on a new instruction?

- **Truly mid-motion, no stop and no full retract: SwitchVLA [1], Causeway [5], and RoboPrompt [10].**
  - **SwitchVLA [1]** is the strongest learned example. The instruction can change at any timestep, and the policy forward/rollback/advances at the next chunk. Advance interpolates toward the new task's canonical start pose, so it is a learned partial retract rather than an in-chunk blend. It is text-only, on dual Franka arms. Its code is not released per the paper and site.
  - **Causeway [5]** repairs reachability after a mid-approach or pre-grasp switch. A training-free gradient write makes π0.5 / OFT / GR00T decode a return motion to a task-B re-entry pose. It is text-only, runs on an xArm6, and costs 2.5–2.8× chunk latency.
  - **RoboPrompt [10]** blends sparse sketch or direction steering into ongoing flow/diffusion chunks without stopping. But it is motion steering, not a new task instruction, and has no speech.
- **Speech mid-motion, but resolved by stop-and-retract: VITA-E [2].** It preempts and then "returns the robot to the initial pose" via an inverse action stack. Its authors explicitly leave smoother transitions to future work. It is the closest on the speech-concurrency axis and the clearest stated example of the baseline a repair method would beat.
- **Speech mid-task, but switching at the command level: Hi Robot [3].** It uses Whisper ASR on completed utterances. The high-level VLM recomputes immediately, and in-chunk handling is unspecified.
- **Not mid-motion repair:**
  - CIRRA [6] waits for an interruptibility boundary or pauses the skill.
  - ARMS [7] runs the new demand concurrently on the other arm.
  - TempoBridge [8] modulates within a fixed instruction.
  - CorrectVLA [9] corrects between episodes.
  - One Word, Different Action [4] is an offline LLM decision benchmark.
- **Distance to "speech-overlap mid-motion repair on a low-cost arm" (inference):**
  - None of the ten does all three: (a) act on speech that is still in progress or overlaps the motion, rather than a completed ASR transcript; (b) repair or blend the in-flight chunk instead of retracting; (c) run on a low-cost arm such as SO-101, with ACT or SmolVLA.
  - Closest per axis: VITA-E for speech during motion (but it retracts), SwitchVLA and Causeway for mid-motion switching (text only, Franka/xArm), and RoboPrompt for in-chunk blending (no speech).
  - No paper uses SmolVLA or a low-cost arm for switching. VITA-E uses SmolVLA only as a manipulation baseline [2], and SwitchVLA has MT-ACT only as a baseline, which scores 0.0 on mid-switch [1].
  - No paper uses RTC for the switch.
  - None reports a switching-smoothness metric (jerk etc.) or an instruction-onset-to-motion-change latency. ARMS's under-200 ms trigger-to-decision [7] and Causeway's per-chunk latency [5] are the nearest.

---

## Coverage Status
| Q | Paper | Status |
|---|---|---|
| 1 | SwitchVLA | done (full text) |
| 2 | VITA-E | done; speech-input mechanism (ASR vs end-to-end) needs follow-up — not explicit in text |
| 3 | Hi Robot | done; in-flight chunk handling not described in paper |
| 4 | One Word Different Action | done; robot model not identified |
| 5 | Causeway | done |
| 6 | CIRRA | done; real-robot instruction modality (typed vs spoken) not explicit, no speech mentioned |
| 7 | Watch Recall Act (ARMS) | done; RTC usage unknown |
| 8 | TempoBridge | done |
| 9 | CorrectVLA | done |
| 10 | RoboPrompt | done; pause-during-drawing and latency not found |

- All primary text came from `feynman alpha get --full-text <id>`, the alphaXiv-extracted paper text. Tables were parsed from extracted text, so their column alignment was reconstructed by reading. "[V by absence]" means a keyword grep of the full text found no mention (speech, voice, ASR, RTC, SmolVLA, github).
- I did not inspect the code repos [11] [12] beyond confirming they return HTTP 200.

## Sources
1. Li et al., "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models" — https://arxiv.org/abs/2506.03574 (site https://switchvla.github.io)
2. Liu et al., "VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting" — https://arxiv.org/abs/2510.21817 (homepage https://lxysl.github.io/VITA-E/)
3. Shi et al., "Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models" — https://arxiv.org/abs/2502.19417 (https://www.pi.website/research/hirobot)
4. Liu, Yang, Lei, "One Word, Different Action: A Real-Robot Benchmark for Language-Conditioned Embodied Reasoning" — https://arxiv.org/abs/2609.05260
5. Wang et al., "Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies" — https://arxiv.org/abs/2609.30913
6. Zhang et al., "CIRRA: Dual-Level Continual Instruction Reconciliation with Ongoing Execution…" — https://arxiv.org/abs/2610.08862
7. Yi et al., "Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams" — https://arxiv.org/abs/2609.28429
8. Lee et al., "TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies" — https://arxiv.org/abs/2610.09451 (https://lysees.github.io/tempobridge-page/)
9. Kwon et al., "Training-Free Action Correction for VLA Model Failures via Language Feedback" — https://arxiv.org/abs/2608.29967 (https://correctvla.github.io)
10. Zou et al., "RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input" — https://arxiv.org/abs/2610.10534 (https://yanwen-zou.github.io/Roboprompt-Website/)
11. VITA-E code branch — https://github.com/Tencent/VITA/tree/VITA-E
12. RoboPrompt code — https://github.com/yanwen-zou/Roboprompt
