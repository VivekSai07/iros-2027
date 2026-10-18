# Candidate directions

| ID | Idea | Status after 5 iterations |
|---|---|---|
| A | Precision connector/plug-in on a hobby arm, sim-trained (Newton cables/VBD, backlash randomization) | Least collided in searches; hardware-risky (STS3215 backlash, secondary-source ±2–4 mm repeatability, ~500 g payload) |
| B | Aging-aware twin / endurance (hours-scale deployment, servo overheating) | Literature only hours-scale (RECAP 13 h, RL-100 ~7 h); pairs naturally with A. NeuralActuator (2607.11734) includes SO-101 STS3215 load registers |
| C | Assistive arm with users | Heavy human-study burden; not pursued |
| H1 | "Say it mid-motion": physical state-update/repair under spoken interruption (full-duplex HRI + manipulation) | **Leading.** Crowded but a narrower wedge survives (see 05) |
| H2 | "Knows when NOT to help": consequence prediction / world model for proactive assistance | Partly covered (NIABench, PACT, Attentive Support, MICoBot); consequence-prediction angle unchecked; compute-heavy |

## A+B detail
- Risk: week-2 repeatability/backlash measurement is the go/no-go.
- Strengths: sim-to-real story with Newton VBD; distinct from VLA crowd.
- Weaknesses: IROS reviewers may see hobby-arm precision as a stretch; endurance claims need long runs.

## H1 detail
See `05-gap-analysis.md`, `06-paper-story.md`.

## H2 detail
- Prior art: PACT (2605.24350, sim humans), Event-Driven Proactive Assistive Manipulation (2603.23950), NIABench (2605.01368, IROS 2026), Attentive Support (IROS 2024), Baraglia et al., AURA, LIT (2406.13787), HOI4ABOT, GUIDER, Smart Help.
- Aligns with Karcini pillar 3 (physics-grounded world models for consequence prediction).
- Risks: 8 GB machines, large human-study burden, ground-truth "should not help" labeling is hard.

## Decision rule
Pick H1 unless the 24 Oct sprint shows (a) a new scoop of the benchmark wedge, or (b) A+B repeatability is clearly <1–2 mm and the team prefers hardware-centric work.
