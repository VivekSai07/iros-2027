# Mid-motion instruction handling: ELLSA vs VITA-E vs Hi Robot vs SwitchVLA (R1)

Date: 2026-10-18. Tags: **[V]** I read it in the primary text (paper HTML, official README/model card, or repo code). **[S]** secondary source. **[U]** my inference or unverified.
Context: SO-101 + SmolVLA (450M) / ACT; GPUs: 8 GB consumer + 1× 48 GB RTX 6000 Ada.

## Summary table

| | ELLSA [1] | VITA-E [3] | Hi Robot [7] | SwitchVLA [9] |
|---|---|---|---|---|
| Trigger / entry | TTS speech (CosyVoice2) fed **end-to-end** via a streaming Mamba encoder; no ASR in the loop [V] | Live voice → VITA-1.5 audio encoder (end-to-end audio tokens) + Silero VAD in demo [V code/README] | Text or live speech → **Whisper large-v2 ASR** → text [V] | Text instruction tokens (BART encoder) [V]; no speech |
| At interruption | **Stop**: says "Action Cancelled" and stops [V] | Stop = instant `[HALT]`; Switch = preempt → **retract to initial pose** → new task [V] | High-level VLM re-runs **immediately**; low-level π0 gets a new atomic command [V] | Policy picks **forward / rollback / advance** from contact state [V] |
| Key latency | 854 ms (S2S) / 786 ms (speech→action) per 1 s block, A100 [V] | 2.26 s average voice-response latency; GPU not stated [V] | Low-level 73 ms on-board / 86 ms off-board; high-level 47+13.2 ms, RTX 4090 [V] | Not reported; 15 Hz control on RTX 4090 [V] |
| Backbone | Llama-3.1-8B + Emu3-Base (UniVLA), FAST tokens [V] | VITA-1.5 (Qwen2, hidden 3584) + GR00T-N1 DiT; horizon 16 [V config] | 2× PaliGemma-3B (π0 + high-level VLM) [V] | Florence-2-base, flow matching, chunk 100 [V] |
| Robot | Sim only: LIBERO (+CALVIN) [V] | Fourier GR2 humanoid + LIBERO [V] | UR5e, bimanual ARX, mobile ARX [V] | 2× dual-arm Franka + LIBERO-Goal [V] |
| Human study | None [V] | None (human raters in ablation) [V] | None; blind human evaluator scores IA/TP [V] | None [V] |
| Code / weights | HF weights + eval code; training "coming soon" [V] | Code + weights (Tencent/VITA@VITA-E; HF) [V] | None found [V for paper/project page] | None found [V for paper/site] |
| Fits 8 GB? | No; 48 GB is tight [U] | No; README says 48 GB [V] | Probably not both models at once; 48 GB OK [U] | Likely yes [U] |

---

## 1. ELLSA, arXiv 2510.16756 (ICLR 2026 per the model card)
**Strategy: stop on barge-in.**

- **(a) Trigger.** All instructions, including barge-in commands, are synthetic TTS speech: "each interruptive command is generated 150 times with CosyVoice2-0.5B for training and 20 times for testing. We additionally employ Whisper-medium-en … to filter samples" [V][1]. Whisper is used only to filter data, not at inference. Audio enters end-to-end. A "streaming Mamba encoder" runs at 25 Hz, is downsampled to 5 Hz, and feeds the Llama speech expert [V][1]. The test set has 10 commands, e.g. "Stop now.", "Hold on.", "Do not move." [V][1].
- **(b) What happens physically.** "Upon hearing such a command, ELLSA must immediately stop the ongoing action … ELLSA explicitly responds with 'Action Cancelled', upon receiving an interruptive command, as an indicator to stop action." [V][1]. Evaluation inserts the speech query "2–8 seconds after the initial action instruction" [V][1]. The model runs in 1 s time blocks, so the stop can only take effect at a 1 s block boundary [U]. Interruptive-command success: **94.3%**; general question: 100.0%; silence: 100.0% (Table 3c) [V][1].
- **(c) Repair or continuation.** None described after the stop. For non-interruptive speech, it keeps acting while answering ("speaking-while-acting") [V][1].
- **(d) Latency.** Table 9(d), "average per–time-block latency measured on an A100 GPU": 1 s block → **854ms** speech-to-speech, **786ms** speech-to-action. 0.48 s block → 455ms and 428ms [V][1]. Turn-taking counts as successful "if the model responds within 1 second after the question ends" [V][1].
- **(e) Backbone.** Speech expert is LLama-3.1-8B-Instruct with LoRA r=256. Action expert is Emu3-Base (pretrained UniVLA) with "the final 1,024 token IDs … replaced with FAST tokens". The two are fused by SA-MoE attention with a shared KV cache. CosyVoice2-0.5B is the synthesizer [V][1]. Each 1 s block contains 8 text tokens and "one second of speech and action output" [V][1]. The 0.48 s variant produces "5 action frames per block" [V][1]. The paper gives no explicit chunk size for the 1 s block.
- **(f) Robot.** Simulation only: LIBERO, plus a CALVIN variant. Limitations section: "has yet to be validated in real-world settings" [V][1].
- **(g) Human study.** None [V].
- **(h) Code and weights.** The paper points to github.com/bytedance/SALMONN/tree/ELLSA, which is robots-disallowed (see Blocked sources). The HF model `tsinghua-ee/ELLSA` exists: 8 safetensors shards, about 36.6 GB in total, Apache-2.0. Its README TODO marks LIBERO and speech eval as supported, with "Release the training data" and "Support for training" still unchecked [V][2].
- **(i) GPU.** Trained and timed on A100 [V][1]. About 36.6 GB of bf16 weights does not fit on 8 GB. On 48 GB it is borderline once KV cache, the Emu3 tokenizer and CosyVoice are added [U].
- **(j) Applicability to SO-101.** The barge-in behaviour is learned inside a 16B-class joint model, so it cannot be transplanted to SmolVLA or ACT [U]. What does carry over: the time-block design, where every control tick consumes the latest audio and the model can emit a stop/"cancel" token, and the stop-command phrase list. A separate small keyword-spotting or VAD+ASR head on the 8 GB GPU could gate the policy loop with the same behaviour [U].
- **(k) Key claim and caveat.** First end-to-end full-duplex listen/look/speak/act model, with 94.3% action barge-in. Caveat: simulation only, TTS-only speech, the robot only stops (no repair), and stopping is quantized to the 1 s block [U].

## 2. VITA-E, arXiv 2510.21817
**Strategy: halt, or retract-to-home and then switch.**

- **(a) Trigger.** Live user speech. The released VLM config uses `mm_audio_encoder: VITA-MLLM/VITA-1.5_AudioEnc` and an InternViT-300M vision tower [V][5]. The server code calls `vita_model.get_audio_encoder()`, which means audio is tokenized end-to-end rather than going through a separate ASR step [V][4]. The demo needs a Silero VAD module [V][4]. The paper itself formalizes the input only as "a natural language instruction" [V][3].
- **(b) What happens physically.**
  - Emergency stop: the Standby model "generates a [HALT] token and triggers an immediate preemption of the Active Model, which breaks its action-generation loop and sends a final halt command to the robot client" [V][3].
  - Task switch: "The Standby Model then preempts the Active Model, halting its execution of Task A … To ensure safety during this transition, a retraction mechanism is employed, which returns the robot to the initial pose by sequentially popping and executing inverse movements from a stored action stack." [V][3].
  - In the code, every generated action chunk is pushed to `action_feature_stack`. When the top of the stack belongs to the other model, one chunk per observation is popped and sent as type `"retraction"`; that cycle's action generation is skipped [V][4]. I did not see a within-chunk reversal in the client [V][4]. Because actions are absolute joint targets, replaying the chunks in LIFO order approximately retraces the path [U].
  - Questions asked during an action are answered by the Standby model "without interrupting the ongoing physical task" [V][3].
- **(c) Repair or continuation.** Retract to the initial pose, then the new Active model starts Task B. The paper names this as future work: "while our current task-switching relies on a safe retraction to a neutral state, we plan to explore … smoother … transitions" [V][3]. Task A is not resumed.
- **(d) Latency.** "The average latency of VITA-E's voice responses across ten tests is 2.26s" [V][3]. The paper gives no halt-to-motion-stop latency and no GPU. Success over 30 trials: speech interruption 100%, emergency stop 100%, task switching **93.3%**. Switching failures came from the VLM misreading the command as a question [V][3][4]. Ablation accuracy: emergency stop "from 0% to 100%"; correct action instruction "from under 10% to 95%" [V][3].
- **(e) Backbone.** VITA-1.5 VLM. The config is Qwen2 with hidden 3584 and 28 layers, which suggests a ~7B LLM [U]. Action head is the GR00T-N1 DiT (`_name_or_path: nvidia/GR00T-N1-2B`, 16 layers), with `action_horizon: 16`, `action_dim: 32` and 16 inference timesteps [V][5]. Only the projection head is fine-tuned on robot data [V][3]. Two full instances run at once (Active and Standby) [V][3].
- **(f) Robot.** Fourier GR2 humanoid. 300 teleop demos per task at 20 Hz over 26 DoF; 2 pick-and-place tasks; 30 trials each. SmolVLA is one of the baselines [V][3]. LIBERO results are below GR00T [V][3].
- **(g) Human study.** None. Human evaluators judge the VLM-response accuracy in the ablation [V][3].
- **(h) Code and weights.** `github.com/VITA-MLLM/VITA-E` returns **HTTP 404** [V]. The code lives at `github.com/Tencent/VITA`, branch `VITA-E`. I cloned it and checked `inference_vita_e.py`, `vita_e/server_vla_vita.py`, `vita_e/vla_robot_client.py` and `gr00t/` [V][4]. Weights are at HF `VITA-MLLM/VITA-E`: `vita_vla_finetune` (~16.6 GB) and `vita_gr00t_robot` (~20 GB) [V][5].
- **(i) GPU.** README: "A total of 48 GB GPU memory is needed" for the web demo [V][4]. The paper names no GPU. Won't fit 8 GB. 48 GB is right at the edge [U].
- **(j) Applicability to SO-101.** These parts are backbone-agnostic [U]:
  - an action-chunk LIFO stack with retract-to-home;
  - a supervisor process with preemption semaphores;
  - a control-token vocabulary (`[RES]/[ACT]/[INST]/[HALT]/[END]`).
  
  These can wrap SmolVLA or ACT chunks unchanged [U]. The "model-as-controller" part needs a VLM that emits the tokens. That could be a small VLM or an ASR+LLM router on the 48 GB card, with SmolVLA on the 8 GB card [U].
- **(k) Key claim and caveat.** Dual-model preemption gives 100% stop and 93.3% switching on a real humanoid. Caveats: n=30, no motion-stop latency, two ~7B+2B instances, and switching discards progress by retracting home.

## 3. Hi Robot, arXiv 2502.19417 (ICML 2025)
**Strategy: hierarchical VLM re-prompts π0.**

- **(a) Trigger.** "text commands or spoken language (which is then transcribed into text)". Hardware is a lavalier mic and local Whisper large-v2. Spoken replies use the Cartesia TTS API (the paper spells it "Cartetia") [V][7].
- **(b) What happens physically.** The robot does **not** wait for the step to finish. "When the system receives a user intervention, the high-level inference is triggered immediately to recompute ℓ̂t". Otherwise the high level re-runs "when one second has elapsed" [V][7]. The physical change happens when π0 receives the new low-level command at its next chunk inference [U]. No explicit stop or retract is described. The paper's example: "when the user says, 'that's not trash,' the robot correctly puts the bowl back down" [V][7].
  - **Note:** VITA-E describes Hi Robot as adjusting "the control policy for the next step after the current atomic step has been completed" [S][3]. Hi Robot's own text contradicts that. The SwitchVLA paper makes the same "wait" claim about planner methods generally [S][9].
- **(c) Repair or continuation.** The VLM issues corrective atomic commands, plus optional verbal confirmations. "When an interjection ('leave it alone') has been fulfilled, the user can signal to the robot that it may switch back to the previous command and continue" [V][7]. It has no memory: a listed failure is "Difficulty with instructions requiring long-context reasoning, since the current system lacks memory" [V][7].
- **(d) Latency on RTX 4090.**
  - Low-level per step: image encoding 14 ms, observation processing 32 ms, action prediction (x10) 27 ms; "Total (on-board) 73", "Total (off-board + WiFi) 86" ms [V][7].
  - High-level single decoding step: "RTX 4090: 47 ms (prefill) + 13.2 ms (decode)"; H100: 17.3 + 5.7 ms [V][7].
  - Quote: "real-time feasibility at ∼10 Hz … With action chunking … 50 Hz" [V][7]. ASR and TTS latency are not reported.
- **(e) Backbone.** Both policies start from PaliGemma-3B. The low level is π0 with a flow-matching action expert that outputs action chunks A_t of H actions. H is not stated in the text I read [V][7].
- **(f) Robot.** UR5e (single arm), bimanual ARX, mobile ARX. Tasks: table bussing, sandwich making, grocery shopping [V][7].
- **(g) Human study.** No user study. "a human evaluator who is blind to the method … 20 trials per task per method" scores Instruction Accuracy and Task Progress [V][7]. Project-page averages: Hi Robot IA 76 / TP 81; GPT-4o high-level 30 / 64; flat VLA 36 / 44; expert human 100 / 89 [V][8].
- **(h) Code and weights.** The paper and project page link no code [V][7][8]. π0 is available through openpi (I did not check it for this run) [U].
- **(i) GPU.** "one to two NVIDIA GeForce RTX 4090" (24 GB) for inference. High-level training took "approximately 2 hours on 8×H100" [V][7]. Two ~3B models in bf16 will not both fit in 8 GB. 48 GB is comfortable [U].
- **(j) Applicability to SO-101.** This is the most policy-agnostic of the four. The paper says: "our framework is inherently modular, allowing for the integration of alternative language-conditioned policies" [V][7]. SmolVLA can serve as the language-conditioned low level [U]. ACT has no language input, so it would need per-skill models or a task-ID input [U]. A small VLM fine-tuned on synthetic interjections can run on the 48 GB card [U].
- **(k) Key claim and caveat.** Event-triggered high-level re-planning lets mid-task corrections be grounded in the scene. Caveats: there is no explicit motion-safety behaviour at interruption, and the low level can "temporarily ignor[e] instructions … due to training bias toward proximal objects" [V][7].

## 4. SwitchVLA, arXiv 2506.03574
**Strategy: execution-aware switching.**

- **(a) Trigger.** A new text instruction l′ "at arbitrary times". It is encoded with BART and padded to 20 tokens, together with the previous instruction and contact state [V][9]. No speech.
- **(b) What happens physically.** The policy predicts the behaviour mode b_t each step:
  - "forward … continues standard execution";
  - "rollback … undoes previous actions upon detecting an intent mismatch while in contact" (e.g. put the cookie box back down);
  - "advance … transitions to a new subtask when the instruction updates and no physical interaction is present".
  
  New instructions "can be issued at any timestep, upon which the model re-evaluates b_t" [V][9].
- **(c) Repair mechanism.** Training needs no extra switch data [V][9]:
  - Rollback targets are reversed demo actions {a_{t−1}…a_{t−K}}.
  - Advance targets are a linear joint-space interpolation toward a canonical start pose (the mean of initial poses for l_cur).
  - Contact labels come from GPT-4o on wrist images "at 1/3 Hz" plus the gripper state (80.7% labeling accuracy).
  - Losses: flow matching for actions, cross-entropy for contact and mode [V][9].
- **(d) Latency.** No latency figure. "data collection and inference frequency is 15Hz", single RTX 4090 [V][9].
- **(e) Backbone.** Florence-2-base (DaViT, BART, token dim 768) with a transformer-decoder "Conditional Execution Expert". It predicts "100 future actions (chunk size) and use first 30 actions for temporal ensembling … following … ACT". Optimizer AdamW, lr 5e-5, batch 512 [V][9]. The parameter count is not stated in what I read; Florence-2-base is ~0.23B [U].
- **(f) Robot and data.**
  - Real: two dual-arm Franka workstations, 4 tasks each, 200 teleop trajectories per task, 3 cameras.
  - Sim: LIBERO-Goal, 8 tasks × 50 demos.
  - Protocol: switching at early (pre-contact), mid (in-contact) and late (post-action) phases; 12 trials per evaluation [V][9].
  - Results:
    - LIBERO-Goal switch success, early/mid/late: SwitchVLA 93.5 / 50.9 / 68.7; π0 40.7 / 8.3 / 10.2 [V][9].
    - Real Workstation 1: SwitchVLA 99.3 / 95.1 / 75.0 vs π0 50.1 / 0.0 / 32.0 and MT-ACT 0.0 / 0.0 / 4.9 [V][9].
    - Long-sequence real accumulated success: 95.6 (A→B) down to 54.2 (A→…→F) [V][9].
- **(g) Human study.** None [V].
- **(h) Code and weights.** The project site switchvla.github.io has videos only. I found no repo or weights [V for site/arXiv; search may be incomplete].
- **(i) GPU.** Inference on a single RTX 4090 [V][9]. A Florence-2-base-sized policy should run within 8 GB [U].
- **(j) Applicability to SO-101.** The core idea (extra contact and behaviour-mode conditioning, reversed-demo rollback labels, interpolate-to-start advance) is a data and conditioning recipe. It can be grafted onto ACT, which already uses chunking and temporal ensembling, or onto SmolVLA's action expert. It needs re-training but no new teleop [U]. The contact label can come from the SO-101 gripper state [U]. Limitations section: "relies on contact-based phase segmentation as a proxy … three discrete behavior modes … may constrain flexibility" [V][9].
- **(k) Key claim and caveat.** Mid-contact switching goes from 0% (π0, MT-ACT) to about 95% with no extra data. Caveats: text only, no latency figures, no code, 12 trials, and "advance" assumes a canonical start pose.

---

## Cross-system observations
1. The four systems span the response options: stop (ELLSA, VITA-E `[HALT]`), retract-then-switch (VITA-E), re-prompt and blend through the low level (Hi Robot), and learned rollback/advance (SwitchVLA) [V][1][3][7][9].
2. None has a user study of perceived responsiveness. None reports latency from utterance end to arm-motion stop [V]. That is an open gap the SO-101 project could fill [U].
3. Only Hi Robot and VITA-E use live human speech on a real robot. ELLSA is TTS in simulation, and SwitchVLA is text only [V].
4. Feasibility on our GPUs [U]: SwitchVLA-style conditioning and the Hi Robot-style hierarchy (SmolVLA on 8 GB + router on 48 GB) are feasible. VITA-E's retraction stack can be reused without its models. ELLSA can't be reproduced on this hardware except as a 48 GB inference-only experiment.

## Blocked sources
- github.com/bytedance/SALMONN/tree/ELLSA: ROBOTS_DISALLOWED (known; not retried). I used the HF model card [2] instead.
- github.com/VITA-MLLM/VITA-E: HTTP 404 (the README's own clone URL). I used Tencent/VITA@VITA-E [4].

## Coverage status
- Done: all four systems, fields (a)–(k).
- Unresolved:
  - ELLSA action-chunk length per 1 s block.
  - VITA-E figure-only numbers (LIBERO; real-robot Fig. 6) and its inference GPU.
  - Hi Robot chunk length H and ASR latency.
  - SwitchVLA parameter count and latency.
  - Whether openpi or any Hi Robot high-level code is public.

## Sources
1. Wang et al., ELLSA, arXiv 2510.16756v2 — https://arxiv.org/html/2510.16756v2
2. ELLSA HF model card / files — https://huggingface.co/tsinghua-ee/ELLSA
3. Liu et al., VITA-E, arXiv 2510.21817 — https://arxiv.org/html/2510.21817 ; project page https://lxysl.github.io/VITA-E/
4. VITA-E code, Tencent/VITA branch VITA-E — https://github.com/Tencent/VITA/tree/VITA-E (README: https://github.com/Tencent/VITA/blob/VITA-E/README.md)
5. VITA-E weights — https://huggingface.co/VITA-MLLM/VITA-E (configs: vita_gr00t_robot/config.json, vita_vla_finetune/config.json)
6. (unused ID)
7. Shi et al., Hi Robot, arXiv 2502.19417v2 — https://arxiv.org/html/2502.19417v2
8. Hi Robot project page — https://www.pi.website/research/hirobot
9. Li et al., SwitchVLA, arXiv 2506.03574v1 — https://arxiv.org/html/2506.03574v1 ; site https://switchvla.github.io
