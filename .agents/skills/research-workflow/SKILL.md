---
name: research-workflow
description: "Use when doing literature review, paper implementation audits, novelty or research-question evaluation, methodology development, dataset collection, experiment analysis, paper preparation, or research handover in this repository."
---

# Research Workflow

Read [shared policy](../../../AGENTS.md) and [current state](../../../knowledge/index.md). Select the relevant section of the [workflow handbook](../../../docs/workflows.md) and its [record template](../../../docs/templates.md). Name the output path and acceptance check before acting.

Route tools through [the integration guide](../../../tools/README.md):

- Literature: Feynman in a unique job directory; keep provenance and verify before promotion.
- Shared knowledge: pinned claude-obsidian skills and portable CLI; one coordinator applies reviewed writes.
- Source implementation: pinned Understand-Anything skill and direct source checks. Explicitly select this checkout's plugin root and the target paper repository; set `UNDERSTAND_NO_WORKTREE_REDIRECT=1`. No post-commit auto-update.
- Artifact/runtime questions: REA only where justified and authorized; the reference catalog helps select a tool, not a novelty claim.

Do not activate the gated CLI dependencies without human risk approval. Do not treat source installation as authentication, backend readiness, successful reproduction, or proof of novelty. Keep the research question open until a recorded team decision.

An inspected primary abstract may support a [V, abstract] claim within its scope. That does not verify paper-wide details or novelty; those remain [U] or explicitly labeled inference until the relevant evidence is checked.

Use separate worktrees for concurrent writers. End with a factual task log, checks actually run, evidence status, blockers, and next action. Local commits are permitted after notice; merges require user approval and `--no-ff`; agents never push.