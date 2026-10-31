# Data

Track dataset cards, schemas, annotation instructions, split definitions, retrieval scripts, and checksummed manifests here. Payloads stay within the workspace but outside ordinary Git history:

- `raw/`: immutable source recordings and observations.
- `processed/`: reproducible transformations of raw data.
- `private/`: restricted local material; prefer institution-approved encrypted storage for identities and consent forms.

Create these ignored directories when needed. Before shared collection, agree on a team-accessible storage backend and add credential-free retrieval instructions. A local path alone is not a shared dataset. DVC, an institutional object store, or a dataset registry can be added once storage/access requirements are known; none is configured yet.

Use a [dataset card](../docs/templates.md#dataset-card). Keep secrets, identifiable participant data, and restricted papers out of Git even in a private repository. Review licenses, consent, ethics, retention, and split leakage before collecting or publishing.