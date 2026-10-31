# G1 novelty re-check: is there a speech-interruption benchmark for manipulation with a physical failure taxonomy?

Citation convention: every arXiv ID in this document is a citation to https://arxiv.org/abs/<ID> (resolved via the arXiv export API on 2026-10-18 unless marked otherwise). Non-arXiv sources are numbered [W1]–[W4] and listed under Sources.

Date: 2026-10-18 · Scope: arXiv/alphaXiv, Semantic Scholar/OpenAlex, NeurIPS virtual site, GitHub, web · Status flags: [V] verified from primary page/abstract/full text in this pass, [S] secondary only, [U] unverified.

## Executive summary

- **Verdict: G1 is still open, but only as a conjunction, and the window is closing.** I found no benchmark, sim or real, that does all five of these together: (1) puts **spoken** interruptions on top of (2) **ongoing manipulation**, (3) **anchors the interruption in time** to the motion phase, (4) scores the outcome with a **physical failure taxonomy** (residual motion, retraction, spurious halt, wrong-object commit) and repair metrics, and (5) **validates those metrics against human judgement**. Every component already exists somewhere. Only the combination is unclaimed.
- **The gap narrowed a lot in late 2026-09 and early 2026-10.** Eleven adjacent papers appeared between 2026-09-21 and 2026-10-14 (arXiv dates): MIRA, ARMS, RoboRecover, Causeway, MAIL-Bench, LIBERO-MAX, SocialVLA, Kennington et al., JitterVLA, RASSG and EarlyCommit. Together they cover switch timing, mid-task-event paired protocols, interruption-survival metrics, speech barge-in on a physical robot, false-stop counts and motion-quality replay.
- **Nearest competitor overall: SocialVLA (2610.02360).** It has real human vocal reactions and stop phrases, real manipulation (Unitree G1), latency from reaction onset to hold, a false-stop count, and 15+1 participants. It is a *detector/gateway*, not a benchmark. Its trigger is a reaction to a failure, not an instruction-bearing correction, and it stops ("hold") instead of repairing. **Nearest benchmark protocol: Causeway (2609.30913) plus LIBERO-MAX (2609.36518).** They use text instruction switches at three switch timings and a paired with/without mid-task-event protocol. G1 has to cite them and borrow their protocol rather than claim it.
- **Correction to our own notes.** RIAP's NeurIPS abstract reports unsafe commitments falling **from 27.5% to 1.6%**, over **8,160 simulation replays**. `04-literature-map.md` says "0% unsafe commits".

## 1. What exactly G1 claims (restated for testing)

From `05-gap-analysis.md`: a time-anchored, speech-overlap interruption benchmark for **manipulation**, with a **physical** failure taxonomy (physical analogs of EchoChain's contextual inertia / interruption amnesia / objective displacement, plus residual motion, retraction penalty, spurious halt), and metrics including repair latency, trajectory continuity, post-repair success and false-barge-in rate.

I decomposed this into five testable properties, which are the columns of the matrix below:

| Column | Meaning |
|---|---|
| Speech audio | Interruption is delivered as audio (TTS or human), not text |
| Overlap timing | Interruption onset is controlled or measured relative to ongoing robot motion (or speech, for speech-only work) |
| Manipulation physics | Robot is manipulating objects (sim physics or real), not gesturing or dialogue-only |
| Failure taxonomy | Named categories of interruption-handling failure (✓ = interruption-specific; ~ = generic deviation or behaviour categories) |
| Human validation | Human participants or human ratings used to validate behaviour or metrics |

## 2. Coverage matrix

Legend: ✓ present · ~ partial · ✗ absent · ? not determinable from what was read.

| Work (ID, date) | Type | Speech audio | Overlap timing | Manipulation physics | Failure taxonomy | Human validation | Status |
|---|---|---|---|---|---|---|---|
| **EchoChain** (2604.16456, Apr 2026) | Benchmark | ✓ | ✓ injected "at a standardized point relative to assistant speech onset" | ✗ voice only | ✓ contextual inertia, interruption amnesia, objective displacement | ? | [V abstract] |
| **Full-Duplex-Bench v1** (2503.04721) | Benchmark | ✓ | ~ pause/backchannel/turn-taking/interruption events | ✗ | ~ behaviour categories | ? | [V metadata+abstract] |
| **Full-Duplex-Bench v1.5** (2507.23159, ICASSP 2026) | Benchmark | ✓ | ✓ four overlap scenarios (interruption, backchannel, talking to others, background speech) | ✗ | ~ | ? (fully automated) | [V abstract] |
| **Full-Duplex-Bench v2** (2510.07838, ACL 2026) | Benchmark | ✓ | ~ Fast/Slow pacing, automated examiner | ✗ | ~ task families incl. correction | ? | [V abstract] |
| **Talking Turns** (2503.01174, ICLR 2025) | Benchmark | ✓ | ✓ turn-taking events [S] | ✗ | ~ [S] | ? | [V metadata]; contents [S] |
| **TurnBench** (2608.25218) | Benchmark | ✓ | ✓ | ✗ | ~ | ? | [V metadata]; contents [S] |
| **Duplex Cue** "Continue, Adapt, or Yield" (2609.13117, Sep 2026) | Evaluation | ✓ real conversations | ✓ cue onset while speaker active | ✗ | ✓ continue / adapt / yield | ✓ 300 human-confirmed cues; human vs model | [V abstract] |
| **RASSG / ReCAST** (2610.14659, Oct 2026) | Method + eval | ✓ | ✓ controlled execution clock | ✗ software tools, but "irreversible effects" | ~ stale execution | ✗ | [V abstract] |
| **ELLSA** action barge-in (2510.16756, ICLR 2026) | System + eval | ✓ TTS (CosyVoice2), 10 fixed phrases | ~ random 2–8 s after instruction, not phase-anchored | ✓ sim (LIBERO) | ✗ binary success (94.3%) | ✗ | [V full text] |
| **VITA-E** (2510.21817) | System + eval | ✓ | ✗ not reported as controlled | ✓ real humanoid (Fourier GR2) | ✗ success rates over 30 trials | ✗ | [V full text] |
| **MIRA** (2609.24547, Sep 2026) | System + eval | ✓ live | ~ preemption measured from speech_started (466 ms P50) | ✗ co-speech gestures and social behaviours only | ~ arbiter IGNORE/REPLY/INTERRUPT_AND_REPLY | ✗ ("human-subject studies ... next step") | [V full text] |
| **SocialVLA** (2610.02360, Oct 2026) | Detector/gateway + eval | ✓ paralinguistic audio, stop phrases, verbal corrections | ✓ onset-to-hold 1.021 s, gate-to-hold 336 ms | ✓ real (Unitree G1) | ~ false-stop episodes (100 → 57); intervention-worthy vs not | ✓ 15 participants + 1 prospective | [V abstract] |
| **RIAP** (NeurIPS 2026 poster 162424) [W1] | Policy + eval | ? (conversational cues; "mid-utterance revisions") | ✓ act/wait/defer over incremental intent | ? "simulation replays"; physics unclear | ~ unsafe commitments | ✓ 30 participants | [V abstract]; details [U] |
| **Premover** (2605.12160 v2) | Method | ✓ speech + online transcription | ✓ acts during instruction delivery | ✓ real SO-101 + LIBERO | ✗ | ? | [V abstract] |
| **EarlyCommit** (2610.20531, Oct 2026) | Tool | ✓ streaming speech front end | ✓ word-by-word | ~ object commitment, not motion | ~ wrong-object commit risk (1−τ) | ✗ | [V abstract] |
| **Causeway** (2609.30913, Sep 2026) | Method + protocol | ✗ text | ✓ **three switch timings** | ✓ LIBERO-Goal/Object + real xArm | ~ "task islands", handoff-neighbourhood rate | ✗ | [V abstract] |
| **SwitchVLA** (2506.03574) | Method | ✗ text | ~ execution-aware, contact phases | ✓ sim + real | ✗ | ? ("interaction naturalness" claimed) | [V abstract] |
| **ARMS / Watch-Recall-Act** (2609.28429, Oct 2026) | Method + dataset/benchmark | ✗ text guards/recall | ~ instructions arrive mid-stream; not phase-controlled | ✓ real dual-arm (Cobot Magic) | ~ per-family metrics: cross-interruption recall, foreground-continuation, non-interference | ✗ (teleop oracle as ceiling only) | [V full text] |
| **CIRRA / CHIRP** (2610.08862, Oct 2026) | Method + text benchmark | ✗ | ~ "interrupts ongoing skills at the correct moment" | ~ plan-level; G1 humanoid demo | ✗ | ? | [V abstract] |
| **LIBERO-MAX** (2609.36518, Sep 2026) | Benchmark | ✗ | ✓ paired mid-task events, pre-event actions fixed | ✓ sim | ~ 8 change types (world events) | ✗ | [V abstract] |
| **RoboRecover** (2609.28952, Sep 2026) | Benchmark | ✗ | ~ recovery point via action-prefix replay | ✓ sim (RoboTwin, LIBERO) | ~ Stage × Deviation (incl. **Wrong Target**) | ✗ | [V full text] |
| **MAIL-Bench** (2609.35003, Sep 2026) | Benchmark | ✗ (camera-loss "interruptions") | ✓ multiple stages of reference trajectory | ✓ sim + real AgiBot G2 | ✗ | ✗ | [V abstract] |
| **One Word, Different Action** (2609.05260, Sep 2026) | Benchmark | ✗ | ✗ not mid-execution | ~ fixed physical anchors, finite decisions, evaluated with text LLMs | ~ invariance / sensitivity | ✗ | [V full text] |
| **Kennington et al.** (2610.08733, Oct 2026) | Benchmark *proposal* | ✓ (planned) | ? | ✗ base task (manipulation only a proposed extension) | ✗ (interruptions/barge-ins listed as possible metrics) | planned | [V full text] |
| **JitterVLA** (2610.13628, Oct 2026) | Replay benchmark | ✗ | ~ command-arrival traces/delays | ✓ VLA pipelines + real UR3 | ~ jerk/discontinuity | ✗ (20 people's hand trajectories are inputs, not ratings) | [V abstract] |
| **NIABench** (2605.01368) | Benchmark | ✗ | ✓ "when to act" (robot must *avoid* interrupting) | ~ sim | ✗ | ? | [V abstract] |
| **YAY Robot / RT-H / RACER** (2403.12910 / 2403.01823 / 2409.14674) | Methods | ~ verbal corrections (YAY) | ✗ | ✓ | ✗ | ~ humans give corrections | [V abstract] |
| **LIBERO-PRO / LIBERO-Plus** (2510.03827 / 2510.13626) | Benchmarks | ✗ | ✗ pre-execution perturbations | ✓ sim | ~ perturbation dimensions | ✗ | [V abstract] |
| **SafeVLA-Bench 3.0** (GitHub Jatshi) [W2] | Benchmark | ✓ spoken instruction under SNR noise | ✗ instruction before acting | ✓ sim (ManiSkill) | ~ execute/clarify/stop | not found | [V README, truncated] |
| **Yu & Qiu, SO-101 failure/recovery** (2606.08881, Jun 2026) | Benchmark | ✗ | ✗ | ✓ real SO-101 (π0.5, SmolVLA, Wall-X, ACT) | ✓ structured failure taxonomy (not interruption) | ? | [V abstract] |

**Reading the matrix.** No row has ✓ in all five columns.

- Rows with speech audio *and* manipulation physics: ELLSA, VITA-E, SocialVLA, Premover, SafeVLA-Bench.
- Of those, only SocialVLA also has measured overlap timing and human data. Its taxonomy is limited to false stops versus intervention-worthy episodes, and it evaluates *holding*, not repair.
- Rows with a timing variable *and* manipulation (Causeway, LIBERO-MAX, MAIL-Bench) all use text or non-language events.

## 3. How the proposed physical failure modes map onto existing work

This table maps G1's *proposed* categories (our design, not evidence) to the nearest existing measurement. It shows what G1 must cite and what is genuinely new.

| Proposed G1 failure mode | Nearest existing measurement | Covered? |
|---|---|---|
| Residual motion (robot keeps moving after a valid interruption) | MIRA bounds committed motion to a 0.50 s prefix and reports speech→abort-command latency (466 ms), but does not measure post-command motion. SocialVLA reports gate-to-physical-hold 336 ms. | ~ latency yes; displacement/energy after onset **not measured anywhere found** |
| Retraction penalty (cost of undoing progress) | VITA-E switches by "returns the robot to the initial pose" via an inverse action stack. That is the behaviour, not a metric. | **Not measured** |
| Spurious halt / false barge-in (stops on backchannel or off-target speech) | SocialVLA false-stop episodes (100 → 57). FDB v1.5 backchannel and "talking to others" scenarios (speech only). ELLSA does not handle backchannels (its own limitation). | ~ counted for reactions (SocialVLA); **not for backchannels during manipulation** |
| Wrong-object commit | RoboRecover "Wrong Target" deviation type (no language). EarlyCommit accepted risk 1−τ (pre-motion). RASSG stale-execution rate (software tools). | ~ analogs only |
| Interruption amnesia (forgets the correction or prior context) | ARMS cross-interruption recall (text). EchoChain (speech only). | ~ text-manipulation and speech-only analogs |
| Objective displacement (abandons the original goal when it should resume) | ARMS foreground-continuation rate (FG-Res). EchoChain (speech only). | ~ text-manipulation analog |
| Contextual inertia (keeps executing the old plan) | ELLSA failed-to-stop cases (100 − 94.3 = 5.7% of interruptive commands). Causeway bare-switch success 3–26%. | ~ as success rates, not as a named category |
| Trajectory continuity | JitterVLA p99 jerk (no interruption). RTC/async-chunking literature. | ~ metric exists, not tied to interruptions |
| Post-repair success | Causeway switch success. ARMS EAS. RoboRecover RSR. | ~ text/world-event analogs |
| Human-validated metric | SocialVLA (detector accuracy on participants), RIAP (N=30 subjective UX), Duplex Cue (human vs model, speech). | **No work found that correlates benchmark metrics with human-rated fluency for manipulation interruptions** |

Inference: the parts of G1 that remain novel are **(a)** residual-motion and retraction metrics conditioned on interruption onset, **(b)** spurious halts triggered by *backchannels and self-corrections during manipulation*, **(c)** naming EchoChain's three categories as physical failure modes in one taxonomy, **(d)** controlled time-anchoring of *spoken* corrections to the motion phase (approach / grasp / transport / place), and **(e)** a validity study. Items (d) and (e) are the most defensible differentiators. Each column on its own is now precedented.

## 4. Verdict

**G1 survives in narrowed form.** A defensible claim would read roughly: "the first benchmark that evaluates *spoken* corrections overlapping *manipulation*, time-anchored to motion phase, with a physical repair taxonomy and metrics validated against human fluency ratings." Claims we can no longer make:

- "First to evaluate interruption timing in manipulation." Causeway uses three switch timings; LIBERO-MAX uses paired mid-task events; MAIL-Bench interrupts at multiple trajectory stages.
- "First manipulation benchmark for interruptions." ARMS's dataset scores cross-interruption recall and foreground continuation on a real robot (text). MAIL-Bench uses the word "interruption" for camera loss.
- "First to measure false stops / latency with real users." SocialVLA has 15 participants, false-stop counts and onset-to-hold latency.
- "First failure taxonomy on SO-101." Yu & Qiu (2606.08881) built a failure/recovery taxonomy benchmark on SO-101 with SmolVLA and ACT, the same platform and policies we use.
- "First speech barge-in during manipulation." ELLSA and VITA-E (already invalidated).

**Scoop risk: high.** Inference: the Skoltech group of Tsetserukou et al. is co-author on both SocialVLA (reaction-triggered VLA interruption with users) and JitterVLA (motion-quality replay for VLA HRI). Combining the two would land very close to G1. The NeurIPS 2026 RTCA workshop [W3] lists "interruption handling" and "datasets and benchmarks for interactive evaluation" as topics. Submissions closed on 10 Sep 2026 and notifications went out on 29 Sep. Its accepted papers could not be checked (OpenReview page blocked, see below).

## 5. Nearest competitor and how to differentiate

| Rank | Competitor | Why it is near | How G1 must differ |
|---|---|---|---|
| 1 | **SocialVLA** (2610.02360) | Most matrix columns: real audio, real manipulation, latency, false stops, participants | G1 is a reproducible **benchmark** (sim + real) rather than a detector. Its interruptions are **instruction-bearing** (target change, constraint, cancel, self-correction, backchannel), not failure reactions. It scores **repair** (post-repair success, continuity, retraction, residual motion) instead of only hold. It **controls onset timing by motion phase**. |
| 2 | **Causeway** (2609.30913) + **LIBERO-MAX** (2609.36518) | Timing-as-variable switch protocol and paired event protocol on LIBERO with several VLAs | Adopt the paired with/without-interruption design and cite it. Differ on **speech audio** (TTS + human, incl. disfluency/backchannel), **overlap** (speech and motion co-occur rather than an instantaneous text swap), and the **physical taxonomy and human validation**. |
| 3 | **ARMS** (2609.28429) | Real-robot interruption metrics (cross-interruption recall, foreground continuation) | Cite as the text analog of amnesia/displacement. G1 adds speech, timing control, and residual/retraction metrics. |
| 4 | **ELLSA** (2510.16756) | Only speech barge-in evaluated on a manipulation benchmark | Its evaluation is binary stop success on 10 fixed TTS phrases at random 2–8 s offsets in sim, with no backchannels. G1 generalizes this into a taxonomy, adds repair, and adds real robot plus humans. |

## 6. Caveats and disagreements

- Most of the 2026-09/10 papers are v1 preprints. Their numbers are as reported and were not reproduced.
- Several rows are abstract-level only (Causeway, LIBERO-MAX, SocialVLA, RIAP, CIRRA, JitterVLA, MAIL-Bench). A full-text read could reveal timing controls or human ratings that would change a cell. SocialVLA and Causeway are the two whose full text matters most.
- "Human validation" is marked "?" for FDB, Talking Turns and TurnBench because their abstracts were not checked for human-rating correlation. This does not affect the verdict, since none of them involve manipulation.
- RIAP's modality and physics are unclear from the abstract ("conversational cues", "simulation replays"). If RIAP simulates manipulation physics with spoken revisions, it becomes a top-3 competitor. Its full text is not available.
- Terminology clash: MAIL-Bench and LIBERO-MAX use "interruption"/"mid-task event" for sensor loss and world changes. The G1 paper should define "spoken interruption" explicitly to avoid confusion with these.

## 7. Open questions

1. Does SocialVLA's full text include an instruction-revision evaluation (post-hold continuation success, residual motion)? If so, competitor 1 moves closer.
2. What is in RIAP's full paper (physics sim? spoken revisions during motion?)? Needs the camera-ready or a preprint.
3. Which NeurIPS 2026 RTCA workshop papers involve robots or manipulation? Blocked (OpenReview is JS-rendered).
4. Is the ELLSA code and barge-in data released? Still pending from D-007 (user check).

## 8. Next steps (recommended)

1. Read the full text of SocialVLA and Causeway (highest leverage).
2. Fix `04-literature-map.md` for the RIAP numbers and add the new rows (ARMS, Causeway, LIBERO-MAX, MIRA, SocialVLA details, Yu & Qiu SO-101, JitterVLA, RASSG, EarlyCommit, Duplex Cue, Kennington).
3. Reframe C1 in `06-paper-story.md` around the conjunction: spoken × phase-anchored × manipulation × repair taxonomy × validity. Drop any "first" claim on timing, interruption-in-manipulation, false-stop measurement, or an SO-101 failure taxonomy.
4. Re-run this check weekly until submission. Suggested keyword alerts: "spoken correction manipulation", "barge-in VLA", "interruption benchmark robot", plus the Skoltech (Tsetserukou) and ELLSA (Tsinghua/ByteDance) groups.

## Blocked sources

- OpenReview group page for NeurIPS 2026 Workshop RTCA: JavaScript-rendered, fetch failed. Not worked around. Needs a manual check by the user.
- ELLSA GitHub (bytedance/SALMONN, ELLSA branch): previously ROBOTS_DISALLOWED (D-007). Not re-attempted.
- RIAP full text: no arXiv or preprint found. Only the NeurIPS virtual abstract page is accessible.
- SafeVLA-Bench README: fetch truncated at 8K characters, so `docs/TECHNICAL_REPORT.md` was not reviewed.

## Sources

arXiv (abs URLs as returned by the arXiv export API on 2026-10-18 unless noted; "alphaXiv" = ID taken from the alphaXiv index, abstract read there):

- EchoChain: A Full-Duplex Benchmark for State-Update Reasoning Under Interruptions (2026) — https://arxiv.org/abs/2604.16456
- Full-Duplex-Bench (ASRU 2025) — https://arxiv.org/abs/2503.04721 (Semantic Scholar metadata)
- Full-Duplex-Bench v1.5 (ICASSP 2026) — https://arxiv.org/abs/2507.23159 (Semantic Scholar metadata)
- Full-Duplex-Bench-v2 (ACL 2026 short) — https://arxiv.org/abs/2510.07838 (Semantic Scholar metadata)
- Talking Turns (ICLR 2025) — https://arxiv.org/abs/2503.01174 (alphaXiv)
- TurnBench (2026) — https://arxiv.org/abs/2608.25218 (alphaXiv)
- Continue, Adapt, or Yield / Duplex Cue (2026) — https://arxiv.org/abs/2609.13117
- RASSG (2026) — https://arxiv.org/abs/2610.14659
- ELLSA: End-to-end Listen, Look, Speak and Act (ICLR 2026) — https://arxiv.org/abs/2510.16756
- VITA-E (2025) — https://arxiv.org/abs/2510.21817
- MIRA (2026) — https://arxiv.org/abs/2609.24547 (alphaXiv full text v2)
- SocialVLA (2026) — https://arxiv.org/abs/2610.02360
- Premover (2026, v2) — https://arxiv.org/abs/2605.12160
- EarlyCommit (2026) — https://arxiv.org/abs/2610.20531
- Causeway (2026) — https://arxiv.org/abs/2609.30913
- SwitchVLA (2025) — https://arxiv.org/abs/2506.03574
- Watch, Recall, Act / ARMS (2026) — https://arxiv.org/abs/2609.28429 (alphaXiv full text v2)
- CIRRA / CHIRP (2026) — https://arxiv.org/abs/2610.08862
- LIBERO-MAX (2026) — https://arxiv.org/abs/2609.36518
- RoboRecover (2026) — https://arxiv.org/abs/2609.28952 (alphaXiv full text)
- MAIL-Bench / Learning to Act under Visual Interruptions (2026) — https://arxiv.org/abs/2609.35003
- One Word, Different Action (2026) — https://arxiv.org/abs/2609.05260 (alphaXiv report)
- Towards an Extensible Benchmark for Spoken Dialogue with Social Robots (2026) — https://arxiv.org/abs/2610.08733 (alphaXiv full text)
- JitterVLA (2026) — https://arxiv.org/abs/2610.13628
- NIABench / Assistance Without Interruption (2026) — https://arxiv.org/abs/2605.01368
- Yell At Your Robot (2024) — https://arxiv.org/abs/2403.12910
- RT-H (2024) — https://arxiv.org/abs/2403.01823
- RACER (2024) — https://arxiv.org/abs/2409.14674 (alphaXiv)
- LIBERO-PRO (2025) — https://arxiv.org/abs/2510.03827 (OpenAlex)
- LIBERO-Plus (2025) — https://arxiv.org/abs/2510.13626 (Semantic Scholar)
- Benchmarking VLA Models on SO-101: Failure and Recovery Analysis (2026) — https://arxiv.org/abs/2606.08881
- SafeStage (2026) — https://arxiv.org/abs/2609.21223 (screened; not in matrix as no interruption/speech)
- ELLSA 2 (2026) — https://arxiv.org/abs/2610.21452 (screened; gestures, no manipulation)
- DuplexSLA (2026) — https://arxiv.org/abs/2605.20755 (screened; tool actions, not physical)

Web:
- [W1] RIAP abstract, NeurIPS 2026 virtual poster 162424 — https://neurips.cc/virtual/2026/poster/162424 (fetched 2026-10-18)
- [W2] SafeVLA-Bench 3.0 README — https://github.com/Jatshi/SafeVLA-Bench (fetched 2026-10-18; truncated)
- [W3] NeurIPS 2026 RTCA workshop site — https://rtcaneurips26.github.io/ (fetched 2026-10-18)
- [W4] NeurIPS 2026 RTCA OpenReview group — https://openreview.net/group?id=NeurIPS.cc%2F2026%2FWorkshop%2FRTCA (BLOCKED: JS-rendered)

Research notes: `outputs/.drafts/g1-interruption-benchmark-novelty-research-direct.md`.
