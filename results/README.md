# Results

Use `<experiment-id>/<run-id>/` for a [run record](../docs/templates.md#run-record), small metrics, reviewed tables/figures, and links to the protocol and analysis command. Keep bulky traces, model checkpoints, and video in ignored `artifacts/<run-id>/` at the repository root, with hashes and shared-storage references in the run record.

Never overwrite a completed run. Preserve failed runs, negative findings, and exclusions. A reported figure must trace to the exact run IDs, data, code commit, environment lock, and analysis command. Do not commit fabricated example results.