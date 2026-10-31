# Repository Setup: 2026-10-31

Owner: requesting maintainer. Branch: `chore/research-workspace`, from main at `5135470`. Scope: repository organization, shared agent policy, pinned integrations, and research workflows. No RQ, method, dataset backend, paid research job, or hardware operation was selected or run.

## Work Completed

- Moved existing numbered research documents and inputs/notes/outputs/refs together under `knowledge/`. Byte comparisons against main passed before appending D-019, pass 9, and the navigation update. The existing experiment is unchanged.
- Added root navigation, canonical policy and thin client entry points, a shared portable skill, research workflows/templates, data/results/manuscript responsibilities, task logs, and resource coordination.
- Added opt-in local Git safeguards, plain-message validation, source/CLI pins, a dependency lock, isolated literature job records, offline repository checks, and read-only CI.
- Adopted the vault through the pinned upstream's reviewed additive transaction. Doctor and contracts returned `ok: true`. No legacy report was ingested or freshly verified.
- Pinned source checkouts for claude-obsidian, Understand-Anything, and the reference catalog are present locally. Feynman/REA dependencies are locked but not installed or enabled due the documented advisories; no risk exception was granted.

## Review And Verification

- A read-only review found no blocking issue. Its record-write observation was addressed with atomic replacement and focused failure-preservation tests. Partial downloads are deliberately preserved for manual inspection, not automatically deleted.
- Scope-specific tests cover Git hooks, plain-message rules, isolated job IDs, dates, non-overwrite behavior, and atomic record preservation.
- Repository checks validate new local Markdown targets, JSON, immutable source pins, CLI lock consistency, and canonical skill links. They do not inspect legacy links, remote URLs, anchors, credentials, or live client loading.
- The old experiment was not rerun, optional CLI/MCP/native-provider workflows were not executed, and no graph pipeline was run. Source installation is not equivalent to those checks.
- Implementation checkpoint: `a0d1d65` (`chore: organize shared research workspace`), authored and committed using the existing `VivekSai07` identity, with no attribution trailer.
- Final implementation suite: 14 tests passed; repository checks and Git whitespace checks passed. Vault contract verification returned `ok: true` after navigation updates.
- A separate clean local clone of the implementation checkpoint passed all 14 tests, repository/commit-message/whitespace checks, and the vault doctor using the pinned source tool. The clone had no ignored downloads or caches; source tools remain an opt-in installation for teammates.
- Local hooks are enabled in the working clone. Main remains at `5135470`. No merge, push, risk exception, paid research, or global runtime change occurred.

## Remaining Decisions

Choose and record the research question as a team using the workflow gate. Review upstream advisories before any Feynman/REA activation. Agree on shared artifact storage before collection; local ignored data is not automatically shared. Verify venue requirements, ethics, hardware access, task ownership, and distribution licenses when their workflows begin.

## Next Commands

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_repo.py
python3 tools/bootstrap.py check
```

The last command intentionally returns nonzero while optional CLI runtimes are gated. Open `knowledge/` as the Obsidian vault; use `knowledge/index.md` for current research state. Merge and push remain unapproved and must not be performed by the setup task.

## Addendum: Tool Activation And Merge

The maintainer asked to set up Feynman and REA, remove the reverse-engineering catalog, and merge locally (D-020). Superseding the gated status above:

- `bootstrap.py runtime --accept-upstream-risk` installed local Node 24.22.1 and the locked packages; npm audit still reports 7 moderate / 3 high affected entries. `bootstrap.py check` reports all components ready.
- Feynman 0.5.61: `--version` and `status` ran through the wrapper; Pi runtime ready, telemetry off, no model authenticated (maintainer runs `feynman setup`). The wrapper now runs admin commands without a job; research commands still require one (tests added).
- REA 6.8.0: stdio MCP handshake returned 229 tools. Claude discovers the tracked `.mcp.json` server as pending approval. VS Code config tracked; its discovery not exercised here. Codex ignored a project `.codex/config.toml` even with temporary trust, so that file was dropped and a per-user `codex mcp add` command documented. No native provider installed; no target analyzed.
- Catalog pin, local checkout, and references removed.
- Merge into main approved by the maintainer; performed locally with `--no-ff`. Push is left to the maintainer.