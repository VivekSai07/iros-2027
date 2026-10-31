# Record Templates

Copy the relevant section into a uniquely named task, paper, protocol, or result file. Replace fields before a run; retain explicit unknowns instead of inventing evidence. These are templates, not completed research records.

## Task Record

```markdown
# <date>-<owner>-<topic>
Status: planned | active | blocked | complete
Owner:
Branch and base commit:
Question and scope:
Acceptance check:
Budget and resource reservation:
Inputs and output paths:
Work completed:
Checks run and actual outcomes:
Decisions/evidence changed:
Blockers and access requests:
Next step and exact command:
Reviewer:
```

## Paper Note

```markdown
---
id: <doi-or-arxiv-id-version>
type: source
status: unreviewed
---
# <title>
Authors, venue/status, year:
Primary URL, paper version, accessed date:
Code URL/commit, license, data/checkpoints:
Reading depth: abstract | full text | code inspected | reproduced
Problem and claimed contribution:
Core mechanism/equations:
Training and evaluation conditions:
Claim | [V]/[S]/[U] | page/table/file | evidence scope
Author-stated limitations:
Our inferred limitations and counterevidence:
Relationship to candidate RQs and nearest competitors:
Unknowns / blocked sources:
Reviewer and review date:
```

## Paper/Code Audit

```markdown
# <paper-id> implementation audit
Question:
Paper version and code commit:
Source/checkpoint licenses and execution permission:
Environment/lock and hardware requirements:
Paper component | code file/symbol | config | agreement/deviation | evidence
Inputs -> preprocessing -> core method -> output -> evaluation:
Minimal reproduction command and expected result:
Observed result, run ID, error bounds, and deviations:
Not executed / unsupported conclusions:
Potential research question, alternative explanation, discriminating test:
Graph/artifact provenance and reviewer:
```

## Question Proposal

```markdown
# <rq-id>: <question>
State: proposed | adopted | rejected | superseded
Problem and affected users/tasks:
Closest prior work with primary evidence:
Limitations: author-stated vs our inference:
Falsifiable question and hypothesis:
Novelty comparison and strongest counterexample:
Baseline, control, primary metric, meaningful effect:
Cheapest discriminating experiment:
Compute/hardware/data/ethics needs and budget:
Failure/pivot criteria:
Team decision, date, and decision-log ID:
```

## Experiment Protocol

```markdown
# <experiment-id>
State: pilot | exploratory | confirmatory
RQ/hypothesis and linked decision:
Independent variable, baseline, controls, ablations:
Primary metric and practical effect threshold:
Secondary metrics and multiple-comparison handling:
Experimental unit, sample-size rationale, uncertainty method:
Data version, immutable split, leakage checks:
Seeds, order/randomization, exclusion and stopping rules:
Code/config/environment lock:
Expected outputs and analysis command:
Budget, resource reservation, safety/ethics approval:
Go/no-go and failure/pivot criteria:
Protocol revisions with dates and reasons:
```

## Dataset Card

```markdown
# <dataset-id>@<version>
Owner, license/consent, intended use and restrictions:
Source and collection protocol:
Schema, units, clocks, sensors and calibration:
Sampling/annotation/quality checks:
Split definitions and leakage unit:
Raw payload hashes and transformations:
Storage URI, retrieval command, access contact (no credentials):
Participant privacy, retention, withdrawal process:
Known biases, missingness and limitations:
```

## Run Record

Store as `results/<experiment-id>/<run-id>/run.json`, with small metrics/figures alongside. Replace the example values; no fake measurements.

```json
{
  "run_id": "YYYY-MM-DD-owner-unique-id",
  "experiment_id": "linked-protocol-id",
  "status": "planned",
  "code_commit": null,
  "dirty": null,
  "patch_reference": null,
  "command": null,
  "config_path": null,
  "config_sha256": null,
  "environment_lock": null,
  "data_version": null,
  "split_sha256": null,
  "seeds": [],
  "hardware": null,
  "started_at": null,
  "finished_at": null,
  "exit_code": null,
  "artifacts": [],
  "analysis_command": null,
  "failures_and_exclusions": [],
  "reviewer": null
}
```

Each artifact entry records a local path or credential-free URI plus checksum. Change status to running/completed/failed/aborted honestly; completed records must have the fields needed to reproduce the run. Never use a planned template as evidence for a paper claim.