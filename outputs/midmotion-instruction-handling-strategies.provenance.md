# Provenance — midmotion-instruction-handling-strategies

- **Date:** 2026-10-18 (original run interrupted by HTTP 429 before verify/deliver; finished in a resumed session without redoing the research)
- **Workflow:** /compare (source comparison)
- **Final artifact:** `outputs/midmotion-instruction-handling-strategies.md` (Status: COMPLETE). The plan named `...-comparison.md`; the user's resume instruction set the path used here.
- **Plan:** `outputs/.plans/midmotion-instruction-handling-strategies.md`
- **Research notes (unchanged, not re-run):** `outputs/.drafts/midmotion-instruction-handling-strategies-R1.md` (ELLSA, VITA-E, Hi Robot, SwitchVLA), `-R2.md` (Causeway, Premover, RIAP, EarlyCommit, SocialVLA, MIRA), `-R3.md` (RTC, LeRobot async, SmolVLA/ACT)
- **Draft:** `outputs/.drafts/midmotion-instruction-handling-strategies-draft.md`
- **Verification report:** `outputs/.drafts/midmotion-instruction-handling-strategies-verification.md`
- **Revised text:** `outputs/.drafts/midmotion-instruction-handling-strategies-revised.md` (final artifact = this file + COMPLETE status line; body identical, checked with `diff`)

## Sources
- Systems compared: 12 (ELLSA, VITA-E, Hi Robot, SwitchVLA, Causeway, Premover, RIAP, EarlyCommit, SocialVLA, MIRA, RTC, LeRobot async) plus SmolVLA, ACT and VLASH as context.
- arXiv IDs checked via the arXiv export API: 13/13 resolve to the named titles.
- Non-arXiv URLs checked via `curl -L`: 12/12 return HTTP 200 (titles matched where pages expose a title; RIAP NeurIPS page abstract text matched); `github.com/VITA-MLLM/VITA-E` returns 404, as the report states.
- Primary-text spot-checks: Hi Robot §4.1/§4.2/App. B.3; SwitchVLA Tables 1, 3, 11 and intro refs [12–16]; VITA-E related work, §results, README; SocialVLA latency table (b); MIRA §fast gate, §RHPC, Table 3; ELLSA Table 3(c) (page-9 screenshot) and per-block latency table; Causeway §V-d; RTC §setup, Fig. 1, delay results; Premover App. H and limitations; EarlyCommit §judge/§speed/§limitations; SmolVLA async table; LeRobot main README + `inference/{base,sync,rtc}.py`, `remote_inference/engine.py`, `rollout/interactive.py` (fetched 2026-10-18 from `main`).

## Verification result
- FATAL 0 · MAJOR 3 · MINOR 9, all applied (checked by grep/diff of the revised file).
- MAJOR fixes: (M1) LeRobot "fresh replanning can lose task progress" quote moved to its actual context (VQA/language waits), and the retarget case re-flagged [U]; (M2) headline absence claim re-flagged [U] (synthesis over the compared set), and the unsupported "slow hierarchy" wording removed; (M3) LeRobot no-pending-inference path added (buffered old-task actions keep executing), with the taxonomy updated.

## Blocked / open
- ELLSA GitHub (`bytedance/SALMONN` ELLSA branch) is blocked by robots.txt (D-007); not accessed.
- RIAP: only the abstract is available; no full text.
- EarlyCommit code: anonymised supplement, no public URL.
- Cells not re-checked this pass (researcher-note [V] kept): listed under "Open" in the final artifact.
- Not measured anywhere: LeRobot planned-hold latency on SO-101, and progress loss on retarget (TODO experiments).

## Integrity
- No numbers were reproduced experimentally. All quantitative cells are quoted from the sources listed above.
- No subagents were spawned in the resumed session. No broad new searches were run. No files outside `outputs/` were edited.
