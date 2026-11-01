# Assistance-boundary research-question scan — 2026-11-01

State: reviewed research output; proposals remain **unadopted**.

## Scope and protocol

Question: what is actually missing in human-intent-aware physical collaboration, specifically a robot deciding when to help, clarify, wait, or refrain?

Search: public web/manual primary-source search on 2026-11-01, primarily arXiv full text and official IEEE/ACM pages. Initial window: 2022-11-01 through 2026-11-01, extended to 2016/2021 for seminal initiative and shared-autonomy work. Included embodied or directly transferable work on assistance timing, initiative, uncertainty, clarification, abstention, closed-loop adaptation, and counterfactual cost. Pure conversational systems were excluded unless the decision mechanism transferred directly. This pass is bounded, not exhaustive.

Feynman was not used: the current checkout lacks its ignored local Node/runtime (`python tools/run_tool.py feynman status` failed before authentication or a research job). No paid search or model call was made.

Evidence notation: `[V full]` = primary full text inspected; `[V abstract]` = primary abstract/publisher record inspected; `[S]` = secondary only; `[U]` = not checked.

## Bottom line

The broad claim “a robot that knows when to help or not help” is **not open**. It is directly covered by non-intrusive assistance, proactive initiative, attentive support, mixed initiative, confidence-aware shared autonomy, and a 2026 theoretical framework devoted to socially appropriate help.

The defensible opening is narrower:

> A real-time, uncertainty-calibrated **assistance-boundary policy** that chooses among direct help, clarification, deliberate observation/waiting, and refraining; it is evaluated in closed loop by counterfactual human work saved minus wrong-help, undo, interruption, and social costs, and its proxy evaluation is validated with real human partners.

No inspected work established that full conjunction. This is an inference over the bounded comparison below, not a novelty verdict.

## Nearest-neighbor comparison

| Work | Decision covered | Evaluation | Limitation relevant to this project | Evidence |
| --- | --- | --- | --- | --- |
| Ramnauth, Brščić, Scassellati, *To Help or Not to Help?* (THRI 2026, DOI 10.1145/3797264) | Offer help vs do not offer, using relative skill and help utility/cost | Large online vignette study | Explicitly leaves help timing under uncertain human/robot skill and “offer versus directly do” as future work; no physical collaboration | [V full, publisher page] |
| Patel & Chernova, *Robots That Take Initiative* / GAP (arXiv:2609.28910) | Unprompted act/no-op with counterfactual net value/cost | Closed-loop VirtualHome with an LLM-adaptive human; prior offline methods can add work | LLM proxy only; authors call for longitudinal real-user validation; no clarification action or physical robot | [V full] |
| Zhang et al., NIABench (arXiv:2605.01368) | When and what non-intrusive help to execute | AI2-THOR benchmark; two real-robot demonstrations | Simplified task plans; benchmark has no visual modality; dynamic plan changes and partial observability are future work; no participant study reported | [V full] |
| He et al., PACT (arXiv:2605.24350) | Ask or act under partial observation and cross-day history | Profile-conditioned simulated humans; Clarification Utility = accuracy / (1 + ask rate) | No physical robot or real users; no deliberate wait/refrain mode; equal cost for all questions | [V full] |
| Ghose et al., BALI (HRI 2026; arXiv:2512.04453) | Ask when expected information gain exceeds interruption cost, then select supportive action | Collaborative cooking simulation and proof-of-concept real-world task | Fully observable high-level turn-taking; no real-user outcome validation found in inspected text; no calibrated abstention boundary | [V full] |
| Liu et al., event-driven proactive assistance (arXiv:2610.08344v2) | Decide whether assistance is appropriate after observed state transitions | Three real tabletop tasks, no task-specific fine-tuning | Event completion is the trigger; no human study or uncertainty/cost calibration found | [V abstract; targeted full-text check] |
| Schneider et al., *Attentive Support* (IROS 2024, DOI 10.1109/IROS58592.2024.10801517) | Help or remain silent in human groups | Scenario evaluation with a robot | LLM common-sense pipeline; no formal calibrated utility/uncertainty decision identified from the abstract | [V abstract] |
| Baraglia et al., *Initiative in robot assistance* (HRI 2016, DOI 10.1109/HRI.2016.7451735) | Human-initiated, reactive, and proactive help | Physical tabletop study, N=18 | Proactive improved fluency, but people preferred control over help timing; fixed trigger models, not uncertainty-calibrated | [V abstract] |
| Natarajan et al., mixed-initiative Bayesian adaptation (arXiv:2403.16178) | Adapt intervention style to willingness to comply | Sequential decision game with user studies | Models compliance/intervention style rather than physical assistance utility and help/ask/wait/refrain selection | [V abstract] |
| Zurek et al., situational confidence shared autonomy (arXiv:2104.06556) | Assist when intent is in repertoire; return control when it is not | Case study and user study | Teleoperation/shared autonomy rather than unprompted proactive help; demonstrates why abstention under model mismatch matters | [V abstract] |
| ICRA 2026, *Detecting Help-Seeking via Implicit Signals* (DOI 10.1109/ICRA57385.2026.11696882) | Detect whether a person needs help | Robot-assisted assembly user study; abstract reports F1 0.98 | Need detection does not by itself select the socially appropriate intervention mode or account for wrong-help cost | [V abstract] |

## What is closed, partial, and open

Closed as broad novelty claims:

- “The robot decides when to help.”
- “The robot sometimes does not help.”
- “The robot asks when uncertain.”
- “Intent-aware proactive assistance improves collaboration.”
- “A benchmark measures non-intrusive assistance.”

Partially covered:

- Counterfactual work saved/added is formalized by GAP, but only with an LLM-adaptive simulated human.
- Ask-versus-act is covered by PACT and BALI, but not together with a physical, socially calibrated abstention boundary.
- Real-robot non-intrusive help exists, but participant validation and dynamic uncertain intent are weak or absent in the nearest examples.
- User preference for control and intervention style is known, but not integrated with modern proactive manipulation policies.

Open in this bounded pass:

- Joint selection among `DO`, `ASK`, `WAIT/OBSERVE`, and `REFRAIN` under uncertainty about human goal, human skill/preference, and robot capability.
- A metric that charges the policy for wrong help, undo/rework, interruption/query burden, and social intrusiveness—not only task success or help accuracy.
- Validation that an adaptive simulated-human evaluation predicts policy ordering and failure modes with real people in physical collaboration.
- Online personalization of the assistance boundary without overfitting to compliance or suppressing user agency.

## RQ-A — Assistance-boundary policy (recommended method question)

State: proposed.

Problem and affected users/tasks: In tabletop collaboration, proactive help can save effort but a mistaken or mistimed intervention can add work, interrupt the person, or undermine agency. Existing methods usually select a subset of act/no-op, ask/act, or return-control choices.

Closest prior work with primary evidence: Ramnauth et al. [V full], GAP [V full], NIABench [V full], PACT [V full], and BALI [V full].

Author-stated limitations vs inference: Ramnauth explicitly leaves uncertainty-aware timing and offer-versus-do decisions open. GAP explicitly lacks real longitudinal users. NIABench explicitly simplifies human plans and lacks dynamic changes/partial observability. The absence of a four-way physical policy is our bounded-search inference.

Falsifiable question: **In ambiguous tabletop collaboration, can an uncertainty-calibrated policy choosing `DO`, `ASK`, `WAIT`, or `REFRAIN` reduce counterfactual human work without increasing wrong-help/undo events or perceived intrusiveness, compared with always-help, act/no-op, and ask/act policies?**

Hypothesis: the four-way policy will reduce net human cost because it can gather information without always interrupting and can abstain when both direct action and clarification have negative expected value.

Strongest counterexample: BALI already trades expected information gain against interruption cost and selects supportive actions; PACT learns ask-or-act. The proposal is weak unless `WAIT` and `REFRAIN` are operationally distinct, robot capability uncertainty is included, and evaluation uses physical closed-loop human consequences rather than only inference accuracy.

Baseline, control, primary metric, meaningful effect:

- Baselines: always-help; calibrated act/no-op; PACT-style ask/act; human-request-only; oracle.
- Control: identical intent/capability estimator and action primitives across policies.
- Primary metric: `Net Assistance Value = counterfactual human action/time cost saved - undo/rework cost - query/interruption cost - robot-caused failure cost`.
- Preliminary practical threshold for a go decision: at least 15% lower human action/time cost than the strongest baseline, with no more than a 5 percentage-point increase in failure or wrong-help episodes. Thresholds must be justified and frozen before a confirmatory run.

Cheapest discriminating experiment: a small closed-loop simulation with two tasks, ambiguous goal pairs, injected robot capability failures, and four scripted human-response profiles. Test whether `WAIT` or `REFRAIN` is chosen and produces benefit beyond ask/act. Only if that survives, run an ethics-approved physical pilot on SO-101.

Compute/hardware/data/ethics needs and budget: light decision layer and simulator; one SO-101 for the pilot; no large-model training required if a frozen VLM/LLM supplies semantic hypotheses. Any real-human pilot requires the institutional ethics route and a data/retention plan.

Failure/pivot criteria: reject the method wedge if ask/act matches the four-way policy, the policy cannot calibrate uncertainty, or perception errors dominate decision-policy differences. Pivot to RQ-B as a systematic evaluation paper.

## RQ-B — Do proxy evaluations predict real proactive-assistance outcomes? (recommended scientific spine)

State: proposed.

Problem and affected users/tasks: proactive-assistance methods are often ranked offline or against scripted/LLM humans, but robot actions change the environment and human behavior. A method can look helpful offline and add work in closed loop.

Closest prior work with primary evidence: GAP demonstrates the offline/closed-loop ranking problem [V full] but uses an LLM proxy; NIABench is mainly benchmark/simulation plus demonstrations [V full]; the 2016 initiative study and 2024 mixed-initiative work show that human preference and response vary by intervention style [V abstract].

Falsifiable question: **Which evaluation setup—static replay, scripted adaptive human, or LLM-adaptive human—best predicts the ordering and failure modes of proactive-assistance policies with real human partners on a physical tabletop task?**

Hypothesis: static replay will overestimate aggressive proactive policies; an adaptive proxy will better predict net work saved, but will still mispredict subjective intrusiveness and control preference.

Strongest counterexample: GAP may already be sufficient if reviewers accept its LLM proxy as validated. This proposal therefore requires real participants, a physical system, preregistered policy-ranking predictions, and analysis of where proxy and human behavior disagree.

Baseline, control, primary metric, meaningful effect:

- Policies: human-request-only, always-help, calibrated act/no-op, ask/act, and optionally RQ-A.
- Primary metric: rank agreement between each proxy and real-human `Net Assistance Value`, with policy-level confidence intervals.
- Secondary: wrong-help rate, human idle/action time, undo actions, task success, perceived intrusiveness, control preference, and trust calibration.
- Meaningful result: a reproducible ranking reversal or a clear proxy whose rank agreement is materially higher than static replay; exact correlation/effect thresholds require a power simulation before adoption.

Cheapest discriminating experiment: preregister predicted rankings for three policies on two short simulated tasks; run a very small ethics-approved physical feasibility pilot to estimate variance and detect whether any ranking reversal exists before powering the study.

Compute/hardware/data/ethics needs and budget: modest simulation/LLM inference; SO-101; participant approval, consent, and privacy plan. This is more human-study dependent than RQ-A's simulation gate but needs less novel robot learning.

Failure/pivot criteria: stop if tasks are too easy to separate policies, proxy variability overwhelms policy effects, or ethics timing cannot support a powered study. The remaining artifact can become a benchmark methodology note rather than an IROS claim.

## RQ-C — Longitudinal personalization of the help boundary (high-risk alternative)

State: proposed, not recommended for the March 2027 schedule.

Falsifiable question: **Can a robot personalize its help/ask/refrain boundary from interaction history while preserving task performance and user agency better than a population policy?**

Closest counterexamples: PACT already uses cross-day history with simulated humans; GAP learns routines from passive observation; mixed-initiative Bayesian adaptation models willingness to comply. A contribution would require real longitudinal users and a richer preference/skill model, making it scientifically attractive but operationally risky.

Cheapest discriminating experiment: simulation with preference drift and held-out human profiles. Do not proceed to longitudinal collection without an ethics route, retention plan, and a clear advantage over RQ-A/B.

## Recommendation

Use **RQ-B as the paper's scientific spine** and **RQ-A as the optional method**. This yields a valuable result even if the new policy fails: the team can report when static, scripted, and LLM-adaptive evaluations do or do not predict real collaboration. It also directly answers an author-stated limitation in the closest September 2026 framework.

Do not adopt this recommendation yet. The three authors should first decide whether they want a human-study-centered systematic paper, whether an ethics route is available immediately, and whether they are willing to narrow the application to a controlled tabletop collaboration task.

## Primary links inspected

- https://doi.org/10.1145/3797264
- https://arxiv.org/html/2609.28910v1
- https://arxiv.org/html/2605.01368v1
- https://arxiv.org/html/2605.24350v1
- https://arxiv.org/abs/2512.04453
- https://arxiv.org/html/2610.08344v2
- https://ieeexplore.ieee.org/document/10801517
- https://ieeexplore.ieee.org/document/7451735
- https://arxiv.org/abs/2403.16178
- https://arxiv.org/abs/2104.06556
- https://ieeexplore.ieee.org/document/11696882
