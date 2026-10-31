#!/usr/bin/env bash
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
cd "$root"
existing="$(git config --get core.hooksPath || true)"
if [[ -n "$existing" && "$existing" != .githooks ]]; then
    printf 'Existing hooksPath %s: reconcile it manually; nothing changed.\n' "$existing" >&2
    exit 1
fi
if [[ -z "$existing" ]]; then
    hooks_dir="$(git rev-parse --git-path hooks)"
    for hook in "$hooks_dir"/*; do
        if [[ -f "$hook" && "$hook" != *.sample ]]; then
            printf 'Existing hook %s: reconcile it manually; nothing changed.\n' "$hook" >&2
            exit 1
        fi
    done
fi
chmod +x .githooks/commit-msg .githooks/pre-commit .githooks/pre-push
git config --local core.hooksPath .githooks
git config --local merge.ff false
git config --local user.useConfigOnly true
printf 'Local hooks enabled; merge.ff=false. Identity and remote settings unchanged.\n'