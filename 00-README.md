# IROS 27 — research project index (agent entry point)

Team: 3 people, robotics background (contact.sparclab@gmail.com, Europe/Berlin).
Goal: a unique, understandable, best-paper-aspiring **application paper** (else systematic study) at **IROS 2027** (Florence, 26 Sep–1 Oct 2027; paper deadline **1 March 2027**, hard).
Hardware/compute: SO-101 arm(s); one shared 48 GB RTX 6000 Ada; everyone else has 8 GB GPUs. Strong sim skills (Isaac Sim/Lab, Newton, MuJoCo).
Reusable stack: LeRobot with SO-101 rollout.

## Reading order for an agent
1. `00-README.md` (this file)
2. `01-decision-log.md` — append-only; what was decided and why. Never edit old entries; supersede.
3. `02-iros-2027-constraints.md` — calendar, award categories, scoop-risk context
4. `03-candidate-directions.md` — A, B, C, H1, H2 and their status
5. `05-gap-analysis.md` — which gaps are still open after 5 literature iterations (READ the "invalidated gaps" section)
6. `06-paper-story.md` — current reconstructed story, RQs, experiments
7. `04-literature-map.md` + `refs/bibliography.md` — per-paper findings with verified/unverified flags
8. `07-iteration-log.md` — how the research was done (queries, what each iteration changed)
9. `08-open-questions-and-access-needs.md` — what we need from the humans
10. `09-session-handover.md` — chat-session handover: timeline, state, next steps, tooling notes
11. `10-research-map-and-implementation.md` — Mermaid maps: covered vs missing, focus options, implementation structure, timeline
12. `outputs/` — Feynman reports (G1, G2, G4, comparison, paper summaries); check each file's status header

## Rules (from the user)
- Use proper sources/searches. **If a site cannot be accessed, do not skip or work around it — ask the user for access / a manual check** (e.g. ELLSA GitHub returned ROBOTS_DISALLOWED; user must check release status).
- Every claim in the literature map carries a status: `[V]` verified from the primary page/abstract, `[S]` secondary source only, `[U]` unverified.
- Log decisions in `01-decision-log.md` (append-only, Q/A style).
- Never write pasted tokens/secrets into files.

## Status (2026-10-13)
- Chat handover in `09-session-handover.md` (2026-10-18).
- 5 literature iterations done. Direction still **undecided** — team must choose (see decision log D-009 and `06-paper-story.md`).
- Leading candidate: **H1-benchmark+method** ("say it mid-motion": interruption/repair benchmark for manipulation + low-cost learned repair + human validation).
- Hedge: two-week sprint to 24 Oct (SO-101 repeatability test for A+B; minimal H1 interruption demo; novelty re-check).
- Fallback venue: ICRA 2028 (deadline ~16 Aug 2027).
