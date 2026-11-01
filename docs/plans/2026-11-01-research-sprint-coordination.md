# Research Sprint Coordination Plan

Status: approved for setup on 2026-11-01. This plan coordinates evidence gathering; it does **not** select the research question or authorize experiments.

## Intent

The three-person team will independently challenge and refine candidate research directions before choosing one. The immediate objective is an evidence-backed short list by 14 November 2026, followed by a team decision no later than 21 November. Paper prose is written continuously in portable Markdown and later transferred into the verified conference LaTeX template.

## Approaches considered

1. Everyone researches the same idea in a shared document. Fast, but vulnerable to confirmation bias and edit conflicts.
2. Three independent branches, then one coordinator reconciles evidence. Slower at first, but preserves disagreement, produces an adversarial novelty check, and follows the repository's one-coordinator rule.
3. Three unrelated projects. Maximizes exploration but is too broad for the March submission timeline.

Chosen approach: **2**. The assistance-boundary question is the current candidate to challenge, not an adopted direction. H1 interruption repair and A+B hardware reliability remain valid alternatives until the team records a decision.

## File responsibilities

| Path | Responsibility |
| --- | --- |
| `TODO.md` | Current team-facing owner, branch, milestone, and acceptance board. |
| `logs/<date>-<owner>-<topic>.md` | Factual task record for each branch. |
| `knowledge/outputs/` | Per-task reports, matrices, and question proposals. |
| `knowledge/04-literature-map.md`, `05-gap-analysis.md`, `06-paper-story.md` | Shared syntheses. Only the appointed coordinator updates them after review. |
| `paper/` | Shared Markdown drafting sources. Each section has one writing owner per milestone; all claims link to evidence or run records. |

## Independent sprint assignments

| Owner | Proposed branch | Scope | 14 November acceptance artifact |
| --- | --- | --- | --- |
| Vivek | `research/vivek/assistance-boundary` | Primary-source map of direct help, clarification, waiting, abstention, human agency, and socially appropriate assistance. | Question proposal with nearest-neighbor matrix and source locations. |
| Sahil | `research/sahil/rq-red-team` | Adversarial novelty search: find work that invalidates the assistance-boundary candidate, H1, or A+B; identify strongest counterexamples. | Red-team report: closed claims, surviving narrow claims, and evidence status. |
| Rakesh | `research/rakesh/evaluation-feasibility` | Cheapest discriminating simulations/physical tasks, baselines, metrics, SO-101 constraints, and ethics/data implications. | Feasibility memo with a falsifiable hypothesis, cost, controls, and pivot criteria. |

Each person starts from current `main`, uses a separate worktree if writing concurrently, creates a task log, and writes only their own artifacts. Findings return to the coordinator; they do not concurrently update the shared literature map or paper story.

## Milestones

Dates are provisional and use the reported 1 March 2027 IROS paper deadline; reconfirm the official CFP before locking the submission plan.

| Milestone | Window | Decision/output | Paper-writing increment |
| --- | --- | --- | --- |
| M0: coordination | 1–3 Nov | Branches, evidence protocol, task logs, and shared writing structure ready. | Outline, claim discipline, and section ownership. |
| M1: independent discovery | 4–14 Nov | Three reviewed evidence reports and candidate-question proposals. | Problem framing and related-work evidence notes. |
| M2: convergence | 15–21 Nov | Team ranks 2–3 questions; records an adopted direction or explicit hedge. | Introduction problem statement, prior-art table, and contribution candidates marked provisional. |
| M3: design gate | 22 Nov–5 Dec | Falsifiable hypothesis, baselines, metrics, protocol, ethics/data decision, and cheapest simulation feasibility result. | Method/evaluation plan and limitations draft. |
| M4: minimum system | 6 Dec–5 Jan | Reproducible baseline and benchmark/task harness; no unrecorded reruns. | System description, figures-to-make list, and result-table shells. |
| M5: main evaluation | 6 Jan–2 Feb | Main experiments, controls, ablations, negative results, and analysis scripts. | Results and discussion updated only from run records. |
| M6: study/freeze | 3–16 Feb | Ethics-approved human study if applicable; otherwise final evaluation; freeze reported results. | Human-study/method detail, limitations, and abstract candidate. |
| M7: submission readiness | 17 Feb–1 Mar | Reproduction check, author review, venue compliance, and human submission. | Transfer reviewed Markdown into the official LaTeX template; final references and disclosures. |

## Paper-writing rules

- Write evidence-backed content throughout; no fabricated results, placeholder citations presented as facts, or prose that turns a proposed method into a result.
- `paper/sections/` is shared, but one person owns edits to any section in a milestone. Others submit comments or branch-specific drafts.
- Every quantitative statement links to a run record; every literature claim links to a reviewed source note or retains its `[V]`, `[S]`, or `[U]` status.
- Keep Markdown portable. The team will add the official LaTeX template only after verifying venue requirements in December.

## Third-party academic-research skills

The reviewed `Imbad0202/academic-research-skills` project is a useful reference, especially for claim/citation checks and review discipline. It is not added as a submodule or copied into this repository now: it is a large, fast-moving external suite and uses CC BY-NC 4.0. If a teammate wants it later, review a pinned revision, data flows, and license fit on a tooling branch; install only a selected Codex-native skill locally rather than making it a project dependency. This repository's `AGENTS.md` remains authoritative.

## Verification

- Verify Markdown links and repository policy checks on a supported Linux/WSL environment until the Windows workflow finding is resolved.
- Re-read this plan at M2. Amend future milestones rather than silently shifting dates.
