# Decision log (append-only)

Convention: chronological, Q/A format. Supersede earlier entries by adding a new one; never edit old ones.

---
## D-001 — 2026-10-08 — Goal and constraints
**Q:** What are we trying to do? **A:** Publish at the next IROS (IROS 2027). Three-person robotics team, SO-101 hardware, imitation-learning experience from the earlier warm-up.

## D-002 — 2026-10-08 — Warm-up scope
**Q:** Is the policy comparison (ACT/SmolVLA/etc.) part of the paper? **A:** No. It was only a warm-up. The new research must be related to who we are and what hardware we have.

## D-003 — 2026-10-08 — Paper type, compute, novelty bar
**Q:** Paper type? **A:** Application paper preferred; otherwise a systematic study.
**Q:** Compute? **A:** One shared 48 GB RTX 6000 Ada; everyone else has 8 GB.
**Q:** Bar? **A:** Unique, understandable, stands out across multiple applications, aims for best-paper-level, fits an IROS category, no copying of existing papers. Team is strong in simulation (Isaac Sim/Lab, Newton, MuJoCo).

## D-004 — 2026-10-10 — Friends' inputs recorded
- Rakesh: full-duplex speech-to-speech HRI. Gemini-sourced list: ELLSA, VoxMind, "Decoupling Conversational Dynamics…", Easy Turn, ICLR 2025 turn-taking benchmark.
  - Corrections: "Decoupling…" is an RL framework (DuplexPO) separating *when* to speak from *what* to say; VoxMind is spoken tool use (not robotics); benchmark's real title is "Talking Turns".
- Vivek: "DUM-E" (team's own framing; fictional Iron Man character) — context-aware assistant, intent-aware manipulation, expressive manipulation; six-thesis table incl. "Knows When NOT to Help"; cites Karcini et al. 2026 (arXiv 2606.06556). arXiv 2406.13787 is LIT (sous-chef intention tracking), not DUM-E.

## D-005 — 2026-10-13 — Project setup
**Q:** Create a Claude Project and move this work there? **A:** Session is attached to Project "IROS 27". Docs live in the project (via project_write) and mirrored locally in `iros27-research/`.

## D-006 — 2026-10-13 — Research protocol
5 literature iterations covering findings/methods/experiments/related work; open research per paper; story arrangement; gap analysis; gap reconstruction. Access rule: do not skip inaccessible sources — ask the user.

## D-007 — 2026-10-13 — Access blocker: ELLSA code
ELLSA GitHub page fetch returned ROBOTS_DISALLOWED. Not bypassed. **Action for user:** check github.com/bytedance/SALMONN (branch ELLSA) for released code/checkpoints/barge-in data. Needed to decide if ELLSA is usable as a baseline (it is ~2×8B, LIBERO sim only → likely not directly usable on SO-101).

## D-008 — 2026-10-13 — Iteration 5 result: a gap was invalidated
The earlier gap "timing/commit as a decision variable for speech-driven manipulation" (G3) is **already covered** by RIAP (NeurIPS 2026 listing) and Premover (2605.12160). User-validated interruption is also partly covered by SocialVLA (n=15), CMU HRI 2026 (n=18 older adults), MICoBot (18 participants). We must not claim these as novelty.

## D-009 — 2026-10-13 — Direction: OPEN, recommendation made
Recommendation (not yet accepted by team): **H1-benchmark+method** — a time-anchored speech-overlap interruption benchmark for manipulation with a physical failure taxonomy, a low-cost learned mid-motion repair method (no stop/retract), and validation that benchmark scores predict human-rated fluency. Hedge: 2-week sprint to ~24 Oct (A+B repeatability go/no-go; minimal H1 demo; novelty re-check). Fallback venue ICRA 2028.
**Pending:** team choice among H1 / H2 / A+B.

---
## D-010 — 2026-10-18 — Feynman research agent
**Q:** Install github.com/companion-inc/feynman? **A:** Not installable in the cloud sandbox (npm registry blocked by policy; not bypassed). The linked-computer shell is a Linux VM, so it cannot install on the user's Windows PC. User to install locally (`npm install -g @companion-ai/feynman`, `feynman setup`; telemetry off via `FEYNMAN_TELEMETRY=off`). Results to be merged into the literature map when available.

## D-011 — 2026-10-18 — Move project to VS Code
**Q:** Can the project move to VS Code? **A:** Yes. Folder packaged as `iros27-research.zip` with `CLAUDE.md`/`AGENTS.md`; the VS Code folder becomes the source of truth; project-copy sync is manual. Chat handover added as `09-session-handover.md`.

---
## D-012 — 2026-10-18 — Folder rename and Feynman adoption
**Q:** Where does this work live now? **A:** Folder renamed `iros27-research/` -> `literature-review-iros27-sahil/` in repo `learning-methods-so101`, branch `research/literature-review`. Older entries (D-005, D-011) and `09-session-handover.md` still say `iros27-research/`; they are historical and not edited. Commits are authored by the human (`sahilrajpurkar03`), never an agent.
**Q:** Feynman? **A:** Installed (v0.5.49, npm global), Anthropic model, alphaXiv signed in. One-shot runs via `feynman --prompt="/lit ..."` from this folder write to `outputs/`. Running six in parallel hit an Anthropic rate limit (HTTP 429): run at most 1-2 at a time and watch usage (user asked to pause and ask at 75% weekly).

## D-013 — 2026-10-18 — Iteration 6-7 findings (supersede gap statuses in D-009 where they differ)
- G1 stays open only as a conjunction (spoken x phase-anchored x manipulation x repair taxonomy x human validity); nearest competitors SocialVLA, Causeway+LIBERO-MAX, ARMS. Scoop risk high.
- G2 broad claim is closed (SwitchVLA, ReSteer, Causeway do text switching without retract). Surviving wedge: speech-triggered, prefix-aware in-flight chunk retargeting on SmolVLA/SO-101.
- G4 must be scoped narrower (Song et al. 2607.00530 already ran n=24 spoken-command study on Dobot). Use a trial-level design.
- Correction: RIAP unsafe commits fell 27.5% -> 1.6%, not 0%.
- Direction still not chosen by the team. See `10-research-map-and-implementation.md`.

## D-014 — 2026-10-18 — Paper story v2 adopted; RTC audit result
`06-paper-story.md` replaced by v2 (conjunction novelty claim, wedge-specific C2, baselines B1-B6 with SmolVLA-only repair claims, operational metrics, C3 as a trial-level hypothesis with human ratings as criterion, scoop risk HIGH). Previous version kept as `06-paper-story-v1-2026-10-13.md`. Source: `outputs/paper-story-review.md`.
RTC-vs-LeRobot audit (`outputs/rtc-smolvla-lerobot-audit.md`): RTC runs on SmolVLA in LeRobot main (146d847) but defaults differ from the paper (identity Jacobian instead of VJP, beta 10 vs 5, LINEAR vs EXP schedule, 10-step guided region); a no-hold retarget path, immediate re-request on task change and per-request guidance profile are missing. G2 wedge judged feasible, 1-2 weeks to a bench-validated prototype [U estimate]. Direction choice (H1/H2/A+B) is still the team's.
