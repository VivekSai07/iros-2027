# Decision log (append-only)

Convention: chronological, Q/A format. Supersede earlier entries by adding a new one; never edit old ones.

---
## D-001 — 2026-10-08 — Goal and constraints
**Q:** What are we trying to do? **A:** Publish at the next IROS (IROS 2027). Three-person robotics team, SO-101 hardware, prior imitation-learning experience.

## D-002 — 2026-10-08 — Prior work scope
**Q:** Is earlier policy-comparison work part of the paper? **A:** No. The new research must be related to who we are and what hardware we have.

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
**Q:** Where does this work live now? **A:** In its own folder under version control. Older entries (D-005, D-011) and `09-session-handover.md` still say `iros27-research/`; they are historical and not edited. Commits are authored by the human (`sahilrajpurkar03`), never an agent.
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

## D-015 — 2026-10-18 — ELLSA release status resolved (supersedes the unknown in D-007)
User supplied the ELLSA branch README (`inputs/ellsa-readme.md`). Code, training scripts, evaluation scripts, the ELLSA checkpoint, test data and training-data transcripts are released (HuggingFace links); there are no GitHub releases. Heavy stack (Llama-3.1-8B + Emu3 + UniVLA + CosyVoice2), LIBERO simulation only, no SO-101 or real-robot support stated, and no dedicated barge-in eval script or test set is mentioned. Consequence: ELLSA is usable only as a LIBERO-sim reference baseline (needs the 48 GB GPU; not on 8 GB machines); it is not a feasible SO-101 baseline. Whether its barge-in test data is among the released test data is still [U]. RIAP full text and the RTCA workshop list remain pending.

## D-016 — 2026-10-18 — RIAP full text read (supersedes the "details unverified" caveats in D-008 and G1 §6)
User supplied the RIAP PDF; notes in `inputs/riap-notes.md`. It is a NeurIPS 2026 workshop paper whose 8,160 trials are synthetic semantic-evidence replay (no speech audio, no physics, no humans); its 30-participant study rates a browser mobile-base task and compares system bundles; code is not released; WAIT cannot brake motion already in progress. RIAP therefore does not cover post-onset spoken corrections: it is not a G1/G2 competitor. G3 (commit timing) stays invalidated. `06-paper-story.md` positioning row and `04-literature-map.md` updated.

## D-017 — 2026-10-18 — RTCA workshop accepted list read (resolves the blocked item in G1 §7 Q3)
User supplied the 37 accepted posters (`inputs/rtca-accepted.md`; the page may continue beyond what was pasted [U]). Triage from titles only: no paper on robot manipulation with spoken interruption; RIAP (read in full, D-016) and The Puppet Test (nonverbal HRI) are the only robot-related ones. Titles to abstract-check later: Continue/Adapt/Yield (already G1's Duplex Cue), Cancelled Tools / Stopping Superseded Tool Calls (software analogs of residual effects), Dual-State KV Forking, From Text to Voice (interruption recovery), Hear2Act, Multi-Party Backchannel Prediction. G1 scoop risk from this workshop is lowered; overall G1 scoop risk stays HIGH because of the 11 other adjacent papers (Sep-Oct 2026).

## D-018 — 2026-10-18 — Moved to a standalone repository (`iros27-hri`)
**Q:** Why a new repo? **A:** IROS 2027 is a serious effort and must not share a repository with unrelated earlier work. The folder was extracted with its 5 commits and authorship preserved; files now live at the repo root (older entries that mention a folder path are historical). References to the earlier project were removed. No remote yet; local only. Repo name is provisional.

---
## D-019 — 2026-10-31 — Shared research workspace and collaboration policy
**Q:** Is the earlier literature or H1 recommendation final? **A:** No. The team is still discussing the problem statement and research question. Repository setup does not select a direction or methodology, reverify literature, or claim experimental outcomes.

**Q:** How is the repository organized? **A:** The user approved a research monorepo with a shared knowledge area, reusable code, configurations, experiments, dataset manifests/local payloads, results, manuscript material, documentation, task logs, and pinned tool integrations. Existing numbered research documents plus inputs/notes/outputs/refs were moved together under `knowledge/`, preserving relative paths and original contents before these append-only updates. The existing power experiment was not changed. Root `README.md`, `AGENTS.md`, and `knowledge/index.md` are the new entry points. This supersedes earlier location/setup descriptions without erasing them.

**Q:** What does "no AI footprint" mean? **A:** The user explicitly clarified: it applies to commit messages. No AI branding, generated-by text, AI trailers, or AI co-authorship in commits. Agent configuration, tool provenance, and useful task logs may be tracked. Third-party licenses and required research disclosures remain intact.

**Q:** What may agents do with Git? **A:** Inform the user and make local commits without asking, using the existing human Git identity. Start features/methods/tasks on branches from main. Never push. Merge only after explicit approval of the named branch, always with `--no-ff` and a retained merge commit. Implementation approval is not merge approval. Use separate worktrees for concurrent writers. Local hooks are safeguards, not proof of human authorization.

**Q:** How do Claude, Codex, and Copilot share instructions? **A:** Root `AGENTS.md` is canonical. Claude imports it; Copilot's entry point references it; Codex reads it directly. The portable research-workflow skill is stored once and linked to client discovery directories. Shared artifacts and logs, not private chat memory, carry state.

**Q:** How are the requested tools included? **A:** Versioned integration code, source pins, dependency lock, and workflow routes are tracked. Pinned source checkouts are local under `.tools/`; heavy payloads and credentials are not tracked. claude-obsidian's vault foundation is initialized and checked. Understand-Anything and the reference catalog are checked out; no graph or native analysis was run. Feynman and REA package versions are pinned, but activation is gated after npm reported upstream dependency advisories (7 moderate, 3 high affected package entries). Human risk review or a reviewed upstream update is required before activation. No paid research or authentication was performed. See `../tools/README.md` for exact status and primary upstream links.

**Q:** What remains a team decision? **A:** The RQ/method, individual task ownership, shared artifact backend, dataset/participant permissions, experiment budgets, repository release license, and conference requirements. Setup does not silently decide them.

## D-020 — 2026-10-31 — Feynman and REA activated; reverse-engineering catalog removed
**Q:** Should the gated Feynman/REA runtimes be set up despite the npm advisories (7 moderate, 3 high affected entries, D-019)? **A:** Yes; the maintainer asked for both to be set up. This is a bounded exception for the pinned versions (Feynman 0.5.61, REA 6.8.0): public papers, public repositories, and team-owned non-sensitive artifacts only; no participant data, credentials, unpublished third-party material, or untrusted network services. Recheck advisories whenever pins change. Supersedes the "no exception granted" status in D-019.

**Q:** Keep awesome-reverse-engineering? **A:** No. The maintainer removed it because REA covers the team's reverse-engineering needs. Pin, local checkout, and references were removed.

**Q:** How are the tools exposed to clients? **A:** REA's MCP server is registered at project scope for Claude (`.mcp.json`) and VS Code (`.vscode/mcp.json`); Codex needs a per-user `codex mcp add` because Codex 0.160.1 did not load a project config here. Feynman is a CLI used through `tools/run_tool.py`; each teammate authenticates their own model provider. No research job or native analysis was run.

**Q:** Merge? **A:** The maintainer approved a local merge of `chore/research-workspace` into main with `--no-ff`; the maintainer pushes.
