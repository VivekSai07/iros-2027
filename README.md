# IROS 2027 Research Workspace

Shared workspace for a three-person robotics research team. **The research question and methodology are not yet selected.** Earlier literature is evidence to assess, not a commitment to its leading candidate.

## Start Here

1. [Current research state](knowledge/index.md)
2. [Setup and collaboration](docs/setup.md)
3. [Research workflows](docs/workflows.md)
4. [Agent policy](AGENTS.md)

## Where Work Lives

| Directory | Contents |
| --- | --- |
| [knowledge](knowledge/index.md) | Literature, source provenance, linked notes, gap analysis, append-only decisions |
| [src](src/README.md) | Reusable method, framework, and evaluation code |
| [configs](configs/README.md) | Versioned experiment configurations |
| [experiments](experiments/README.md) | Experiment protocols and entry points, including the existing power simulation |
| [data](data/README.md) | Dataset cards/manifests; local raw, processed, and restricted data |
| [results](results/README.md) | Run records, small metrics, reviewed figures and tables |
| [paper](paper/README.md) | Manuscript, references, supplementary material |
| [docs](docs/workflows.md) | Setup, workflows, plans, and methodology documentation |
| [logs](logs/README.md) | Per-task progress, handovers, and resource reservations |
| [tools](tools/README.md) | Pinned external integrations and repository checks |
| [tests](tests/test_commit_message.py) | Lightweight tests, independent of hardware and credentials |

All work has a home here. Large datasets, recordings, model weights, downloaded tools, caches, and credentials do not belong in ordinary Git history. Track manifests and reproducible retrieval instructions; choose and configure team artifact storage explicitly before collection.

## Daily Loop

Start a topic branch from `main`, record the question and acceptance check, do the work, validate, and make local commits. Ask for approval before merging with `--no-ff`. Only a human pushes.

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_repo.py
```

The external integrations are opt-in and do not run during these checks. See [tools](tools/README.md) for setup, prerequisites, and verification status.