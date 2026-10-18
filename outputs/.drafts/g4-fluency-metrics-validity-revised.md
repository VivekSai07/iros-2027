# G4 — Do benchmark metrics predict human-perceived fluency in speech-driven HRC on low-cost arms? (literature review, 2026-10-18, revised)

> **Revision status (2026-10-18).** This version applies all verifier fixes (I1–I4, H1, H2, the Synthetic TLX flag upgrade) and all reviewer findings: FATAL W1, MAJOR W2–W11, and MINOR W12–W22. No new literature search was run for this revision. Two reviewer-run computations were reproduced in memory (see §8 and the provenance file). Items that remain unverified are listed in §10.

Status flags:
- **[V]**: verified from the primary page, abstract or full text, by the drafting run or the verification run.
- **[S]**: secondary only. This covers search snippets, citing papers, alphaXiv AI Q&A answers not cross-checked against the PDF, and carried-over project notes.
- **[U]**: unverified.

"Full text" means text retrieved through alphaXiv/arXiv or an author-hosted PDF.

## 1. Bottom line

1. **Hoffman's original validity study finds weak links between his objective fluency metrics and perceived fluency.**
   - Hoffman (2019) correlated the four metrics with an 8-item subjective fluency composite, and every correlation was small: |r| ≤ 0.123.
     - F-DEL had the strongest correlation, which was negative.
     - H-IDLE was *positively* correlated with perceived fluency.
     - R-IDLE and C-ACT were not significant.
   - The raters were online (MTurk) viewers of ~40 s simulated clips, not co-located participants.
   - The correlations are pooled over ~497 clip-level ratings (r(495)), so they are rating-level effects, not between-participant effects. [V]
2. **A follow-up on real-robot video (Weiss et al., 2023) mostly found evidence *against* per-metric effects.**
   - The main exception was concurrent activity/concurrent idleness, which had the strongest effect, on the "team fluency" item. A few other metrics got weak support.
   - Like Hoffman, it used video and MTurk raters; the robot was a Sawyer. [V]
3. **Live studies show that better task performance and timing do not automatically mean a better experience. The evidence for this is thin.**
   - **Speech HRI: Skantze & Irfan (HRI 2025, n=39, within-subject).**
     - Objective timing improved: median response time fell from 2.7 to 1.5 s, and the interruption rate fell from 16.6% to 6.9%.
     - Participants rated the system more fluid and preferred it.
     - The single item "The robot was slow to respond" did not reach significance after Bonferroni correction (adjusted p = 1.0). The medians were 2 vs 3, in the expected direction.
     - This is a single-item, single-study non-significant result, not evidence that the item showed no difference. [V]
   - **Physical HRC: Kille et al. (2025, n=26).**
     - Higher automation improved task accuracy but reduced flow and sense of agency. [S; reviewer read via alphaXiv]
4. **Closest scoop-risk paper (2026-07): Song et al. (arXiv 2607.00530).**
   - **Design:** within-subject, n=24, spoken commands, a low-cost **Dobot Magician** arm.
   - **Result:** participants detected and preferred the configuration that a *prior ablation* had found to be 15 pp more successful (75%→90%).
     - Preference was 17/24 (p=0.043).
     - d_z was 1.54–2.03 on the speed, reliability and fluency composites.
     - Success itself was not measured in the study sessions, and the two configurations may also differ in latency and other properties. [V]
   - **Limitation that leaves G4 open:** there is no trial-level or participant-level metric↔rating analysis, and no interruptions or mid-motion repair. [V]
   - **Consequence:** we can no longer claim "first study checking benchmark metrics against user perception on a low-cost arm with speech". G4 must be scoped narrower (see §8).
5. **Simulated users are useful for scale but are not validated substitutes for people.**
   - **Evidence (Zhou et al. 2026, τ-bench):** 451 real users were compared with 31 LLM simulators.
     - Simulators are over-cooperative and inflate agent success: 77.8% for the top simulators vs 63.6% for humans.
     - LLM-rated quality is inflated.
     - Binary task reward is "largely orthogonal" to human-perceived quality. [V]
   - **Scope:** this evidence comes from text-based agentic tasks and NASA-TLX workload (§3, §6). Carrying it over to embodied speech HRI is our inference.
   - EchoChain validates only voice realism; see §6.
6. **Feasibility for N≈20–40 depends on within-condition variance that is not yet known.**
   - **Between-participant correlations are underpowered at these sizes.** r=0.3 needs n=85; `power_results.txt`.
   - **The comparison with Hoffman's r≈0.12 should be made at the trial level.**
     - At N=24 with 32 episodes per participant, an *unconditional* repeated-measures correlation of r=0.12 has power ≈0.91 (analytic; reproduced, §8).
   - **The refined claim needs more than that.** It is "metrics predict ratings *beyond condition labels*", which is driven only by variance *within* conditions.
     - At N=24, 4 conditions × 8 episodes and r=0.2, power ranges from ≈0.97 down to ≈0.37. It falls as the share of metric variance explained by condition rises from 50% to 90% (§8).
   - **Conclusion:** the trial-level within-subject design is the most direct route. It is feasible **only if** the pilot shows substantial within-condition metric spread, and the design should create that spread deliberately (onset phase, injected latency).
   - **Optional complement:** a third-person video-rating arm (Hoffman/Weiss paradigm) can add statistical power. It measures *observer* perception, not participant experience.

## 2. Hoffman fluency metrics — primary sources

| Item | Finding | Status |
|---|---|---|
| Primary journal source | G. Hoffman, "Evaluating Fluency in Human–Robot Collaboration," *IEEE Trans. Human-Machine Systems* 49(3):209–218, 2019, DOI 10.1109/THMS.2019.2904558. Read via the author-hosted PDF (hrc2.io). The IEEE Xplore version is paywalled or closed-access per OpenAlex, and Xplore blocked the verifier (HTTP 202 bot challenge). Volume and pages confirmed via Crossref | [V] |
| Earlier version | Hoffman, RSS 2013 Workshop on Human-Robot Collaboration. The author page says "please refer to the new journal version"; the 2013 year comes from Hoffman 2019 ref. [9] | [V] (author page + citing ref) |
| Origin of 3 of the 4 metrics | Hoffman 2019 states that C-ACT, H-IDLE and F-DEL were proposed in Hoffman & Breazeal, "Cost-based anticipatory action-selection for human-robot fluency," IEEE T-RO 23(5):952–961, 2007. R-IDLE was added later | [V] as cited in Hoffman 2019; the T-RO paper itself was not read [U] |
| Definitions | **H-IDLE:** % of total task time the human is not active.<br>**R-IDLE:** % of time the robot is not *perceivably* active; authors may include or exclude time when the robot is internally active but seems idle.<br>**C-ACT:** % of time both agents are active.<br>**F-DEL:** accumulated time between one agent finishing and the other starting, as a ratio of task time; it can be negative when actions overlap and can exceed 1.<br>All four presuppose that **both agents act on a shared task** (see §8, W3) | [V] |
| Subjective fluency scale | Fig. 1 inventory: a 3-item direct fluency scale plus 6 downstream scales, including an adapted Working Alliance Inventory. The validity study used an 8-item composite on a 7-pt Likert scale, rated by third-person video viewers. α=0.81 in the pretest (n=21) and α=0.74 in the study. Dropping "The human was the most important member" raises α to 0.84 | [V]; wording of the individual items was not extracted [U] |
| Validity study design | MTurk; 143 recruited, 104 analysed; each viewed 5 of 50 simulated clips (~40 s); paid $0.10 | [V] |
| Results | Correlations with the composite:<br>• R-IDLE r(495)=−0.074, n.s.<br>• H-IDLE r=0.119, p<.01 (positive; the paper says "surprisingly")<br>• C-ACT r=0.047, n.s.<br>• F-DEL r=−0.123, p<.01<br>Tercile analysis: very high R-IDLE and very low C-ACT reduce perceived fluency, so the relation is non-linear. The robot's personality traits were not strongly correlated with the objective metrics | [V]; that the coefficient is "Pearson" was not checked [U] |
| Measurement caveat | Simulations show an initial "ringing" period and late perturbations under timing variance. With few turns, evaluate per turn rather than over total task time | [V] |
| MAD-TN | Isaacson, Rice, Boerkoel, "MAD-TN: A Tool for Measuring Fluency in Human-Robot Collaboration," AI-HRI 2019, arXiv 1909.06675. Its Multi-Agent Daisy Temporal Network models the task and computes Hoffman's metrics. It adds **concurrent inactivity** and **resource delay**, which it *hypothesizes* correlate with perceived fluency; that paper has no human data | [V] abstract; [V] metric definitions (the verifier checked them in the arXiv PDF) |
| MAD-TN follow-up | Weiss, Jacotin, Jackson, Yuan, Boerkoel, "Analyzing the Fluency of Human-Robot Interactions" (AAAI copyright 2023; the PDF does not state the venue).<br>**Design:** MTurk viewers of real videos of a human with a Sawyer robot; 49–53 participants per metric set; Bayesian repeated-measures ANOVA.<br>**Results:** per statement, mostly BF<1, i.e., evidence against an effect. CON-ACT/CON-IDLE effect on the team-fluency item: BF=18.5. The H-IDLE effect went in the opposite direction from the hypothesis. FUNC-DELAY and RESOURCE-DELAY: weak or mixed | [V] (author-hosted PDF). [U]: the venue, and whether raters used all of "Hoffman's 8 statements" (the verifier saw only F1, F2, F5 and F6) |

**Inference.** Hoffman's metrics are well-defined, but their criterion validity against human-perceived fluency is weak and non-linear. The only direct tests (Hoffman 2019; Weiss et al. 2023) are third-person and video-based.

Live, co-located HRC studies do collect both objective and subjective data:
- Kille et al. 2025 report one objective↔experience link: grip force ↔ sense of agency, r=0.20.
- RAPIDDS 2026 reports condition effects on both kinds of measure but does not link them.

No study we found validates objective metrics against ratings for live, speech-mediated, *interrupted* manipulation. That is the defensible core of G4.

**Search log (W7).** The original search pass did not record its exact queries; the plan's verification log was left empty. What is known:
- The plan named alpha_search, feynman_science_database_search (Semantic Scholar, OpenAlex, arXiv), and the web for ethics pages.
- The reviewer then ran one alphaXiv query, "objective fluency metrics ↔ subjective fluency ratings in HRC", on 2026-10-18. It surfaced Kille et al. and RAPIDDS.
- The reviewer also checked SocialVLA, MICoBot and ExpressMM full texts via alphaXiv. None relates metrics to ratings.

The gap statement is therefore scoped to "no study we found". The search was not systematic; see §10.

## 3. Other evidence linking objective interaction metrics to subjective ratings

| Source | Setting / n | Objective ↔ subjective finding | Status |
|---|---|---|---|
| Skantze & Irfan, "Applying General Turn-taking Models to Conversational HRI," HRI 2025 (pp. 859–868), arXiv 2501.08946 | Furhat robot; n=39 native English speakers; 2 (order) × 2 (scenario) within-subject; 2 × 7 min of interaction; 1.5 h per participant | **Timing:** median response 1.5 vs 2.7 s (W=776, p<.001); interruption rate 6.9% vs 16.6%.<br>**Ratings:** the proposed system was rated more fluid (p=.014), more human-like, as interrupting less, as more interruptible, and as needing less effort. "Slow to respond": medians 2 (2–3) vs 3 (2–4), Bonferroni-adjusted p=1.0.<br>**Preference:** 9/39 preferred the baseline and 3 had no preference, so 27/39 preferred the proposed system (we derived the 27; the paper does not state it).<br>**Interruption annotation:** participants **annotated interruptions themselves** via audio playback ("did not let them speak").<br>**Sample size:** G*Power with f=0.25 → 34; 39 recruited (power .86).<br>**Ethics:** "reviewed and endorsed by the university's research ethics and data officers" | [V] (arXiv full text; venue via Crossref) |
| Kille et al., "Beyond Task Performance: Human Experience in Human-Robot Collaboration," arXiv 2505.04182 (2025) | Co-located physical HRC (drilling task, LBR arm); n=26 analysed; within-subject, 4 automation levels | Higher automation raised task accuracy but lowered flow and sense of agency (inverted-U pattern). Ranked grip force ↔ sense of agency: r=0.20, p=.045. HRV-based flow classification reached only 61% accuracy | [S] (reviewer, alphaXiv full-text Q&A; numbers not cross-checked against the PDF) |
| Cuellar, Hagenow, Shah, "Multi-Cycle Spatio-Temporal Adaptation in Human-Robot Teaming" (RAPIDDS), arXiv 2604.19670 (2026) | n=32; 4 systems; Latin square; 7-DoF arm | Objective spatial and temporal costs plus a Hoffman-style fluency survey per system. Effects are reported per condition (ART ANOVA); **no metric↔rating link**. Design precedent for N=32 with 4 conditions | [S] (reviewer, alphaXiv full-text Q&A) |
| Shiwa et al., "How quickly should communication robots respond?" HRI 2008 (journal version JRSJ 27(1):87–95, 2009, DOI 10.7210/jrsj.27.87) | Communication robot | Preference highest at a 1 s response time and levels off at 2 s; conversational fillers moderate the impression of long delays | [V] abstract (J-STAGE); ACM version blocked |
| Song, Zi, Guanting, arXiv 2607.00530 (2026-07-01) | Dobot Magician + Whisper/LLM/VLM; n=24; within-subject; 2 runs per system; ~30 min; systems blinded as "System A/B" | **Results:** preference 17/24 (p=.043, h=0.43). d_z: speed 1.85, reliability 1.54, competence/fluency 2.03 (Holm p<.001).<br>**Analysis deviation:** the plan named Wilcoxon as the default test, but paired t-tests were reported after Shapiro–Wilk.<br>**Other:** the hypotheses are called "pre-registered" with no visible registry link, and no in-session objective logging is reported | [V] full text; preregistration [U]; ethics approval not seen [U] |
| Zhou et al., "Mind the Sim2Real Gap in User Simulation for Agentic Tasks," COLM 2026, arXiv 2603.11245 | τ-bench (text agents); 451 Prolific participants; 165 tasks; 31 simulators | **Task-success judgments:** human–human agreement 95.6% vs human–LLM 29.7–81.1%.<br>**Realism (USI):** best simulator 76.0 vs 92.7 for human inter-annotator.<br>**Rating bias:** GPT-5.1 overestimates human-likeness by 55% and the overall score by 18% of the scale.<br>**Task reward:** binary reward is "largely orthogonal" to perceived quality | [V] |
| TurnNat, arXiv 2607.01345 (2026-07) | 150 natural/perturbed pairs × 3 annotators | Humans preferred the natural clip in 70.0% of judgments (78.0% by majority vote). The automatic score reached 88.0% pair accuracy on a 1,000-pair automatic benchmark. This validates *detectability of gross timing perturbations*, not correlation with ratings of real systems | [V] |
| French Full-Duplex-Bench, arXiv 2609.10765 (2026-09) | Human–human vs model dialogues | Human–human conversations "do not always yield optimal FDB scores". The authors report a trade-off between optimizing benchmark metrics and preserving naturalness. Response quality is judged by an LLM (llama3.3:70b); there are no human raters | [V] |
| Conversational Distribution Score (CDS), arXiv 2609.31719 (2026-09) | 374 conversations, 56 callers; 1,026 pairwise listener votes | The composite CDS correlates with listener preference at ρ=0.222–0.266. A single feature (Sylber syllable duration) reaches ρ=0.615. Excerpts of one minute or less fail to reproduce system rankings | [V]; author affiliation not checked [U] |
| Synthetic TLX, arXiv 2609.12273 (2026-09) | 3 tasks; NASA-TLX from agents vs humans; human sample 162 = 54 per task = 18 per group | **Correlation:** best prompting (human persona + active simulation) gives r=0.648/0.679/0.834 over 54 paired data points per task.<br>**Ordering:** agents *reverse* the human ordering of intrinsic vs extraneous load in 2 of 3 tasks (email, website); the human difference for email was only marginal | [V] (paper: "162 participants, with 54 participants per task, and 18 participants per group") |

## 4. Questionnaires: what they measure and fit for our study

| Instrument | Primary source | Fit / caveat | Status |
|---|---|---|---|
| **PMQ** (Partner Modelling Questionnaire) | Doyle et al., ACM TOCHI 32(4), 2025, DOI 10.1145/3729170; arXiv 2308.07164 | 18-item semantic differential with 3 factors: communicative competence & dependability; human-likeness in communication; communicative flexibility. Good test-retest reliability. Validated for **non-embodied speech interfaces**. ExpressMM used adapted PMQ items with a TurtleBot-4 + SO-101 platform, so embodied use has a precedent, but it remains an extrapolation from the validation sample | [V] abstract; ExpressMM precedent [S] (reviewer) |
| Hoffman fluency scales | Hoffman 2019 (above) | Directly targets fluency. Recommended: the **7-item** composite (the 8 items minus "The human was the most important member"), given per condition. The composite was validated with third-person video viewers, so rewording for first-person, co-located use is an adaptation that must be reported | [V]; item wording [U] |
| Almere model | Heerink, Kröse, Evers, Wielinga, *Int J Soc Robotics* 2(4):361–375, 2010, DOI 10.1007/s12369-010-0068-5 | UTAUT extension for **older adults' acceptance of assistive social agents**. It targets acceptance and intention, not episode-level fluency. ExpressMM used adapted Almere items on SO-101. We diverge because our target construct is interaction fluency under interruption, not technology acceptance. We have not verified its length | [V] (metadata/DOI only); ExpressMM use [S] |
| SUS | Brooke 1996 (original not retrieved) | 10-item usability scale; measures the system level, not individual episodes | [U] original reference not verified by tool |
| NASA-TLX | Hart & Staveland 1988 (original not retrieved) | Workload. Synthetic TLX reports 522 CHI papers using it in 2006–2024, nearly 10% of CHI 2024 papers | usage stat [V] via 2609.12273; original [U] |
| Trust | Schaefer, "The Perception and Measurement of Human-robot Trust" (2013, UCF doctoral dissertation; UCF STARS ETD 2688. The OpenAlex record W2563047483 mislabels it as a journal article) | Trust Perception Scale-HRI; item counts not verified here | [V] metadata only; content [U] |

## 5. Sample sizes and designs in the field

- **Baxter et al. (alt.HRI 2016):** analysed 101 HRI full papers from 2013–2015. [V] (author-hosted PDF)
  - Per their Fig. 3, "the majority of conditions have fewer than 20 subjects".
  - WoZ appears in 25 papers per their Table I (12%/35%/28% by year); the text says 26.
- **Leichtmann, Nitsch & Mara (Frontiers Robotics & AI 2022):** review 8 HRI meta-analyses. [V]
  - Reported sample sizes include mean 46.5 (Mdn 29), Mdn 37, mean 27.7 (Mdn 22), and Mdn 21.
  - They infer that many HRI studies are underpowered.
- **Bartlett et al. (2022):** "Have I Got the Power? Analysing and Reporting Statistical Power in HRI," ACM THRI 11(2):1–16, DOI 10.1145/3495246. Metadata confirmed via Crossref. The full text is **blocked** (ACM DL returned 403 in the verification run). [S]
- **Adjacent prior art.** The n values below are not comparable "user studies". We draw no generalisation about design norms from them.

| Study | n | Study type / conditions | Ratings | Metric↔rating analysis | Status |
|---|---|---|---|---|---|
| SocialVLA (2610.02360) | 15 + 1 | Annotated reaction corpus plus 1 prospective participant; Unitree G1 | None (no questionnaires) | No | [S] (reviewer, alphaXiv) |
| MICoBot (2508.05535) | 18 (6 per task × 3 tasks) | 2 systems; TIAGo; sequential turn-taking | 5-pt Likert, preference | No (condition-level Wilcoxon) | [S] (reviewer) |
| ExpressMM (2604.05320) | 23 | Classroom audience watching one researcher; single condition; TurtleBot-4 + SO-101 | Adapted Almere + PMQ | No (descriptive) | [S] (reviewer) |
| Kille et al. (2505.04182) | 26 analysed | Within-subject, 4 automation levels, physical HRC | Flow, SoA, embodiment, satisfaction | Partial (grip force ↔ SoA) | [S] (reviewer) |
| RAPIDDS (2604.19670) | 32 | 4 systems, Latin square | Fluency survey + ranking | No | [S] (reviewer) |
| Song et al. (2607.00530) | 24 | Within-subject, 2 systems | Composites + preference | No | [V] |
| Skantze & Irfan (2501.08946) | 39 | Within-subject, 2 systems, speech only | Questionnaire + preference | No (condition-level) | [V] |
| CMU HRI 2026 (bidirectional pHRI) | 18 | Older adults | Not checked | Not checked | [S] (carried over from 04/05; unchecked) |
| RIAP (NeurIPS 2026 listing) | 30 | Human study; details beyond the abstract unknown | Not checked | Not checked | [S] (carried over from 04; no preprint) |

## 6. Wizard-of-Oz and simulated-user protocols

- **WoZ.**
  - Riek, "Wizard of Oz Studies in HRI: A Systematic Review and New Reporting Guidelines," JHRI 1(1):119–136, 2012, DOI 10.5898/JHRI.1.1.Riek. [V metadata; content not read, so the guideline details are U]
  - Baxter et al. note that 5 of 26 WoZ papers never use the word "wizard". [V]
  - *Recommendation (inference):* a WoZ "oracle repair" upper bound is deferred beyond the IROS study because of session time (§8). If it is used later, it should follow Riek's reporting guidelines.
- **EchoChain** (arXiv 2604.16456):
  - **Simulated users:** the dialogue planner is GPT-5.2 and the user simulator is Gemini 3 Pro. Speech is pre-synthesised with MiniMax voice cloning from a pool of recorded voice actors.
  - **Barge-in:** injected at a fixed offset from the onset of the assistant's speech.
  - **Validation covers voice realism only, not simulated-user behaviour:** 240 judgments over 80 pairs → 97 favoured the cloned sample, 92 the human sample, 51 neutral; χ²=0.92, p=0.63. [V]
- **PACT** (arXiv 2605.24350):
  - **Simulated humans:** follow the COOPERA protocol (Habitat 3.0, a Llama-3.1-8B behaviour generator, Big-Five profiles).
  - **Reported validation**, from the earlier COOPERA study: real users identify the same simulated human (0.764) and match its traits (0.712). SBERT alignment with real routines is 0.810. [V]
  - *Inference:* PACT itself reports no real-human evaluation. The paper does not state this, and nothing in it contradicts it.
- **How well simulated users predict real users.**
  - **Zhou et al. 2026 (§3)** is the best direct evidence. Simulators make tasks easier and ratings rosier. [V]
    - The paper reports that the *ordering of user simulators* (by USI) is largely preserved when the agent under test is swapped (5 simulators checked).
    - That is **not** evidence that simulators preserve the ranking of the systems or conditions under test.
  - **Synthetic TLX** shows a high correlation for aggregated workload but the wrong ordering of load sources. [V]
  - **Inference / hypothesis to test:** no source we found shows that simulated and human condition rankings agree in HRI.
    - Simulated users should be used only as a source of *speech input*.
    - Never report simulated "ratings" as user perception. §8 defines an agreement check on objective metrics.

## 7. Ethics / IRB in Europe (for naive adult participants, voice recording)

- **The team's ethics committee is unknown** (`08-open-questions-and-access-needs.md`, Q8 open). LMU and ETH below are examples of published timelines, not the team's route.
- **DFG (Germany).**
  - For social sciences, humanities and engineering, an ethics statement is generally required only if patients or human material are involved. [V]
  - It "may be necessary" for vulnerable groups, strong emotional stress, physical risk or pain, non-disclosure or deception, or particular risks. [V]
  - *Inference:* an SO-101 study with healthy adults and full disclosure may not be *DFG-mandated*. An ethics approval statement is still commonly expected by universities and robotics venues. We did not check an IROS 2027 human-subjects policy [U].
- **Published timelines** (official pages):
  - **LMU Munich CS ethics committee:** regular ~6–8 weeks, fast-track ~2–4 weeks. Both figures are explicitly calculated **assuming no queries or revisions**. [V]
  - **ETH Zurich:**
    - Submit at least 2 months before the planned start. [V]
    - 3–6 weeks to the first decision, plus 2–3 weeks if revisions are needed. [V]
    - The current platform (eResearch) closes 22 Nov 2026; the new platform opens 1 Dec 2026. [V]
    - It is closed over the holidays and reopens 4 Jan 2027; the start of the closure is not stated. [V]
- **GDPR / voice.**
  - EDPB Guidelines 02/2021, para. 31: "voice data is inherently biometric personal data". [V]
  - It becomes Art. 9 special-category data when processed to uniquely identify a person. That processing then needs an Art. 9 derogation, e.g., explicit consent (para. 128). [V]
  - *Inference:*
    - Recording participants' speech is personal-data processing. It needs consent, a DPIA screening under Art. 35 GDPR, and a retention plan.
    - Cloning participants' voices creates a reusable voice model. Use consenting voice actors (as EchoChain did), or obtain explicit, separate consent.
- **Projected timeline for IROS (deadline 1 Mar 2027; experiments frozen mid-Feb per `02-iros-2027-constraints.md`).** This is our inference. It assumes submission ~16 Nov 2026, before ETH's 22 Nov platform closure, and the team still has to confirm its own committee's rules.

| Scenario | Assumptions | Approval ≈ | Data-collection window before mid-Feb freeze |
|---|---|---|---|
| Best | Fast-track (LMU 2–4 wk), no revisions | 30 Nov–14 Dec 2026; recruiting realistically starts after the holidays (~4–11 Jan) | ~5–6 weeks |
| Likely | Regular review (LMU 6–8 wk), no revisions; holiday closure | 28 Dec 2026–11 Jan 2027, effectively ~mid-Jan | ~4 weeks |
| Worst (still within IROS) | Regular review + one revision round (+2–3 wk, ETH figure) + holidays | ~11 Jan–1 Feb 2027, later if the holiday closure pauses review | ~2–4 weeks, which is not enough for N=24 sessions of ~90 min plus analysis |

- **Gates (all must hold):**
  1. Protocol frozen by ~mid-Nov 2026. This includes the G1 metric definitions, the primary predictor and criterion (§8), and the consent and data-management texts.
  2. The ethics submission goes in ~mid-Nov 2026.
  3. The G2 mid-motion repair condition runs reliably on real SO-101 hardware by ~mid-Jan 2027.
  4. Pilot (n=4–6) completed in the first approved week.
- **Fallback:** if approval lands after ~1 Feb 2027 or the G2 gate fails, the IROS paper reports the benchmark plus a pilot only. The human-validity component moves to the ICRA 2028 version, consistent with `05-gap-analysis.md` ("pivot to ICRA 2028 with the user-study-heavy version").

## 8. Recommended study design (N = 20 / 24 / 40)

**Claim to target (refined G4).**
- **Primary:** a pre-specified trial-level physical-repair metric from our benchmark predicts participants' per-episode fluency ratings for *spoken mid-motion corrections* on SO-101, **beyond what condition labels explain**.
- **Secondary:** the other benchmark metrics, Hoffman metrics, and questionnaires (FDR-controlled or exploratory).
- **Agreement check:** objective metrics measured with TTS-simulated speakers vs human speakers in matched cells.

**Implications for `06-paper-story.md` (W10).**
- The current C3 ("correlation of benchmark metrics with Hoffman fluency metrics and PMQ/SUS") is inconsistent with this claim:
  - Benchmark ↔ Hoffman *objective* metrics is objective↔objective, not validity against perception.
  - PMQ and SUS are once-per-condition or once-per-session measures, so they cannot carry a trial-level claim.
- **Proposed C3:** "trial-level benchmark metrics predict per-episode human fluency ratings beyond condition (primary); Hoffman metrics and PMQ/SUS secondary/exploratory."
- This review does not edit 06. The change needs a decision-log entry.

**Not to claim** (consolidated from `05-gap-analysis.md` and this review):

| Do not claim | Prior work | Source |
|---|---|---|
| "First user study with speech on a low-cost arm" | Song et al. 2607.00530 | this review |
| "First interruption user study" | SocialVLA, CMU HRI 2026, MICoBot, ExpressMM, Skantze & Irfan | 05 |
| "First full-duplex physical preemption" | VITA-E, MIRA 2609.24547 | 04 |
| Timing/commit as a decision variable | RIAP, Premover | 05 |
| "Speech barge-in stops a robot" | ELLSA (sim), VITA-E (real humanoid) | 05 |
| "Acting on partial speech" | Premover, Tufts/TUW | 05 |
| First timing-controlled switch evaluation in manipulation | Causeway, LIBERO-MAX, MAIL-Bench | 05 |
| First manipulation interruption metrics | ARMS | 05 |
| First false-stop + latency with users | SocialVLA | 05 |
| First SO-101 failure taxonomy | Yu & Qiu 2606.08881 | 05 |

The SocialVLA entry matters here because our metrics include false-barge-in and latency.

**Participants.**
- Target N=24, minimum 20, stretch 40. These are multiples of 4, so a balanced 4×4 Latin square stays balanced.
- For comparison, RAPIDDS used N=32 with 4 systems in a Latin square [S].

**Conditions.**
- The four conditions are stop-and-replan, retract-and-restart, wait-for-boundary, and mid-motion repair.
- The WoZ oracle condition is **dropped for IROS** because of the session-time budget.

**Episodes and within-condition variance (W1).**
- **Count:** k = 8 correction episodes per condition (32 per participant). The fallback is k = 4 per condition (16 per participant) if the pilot shows the session is too long.
- **Built-in variation:** within each condition, vary **interruption onset phase** (e.g., early, mid or late in the reach) and, if feasible, **injected pipeline latency**. This creates the within-condition metric spread that the beyond-condition claim needs.
- **Interruption types:**
  - **Primary analysis:** correction types only (target change, constraint, self-correction).
  - **Secondary:** cancel and backchannel-should-not-interrupt episodes, each with type-specific items. For a backchannel episode, the item asks whether the robot correctly kept going; "post-repair success" is undefined for a cancel.

**Criterion measure (W4).**
- **Primary criterion:** a single per-episode 7-pt item, adapted from Hoffman's 3-item direct-fluency subscale and given immediately after each episode. Extracting the exact item wording from the Hoffman 2019 author PDF is an open task (§10).
- **"The robot reacted in time":** demoted to secondary. It resembles the Skantze & Irfan item that did not separate conditions.
- **Validity checks, pre-specified:**
  - **Convergent:** per-participant × condition mean micro-rating vs the per-condition 7-item Hoffman composite. The target r is to be fixed in the preregistration (TODO).
  - **Reliability:** within-person split-half reliability across repeated episodes.

**Objective metrics (W3, W5).**
- **Primary predictor, exactly one.** Recommended: **repair latency**, from the onset of the spoken correction to the first robot motion consistent with the corrected goal. Alternatively, a single G1 composite score, if G1 fixes one before the protocol freeze. *This choice is ours (inference); it is not taken from any source.*
- **Secondary, with Benjamini–Hochberg FDR:** residual motion, retraction penalty, trajectory continuity, post-repair success, false-barge-in, and speech timing (response gap, robot-overlap rate).
- **Exploratory:** Hoffman H-IDLE/R-IDLE/C-ACT/F-DEL and MAD-TN concurrent inactivity.
  - These metrics assume both agents act on a shared task. In a speech-supervised single-arm episode, "human active" is undefined. H-IDLE would collapse to roughly 1 − speech fraction, and C-ACT to the speech–motion overlap.
  - **If they are kept:** define human activity operationally as speaking, gesturing, or doing a concurrent physical subtask, and preferably add such a subtask (e.g., the human stages objects while the robot picks).
  - **Episode length:** episodes are seconds long, so Hoffman's "ringing" caveat applies. Report the metrics per episode and do not interpret them as task-level fluency.

**Questionnaires (W9).**
- **Per condition:** the 7-item Hoffman composite and raw NASA-TLX.
- **Once at the end of the session:** a short trust scale, PMQ (exploratory, given the non-embodied validation) and SUS (once, optional). Almere is skipped.

**Interruption annotation (W9).**
- Use in-episode button presses ("robot ignored or overrode me").
- If time allows, add playback annotation on a sampled subset of episodes, following the Skantze & Irfan protocol. Full playback is not budgeted.

**Session time budget (W9; pilot-measured, values TODO).**

| Component | Count | Per-unit time | Total |
|---|---|---|---|
| Consent, briefing, practice | 1 | TODO (pilot) | TODO |
| Episode incl. SO-101 scene reset + micro-rating | 32 (fallback 16) | TODO (pilot) | TODO |
| Per-condition questionnaires (7-item Hoffman + raw TLX) | 4 | TODO | TODO |
| End-of-session trust, PMQ, optional SUS | 1 | TODO | TODO |
| Breaks, debrief | — | TODO | TODO |

- **Precedents:** Skantze & Irfan needed 1.5 h for 2 × 7 min of interaction including annotation [V]. Song et al. needed ~30 min for 4 runs [V].
- **Decision rule:** if the pilot projects more than ~90 min, drop to k = 4 per condition before cutting conditions. Re-check power at that point (see the k/cond = 4 rows below).

**Analysis (W5).**
- **Primary model, one pre-specified:** `rating ~ primary_metric + condition + (1 + primary_metric | participant)`, two-sided α = .05.
  - The test is on the `primary_metric` coefficient.
  - Report the marginal R² gain over the condition-only model.
- **Sensitivity:** an ordinal cumulative-link mixed model (7-point ratings).
- **Secondary:** an unconditional repeated-measures correlation, which does not adjust for condition. It answers a different, weaker question and is reported as such.
- **Condition contrasts:** one planned contrast, mid-motion repair vs stop-and-replan, at α = .05. The other pairwise contrasts use Holm correction.
- **Pre-registration:** on OSF before the first participant.

**Simulated-vs-real agreement check (W8).**
- **Unit:** matched cells of condition × interruption type × onset phase (≈ 4 × 3 correction types × 3 phases).
- **Quantity:** the *objective* benchmark metrics measured when the same scripted corrections are spoken by consented-voice-actor TTS vs by human participants. Simulated users never produce ratings.
- **Statistic:** cell-level ICC or agreement correlation with bootstrap 95% CIs. The minimum agreement threshold is fixed in the preregistration (TODO).
- A Kendall τ over 4 condition rankings is **not** used. With only 24 possible orderings it is nearly uninformative.

**Optional complement (W11): third-person rating arm.**
- Recorded SO-101 episodes are rated online by many raters, as in the Hoffman/Weiss paradigm. This allows precise metric↔rating slopes, independent of in-lab session time.
- It measures observer perception, not participant experience.
- It needs separate ethics cover, and video of participants needs consent for that use.

**Power.**

Sources:
- (a) `experiments/g4-fluency-metrics-validity/power_results.txt`. The reviewer reproduced it exactly.
- (b) Analytic Fisher-z repeated-measures correlation and Holm-adjusted paired-t minimum detectable effects (MDE). The reviewer computed these, and I reproduced them in memory in this revision (provenance file).
- (c) The reviewer's "beyond condition" simulation (review Appendix A), reproduced in memory in this revision with seed 0 and 1000 simulations; the values shown are from my reproduction.

| Analysis | N=18 | N=24 | N=39 | Source |
|---|---|---|---|---|
| Paired t, min. detectable d_z (80%, α=.05, single planned contrast) | 0.70 | 0.60 | 0.46 | (a) |
| Paired t, min. detectable d_z (80%, Holm first step α=.05/6) | 0.92 | 0.77 | 0.58 | (b) |
| Between-participant r=0.3, power | 0.22 | 0.29 | 0.46 | (a) |
| Between-participant r=0.5, power | 0.57 | 0.71 | 0.91 | (a) |
| Unconditional rmcorr, **r=0.12** (Hoffman anchor), k=8 total | 0.27 | 0.34 | 0.51 | (b) |
| Unconditional rmcorr, r=0.12, k=16 total | 0.51 | 0.63 | 0.83 | (b) |
| Unconditional rmcorr, r=0.12, k=32 total | 0.81 | 0.91 | 0.99 | (b) |
| Unconditional rmcorr, within-r=0.2, k=8 (sim.) | 0.62 | 0.73 | 0.91 | (a) |
| Unconditional rmcorr, within-r=0.3, k=8 (sim.) | 0.93 | 0.98 | 1.00 | (a) |

The columns above are N = 18/24/39 because that is how `power.py` was run. The recommended N = 20/24/40 sit close to these values; the exact numbers for 20 and 40 were not computed.

**"Beyond condition" power (the primary estimand).** N=24, 4 conditions; source (c).
- "Share" is the fraction of metric variance between conditions; each cell gives power beyond condition / power unconditional.
- r is the total metric–rating correlation.

| Share | k/cond | r = 0.12 | r = 0.20 | r = 0.30 |
|---|---|---|---|---|
| 0.5 | 8 | 0.59 / 0.92 | 0.97 / 1.00 | 1.00 / 1.00 |
| 0.8 | 8 | 0.30 / 0.92 | 0.66 / 1.00 | 0.96 / 1.00 |
| 0.9 | 8 | 0.16 / 0.91 | 0.37 / 1.00 | 0.73 / 1.00 |
| 0.5 | 4 | 0.24 / 0.62 | 0.68 / 0.97 | 0.96 / 1.00 |
| 0.8 | 4 | 0.17 / 0.65 | 0.35 / 0.97 | 0.68 / 1.00 |
| 0.9 | 4 | 0.11 / 0.66 | 0.19 / 0.98 | 0.41 / 1.00 |

**Reading the power results.**
- **Effect-size anchor.** The only direct prior estimate is r≈0.12 (Hoffman, rating-level, third-person video). No source supports r=0.2–0.3 for our setting; those values are scenarios, not expectations.
- **With the planned 32 episodes:** a Hoffman-size *unconditional* effect is detectable at N=24. The *beyond-condition* effect is well powered only if condition explains ≤~50% of the metric's variance, or if the true r is ≥0.3.
- **Required pilot step:** estimate the between-condition variance share and the within-condition SD of the primary metric, then re-run the power analysis before preregistration.
- **Not run (TODO):** a simulation with random slopes, 7-point discretisation and condition-structured metrics at N = 20/24/40. All values above assume random intercepts only and continuous ratings, so they are optimistic upper bounds.
- **Checks recorded.**
  - Paired-t n for d_z=0.5 is 34, which matches the standard G*Power paired-t output.
  - The value 34 reported by Skantze & Irfan came from a different (f=0.25) configuration, so that match is a coincidence of conventions.
  - r=0.3 → n=85, against ≈84 in textbook tables.

## 9. Risks

1. **Effect size and estimand.**
   - Metric↔rating correlations may be tiny (r≈0.12) and non-linear.
   - Variance created by the manipulation is absorbed by the condition term, so "strong manipulation spread" between conditions does *not* help the primary claim.
   - **Mitigation:** deliberate within-condition variation (onset phase, injected latency), measured in the pilot. Add threshold/tercile analyses as secondary.
2. **Perception ≠ timing (possible, weakly supported).** Perceived responsiveness may not track objective latency. The supporting evidence is limited to one non-significant Bonferroni-corrected item (Skantze & Irfan) and the performance↔experience dissociation in Kille et al. [S]. Report this honestly if it happens; it is itself a finding.
3. **Measurement validity.**
   - The primary criterion is a single adapted item; mitigated by the convergent and reliability checks.
   - Hoffman metrics are ill-defined for speech-only supervision, which is why they are exploratory.
4. **Scoop.**
   - **Differentiation vs Song et al.:** interruption-specific physical-repair metrics plus trial-level metric↔rating validity beyond condition. Interruption user studies *per se* are not new (05: SocialVLA, CMU HRI 2026, MICoBot, ExpressMM).
   - CDS, TurnNat and Synthetic TLX are moving fast on metric validation for speech.
   - CMU HRI 2026 and RIAP have not been checked for metric↔rating analyses.
5. **Simulated users inflate success and ratings** (Zhou et al.; text agents). Use them only for speech input and never substitute them for human ratings.
6. **Ethics timeline and institution.**
   - The committee is unknown, LMU-style estimates assume no revisions, and holiday or platform closures apply. The worst in-IROS case leaves ~2–4 weeks of data collection.
   - GDPR voice handling and voice cloning need explicit consent.
7. **Dependency on G2.** The mid-motion repair condition must run reliably on SO-101 by ~mid-Jan 2027. Otherwise the study compares only the baselines, and G4 loses its central condition.
8. **Session time.** 32 physical episodes with resets may exceed ~90 min. Mitigations are the k=4 fallback (with reduced power, see the table) and the pilot-measured budget.
9. **Low-cost hardware noise.** SO-101 jitter or latency variance can confound the metrics. Log hardware timing and pilot with n=4–6.
10. **Order, novelty and demand effects.** Use a balanced Latin square (N a multiple of 4) and blind the condition labels, as Song et al. did with "System A/B".

## 10. Blocked / open items

**Blocked (paywall/bot challenge; not worked around):**
- **Hoffman & Breazeal 2007, IEEE T-RO** (original metric definitions): IEEE paywall, not fetched.
- **IEEE Xplore** (HTTP 202 bot challenge):
  - Hoffman 2019 THMS: read via the author PDF; pagination confirmed via Crossref.
  - Skantze & Irfan HRI 2025: read via arXiv.
  - Baxter 2016: read via the author PDF.
- **ACM DL (403):**
  - Shiwa et al. HRI 2008: the JRSJ abstract was read instead.
  - PMQ (TOCHI): the arXiv abstract was read.
  - Bartlett et al. THRI 2022: only the snippet and Crossref metadata were seen.
  - Riek 2012 JHRI: guideline content not read.

**Open / unverified, with no fetch in this revision:**
- **Hoffman 2019:** the exact wording of the fluency scale items, needed for the primary criterion (from the hrc2.io PDF, Fig. 1), and whether the coefficient is Pearson.
- **Weiss et al.:** whether all 8 Hoffman statements were used, and the venue.
- **CDS:** author affiliation.
- **Almere:** item count and length.
- **Kille et al. 2025, RAPIDDS 2026, SocialVLA, MICoBot, ExpressMM:** the numbers come from the reviewer's alphaXiv full-text Q&A, not a PDF cross-check, so they are [S].
- **CMU HRI 2026 and RIAP:** not checked for metric↔rating analyses (paywalled / no preprint). These are open scoop surfaces.
- **Carried-over project-note items:** VITA-E and the n values in 04/05 have no source URL in this review.
- **Undefined thresholds:** the IROS 2027 human-subjects/ethics-statement policy was not checked; the convergent-validity target r and the agreement threshold are left as TODO.
- **Search log:** no systematic search log exists for the original pass (see §2). A logged search (databases, queries, dates) is needed before the gap statement is put in the paper.
- **Power analysis not run:** the full re-simulation (random slopes, 7-pt discretisation, N=20/24/40) is TODO, and pilot estimates of within-condition variance are required.

## Sources
- Hoffman 2019 THMS — https://doi.org/10.1109/THMS.2019.2904558 ; author copy https://hrc2.io/assets/pdfs/papers/HoffmanTHMS19.pdf ; RSS'13 page http://guyhoffman.com/evaluating-fluency-in-human-robot-collaboration/
- MAD-TN — https://arxiv.org/abs/1909.06675
- Weiss et al. 2023 — https://rbjackson.github.io/paper_pdfs/weiss2023analyzing.pdf
- Skantze & Irfan HRI 2025 — https://arxiv.org/abs/2501.08946 ; https://doi.org/10.1109/HRI61500.2025.10973958
- Kille et al. 2025 — https://arxiv.org/abs/2505.04182
- Cuellar, Hagenow, Shah 2026 (RAPIDDS) — https://arxiv.org/abs/2604.19670
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
- SocialVLA — https://arxiv.org/abs/2610.02360
- MICoBot — https://arxiv.org/abs/2508.05535
- ExpressMM — https://arxiv.org/abs/2604.05320
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
- Carried-over project notes (no URL in this review): VITA-E, ELLSA, Premover, RIAP, Tufts/TUW, CMU HRI 2026, Causeway, LIBERO-MAX, MAIL-Bench, ARMS, Yu & Qiu 2606.08881 — see `04-literature-map.md`, `05-gap-analysis.md`
- Local artifacts: `experiments/g4-fluency-metrics-validity/power.py`, `power_results.txt`; `outputs/.drafts/g4-fluency-metrics-validity-review.md` (Appendix A/B)
