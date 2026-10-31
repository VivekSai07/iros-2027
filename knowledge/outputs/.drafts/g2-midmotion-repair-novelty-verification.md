# Verification report: g2-midmotion-repair-novelty-draft.md

**Date:** 2026-10-18 · **Verifier scope:** the draft `outputs/.drafts/g2-midmotion-repair-novelty-draft.md`, checked against research-A/B/C/D and `notes/g2-midmotion-repair-novelty-lead-notes.md`. The draft was not edited; this file is the only output.

**Method:**
- **arXiv IDs.** All 43 IDs were checked with `feynman_science_database_search` (source=arxiv, `arxiv_get_papers`, 3 batches).
- **Primary text.** `alpha_get_paper` / `alpha_ask_paper` were not available in this session. I read primary text instead from arXiv HTML (`arxiv.org/html/<id>`) or the arXiv PDF, using `fetch_content`, then exact-string search.
- **LeRobot.** Docs were fetched from `raw.githubusercontent.com`. The line number was checked with `curl` + `grep -n`, and the commit with the GitHub API.
- **URLs.** All URLs were checked with `curl -L` for HTTP status.

## 1. Bottom line

- **No ID/title mismatches.** All 43 arXiv IDs resolve to the paper the draft names, and every v1 date matches the month the draft gives.
- **High-stakes spot-checks.** 10 of the 10 claims are supported by primary text. Two need wording corrections:
  - **SwitchVLA:** the "canonical start pose" interpolation is how *training targets* for the advance mode are built, not a stated runtime rule.
  - **MIRA:** 466 ms is the *median* time from speech onset to *abort-command dispatch*, not to a physical stop.
- **LeRobot quote confirmed verbatim** at `docs/source/inference.mdx` line 419, on main @ `146d8474932c8b566717eb2738ba459337ab71c4` (commit date 2026-10-16T11:55:57Z).
- **Upgrades from the draft's [U]/[S] flags:**
  - VLA-Corrector's ID is now confirmed.
  - The ReSteer release statement and its 33%/73% numbers were read in primary text.
  - URLs for the DiscreteRTC and FutureRTC project sites were found; both resolve.
- **Corrections to apply:**
  - FutureRTC has 3 real tasks, not 1.
  - ReSteer's 33% baseline is the teleop-fine-tuned π0.5, not zero-shot (zero-shot is 7%).
  - SwitchVLA's "code not released" should read "not stated".
- **URLs:** all URLs resolve (HTTP 200) except two project pages the draft already lists as 404: ChunkFlow and FASTER.

## 2. arXiv ID ↔ title/date check (arXiv API)

| ID | arXiv title (API) | v1 date | First author | Draft label/date | Status |
|---|---|---|---|---|---|
| 2506.07339 | Real-Time Execution of Action Chunking Flow Policies | 2025-06-09 | K. Black | RTC, 2025-06, NeurIPS 2025 (comment confirms) | match |
| 2512.05964 | Training-Time Action Conditioning for Efficient Real-Time Chunking | 2025-12-05 | K. Black | 2025-12 | match |
| 2604.25050 | DiscreteRTC: Discrete Diffusion Policies are Natural Asynchronous Executors | 2026-04-27 | P. Wang | 2026-04 | match |
| 2605.25537 | Action-Prior Denoising for Smooth Real-Time Chunking | 2026-05-25 | D. Liu | Soft RTC, 2026-05 | match |
| 2603.19199 | FASTER: Rethinking Real-Time Flow VLAs | 2026-03-19 | Y. Lu | 2026-03 | match |
| 2607.12992 | ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning | 2026-07-14 | Z. Yang | 2026-07 | match |
| 2607.14695 | Reflex: Real-Time VLA Control through Streaming Inference | 2026-07-16 | Y. Guo | 2026-07, ICML 2026 (comment confirms) | match |
| 2607.24008 | FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking | 2026-07-27 | H. Jiang | 2026-07 | match |
| 2607.26055 | πR²: Reactive Real-time Flow Policies | 2026-07-28 | S. Park | 2026-07 | match |
| 2512.01031 | VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference | 2025-11-30 (v2 2026-07-26) | J. Tang | 2025-11; v2 2026-07 | match |
| 2609.34170 | RAVEL: Asynchronous Rolling Inference for Flow-Based VLA Models | 2026-09-28 | Y. Chen | 2026-09 | match |
| 2609.36540 | Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment | 2026-09-29 | M. Zoellner | 2026-09 | match |
| 2610.12007 | REACT: Rolling Denoising and Dual Decoupling … | 2026-10-08 | H. Xiong | 2026-10, CoRL 2026 (comment: Spotlight) | match |
| 2610.14997 | Barrier-Constrained Guidance For Real-time Asynchronous VLA Execution | 2026-10-10 | W. Yu | FreeBar, 2026-10, CoRL 2026 (comment confirms) | match |
| 2606.18589 | DREAM-Chunk: Reactive Action Chunking with Latent World Model | 2026-06-17 | W. Chen | 2026-06 | match |
| 2506.03574 | SwitchVLA: Execution-Aware Task Switching for VLA Models | 2025-06-04 | M. Li | 2025-06 | match |
| 2502.19417 | Hi Robot: Open-Ended Instruction Following with Hierarchical VLA Models | 2025-02-26 | L. X. Shi | 2025-02, ICML 2025 | match |
| 2510.21817 | VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting | 2025-10-21 | X. Liu | 2025-10 | match |
| 2510.16756 | End-to-end Listen, Look, Speak and Act | 2025-10-19 | S. Wang | ELLSA, 2025-10, ICLR 2026 (journal_ref confirms) | match |
| 2610.21452 | Full-Duplex Interaction with Speech, Expressions and Gestures | 2026-10-15 | S. Wang | ELLSA 2 (abstract names "ELLSA 2") | match |
| 2603.17300 | ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies | 2026-03-18 | Z. Chen | 2026-03 | match |
| 2609.30913 | Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies | 2026-09-25 | Q. Wang | 2026-09 | match |
| 2609.05260 | One Word, Different Action: A Real-Robot Benchmark … | 2026-09-04 | Y. Liu | 2026-09 | match |
| 2609.28429 | Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams | 2026-09-23 | D. Yi | ARMS, 2026-09, CoRL 2026 (comment confirms) | match |
| 2609.24547 | MIRA: Real-Time Full-Duplex HRI for Embodied Companions | 2026-09-21 | L. Lin | 2026-09 | match |
| 2610.02360 | SocialVLA: A Social Perception Gateway … | 2026-10-01 | S. Konstantinova | 2026-10 | match |
| 2610.08862 | CIRRA: Dual-Level Continual Instruction Reconciliation … | 2026-10-05 | C. Zhang | 2026-10 | match |
| 2610.09451 | TempoBridge: Language-Guided Tempo Control for VLA Policies | 2026-10-07 | Y. Lee | 2026-10 | match |
| 2608.29967 | Training-Free Action Correction for VLA Model Failures via Language Feedback | 2026-08-30 | O. Kwon | CorrectVLA, 2026-08 | match |
| 2610.10534 | RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input | 2026-10-07 | Y. Zou | 2026-10 | match |
| 2606.10180 | Flow Control: Steering VLA Models with Simple Real-Time Inputs | 2026-06-08 | J. C. Kao | 2026-06 | match |
| 2605.12160 | Premover: Fast VLA Control via Early Execution During Instruction Delivery | 2026-05-12 (v2 2026-10-05) | J. Park | 2026-05; v2 2026-10 | match |
| 2610.20531 | EarlyCommit: Calibrated Word-by-Word Commitment … | 2026-10-14 | M. H. Khan | match | match |
| 2610.17977 | ReEnvision: Future-Guided Selective Action Repair … | 2026-10-13 | X. Zeng | match | match |
| 2610.14864 | Predict in Chunks, Revise in Spans … (CMAP) | 2026-10-10 | C. Wang | match | match |
| 2609.15012 | Atomic Motion Coordinate for Language-Steerable and Force-Responsive Manipulation | 2026-09-14 | J. Zhai | match | match |
| 2609.22587 | React When You Need To: Event-Triggered Asynchronous Inference for VLA Policies | 2026-09-18 | Y. Wu | match | match |
| 2609.21022 | Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs | 2026-09-17 | Y. Ji | VLA-Feedback | match |
| 2609.08230 | ActionSplice: In-Flight Action Editing for Interactive World Models | 2026-09-08 | P. Taghavi | match | match |
| 2607.01804 | VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon | 2026-07-02 | Y. Pan | draft flags "[U] ID not API-confirmed" | **match. Remove the [U] flag on the ID.** The SmolVLA-evaluation detail is still [S]: the abstract names no policies. |
| 2606.08881 | Benchmarking VLA Models on SO-101: Failure and Recovery Analysis | 2026-06-07 | Y. Yu | match (abstract lists π0.5, SmolVLA, Wall-X, ACT) | match |
| 2506.01844 | SmolVLA: A VLA Model for Affordable and Efficient Robotics | 2025-06-02 | M. Shukor | match | match |
| 2602.22818 | LeRobot: An Open-Source Library for End-to-End Robot Learning | 2026-02-26 | R. Cadene | match | match |

**Mismatches: none.** The secondary-index cross-check (OpenAlex/Semantic Scholar) was not run. Only the arXiv API record was matched (see residual risks).

## 3. High-stakes claim spot-checks (primary text)

| # | Draft claim | Status | Evidence (primary text) | Corrected text (if any) |
|---|---|---|---|---|
| C1 | SwitchVLA "advance interpolates in joint space toward the new task's canonical start pose; effective at next chunk" (§1, §3b, §5) | **corrected (nuance)** | arXiv HTML 2506.03574v1, method §: "advance (b_t=2): Interpolate linearly in joint space between the current action a_t^i and a canonical start pose a_0^normal, defined as the mean of initial trajectories for instruction l^cur … enabling rapid subtask switching under the assumption of no contact." This sits in the data-sampling/training-target section and is followed by "Action sequences are optimized using flow-matching loss". Timing: "After each action chunk is executed, the model updates l^pre ← l^cur … New instructions can be issued at any timestep, upon which the model re-evaluates b_t." | "SwitchVLA learns an *advance* mode. Its training targets interpolate linearly in joint space from the current action toward a canonical start pose (the mean initial pose) of the new instruction. The policy re-evaluates its behaviour mode when a new instruction arrives, and l_pre is updated after each executed chunk. That the switch takes effect at the next chunk is our inference." |
| C2 | SwitchVLA "MT-ACT baseline scores 0.0 on mid-switch (real WS1)" | **confirmed** | Table 3: MT-ACT WS1 No/Early/Mid/Late = 56.3 / 0.0 / 0.0 / 4.9 (WS2 mid also 0.0). | — |
| C3 | SwitchVLA "Code: Not released [V]" | **corrected** | The paper text gives no code URL. The research-B project-page check found no code link. Neither source states "not released". | "Code: not stated in paper; no code link on the project page (research-B)." |
| C4 | VITA-E "retract to initial pose via inverse action stack; authors list smoother transitions as future work" | **confirmed** | arXiv HTML 2510.21817v1: "a retraction mechanism is employed, which returns the robot to the initial pose by sequentially popping and executing inverse movements from a stored action stack". Conclusion: "while our current task-switching relies on a safe retraction to a neutral state, we plan to explore methods for achieving smoother and more efficient transitions". The platform is a Fourier GR2. SmolVLA is a trained manipulation baseline only. "ASR" has no match in the text, so the draft's [U] on ASR vs end-to-end holds. | — |
| C5 | Causeway real-robot pooled numbers 42.9→100 / 14.3→94.3 / 17.1→82.9 and "without put-down or re-grasp" | **confirmed** | PDF 2609.30913v1 Table II (xArm, π0.5 fine-tuned, 5 trials/cell, 7 ordered pairs): "Pooled 42.9 100 14.3 94.3 17.1 82.9" for Approach / Pre-grasp / After-A, bare vs ours. HTML §VI names the arm as "an xArm 6". Text: "re-routing a held bowl from plate to shelf without put-down or re-grasp". Also confirmed: latency "2.5–2.8× (102/75/128 → 253/187/362 ms)" on A100; "requiring per-architecture calibration"; "‖Δa‖ drops by one to two orders of magnitude" before contact. | Optional precision: the per-cell values are 5 trials each, and the paper's prose rounds the result as "pooled success to 82–100%". |
| C6 | ReSteer "real steering 33% vs 73% on π0.5 DROID" | **confirmed, with clarification** | arXiv HTML 2603.17300v1 §VI-B: "standard teleoperation finetuning (π0.5-FT) saturates single-task success at 90%, it yields only marginal improvements in steerability (33%) compared to the 7% of the zero-shot baseline … ReSteer achieves a 73% steering success rate—a 2.2× improvement over the finetuned baseline—while maintaining high single-task proficiency (85%)". Platform: "DROID platform and the π0.5 DROID checkpoint". Release: "We will release all code, data, and models". | Replace "steering success 33%→73% real [V via alphaXiv report]" with "real-robot steering success 73% vs 33% for teleop-fine-tuned π0.5 (7% zero-shot π0.5-DROID) [V primary]". Change the code entry from "commitment to release [S]" to "authors state they will release code, data and models [V]". |
| C7 | Reflex "instruction 'computed once' and 'permanently pinned' in KV cache"; SmolVLA appendix 2.29× | **confirmed** | arXiv HTML 2607.14695v1 §3.1: "The Static Prefix contains system instructions ℓ1:L that defines the task; these are computed once and permanently pinned in the KV-cache." App. D.7: "SmolVLA … (500M parameters) … Reflex still achieves a consistent 2.29× speedup". Code: github.com/9yc/Reflex. | — |
| C8 | DREAM-Chunk SmolVLA on SO-101: USB 75→95%, moving object 60→80% | **confirmed** | PDF 2606.18589v1 Table 1 ("Success rates over 20 rollouts on three SO-101 tests with SmolVLA"): USB unplug/insert 75%→95%, Pick moving object 60%→80%, Pick and insert toy 35%→45%. N=10 candidates. | Optional: add "(20 rollouts/task; third task 35→45%)". |
| C9 | FutureRTC SmolVLA-450M LIBERO: RTC 69.7% at d=5, ours 75.8%; "real (Hang Cups)" | **numbers confirmed; real-robot scope corrected** | PDF 2607.24008v1 Table 1, SmolVLA-450M d=5: RTC "69.7 / 208.1", Ours "75.8 / 198.7". The real-world figure shows three tasks: "Stack Plates, Fold Towel, Hang Cups", with π0.5 as the backbone. Project site in the arXiv comment: https://jianghaiscu.github.io/FutureRTC_proj/ (HTTP 200). | "Kinetix + LIBERO + real (Stack Plates, Fold Towel, Hang Cups; π0.5)". Code column: "Project website https://jianghaiscu.github.io/FutureRTC_proj/ (code status not checked)". |
| C10 | MIRA "VAD barge-in → abort, 466 ms speech-start→abort" | **corrected (precision)** | arXiv HTML 2609.24547v2 Table 3: "speech_started → abort_cmd_sent 466 ms". Text: "the preemption latency is 466 ms at the median, measured from speech onset (speech_started) to abort-command dispatch (abort_cmd_sent)". VAD gate "450 ms interruption-confirmation threshold". "safe physical halting" is confirmed. | "MIRA (VAD barge-in → abort; median 466 ms from speech onset to abort-command dispatch)". |
| C11 | SocialVLA "336 ms gate-to-hold"; "remains paused until the participant explicitly requests continuation"; revision for "a subsequent VLA action" | **confirmed** | arXiv HTML 2610.02360v1 and abstract: "median VLA-gate-to-physical-hold latency is 336 ms". §III-H: "The robot remains paused until the participant explicitly requests continuation … or provide a revised instruction for a subsequent VLA action." Vosk confirmed; platform is Unitree G1 with a GR00T policy. | — |
| C12 | ELLSA "'Action Cancelled' + stop, LIBERO sim" | **confirmed** | arXiv HTML 2510.16756v2: "If the input is an interruptive command, ELLSA is expected to respond with 'Action Cancelled' and immediately stop the action (action barge-in)." Action expert: Emu3-Base with FAST tokenizer. No real-robot evaluation found. | — |
| C13 | LeRobot inference.mdx L419 quote; commit 146d847 dated 2026-10-16 | **confirmed verbatim** | raw `docs/source/inference.mdx` line 419: "…On a robot supporting local hold, the engine invalidates queued/interpolated motion, waits for the control loop to acknowledge the hold, then requests fresh motion under the new task. Expect a stop during this transition; it is not a guaranteed continuous blend. A change between requests can retain already accepted actions for continuity. Local RTC on a robot without hold support still discards the obsolete result, but can exhaust its remaining actions and terminate." GitHub API main sha `146d8474932c8b566717eb2738ba459337ab71c4`, date 2026-10-16T11:55:57Z. Other quotes also confirmed: `controller.set_task("grab the red cube")  # re-instruct mid-run`; `/subtask` "may enter a planned hold … Only affects policies that condition on language (SmolVLA, π0/π0.5, and similar)". | — |
| C14 | LeRobot README "Immediate planned language wait — discards continuation and can disrupt task progress"; "Buffered motion during informational VQA" as extension | **confirmed** | raw `src/lerobot/remote_inference/README.md`: "Immediate planned language wait \| Simple serialized state; discards continuation and can disrupt task progress. Buffered VQA is a priority." Also: "**Buffered motion during informational VQA** \| Priority follow-up to reduce observed task discontinuity…". The policy table includes "SmolVLA \| … guided RTC supported" and "ACT \| Current observation, temporal ensembling disabled." | The draft calls it "a potential extension"; the README calls it a "priority follow-up". The stronger wording raises the infrastructure-scoop risk. |
| C15 | remote_inference.mdx "Instruction change during inference: Discard the old prediction, pause and obtain fresh actions…"; async_inference retired | **confirmed** | raw `docs/source/remote_inference.mdx` table row and "Migrating from lerobot[async]" block, verbatim. | — |
| C16 | πR² quote "struggles to recover from failures because previously generated in-flight actions bias the policy toward continuing its recent motion" | **confirmed** | arXiv HTML 2607.26055v1 results §: "We observe that RTC also struggles to recover from failures because previously generated in-flight actions bias the policy toward continuing its recent motion". | — |
| C17 | RAVEL holds "the same … language instructions" fixed | **confirmed** | PDF 2609.34170: "All methods use the same task configurations, environment seeds, and language instructions." | — |
| C18 | VLASH real SO-101 with π0.5/GR00T; SmolVLA in LIBERO only | **confirmed** | PDF 2512.01031v2: real experiments use "π0.5 and GR00T N1.6 on … Galaxea R1 Lite and the LeRobot SO-101"; LIBERO Table I includes SmolVLA (delay 3: 79.1% vs sync 79.0%). | — |
| C19 | Hi Robot: Whisper large-v2 ASR; high-level re-triggered immediately on intervention | **confirmed** | arXiv HTML 2502.19417v2 §4.2: "these interventions take the form of text commands or spoken language (which is then transcribed into text). When the system receives a user intervention, the high-level inference is triggered immediately"; App. B.1: "Whisper large-v2". | — |
| C20 | Premover waits on ambiguous prefix; SmolVLA only cited | **confirmed** | arXiv HTML 2605.12160v2 App. C: "the robot remains still and waits for the next word before checking again". SmolVLA appears only in related work and the references. | — |
| C21 | EarlyCommit "no physical robot … a commit is never revised" | **confirmed** | arXiv HTML 2610.20531v1 limitations, verbatim. | — |
| C22 | ARMS hard-interrupt ablation FG continuation 76→41; speech not shown | **confirmed** | arXiv HTML 2609.28429v2: "Replacing asynchronous concurrency with a hard interrupt … (76→41, 78→38)". No match for "speech", so the draft's [U] stands. "We will publicly release ARMS Dataset and the construction code". | — |
| C23 | SmolVLA latency ~99 ms on RTX 4090; async vs sync success 73.3 vs 78.3 | **confirmed; add citation** | arXiv HTML 2602.22818v1 Table 3: SmolVLA "99.244 ± 1.195" ms on RTX 4090. Table 5(a): Sync 75/90/70 avg 78.3; Async 80/90/50 avg 73.3. The 9.70 vs 13.75 s and 19 vs 9 cube numbers sit in table images and could not be text-matched; they rest on research-D only. | §5 "~99 ms on RTX 4090 [V]" should cite LeRobot paper 2602.22818 Table 3. |
| C24 | DiscreteRTC "Website (URL not extracted) [U]" | **corrected** | The arXiv abstract gives https://outsider86.github.io/DiscreteRTCSite/ (HTTP 200). "~0.7 computation" is confirmed in the abstract. | Code column: "Website https://outsider86.github.io/DiscreteRTCSite/ (code status not checked)". |
| C25 | VLA-Corrector "ID not API-confirmed [U]" (§3b, Sources) | **corrected** | arXiv API returns 2607.01804 = "VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon", 2026-07-02, Y. Pan et al. The abstract confirms truncation + Online Gradient Guidance replanning. | Use https://arxiv.org/abs/2607.01804 and drop "[U ID]". Keep "[S]" for "evaluated on SmolVLA" (the abstract names no policies). |
| C26 | "≥8 directly adjacent papers 2026-09-01 to 2026-10-15" | **confirmed** | v1 dates per the API: Causeway 09-25, ARMS 09-23, CIRRA 10-05, MIRA 09-21, SocialVLA 10-01, RoboPrompt 10-07, EarlyCommit 10-14, REACT 10-08. | — |

**Not re-checked against primary text.** These rest on the research files only, which mark them [V] or [V report]:
- DiscreteRTC real UR5e
- Soft RTC real details
- ChunkFlow
- FASTER
- Training-time RTC details
- Reactive RT Flow "SmolVLA all experiments"
- REACT/FreeBar hardware
- Hi Robot platforms
- CIRRA
- TempoBridge
- CorrectVLA
- RoboPrompt
- Flow Control ("π0.5-DROID, 16-user study" is [V report] from the research files and was not seen by me)
- One Word Different Action
- the LeRobot code-level line numbers other than inference.mdx L419

None of these was contradicted by the API abstracts I read.

## 4. Source URL resolution (curl -L, 2026-10-18)

### arXiv abstract pages: all 42 returned HTTP 200
2506.07339, 2512.05964, 2604.25050, 2605.25537, 2603.19199, 2607.12992, 2607.14695, 2607.24008, 2607.26055, 2512.01031, 2609.34170, 2609.36540, 2610.12007, 2610.14997, 2606.18589, 2506.03574, 2502.19417, 2510.21817, 2510.16756, 2610.21452, 2603.17300, 2609.30913, 2609.05260, 2609.28429, 2609.24547, 2610.02360, 2610.08862, 2610.09451, 2608.29967, 2610.10534, 2606.10180, 2605.12160, 2610.20531, 2610.17977, 2610.14864, 2609.15012, 2609.22587, 2609.21022, 2609.08230, 2606.08881, 2506.01844, 2602.22818 — all `https://arxiv.org/abs/<id>` → 200.

### Other URLs
| URL | Status |
|---|---|
| https://www.alphaxiv.org/abs/2607.01804 | 200 (prefer https://arxiv.org/abs/2607.01804, which is now confirmed) |
| https://github.com/Physical-Intelligence/real-time-chunking-kinetix | 200 |
| https://github.com/innovator-zero/FASTER | 200 |
| https://github.com/9yc/Reflex | 200 |
| https://pi-r2-flow.github.io/ | 200 |
| https://github.com/mit-han-lab/vlash | 200 |
| https://react-vla.github.io | 200 |
| https://github.com/NamelessCrew/FreeBar | 200 |
| https://github.com/Tencent/VITA/tree/VITA-E | 200 |
| https://github.com/yanwen-zou/Roboprompt | 200 |
| https://github.com/bytedance/SALMONN/tree/ELLSA | 200 on an HTTP status check only. Content not read; the fetch tool previously reported ROBOTS_DISALLOWED, so it was not fetched. |
| https://cytoderm-ai.github.io/chunkflow | **404** (as the draft states) |
| https://innovator-zero.github.io/FASTER | **404** (as the draft states) |
| https://jianghaiscu.github.io/FutureRTC_proj/ | 200 (new; add to the draft) |
| https://outsider86.github.io/DiscreteRTCSite/ | 200 (new; add to the draft) |
| https://resteer-vla.github.io/ | 200 (new; optional) |
| https://wenxichen2746.github.io/DREAM-Chunk/ | 200 |
| https://gagajian.github.io/MIRA/ | 200 |
| https://switchvla.github.io | 200 |
| https://github.com/huggingface/lerobot | 200 |
| https://github.com/huggingface/lerobot/blob/main/docs/source/inference.mdx | 200; quote confirmed at L419 via raw.githubusercontent.com |
| https://github.com/huggingface/lerobot/blob/main/docs/source/remote_inference.mdx | 200; quote confirmed |
| https://github.com/huggingface/lerobot/blob/main/src/lerobot/remote_inference/README.md | 200; quotes confirmed |
| https://github.com/huggingface/lerobot/blob/main/docs/source/rtc.mdx | 200 (content not re-read) |
| https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/rtc.py | 200 (content not re-read) |
| https://github.com/huggingface/lerobot/tree/v0.6.1/src/lerobot/async_inference | 200 (content not re-read) |

## 5. Citation-structure notes for the draft

- The draft uses status flags ([V]/[S]/[U]) and an unnumbered Sources list rather than numbered inline citations. Every arXiv paper named in the body appears in Sources, and every Sources entry is mentioned in the body. So there are no orphans by name, but no `[N]` mapping exists either.
- §5 "~99 ms on RTX 4090 [V]" has no paper attribution. Attribute it to LeRobot 2602.22818 Table 3.
- §3c "Paper numbers … [V, 2506.01844 / 2602.22818]": the success numbers are confirmed. The completion-time and cube numbers depend on research-D.
- **Wording that outruns evidence:**
  - Bullet 2 says "[V for all 10 papers read in research-A plus RTC, πR², FutureRTC, DiscreteRTC]". Research-D read only the RTC paper's abstract. The lead notes say RTC was checked via alpha_ask_paper, but this session did not re-verify the "no instruction change" absence for RTC.
  - The universal "none treats a changed instruction as a trigger" across "≥12 descendants" is an absence claim from keyword search. Keep it as "none found".

## Blocked sources

- None blocked by robots.txt, paywall or login in this verification run.
- The ELLSA GitHub page was recorded earlier as ROBOTS_DISALLOWED for the fetch tool. I did **not** fetch its content; only the HTTP status was observed.
- Unavailable: the ChunkFlow and FASTER project pages (404).
- Tool limitations:
  - `alpha_get_paper` / `alpha_ask_paper` were not exposed, so arXiv HTML/PDF primary text was used instead.
  - Causeway, DREAM-Chunk and FutureRTC tables were missing from the HTML extraction, so their PDFs were used.
