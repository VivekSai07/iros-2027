# Research Workspace Implementation Plan

**Goal:** One reproducible research workspace for three collaborators, with the research question still open.

**Architecture:** Git owns code, configuration, evidence, small results, and documentation. The knowledge directory is a normal Markdown/Obsidian vault. Pinned external tools live in ignored local directories; credentials never enter version control.

**Stack:** Markdown, Git, Python standard-library checks, opt-in upstream CLI/plugin installations.

## Approved Constraints

- Preserve existing research and its verification flags; migration is not a fresh literature verification.
- The user approved the design and implementation without additional design checkpoints.
- No AI attribution or branding in commit messages or AI co-authorship trailers. Configuration and task logs may name tools.
- Local commits are allowed after informing the user. No agent pushes.
- Branch from main. Merge only with explicit user approval and a non-fast-forward merge commit.
- Do not select a research direction, run paid searches, collect participant data, or operate hardware during setup.
- Preserve third-party licenses and required publication disclosures.

## 1. Repository And Commit Policy

- [x] Inspect current research, instructions, upstream READMEs, and clean main branch.
- [x] Create and switch to `chore/research-workspace` from main.
- [x] Run the new commit-message tests and confirm they fail before the guard exists.
- [x] Implement the guard and opt-in repository hooks; run `python3 -m unittest discover -s tests -v`.
- [x] Move numbered research files plus inputs, notes, outputs, and refs into knowledge, preserving relative paths.
- [x] Compare migrated file bytes against main, allowing only explicitly documented append-only log updates.
- [x] Add root README, canonical AGENTS policy, thin Claude/Copilot entry points, and local Git setup instructions.

## 2. Research Workflows And Tool Integration

- [x] Create a workflow handbook and templates for literature evidence, paper/code audit, RQ proposal, experiment, dataset, run record, and handover.
- [x] Add purpose-specific directories without choosing a robotics framework or implementing a research method.
- [x] Record exact source revisions and package versions for all five requested tools.
- [x] Add opt-in setup commands, isolated output paths, and client registration examples using upstream-documented interfaces.
- [x] Add a shared research skill; all clients must use the same handbook and canonical policy.
- [x] Keep model authentication, heavy artifacts, vault runtime locks, and personal editor state untracked.
- [x] Smoke-test locally available integrations without paid calls; record missing prerequisites explicitly. Vault checks passed; optional CLI activation is intentionally gated by dependency advisories, with no risk exception granted.

## 3. Verification And Handover

- [x] Run unit tests, repository/link/config checks, and Git whitespace validation.
- [x] Exercise hooks with temporary Git repositories, including main-branch protection and valid merge commits.
- [x] Append the repository decision and tooling pass to the research logs; publish a current-state index and task handover.
- [ ] Review the final staged changes and local commit metadata.
- [ ] Inform the user, make a plain-message local commit, and leave the branch unmerged and unpushed.

## Acceptance Checks

The initial literature and existing power experiment survive migration; current state does not adopt H1. Each tool has a reproducible integration route and an honest tested/configured status. The three agent entry points resolve to one policy. A fresh clone can run lightweight checks without credentials, GPU access, network access, or upstream plugins. Hooks are local safeguards, not proof of human approval; remote protections require owner configuration.