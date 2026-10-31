# Setup And Collaboration

## Lightweight Setup

Use Linux or WSL, Git, Bash, and Python 3.11+. No GPU, API key, Obsidian installation, or external research tool is needed to read notes or run repository checks.

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_repo.py
bash tools/setup_git.sh
```

The Git setup is local to this clone and must be run by each collaborator. It refuses to replace existing hooks, sets `merge.ff=false`, and requires a configured Git identity without changing it. Configure your own name/email through your normal Git setup if missing. Hooks are not enabled merely by cloning; CI also checks new commit messages.

The commit-message hook rejects AI branding/attribution, the pre-commit hook blocks direct main/master and detached-HEAD development, and pre-push requires a deliberate human override. Human co-authorship is permitted. These are accident-prevention measures, not tamper-proof controls or a substitute for approval.

## Branches And Concurrent Work

Start from reviewed local main. Humans fetch/pull the desired upstream state first when needed; do not assume the remote-tracking ref is current.

```bash
git switch main
git switch -c research/your-name/topic main
```

For simultaneous tasks, use separate worktrees. The ignored worktree directory keeps all local work under the same workspace while Git shares the history:

```bash
git worktree add .worktrees/topic -b feat/your-name/topic main
```

Each worktree has its own files and local tool installation; do not share writable caches or vault journals across writers. Use one coordinator per task and unique per-paper/per-task records. Agree on GPU/robot bookings with the team, not only in unmerged files.

Agents may commit locally after informing you and checking the change. They may not push. To review a branch:

```bash
git diff --stat main...your-topic-branch
git log --oneline main..your-topic-branch
```

## Merge And Publish

Only after the user approves the named branch and checks:

```bash
git switch main
git merge --no-ff your-topic-branch
python3 -m unittest discover -s tests -v
python3 tools/check_repo.py
```

The merge commit retains both parents even when a fast-forward was possible. Never use squash/rebase/fast-forward merges into main. Merge approval does not authorize a push.

**The human alone runs the publishing command**, after reviewing local history and the remote destination:

```bash
RESEARCH_HUMAN_PUSH=1 git push origin main
```

To publish a topic branch for review, the human uses the same prefix and the chosen branch name. Agents must never set this variable or run either push. A noninteractive editor push without the override will be rejected by design. Never put the override in a persistent environment or client configuration.

Repository owners should configure hosting protections: require reviewed PRs and passing `repository-checks`, disable force pushes and deletion of main, permit merge commits, disable squash/rebase merge, and **do not require linear history**, which conflicts with merge commits. Permissions, review counts, and bypass rules must be set by the owner; this setup does not change remote settings.

## Clients And Integrations

- Codex reads the root [AGENTS.md](../AGENTS.md).
- Claude imports the same policy through [CLAUDE.md](../CLAUDE.md); project attribution settings suppress default trailers.
- Copilot follows [its entry point](../.github/copilot-instructions.md), which links the same policy.
- The portable `research-workflow` skill is shared across all three; see [tools](../tools/README.md) for discovery and optional MCP/plugin setup.

Enable only the tools needed for a task. Local readiness checks and CLI help do not prove that a client has loaded a plugin or authenticated. Keep credentials in the client's secure credential store; never paste them into configuration committed here.

## Storage And Safety

See [data](../data/README.md) and [results](../results/README.md). Large payloads stay local until a shared backend is approved and documented. Git does not synchronize ignored files. Do not begin team collection with only one person's local dataset path.

Participant studies and physical robot operation need separate approvals. No tool installation grants permission to execute arbitrary upstream code, bypass source access restrictions, collect private data, or publish artifacts.