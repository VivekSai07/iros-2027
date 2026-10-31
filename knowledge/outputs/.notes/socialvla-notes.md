# SocialVLA (2610.02360v1) — windowed notes
Source text: outputs/.notes/socialvla-raw.txt (pdftotext -enc UTF-8 of https://arxiv.org/pdf/2610.02360, 8 pages, 41630 chars). Tier 2, window=6000.

## Windows 1-2 (chars 0-12000)
- Title: "SocialVLA: A Social Perception Gateway for Human-Reaction-Based Failure Detection and Recovery in VLA Manipulation". Authors Konstantinova, Altamirano Cabrera, Lykov, Tsetserukou; Skoltech ISR Lab + MWS R&D Center, Moscow. v1, 1 Oct 2026, cs.RO. [V]
- Abstract numbers [V]: 15 participants; 238 annotated intervention-worthy reaction episodes; 1.038 h annotated non-intervention; frozen offline replay cascade 54.6% event recall / 69.5% precision; unfiltered first-event A-V fusion 64.3% recall; relevance module false-stop episodes 100->57, precision 60.5%->69.8%; prospective 16th unseen participant 59.5% recall / 91.7% precision; median detector-to-fusion 47.9 ms; median VLA-gate-to-physical-hold 336 ms; matched reaction-onset-to-physical-hold 1.021 s.
- After intervention a separate speech channel records participant's verbal correction and associates it with the interrupted VLA action -> "participant-directed continuation, restart, or instruction revision". Abstract calls it "a participant-directed recovery interface". [V]
- Contribution 3 lists what is measured: reaction detection, false interventions, timely recall, end-to-end physical stopping latency. No repair metric listed among contributions. [V]
- Scope: "failure detection refers to detecting human-perceived intervention need ... rather than exhaustively identifying all physical robot failures". Cannot verify observer interpretation is physically correct. [V]
- Related: SAFE, FAIL-Detect, AHA, Stiber et al., BAD, REFLEX, ERR@HRI. Section II.C: reaction+correction records proposed as temporal supervision for future policy learning (future, not done). [V]
- Arch: event e_i=(modality, class, score, source interval, publish time); audio 16 kHz mono, causal 320-ms windows; Aniemore emotion model (wav2vec 2.0) 7 emotion logits. [V]

## Windows 3-4 (chars ~11500-24000)
- Audio heads: 28 features (latest logits, mean, std, delta); history cleared on gaps >0.21 s; fast head h<=0.4 s, extended head h<=2.0 s; ExtraTrees 160 trees, min leaf 2. Audio labels strictly modality-local. [V]
- Lexical path: Vosk, "authorized Russian stop commands and negative phrases" (restricted vocabulary) -> unit-strength candidate. [V]  => language is Russian; not English.
- Video: YuNet face + MobileFaceNet 7 expression scores; 25-dim per-frame + 400-ms diff = 50 features; ExtraTrees 160 trees min leaf 20; mirrored augmentation on training only. [V]
- Relevance head: video-only logistic, r=P(robot_related|x_v); 4-class attention head diagnostic only (not veto). [V]
- Fusion: u_q=max(p_a^q, p_v, v); a(r,v)=0.85+0.15r if lexical else 0.70+0.30r; s_q=u_q*a; threshold theta=0.772; r=0.5 default; association window W=700 ms (not a waiting period); t_request = min publish time over authorized classes (first-event). [V]
- Stop-and-correct interface (III.H) [V]: "gasp-vla-gate" sends ONE pause command -> hold; robot stays paused until participant explicitly requests continuation; options: resume from held state, adjust workspace and restart action, or give revised instruction for a SUBSEQUENT VLA action. Post-stop Vosk logging session records unrestricted correction + timestamp; "non-safety-critical: it cannot resume the robot, clear the hold state, or issue motion commands". Resume only via explicit resume command.
  => Corrections are LOGGED, not parsed into robot behaviour by the system itself in the described design; revision applies to a subsequent action (no mid-motion re-targeting).
- Episode record M_k=(id, t_r, t_s, t_c, a_k active VLA action/chunk, modalities, evidence, y_k transcript). "policy retraining itself is outside the scope of this work". [V]
- Platform [V]: physical Unitree G1 humanoid, GR00T-WholeBodyControl, GR00T policy trained for pick-and-place (grasp ball, place in target region). Failures naturally occurring, not announced; participants not instructed to react.
- "prediction target ... is the observer's intervention-worthy response rather than a predefined taxonomy of physical failure modes." [V]
- Recording [V]: 15 finalized sessions / 15 participants, ~1 m from robot, knew task. Labels: modality, intervention status, robot-related, attention target, reaction subtype, event id. 238 robot-related intervention-worthy episodes; 62.3 min non-intervention (=1.038 h). A/V merged if overlap or <=700 ms.
- Eval protocol [V]: (1) frozen cascade + ablations replayed over 15-participant corpus (NOT an unseen-participant generalization estimate, explicitly); (2) prospective live on 16th unseen participant, excluded from all fitting/selection. Match: first crossing within [onset, onset+1 s]; "timely" criterion onset..500 ms; predicted episodes merge crossings <=400 ms; one-to-one matching; predictions before onset not counted. Operating point maximizes recall s.t. exploratory non-intervention FPR target 0.10.

## Windows 5-6 (chars ~23500-36000)
- Metrics defined [V]: Precision, Recall, NonInt-FPR = N_NonInt,triggered / N_NonInt (episode-level), F1; false stop episodes/h; median & p95 onset->first stop request; timely Recall500. Wilson 95% CIs for recall/precision/FPR; participant bootstrap for cross-participant comparisons.
- Table I (full offline frozen cascade, 15 sessions) [V]: TP 130, FP 57, FN 108; Recall1s 54.6%; Timely Recall500 45.4%; Precision 69.5%; Non-interv. FPR 28.9%; False stops/h 54.9.
- Table II(a) prospective, 16th participant [V]: TP 22, FP 2, FN 15; Recall 59.5%; Precision 91.7%; Non-interv. FPR 9.5% (over 21 annotated non-intervention episodes); false stops/h 20.9 (over 344.18 s non-intervention; Poisson 95% CI 2.53-75.57/h); Recall500 21.6%; reaction-to-request median/p95 0.742/0.932 s. Wilson CIs: recall 43.5-73.7%, precision 74.2-97.7%, FPR 2.7-28.9%.
- Table II(b) live latency, median/p95/max (s) [V]: detector->fusion (n=22) 0.048/0.085/0.091; fusion->VLA gate (n=22) 0.001/0.001/0.001 (text: 0.66 ms median, 0.93 ms p95); VLA gate->physical hold (n=24) 0.336/0.681/1.559; reaction onset->physical hold (n=14) 1.021/1.569/1.576.
- Physical hold definition [V]: "pre-stop body or hand motion of at least 0.12, followed by five consecutive telemetry samples with maximum absolute velocity at most 0.06" (units not stated in extracted text). Onset->hold computed per matched event, not by summing. This is the ONLY motion-after-stop measure: a latency to standstill, not a residual displacement/energy metric.
- Table III ablations (offline, 15 sessions; TP/FP/FN, Recall1s, Recall500, Precision, NonInt FPR, FS/h) [V]:
  Audio-fast 115/72/123, 48.3%, 41.6%, 61.5%, 32.2%, 69.3
  Audio-context 111/30/127, 46.6%, 39.9%, 78.7%, 20.0%, 28.9
  Video 53/30/185, 22.3%, 16.8%, 63.9%, 17.8%, 28.9
  Audio+Video 153/100/85, 64.3%, 54.6%, 60.5%, 41.1%, 96.3
  A+V+relevance 132/57/106, 55.5%, 45.8%, 69.8%, 27.8%, 54.9
  Full SocialVLA 130/57/108, 54.6%, 45.4%, 69.5%, 28.9%, 54.9
  (column alignment reconstructed from pdftotext; values consistent with text: A+V 64.3%, relevance 100->57 FP, 60.5->69.8% precision, 41.1->27.8% FPR, 132 of 153 TP retained.)
- Runtime: 47.6 ms per 320-ms audio window (batched offline). [V]
- V.D Stop-correct operation [V]: while held, post-stop channel records participant's verbal description + reaction, active action, stop timestamps; participant can continue, restart from adjusted scene, or provide revised instruction. "each intervention produces a reaction-centered marker ... for subsequent VLA dataset curation." NO quantitative result reported for corrections (no transcription accuracy, no post-correction success, no counts of continue/restart/revise).
- Discussion [V]: less effective when observer doesn't react / ambiguous / unrelated stimulus; suggests combining with robot-internal monitors ("non-intervention or FAIL-Detect" — apparently a typo in source).
- Limitations start [V]: 16 participants total; sample doesn't establish generalization across language, culture, age, appearance, neurodiversity, reaction style.

## Window 7 (chars ~35500-41630) + targeted greps
- Limitations [V]: relevance head may confuse robot-related with coincident behaviour; "0.7 floor" lets unrelated strong reactions pass; calibration/false stops need longer recordings with natural distractors; ground truth = human-perceived need, unnoticed failures out of scope, observer may react to non-failures; "not a certified safety system; a hardware emergency stop, conservative robot limits, and independent supervision remain necessary."
- Section VII is titled "Limitations and Ethical Considerations" but grep for consent|ethic|IRB|approv|committee|recruit|compens -> only the section title matches. NO ethics-board approval, informed-consent, recruitment, demographics or compensation statement in the v1 text. [V by absence in extracted text]
- Conclusion [V]: "demonstrating end-to-end operation of the complete stop-and-correct pipeline"; future work: combine with robot-internal monitors; "investigate how reaction-centered correction records can support subsequent policy adaptation".
- Code/data release: no GitHub/project URL in PDF text; arXiv abs page has no Comments field and no code link (grep). Only external URL is Aniemore HF model (wav2vec2-emotion-russian-resd). => No code/data release stated. [V by absence]
- 8 pages, refs [1]-[19]; ERR@HRI 3.0 (arXiv:2607.11570) cited for anticipatory vs post-failure reactions.
