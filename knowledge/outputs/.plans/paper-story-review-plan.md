# Review plan — paper-story (slug: `paper-story`)

- **Artifact:** `06-paper-story.md` (local Markdown, ~340 words; a working draft of the paper narrative for IROS 2027, not a manuscript).
- **Evidence base (user-specified):** `05-gap-analysis.md`, `10-research-map-and-implementation.md`, `outputs/g1-interruption-benchmark-novelty.md`, `outputs/g2-midmotion-repair-novelty.md`. G4 (`outputs/g4-fluency-metrics-validity.md`) and `02-iros-2027-constraints.md` were grep-checked only because 10-research-map relies on them.
- **Constraints:** no new web searches except to check a specific claim I challenge; no subagents; review under 1500 words; [V]/[S]/[U] flags; write only under `outputs/`.

## Review criteria
novelty · empirical rigor · baselines · reproducibility · claims validity · figures/tables · metrics · related work · writing quality

## Verification checks
1. Prior-work claims in Narrative §2 vs the G1/G2 coverage matrices (SocialVLA, MIRA, Causeway, SwitchVLA, ReSteer).
2. C1 wording vs the G1 verdict (conjunction framing, the "do NOT claim" list).
3. C2 wording vs the G2 verdict (broad claim closed, narrow wedge, ACT has no language input, LeRobot `set_task`).
4. C3 vs the G4 findings (Hoffman |r| ≤ 0.123, power, Song 2607.00530).
5. Baselines vs the G2 §6 list.
6. Scoop-risk level vs 05/G1.
7. Reported metrics/results: the story contains none. Check that no result is asserted as fact.
8. Data/code: nothing built yet (10 §4). Record as not-run.
9. One targeted primary check: the SocialVLA and Causeway abstracts through the arXiv API, to test the narrative's claim that no existing work measures physical outcomes.
