# Review: g4-fluency-metrics-validity-draft.md (2026-10-18)

**Reviewer role:** adversarial evidence and logic audit. The draft was **not** edited.

**Inputs read:**
- `outputs/.drafts/g4-fluency-metrics-validity-draft.md`, the draft under review.
- `outputs/.drafts/g4-fluency-metrics-validity-verification.md`, the verifier report.
- `experiments/g4-fluency-metrics-validity/power.py` and `power_results.txt`.
- Project context: `05-gap-analysis.md`, `06-paper-story.md`, `02-iros-2027-constraints.md`, `04-literature-map.md` (rows for SocialVLA, MICoBot, ExpressMM, RIAP, Premover, VITA-E, ELLSA) and `08-open-questions-and-access-needs.md`.

**Independent checks run in this review:**
1. **Power script.** I re-ran `power.py`. Its output is byte-identical to `power_results.txt` once CRLF line endings are normalised. Every power number in the §8 table matches the script output after rounding.
2. **Extra power analysis.** I ran an analytic and simulation check of trial-level power:
   - at Hoffman's effect size r = 0.12;
   - at the design's actual episode count (k = 32);
   - for the claim the draft actually makes ("beyond condition labels").

   The code and results are in Appendix A.
3. **Scoop check on adjacent interruption studies.** Using full text via alphaXiv, I checked whether SocialVLA (2610.02360), MICoBot (2508.05535) and ExpressMM (2604.05320) relate objective metrics to subjective ratings. None of them does (Appendix B).
4. **Gap search.** One alphaXiv search ("objective fluency metrics ↔ subjective ratings, HRC") found two live, co-located HRC studies the draft misses: Kille et al. 2025 (2505.04182) and RAPIDDS 2026 (2604.19670). I read both in full text.

---

# Part 1: Structured Review

## Summary

The draft asks whether benchmark-style objective metrics predict human-perceived fluency in speech-driven HRC on low-cost arms. It reviews five bodies of evidence:
- Hoffman's (2019) objective fluency metrics and their single online validity study, plus the Weiss et al. (2023) follow-up;
- live speech-HRI evidence that objective timing and perceived timing come apart (Skantze & Irfan 2025);
- a new July 2026 scoop-risk paper (Song et al. 2607.00530) that frames "technical metrics → user perception" on a Dobot arm with speech;
- the limits of LLM/TTS simulated users (Zhou et al. 2026, EchoChain, Synthetic TLX);
- questionnaires, sample sizes in the field, Wizard-of-Oz (WoZ) protocols, and European ethics/GDPR timelines.

It ends with a refined G4 claim (trial-level physical-repair metrics predict per-episode ratings beyond condition labels) and a concrete N≈24 within-subject design, supported by a seeded power script.

The literature synthesis (§§2–4) is accurate where it was checked, and the verifier's interpretation fixes (I1–I4, H1) are in place. The weak part is §8, the design and power section that the project will act on:
- **Power does not match the claim.** The simulation powers an unconditional repeated-measures correlation, but the claim is incremental over condition labels.
- **Inconsistent trial counts.** The table uses 8 trials per participant; the design specifies ≥32 episodes per participant.
- **Wrong comparison.** Hoffman's r≈0.12 is a rating-level effect but is used as a between-participant benchmark.
- **Unsupported feasibility and validity.** The ethics timeline arithmetic, the session-length budget, the construct validity of Hoffman metrics for a speech-supervised single-arm task, the criterion validity of ad-hoc micro-ratings, and the simulated-vs-real ranking check are each asserted rather than supported.

Status-flag hygiene is mostly good, with about six specific misuses. No sentence re-asserts a forbidden novelty claim, but the "Not to claim" list is incomplete, and one risk statement can be read as treating "interruption" as a differentiator.

## Strengths

- **[S1] The numbers can be traced to sources.**
  - The verifier confirmed spot-checks (a)–(f) against primary text: Hoffman r(495) values and α; Skantze & Irfan 1.5 vs 2.7 s and Q3 p=1.0; Song 17/24 and d_z; Zhou 63.6/77.8%; EchoChain 97/92/51; LMU/ETH timelines.
  - The draft incorporates all four interpretation fixes. I1 is §6 "That is **not** evidence that simulators preserve the ranking of the systems…". I2 is "(→ 27/39 proposed, derived by us)". I3 is "do not always yield". I4 is the UCF STARS citation.
  - It also incorporates H1 (Bartlett is now in Sources).
- **[S2] The power analysis can be reproduced.**
  - `power.py` is seeded and declares its sanity checks (C1–C3) before running, and the output reproduces exactly.
  - The paired-t and correlation numbers agree with standard references: d_z=0.5 → 34; r=0.3 → 85 against ≈84 exact.
  - The draft states its main simplifying assumptions ("independent trials, random intercepts only, and no random slopes") and calls the values upper bounds.
- **[S3] Honest re-scoping after a scoop.**
  - §1.4 openly withdraws the "first study checking benchmark metrics against user perception on a low-cost arm with speech" claim because of Song et al.
  - It names the specific gap that remains: Song's objective numbers come from a prior ablation, with no trial-level metric↔rating link and no interruptions.
- **[S4] Simulated-user evidence is read correctly.**
  - The draft separates EchoChain's *voice-realism* validation from *behavioural* validity.
  - After the I1 fix, it frames simulated↔human ranking agreement as a hypothesis to test, not a finding ("Never report simulated ratings as user perception").
- **[S5] The GDPR treatment is careful.** It quotes EDPB paras 31/128 accurately: voice is biometric personal data, and it becomes Art. 9 data only when processed for unique identification. It draws the right practical conclusion: use consenting voice actors for cloning.
- **[S6] My scoop check supports the core gap claim.** I added this check myself; it is not in the draft:
  - **SocialVLA:** no subjective ratings at all.
  - **MICoBot:** between-condition Likert only, with no metric↔rating analysis.
  - **ExpressMM:** a single-condition classroom audience, with no metric↔rating analysis.

  So the narrowed G4 gap survives these three. CMU HRI 2026 and RIAP remain unchecked (paywalled / no preprint).

## Weaknesses

### FATAL

- **[W1] FATAL (for the §8 design recommendation): the power evidence does not test the claim being targeted, and three inconsistencies make the "N=24 is enough" conclusion unsafe.** Locations: §1.6, §8 "Claim to target", §8 "Analysis", §8 "Power" table, `power.py::sim_rmcorr_power`.
  - **(a) Wrong estimand.** The refined claim is that metrics predict ratings "*beyond what condition labels explain*", via `rating ~ metric + condition + (1|participant)` and "marginal R² gain … over condition dummies".
    - The simulation draws the metric `x` independently of any condition and tests an *unconditional* participant-centred correlation.
    - In the real study, most metric variance is *created by* the condition manipulation (stop-and-replan vs mid-motion repair differ systematically in residual motion, latency and retraction). Condition dummies absorb that variance; only within-condition variance can show an incremental effect.
    - My simulation (Appendix A) used N=24, 4 conditions × 8 episodes and within-r=0.2. When 50% / 80% / 90% of metric variance is between conditions, power for the beyond-condition effect is 0.96 / 0.68 / 0.38, while unconditional power stays at 1.00.
    - The draft's own Risk 1 mitigation, "strong manipulation spread", increases exactly the variance that the claim then partials out.
  - **(b) Wrong trial count.** The table uses "8 trials". The design specifies "≥8 interruption episodes per condition" × 4 conditions, which is ≥32 per participant. The draft never says which k the table corresponds to.
  - **(c) Wrong benchmark effect size.** §1.6 says "Hoffman-size effects (r≈0.12) would need n≈543" in a *between-participant* design. But Hoffman's r(495) is computed over ~497 clip-level ratings: 104 participants × ~5 clips, pooled. That is a *rating-level* (trial-level) effect, not a between-participant one.
    - The trial-level simulations then assume within-r = 0.2–0.3, about 1.7–2.5× the only direct prior estimate. No source is given for 0.2–0.3.
    - At r=0.12 (analytic, Appendix A), unconditional rmcorr power is 0.34 at N=24, k=8 and 0.91 at N=24, k=32. So the design's real k could rescue a Hoffman-size *unconditional* effect, but not obviously the conditional one.
  - **Fix:**
    1. Re-simulate the actual estimand: condition-structured metric, a stated between-condition variance share (pilot-estimate it; scan 0.5–0.9), random slopes, 7-point discretisation, k = 32 and k = 16 (if episodes get cut).
    2. Add r = 0.12 as the pessimistic anchor and justify any larger effect size.
    3. Replace "would need n≈543" with the trial-level comparison.
    4. Until then, downgrade §1.6 and §8 from a recommendation to "feasible only if within-condition metric variance is substantial; to be estimated in the pilot".
    5. Consider a design that adds *within-condition* variance on purpose, e.g., parametrically varying interruption onset phase or injected latency inside each condition. That spread is what the incremental claim needs.

### MAJOR

- **[W2] MAJOR: the ethics timeline arithmetic is optimistic and internally inconsistent, and the institution is unknown.** Location: §7 "Projected timeline for IROS".
  - **The arithmetic.**
    - "6–8 weeks plus one revision round, a mid-November 2026 submission → approval ~early/mid-January 2027" does not add up.
    - LMU's 6–8 weeks explicitly *assume no revisions* (verifier §A(f)). Mid-Nov + 6–8 weeks is already ~27 Dec–10 Jan.
    - Adding ETH's "+2–3 weeks if revisions" gives ~10–31 Jan, before any allowance for the holiday closure ("until 4 Jan 2027") the draft itself lists.
    - ETH also requires submission "≥2 months before recruitment" (→ mid-Jan at the earliest).
  - **The schedule squeeze.** `02-iros-2027-constraints.md` freezes experiments mid-Feb with submission on 1 Mar. On those numbers, data collection would realistically be squeezed into ~late Jan–mid Feb, before analysis and writing.
  - **The institution is unknown.** `08` Q8 ("is there an institutional ethics route?") is still open, and the draft does not say which committee the projection assumes.
  - **Missing dependency.** The study requires the G2 mid-motion repair condition to run reliably on real SO-101 by mid-Jan. The risks section does not list this.
  - **Fix:**
    - Recompute with explicit assumptions (institution, revision rounds, closures) and give a best/likely/worst range.
    - State that the protocol must be frozen (including the metric definitions from G1) before submission ~mid-Nov.
    - Add "G2 method ready on hardware" as a gating dependency.
    - State the fallback explicitly: the human-validity component moves to the ICRA 2028 version.

- **[W3] MAJOR: Hoffman's metrics may be ill-defined for this task, and the draft does not address it.** Location: §8 "Hoffman H-IDLE/R-IDLE/C-ACT/F-DEL computed per episode".
  - Hoffman's metrics assume a *shared task in which both agents act* (human idle vs active, concurrent activity, functional delay between agents' actions).
  - In the proposed episodes, the human speaks a correction while a single arm moves. What "human active" means is undefined: speaking only? Watching? So H-IDLE ≈ 1 − speech fraction, C-ACT ≈ the overlap of speech and motion, and F-DEL is unclear for a cancel or a backchannel.
  - The draft criticises Hoffman's video-based validity (§2 inference) but then imports the metrics into a structurally different interaction without operational definitions.
  - **Fix:** either
    - define human activity operationally (e.g., speech + gesture + a concurrent human subtask), or
    - redesign the task so the human also acts physically (e.g., the human stages objects while the robot picks), or
    - demote Hoffman metrics to exploratory and say why.

    Also apply Hoffman's "ringing"/few-turn caveat (§2) explicitly to episodes that are only a few seconds long.

- **[W4] MAJOR: the criterion measure (per-episode micro-ratings) is unvalidated, and some episode types have nothing to rate.** Locations: §8 "Per-episode micro-rating" and "Episodes".
  - The validity claim validates metrics *against* 1–2 ad-hoc items ("The robot handled my correction smoothly"; "The robot reacted in time"). No reliability or convergent validity is planned.
  - The episode mix includes "backchannel-should-not-interrupt" and "cancel". For a backchannel there is no correction to rate "smoothly", and "post-repair success" is undefined for a cancel.
  - "The robot reacted in time" is close to the Skantze & Irfan item that failed to separate conditions (see W6). That makes it a risky primary criterion.
  - **Fix:**
    - Adapt the micro-items from Hoffman's 3-item direct fluency subscale, or pre-specify a convergent-validity check: the per-condition mean of the micro-ratings vs the per-condition Hoffman composite, with a target r.
    - Define type-specific items or exclude non-correction types from the primary analysis.
    - Report within-person reliability (e.g., split-half across repeated episodes).

- **[W5] MAJOR: no primary metric is pre-specified, so the analysis has many forking paths.** Location: §8 "Objective metrics logged per episode" + "Analysis".
  - About 13 candidate predictors are listed: 6 benchmark metrics, 4 Hoffman metrics, MAD-TN, 2 speech-timing measures. Combined with 2 rating items and LMM-or-rmcorr alternatives, a "pre-registered" claim that "benchmark metrics predict ratings" without a named primary metric is weak.
  - **Fix:**
    - Name one primary predictor (or a pre-specified composite, e.g., the first PC of the benchmark metrics, or a benchmark score defined in G1) and one primary rating.
    - Treat the rest as secondary with FDR control.
    - Run the power analysis for that primary test.

- **[W6] MAJOR: the Skantze & Irfan Q3 null result is over-read in the bottom line and in Risk 2.** Locations: §1.3 "did **not** differ (Bonferroni p = 1.0)"; §9.2 "perceived responsiveness may not track objective latency (Skantze & Irfan Q3)".
  - A Bonferroni-adjusted p capped at 1.0 across many items is weak evidence of *no difference*.
  - The medians point the expected way: per the verifier, the proposed system was 2 (2–3) vs baseline 3 (2–4) on "slow to respond".
  - The headline "objective timing gains do not map one-to-one onto perceived timing" is therefore an inference from absence of evidence, resting on a single source.
  - **Fix:**
    - Rephrase as "a 1.2 s median reduction did not produce a significant difference on the single 'slow to respond' item after Bonferroni correction (medians 2 vs 3)".
    - Flag it as a single-item, single-study observation.
    - Add the live-HRC dissociation evidence from W7.

- **[W7] MAJOR: a critical finding rests on one source, and live co-located HRC studies are missing.** Locations: §2 inference ("criterion validity … mostly third-person/video-based. No study we found…"); §3 table; §1.3.
  - The claim that objective improvements diverge from experience in *live* interaction rests on Skantze & Irfan (speech-only Furhat, no manipulation) and τ-bench (text agents).
  - Two directly relevant live, co-located studies are missing:
    - **Kille et al. 2025, arXiv 2505.04182 (KIT/Freiburg).**
      - Design: n=26 analysed, within-subject, 4 automation levels, physical HRC (a drilling task with an LBR).
      - Finding: higher automation *improved task accuracy* but *reduced flow and sense of agency* (an inverted U).
      - They also relate an objective signal to experience: ranked grip force ↔ SoA r=0.20, p=.045.
      - This is direct evidence of a performance↔experience dissociation in live physical HRC.
    - **RAPIDDS, Cuellar, Hagenow & Shah 2026, arXiv 2604.19670 (MIT).**
      - Design: n=32, 4 systems, Latin square, objective spatial/temporal costs plus a Hoffman-style fluency survey per system.
      - It reports both condition effects but *no* metric↔rating link.
      - It is a close design precedent (and shows that N=32 with 4 conditions is a normal size for this design).
  - Also, the "No study we found" claim has no search log (queries, databases, date) to back it.
  - **Fix:**
    - Add both papers to §3, and use RAPIDDS as a design precedent in §5/§8.
    - Add a short search-log paragraph.
    - Keep the gap statement scoped as written ("no study we found …"); it survives these additions.

- **[W8] MAJOR: the simulated-vs-real agreement check is statistically uninformative as specified.** Location: §8 "Report Kendall τ between simulated and human condition rankings and ICC per metric."
  - With 4 conditions there are only 24 possible rankings, so even τ=1 is barely significant (one-sided p≈0.04) and τ cannot be estimated precisely.
  - It is also unclear *what* is ranked: objective metrics under simulated vs human speakers, or simulated "ratings" (which §6 says must never be reported as perception).
  - "ICC per metric" between a TTS speaker and a human requires matched episodes, which the draft does not define.
  - **Fix:**
    - Define the unit: e.g., condition × interruption-type × onset-phase cells (≈4×5×k), with the objective benchmark metric measured under TTS vs human speech in matched cells.
    - Report a cell-level agreement correlation or ICC with bootstrap CIs, and pre-specify a minimum agreement threshold.
    - Keep simulated users only as a source of *speech input*, never of ratings.

- **[W9] MAJOR: the session-time budget is not supported.** Location: §8 "Session ≤75 min" together with the episode, questionnaire and annotation lists.
  - The design packs the following into ≤75 min:
    - ≥32 physical episodes on SO-101 with scene resets;
    - 32+ micro-ratings;
    - 4 × (Hoffman composite + raw NASA-TLX + trust scale, plus SUS "if time allows");
    - PMQ (18 items) at the end;
    - an optional 5th WoZ condition;
    - a post-session playback annotation (Skantze & Irfan).
  - The draft's own precedents point the other way. Skantze & Irfan needed **1.5 h** for only 2×7 min of interaction including annotation. Song et al. needed ~30 min for only 4 runs.
  - **Fix:**
    - Make a time budget per component (reset time per SO-101 episode measured in the pilot).
    - Cut playback annotation to a sampled subset or replace it with in-episode button presses.
    - Drop the WoZ condition for IROS, and move PMQ/SUS to a single end-of-session administration.

- **[W10] MAJOR: the refined G4 claim conflicts with `06-paper-story.md` C3, and the draft does not flag it.** Location: §8 "Claim to target (refined G4)" vs `06-paper-story.md` C3, "showing correlation of benchmark metrics with Hoffman fluency metrics and PMQ/SUS".
  - Correlating benchmark metrics with Hoffman *objective* metrics is objective↔objective, not validity against perception.
  - PMQ and SUS are once-per-condition or once-per-session measures, so they cannot carry a trial-level claim.
  - The draft silently replaces C3 but does not say that the paper story must change. That leaves two incompatible C3s in the project.
  - **Fix:** add an explicit "Implications for 06-paper-story" note. C3 should become "trial-level benchmark metrics predict per-episode human ratings (primary), with Hoffman metrics and PMQ/SUS as secondary or exploratory".

- **[W11] MAJOR: "only reachable with a trial-level design" overstates the case and omits a complementary design.** Location: §1.6.
  - A third-person rating study is a standard way to get power for a metric↔perception link: recorded SO-101 episodes rated online by many raters (Prolific), which is exactly the Hoffman and Weiss paradigm.
  - The draft rightly says video ratings are not co-located experience. But it can serve as a large-N secondary arm: hundreds of raters × the same logged episodes, which lets metric↔rating slopes be estimated precisely. It is also independent of in-lab session time, though it still needs ethics cover.
  - **Fix:** say "most directly reachable with …". Add a third-person rating arm as an optional complement, with the explicit caveat that it measures observer perception, not participant experience.

### MINOR

- **[W12] MINOR: status-flag misuse (the draft's own legend says snippets are [S]).**
  - §2 MAD-TN: "[V] metric definitions via ar5iv snippet". By the draft's legend, a snippet is [S]. The verifier confirmed the definitions in the arXiv PDF, so upgrade with that provenance.
  - §2 Weiss: "Hoffman's 8 statements" sits under [V], but the verifier saw only F1, F2, F5 and F6 (§E). Mark it [U] or verify.
  - §2/§1.1: "Pearson" sits under [V] but was not checked (verifier §E).
  - §3 CDS: the "KTH et al." affiliation sits under [V] and was not checked.
  - §4 Almere: "[V] (Springer abstract/metadata)" with the claim "Long". The item count was not verified, and only metadata was checked.
  - §6 PACT: "PACT itself has no real-human evaluation. … [V]". The verifier says this is an inference.
  - §3 Synthetic TLX: "[V, per verifier quote]". Cite the paper quote rather than the verifier.

  **Fix:** correct each flag; add provenance.

- **[W13] MINOR: inference stated as fact about Song et al.** Location: §1.4 "A 15-pp end-to-end success gain (75%→90%) was perceptible".
  - Success was not measured in-session, and the improved configuration may differ in latency and other properties.
  - **Fix:** "Participants detected and preferred the configuration that a prior ablation found to be 15 pp more successful."

- **[W14] MINOR: "The one direct validity study" contradicts the next bullet.** Location: §1.1.
  - Weiss et al. (§1.2) is also a direct validity study of the same metrics.
  - **Fix:** "The original validity study …".

- **[W15] MINOR: the adjacent-prior-art sample sizes are heterogeneous, unflagged, and used for an unsupported generalisation.** Location: §5 "SocialVLA n=15 … Within-subject designs dominate for system comparisons."
  - My check (Appendix B) shows these are not comparable "user studies":
    - **SocialVLA:** 15 is an annotated *reaction corpus* plus 1 prospective participant, with no questionnaires.
    - **ExpressMM:** 23 is a *classroom audience* watching one researcher interact, single-condition, using adapted Almere + PMQ items on a TurtleBot-4 + SO-101.
    - **MICoBot:** 18 is 6 per task × 3 tasks, 2 systems.
  - "Within-subject designs dominate" has no flag and is not supported by this list.
  - **Fix:** add a "study type / conditions / rating instrument" column, flag the list [S] (carried over) or [V] where checked here, and delete or source the generalisation.

- **[W16] MINOR: the questionnaire section misses a direct precedent and has notation drift.** Locations: §4 PMQ and Almere rows; §8 "Hoffman 8-item fluency composite (minus weak item)".
  - ExpressMM already used adapted PMQ + Almere items on an **SO-101** platform. That is a precedent for "PMQ on an embodied arm" and the likely source of 06's PMQ choice. The draft's "skip Almere" and "embodied-arm use is an extrapolation" should acknowledge it and explain why we diverge.
  - "8-item composite minus the weak item" is 7 items. Say "7-item".
  - Individual item wording is [U] (§4), yet the instrument is recommended for first-person, co-located use when it was validated for third-person video. Note that adapting it is required.

- **[W17] MINOR: the power-script "check" compares different tests.** Location: §8 "paired n for d_z=0.5 = 34 (matches the G*Power value reported by Skantze & Irfan)".
  - Skantze & Irfan's 34 came from an f=0.25 repeated-measures ANOVA setting, not from a paired t with d_z=0.5. The numerical match is a coincidence of conventions.
  - **Fix:** cite G*Power's paired-t output (34) as the reference, not Skantze & Irfan.

- **[W18] MINOR: the multiplicity adjustment is not reflected in the minimum detectable effects.** Location: §8 table row "Paired t, min. detectable d_z (80%)".
  - With 4 conditions (6 pairwise contrasts) and Holm, the first-step α is .05/6. The minimum detectable d_z becomes 0.92 / 0.77 / 0.58 at N = 18 / 24 / 39 (Appendix A), not 0.70 / 0.60 / 0.46.
  - `05-gap-analysis` itself warns that "Gains may be small vs stop-and-replan".
  - **Fix:** add the Holm-adjusted row, or pre-specify one planned contrast (mid-motion repair vs stop-and-replan).

- **[W19] MINOR: balancing breaks at the minimum and stretch N.** Location: §8 "balanced Latin square for 4 conditions), minimum 18, stretch 39".
  - A balanced 4×4 Latin square needs multiples of 4; 18 and 39 break the counterbalancing.
  - **Fix:** use 20 / 24 / 40, or state the partial-balance handling.

- **[W20] MINOR: zombie and orphan material.**
  - **Sources:** "Kennington et al. benchmark proposal — 2610.08733" is never cited in the body.
  - **§10:** "Lasota & Shah 2015" and "CMU HRI 2026 bidirectional pHRI" are listed as blocked but are never used in the body.
  - **§6 PACT:** "Clarification Utility U = Acc/(1+AskRate)" is irrelevant to G4.
  - **§7:** "WU Vienna" and "TU Chemnitz: next board meeting 19.10.2026 [S snippet]" relate to no known team institution, and the Chemnitz date is one day from today, so it is stale on arrival.
  - **§1.5 vs §6:** EchoChain is described twice.
  - **Fix:** delete these, or give each a one-line reason for being there. Keep only the ethics bodies relevant to the team once `08` Q8 is answered.

- **[W21] MINOR: the "Not to claim" list is incomplete, and one risk sentence could be read as an interruption-novelty claim.** Locations: §8 "**Not to claim:**" and §9.3 "Differentiation must be interruption + physical repair + trial-level validity."
  - No sentence in the draft re-asserts a forbidden novelty claim. I checked the timing-as-decision-variable, first-interruption-user-study and speech-barge-in-stop claims.
  - But the "Not to claim" list omits several items from `05`:
    - **Timing/commit as a decision variable:** RIAP, Premover.
    - **Speech barge-in stops a robot:** ELLSA (sim) and VITA-E (it lists VITA-E only under "full-duplex physical preemption").
    - **Acting on partial speech:** Premover, Tufts/TUW.
    - **First false-stop + latency with users:** SocialVLA. This matters because the benchmark metrics include false-barge-in and latency.
  - §9.3 lists "interruption" as a differentiator. Against Song that is true, but read on its own it suggests interruption user studies are new (SocialVLA, CMU HRI 2026, MICoBot and ExpressMM all exist).
  - **Fix:**
    - Copy the full `05` do-not-claim list into §8.
    - Rephrase §9.3 as "Differentiation vs Song et al.: interruption-specific physical-repair metrics + trial-level metric↔rating validity. Interruption user studies per se are not new (05)".
    - The §1.4 sub-bullet "no interruptions or mid-motion repair" is fine as a statement about Song only.

- **[W22] MINOR: claims with no support.**
  - §2 "widely used": no evidence, e.g., a citation count.
  - §7 "IROS reviewers still expect an ethics approval statement": no IROS policy cited.
  - §7 "DPIA-lite": not a GDPR term. Say "DPIA screening (Art. 35)" instead.
  - The simulated-user conclusion (§1.5) generalises from τ-bench text agents and NASA-TLX to embodied speech HRI. The conclusion is conservative, but the scope should be stated.

## Questions for Authors

- **[Q1]** What share of each benchmark metric's variance do you expect to be *within* condition? Without a pilot estimate, the "beyond condition labels" claim cannot be powered (W1).
- **[Q2]** Which single metric (or composite) is the primary predictor, and which single item is the primary criterion (W4, W5)?
- **[Q3]** Operationally, what counts as "human active" for H-IDLE/C-ACT in a speech-only supervision episode (W3)?
- **[Q4]** Which ethics committee will review this, and is there an umbrella approval (W2, `08` Q8)?
- **[Q5]** For the simulated-vs-real check, is the compared quantity the objective metric under TTS vs human speech, or something else (W8)?
- **[Q6]** What is the measured reset time per SO-101 episode? It drives the 75-min budget (W9).
- **[Q7]** Were CMU HRI 2026 (n=18 older adults) and RIAP (N=30) checked for metric↔rating analyses? Both remain unverified scoop surfaces for the narrowed G4.

## Verdict

The **literature synthesis (§§2–4, 6) is accurate and appropriately hedged** where checked, and it reflects the verifier's corrections. The **design and feasibility section (§8, with §1.6 and §7's timeline) is not yet decision-grade**:
- the power analysis targets a different estimand than the refined claim, with an inconsistent trial count and an unsourced effect size (W1);
- the ethics critical path is optimistic by roughly 2–4 weeks (W2);
- the construct and criterion validity of the measures is not addressed (W3, W4);
- the analysis has no named primary test (W5).

None of this changes the qualitative conclusion that G4 survives only as a narrow, trial-level, interruption-specific validity claim; my own scoop checks support that conclusion. It does change whether N≈24 within the IROS window is credible.

**Revision priority:** High for §8/§1.6/§7, low–medium for §§2–6.

**Confidence:** 0.8. The main uncertainties are the true within-condition metric variance (unknown until a pilot) and the unread CMU HRI 2026 and RIAP full texts.

## Revision Plan

1. **(W1) Redo the power simulation for the actual estimand.**
   - Simulate condition-structured metrics (between-condition variance share 0.5–0.9), random slopes, 7-point discretisation, k ∈ {16, 32}, and r ∈ {0.12, 0.2, 0.3}.
   - Report power for "metric beyond condition".
   - Rewrite §1.6 and the §8 table accordingly.
   - Add within-condition parametric variation (onset phase / injected latency) to the design.
2. **(W5, W4) Pre-specify the primary test and criterion.**
   - Name one primary predictor and one primary rating, with FDR control for the secondary tests.
   - Adapt the micro-items from Hoffman's direct-fluency subscale and add a convergent-validity check.
   - Restrict the primary analysis to correction-type episodes.
3. **(W2) Rebuild the ethics timeline.**
   - Name the institution and its revision and closure rules, and give best/likely/worst dates.
   - Add "protocol frozen by mid-Nov" and "G2 ready on hardware by mid-Jan" as gates.
   - State the ICRA 2028 fallback for the human-study component.
4. **(W3) Define Hoffman metrics operationally** for speech-supervised single-arm episodes, or redesign the task so the human acts concurrently. Otherwise demote them to exploratory.
5. **(W9) Build a measured time budget from a pilot** (n=4–6). Cut the WoZ condition and the full playback annotation; give PMQ/SUS once.
6. **(W8) Redefine the simulated-vs-real check** at the cell level, with a CI and a pre-set threshold, comparing objective metrics only.
7. **(W10) Add an "Implications for 06-paper-story" note** rewriting C3.
8. **(W6, W7, W11) Literature fixes.**
   - Soften the Q3 inference.
   - Add Kille et al. 2025 and RAPIDDS 2026.
   - Add a search log.
   - Mention a third-person rating arm as an optional complement.
9. **(W12–W22) Hygiene.**
   - Fix status flags and the 7-item drift.
   - Correct the G*Power check attribution, add Holm-adjusted MDEs, and choose N in multiples of 4.
   - Delete the zombies (Kennington, Lasota, CMU in §10, PACT U formula, WU Vienna/TU Chemnitz).
   - Complete the do-not-claim list and rephrase §9.3.

---

# Part 2: Inline Annotations

> "**The one direct validity study of Hoffman's objective fluency metrics finds weak links.**"

**[W14] MINOR:** Weiss et al. (next bullet) is also a direct validity study. Use "The original validity study".

> "In live speech HRI, objective timing gains do not map one-to-one onto perceived timing."

**[W6] MAJOR:** This rests on one non-significant Bonferroni-corrected item from one study (medians 2 vs 3, in the expected direction). State it as "did not reach significance on the single 'slow to respond' item". Add live physical-HRC evidence (Kille et al. 2025) if the general claim is kept.

> "but \"The robot was slow to respond\" did **not** differ (Bonferroni p = 1.0)."

**[W6] MAJOR:** "Did not differ" treats absence of evidence as evidence of absence. A Bonferroni-adjusted p of 1.0 is a cap, not an effect estimate.

> "A 15-pp end-to-end success gain (75%→90%) was perceptible"

**[W13] MINOR:** Success was not measured in the study sessions, and the systems may differ on other dimensions. Attribute the perception to the *configuration*, not to the success gain.

> "Correlations computed across participants are underpowered at these sizes; Hoffman-size effects (r≈0.12) would need n≈543. The validity claim is only reachable with a **trial-level design**"

**[W1] FATAL / [W11] MAJOR:**
- Hoffman's r(495) is a pooled *rating-level* correlation (~497 clip ratings), so comparing it with a between-participant n is a category error. At the trial level, r=0.12 has power ≈0.91 at N=24, k=32 (unconditional; Appendix A).
- "Only reachable" ignores third-person rating designs (Hoffman's and Weiss's own paradigm) as a large-N complement.

> "Example: N=24, 8 trials/participant, within-r=0.3 → simulated power 0.98."

**[W1] FATAL:**
- This is the unconditional rmcorr. The refined claim is "beyond condition labels", and power for that depends on the within-condition metric variance: 0.38–0.96 at r=0.2 in Appendix A.
- k=8 does not match the design's ≥32 episodes.
- r=0.3 is 2.5× the only prior estimate and has no source.

> "[V] abstract; [V] metric definitions via ar5iv snippet"

**[W12] MINOR:** By the draft's own legend, a snippet is [S]. The verifier confirmed the definitions in the arXiv PDF; cite that and keep [V].

> "MTurk viewers of real human+Sawyer videos, ~49–53 participants per metric set, Hoffman's 8 statements"

**[W12] MINOR:** "Hoffman's 8 statements" is not verified (the verifier saw F1, F2, F5 and F6 only). Mark it [U] or check Table 1 of the Weiss PDF.

> "Hoffman's metrics are well-defined and widely used."

**[W22] MINOR:** "Widely used" has no support. Add a citation count or examples, or drop it.

> "No study we found validates them for live, speech-mediated, *interrupted* manipulation. This is the defensible core of G4."

**[W7] MAJOR:**
- The statement holds after my checks of SocialVLA, MICoBot and ExpressMM (none relates metrics to ratings). But it needs a search log.
- It should cite the live co-located HRC studies that *do* collect both kinds of data: Kille et al. 2505.04182 (performance↑ yet flow/SoA↓; grip force↔SoA r=0.20) and RAPIDDS 2604.19670 (n=32, Latin square, fluency survey + objective costs, no linkage).
- CMU HRI 2026 and RIAP remain unchecked; say so.

> "Directly targets fluency; use the 8-item composite minus the weak item"

**[W16] MINOR:** That is 7 items. Item wording is [U], and the composite was validated for third-person video viewers, so adapting it to first-person co-located use must be stated.

> "Long and acceptance/intention-oriented → poor fit for a 60-min lab study"

**[W12]/[W16] MINOR:** "Long" is not verified (metadata only). ExpressMM used adapted Almere + PMQ items on SO-101. Acknowledge that precedent and justify the divergence. Note also "60-min" here vs "≤75 min" in §8.

> "SocialVLA n=15, CMU HRI 2026 n=18, MICoBot 18, ExpressMM 23, Song et al. 24 (new), RIAP N=30, Skantze & Irfan 39."

**[W15] MINOR:** These are not comparable user studies:
- SocialVLA: an annotated reaction corpus, no questionnaires.
- ExpressMM: a single-condition classroom audience.
- MICoBot: 6 per task.

Add study-type and condition columns and flag the list.

> "Within-subject designs dominate for system comparisons."

**[W15] MINOR:** This has no flag and no support; two of the listed studies have no condition comparison at all. Delete it or source it.

> "PACT itself has no real-human evaluation."

**[W12] MINOR:** This is an inference (the verifier notes the paper does not state it), yet it is under [V]. Mark it "(inference)".

> "Clarification Utility U = Acc/(1+AskRate). [V]"

**[W20] MINOR:** This is a zombie detail, irrelevant to the G4 validity question. Delete it.

> "Most universities and IROS reviewers still expect an ethics approval statement."

**[W22] MINOR:** Cite the IROS 2027 human-subjects policy or soften to "commonly expected".

> "TU Chemnitz: next board meeting 19.10.2026. [S snippet]"

**[W20] MINOR:** This institution is not linked to the team (08 Q8 is open), and the date is tomorrow, so it is stale on arrival. Delete it, or keep only the team's committee.

> "Inference: recording participants' speech is personal data (consent, DPIA-lite, retention plan)."

**[W22] MINOR:** "DPIA-lite" is not a GDPR concept. Use "DPIA screening under Art. 35".

> "with 6–8 weeks plus one revision round, a mid-November 2026 submission → approval ~early/mid-January 2027 → data collection mid-Jan to mid-Feb."

**[W2] MAJOR:** LMU's 6–8 weeks *excludes* revisions. Mid-Nov + 8 weeks + a 2–3-week revision round, plus the holiday closure, lands in late January. Name the institution, give a range, and add G2-on-hardware readiness as a gate.

> "**Claim:** trial-level physical-repair metrics from our benchmark predict participants' per-episode fluency and responsiveness ratings for *spoken mid-motion corrections* on SO-101, beyond what condition labels explain."

**[W1] FATAL / [W10] MAJOR:**
- The incremental ("beyond condition") estimand is not what `power.py` simulates.
- The claim also replaces 06-paper-story C3 (benchmark ↔ Hoffman metrics and PMQ/SUS) without saying so. Add an explicit note that C3 must be rewritten.

> "**Not to claim:** \"first user study with speech on a low-cost arm\" (Song et al. 2607.00530), \"first interruption user study\" (05-gap-analysis), or \"first full-duplex physical preemption\" (VITA-E per 04-literature-map.md; MIRA 2609.24547)."

**[W21] MINOR:** This list is incomplete relative to `05`. Add:
- timing/commit as a decision variable (RIAP, Premover);
- speech barge-in stopping a robot (ELLSA, VITA-E);
- acting on partial speech (Premover, Tufts/TUW);
- first false-stop + latency with users (SocialVLA).

> "**Participants:** target N=24 (balanced Latin square for 4 conditions), minimum 18, stretch 39."

**[W19] MINOR:** 18 and 39 are not multiples of 4. Use 20 / 24 / 40, or describe the partial balancing.

> "**Episodes:** ≥8 interruption episodes per condition, mixing interruption types (target change, constraint, cancel, backchannel-should-not-interrupt, self-correction). Session ≤75 min."

**[W9]/[W4] MAJOR:**
- ≥32 physical episodes plus resets, per-episode ratings, 4 questionnaire blocks, PMQ, playback annotation and an optional 5th condition will not fit in 75 min. Skantze & Irfan needed 1.5 h for 14 min of interaction.
- Backchannel and cancel episodes have no "correction" to rate.

> "(e.g., \"The robot handled my correction smoothly\"; \"The robot reacted in time\")"

**[W4] MAJOR:** These are unvalidated single items, used as the *criterion* in a validity claim. Adapt them from Hoffman's direct-fluency subscale and add a convergent-validity check against the per-condition composite.

> "Hoffman H-IDLE/R-IDLE/C-ACT/F-DEL computed **per episode**, as Hoffman recommends for few turns."

**[W3] MAJOR:** In a speech-supervised single-arm episode, "human active" is undefined, so H-IDLE and C-ACT reduce to speech-fraction and overlap measures. Define the human activity or redesign the task. Hoffman's per-turn advice also comes with a "ringing" caveat for short sequences.

> "Primary: linear mixed model `rating ~ metric + condition + (1|participant)` or repeated-measures correlation."

**[W5] MAJOR:**
- "Or" leaves the primary test open, and "metric" is one of ~13 candidates.
- The two options estimate different things: rmcorr does not adjust for condition.
- Pre-specify one model, one predictor and one criterion. Consider random slopes and an ordinal (CLMM) link.

> "Report Kendall τ between simulated and human condition rankings and ICC per metric."

**[W8] MAJOR:** With 4 conditions, τ is nearly uninformative (24 permutations). Define matched cells (condition × type × onset phase), compare objective metrics under TTS vs human speech, and report agreement with a CI and a pre-set threshold.

> "Checks: paired n for d_z=0.5 = 34 (matches the G*Power value reported by Skantze & Irfan)"

**[W17] MINOR:** Skantze & Irfan's 34 came from an f=0.25 ANOVA configuration. Cite G*Power's paired-t output as the reference instead.

> "Secondary: paired condition contrasts with Holm correction. Pre-register on OSF."

**[W18] MINOR:** The table's minimum detectable d_z values ignore this Holm correction. At α=.05/6 they are 0.92 / 0.77 / 0.58 for N = 18 / 24 / 39.

> "Mitigation: trial-level design, strong manipulation spread, threshold or tercile analysis."

**[W1] FATAL (linked):** Spread created by the manipulation is absorbed by the condition dummies in the "beyond condition" model. What helps is *within-condition* spread.

> "Differentiation must be interruption + physical repair + trial-level validity."

**[W21] MINOR:** "Interruption" is a differentiator only relative to Song et al. Interruption user studies exist (SocialVLA, CMU HRI 2026, MICoBot, ExpressMM; 05). Rephrase so it cannot be read as a novelty claim.

> "Kennington et al. benchmark proposal — https://arxiv.org/abs/2610.08733"

**[W20] MINOR:** This is an orphan source, never cited in the body. Cite it where relevant (e.g., §3, speech-HRI benchmark validity) or remove it.

> "Lasota & Shah 2015 Human Factors (PMC page JS-rendered; not read)."

**[W20] MINOR:** This appears only in §10. Either explain why it matters (objective safety/efficiency + subjective comfort in close-proximity HRC; cited by RAPIDDS) or remove it.

---

## Appendix A: Independent power checks (reviewer-run, not in the repo)

**Reproduction.** `python experiments/g4-fluency-metrics-validity/power.py` → output identical to `power_results.txt` after CRLF normalisation; runtime ~4 s.

**Analytic rmcorr power at Hoffman's r = 0.12** (Fisher z, df = N(k−1)−1):

| N | k=8 | k=32 |
|---|---|---|
| 18 | 0.27 | 0.81 |
| 24 | 0.34 | 0.91 |
| 39 | 0.51 | 0.99 |

**Holm first-step (α = .05/6) minimum detectable d_z at 80% power:** N=18: 0.92; N=24: 0.77; N=39: 0.58.

**Simulation: "beyond condition" vs unconditional.** Settings: N=24, 4 conditions × 8 episodes, 1000 simulations.
- **Model:** the metric x = condition mean + within-condition noise, scaled so that a fixed share of x's variance is between conditions. The rating y = participant offset + r·x + noise.
- **Beyond-condition test:** correlation after centring within participant × condition, df = N·C·(k−1)−1. This approximates the condition-adjusted LMM with participant intercepts.
- **Unconditional test:** correlation after centring within participant (as in `power.py`).

| Between-condition share of metric variance | r | Power beyond condition | Power unconditional |
|---|---|---|---|
| 0.5 | 0.12 | 0.62 | 0.93 |
| 0.5 | 0.20 | 0.96 | 1.00 |
| 0.8 | 0.12 | 0.31 | 0.93 |
| 0.8 | 0.20 | 0.68 | 1.00 |
| 0.8 | 0.30 | 0.95 | 1.00 |
| 0.9 | 0.12 | 0.16 | 0.92 |
| 0.9 | 0.20 | 0.38 | 1.00 |
| 0.9 | 0.30 | 0.74 | 1.00 |

**Caveats:**
- There are no random slopes and ratings are continuous, so true power is lower still.
- Here r is the total metric–rating correlation; the incremental effect is carried only by the within-condition component.

Core of the simulation:
```python
cmeans = np.linspace(-1, 1, C); cmeans = cmeans / cmeans.std() * np.sqrt(share)
x = cmeans[None, :, None] + rng.normal(size=(N, C, k)) * np.sqrt(1 - share)
y = rng.normal(size=(N, 1, 1)) + r * x + np.sqrt(1 - r**2) * rng.normal(size=x.shape)
# beyond-condition: centre within participant x condition; df = N*C*(k-1)-1
# unconditional: centre within participant; df = N*(C*k-1)-1
```

## Appendix B: Scoop and related-work checks (reviewer-run)

| Paper | Ratings collected? | Metric ↔ rating analysis? | Notes |
|---|---|---|---|
| SocialVLA 2610.02360 | No questionnaires | No | 15-participant annotated reaction corpus + 1 prospective participant; Unitree G1; stop-centric |
| MICoBot 2508.05535 | 5-pt Likert (satisfaction, communicative ability, …), preference | No (condition-level Wilcoxon only) | TIAGo; 6 per task × 3 tasks; sequential turn-taking; no mid-motion interruption |
| ExpressMM 2604.05320 | 5-pt Likert, adapted Almere + PMQ items | No; single-condition descriptive | 23 students watched one researcher interact live; TurtleBot-4 + SO-101 |
| Kille et al. 2505.04182 | Flow Short Scale, SoA, embodiment, satisfaction | Partly: grip force ↔ SoA r=0.20; HRV → flow classification failed (61% accuracy) | Co-located physical HRC, n=26 analysed, 4 automation levels; performance↑ but flow/SoA↓ at high automation |
| RAPIDDS 2604.19670 | Fluency survey per system + ranking | No (condition-level ART ANOVA) | n=32, 4 systems, Latin square, 7-DoF arm; objective spatial/temporal costs |

None of these papers invalidates the narrowed G4 claim. Kille et al. and RAPIDDS should be cited: Kille et al. as evidence that performance and experience dissociate, and RAPIDDS as a design precedent.

## Sources

- Draft under review: `outputs/.drafts/g4-fluency-metrics-validity-draft.md`
- Verification report: `outputs/.drafts/g4-fluency-metrics-validity-verification.md`
- Power script / results: `experiments/g4-fluency-metrics-validity/power.py`, `power_results.txt`
- Project context: `05-gap-analysis.md`, `06-paper-story.md`, `02-iros-2027-constraints.md`, `04-literature-map.md`, `08-open-questions-and-access-needs.md`
- SocialVLA — https://arxiv.org/abs/2610.02360
- MICoBot — https://arxiv.org/abs/2508.05535
- ExpressMM — https://arxiv.org/abs/2604.05320
- Kille et al., "Beyond Task Performance: Human Experience in Human-Robot Collaboration" — https://arxiv.org/abs/2505.04182
- Cuellar, Hagenow, Shah, "Multi-Cycle Spatio-Temporal Adaptation in Human-Robot Teaming" (RAPIDDS) — https://arxiv.org/abs/2604.19670
- alphaXiv search used for the gap check — https://www.alphaxiv.org (query: objective fluency metrics ↔ subjective fluency ratings in HRC)

---

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Review written to outputs/.drafts/g4-fluency-metrics-validity-review.md with a structured review (1 FATAL, 10 MAJOR, 11 MINOR, each with location and fix), inline annotations quoting exact draft text (all quotes grep-verified as unique matches), Appendix A (re-run plus extended power checks) and Appendix B (scoop checks), and residual risks listed below."
    }
  ],
  "changedFiles": [
    "outputs/.drafts/g4-fluency-metrics-validity-review.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python experiments/g4-fluency-metrics-validity/power.py > /tmp/power_rerun.txt; diff (CRLF-normalised) vs power_results.txt",
      "result": "passed",
      "summary": "Output byte-identical after CRLF normalisation; all §8 table values match after rounding"
    },
    {
      "command": "python /tmp/g4chk.py (reviewer-written check: analytic rmcorr at r=0.12, Holm-adjusted MDE, beyond-condition vs unconditional simulation)",
      "result": "passed",
      "summary": "r=0.12 power 0.34 (k=8) / 0.91 (k=32) at N=24; Holm MDE 0.92/0.77/0.58; beyond-condition power 0.38–0.96 at r=0.2 depending on between-condition variance share"
    },
    {
      "command": "grep -c for 27 quoted draft passages",
      "result": "passed",
      "summary": "Every inline-annotation quote matches exactly once in the draft"
    },
    {
      "command": "alpha_ask_paper on 2610.02360, 2508.05535, 2604.05320, 2505.04182, 2604.19670; alpha_search for objective↔subjective fluency",
      "result": "passed",
      "summary": "No scoop of the narrowed G4 found; two missed related works identified (Kille et al. 2025, RAPIDDS 2026)"
    }
  ],
  "validationOutput": [
    "power.py reproduces power_results.txt exactly",
    "All verifier fixes I1–I4 and H1 confirmed present in the draft; H2 partially addressed",
    "The draft itself was not edited"
  ],
  "residualRisks": [
    "CMU HRI 2026 (paywalled) and RIAP (no preprint) not checked for metric↔rating analyses; they remain possible scoop surfaces for the narrowed G4.",
    "The beyond-condition simulation is a simplified approximation (participant×condition centring, no random slopes, continuous ratings); real power depends on pilot-estimated within-condition metric variance.",
    "The gap search was a single alphaXiv query; older HRC studies (e.g., Lasota & Shah 2015, Gombolay et al., Hoffman & Breazeal 2007) were not read and could contain trial-level objective↔subjective analyses.",
    "Ethics timeline critique assumes the LMU/ETH rules the draft cites; the team's actual institution is unknown (08 Q8)."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one new review file; no other files modified.",
  "reviewFindings": [
    "FATAL W1: §8/§1.6 power simulation tests unconditional rmcorr at k=8 with unsourced r=0.2–0.3, while the claim is 'beyond condition labels' with ≥32 episodes; Hoffman r=0.12 is mis-framed as between-participant",
    "MAJOR W2: §7 ethics timeline arithmetic optimistic (LMU 6–8 wk excludes revisions; holiday closure); institution unknown; G2 readiness not gated",
    "MAJOR W3: Hoffman H-IDLE/C-ACT undefined for speech-supervised single-arm episodes",
    "MAJOR W4/W5: unvalidated micro-rating criterion; no pre-specified primary metric among ~13",
    "MAJOR W6/W7: Skantze Q3 null over-read; live HRC evidence rests on one source; Kille 2025 and RAPIDDS 2026 missing",
    "MAJOR W8: Kendall τ over 4 conditions uninformative",
    "MAJOR W9: 75-min session budget unsupported",
    "MAJOR W10: refined claim conflicts with 06-paper-story C3 without flagging",
    "MAJOR W11: 'only reachable' overstates; third-person rating arm omitted",
    "MINOR W12–W22: status-flag misuse (snippet as [V], unverified 'Pearson'/'8 statements'/KTH/PACT inference), notation drift (8 vs 7 items), zombie sources (Kennington, Lasota, PACT U, TU Chemnitz), incomplete do-not-claim list (RIAP/Premover/ELLSA/SocialVLA), G*Power check misattributed, Holm MDE omitted, Latin-square N"
  ],
  "manualNotes": "No sentence in the draft re-asserts forbidden novelty (timing-as-decision-variable, first interruption user study, speech barge-in stop). The issues are an incomplete do-not-claim list and one ambiguous risk sentence (§9.3). The literature synthesis is sound; the decision-relevant problems are concentrated in §8, §1.6 and §7's timeline."
}
```
