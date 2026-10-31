# Mid-motion instruction handling, R3: RTC, LeRobot async inference / SmolVLA, ACT, VLASH note

Date: 2026-10-18. Tags: **[V]** means I read it in the primary text (paper full text through `feynman alpha ask/get` or arXiv HTML, or source code through `feynman alpha code` / raw GitHub). **[S]** means secondary. **[U]** means my inference or unverified. The numbers below are quoted from the sources.
Tool note: the `alpha_*` tools named in the task were reached through the `feynman alpha` CLI (`ask`, `get`, `code`). The `alpha get` output for 2506.07339 was an AI-written overview, so I used only the raw page text that `alpha ask` returns, plus the arXiv HTML.

## Evidence table

| # | Source | URL | Key claim | Type | Conf. |
|---|---|---|---|---|---|
| 1 | Black, Galliker, Levine, RTC (NeurIPS 2025) | https://arxiv.org/abs/2506.07339 | Async chunking framed as inpainting: the first d actions are frozen and soft-masked guidance is applied over the H−s overlap | primary | high |
| 2 | RTC Kinetix repo | https://github.com/Physical-Intelligence/real-time-chunking-kinetix | Sim-only code; checkpoints in `gs://rtc-assets/` | primary (code) | high |
| 3 | LeRobot main @146d847 (2026-10-16), `remote_inference/`, `inference/`, `policies/rtc/` | https://github.com/huggingface/lerobot | Current async stack: task versioning, a planned hold on instruction change, and guided RTC for SmolVLA | primary (code) | high |
| 4 | LeRobot v0.4.0 `async_inference/` (legacy) | https://github.com/huggingface/lerobot/tree/v0.4.0/src/lerobot/async_inference | `chunk_size_threshold`, `aggregate_fn_name`, task fixed per run | primary (code) | high |
| 5 | Shukor et al., SmolVLA | https://arxiv.org/abs/2506.01844 | 450M parameters, n=50; async ~30% faster on SO100 | primary | high |
| 6 | Zhao et al., ACT/ALOHA | https://arxiv.org/abs/2304.13705 | ~80M parameters, temporal ensemble w_i=exp(−m·i), 0.01 s inference on a 2080 Ti | primary | high |
| 7 | Tang et al., VLASH | https://arxiv.org/abs/2512.01031 | "SmolVLA implements naive asynchronous inference by directly switching to new action chunks" | primary (claim about [5]) | high (that VLASH says it) |
| 8 | lerobot/smolvla_base weights | https://huggingface.co/lerobot/smolvla_base | `model.safetensors` is 906,712,520 bytes | primary | high |

## Comparison table

| Field | (1) RTC [1][2] | (2a) LeRobot async (current main) + SmolVLA [3][5] | (2b) Legacy LeRobot async v0.4.0 [4] | (2c) ACT [6][3] |
|---|---|---|---|---|
| (a) Trigger / entry | **Observation** only. No language-change trigger is studied. The prompt is part of the π0.5 input [U] | **Typed text**, entered with `/subtask <text>` on stdin (`rollout/interactive.py`) or `set_task()`. It is tokenized as the VLA prompt. No speech or ASR | Text `--task` set once on the CLI | **None.** ACT has no language input (no task/language use in `modeling_act.py`) [V-code, absence by grep] |
| (b) At interruption | Keeps executing. The d actions already committed are frozen, then the new chunk swaps in ("Swap to the new chunk as soon as it is available") | **Hold** if inference is in flight, otherwise old buffered actions **finish** (see below) | Not supported mid-episode. Overlaps are aggregated by weighted average | No instruction channel. With temporal ensembling, blends every step |
| (c) Repair | Guidance inpainting toward the previous chunk | Fresh request from a post-hold observation, then aligned/blended/RTC merge | `aggregate_fn` on overlapping timesteps | Not applicable |
| (d) Latency | 76 ms vanilla / 97 ms RTC (model, RTX 4090). 108.76–138.98 ms total | Not quantified in code. Paper: 9.7 s vs 13.75 s task time | Not applicable | "around 0.01 seconds" (2080 Ti) |
| (e) Backbone | π0.5. "VLM backbone (3B parameters)" plus "action expert (300M parameters)"; H=50 real, H=8 sim | SmolVLA 450M (~100M expert), flow matching, n=50, `chunk_size: int = 50` | Any of `act, smolvla, diffusion, tdmpc, vqbet, pi0, pi05` | ~80M CVAE transformer; `chunk_size: int = 100` default |
| (f) Robot / sim | Bimanual, two 6-DoF arms; Kinetix, 12 tasks | SO100 (3 tasks) + SO101; LIBERO, Meta-World | SO100/SO101 | ALOHA (ViperX); 2 sim tasks |
| (g) Human study | None | None | None | N=6 teleoperation study (not about policy interruption) |
| (h) Code / weights | Sim code yes. Real-robot code not in that repo. Kinetix checkpoints on GCS | Code yes; `lerobot/smolvla_base` weights yes | Code at tag v0.4.0 | Code in LeRobot; trained per task, no general weights |
| (i) GPU | Inference on RTX 4090; fine-tuning 8×H100 | Not stated for inference; "4 GPUs" for pretraining, ~30k GPU-h | Not applicable | 11 GB RTX 2080 Ti |
| (j) Fits 8 GB? | Unlikely or tight for π0.5 + RTC backprop [U]; 48 GB fine | Yes [U] (~0.9 GB weights file) | Yes | Yes |

## Notes per system

### (1) Real-Time Chunking (RTC), arXiv 2506.07339 [1][2]

- **Mechanism [V].**
  - "The first d actions from the new chunk cannot be used, since those timesteps will have already passed by the time the new chunk becomes available. Thus, it makes sense to 'freeze' those actions to the values that we know will be executed."
  - Soft mask (Eq. 5): "The first d actions get a weight of 1; the last s actions of the new chunk … get a weight of 0; the actions in between get weights that exponentially decay from 1 to 0."
  - Guidance is ΠGDM with weight clipping β. Hyperparameters (Table 4): n=5, H=8 (sim) / 50 (real), s_min=25 (real), β=5, delay buffer b=10. The delay is estimated as `d = max(Q)` ("conservatively").
- **When the observation changes mid-chunk [V].** "the new chunk should still incorporate new observations, so that the policy does not lose the ability to react and make corrections." Execution never stops. Algorithm 1: "A_cur = A_new ▷ Swap to the new chunk as soon as it is available."
- **Instructions [U].** The paper never changes the language instruction. A prompt change would be just another conditioning change: it can take effect only after ≥ d steps, and the guidance actively pulls the overlap region toward the *old* plan.
- **Latency [V].**
  - Model latency: "76ms for the baselines and 97ms for RTC". LAN "adds 10-20ms", giving "d ≈ 6". Injected +100/+200 ms gives "d ≈ 11 and d ≈ 16".
  - Table 3: SigLIP 18 ms, "LLM prefill (Gemma 2B) 44ms", denoising ×5 = 14 ms → 35 ms with RTC. "RTC incurs a 2.5x latency increase per denoising step."
  - Table 2 totals: "138.98 ± 6.71ms" (mobile), "108.76 ± 2.34ms" (non-mobile). Hardware: "All of our real-world inference is done on a single NVIDIA RTX 4090 GPU." The headline claim is robustness to "inference delays in excess of 300 milliseconds".
- **Robot and baselines [V].** Bimanual system with "two 6-DoF arms and parallel jaw grippers". 6 tasks, "480 episodes", 28 h. Baselines: Synchronous (s=25, pauses), TE sparse/dense, and BID in simulation.
- **Human study.** None [V].
- **Code [V].** "The code for the simulated experiments is available at …real-time-chunking-kinetix". The repo contains `src/{eval_flow,train_flow,train_expert,generate_data,model}.py` and 12 `worlds/l/*.json`. The README also covers "Training-Time RTC" (arXiv 2512.05964; not read here).
- **SO-101 applicability [U].** Policy-agnostic for any flow/diffusion chunker ("applicable only to diffusion- and flow-based policies" [V]). That means SmolVLA (flow matching) qualifies and **ACT (CVAE, deterministic decode) does not**.
- **Key claim + caveat.** RTC gives smooth, delay-robust async execution with no retraining. Caveat: it is designed for continuity, not for retargeting. Freezing and guidance resist abrupt task switches [U].

### (2) LeRobot async inference, SmolVLA, ACT [3][4][5][6]

**Repo state.** At main HEAD `146d847` (2026-10-16), `src/lerobot/async_inference/` no longer exists (alpha code: "Path not found"). It was replaced by `src/lerobot/remote_inference/` (Zenoh client/server; `scripts/lerobot_policy_server.py`) plus `src/lerobot/inference/{sync,rtc,base,execution}.py` and `src/lerobot/rollout/` [V]. The legacy names exist only at tags such as v0.4.0 [4].

**Legacy v0.4.0 [V, 4]**
- `robot_client.py`: `_ready_to_send_observation()` returns `action_queue.qsize() / action_chunk_size <= self._chunk_size_threshold` (default `chunk_size_threshold: float = 0.5`).
- `_aggregate_action_queues` merges same-timestep actions using `aggregate_fn`.
- `configs.py`, `AGGREGATE_FUNCTIONS`:
  - `"weighted_average": 0.3*old + 0.7*new` (the default)
  - `"latest_only"`
  - `"average"`
  - `"conservative": 0.7*old + 0.3*new`
- The task enters via `raw_observation["task"] = task`, and `client.control_loop(task=cfg.task)` fixes it for the whole run. There is **no mid-episode task change**.
- `constants.py`: `SUPPORTED_POLICIES = ["act", "smolvla", "diffusion", "tdmpc", "vqbet", "pi0", "pi05"]`; `SUPPORTED_ROBOTS` includes `so101_follower`.

**Current main [V, 3]**
- **The instruction can change mid-episode.** `/subtask <text>` comes from `rollout/interactive.py` ("chat-style stdin commands") and goes to `RolloutController.set_task`, which is documented as "effective from the next inference". `README.md` §9: "Tasks carry a version … In-flight obsolete task results cannot execute. Supported in-flight retargets use a planned wait and fresh resumption; between-request changes can preserve eligible continuity."
- **Sync engine (`inference/sync.py`).** On a task change: "Chunking policies queue actions computed under the previous instruction, so drop them and let the new one take effect on this tick" → `self._policy.drop_queued_actions()`. That is an **immediate switch**, after one inline inference [V]. The likely brief stall of one forward pass is [U].
- **Local RTC (`inference/rtc.py`, `set_task`).** "Retarget an in-flight prediction through a planned hold when supported. Old-task results remain invalid." The hold is requested only if the pending request's `task_version` is stale and the robot `supports_hold`.
- **Remote (`remote_inference/engine.py`, `set_task`).** "Accept a changed instruction, holding if action inference is pending … Actions already accepted can retain continuity, but pending results for the old task cannot be accepted."
- **What the hold does (README §8).** "`ThreadSafeRobot` retains the complete finite position target returned by the driver after a send … Target retention may still allow the robot to settle toward that target; it does not prove instantaneous stillness." "SO/OMX, Koch, HopeJr and Rebot support this contract."
- **Merging.**
  - Append: "Plain append executes the current chunk and then its accepted successor".
  - Alignment trims the consumed prefix ("The currently committed/interpolating endpoint cannot be replaced").
  - Blending: `blended = q_t + b_w * (i_t - q_t)`.
  - RTC: "conditions prediction on an ongoing model-space continuation rather than averaging".
  - The refill threshold is `effective_refill = max(refill_seconds, recent_max_turnaround + action_interval)`.
- **RTC support.**
  - Sources list: "Source declarations allow RTC for SmolVLA, π0, π0.5, FineART, EVO1, GR00T and continuous MolmoAct2".
  - Policy table: "SmolVLA … guided RTC supported", with evidence "Remote HW and local guided RTC: `imstevenpmwork/super_chatton_smolvla`". ACT: "Current observation, temporal ensembling disabled."
  - `policies/rtc/configuration_rtc.py` defaults: `mode="guided"`, `prefix_attention_schedule=LINEAR` ("# Todo change to exp"), `max_guidance_weight=10.0`, `execution_horizon=10`. Note that the default is linear, not the paper's exponential schedule [V].
- **Hardware caveat [V].** "Fresh replanning can lose task progress, as observed on hardware; resumed motion alone does not establish task continuity."

**SmolVLA paper [V, 5]**
- **Size.** "Our main model, contains 450 million parameters, with approximately 100 million dedicated to the action expert". "chunks of n=50 actions"; 10 flow steps.
- **Async control.** Algorithm 1 triggers on "|A_t|/n < g". Queues stay non-empty when "g ≥ (E[ℓ_S]/Δt)/n", with Δt = 33 ms. At "g = 0.7" the result is "obtained aggregating queues on the overlapping timesteps". Near-duplicate observations are dropped by a joint-space threshold ϵ.
- **Async results (SO100 Pick-Place).**
  - "completes the task in 9.7 seconds, compared to 13.75 seconds … (∼ 30% faster)".
  - "19 successful pick-and-place cycles, compared to only 9".
  - Success Sync 78.3 vs Async 73.3 average (Sorting 70→50).
- **Real-robot evaluation mode.** Other real-world results used synchronous inference.
- **Compute.**
  - "designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs".
  - "Pretraining was conducted using 4 GPUs … approximately 30k GPU hours".
  - "consumes 6× less memory" than π0.
  - No GPU model and no absolute memory are stated.
- **Robots.** "three datasets using the SO-100 robot arm and 1 with SO-101".

**ACT paper [V, 6]**
- "The model has around 80M parameters … training takes around 5 hours on a single 11G RTX 2080 Ti GPU, and the inference time is around 0.01 seconds".
- Temporal ensemble: "weighted average … w_i = exp(−m ∗ i), where w_0 is the weight for the oldest action … smaller m means faster incorporation." Success rises "from 1% at k=1 to 44% at k=100".
- LeRobot `configuration_act.py` notes "the value used in ACT when temporal ensembling is enabled is 0.01". It requires `n_action_steps == 1` with ensembling [V].

**Applicability [U]**
- On SO-101 at 8 GB, the current LeRobot stack gives versioned task injection, hold-on-retarget and guided RTC for SmolVLA essentially for free.
- The *policy-agnostic* parts are: task versioning, hold, alignment/blending, and the queue threshold.
- *Backbone-specific* parts are: RTC (flow only) and the language conditioning itself (SmolVLA only; ACT would need a separate per-task model or a language-conditioning modification).

### (3) VLASH note [V, 7]

"SmolVLA [5] implements naive asynchronous inference by directly switching to new action chunks, but this leads to notable prediction-execution misalignment and unstable control. Real-time Chunking (RTC) [4] mitigates this by freezing actions…" (confirmed in 2512.01031v2, §1).

Nuance [V/U]: the legacy v0.4.0 *default* aggregation was `weighted_average` (0.3 old + 0.7 new), with `latest_only` as an option. "Directly switching" therefore matches the paper's description and `latest_only`, but not the code default exactly.

## What physically happens if a new task string is injected mid-chunk

- **RTC (paper) [U]:** The arm keeps moving. ≥ d actions under the old plan execute, then the overlap region is guided toward the old chunk. The new task can steer freely only in the last s actions, so the redirect is delayed and smoothed with no pause. The paper does not test this.
- **LeRobot v0.4.0 async [V/U]:** The API cannot change the task mid-run [V]. If hacked in, the next chunk would be averaged (0.7 new) into the remaining queue, with no hold [U].
- **LeRobot main, sync engine (ACT or SmolVLA) [V]:** Queued actions are dropped and the policy re-infers this tick with the new task. This is an immediate switch; any pause equals one forward pass [U]. For ACT the string has no effect on actions (no language input).
- **LeRobot main, local RTC / remote, inference in flight [V]:** The planned hold retains the last driver position target. The old-task result is discarded, and motion resumes from a fresh post-hold observation under the new task.
- **LeRobot main, no request in flight [V]:** Already-accepted old-task actions may keep executing ("can preserve eligible continuity"). The next request uses the new task and is merged by alignment/blend/RTC.
- **SmolVLA paper async (per VLASH) [V]:** It switches directly to the new chunk when it arrives, with no hold.

## Coverage Status

- **Done:**
  - RTC: paper text plus repo root/README.
  - LeRobot main: remote_inference README/engine, inference/base/sync/rtc, rollout/interactive, policies/act/smolvla/rtc.
  - LeRobot v0.4.0: async_inference robot_client/configs/constants.
  - SmolVLA and ACT papers.
  - VLASH quote.
- **Not done / uncertain:**
  - RTC pages 4–5 were missing from `alpha ask` output (recovered from arXiv HTML).
  - No measured LeRobot hold/retarget latency.
  - π0.5 VRAM on 8 GB not measured [U].
  - ACT Table III final k / m not extracted.
  - Training-time RTC (2512.05964) not read.

## Blocked sources

- None encountered in this run. Per instruction, I did not access ELLSA `github.com/bytedance/SALMONN` (known ROBOTS_DISALLOWED).
- `feynman alpha code` cannot read git tags. For v0.4.0 I used raw.githubusercontent.com, which was not blocked.

## Sources

1. Black, Galliker, Levine. Real-Time Execution of Action Chunking Flow Policies. https://arxiv.org/abs/2506.07339 (HTML: https://arxiv.org/html/2506.07339v2)
2. Physical-Intelligence/real-time-chunking-kinetix. https://github.com/Physical-Intelligence/real-time-chunking-kinetix
3. huggingface/lerobot main @146d847. https://github.com/huggingface/lerobot (files: `src/lerobot/remote_inference/README.md`, `remote_inference/engine.py`, `inference/{base,sync,rtc}.py`, `rollout/interactive.py`, `policies/rtc/{configuration_rtc,action_queue}.py`, `policies/act/{configuration,modeling}_act.py`, `policies/smolvla/configuration_smolvla.py`, `policies/pretrained.py`); commit https://github.com/huggingface/lerobot/commit/146d8474932c8b566717eb2738ba459337ab71c4
4. LeRobot v0.4.0 async_inference. https://raw.githubusercontent.com/huggingface/lerobot/v0.4.0/src/lerobot/async_inference/robot_client.py , …/configs.py , …/constants.py
5. Shukor et al. SmolVLA. https://arxiv.org/abs/2506.01844
6. Zhao et al. Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT). https://arxiv.org/abs/2304.13705
7. Tang et al. VLASH. https://arxiv.org/abs/2512.01031
8. lerobot/smolvla_base. https://huggingface.co/lerobot/smolvla_base
