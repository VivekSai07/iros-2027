# Shared Resource Reservations

No resources are reserved by repository setup. Hardware availability is a historical assumption to confirm, not an active allocation.

Before GPU or hardware work, add a row and confirm with the team. Git branches do not provide a distributed lock: agree on a reservation in the shared team channel and reconcile it here before running. Do not assume an unmerged reservation is visible to others.

| Resource | UTC start/end | Owner | Task/branch | Budget | Supervisor/safe-stop plan | State |
| --- | --- | --- | --- | --- | --- | --- |

Use reserved/running/released/cancelled states. Jobs stop at the agreed time/budget or on safety and rate-limit failures. Participant work needs separate ethics and consent approval.