# Repository audit — 2026-11-01

Scope: repository structure, collaboration safeguards, local/remote verification, research provenance, and current-state consistency. This audit did not change implementation, policy, or scientific conclusions. Base: `main` at `111f1d3`; task branch: `research/codex/repo-audit-rq`.

## Executive assessment

The repository has unusually strong governance for a two-day-old research workspace: a canonical agent policy, explicit Git authority boundaries, task/experiment/data templates, immutable tool pins, negative-result preservation, and an honest `Direction: OPEN` state. The main weaknesses are cross-platform operability and research-evidence maturity, not folder structure.

The repository is suitable as a shared research workspace after the team resolves the high-priority items below. It is not yet a publication-ready evidence base: the managed source/claim ledgers are empty, legacy claims have not been reverified, and several synthesis documents contain stale resolved actions.

## Findings

### High — The documented local workflow does not work in this Windows checkout

- The required `python3` commands resolve to the Microsoft Store application-alias stub and exit `9009`; `python` is the working interpreter (`Python 3.11`).
- Four of 16 tests fail/error when invoked with `python -m unittest discover -s tests -v`. The commit-message hook hard-codes `python3`; the direct pre-push test invokes bare `bash`, which resolves to WSL while receiving a Windows `C:\...` path.
- `tools/check_repo.py` fails because `.claude/skills` and `.github/skills` are Git symlinks but this clone has `core.symlinks=false`. Git stores them correctly as mode `120000`; the Windows worktree materializes them as one-line regular files, so `<adapter>/research-workflow/SKILL.md` does not exist.
- Ubuntu CI for `111f1d3` passed on 2026-10-31 [V, public GitHub Actions], so this is a platform-boundary defect rather than evidence that the Linux checks are broken.

Impact: Windows-native collaborators cannot rely on the hooks, client skill adapters, or advertised verification commands. Decide whether the supported environment is strictly a WSL/Linux clone or make the hooks, adapters, tests, and setup instructions Windows-aware. Add a Windows CI job if Windows-native use is supported.

### High — The public repository exposes high-scoop-risk research drafts

The remote is publicly readable [V, public GitHub repository] and contains detailed provisional contribution claims, competitor matrices, implementation sketches, and fallback strategy. The repository itself rates the H1 scoop risk as high. No project-wide release license has been selected.

Impact: this may be intentional, but it is a research-strategy and disclosure decision the three authors should make explicitly. If public visibility is not intentional, repository visibility and already-published history require human review; an agent must not rewrite or delete remote history. If it is intentional, add a concise repository description and decide licensing/distribution terms.

### High — Scientific provenance is structured but not yet promoted to claim-level evidence

- `knowledge/wiki/meta/ledgers/source-ledger.json` and `claim-ledger.json` are empty.
- `knowledge/index.md` correctly says migrated reports were not reverified. Many historical `[V]` statements rely on generated reports or abstract-level checks rather than reviewed paper notes with exact page/table/equation locations.
- Historical raw notes and provenance files are valuable, but they are not a substitute for primary-source claim records.

Impact: do not copy the existing novelty matrix or paper story into a submission as established fact. Promote only the nearest competitors and central claims through reviewed paper notes first.

### Medium — Current-state drift can mislead new collaborators

- `knowledge/10-research-map-and-implementation.md` still lists the story rewrite and RTC audit as pending even though later records say both are complete.
- Several historical pages retain the expired 24 October decision sprint and resolved access items. The top-level index labels them historical, but individual pages do not always make supersession obvious.
- `knowledge/06-paper-story.md` says it supersedes itself; it appears intended to say it supersedes `06-paper-story-v1-2026-10-13.md`.
- The official IROS 2027 site currently lists 27 September–1 October 2027 [V, official conference site], while the repository uses 26 September–1 October in several places. The 1 March paper deadline is still secondary/tracker evidence; the official conference site has not yet published the full call.

Impact: add supersession banners or a compact current-state dashboard; correct only current navigation/constraints, preserving historical logs.

### Medium — Remote governance is only partially verifiable

The public workflow exists and its only run passed. Branch-protection, required-review, force-push, deletion, and merge-strategy settings are not publicly readable and were not verified. The repository policy documents the desired settings but documentation is not enforcement.

Impact: a repository owner should verify the settings in GitHub and record the result without exposing account-sensitive details.

### Medium — Optional tool readiness is clone-local

The setup log records Feynman/REA activation in the setup environment, but this checkout lacks the ignored local Node/runtime; `python tools/run_tool.py feynman status` exits with “Local Node is missing.” The documentation correctly says each teammate installs locally, but the current machine is not research-tool ready.

Impact: use a per-machine readiness checklist. Do not infer local authentication or runtime readiness from the tracked setup log.

### Low — The repository is intentionally infrastructure-heavy

There is no selected robotics stack, method code, dataset backend, experiment protocol, or manuscript build yet. This is consistent with the open direction and is not a defect. The next work should be evidence gating and a cheap discriminating experiment, not filling empty directories.

## Checks and observations

- `git fsck --full`: no output, exit 0.
- `git diff --check`: no whitespace errors before report creation.
- Basic tracked-secret pattern scan: no filenames matched; this is not a full secret audit.
- `python3 -m unittest discover -s tests -v`: could not start, exit 9009.
- `python3 tools/check_repo.py`: could not start, exit 9009.
- `python -m unittest discover -s tests -v`: 12 passed, 3 failed, 1 error; failures are the Windows hook/path boundary described above.
- `python tools/check_repo.py`: failed only the two shared-skill adapter checks in this checkout.
- Public GitHub Actions run for commit `111f1d3`: passed on Ubuntu.

## Recommended order

1. Decide whether the public visibility is intentional and whether Windows-native operation is supported.
2. Repair or explicitly constrain the platform workflow, then require a clean local verification run for every teammate.
3. Promote the 6–10 nearest papers into claim-level notes before selecting a question.
4. Choose one research-question proposal and run its cheapest discriminating test; do not begin a full stack build first.
5. Verify GitHub protections, artifact storage, ethics route, and team ownership before data collection.
