# G2 — Mid-motion repair: LeRobot code/infrastructure check (research-D)

Date of check: 2026-10-18. Scope: async inference, language-task plumbing, RTC, queue semantics, ACT temporal ensembling in `huggingface/lerobot`, plus what the LeRobot (2602.22818) and SmolVLA (2506.01844) papers say about async inference.

Flags: **[V]** = verified from primary text (code file read or paper text returned by `feynman alpha ask`); **[S]** = secondary; **[U]** = unverified / inference. Code-derived *inferences* (behaviour I deduced by reading code paths, not a stated claim or a test I ran) are marked **[V-code→inference]**.

## Method / provenance

- `alpha_read_code` / `alpha_ask_paper` were not exposed as callable functions in this session. I used the equivalent CLI commands `feynman alpha code https://github.com/huggingface/lerobot <path>` and `feynman alpha ask <arXiv-id> "<question>"`. alphaXiv was logged in.
- `feynman alpha code` reads only the default branch. It lists `src/lerobot/{inference,remote_inference,policies,rollout}` and returns file bodies identical to the clone below (for example, `def set_task` and "Retarget an in-flight prediction" appear in both). To grep and get line numbers I also made shallow git clones:
  - **main** @ `146d8474932c8b566717eb2738ba459337ab71c4` (commit date Fri Oct 16 2026) — the "current" code.
  - **tag v0.6.1** @ `7e241bd630a3719a56157a497ce5d08f244784f1` (Mon Aug 3 2026). This is the last release that still has `src/lerobot/async_inference/` (`policy_server.py`, `robot_client.py`). `alpha code` returned "Path not found" for tag URLs, so the tag was read from the clone only.
- arXiv IDs 2602.22818, 2506.01844 and 2506.07339 were confirmed with the arXiv API (`feynman_science_database_search`, source=arxiv) → **[V]** IDs.

> **Headline finding [V]:** the old `async_inference` stack (PolicyServer/RobotClient, `chunk_size_threshold`, `aggregate_fn_name`) has been **retired on main**. It was replaced by `lerobot.inference` (local `sync` / `rtc` engines) and `lerobot.remote_inference` (Zenoh-based `lerobot-policy-server` + `lerobot-rollout --inference.type=remote`). `docs/source/remote_inference.mdx` (§"Migrating from lerobot[async]") says: *"The retired `lerobot[async]` extra and `lerobot.async_inference` commands are replaced by `lerobot[remote]`, `lerobot-policy-server` and `lerobot-rollout --inference.type=remote`. The old chunk-size thresholds and aggregation weights are not interchangeable with refill, alignment and blending."* Any paper text that describes "PolicyServer/RobotClient with threshold g and aggregation f" now describes **legacy code (≤ v0.6.1)**.

---

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|---|---|---|---|---|
| 1 | LeRobot main: `src/lerobot/remote_inference/README.md` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/remote_inference/README.md | Design reference for the current async/remote inference: backends sync/rtc/remote, ChunkRuntime, append/aligned/blend/RTC, the policy-support table, task versioning and "immediate planned language wait" | primary (code docs) | high |
| 2 | LeRobot main: `docs/source/remote_inference.mdx` | https://github.com/huggingface/lerobot/blob/main/docs/source/remote_inference.mdx | async_inference retired; instruction change during inference → discard + pause + fresh actions | primary (docs) | high |
| 3 | LeRobot main: `docs/source/inference.mdx` | https://github.com/huggingface/lerobot/blob/main/docs/source/inference.mdx | `/subtask <text>` changes the instruction mid-run; `RolloutController.set_task()` library API; "Expect a stop during this transition; it is not a guaranteed continuous blend" | primary (docs) | high |
| 4 | LeRobot main: `src/lerobot/inference/rtc.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/rtc.py | `RTCInferenceEngine.set_task` (L308–335) requests a hold when a request is pending; `_rtc_loop` (L497+) passes queue leftover as `model_continuation` with `inference_delay` | primary (code) | high |
| 5 | LeRobot main: `src/lerobot/inference/execution.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/execution.py | `ChunkRuntime.invalidate` clears the queue; `should_request` bypasses the threshold on task change only for `aligned`; `accept` rejects results whose task_version is stale; `estimate_delay` | primary (code) | high |
| 6 | LeRobot main: `src/lerobot/policies/rtc/action_queue.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/policies/rtc/action_queue.py | RTC enabled → `_replace_actions_queue` (replace queue, drop first `delay`); RTC disabled → `_append_actions_queue` | primary (code) | high |
| 7 | LeRobot main: `src/lerobot/policies/rtc/modeling_rtc.py`, `configuration_rtc.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/policies/rtc/modeling_rtc.py | Guided RTC = Jacobian guidance toward `prev_chunk_left_over` with prefix weights (ZEROS/ONES/LINEAR/EXP); defaults `max_guidance_weight=10.0`, `execution_horizon=10`, mode `guided`\|`trained` | primary (code) | high |
| 8 | LeRobot main: `docs/source/rtc.mdx` | https://github.com/huggingface/lerobot/blob/main/docs/source/rtc.mdx | RTC for Pi0, Pi0.5, SmolVLA; `trained` mode "currently requires a Pi05 checkpoint trained with `policy.rtc_training_max_delay > 0`" | primary (docs) | high |
| 9 | LeRobot main: `src/lerobot/inference/base.py`, `remote_inference/engine.py`, `rollout/controller.py`, `rollout/interactive.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/base.py | `set_task()` + monotonic `task_version` on every engine; remote `set_task` holds if pending; controller `set_task` stops autosteer | primary (code) | high |
| 10 | LeRobot main: `src/lerobot/policies/act/modeling_act.py`, `configuration_act.py`, `policies/pretrained.py` | https://github.com/huggingface/lerobot/blob/main/src/lerobot/policies/act/modeling_act.py | `ACTTemporalEnsembler` exists, sync `select_action` path only; chunk runner raises "Chunk inference does not support temporal ensembling."; ACT takes no language input; at inference the latent is all zeros | primary (code) | high |
| 11 | LeRobot v0.6.1: `src/lerobot/async_inference/{configs,constants,robot_client,policy_server,helpers}.py` | https://github.com/huggingface/lerobot/tree/v0.6.1/src/lerobot/async_inference | Legacy stack: `chunk_size_threshold=0.5`, `AGGREGATE_FUNCTIONS`, timestep-keyed aggregation, `must_go`, joint-space similarity filter, task fixed by `control_loop(task=cfg.task)`, no RTC | primary (code, tagged release) | high |
| 12 | Cadene et al., "LeRobot: An Open-Source Library for End-to-End Robot Learning", arXiv 2602.22818 (ICLR 2026) | https://arxiv.org/abs/2602.22818 | §3.4 + App. E Table 5: Sync vs Async success / time / cubes; speedup from logical decoupling only (server and client on the same machine) | primary (paper) | high |
| 13 | Shukor et al., "SmolVLA…", arXiv 2506.01844 | https://arxiv.org/abs/2506.01844 | §3.3 Algorithm 1 (threshold g, similarity filter ε, aggregation f); §4.6 Fig. 5: 9.7 s vs 13.75 s (~30% faster), 19 vs 9 cubes | primary (paper) | high |
| 14 | Black, Galliker, Levine, "Real-Time Execution of Action Chunking Flow Policies" (RTC), arXiv 2506.07339 | https://arxiv.org/abs/2506.07339 | RTC "freezing" actions guaranteed to execute and "inpainting" the rest; no re-training (abstract only) | primary (abstract only) | medium (I read only the abstract) |

---

## Q1 — Where the async inference stack lives, how it works, supported policies — **done**

### 1a. Current main (commit 146d847)

**Location [V] [1][4][5][9]:**
- `src/lerobot/inference/`: `base.py` (InferenceEngine, `set_task`, task versioning), `execution.py` (`ChunkRuntime`, `ChunkRequest`, `HoldState`, `estimate_delay`), `rtc.py` (local RTC engine, background thread), `sync.py`, `prediction.py` (`predict_chunk`), `policy_runner.py`, `factory.py` (configs/defaults), `chunk_settings.py`, `contracts.py`, `dispatch.py`.
- `src/lerobot/remote_inference/`: `server.py` (`SessionWorker`), `client.py` (`RemoteClient`), `engine.py` (`RemoteInferenceEngine`), `protocol.py`, `codec.py`, `deployment.py`, `configs.py`, `chunk_contract.py`, `README.md`.
- Entry points: `src/lerobot/scripts/lerobot_policy_server.py`, `src/lerobot/scripts/lerobot_rollout.py`. Transport is Zenoh (`src/lerobot/transport/zenoh.py`).
- Queue: `src/lerobot/policies/rtc/action_queue.py` (`ActionQueue`).

**How it works [V] [1][5]:**
- Three backends (README §1 table): `sync` (rollout control thread, the policy's own `select_action`), `rtc` (a local inference worker, no transport, "Asynchronous RTC through shared prediction/execution components"), and `remote` ("Chunk, aligned/blended chunk, guided RTC or trained RTC" over Zenoh).
- The control thread "never waits for a model or network round trip" (README §2). It publishes an owned observation snapshot plus the task. The worker reserves one `ChunkRequest` and the runtime validates the reply and trims/merges it atomically (README §4).
- **Request trigger (replaces `chunk_size_threshold`) [V] [1][5]:**
  - Remote plain chunks request when playback ≤ `effective_refill = max(refill_seconds, recent_max_turnaround + action_interval)` (README §7). `ChunkRuntime.should_request` computes `playback = queue.qsize()*interval` and compares it with `effective_refill` (execution.py L352–379).
  - Defaults in `inference/factory.py`: `refill_seconds: float = 0.5` (L118), `chunk_merge = "auto"` (L120), `blend_steps = 0`, `blend_weight = 0.5` (L121–122).
  - Local RTC uses `queue_threshold: int = 30` (factory.py L86), not `refill_seconds`.
  - "At most one request or accepted successor is prefetched" (README §6 Append).
- **Overlap handling (replaces `aggregate_fn`) [V] [1][5][6]:**
  - **append**: execute the current chunk, then the accepted successor.
  - **aligned** (default for plain chunks; `chunk_merge=auto` → aligned for `mode=chunk`, append for RTC, factory.py L151–152): trim the first `c_now − c_obs` already-consumed steps and "atomically replace only the future queue". The "currently committed/interpolating endpoint cannot be replaced".
  - **blending** (client-only, aligned plain chunks): `blended = q_t + b_w * (i_t − q_t)`, where `b_w` weights the **incoming** prediction. `blend_steps=0` disables it.
  - **RTC**: "conditions prediction on an ongoing model-space continuation rather than averaging independently produced canonical chunks" (README §6).
- **Observation sending [V] [1][5]:**
  - Observations are timestamped at read start, copied into an immutable `ObservationSnapshot` and tagged with task/version. Aligned snapshots also capture the commitment cursor and execution generation.
  - Gates include a source-age check: `begin()` returns None if `age > self.max_age`. The default source age is 5 s (README §11).
  - There is **no joint-space similarity filter** on main. That was a v0.6.1 server feature (see 1b) **[V-code→inference]**: I found no `observations_similar` under `src/lerobot/inference` or `src/lerobot/remote_inference` in the files I grepped.
- **Supported policies (README §5 "Policy support" table) [V] [1]:**
  - **ACT**: "Current observation, temporal ensembling disabled." Remote HW evidence: `maximellerbach/omx_multicubes_act`, `maximellerbach/omx_pickandplace_act`.
  - **SmolVLA**: "Declares existing camera masking/resizing; guided RTC supported." Evidence: "Remote HW and local guided RTC: `imstevenpmwork/super_chatton_smolvla`".
  - XVLA, LaWAM, EVO1, FineART VLA have remote HW evidence.
  - π0/π0.5 are "Current-observation candidates … No remote HW acceptance established here."
  - Diffusion, Multi-task DiT and VQ-BeT: "Default history and/or per-step queue preparation do not satisfy the direct current-observation contract". TD-MPC and Gaussian actor are unsupported.
  - "Source declarations allow RTC for SmolVLA, π0, π0.5, FineART, EVO1, GR00T and continuous MolmoAct2."

### 1b. Legacy stack (tag v0.6.1, `src/lerobot/async_inference/`) — what the papers describe

All [V] [11]:
- `constants.py`: `DEFAULT_FPS = 30`, `DEFAULT_OBS_QUEUE_TIMEOUT = 2`, `SUPPORTED_POLICIES = ["act", "smolvla", "diffusion", "tdmpc", "vqbet", "pi0", "pi05", "groot"]`, `SUPPORTED_ROBOTS = ["so100_follower", "so101_follower", "bi_so_follower", "omx_follower"]`.
- `configs.py`:
  - `AGGREGATE_FUNCTIONS = {"weighted_average": 0.3*old + 0.7*new, "latest_only": new, "average": 0.5/0.5, "conservative": 0.7*old + 0.3*new}`.
  - `RobotClientConfig`: `chunk_size_threshold: float = 0.5`, `aggregate_fn_name = "weighted_average"`, `actions_per_chunk` (required), `task: str = ""`.
  - `PolicyServerConfig`: `port=8080`, `inference_latency = 1/30`.
- `robot_client.py`:
  - `_ready_to_send_observation()` returns `action_queue.qsize() / action_chunk_size <= chunk_size_threshold`.
  - `control_loop_observation()` sets `raw_observation["task"] = task` and `must_go = must_go.is_set() and action_queue.empty()`.
  - `_aggregate_action_queues()` builds a new `Queue`:
    - incoming actions with `timestep <= latest_action` are skipped;
    - new timesteps are added;
    - overlapping timesteps get `aggregate_fn(old, new)`;
    - **old queued timesteps that the incoming chunk does not cover are dropped**, because only incoming actions are put into `future_action_queue`.
- `policy_server.py`: `_obs_sanity_checks` skips an observation if its timestep was already predicted, or if `observations_similar(...)` holds. `helpers.py` compares joint-space state with default `atol = 1`. `_enqueue_observation` bypasses the check when `obs.must_go`. `_get_action_chunk` returns `chunk[:, :actions_per_chunk, :]`. There are no references to RTC (`grep -c rtc` = 0 in both files).

---

## Q2 — How the language task is passed; is it updatable at runtime? — **done**

**Legacy v0.6.1 [V] [11]:** the task is **fixed at client start**. `async_client()` calls `client.control_loop(task=cfg.task)`, and every observation gets `raw_observation["task"] = task`. There is no setter API. The local RTC engine in v0.6.1 (`src/lerobot/rollout/inference/rtc.py`) stores `self._task = task` in `__init__` and has no `set_task` (grep found none).

**[V-code→inference]** In v0.6.1 the server's similarity filter compares only joint state, so if `task` were mutated while the arm is static, a new observation could be skipped as "too similar" unless `must_go` is set.

**Current main [V] [3][4][9]:**
- **Runtime updatable.** Every engine has `set_task(task) -> bool` with a monotonic `task_version` ("Monotonic instruction identity, including changes back to the same text", base.py L210–228).
- **APIs:**
  - CLI: `lerobot-rollout ... --interactive=true`, then `/subtask <text>`. inference.mdx: "Change the instruction within the current run; asynchronous inference may enter a planned hold … Only affects policies that condition on language (SmolVLA, π0/π0.5, and similar)".
  - Library: `RolloutController.set_task("grab the red cube")  # re-instruct mid-run` (inference.mdx L486–509; `rollout/controller.py` L281). It returns False once stopping/stopped and stops autosteer.
  - Remote: `RemoteInferenceEngine.set_task` (`remote_inference/engine.py` L421–443). It validates the length against `max_input_chars` and emits a `task` event.
  - There is also `/autosteer <goal>` and an external VLM planner (`--planner.model_id`) that applies subtasks "through the same path as `/subtask`" (inference.mdx L427, L452).
- **Semantics of a mid-episode change [V] [2][3][4][5]:**
  - **Change while a request is in flight (local RTC):** `RTCInferenceEngine.set_task` computes `needs_hold` (pending request of the old version, policy active, robot `supports_hold`) and calls `_request_hold("Instruction change", ...)`. That calls `self._runtime.invalidate(held=True, ...)`, which bumps `generation`, **`queue.clear()`**, and sets `pending=None` and `_last_anchor=None` (execution.py L242–263). The worker then waits for the control-thread hold acknowledgment, calls `self._policy.drop_queued_actions()`, releases the hold and requests a **fresh** chunk. Docs: "On a robot supporting local hold, the engine invalidates queued/interpolated motion, waits for the control loop to acknowledge the hold, then requests fresh motion under the new task. **Expect a stop during this transition; it is not a guaranteed continuous blend.**" (inference.mdx L419). "Instruction change during inference: Discard the old prediction, pause and obtain fresh actions for the new instruction. Changes between requests may preserve accepted motion." (remote_inference.mdx table).
  - **Stale results are rejected:** `ChunkRuntime.accept` returns False if `request.observation.task_version != task_version` (execution.py L437–438).
  - **Change between requests:** accepted actions are retained ("A change between requests can retain already accepted actions for continuity"). In `aligned` mode `should_request` returns True immediately on a task-version change ("Aligned task changes may bypass the playback threshold", execution.py L352–368). In `append` mode (the default for RTC) there is no bypass, so the next request waits for the normal playback threshold. **[V-code→inference]**
  - **Robots without hold support:** "Local RTC on a robot without hold support still discards the obsolete result, but can exhaust its remaining actions and terminate." (inference.mdx L419).
  - **Recording provenance:** "Frames carry the task provenance of the action actually sent, so actions already queued or interpolated under the old task keep the old label." (inference.mdx L433)
  - **Design status:** README §12 lists "Immediate planned language wait | Simple serialized state; discards continuation and can disrupt task progress", and §9 says "Fresh replanning can lose task progress, as observed on hardware" (said of VQA, which uses the same hold path).

---

## Q3 — Does LeRobot implement Real-Time Chunking? For which policies? — **done**

**Yes [V] [7][8][4]:**
- **Implementation:** `src/lerobot/policies/rtc/` (`modeling_rtc.py` `RTCProcessor.denoise_step`, `configuration_rtc.py` `RTCConfig`, `action_queue.py`, `latency_tracker.py`, `relative.py`, `action_interpolator.py`, debug tracker/visualizer).
- **Execution:** local RTC through `src/lerobot/inference/rtc.py`; remote RTC through `remote_inference/` (mode `rtc_guided`/`rtc_trained`). Guidance reference URL in the docstring: https://www.physicalintelligence.company/download/real_time_chunking.pdf.
- **Guided mechanism** (`denoise_step`, modeling_rtc.py L122–253):
  - `x1_t = x_t − time·v_t`
  - `err = (prev_chunk_left_over − x1_t) * weights`
  - the correction is the autograd VJP; the guidance weight is clipped by `max_guidance_weight`.
  - `prev_chunk_left_over` is right-padded with zeros when shorter than the chunk.
  - **`execution_horizon` is clamped to the leftover length**: `if execution_horizon > prev_chunk_left_over.shape[1]: execution_horizon = prev_chunk_left_over.shape[1]`.
  - Prefix weights via `get_prefix_weights(inference_delay, execution_horizon, T)` with schedules `ZEROS` (1 for the first `delay` steps only), `ONES`, `LINEAR` (default), `EXP`.
- **Config defaults** (`RTCConfig`): `enabled=True`, `mode="guided"`, `prefix_attention_schedule=LINEAR`, `max_guidance_weight=10.0`, `execution_horizon=10`. The docstring says RTC treats chunk generation "as an inpainting problem … using prefix attention".
- **Trained mode:** `trained` "hard-inpaints a prefix and requires a compatible training-time RTC checkpoint" (configuration_rtc.py). rtc.mdx: "It currently requires a Pi05 checkpoint trained with `policy.rtc_training_max_delay > 0`". `rtc_training_max_delay` is defined only in `policies/pi05/configuration_pi05.py` (L79) among policy configs.

**Policies [V] [1][7][8][10]:**
- **SmolVLA:** `SmolVLAPolicy.supports_rtc() → True` (modeling_smolvla.py L150). `rtc_config: RTCConfig | None = None` (configuration_smolvla.py L104). `VLAFlowMatching` gets `rtc_processor` and passes `inference_delay` / `prev_chunk_left_over` (L805–808). `select_action` asserts RTC is not used ("RTC is not supported for select_action, use it with predict_action_chunk"). Guided mode only. Test: `tests/policies/smolvla/test_smolvla_rtc.py` exists (not run).
- **π0:** `rtc_config` in configuration_pi0.py L62. Tests `tests/policies/pi0_pi05/test_pi0_rtc.py` and `test_pi05_rtc.py` exist (not run).
- **π0.5:** guided plus trained (`test_pi05_training_time_rtc.py` exists).
- **Others with RTC declarations:** EVO1, GR00T, MolmoAct2 (continuous), FineART (README §5). pi0_fast config references rtc (grep hit), but I did not inspect it.
- **ACT: no RTC.** There are no `rtc` references in `policies/act/` (grep). `PreTrainedPolicy` adds `RTC_GUIDED` to `modes` only `if self.supports_rtc()` (pretrained.py L345–350). ACT is not flow/diffusion-based, so there is no denoising loop to guide.
- `search "inpaint"`: only docstrings/docs ("hard-inpaints"); there is no separate inpainting module.

---

## Q4 — What happens to queued actions when a new chunk arrives? — **done**

All [V] [6][5][11]:
- **Main, RTC enabled** (`ActionQueue.merge` → `_replace_actions_queue`): "Replaces the entire queue with new actions, accounting for inference delay". The new queue is `new_chunk[clamped_delay:]`, where `delay = min(max(0, real_delay), max(0, cursor_now − snapshot.cursor))`. **All old unconsumed actions are discarded** and replaced by the new chunk minus the first `delay` steps. The old leftover influenced the new chunk only through guidance during denoising.
- **Main, RTC disabled, append** (`_append_actions_queue`): the old remainder is kept and the new chunk is concatenated after it.
- **Main, aligned plain chunks** (`ChunkRuntime._accept_aligned` → `ActionQueue.replace_future`): the future is replaced if the cursor/generation snapshot is unchanged. The committed endpoint is never replaced. Optional `blend_steps` blending applies on overlapping slots.
- **Main, invalidate/hold** (task change in flight, VQA, reset, starvation): `queue.clear()` plus a generation bump. Everything is discarded.
- **Legacy v0.6.1:** timestep-keyed merge with `aggregate_fn`. Already-executed timesteps are skipped. Old queued timesteps not present in the incoming chunk are dropped, because the rebuilt queue contains only incoming actions (see 1b).

---

## Q5 — ACT temporal ensembling support — **done**

All [V] [10][1]:
- `ACTTemporalEnsembler` (modeling_act.py L170+): "Temporal ensembling as described in Algorithm 2 of https://huggingface.co/papers/2304.13705". Weights are `wᵢ = exp(-temporal_ensemble_coeff * i)` with w₀ the oldest action. The docstring note says the original ACT value is 0.01.
- `configuration_act.py`: `temporal_ensemble_coeff: float | None = None`. It raises if set together with `n_action_steps > 1` ("`n_action_steps` must be 1 when using temporal ensembling … the policy needs to be queried every step").
- It is used only in `ACTPolicy.select_action` (sync path): `actions = self.predict_action_chunk(batch); action = self.temporal_ensembler.update(actions)`.
- **It is not available in async/RTC/remote:** `PreTrainedPolicy` chunk-spec derivation raises `ValueError("Chunk inference does not support temporal ensembling.")` when `temporal_ensemble_coeff` is set (pretrained.py ~L333). The README policy table says ACT runs with "temporal ensembling disabled", and §5 says "Checkpoint history, temporal ensembling or executed-action feedback cannot be emulated by merely taking the latest frame."
- **ACT has no language input:** grep for `task|language|lang` in `policies/act/{modeling,configuration}_act.py` hits only license headers. At inference without the VAE encoder, `latent_sample = torch.zeros(...)` (modeling_act.py L462–465), so the decoder is a single deterministic forward pass.

---

## Paper checks (alpha ask) — **done**

### LeRobot, arXiv 2602.22818 (ICLR 2026) [V] [12]

- **§3.4:** the inference stack decouples prediction from control "both (1) physically and (2) logically". It is an "asynchronous producer-consumer scheme" and "Overlapping predictions are merged via a generalized aggregation function f … ensuring a non-empty action queue". The App. E.2 example uses `RobotClientConfig`, `client.control_loop(task)` with `task = ... # Specify the task using natural language` (task given once at loop start).
- **App. E:** "the speedup presented in Table 5 derives from logical decoupling … rather than physical decoupling, as both the server and client run on the same machine."
- **Table 5** (SmolVLA, SO-100; pick-place / stacking / sorting; "over the 10 test episodes (60s each)"):
  - (a) Success rate (%): Sync 75 / 90 / 70, Avg **78.3**; Async 80 / 90 / 50, Avg **73.3**.
  - (b) Task completion time (s): Sync Total **137.5**, Avg **13.75**, Std 2.42; Async Total **97.0**, Avg **9.70**, Std 2.95.
  - (c) # cubes in fixed time (60 s/episode): Sync Total **9**, Avg 1.8, Std 0.45; Async Total **19**, Avg 3.8, Std 1.3.
- **Table 3** (latency context): SmolVLA (450M) avg inference latency **99.244 ± 1.195 ms** on RTX 4090 and **278.833 ± 1.886 ms** on A100. ACT (52M) **5.013 ± 0.061 ms** on RTX 4090 (fp32, 10 denoising steps for flow/diffusion).
- §3.3 notes ACT is single-task and "necessitates retraining whenever changes in the experimental conditions occur", while SmolVLA "allows to control real-world robots via language conditioning".
- **RTC / mid-episode instruction change:** not mentioned in the pages returned by alpha ask **[U]**. The tool returned selected pages (1, 2, 4, 7, 8, 9, 11–13, 19, 20), not the full text, so absence is not proven.

### SmolVLA, arXiv 2506.01844 [V] [13]

- **§3.3, Algorithm 1:** "Input: horizon T, chunk size n, threshold g ∈ [0, 1]". New observation when "|A_t|/n < g". `NeedsProcessing` = "similarity filter, or triggers direct processing". `A_{t+1} ← f(A_t, Ã_{t+1})` "aggregate overlaps".
  - Near-duplicates: "if their distance in joint-space is under a predetermined threshold, ϵ ∈ R+". "when the queue … eventually becomes empty, the most recent observation is processed regardless of similarity."
  - Analysis: "With a real-world frame-rate of 30 frames per second, ∆t = 33ms". Exhausted queues are avoided for "g ≥ (E[ℓ_S]/∆t)/n". Regimes g = 0 (sequential), g = 0.7 (async example), g = 1 (compute-intensive). Observations are sent every "(1−g)n⋅∆t seconds".
- **§4.6 / Fig. 5** (Sync vs Async, real world):
  - Same success / time / cube numbers as LeRobot Table 5.
  - "On average, it completes the task in 9.7 seconds, compared to 13.75 seconds in the synchronous setting (∼ 30% faster)."
  - "the asynchronous mode allows the robot to complete 19 successful pick-and-place cycles, compared to only 9 in the synchronous case".
  - "Hyperparameters have been optimized for Pick-Place and reused across tasks."
  - The speed experiments use Pick-Place: "10 trials and 5 different cube positions", and the fixed limit is "(e.g., 60 seconds)".
  - Qualitative: "greater robustness to shifts in object positions and external disturbances".
- **Related ablation, Table 13** (LIBERO, action execution steps before re-observing): avg **80.3** (1 step), **82.8** (10), **70.8** (30), **51.8** (50). "Sampling new observations more frequently … significantly improves performance."
- §5: async "is model-agnostic and can be integrated with any policy that outputs chunks of actions."
- **RTC / mid-episode instruction change:** not mentioned in the returned pages **[U]** (partial-page return, as above). Observation: Async had a **lower** sorting success (50 vs 70) and avg (73.3 vs 78.3); the papers describe success as "similar"/"comparable".

---

## Minimal code change for spoken-instruction mid-motion repair (proposal, untested) — **done (design only)**

All of the below is **[U] proposal**, derived from the code read above. Nothing was implemented or run. Targets main @ 146d847. Status quo [V]: `set_task` → hold → `queue.clear()` → fresh chunk **without** an RTC prefix (the queue is empty, so `model_actions=None`), giving a visible stop.

### (a) Truncate the queue instead of clearing it + force an immediate re-query

1. **`src/lerobot/policies/rtc/action_queue.py`** — add a cursor-preserving truncation. It must not bump `_generation`/`_cursor`, so `snapshot()`-based delay math stays valid:
   ```python
   def truncate_future(self, keep: int) -> int:
       with self.lock:
           if self.queue is None:
               return 0
           end = self.last_index + max(0, keep)
           self.queue, self.original_queue = self.queue[:end], self.original_queue[:end]
           if self._task_queue is not None:
               self._task_queue = self._task_queue[:end]
           self._provenance_queue = self._provenance_queue[:end]
           return len(self.queue) - self.last_index
   ```
2. **`src/lerobot/inference/execution.py` (`ChunkRuntime`)** — add `retarget(keep)`:
   - Under `self.lock`, call `self.queue.truncate_future(keep)`.
   - Abandon the old-task pending request (`self.pending = None`). Its result is already rejected by the `task_version` check in `accept`.
   - Set `self._force_request = True`.
   - In `should_request`, return True when `_force_request` (after the failure/active/held/pending gates). This mirrors the existing aligned-mode task-change bypass at L362–368.
   - Clear the flag in `begin`.
3. **`src/lerobot/inference/rtc.py` (`RTCInferenceEngine.set_task`)** and **`remote_inference/engine.py` (`set_task`)**:
   - Behind a new config switch (e.g. `--inference.retarget=hold|repair`, default `hold`), replace `self._request_hold("Instruction change", …)` with `self._runtime.retarget(keep)`.
   - Use `keep = estimate_delay(turnaround, interval, mode, …) + margin`. Because a local-RTC model call cannot be interrupted (README §2: cancellation "does **not** interrupt a GPU call"), a safe `keep` must cover the remaining old call plus one new call, roughly 2× turnaround in steps.
   - With SmolVLA at the paper's 99.244 ms (RTX 4090) and 30 fps (∆t ≈ 33 ms), that is ~3 steps per call, so keep ≈ 6–8 steps. **[U] inference**: arithmetic from [12][13]; real turnaround includes pre/post-processing.
   - The robot keeps moving on the old-task prefix for `keep` steps. Without hold support this is also safer than the current "may exhaust and terminate" path.

### (b) Re-query SmolVLA with RTC prefix conditioning

- No new policy code is needed for guided RTC. `_rtc_loop` already passes `model_continuation = request.continuation.model_actions` and `inference_delay = request.delay` into `predict_chunk`, and from there into `RTCProcessor.denoise_step` [V].
- After step (a), the continuation is exactly the truncated `keep`-step old-task prefix. Because `denoise_step` **clamps `execution_horizon` to the leftover length** [V], guidance automatically covers only those `keep` steps. Steps after `keep` get zero weight and are free to follow the new instruction.
- For remote RTC, the client already serialises `model_continuation`/`canonical_continuation` + `cursor` into the request (`remote_inference/client.py` L487–498) [V], so (a) suffices on the client side.
- Optional per-request tuning [U]: for the repair request, pass `rtc_horizon=keep` explicitly and/or use the `ZEROS` schedule, which hard-weights only the first `delay` steps. That maximises reactivity to the new command. Keep the default LINEAR schedule for normal refills.
- Merge: `_replace_actions_queue` then drops the first `min(delay, actual progress)` steps [V]. The new-task chunk starts where the robot is.
- **Caveats [U]:**
  - SmolVLA supports only `guided` (Jacobian guidance needs a backward pass; README notes guided RTC must run under `no_grad`, not inference mode), so the latency of the repair request is higher than a plain chunk. `trained` mode is π0.5-only.
  - Relative-action checkpoints need the re-anchoring path in `policies/rtc/relative.py` (README §5).
  - With `torch.compile`, a new instruction "that changes processed tensor shapes can trigger recompilation" (inference.mdx L421).
  - The old-task prefix was generated under a different instruction. Guidance forces consistency only on the committed prefix; whether SmolVLA cleanly "turns" toward the new goal afterwards is an empirical question (the novelty experiment).

### (c) What is possible for ACT (non-diffusion)

1. **The instruction cannot reach ACT** [V]. ACT takes no language input (modeling/configuration_act.py), and the LeRobot paper calls it single-task [12]. A spoken command can only (i) select among several single-task ACT checkpoints, or (ii) require a new language/task-ID-conditioned ACT variant (not in LeRobot). Task-based model selection is listed as **future work** in README §13 ("Select one compatible deployment/instance explicitly, invalidate incompatible continuation …") [V].
2. **No inpainting/RTC** [V]. ACT inference is a single deterministic decoder pass with latent = zeros, so there is no denoising trajectory to guide and `supports_rtc()` is not overridden for ACT.
3. **What *is* possible with existing machinery** [V for mechanisms, U for suitability]:
   - Same truncation (a) plus a forced request.
   - Then `chunk_merge=aligned` with client-side **blending** (`blend_steps>0`, `blend_weight`, explicit continuous `blend_components`, never the gripper) to crossfade old-prefix → new-checkpoint chunk over the overlap: `blended = q_t + b_w*(i_t − q_t)`.
   - This is a post-hoc canonical-space average, not conditioning. The README warns "A smooth average of incompatible plans can miss the object."
4. **Temporal ensembling** [V] works only in the sync `select_action` path with `n_action_steps=1` (one forward pass per tick; ~5 ms on an RTX 4090 per [12] Table 3). It is rejected by the chunk runner, so it cannot be combined with remote/RTC. In the sync path a task/checkpoint switch could use `drop_queued_actions()`; for TE one would also need to reset or re-weight `temporal_ensembler` [U]. Note that `ACTPolicy._action_queue_attrs` covers `_action_queue`, not the ensembler state [V-code→inference from `pretrained.py` L97].

---

## Coverage Status

| Item | Status |
|---|---|
| Q1 async stack location/mechanics/policies | done (main + legacy v0.6.1) |
| Q2 task passing / runtime update API | done |
| Q3 RTC implementation & policy coverage | done (tests located, not run) |
| Q4 queued actions on new chunk | done |
| Q5 ACT temporal ensembling | done |
| Paper 2602.22818 async claims | done (partial-page return) |
| Paper 2506.01844 async claims | done (partial-page return) |
| Minimal code change (a)(b)(c) | done as design; **not implemented or tested** |

**Checked directly:** all code paths cited above (clone of main @146d847, cross-checked against `feynman alpha code` output for `inference/`, `remote_inference/`, `rollout/`, `policies/rtc/action_queue.py`); legacy files from tag v0.6.1; paper text through `feynman alpha ask`.

**Uncertain:**
- Whether either paper mentions RTC or instruction changes on pages not returned.
- Whether the `append`+RTC between-request task change in practice yields a smooth new-task chunk conditioned on the old prefix. This is deduced from code and was not run.
- pi0_fast RTC status (not inspected).
- Hardware behaviour of all proposals.

## Blocked sources

- None blocked by robots.txt, paywall or login.
- Tool limitation (not a block): `feynman alpha code` could not read the `v0.6.1` tag ("Path not found"), so the legacy files were read from a `git clone --branch v0.6.1`.
- 2506.07339 (RTC paper): only the arXiv abstract was read. Its numeric claims are not used here.

## Sources

1. LeRobot main — `src/lerobot/remote_inference/README.md` — https://github.com/huggingface/lerobot/blob/main/src/lerobot/remote_inference/README.md
2. LeRobot main — `docs/source/remote_inference.mdx` — https://github.com/huggingface/lerobot/blob/main/docs/source/remote_inference.mdx
3. LeRobot main — `docs/source/inference.mdx` — https://github.com/huggingface/lerobot/blob/main/docs/source/inference.mdx
4. LeRobot main — `src/lerobot/inference/rtc.py` — https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/rtc.py
5. LeRobot main — `src/lerobot/inference/execution.py` — https://github.com/huggingface/lerobot/blob/main/src/lerobot/inference/execution.py
6. LeRobot main — `src/lerobot/policies/rtc/action_queue.py` — https://github.com/huggingface/lerobot/blob/main/src/lerobot/policies/rtc/action_queue.py
7. LeRobot main — `src/lerobot/policies/rtc/modeling_rtc.py` / `configuration_rtc.py` — https://github.com/huggingface/lerobot/tree/main/src/lerobot/policies/rtc
8. LeRobot main — `docs/source/rtc.mdx` — https://github.com/huggingface/lerobot/blob/main/docs/source/rtc.mdx
9. LeRobot main — `src/lerobot/inference/base.py`, `src/lerobot/remote_inference/engine.py`, `src/lerobot/rollout/controller.py`, `src/lerobot/rollout/interactive.py` — https://github.com/huggingface/lerobot/tree/main/src/lerobot
10. LeRobot main — `src/lerobot/policies/act/modeling_act.py`, `configuration_act.py`, `src/lerobot/policies/pretrained.py`, `src/lerobot/policies/smolvla/modeling_smolvla.py` — https://github.com/huggingface/lerobot/tree/main/src/lerobot/policies
11. LeRobot v0.6.1 — `src/lerobot/async_inference/` — https://github.com/huggingface/lerobot/tree/v0.6.1/src/lerobot/async_inference
12. Cadene et al., LeRobot: An Open-Source Library for End-to-End Robot Learning, arXiv 2602.22818 — https://arxiv.org/abs/2602.22818
13. Shukor et al., SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics, arXiv 2506.01844 — https://arxiv.org/abs/2506.01844
14. Black, Galliker, Levine, Real-Time Execution of Action Chunking Flow Policies, arXiv 2506.07339 — https://arxiv.org/abs/2506.07339
