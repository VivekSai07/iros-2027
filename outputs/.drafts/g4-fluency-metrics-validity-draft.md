# G4 — Do benchmark metrics predict human-perceived fluency in speech-driven HRC on low-cost arms? (literature review, 2026-10-18)

Status flags: **[V]** verified from primary page/abstract/full text in this run; **[S]** secondary only (search snippet, citing paper, or AI summary not cross-checked); **[U]** unverified. "Full text" = text retrieved through alphaXiv/arXiv or an author-hosted PDF.

## 1. Bottom line

1. **The one direct validity study of Hoffman's objective fluency metrics finds weak links.** Hoffman (2019) correlated the four metrics with an 8-item subjective fluency composite: |r| ≤ 0.123. F-DEL had the strongest (negative) correlation, H-IDLE was *positively* correlated, R-IDLE and C-ACT were not significant. Raters were online (MTurk) viewers of ~40 s simulated clips, not co-located participants. [V]
2. **A follow-up on real-robot video (Weiss et al., 2023) mostly found evidence *against* per-metric effects.** The exceptions were concurrent activity/concurrent idleness (strongest effect on the "team fluency" item) and weak support for some others. Again video, MTurk, Sawyer. [V]
3. **In live speech HRI, objective timing gains do not map one-to-one onto perceived timing.** Skantze & Irfan (HRI 2025, n=39, within-subject) reduced median response time (1.5 vs 2.7 s) and interruption rate (6.9% vs 16.6%). Participants rated the system more fluid and preferred it, but "The robot was slow to respond" did **not** differ (Bonferroni p = 1.0). [V]
4. **Closest scoop-risk paper (2026-07):** Song et al. (arXiv 2607.00530) ran a within-subject study (n=24) with spoken commands on a low-cost **Dobot Magician** arm. A 15-pp end-to-end success gain (75%→90%) was perceptible: preference 17/24, p=0.043; d_z 1.54–2.03 on speed/reliability/fluency composites. [V]
   - **Limitation that leaves G4 open:** the objective numbers come from a *prior ablation*, not from the study sessions. There is no trial-level or participant-level metric↔rating correlation, and no interruptions or mid-motion repair. [V]
   - **Consequence:** we can no longer claim "first study checking benchmark metrics against user perception on a low-cost arm with speech". G4 must be scoped narrower (see §8).
5. **Simulated users are useful for scale but are not validated substitutes for people.** On τ-bench, 451 real users vs 31 LLM simulators: simulators are over-cooperative and inflate agent success (top simulators 77.8% vs human 63.6%). LLM-rated quality is inflated, and binary task reward is "largely orthogonal" to human-perceived quality. [V]
   - EchoChain validates only that its *cloned voices* are indistinguishable from real recordings (240 judgments; χ² p=0.63). It does not validate simulated-user *behaviour*. [V]
6. **Feasibility for n≈18–39 (our calculation, `experiments/g4-fluency-metrics-validity/power_results.txt`).** Correlations computed across participants are underpowered at these sizes; Hoffman-size effects (r≈0.12) would need n≈543. The validity claim is only reachable with a **trial-level design**: many interruption episodes per participant, per-episode micro-ratings, and a repeated-measures correlation or mixed model. Example: N=24, 8 trials/participant, within-r=0.3 → simulated power 0.98.

## 2. Hoffman fluency metrics — primary sources

| Item | Finding | Status |
|---|---|---|
| Primary journal source | G. Hoffman, "Evaluating Fluency in Human–Robot Collaboration," *IEEE Trans. Human-Machine Systems* 49(3):209–218, 2019, DOI 10.1109/THMS.2019.2904558. Read via the author-hosted PDF (hrc2.io); IEEE Xplore version is paywalled/closed OA per OpenAlex | [V] |
| Earlier version | Hoffman, RSS 2013 Workshop on Human-Robot Collaboration (author page says "please refer to the new journal version") | [V] (author page) |
| Origin of 3 of the 4 metrics | Hoffman 2019 states C-ACT, H-IDLE, F-DEL were proposed in Hoffman & Breazeal, "Cost-based anticipatory action-selection for human-robot fluency," IEEE T-RO 23(5), 2007; R-IDLE added later | [V] as cited in Hoffman 2019; T-RO paper itself not read [U] |
| Definitions | H-IDLE = % of total task time the human is not active. R-IDLE = % of time the robot is not *perceivably* active; authors may include or exclude internally-active-but-seemingly-idle time. C-ACT = % of time both agents are active. F-DEL = accumulated time between one agent finishing and the other starting, as a ratio of task time; can be negative with overlap and can exceed 1 | [V] |
| Subjective fluency scale | Fig. 1 inventory: 3-item direct fluency scale + 6 downstream scales (incl. adapted Working Alliance Inventory). Validity study used an 8-item composite, 7-pt Likert; α=0.81 (pretest n=21), α=0.74 in study. Dropping "The human was the most important member" raises α to 0.84 | [V]; individual item wording not extracted [U] |
| Validity study design | MTurk; 143 recruited, 104 analysed; each viewed 5 of 50 simulated clips (~40 s); paid $0.10 | [V] |
| Results | Pearson with composite: R-IDLE r(495)=−0.074 n.s.; H-IDLE r=0.119 p<.01 (positive, "surprisingly"); C-ACT r=0.047 n.s.; F-DEL r=−0.123 p<.01. Tercile analysis: very high R-IDLE and very low C-ACT reduce perceived fluency (non-linear); robot personality traits not correlated with objective metrics | [V] |
| Measurement caveat | Simulations show an initial "ringing" period and late perturbations under timing variance. With few turns, evaluate per turn rather than over total task time | [V] |
| MAD-TN | Isaacson, Rice, Boerkoel, "MAD-TN: A Tool for Measuring Fluency in Human-Robot Collaboration," AI-HRI 2019, arXiv 1909.06675. Multi-Agent Daisy Temporal Network models the task and computes Hoffman's metrics. Adds **concurrent inactivity** and **resource delay**, which it *hypothesizes* correlate with perceived fluency (no human data in that paper) | [V] abstract; [V] metric definitions via ar5iv snippet |
| MAD-TN follow-up | Weiss, Jacotin, Jackson, Yuan, Boerkoel, "Analyzing the Fluency of Human-Robot Interactions" (AAAI copyright 2023; exact venue not stated in PDF). MTurk viewers of real human+Sawyer videos, ~49–53 participants per metric set, Hoffman's 8 statements, Bayesian RM-ANOVA. Results: mostly BF<1 (evidence against) per statement. CON-ACT/CON-IDLE effect on team-fluency item BF=18.5. H-IDLE effect in the opposite direction from hypothesis. FUNC-DELAY and RESOURCE-DELAY weak/mixed | [V] (author-hosted PDF); venue [U] |

**Inference:** Hoffman's metrics are well-defined and widely used. Their criterion validity against human-perceived fluency is weak, non-linear and mostly third-person/video-based. No study we found validates them for live, speech-mediated, *interrupted* manipulation. This is the defensible core of G4.

## 3. Other evidence linking objective interaction metrics to subjective ratings

| Source | Setting / n | Objective ↔ subjective finding | Status |
|---|---|---|---|
| Skantze & Irfan, "Applying General Turn-taking Models to Conversational HRI," HRI 2025, arXiv 2501.08946 | Furhat; n=39 native English speakers; 2(order)×2(scenario) within-subject; 2×7 min; 1.5 h/participant | Median response 1.5 vs 2.7 s (W=776, p<.001); interruption rate 6.9% vs 16.6%. Ratings: fluid (p=.014), human-like, fewer interruptions, interruptible, less effort. But "slow to respond" n.s. (p=1.0). Preference: 9/39 baseline, 3 no preference (→ 27/39 proposed, derived by us). Interruptions were **annotated by participants themselves** via audio playback ("did not let them speak"). G*Power: f=0.25, power .80 → 34; recruited 39 (power .86). Ethics: "reviewed and endorsed by the university's research ethics and data officers" | [V] (arXiv full text) |
| Shiwa et al., "How quickly should communication robots respond?" HRI 2008 (journal version JRSJ 27(1), DOI 10.7210/jrsj.27.87) | Communication robot | Preference highest at 1 s response time, levels off at 2 s; conversational fillers moderate the impression of long delays | [V] abstract (J-STAGE); ACM version blocked |
| Song, Zi, Guanting, arXiv 2607.00530 (2026-07-01) | Dobot Magician + Whisper/LLM/VLM; n=24; within-subject; 2 runs per system; ~30 min | Preference 17/24 (p=.043, h=0.43); speed d_z=1.85, reliability 1.54, competence/fluency 2.03 (Holm p<.001). Analysis plan named Wilcoxon as default but paired t-tests were reported after Shapiro–Wilk. Calls hypotheses "pre-registered" without a visible registry link. No in-session objective logging reported | [V] full text; preregistration [U]; ethics approval not seen [U] |
| Zhou et al., "Mind the Sim2Real Gap in User Simulation for Agentic Tasks," COLM 2026, arXiv 2603.11245 | τ-bench; 451 Prolific participants, 165 tasks; 31 simulators | On task-success judgments: human–human agreement 95.6% vs human–LLM 29.7–81.1%. Best simulator USI 76.0 vs human 92.7. GPT-5.1 overestimates human-likeness by 55% and overall score by 18% of scale. Binary reward orthogonal to perceived quality | [V] |
| TurnNat, arXiv 2607.01345 (2026-07) | 150 natural/perturbed pairs × 3 annotators | Humans preferred the natural clip in 70.0% of judgments (78.0% majority). Automatic score reached 88.0% pair accuracy. Validates *detectability of gross timing perturbations*, not correlation with ratings of real systems | [V] |
| French Full-Duplex-Bench, arXiv 2609.10765 (2026-09) | Human–human vs model dialogues | Human–human conversations "do not always yield optimal FDB scores"; authors report a trade-off between optimizing benchmark metrics and naturalness. No human raters | [V] |
| Conversational Distribution Score, arXiv 2609.31719 (2026-09; KTH et al.) | 374 conversations, 56 callers; 1,026 pairwise listener votes | Composite CDS ρ=0.222–0.266 with listener preference; a single feature (syllable duration) ρ up to 0.615. ≤1-min excerpts fail to reproduce system rankings | [V] |
| Synthetic TLX, arXiv 2609.12273 (2026-09; CMU/Google DeepMind) | 3 tasks; agent vs human NASA-TLX | Best prompting (human persona + active simulation): r=0.648/0.679/0.834 over 54 aggregated points per task. Agents *reverse* human ordering of intrinsic vs extraneous load in 2 of 3 tasks | [V]; human sample 162 = 54 per task, 18 per group [V, per verifier quote] |

## 4. Questionnaires: what they measure and fit for our study

| Instrument | Primary source | Fit / caveat | Status |
|---|---|---|---|
| **PMQ** = Partner Modelling Questionnaire | Doyle et al., ACM TOCHI 2025, DOI 10.1145/3729170; arXiv 2308.07164 | 18-item semantic differential; 3 factors (communicative competence & dependability; human-likeness in communication; communicative flexibility); good test-retest. Validated for **non-embodied speech interfaces** → embodied-arm use is an extrapolation | [V] abstract |
| Hoffman fluency scales | Hoffman 2019 (above) | Directly targets fluency; use the 8-item composite minus the weak item | [V] |
| Almere model | Heerink, Kröse, Evers, Wielinga, *Int J Soc Robotics* 2:361–375, 2010, DOI 10.1007/s12369-010-0068-5 | UTAUT extension for **older adults' acceptance of assistive social agents**. Long and acceptance/intention-oriented → poor fit for a 60-min lab study of interruption handling; skip or use 1–2 constructs | [V] (Springer abstract/metadata) |
| SUS | Brooke 1996 (original not retrieved) | 10-item usability; system-level, not episode-level | [U] original reference not verified by tool |
| NASA-TLX | Hart & Staveland 1988 (original not retrieved) | Workload; Synthetic TLX reports 522 CHI papers 2006–2024 using it, ~10% of CHI 2024 | usage stat [V] via 2609.12273; original [U] |
| Trust | Schaefer, "The Perception and Measurement of Human-robot Trust" (2013, UCF doctoral dissertation; UCF STARS ETD 2688; OpenAlex record mislabels it as a journal article) | Trust Perception Scale-HRI; item counts not verified here | [V] metadata only; content [U] |

## 5. Sample sizes and designs in the field

- Baxter et al. (alt.HRI 2016) analysed 101 HRI full papers from 2013–2015. Per their histogram, "the majority of conditions have fewer than 20 subjects". WoZ appeared in 25 papers (12%/35%/28% by year); the text says 26. [V] (author-hosted PDF)
- Leichtmann, Nitsch & Mara (Frontiers Robotics & AI 2022) review 8 HRI meta-analyses. Reported sample sizes include mean 46.5 (Mdn 29), Mdn 37, mean 27.7 (Mdn 22), and Mdn 21. They infer many HRI studies are underpowered. [V]
- Adjacent prior art (carried over from 04-literature-map.md; not re-verified in this run): SocialVLA n=15, CMU HRI 2026 n=18, MICoBot 18, ExpressMM 23, Song et al. 24 (new), RIAP N=30, Skantze & Irfan 39. Within-subject designs dominate for system comparisons.
- Bartlett et al., "Have I Got the Power? Analysing and Reporting Statistical Power in HRI" (ACM THRI, DOI 10.1145/3495246). Full text **blocked** (ACM 406); only the search snippet was seen. [S]

## 6. Wizard-of-Oz and simulated-user protocols

- **WoZ:** Riek, "Wizard of Oz Studies in HRI: A Systematic Review and New Reporting Guidelines," JHRI 1(1):119–136, 2012, DOI 10.5898/JHRI.1.1.Riek. [V metadata; content not read → guideline details U]
  - Baxter et al. note that 5 of 26 WoZ papers never use the word "wizard". [V]
  - *Recommendation (inference):* use WoZ only as an "oracle repair" upper-bound condition with a scripted wizard, reported per Riek's guidelines.
- **EchoChain** (arXiv 2604.16456):
  - Simulated users: planner GPT-5.2 + user simulator Gemini 3 Pro; speech pre-synthesised with MiniMax voice cloning from recorded voice actors.
  - Barge-in injected at a fixed offset from assistant speech onset.
  - Validation covers voice realism only: 80 pairs × 3 ratings → 97 cloned / 92 human / 51 neutral, χ²=0.92, p=0.63. [V]
- **PACT** (arXiv 2605.24350):
  - Simulated humans follow the COOPERA protocol (Habitat 3.0, Llama-3.1-8B behaviour generator, Big-Five profiles).
  - Reported validation: real users identify the same simulated human (0.764) and match traits (0.712); SBERT alignment with real routines 0.810.
  - PACT itself has no real-human evaluation.
  - Clarification Utility U = Acc/(1+AskRate). [V]
- **How well simulated users predict real users:** best direct evidence is Zhou et al. 2026 (§3). Simulators make tasks easier and ratings rosier. The paper reports that the *ordering of user simulators* (by USI) is largely preserved when the agent under test is swapped (5 simulators checked). That is **not** evidence that simulators preserve the ranking of the systems or conditions under test. [V]
  - Synthetic TLX shows high correlation for aggregated workload but wrong ordering of load sources. [V]
  - **Inference / hypothesis to test:** simulated users may rank conditions at scale, but no source we found shows that simulated and human condition rankings agree in HRI. Treat agreement as an empirical question to measure on a human subset. Never report simulated ratings as user perception.

## 7. Ethics / IRB in Europe (for naive adult participants, voice recording)

- **DFG (Germany):** for social sciences/humanities/engineering, an ethics statement is generally required only if patients or human material are involved. It "may be necessary" for vulnerable groups, strong emotional stress, physical risk/pain, non-disclosure or deception, or particular risks. [V]
  - Inference: an SO-101 study with healthy adults and full disclosure may not be *DFG-mandated*. Most universities and IROS reviewers still expect an ethics approval statement.
- **Timelines (official pages):**
  - LMU Munich CS ethics committee: regular ~6–8 weeks, fast-track ~2–4 weeks, assuming no revisions. [V]
  - ETH Zurich: submit ≥2 months before recruitment; 3–6 weeks to first decision + 2–3 weeks if revisions. Platform switch closes submissions 22 Nov–1 Dec 2026; holiday closure until 4 Jan 2027. [V]
  - WU Vienna: board meets ~monthly, up to 4 weeks. [S snippet]
  - TU Chemnitz: next board meeting 19.10.2026. [S snippet]
- **GDPR / voice:** EDPB Guidelines 02/2021 (para. 31): "voice data is inherently biometric personal data". It becomes Art. 9 special-category data when processed to uniquely identify a person, which then needs an Art. 9 derogation (e.g., explicit consent, para. 128). [V]
  - Inference: recording participants' speech is personal data (consent, DPIA-lite, retention plan). **Cloning participants' voices** for simulated users creates a reusable voice model. Use consenting voice actors (as EchoChain did) or explicit, separate consent.
- **Projected timeline for IROS (deadline 1 Mar 2027):** with 6–8 weeks plus one revision round, a mid-November 2026 submission → approval ~early/mid-January 2027 → data collection mid-Jan to mid-Feb. Very tight. Fast-track or an existing umbrella approval is the critical path. (inference)

## 8. Recommended study design (n≈18–39)

**Claim to target (refined G4):**
- **Claim:** trial-level physical-repair metrics from our benchmark predict participants' per-episode fluency and responsiveness ratings for *spoken mid-motion corrections* on SO-101, beyond what condition labels explain.
- **Agreement check:** report whether simulated-user rankings agree with human rankings.
- **Not to claim:** "first user study with speech on a low-cost arm" (Song et al. 2607.00530), "first interruption user study" (05-gap-analysis), or "first full-duplex physical preemption" (VITA-E per 04-literature-map.md; MIRA 2609.24547).

**Design:**
- **Participants:** target N=24 (balanced Latin square for 4 conditions), minimum 18, stretch 39.
- **Conditions:** stop-and-replan / retract-and-restart / wait-for-boundary / mid-motion repair. Optional WoZ oracle as a 5th condition only if session time allows.
- **Episodes:** ≥8 interruption episodes per condition, mixing interruption types (target change, constraint, cancel, backchannel-should-not-interrupt, self-correction). Session ≤75 min.
- **Per-episode micro-rating:** 1–2 items, 7-pt, immediately after each episode (e.g., "The robot handled my correction smoothly"; "The robot reacted in time").
- **Post-session interruption annotation:** participants mark moments when the robot "ignored or overrode" them, following the Skantze & Irfan playback protocol.
- **Per-condition questionnaires:** Hoffman 8-item fluency composite (minus weak item), raw NASA-TLX, short trust scale. SUS once per condition only if time allows. PMQ once at end (exploratory; non-embodied caveat). Skip Almere.
- **Objective metrics logged per episode:**
  - Benchmark metrics (repair latency, residual motion, retraction penalty, trajectory continuity, post-repair success, false-barge-in).
  - Hoffman H-IDLE/R-IDLE/C-ACT/F-DEL computed **per episode**, as Hoffman recommends for few turns.
  - MAD-TN concurrent inactivity.
  - Speech timing (response gap, robot-overlap rate).
- **Analysis:**
  - Primary: linear mixed model `rating ~ metric + condition + (1|participant)` or repeated-measures correlation.
  - Report marginal R² gain of benchmark metrics over condition dummies.
  - Secondary: paired condition contrasts with Holm correction. Pre-register on OSF.
- **Simulated-vs-real check:** run the same condition × interruption set with voice-cloned TTS users (consented voice actors). Report Kendall τ between simulated and human condition rankings and ICC per metric.

**Power (computed, `experiments/g4-fluency-metrics-validity/power_results.txt`):**

| Analysis | N=18 | N=24 | N=39 |
|---|---|---|---|
| Paired t, min. detectable d_z (80%) | 0.70 | 0.60 | 0.46 |
| Between-participant r=0.3, power | 0.22 | 0.29 | 0.46 |
| Between-participant r=0.5, power | 0.57 | 0.71 | 0.91 |
| Trial-level rmcorr, 8 trials, within-r=0.2 (sim.) | 0.62 | 0.73 | 0.91 |
| Trial-level rmcorr, 8 trials, within-r=0.3 (sim.) | 0.93 | 0.98 | 1.00 |

Checks: paired n for d_z=0.5 = 34 (matches the G*Power value reported by Skantze & Irfan); r=0.3 → n=85 (textbook ≈84). The simulation assumes independent trials, random intercepts only, and no random slopes, so real power will be lower. Treat these values as optimistic upper bounds.

## 9. Risks

1. **Effect size risk:** Hoffman-type metric↔rating correlations may be tiny (r≈0.12) and non-linear. Mitigation: trial-level design, strong manipulation spread, threshold or tercile analysis.
2. **Perception ≠ timing:** perceived responsiveness may not track objective latency (Skantze & Irfan Q3). Report this honestly if it happens; it is itself a finding.
3. **Scoop:** Song et al. 2607.00530 already uses the "technical metrics → user perception, low-cost arm, speech" framing. CDS/TurnNat/Synthetic TLX are moving fast on metric validation for speech. Differentiation must be interruption + physical repair + trial-level validity.
4. **Simulated users inflate success and ratings** (Zhou et al.). Never substitute them for humans.
5. **Ethics timeline:** the holiday period and platform changes can add weeks. GDPR voice handling and voice cloning need explicit consent.
6. **Low-cost hardware noise:** SO-101 jitter or latency variance can confound metrics. Log hardware timing; pilot n=4–6.
7. **Order, novelty and demand effects** in within-subject designs: counterbalance, blind condition labels (as Song et al. did with "System A/B").

## 10. Items needing paywalled/blocked full text

- Hoffman & Breazeal 2007 IEEE T-RO (original metric definitions) — IEEE paywall; not fetched.
- Shiwa et al. HRI 2008 (ACM DL 406); JRSJ abstract read instead.
- Bartlett et al. ACM THRI "Have I Got the Power?" (ACM DL 406).
- Riek 2012 JHRI full guideline content (not fetched; ACM-hosted).
- Lasota & Shah 2015 Human Factors (PMC page JS-rendered; not read).
- CMU HRI 2026 bidirectional pHRI (carried over from 08).
- Hoffman 2019 IEEE Xplore version (read the author-hosted copy instead; pagination may differ).

## Sources
- Hoffman 2019 THMS — https://doi.org/10.1109/THMS.2019.2904558 ; author copy https://hrc2.io/assets/pdfs/papers/HoffmanTHMS19.pdf ; RSS'13 page http://guyhoffman.com/evaluating-fluency-in-human-robot-collaboration/
- MAD-TN — https://arxiv.org/abs/1909.06675
- Weiss et al. 2023 — https://rbjackson.github.io/paper_pdfs/weiss2023analyzing.pdf
- Skantze & Irfan HRI 2025 — https://arxiv.org/abs/2501.08946 ; https://doi.org/10.1109/HRI61500.2025.10973958
- Shiwa et al. — https://doi.org/10.1145/1349822.1349843 ; https://www.jstage.jst.go.jp/article/jrsj/27/1/27_1_87/_article/-char/en
- Song et al. 2026 — https://arxiv.org/abs/2607.00530
- Zhou et al. 2026 — https://arxiv.org/abs/2603.11245
- TurnNat — https://arxiv.org/abs/2607.01345
- French FDB — https://arxiv.org/abs/2609.10765
- CDS — https://arxiv.org/abs/2609.31719
- Synthetic TLX — https://arxiv.org/abs/2609.12273
- EchoChain — https://arxiv.org/abs/2604.16456
- PACT — https://arxiv.org/abs/2605.24350
- MIRA — https://arxiv.org/abs/2609.24547
- Kennington et al. benchmark proposal — https://arxiv.org/abs/2610.08733
- PMQ — https://arxiv.org/abs/2308.07164 ; https://doi.org/10.1145/3729170
- Almere — https://doi.org/10.1007/s12369-010-0068-5
- Baxter et al. 2016 — https://doi.org/10.1109/HRI.2016.7451777 ; https://james-kennedy.github.io/publications/BaxterEtAl2016AltHRI.pdf
- Leichtmann et al. 2022 — https://doi.org/10.3389/frobt.2022.838116
- Bartlett et al. 2022, ACM THRI 11(2) — https://doi.org/10.1145/3495246 (full text blocked; [S])
- Riek 2012 — https://doi.org/10.5898/JHRI.1.1.Riek
- Schaefer 2013 — https://stars.library.ucf.edu/etd/2688 (OpenAlex W2563047483)
- DFG FAQ — https://www.dfg.de/en/research-funding/proposal-funding-process/faq/ethics-committee-statements
- LMU CS ethics — https://ek.mathematik-informatik-statistik.lmu.de/
- ETH Zurich ethics — https://ethz.ch/en/research/ethics/ethics-commission/how-to-apply.html
- EDPB Guidelines 02/2021 — https://www.edpb.europa.eu/system/files/2021-07/edpb_guidelines_202102_on_vva_v2.0_adopted_en.pdf
