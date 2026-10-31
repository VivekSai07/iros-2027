# Research Workflows

Use these workflows from any client or manually. Every task has a human owner, a branch from main, a unique task log, an acceptance check, and a reviewed output. Rotate discovery, implementation, and review roles across the three teammates; do not encode people into permanent silos.

## 1. Start A Task

Read [current state](../knowledge/index.md) and recent [decisions](../knowledge/01-decision-log.md). Check the worktree before editing. Choose a branch such as `research/<owner>/<topic>`, `feat/<owner>/<method>`, `experiment/<owner>/<question>`, or `chore/<topic>`. For concurrent work use a separate worktree, not multiple writers in one checkout. Record the question, scope, budget, output paths, and cheapest acceptance check using the [task template](templates.md#task-record).

Use one coordinator per task. Independent agents may read different papers or inspect different modules. They return evidence and drafts to the coordinator; they do not all append to shared maps or write the vault concurrently. Across branches, keep per-paper and per-task files separate; reconcile shared indexes during review. Never auto-resolve conflicting scientific conclusions.

## 2. Literature Intake And Verification

1. Define a bounded query, date window, databases, inclusion/exclusion criteria, and budget. Log searches even when they find nothing. Deduplicate by DOI or arXiv ID/version.
2. Run Feynman in a unique job directory using [the tool runner](../tools/README.md), or search manually. Respect access restrictions, rate limits, and source licenses. Do not upload unpublished or participant data without approval.
3. Keep raw output and provenance together. Capture legally accessible source text in `knowledge/inbox/`; the vault adapter can preserve immutable captures locally. A summary is not a source.
4. Verify material claims against the primary paper, its exact version, supplementary material, and pinned code where available. Record page/table/equation or file/function references. [V] means the stated evidence was inspected, not that the whole paper is correct or reproduced.
5. Promote a reviewed [paper note](templates.md#paper-note) into `knowledge/wiki/sources/`. Use explicit [S]/[U] for gaps, label inference, link related concepts, and update the bibliography and literature map only after review.
6. Append a research-pass entry to [iteration log](../knowledge/07-iteration-log.md), record blocked sources in [access needs](../knowledge/08-open-questions-and-access-needs.md), and update gap/story documents only if conclusions changed.

Check novelty weekly while choosing a direction and before freezing the submission. No search result supports an unqualified "first" claim without a defensible comparison.

## 3. Paper-To-Code Audit And Reproduction

Pin the paper version, implementation URL/commit, license, checkpoints, environment, and data. Keep upstream checkouts under `.tools/papers/<paper-id>/`, not mixed into our source. Source-available implementations normally use Understand-Anything plus direct code inspection. Use REA only when artifact structure, binaries, or runtime behavior needs investigation; install a native analysis provider only when a specific question needs it.

Produce a [paper/code audit](templates.md#papercode-audit): trace each central equation/algorithm to its actual implementation, preprocessing, training loss, inference path, configurations, and evaluation. Separate documented behavior, inspected behavior, observed behavior, and unknowns. Graph summaries must be checked against code and are not novelty verdicts.

First reproduce a minimal upstream baseline with a CPU/small-data smoke check when feasible, then the agreed evaluation. Record exact commands and deviations. A missing source file is not proof the paper lacks a capability; an implementation default mismatch is not by itself a research contribution. Never run unknown checkpoints with unsafe deserialization or execute downloaded code on a connected robot without review.

## 4. Gap And Research-Question Gate

Build the nearest-neighbor comparison before proposing a method. A [question proposal](templates.md#question-proposal) must state the problem, whom it affects, primary-source limitations, falsifiable question/hypothesis, strongest counterexample, baseline, primary metric, practical significance, cheapest discriminating test, resource cost, and failure/pivot rule.

Discuss alternatives as a team. An agent may recommend, but only a recorded human decision adopts a direction. Append Q/A to [decision log](../knowledge/01-decision-log.md); update [current state](../knowledge/index.md). Keep rejected or invalidated gaps visible with reasons. Do not treat the historical H1 story as selected merely because it has more notes.

## 5. Method And Framework Development

Create a branch from main and a short design tied to the adopted question. Keep reusable components in `src/`, configuration in `configs/`, and experiment-specific orchestration in `experiments/<experiment-id>/`. Choose the framework and dependency lock when needed; no empty robotics stack is preselected.

Write a focused failing check, implement the smallest change, rerun it, and then run relevant regression checks. Inspect paper/code differences before changing borrowed algorithms. Preserve license notices and source attribution. Record expected failure behavior and safety limits, not just the happy path.

## 6. Data Collection

Before collection approve the [dataset card](templates.md#dataset-card): provenance/license, sensors/calibration, units and clocks, schema, sampling, annotation rules, quality checks, immutable split definitions, exclusions, storage/access, and retention. Separate train/validation/test by the leakage unit (for example person, scene, session, object, or trajectory), not blindly by frame.

Pilot collection and validation before scaling. Preserve raw data and write transformations as code. Store local payloads in `data/raw/` and `data/processed/`; identities and consent material belong in restricted storage, never Git. Record checksums, versions, access instructions, and storage URIs without credentials. Select a team-accessible artifact backend before multi-person collection. DVC or a dataset registry is optional once that backend and access policy are agreed.

Human studies require the appropriate ethics approval, informed consent, participant withdrawal/retention process, and access control before recruitment or recording. Real-robot runs require a named supervisor, approved workspace limits, a tested emergency stop, calibration, and an explicit safe-stop procedure. Simulation success is not hardware authorization.

## 7. Experiments And Results

Before a run, fill an [experiment protocol](templates.md#experiment-protocol) and reserve shared resources in [the resource log](../logs/resources.md). Predeclare baseline parity, controls/ablations, primary metric, sample-size rationale, exclusion rules, uncertainty estimates, seeds/splits, timeout, budget, and stopping criteria. Pilot outcomes may change the design, but record changes before confirmatory runs.

Use a unique run ID. Commit a [run record](templates.md#run-record) in `results/<experiment-id>/<run-id>/`; store heavy payloads in `artifacts/<run-id>/`. Record the commit, dirty status/patch reference, dependency lock, data/config hashes, command, hardware, timestamps, completion status, and all seeds. Prefer clean commits for reported runs. Preserve failures and negative findings. Never overwrite a completed run or silently alter its inputs.

Generate metrics, figures, and tables from recorded data with scripts. Report uncertainty and the actual experimental unit; avoid pseudoreplication and train/test leakage. Have a teammate reproduce at least one reported result from its manifest. Link every paper result to its run IDs and analysis command.

## 8. Knowledge Maintenance And Handover

Use claude-obsidian's preview/transaction flow for managed vault changes. Agents draft separately; one coordinator applies a reviewed transaction. If a note changes concurrently, stop and reread instead of forcing a write. Keep private runtime journals and locks local; preserve shareable sources, provenance, linked notes, and task logs in Git. Do not enable Git auto-checkpoints or graph post-commit auto-updates that conflict with repository policy.

End each task with [a handover](templates.md#task-record): what changed, checks actually run, remaining uncertainty, blockers, next command, and artifact links. Update shared indexes sparingly; use per-task files to reduce merge conflicts. A log is factual coordination, not a transcript or private reasoning dump.

## 9. Review, Merge, And Submission

Run lightweight repository checks and the touched code's tests. Review source licenses, secrets/privacy, evidence claims, reproducibility, and the diff. Inform the user before a local commit; use a plain commit message and existing human Git identity.

Present the branch and checks to the user. Only after explicit approval merge with `git merge --no-ff <branch>`. Resolve conflicts semantically and rerun checks. Never push; the human does that. See [setup](setup.md) for optional hooks and hosting protections.

Before submission, reverify official venue dates and formatting, authorship order, ethics/data permissions, related-work freshness, claim-to-evidence mapping, figure provenance, supplementary reproduction instructions, and any required tool-use disclosures. Anonymize the submission and public artifacts as required without destroying the internal research record. Humans approve submission and publication.