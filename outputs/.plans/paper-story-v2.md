# Plan: paper-story-v2 (rewrite of 06-paper-story.md per outputs/paper-story-review.md)

Slug: `paper-story-v2` · Date: 2026-10-18 · Deliverable: `outputs/paper-story-v2.md` (user-specified path; overrides template default `papers/<slug>.md` because user restricted edits to `outputs/`).

## Conflicts with the generic template (resolved in favour of explicit user instructions)
- No subagents (writer/verifier) — user forbade spawning. Verification done by hand: grep of source files for every number.
- No web search — evidence restricted to the 9 listed local files.
- No abstract / full related-work section — user: "story document". A compact positioning table replaces related work.
- No plots → no plotting script.
- Hard cap < 2000 words.

## Proposed title
"Say It Mid-Motion: Benchmarking and Repairing Spoken Corrections During Manipulation on a Low-Cost Arm"

## Sections (same skeleton as 06 + required additions)
1. Working title
2. Novelty claim (one paragraph, conjunction of 5 properties) — G1 §4, 05 update
3. Narrative (revised strategy taxonomy: halt / retract / redirect-text-only / anticipate) — CMP §2, G2 §2
4. Positioning table: SocialVLA, Causeway, LIBERO-MAX, SwitchVLA, ReSteer, ARMS, Yu&Qiu, Song, MIRA, RIAP, Premover
5. Contributions C1 (conjunction benchmark, borrowed protocol), C2 (wedge + prefix-bias + task-island + LeRobot gaps), C3 (hypothesis)
6. Research questions
7. Experiments: baselines B1–B6 (+B7/B8 optional), ACT scoping, state-based onsets, controls (bare text switch, state placement), metric definitions (latency onsets, continuity, retraction, residual motion, false-barge-in denominator), cancel/safety hold path, human study design
8. Why it can stand out (no best-paper language)
9. Risks and fallbacks (scoop HIGH)
10. Sources

## Key claims → source
| Claim | Source | Flag |
|---|---|---|
| No work has all 5 properties | G1 §2/§4 | [V] matrix, absence = inference |
| SocialVLA gate→hold 336 ms, onset→hold 1.021 s, FP 100→57, no repair metric | socialvla-summary | [V] |
| MIRA 466 ms speech→abort cmd | G1, CMP | [V] |
| Causeway 3 timings, bare 3–26% → 47–65% sim, 71 pairs; ‖Δa‖ drop 1–2 orders | causeway-summary | [V] |
| Paired with/without protocol is LIBERO-MAX not Causeway | causeway-summary | [V] absence in Causeway; attribution inference |
| SwitchVLA, ReSteer text switching without retract | G2 §1 | [V] |
| ARMS text metrics | G1 | [V] |
| Yu&Qiu SO-101 taxonomy | G1 | [V abstract] |
| Song n=24 Dobot | G4 | [V] |
| RIAP 27.5%→1.6%, N=30, abstract only | G1, CMP | [V-abstract] |
| Premover real SO-101, no corrections after motion | CMP | [V] |
| πR² prefix bias | G2 §3a | [V] |
| LeRobot: identity Jacobian M1, β=10, LINEAR, exec_horizon 10, set_task hold on SO-101, no per-request profile, no immediate re-request in RTC | RTC audit | [V code] |
| ACT no language, no RTC | RTC audit §5 | [V] |
| Hoffman |r|≤0.123 | G4 | [V] |
| Beyond-condition power 0.97→0.37 (N=24,k=8,r=0.2) | G4 §1/§8 | computed in G4 (reproduced there) |
| r=0.3 between-participant needs n=85 | G4 | computed |
| SmolVLA ~99 ms RTX 4090 | G2/review | [V via G2] — not used numerically beyond citing |
| EchoChain voice cloning from voice actors | G4 §6 | [V] |
| Effort 3–5 dev-days + 2–4 | RTC audit | [U] |

## Verification log (fill during sweep)
- [x] grep 336 / 1.021 / 466 / 0.123 / 27.5 / 0.37 / 85 in sources — done, see below
- [x] word count < 2000 (wc -w)
- [x] every unmeasured number marked TODO
- [x] no "best paper", no "first" claims beyond conjunction
- [x] no file outside outputs/ edited

## Verification results (2026-10-18)
- wc -w outputs/paper-story-v2.md: 1984 (< 2000) ✓
- Numbers grep-traced to sources: 336 ms, 1.021 s (socialvla-summary, G1); 466 ms (G1, G2, CMP); |r|≤0.123 (G4); 27.5→1.6% (G1, CMP); 0.97→0.37, n=85 (G4); 71 pairs, 8 states×3 rollouts (causeway-summary); ~99 ms (G2); PR #4108 / "Buffered motion" (RTC audit, G2); 1–2 orders (causeway, G2); 16 Aug 2027 (10 §3, flagged [S]).
- Dropped the review's "n≈543" figure: not present in G4 itself (only in review/10), so it is untraceable to a primary calculation; used G4's n=85 instead.
- Corrected inherited error: paired with/without protocol is NOT in Causeway (causeway-summary); attribution to LIBERO-MAX marked inference.
- No "best paper", no single-ingredient "first" claims; scoop risk HIGH; 10 TODO markers for unmeasured quantities.
- No subagents, no web search (user instruction). Only outputs/ files written.
