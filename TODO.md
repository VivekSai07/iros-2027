# Team TODO — Direction Selection Sprint

Status: active. The research direction is **OPEN** until the team records a decision.

## Team board

| Owner | Branch | Current task | Due | Done when |
| --- | --- | --- | --- | --- |
| Vivek | `research/vivek/assistance-boundary` | Map primary work on direct help, asking, waiting, refraining, agency, and social appropriateness. | 14 Nov 2026 | A source-located question proposal and nearest-neighbor matrix are in a unique output/report file. |
| Sahil | `research/sahil/rq-red-team` | Red-team the assistance-boundary candidate, H1 interruption repair, and A+B; preserve invalidated claims. | 14 Nov 2026 | A report names the strongest counterexamples, what is closed, and what survives with `[V]`/`[S]`/`[U]` evidence. |
| Rakesh | `research/rakesh/evaluation-feasibility` | Define the cheapest discriminating task, metrics, baselines, simulation/hardware needs, and ethics/data gates. | 14 Nov 2026 | A feasibility memo includes hypothesis, controls, primary metric, budget, and failure/pivot rule. |

## Rules for this sprint

- Start each task from current `main`; use a topic branch and separate worktree for concurrent writers.
- Give every task a unique `logs/<date>-<owner>-<topic>.md` record.
- Keep branch reports separate. Only the appointed coordinator updates `knowledge/04-literature-map.md`, `05-gap-analysis.md`, `06-paper-story.md`, or `knowledge/index.md` after review.
- A paper, simulator, dataset, robot run, human study, and third-party tool installation each need their own workflow gate; none is authorized merely by this TODO.
- Do not merge or push. A human reviews, approves the named branch, and publishes.

## Milestones

| ID | Dates | Checkpoint |
| --- | --- | --- |
| M0 | 1–3 Nov | Coordination plan, branches, task logs, and shared paper-writing space are ready. |
| M1 | 4–14 Nov | Independent evidence reports complete. |
| M2 | 15–21 Nov | Team ranks candidates and records a direction or hedge. |
| M3 | 22 Nov–5 Dec | Research design and simulation feasibility gate. |
| M4 | 6 Dec–5 Jan | Minimum system and reproducible baselines. |
| M5 | 6 Jan–2 Feb | Main evaluation and ablations. |
| M6 | 3–16 Feb | Ethics-approved study if applicable; otherwise final evaluation and freeze. |
| M7 | 17 Feb–1 Mar | Reproduction, venue checks, LaTeX transfer, and human submission. |

## Shared writing, every milestone

Use [paper/](paper/README.md) for portable Markdown prose. Each milestone must improve at least one section, and every claim must remain linked to reviewed evidence or a run record. One owner edits a given section per milestone; others use branch drafts or comments.

## Later decision: academic-research skills

The team may review a pinned, Codex-native subset of [academic-research-skills](https://github.com/Imbad0202/academic-research-skills-codex) on a tooling branch. Do not add it as a submodule or project dependency without a license, data-flow, and workflow-policy review.
