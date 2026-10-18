# Research map: what is covered, what is missing, where to focus, how to build it

Written 2026-10-18 after Feynman passes G1, G2, G4, strategy comparison, and SocialVLA/Causeway full-text summaries (all in `outputs/`). Diagrams are **synthesis** of those reports; the evidence and [V]/[S]/[U] flags live in the reports, not here. View diagrams with VS Code's Markdown Preview (Mermaid support) or on GitHub.

Sources for each claim: G1 = `outputs/g1-interruption-benchmark-novelty.md`, G2 = `outputs/g2-midmotion-repair-novelty.md` (partial delivery, verified), G4 = `outputs/g4-fluency-metrics-validity.md` (partial, fixes not applied), CMP = `outputs/midmotion-instruction-handling-strategies.md` (partial, unverified), SV = `outputs/socialvla-summary.md`, CW = `outputs/causeway-summary.md`.

---
## 1. What is covered vs missing (the five G1 properties)

Each of the five properties already exists somewhere; no single work has all five (G1 §2). Green = precedented, red = nobody found.

```mermaid
flowchart LR
  subgraph P["Five properties of our target benchmark"]
    P1["Spoken audio interruption"]
    P2["Timed relative to motion phase"]
    P3["Real manipulation physics"]
    P4["Physical failure taxonomy and repair metrics"]
    P5["Metrics validated against human ratings"]
  end
  P1 --- E1["ELLSA, VITA-E, SocialVLA, Premover, MIRA"]
  P2 --- E2["Causeway 3 timings, LIBERO-MAX paired events, MAIL-Bench stages"]
  P3 --- E3["ELLSA sim, VITA-E real humanoid, SocialVLA, ARMS, Yu and Qiu SO-101"]
  P4 --- E4["EchoChain speech only, RoboRecover Stage x Deviation, ARMS text metrics"]
  P5 --- E5["SocialVLA n=15 detection, RIAP N=30 UX, Song 2607.00530 n=24 low-cost arm"]
  P1 -.-> X["NO WORK COMBINES ALL FIVE<br/>residual motion and retraction cost: not measured anywhere<br/>backchannel false stops during manipulation: not measured<br/>metric to fluency validity for interruptions: not found"]
  P2 -.-> X
  P3 -.-> X
  P4 -.-> X
  P5 -.-> X
  classDef have fill:#d8f0d8,stroke:#2e7d32,color:#000
  classDef gap fill:#ffd9d9,stroke:#c62828,color:#000
  class E1,E2,E3,E4,E5 have
  class X gap
```

## 2. Gap status after this pass (what changed)

```mermaid
flowchart TD
  G1["G1 Benchmark"] --> G1s["OPEN, narrowed to a conjunction<br/>spoken x phase-anchored x manipulation x repair taxonomy x validity<br/>scoop risk HIGH: 11 adjacent papers 21 Sep to 14 Oct"]
  G2["G2 Mid-motion repair"] --> G2s["BROAD CLAIM CLOSED<br/>SwitchVLA, ReSteer, Causeway switch text instructions without retract<br/>NARROW WEDGE OPEN: speech-triggered, prefix-aware in-flight chunk retargeting on SmolVLA"]
  G4["G4 Validity"] --> G4s["OPEN, must be scoped narrower<br/>Song 2607.00530 already ran n=24 spoken-command study on a low-cost arm<br/>Hoffman metrics correlate weakly, abs r at most 0.123"]
  G3["G3 Commit timing"] --> G3s["INVALIDATED earlier: RIAP, Premover"]
  classDef open fill:#fff3cd,stroke:#b8860b,color:#000
  classDef closed fill:#ffd9d9,stroke:#c62828,color:#000
  class G1s,G4s,G2s open
  class G3s closed
```

## 3. Where research can focus: options and recommendation

Recommendation (inference): **one paper = G1 benchmark as the spine, G2 narrow wedge as the method, G4 trial-level study as validation.** If scooped on the benchmark, the study-heavy variant moves to ICRA 2028. A+B stays the hardware hedge.

```mermaid
flowchart TD
  S["Team decision due about 24 Oct"] --> H1["H1 Say it mid-motion<br/>benchmark + method + study"]
  S --> H2["H2 Knows when NOT to help"]
  S --> AB["A+B precision plug-in plus endurance"]
  H1 --> F1["Focus 1: Benchmark<br/>G1 narrowed"]
  H1 --> F2["Focus 2: Method wedge<br/>G2 narrowed"]
  H1 --> F3["Focus 3: Trial-level human study<br/>G4 narrowed"]
  F1 --> R1["Risk: Skoltech group SocialVLA + JitterVLA could merge into G1"]
  F2 --> R2["Risk: task islands, instruction effect fades near contact<br/>and LeRobot may ship continuous retargeting"]
  F3 --> R3["Risk: ethics timeline, underpowered if per-participant correlation"]
  H2 --> Q2["Partly covered, heavy compute and labeling"]
  AB --> Q3["Least crowded, needs repeatability go/no-go"]
  R1 --> FB["Fallback: ICRA 2028 deadline about 16 Aug 2027"]
  R2 --> FB
  R3 --> FB
```

---
## 4. Implementation structure per focus

### Focus 1 — Benchmark (G1). Build first; sim-first, then real SO-101.

Design borrowed from Causeway (timing grid, success relative to solo, Reach and Finish-given-Reach, same/cross-object strata) and SocialVLA (hold criterion, latency decomposition). Added by us: audio overlap, non-permanent interruption types, motion-quality metrics, human validation.

```mermaid
flowchart LR
  subgraph GEN["Scenario generator"]
    T["Task pairs A to B<br/>same-object and cross-object strata"]
    O["Onset scheduler<br/>by STATE not step count:<br/>approach, grasp, transport, place<br/>hand-object distance, gripper state"]
    U["Utterance bank<br/>target change, constraint, speed or manner,<br/>cancel, backchannel, self-correction"]
  end
  subgraph AUD["Audio"]
    TTS["Voice-cloned TTS users"]
    HUM["Real human speakers"]
  end
  subgraph RUN["Execution under test"]
    POL["Policy: SmolVLA, ACT<br/>LeRobot async stack"]
    HND["Interruption handler under test<br/>B1 to B6 baselines, our method"]
    ENV["MuJoCo or Isaac sim, then real SO-101"]
  end
  subgraph MET["Metrics"]
    M1["Switch success relative to solo task rate"]
    M2["Reach, Finish given Reach"]
    M3["Residual motion after onset, retraction distance"]
    M4["Onset to motion-change latency, jerk discontinuity"]
    M5["False barge-in rate on backchannel and off-target speech"]
  end
  CTRL["Controls: bare text switch, state-placement reference<br/>separates speech failure from task-island failure"]
  T --> O --> U --> TTS --> POL
  U --> HUM --> POL
  POL --> HND --> ENV --> MET
  CTRL -.-> MET
  MET --> TAX["Failure taxonomy labels<br/>inertia, amnesia, displacement,<br/>spurious halt, wrong-object commit"]
```

Planned repo layout (proposal; nothing built yet):

```
benchmark/
  scenarios/      # task pairs, onset rules, utterance bank (YAML)
  audio/          # TTS render + human recording protocol
  harness/        # runs policy + handler, logs joint traces + audio timestamps
  metrics/        # residual motion, retraction, jerk, latency, false-barge-in
  taxonomy/       # label rules + annotator guide
  sim/            # MuJoCo / Isaac scenes (pick-place with 2 objects, 2 bowls)
```

### Focus 2 — Method wedge (G2). Narrow: speech-triggered, prefix-aware in-flight retargeting on SmolVLA.

All four properties must hold together to be novel (G2 §5): speech overlaps motion, no hold or retract, in-flight chunk repair with a latency-bounded committed prefix, low-cost SmolVLA stack, plus physical-continuity evaluation.

```mermaid
flowchart LR
  MIC["Microphone"] --> ASR["Streaming ASR<br/>faster-whisper"]
  MIC --> TURN["Turn and backchannel model<br/>Easy Turn or VAP"]
  ASR --> PARSE["Small LLM<br/>state-update parse:<br/>target, constraint, cancel"]
  TURN --> GATE{"Interrupt or ignore?"}
  PARSE --> GATE
  GATE -->|ignore backchannel| KEEP["Continue current chunk"]
  GATE -->|interrupt| TRUNC["Truncate queued chunk<br/>keep k = remaining inference steps"]
  TRUNC --> RTC["Re-denoise under new instruction<br/>RTC-style guidance over committed prefix only<br/>SmolVLA flow head"]
  RTC --> ARM["SO-101 follower arm"]
  KEEP --> ARM
  ARM --> LOG["Joint traces for metrics"]
  RISK["Known risks: prefix biases toward old intent in pi-R2<br/>instruction influence fades near contact in Causeway"] -.-> RTC
```

Baselines to implement (G2 §6): B1 hold-and-refresh (LeRobot `set_task`, exists), B2 bare switch, B3 truncate + fresh chunk without RTC, B4 retract-to-home (VITA-E style), B5 step-boundary wait (Hi Robot/CIRRA style), B6 ReSteer-style switch-data fine-tune. Optional: B7 Causeway write (high effort, SmolVLA only), B8 ACT checkpoint switch.
Ablation: committed-prefix `keep` in {0, 1x, 2x turnaround}.
Constraint: ACT has no language input, so instruction-triggered repair applies to SmolVLA; ACT only serves as a motion-quality or blending baseline.

### Focus 3 — Trial-level human study (G4)

Per-participant correlation is underpowered at n=18 to 39 (r near 0.12 would need about 543). Use many episodes per participant (G4 §1 item 6: N=24, 8 trials each, within-r 0.3 gives simulated power 0.98).

```mermaid
flowchart TD
  P["Recruit N about 24, within-subject<br/>ethics route started now"] --> C["Conditions: baselines B1, B4, B5 vs our method"]
  C --> E["About 8 interruption episodes per participant<br/>phase-anchored onsets, mixed utterance types"]
  E --> OBJ["Objective: Hoffman H-IDLE, R-IDLE, C-ACT, F-DEL per turn<br/>plus our benchmark metrics"]
  E --> SUB["Per-episode micro-rating, end-of-condition PMQ and SUS"]
  OBJ --> STAT["Mixed model or repeated-measures correlation<br/>benchmark metric to rating"]
  SUB --> STAT
  STAT --> OUT["Claim: which benchmark metrics predict perceived fluency<br/>NOT the claim: first spoken-command study on a low-cost arm"]
```

---
## 5. Timeline to 1 March 2027 (proposal, dates from `02-iros-2027-constraints.md`)

```mermaid
gantt
  dateFormat YYYY-MM-DD
  title IROS 2027 plan, deadline 1 Mar 2027
  section Decide
  Direction choice and hedge sprint   :a1, 2026-10-18, 2026-10-24
  Full-text reads LIBERO-MAX, RIAP    :a2, 2026-10-19, 2026-10-26
  section Build
  Scenario generator and metrics sim  :b1, 2026-10-26, 2026-11-30
  LeRobot async plus streaming ASR demo :b2, 2026-10-26, 2026-11-23
  Baselines B1 to B5                  :b3, 2026-11-23, 2026-12-21
  section Method
  Prefix retargeting on SmolVLA       :c1, 2026-12-01, 2027-01-15
  section Evaluate
  Real SO-101 experiments             :d1, 2027-01-04, 2027-02-05
  Ethics approval and pilot           :d2, 2026-11-01, 2027-01-15
  Human study                         :d3, 2027-01-18, 2027-02-12
  section Write
  Freeze experiments                  :milestone, 2027-02-12, 0d
  Writing and submission              :e1, 2027-02-01, 2027-03-01
```

## 6. Open items this pass created
- Read full texts: LIBERO-MAX (verify where the paired protocol originates), RIAP (physics and speech?), ARMS (spoken?), Song et al. 2607.00530.
- G2, G4 and the comparison are now complete (see iteration 7). Pending: rewrite of `06-paper-story.md` per `outputs/paper-story-review.md`; RTC-vs-LeRobot `/audit` not run.
- Blocked, user action: NeurIPS 2026 RTCA workshop accepted list (OpenReview JS page); ELLSA GitHub; RIAP full text.
- Verify claim in G2 that LeRobot `set_task` is stop-based by running it ourselves on SO-101 (supervisor present, boundaries rule 1).
