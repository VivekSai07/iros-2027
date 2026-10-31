# Verification report: g4-fluency-metrics-validity-draft.md (2026-10-18)

Scope: I did not edit the draft. I checked that every source URL resolves and matches the claimed paper. arXiv IDs were checked against the arXiv API plus abs pages, and DOIs against the Crossref `/works/{doi}` API plus doi.org redirects. I spot-checked the high-stakes numbers (a)–(f) against primary full text and also checked several other [V] claims.

**Overall:**
- **(a)–(e):** every number matches its primary source. (f) is confirmed on the official pages.
- **Mismatches:** there are no number mismatches. Four wording or interpretation issues remain (I1–I4).
- **Hygiene:** there are two citation-hygiene problems (H1–H2).

## A. Spot-checks (a)–(f)

### (a) Hoffman 2019, THMS (author PDF hrc2.io): CONFIRMED
- **n = 104 (bullet 1, §2):** confirmed. "A total of 143 people participated in the study. Of those, 104 participants were analyzed".
- **5 of 50 clips, ~40 s, $0.10:** confirmed.
  - "each participant was presented with five short clips … approximately 40 s in length … chosen from a database of 50 clips"
  - "Participants were paid $0.10"
- **r(495) values:** confirmed. "R-IDLE was not significantly correlated … r(495) = −0.074. H-IDLE was significantly correlated … r(495) = 0.119, p < 0.01. C-ACT was not significantly correlated … r(495) = 0.047. F-DEL was significantly reverse-correlated … r(495) = −0.123, p < 0.01." So |r| ≤ 0.123 is correct.
- **α values 0.81 / 0.74 / 0.84:** confirmed.
  - "pretest (n = 21) … Cronbach's α = 0.81. In the study, Cronbach's α for this composite was 0.74."
  - "Its inclusion in the scale reduces the scale's Cronbach's α from 0.84 to 0.74", referring to "The human was the most important member".
- **H-IDLE positive, terciles, personality:** confirmed.
  - "Surprisingly, H-IDLE is positively correlated with fluency."
  - "very high R-IDLE does lead to a drop in fluency perception, as does very low C-ACT"
  - "the robot's personality traits were not strongly correlated with the objective fluency measures"
- **Origin of three metrics:** confirmed. "Three of them were originally proposed in [5]: … C-ACT … H-IDLE … F-DEL. Later work added a fourth metric: … R-IDLE." Reference [5] is Hoffman & Breazeal, T-RO 23(5):952–961, 2007.
- **Definitions:** confirmed.
  - R-IDLE: "not perceivably active"
  - F-DEL: "F-DEL can be negative when actions are overlapping … can also be larger than 1".
- **Fig. 1 inventory:** confirmed. "a three-item scale evaluating fluency directly (1) and six possible downstream outcomes … Scale 6 is an adaptation of … Working Alliance Inventory".
- **Ringing / per-turn caveat:** confirmed. "there is an initial 'ringing' period … Researchers should evaluate the metrics with respect to a single turn instead of the total task time if the number of turns is low."
- **Volume 49(3):209–218:** not in the author PDF, which says "with the exception of pagination". It is confirmed via Crossref: IEEE THMS vol 49, issue 3, pp. 209–218, 2019, author Hoffman.
- **Not checked:** the claim that the paper used a "Pearson" correlation.

### (b) Skantze & Irfan, arXiv 2501.08946: CONFIRMED
- **n = 39:** confirmed. "within-subject design in an HRI study with 39 participants"
- **Design:** confirmed.
  - "2 (ordering) x 2 (scenario) … 7 minutes with both systems … 1.5 hours per participant"
  - "39 native English speakers (power= 0.86)"
- **Response times 1.5 vs 2.7 s:** confirmed. "The median response time for the proposed system is much shorter (1.5 s vs 2.7 s; Wilcoxon signed-rank test; W = 776; p < 0.001)."
- **Interruption rate 6.9% vs 16.6%:** confirmed. Table I reads "Proposed 1.5 1.5 0.6 6.9% / Baseline 2.2 2.7 2.6 16.6%". The difference test is W = 601, p < 0.001.
- **Q3 p = 1.0:** confirmed.
  - Appendix D: "Q3: The robot was slow to respond 2 (2-3) 3 (2-4) 142 1.0", with "P-values are Bonferroni corrected."
  - Main text: "The only question which did not have a significant difference was the perceived response delay".
- **Q1 fluid p = .014:** confirmed. "Q1: The conversation with the robot was fluid 6 (5-7) 5 (3-6) 277 0.014".
- **Preference 27/9/3:** partly confirmed. The paper says "9 out of the 39 participants indicated a preference for the baseline and 3 had no preference." The figure 27 is derived (39 − 9 − 3) and is not stated in the paper.
- **Participant self-annotation:** confirmed. "Participants were asked to annotate when they felt the robot 'did not let them speak'".
- **G\*Power:** confirmed. "f = 0.25 … required 34 participants … (calculated by G*Power)"
- **Ethics:** confirmed. "reviewed and endorsed by the university's research ethics and data officers"
- **Venue:** the PDF names no venue. The arXiv comment says "Accepted at HRI 2025". Crossref for DOI 10.1109/HRI61500.2025.10973958 gives the same title, authors Skantze and Irfan, HRI 2025, pp. 859–868.

### (c) Song, Zi, Guanting, arXiv 2607.00530: CONFIRMED
- **Metadata:** title "From Technical Metrics to User Perception: A User Study of a Multimodal Human–Robot Interaction System for Object Detection and Grasping". arXiv v1 is dated 1 Jul 2026. Authors are Jian Song, Tian Zi, Shen Guanting, all at Dalian University of Technology.
- **n = 24:** confirmed. "A total of 24 volunteers participated in the study."
- **Robot:** confirmed. "The robotic arm is a Dobot Magician equipped with a suction-based end-effector"
- **Preference:** confirmed. "17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43)"
- **d_z values:** confirmed.
  - Speed: "d_z = 1.85 … t(23) = 9.09, p_adj < 0.001"
  - Reliability: "d_z = 1.54 … t(23) = 7.54"
  - Competence/fluency: "d_z = 2.03 … t(23) = 9.93"
- **75%→90% from prior ablation:** confirmed. "from 75% in a multimodal baseline system to 90% in an improved configuration identified through a prior ablation study". The user study did not measure success itself.
- **Session protocol:** confirmed.
  - "each volunteer therefore completed four live runs: two with the baseline system and two with the improved system"
  - "Each session lasted approximately 30 minutes"
  - "presented neutrally … as System A and System B"
- **Analysis deviation:** confirmed.
  - Plan: "the default inferential test will be the Wilcoxon signed-rank test"
  - Reported: "the paired two-tailed t-test was used as the primary inferential test"
- **Preregistration:** the draft's [U] is correct. The paper says "All three pre-registered hypotheses …" but gives no registry or link.
- **Ethics:** the draft's [U] is correct. The string "ethic" does not appear anywhere in the extracted full text.

### (d) Zhou et al., arXiv 2603.11245 (v2, "Published as a conference paper at COLM 2026"): CONFIRMED, with caveat I1
- **Scale:** confirmed. "451 participants, 165 tasks), benchmarking 31 LLM simulators"
- **Success rates:** confirmed. "higher agent success rates than the human baseline (63.6%), with top models reaching 77.8%."
- **Agreement:** confirmed. Figure 2, under "Success criteria", reads "Human-Human agreement: 95.6%; Human-LLM agreement: 29.7% ~ 81.1%". These are agreement figures on success-criteria judgments; the draft table states them without that qualifier.
- **USI:** confirmed. "the best simulator achieves a USI of 76.0 … far below human scores of 92.7". The 92.7 is labelled "Human (inter-ann.)".
- **GPT-5.1:** confirmed. "overestimates AI assistant's human-likeness by 55% and overall score by 18% of the rating scale."
- **Binary reward:** confirmed. "τ-bench's binary reward is largely orthogonal to human-perceived quality".

### (e) EchoChain, arXiv 2604.16456: CONFIRMED
- **Counts:** confirmed. "240 judgments across 80 pairs … 97 favored the cloned sample, 92 favored the human sample, and 51 reported no detectable difference … X² = 0.92 (p = 0.63)".
- **Models:** confirmed. "Dialogue Planner Module, implemented with GPT-5.2" and "User Simulator Module, implemented with Gemini 3 Pro".
- **Voice cloning:** confirmed. "Minimax Voice Cloning … pool of recorded voice actors".
- **Barge-in timing:** confirmed. "scheduling each barge-in at a fixed offset from the assistant speech onset".

### (f) Ethics timelines: CONFIRMED
- **LMU** (ek.mathematik-informatik-statistik.lmu.de):
  - "[Regulärer Antrag] (avisierte Bearbeitungszeit ca. 6-8 Wochen)"
  - "[Fast-Track Antrag] (avisierte Bearbeitungszeit ca. 2-4 Wochen)"
  - The times are "kalkuliert, dass sich in der Begutachtung keine Rückfragen oder Überarbeitungsbedarfe ergeben", i.e., they assume no queries or revisions.
- **ETH** (how-to-apply page):
  - "at least two months before the planned start of the project"
  - "3-6 weeks until the first decision (depending on the risks)"
  - "2-3 more weeks if … requires further revisions"
  - "Closure of current ethics submission platform eResearch: 22 November 2026"
  - "New platform opening for submissions: 1 December 2026"
  - "close as usual over the holiday period and reopen on 4 January 2027". The start date of the holiday closure is not stated.

## B. Other [V] claims checked

| Claim | Verdict | Evidence |
|---|---|---|
| Weiss et al. 2023: Sawyer, MTurk, Bayesian RM-ANOVA, 49–53 per set | Confirmed | Weiss PDF: "robot Sawyer", "Amazon Mechanical Turk", "Bayesian repeated measures analyses of variance". Table 2 lists 49/53/51/51/51/52 |
| Weiss: CON-ACT/CON-IDLE BF = 18.5; H-IDLE opposite; FUNC-/RESOURCE-DELAY weak or mixed | Confirmed | "strongly favors the model that the video affected participant responses (Bf=18.489) … strongest evidence … in this study". "the opposite of what H1 predicts" (F2, Bf=6.723). RESOURCE-DELAY: "the results are mixed" |
| Weiss venue | [U] is correct | Only "Copyright © 2023, Association for the Advancement of Artificial Intelligence" |
| MAD-TN definitions; no human data | Confirmed (arXiv PDF) | "concurrent inactivity, that measures the amount time both agents are simultaneously inactive". "Resource delay captures the time between when an agent is ready to use a resource and when that resource becomes available". Human study is only "plans to design … experiment" |
| Hoffman RSS'13 author page | Confirmed (year from Hoffman 2019 ref [9]) | Page: "Please refer to the new journal version". The page itself does not show 2013 |
| Shiwa JRSJ: 1 s / 2 s / fillers | Confirmed (J-STAGE abstract) | "highest at one second, and user preference ratings level off at two seconds". "conversational filler … moderated the user's impression toward a long SRT" |
| TurnNat 150×3, 70.0% / 78.0%, 88.0% | Confirmed | "150 natural–perturbed pairs … rated by three independent … annotators". "70.0% … 78.0% of pairs". "88.0% matched-pair accuracy". The 88.0% is measured on the 1,000-pair automatic benchmark |
| CDS: 374 conversations / 56 callers / 1,026 votes; ρ 0.222–0.266; 0.615; ≤1-min excerpts | Confirmed | "374 conversations involving 56 human callers". "1,026 humanness pair–wise judgment votes". Table 1 composite 0.222 and 0.266; Sylber duration 0.615. "Short excerpts of one minute or less fail to reproduce rankings reliably". The "KTH et al." affiliation was not checked |
| Synthetic TLX: r = 0.648/0.679/0.834; 54 points; reversal in 2 of 3 tasks; 522 CHI papers; ~10% | Confirmed | "yielding 54 paired data points". "reaching a peak of r = 0.834". "522 CHI papers used the NASA TLX". "In 2024 alone, nearly 10%". The reversal holds for email and website. Note: the human email difference was only marginal |
| Synthetic TLX: human n = 18 per group (draft marks [S]) | Can be upgraded to [V] | "our final sample consisted of 162 participants, with 54 participants per task, and 18 participants per group within each task." |
| French FDB: trade-off; no human raters | Confirmed, minor wording issue (I3) | "We also find a trade-off between optimizing benchmark metrics and preserving conversational naturalness." Response quality is rated by an LLM judge ("llama3.3:70b") |
| PACT: COOPERA, Habitat 3.0, Llama-3.1-8B, Big-Five, 0.764 / 0.712 / 0.810, U formula | Confirmed | Quotes in Tables 2, 4 and 5 and Eq. (4). The 0.764 and 0.712 come from the earlier COOPERA validation. "PACT has no real-human eval" is an inference: the paper does not state it, but nothing contradicts it |
| Baxter 2016: 101 papers, "<20 subjects", WoZ 25 vs 26, 5 of 26 omit "wizard" | Confirmed | Table I: "Uses WoZ 3 (12%) 11 (35%) 11 (28%) 25". Text: "5 papers from 26 utilising a WoZ omit the word 'wizard'". Fig. 3: "The majority of conditions have fewer than 20 subjects." |
| Leichtmann 2022: 8 meta-analyses; sample sizes | Confirmed | "eight meta-analyses". "M = 46.52 … Mdn = 29", "Mdn = 37", "M = 27.72 … Mdn = 22", "Mdn = 21" |
| DFG FAQ | Confirmed | "must generally be submitted if patients are involved … or if material taken from humans is used". "it may be necessary …", followed by the list of exceptions (vulnerable groups, deception, physical risk, …) |
| EDPB paras 31 and 128 | Confirmed | Para 31: "The EDPB recalls that voice data is inherently biometric personal data … be accompanied by a derogation from Article 9". Para 128: "will require the explicit consent … (Article 9(2)(a) GDPR)" |
| PMQ (abstract) | Confirmed | arXiv abstract: "18-item … semantic differential … non-embodied speech interfaces … three factors". Crossref: TOCHI 32(4), 2025 |

## C. Source list: resolution and metadata

| Source | URL status | Metadata match |
|---|---|---|
| Hoffman THMS DOI | doi.org → IEEE Xplore returned HTTP 202 (bot challenge; **blocked**, not bypassed) | Crossref: title, author Hoffman, 2019, 49(3):209–218. Match |
| hrc2.io author PDF | 200 | Match |
| guyhoffman.com RSS page | 200 | Match |
| arXiv 1909.06675, 2501.08946, 2607.00530, 2603.11245, 2607.01345, 2609.10765, 2609.31719, 2609.12273, 2604.16456, 2605.24350, 2609.24547, 2610.08733, 2308.07164 | All abs pages 200 | All titles, first authors and years match the draft's labels (arXiv API) |
| Weiss PDF (rbjackson.github.io) | 200 | Match |
| Skantze & Irfan DOI | IEEE 202 (**blocked**) | Crossref match |
| Shiwa ACM DOI 10.1145/1349822.1349843 | ACM DL 403 (**blocked**) | Crossref: Shiwa, Kanda, Imai, HRI 2008, pp. 153–160. Match |
| Shiwa J-STAGE | 200 | Crossref 10.7210/jrsj.27.87: JRSJ 27(1):87–95, 2009. Match |
| PMQ DOI 10.1145/3729170 | ACM 403 (**blocked**) | Crossref match (Doyle et al., TOCHI 2025) |
| Almere DOI | 200 (Springer) | Crossref: Heerink et al., IJSR 2(4):361–375, 2010. Match |
| Baxter DOI 10.1109/HRI.2016.7451777 | IEEE 202 (**blocked**) | Crossref: "From characterising three years of HRI to methodology and reporting recommendations", Baxter et al., HRI 2016. Match |
| Baxter author PDF | 200 | Match |
| Leichtmann DOI | 200 | Crossref: "Crisis Ahead? …", Frontiers Robot. AI 9, 2022. Match |
| Riek DOI | → ACM 403 (**blocked**) | Crossref: Riek, JHRI, 2012, pp. 119–136. Match |
| Schaefer OpenAlex W2563047483 | 200 | Partial match, see I4 |
| DFG, LMU, ETH, EDPB PDF | All 200 | Match. The EDPB URL redirects to `/system/files/documents/2021-07/…` |

## D. Issues to fix

**I1 (meaning, §6).** The draft says system *rankings* by USI were "largely preserved" across agents, and uses this to support ranking conditions with simulators. In the source, what is preserved is the **ranking of user simulators** when the agent is swapped for Gemini-3.1-Pro. That check covered only 5 simulators: "the relative ordering of user simulators is largely preserved". It is not evidence that simulators preserve the ranking of the systems or conditions under test.
- Fix: reword the claim.
- Consequence: the inference "use simulated users to rank conditions at scale" loses this support. It should be presented as a hypothesis to test.

**I2 (precision, bullet 3, §3).** The preference count of 27/39 is computed, not quoted. Mark it as derived.

**I3 (wording, §3 French FDB).** The draft says human–human conversations "do not achieve 'optimal' FDB scores". The source says they "do not always yield optimal FDB scores". Change to "do not always".

**I4 (metadata, §4 Schaefer).** The OpenAlex record W2563047483 has type "article". Its source is mislinked to "Journal of International Crisis and Risk Communication Research". Its landing page is stars.library.ucf.edu/etd/2688, which is a UCF ETD (dissertation). The draft's "UCF dissertation per OpenAlex" is right in substance, but the OpenAlex record itself is inconsistent. Cite the UCF STARS URL instead.

**H1 (orphan citation).** Bartlett et al. (DOI 10.1145/3495246) is cited in §5 but missing from Sources. Crossref confirms the metadata: Bartlett, Edmunds, Belpaeme…, ACM THRI 11(2):1–16, 2022. Add it to Sources; the full text is still ACM-blocked, so it stays [S].

**H2 (orphan mention).** VITA-E (§8) and "04-literature-map / 05-gap-analysis" sample sizes (§5) have no entry in Sources. Either add sources or mark them as carried over from internal notes. I did not verify the carried-over n values (SocialVLA 15, CMU 18, MICoBot 18, ExpressMM 23, RIAP 30).

**Upgrade.** The Synthetic TLX human n = 18/group can move from [S] to [V] (quote in §B).

## E. [V] claims not confirmed in this run (not contradicted; just not checked)
- Hoffman 2019 "Pearson" (the word was not searched for).
- Weiss: participants rated "Hoffman's 8 statements" (I only saw F1, F2, F5 and F6).
- CDS "KTH et al." affiliation.
- Almere is marked "[V] (Springer abstract)". Only the metadata and DOI resolution were checked here; the title supports "older adults' … assistive social agent".
- MIRA (2609.24547) and Kennington (2610.08733): only the existence and title of each paper were checked. The MIRA abstract confirms barge-in preemption.

## F. Blocked or unreachable (not worked around)
- **ACM DL (403):**
  - 10.1145/1349822.1349843 (Shiwa)
  - 10.1145/3729170 (PMQ)
  - 10.1145/3495246 (Bartlett)
  - 10.5898/JHRI.1.1.Riek (resolves to dl.acm.org)
- **IEEE Xplore (HTTP 202 bot challenge):**
  - 10.1109/THMS.2019.2904558
  - 10.1109/HRI61500.2025.10973958
  - 10.1109/HRI.2016.7451777
- All seven DOIs are registered, and Crossref metadata matches the draft for each. Open copies were used where they exist: the hrc2.io PDF, arXiv, J-STAGE and the Baxter author PDF.
- No dead links were found.
