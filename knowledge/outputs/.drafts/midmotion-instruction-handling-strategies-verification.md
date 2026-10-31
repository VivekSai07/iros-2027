# Verification — midmotion-instruction-handling-strategies (draft of 2026-10-18)

Verifier: lead (Feynman), resumed session, 2026-10-18. No new research; checks only against primary text.
Method: arXiv export API (`export.arxiv.org/api/query?id_list=...`), `curl -L` HTTP status + `<title>` for non-arXiv URLs, `pdftotext -layout` on downloaded arXiv PDFs + grep, raw GitHub files for LeRobot `main` and Tencent/VITA `VITA-E`, one page screenshot (ELLSA p.9) where text extraction was ambiguous.

**Verdict: no FATAL issues. 3 MAJOR, 9 MINOR. All fixed in `-revised.md`.**

## 1. Identifier and URL resolution

| ID / URL | Resolves to | Status |
|---|---|---|
| arXiv 2510.16756 | "End-to-end Listen, Look, Speak and Act" (ELLSA), v2 | OK |
| arXiv 2510.21817 | "VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting", v1 | OK |
| arXiv 2502.19417 | "Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models", v2 | OK |
| arXiv 2506.03574 | "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models", v1 | OK |
| arXiv 2609.30913 | "Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies", v1 | OK |
| arXiv 2605.12160 | "Premover: Fast Vision-Language-Action Control via Early Execution During Instruction Delivery", v2 | OK |
| arXiv 2610.20531 | "EarlyCommit: Calibrated Word-by-Word Commitment for Robots Acting Before You Finish Speaking", v1 | OK |
| arXiv 2610.02360 | "SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation", v1 | OK |
| arXiv 2609.24547 | "MIRA: Real-Time Full-Duplex Human-Robot Interaction for Embodied Companions", v2 | OK |
| arXiv 2506.07339 | "Real-Time Execution of Action Chunking Flow Policies" (RTC), v2 | OK |
| arXiv 2506.01844 | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics", v1 | OK |
| arXiv 2304.13705 | "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" (ACT), v1 | OK |
| arXiv 2512.01031 | "VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference", v2 | OK |
| neurips.cc/virtual/2026/poster/162424 | 200; title "RIAP: Risk-Aware Incremental Action Policy for Physical Commitment from Partial Speech"; abstract numbers (8,160 replays, 27.5%→1.6%, 1,022 ms, 60.6%, 30 participants) match draft | OK |
| huggingface.co/tsinghua-ee/ELLSA | 200, title "tsinghua-ee/ELLSA" | OK |
| github.com/Tencent/VITA/tree/VITA-E | 200 | OK |
| huggingface.co/VITA-MLLM/VITA-E | 200, title matches | OK |
| lxysl.github.io/VITA-E/ | 200 | OK |
| www.pi.website/research/hirobot | 200 | OK |
| switchvla.github.io | 200, title = SwitchVLA paper title | OK |
| gagajian.github.io/MIRA/ | 200, title = MIRA paper title | OK |
| github.com/Physical-Intelligence/real-time-chunking-kinetix | 200 | OK |
| github.com/huggingface/lerobot/blob/main/src/lerobot/remote_inference/README.md | 200 | OK |
| github.com/huggingface/lerobot/tree/v0.4.0/src/lerobot/async_inference | 200 | OK |
| huggingface.co/lerobot/smolvla_base | 200 | OK |
| github.com/VITA-MLLM/VITA-E | 404 (draft already says 404; listed correctly as not-a-block) | OK |

## 2. High-stakes spot-checks against primary text

| # | Cell | Primary evidence | Result |
|---|---|---|---|
| 1 | Hi Robot "triggered immediately", not "wait for step boundary" | 2502.19417 §4.2: "When the system receives a user intervention, the high-level inference is triggered immediately to recompute ℓ̂t." §4.1: "we rerun high-level inference … either when one second has elapsed, or when a new interaction with the user takes place." | **Confirmed.** Add the 1 s periodic re-run (MINOR m1). |
| 2 | "Wait" characterisation is secondary | VITA-E 2510.21817 Related Work: Hi-Robot adjusts "after the current atomic step has been completed". SwitchVLA 2506.03574 Intro: methods [12–16] "must wait for the current task to complete before re-planning"; [16] = Hi Robot | **Confirmed**; SwitchVLA's statement is a group claim over 5 refs (MINOR m2). |
| 3 | Hi Robot latency | App. B.3 table: low-level total 73 ms on-board / 86 ms "off-board + WiFi"; high-level RTX 4090 47 ms prefill + 13.2 ms decode (H100 17.3 + 5.7) | **Confirmed.** |
| 4 | SwitchVLA real WS1 numbers incl. MT-ACT 0.0/0.0/4.9 | Table 3: MT-ACT 56.3 / 0.0 / 0.0 / 4.9; π0 97.9 / 50.1 / 0.0 / 32.0; SwitchVLA 95.9 / 99.3 / 95.1 / 75.0. Table 1 (LIBERO-Goal): π0 mid 8.3; SwitchVLA mid 50.9. "12 trials" (§4, Table 11). 15 Hz, RTX 4090 (App.) | **Confirmed.** |
| 5 | LeRobot `set_task` behaviour | `inference/base.py::set_task` increments `_task_version`; `inference/sync.py` on task change: "dropping precomputed actions" → `drop_queued_actions()`; `remote_inference/engine.py::set_task` "holding if action inference is pending" — `_request_hold("instruction change")` only if `runtime.pending is not None`; docstring: "Actions already accepted can retain continuity, but pending results for the old task cannot be accepted"; `inference/rtc.py::set_task` same pattern, hold only if pending and robot `supports_hold`. `rollout/interactive.py` exposes `/subtask <text>` → `controller.set_task`. README §285: "Supported in-flight retargets use a planned wait and fresh resumption; between-request changes can preserve eligible continuity." README §147: ACT "temporal ensembling disabled"; §148 SmolVLA "guided RTC supported". | **Confirmed**, but draft omits the no-pending-inference path (MAJOR M3) and misattributes the "lose task progress" quote (MAJOR M1). |
| 6 | SocialVLA latency | 2610.02360 Table (b): Detector→fusion 0.048 s median (n=22); VLA gate→physical hold 0.336 s median, p95 0.681, max 1.559 (n=24); reaction onset→hold 1.021 s median, p95 1.569 (n=14). "paused until the participant explicitly requests continuation." "It is not a certified safety system." | **Confirmed.** Add n and p95 (MINOR m6). |
| 7 | MIRA latency / bounded commitment | 2609.24547: 450 ms interruption-confirmation threshold; early abort "terminates the ongoing robot motion"; §RHPC "only 15 frames (0.50 s) are committed … terminated after the currently committed segment"; Table 3 speech_started→abort_cmd_sent 466 ms, "at the median … to abort-command dispatch". Production trace 199 sessions / 559 decisions. | **Confirmed.** |
| 8 | ELLSA latency + 94.3% | 2510.16756 Table (d): 1 s block 854 ms speech-to-speech / 786 ms speech-to-action; 0.48 s: 455 / 428 ms; "measured on an A100 GPU". Table 3(c) (page screenshot p.9): Interruptive command 94.3%; "Action Cancelled"; interruptions 2–8 s after instruction. | **Confirmed** (text extraction mis-aligned columns; screenshot resolved it). |
| 9 | Causeway per-chunk latency | 2609.30913 §V-d: "On one A100-80GB, per-chunk latency rises 2.5–2.8× (102/75/128 → 253/187/362 ms; replanning 4.0/5.3/2.8 Hz; +4.3 GiB peak) on OFT/π0.5/GR00T"; 3–26% → 47–65%; 5 real trials/cell | **Confirmed.** |
| 10 | RTC latency / delay robustness | 2506.07339: "model latency of 76ms for the baselines and 97ms for RTC" (RTX 4090); Fig. 1 "inference delays in excess of 300 milliseconds"; real experiments inject +100/+200 ms, "completely robust to injected delay" | Numbers confirmed; draft's "robust to injected delays >300 ms" conflates the two (MINOR m3). |
| 11 | Premover / EarlyCommit / VITA-E numbers | Premover App. H: 2.36M params, 0.232 ms over 65.84 ms (LIBERO profiling; GPU not named), SO-101 60.5→49.7 s (−17.9%), 86.0 vs 81.0%; "We do not consider corrections or changes … after execution has begun"; 8×H200. EarlyCommit: 421M ModernBERT-large; 31–35 ms median / 38–41 ms p95 (laptop RTX 3060, Colab T4); 0.79–1.06 s saved; "A commit is final"; "no user study and no physical robot". VITA-E: 2.26 s over ten tests; 100% / 93.3% / 100% over 30 trials; retraction to initial pose via stack; README "(A total of 48 GB GPU memory is needed.)" in the web-demo-with-mocked-robot-state paragraph. SmolVLA: async 9.70 s vs sync 13.75 s; success 73.3 vs 78.3. | **Confirmed**; VITA-E 48 GB context (MINOR m4); Premover hardware wording (MINOR m5). |

## 3. Findings

### FATAL
None. No wrong IDs, no fabricated numbers found in the checked cells.

### MAJOR
- **M1 — Misattributed LeRobot quote.** Draft cites README "Fresh replanning can lose task progress, as observed on hardware" as evidence that instruction-retarget holds lose progress (§3a LeRobot repair cell; §4 evidence matrix caveat; §6 Agreement bullet 3). In the README (§9, language section) the sentence follows "VQA preserves the instruction but discards buffered continuation" — it is about language/VQA planned waits. Retargets use the same planned-wait + fresh-resumption mechanism (README "Supported in-flight retargets use a planned wait and fresh resumption"; tradeoff table "Old trajectory cannot resume a changed state"), so progress loss on retarget is plausible but **not reported** → re-flag [U]. *Fixed.*
- **M2 — Headline absence claim over-flagged; unsupported "slow".** Summary bullet 1 is an absence claim across the 12 compared systems flagged "[V; synthesis]"; an absence claim over a bounded set is synthesis → [U]. "Slow hierarchy" for Hi Robot is not supported (Hi Robot reports 47 + 13.2 ms per decode step and claims real-time feasibility; end-to-end ASR→command latency is unreported). *Fixed: flag [U, synthesis over the compared set], "slow" removed.*
- **M3 — LeRobot physical behaviour incomplete; taxonomy over-simplified.** Draft puts LeRobot main under "Halt first" and describes only the in-flight case. Code: remote and local-RTC engines request a planned hold **only if an inference request is pending**; otherwise already-accepted old-task actions "retain continuity" and keep executing until a new-task chunk replaces the future queue. Sync engine drops queued actions and re-infers (no hold). *Fixed in §1, §2 Mermaid (LeRobot node now conditional, also linked under Redirect), §3a, §7.*

### MINOR
- m1 Hi Robot high level also re-runs every 1 s regardless of user input (§4.1). Added.
- m2 SwitchVLA "must wait" is a group statement about refs [12–16] (Hi Robot = [16]). Clarified.
- m3 RTC delay wording: Fig. 1 claims operation with inference delays >300 ms; injected-delay experiments were +100/+200 ms with no degradation. Reworded in §3a, §4.
- m4 VITA-E 48 GB is stated for the web demo with mocked robot state. Qualified in §3b.
- m5 Premover latency-table hardware "not stated in R2 notes" → "LIBERO profiling run; GPU not named in App. H (experiments on 8×H200)".
- m6 SocialVLA latencies are small-n (n=24 gate→hold, n=14 onset→hold); p95 0.681 s / 1.569 s added.
- m7 Hi Robot IA/TP flag "[V/R1]" is non-standard → "[V, project page via R1; not re-checked this pass]".
- m8 Summary bullet 2 flagged [V] although the four-way grouping is synthesis → "[V per-system; grouping is synthesis]".
- m9 Hi Robot off-board latency is "off-board + WiFi". Added.

### Process note (not a content error)
Plan file named the final artifact `outputs/midmotion-instruction-handling-strategies-comparison.md`; the user's resume instruction specifies `outputs/midmotion-instruction-handling-strategies.md`. Followed the user's path.

## 4. Not re-checked in this pass (retain researcher-pass flags)
Cells whose [V] rests on R1/R2/R3 notes only: ELLSA HF weights ~36.6 GB and 100 episodes/suite; VITA-E Silero VAD in demo code; Hi Robot project-page IA/TP averages; SwitchVLA contact-label details; Causeway 30 demos/task; SocialVLA 238 episodes→false-stop 100→57 (abstract-level confirmed by grep: "from 100 to 57"); SmolVLA weights ~0.9 GB; ACT ~80M / 0.01 s / 2080 Ti (R3 quote); legacy LeRobot v0.4.0 0.3/0.7 weighted-average aggregation; VLASH "directly switch" quote. None were contradicted; they were not re-opened.

## 5. Blocked / open
- `github.com/bytedance/SALMONN/tree/ELLSA` — robots-disallowed (D-007); not accessed.
- RIAP full text — not located; abstract only (NeurIPS virtual page, verified 200 and contents).
- EarlyCommit code — anonymised supplement, no public URL.
- LeRobot planned-hold latency on SO-101 — not measured anywhere (TODO experiment).
