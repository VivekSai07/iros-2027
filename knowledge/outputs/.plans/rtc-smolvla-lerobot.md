# Audit plan: rtc-smolvla-lerobot (2026-10-18)

Paper: Real-Time Execution of Action Chunking Flow Policies (RTC), Black, Galliker, Levine — arXiv 2506.07339 (Physical Intelligence).
Repo: huggingface/lerobot main, shallow clone (depth 1) into outputs/.tmp-lerobot (deleted at end). Optional: PI real-time-chunking-kinetix reference repo, read via raw.githubusercontent only if needed.

Constraints from user: no subagents (overrides template's researcher/verifier requirement; verification done by me with grep/line numbers), no broad web search, edit only under outputs/.

Claims to check:
1. RTC for SmolVLA: guidance weight schedule (paper eq. for W: 1 for i<d, exponential decay over overlap, 0 after H-s), inference delay d, prefix mask, soft masking, max guidance weight beta (paper default β=5), number of denoising steps, ΠGDM guidance form (r_τ^2 / clipping). Defaults in LeRobot config.
2. Action queue: location, truncation/merge on new chunk, leftover handling, execution_horizon clamp; set_task semantics (hold, queue.clear, ack, task_version).
3. Language embedding: recomputed per chunk? (SmolVLA prepare_language / embed_prefix; any KV cache of the prefix across chunks.)
4. Hooks needed for "truncate to k + re-denoise under new instruction with RTC prefix guidance, no hold": files/functions, effort.
5. ACT: language input? RTC support?
6. Issues/PRs mentioning RTC + instruction change: grep repo (docs, README, changelog, TODOs); GitHub issue search via API only if narrow and allowed; else mark blocked/unverified.

Output: outputs/rtc-smolvla-lerobot-audit.md, [V]/[S]/[U] flags, Sources.

## Task ledger
- [x] paper read (alpha)
- [x] clone + map files (main @146d847)
- [x] Q1..Q6
- [x] write artifact, self-verify line refs (spot-checked)
- [x] delete clone (verified gone)

Verification log: M1 identity-Jacobian checked analytically vs repo test expected value (1.80) and corroborated by open PR #4945. No experiment run (torch not installed).
