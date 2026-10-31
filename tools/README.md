# Research Tool Integrations

Tools are dependencies, not our research contribution. [Source pins](upstreams.json) and the [CLI package manifest](package.json) / [lockfile](package-lock.json) are tracked. Downloaded source and runtimes are not. No global installation, API authentication, paid search, graph-generation job, native analysis, or automatic publishing is performed by repository checks.

## Status And Roles

Checked 2026-10-31. [V] below means upstream documentation/metadata was inspected, not that every advertised capability was executed.

| Integration | Pinned version | Role | Local verification |
| --- | --- | --- | --- |
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 3.0.1, exact Git SHA in registry | Shared Markdown vault, source/claim ledgers, controlled writes | Source installed; additive vault adoption, doctor, and contract checks passed |
| [Feynman](https://github.com/Companion-Inc/feynman) | 0.5.61 | Literature searches, paper summaries, paper/code audits, provenance | Activated 2026-10-31 under the accepted exception below; `--version` and `status` ran, Pi runtime ready, telemetry off. No model provider authenticated yet; no research job run |
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 2.9.0, exact Git SHA | Source-code/knowledge graphs and targeted implementation explanation | Source installed and skill paths inspected; build and paid graph pipeline not run |
| [REA](https://github.com/morluto/rea) | 6.8.0 | Paper implementation, artifact, binary, and runtime investigation when source inspection is insufficient | Activated 2026-10-31; MCP `initialize` + `tools/list` handshake returned server 6.8.0 with 229 tools. No native provider (Ghidra/Hopper/IDA/Kuna) installed; no target analyzed |

All four list MIT licenses [V upstream]. Individual dependencies, analysis targets, commercial providers, and datasets retain their own terms. See [third-party notices](../THIRD_PARTY_NOTICES.md). The awesome-reverse-engineering catalog was removed on 2026-10-31 (D-020); REA covers the team's reverse-engineering needs.

## Setup And Readiness

```bash
python3 tools/bootstrap.py sources
python3 tools/bootstrap.py check
```

`sources` downloads two shallow, detached checkouts into `.tools/`, verifies exact commits, and refuses to overwrite existing modified or mismatched source trees. `check` performs no downloads or writes and returns nonzero for missing components. Interrupted installations are left for inspection, not deleted automatically.

### CLI Dependency Gate

`npm --prefix tools audit --json` on 2026-10-31 reported **10 affected package entries: 7 moderate and 3 high**. This count includes dependent packages, not ten independent exploitable defects. Findings include undici network/TLS/cache issues through Feynman's Pi dependency, zod collection-validation memory exhaustion through REA, and glob/minimatch denial-of-service risks. We have not established exploitability for our workflows. No safe upstream-supported fix was established in this setup; npm suggests a major Feynman downgrade for some findings and no fix for others.

**Exception accepted 2026-10-31 (D-020)** by the maintainer for these pinned versions. Bounds: public papers, public repositories, and team-owned non-sensitive artifacts only; no participant data, credentials, unpublished third-party material, or untrusted network services. Recheck advisories whenever pins change and do not run `npm audit fix --force` or silently downgrade. Each teammate installs locally after reading this section:

```bash
python3 tools/bootstrap.py runtime --accept-upstream-risk
```

This installs pinned Node **24.22.1** under `.tools/node/`, then runs `npm ci --engine-strict` in `tools/` using that local runtime. It does not change the user's default Node. It requires npm/network access and runs upstream package install scripts (Node binary download, Frida native binding). The `runtime` command still refuses without the flag so a new pin cannot be activated silently; agents supply it only for pins covered by a recorded exception. Authentication, external model calls, and native backend setup are separate steps.

Advisory references: [undici TLS options](https://github.com/advisories/GHSA-2m5v-pch6-74hx), [undici redirects](https://github.com/advisories/GHSA-4w7w-5xrc-9h26), [zod collections](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5), [minimatch](https://github.com/advisories/GHSA-g3hv-75wg-m249), [glob](https://github.com/advisories/GHSA-3g3m-2fjr-6pw4).

## Knowledge Base

The product is `.tools/claude-obsidian/`; the vault is `knowledge/`. Never confuse them or run an upstream scaffold over our repository root. Open `knowledge/` in Obsidian. All clients can read the same Markdown and use the portable core through the shared runner:

```bash
python3 tools/run_tool.py obsidian doctor --vault knowledge
python3 tools/run_tool.py obsidian contracts --verify --vault knowledge
```

The initial vault is adopted already. Source and claim ledgers start empty: migrated legacy reports have **not** been ingested or freshly verified. The current-state index links the historical research; the managed wiki index catalogs subsequently reviewed knowledge. Capture legally shareable inputs in `knowledge/inbox/`; private `.raw` payloads, journals, recovery state, and editor sessions are ignored. Shareable manifests and ledgers remain tracked.

For ingestion or query, ask any client to read the relevant pinned skill under `.tools/claude-obsidian/skills/` and use the portable CLI above. Claude can alternatively start from the repository root with `claude --plugin-dir .tools/claude-obsidian`. Use preview/approved-hash transactions, one coordinator writer, and no automatic Git checkpoints. Built-in PDF semantic extraction is not provided by the vault core [V upstream]; use an approved separate reader and retain source provenance.

## Literature Engine

Authenticate once per machine (interactive; enter secrets only in the CLI's own prompts, never in chat or tracked files), then confirm:

```bash
python3 tools/run_tool.py feynman setup
python3 tools/run_tool.py feynman status
```

Setup, `doctor`, `status`, `model`, `alpha login/logout/status`, `mcp`, `search`, `packages`, and `update` run from the repository root without a job. Feynman stores credentials and sessions in `~/.feynman/`, outside the repository. Every other invocation is research and needs a unique job:

```bash
python3 tools/run_tool.py feynman 2026-10-31-your-name-gap-check lit "bounded research question"
```

The wrapper creates `knowledge/jobs/<job-id>/`, runs Feynman there, sets `FEYNMAN_TELEMETRY=off`, and records command/version/code/exit metadata in `job.json`. Feynman writes reports and provenance to that job's `outputs/` (drafts to `papers/`). The wrapper refuses reused IDs; resume an interrupted job deliberately through Feynman's own session flow rather than overwriting it.

Start with one job at a time and an explicit cost/time budget. The wrapper records status but does **not** enforce a spend cap or guarantee provenance coverage; confirm both before promoting a report. Read the root policy in each engine session. `feynman mcp add` configures tools used by Feynman; it does not make Feynman an MCP server for our other clients. Claude/Codex/Copilot use its CLI and shared artifacts.

## Paper Implementations And Graphs

Pin each target implementation separately under `.tools/papers/<paper-id>/`, recording its license and commit in a paper/code audit. Read the pinned Understand-Anything skill under `.tools/understand-anything/understand-anything-plugin/skills/`. For Claude, a local plugin launch is:

```bash
UNDERSTAND_NO_WORKTREE_REDIRECT=1 claude --plugin-dir .tools/understand-anything/understand-anything-plugin
```

For Codex and Copilot, the shared research skill routes to the same pinned source skill. When following it, explicitly resolve `PLUGIN_ROOT` to `.tools/understand-anything/understand-anything-plugin` in this checkout; do not select a different global installation. Its first build needs Node >=22 and pnpm >=10 [V pinned skill]; inspect its locked setup before running it. Never fall back from a frozen lockfile to an unpinned install silently.

**Always set `UNDERSTAND_NO_WORKTREE_REDIRECT=1` and explicitly choose the target checkout.** The pinned skill otherwise redirects worktree graph writes to the primary checkout [V code], violating our isolation rule. Disable `--auto-update` and post-commit graph hooks. Do not analyze the whole research monorepo or private data to answer a narrow paper question.

Graphs live in the target's `.ua/` (or existing `.understand-anything/`). Promote a reviewed graph/snapshot into a paper-specific knowledge folder with its source commit, generation command, limitations, and a pointer to the audit. Omit intermediate scratch and diff overlays. No graph has been generated by this setup.

## REA And Client MCP Setup

`python3 tools/run_tool.py rea --help` uses the pinned package; `python3 tools/run_tool.py rea mcp` is its stdio MCP server [V pinned server manifest; handshake verified]. The pinned REA workflow skill is `tools/node_modules/rea-agents/skills/reverse-engineer-anything/SKILL.md`; read it before an investigation. Static JavaScript, Python-package, model-artifact, and other built-in inspections need no native engine. Native binaries need Ghidra, Hopper, IDA, or Kuna installed separately; none is installed. Use only software you are authorized to inspect. Prefer direct source reading for ordinary Python research code.

Registered servers (tracked, project scope; start clients from the repository root):

- **Claude:** [.mcp.json](../.mcp.json). `claude mcp list` discovers `rea` as pending approval; approve it once in an interactive `claude` session.
- **VS Code Copilot:** [.vscode/mcp.json](../.vscode/mcp.json). Start/trust the `rea` server from the MCP view when prompted.
- **Codex:** Codex 0.160.1 did not load a project `.codex/config.toml` here, even with a temporary trust override, so each teammate registers it in their own user config with their checkout's absolute path:

  ```bash
  codex mcp add rea -- python3 "$PWD/tools/run_tool.py" rea mcp
  ```

The server starts only after `runtime` installation; otherwise the wrapper exits with a setup message. Never commit API keys or native-tool license credentials.

## Updating Or Removing Tools

Use a tooling branch: inspect upstream changes/licenses/advisories, update exact pins and the lockfile, validate with minimal non-sensitive examples, then seek merge approval. Do not auto-update. Keep source checkouts with modifications for review rather than resetting them. Removing a local tool must not remove the vault, job outputs, provenance, or paper audits.