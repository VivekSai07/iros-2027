# Causeway windowed notes (Tier 2, window=6000, source outputs/.notes/causeway-raw.txt, 41,225 chars, pdftotext of arXiv PDF v1)

## W1 (0–6000)
- Title: "Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies". Authors Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li, Dinesh Manocha (UMD; Shi at USC). arXiv:2609.30913v1 [cs.RO], 25 Sep 2026. [V]
- Setting: "instruction switching": policy begins task A and *permanently* receives instruction ℓB at an intermediate or terminal state. Text instruction swap, no speech. [V]
- "Task islands": states produced by A from which B (reliable from nominal init) can't be initiated; depends on target task + physical state, not elapsed time. [V]
- Relation: ReSteer [6] (state-dependent steerability, trains on generated transitions) — Causeway is complementary: online, training-free recovery after a bare switch fails. [V]
- Finding: accessibility declines near contact and grasp events; new instruction still changes text representation but its effect on decoded action weakens; action-stream representation still locally steerable by state-directed gradient. [V]
- Method: re-entry pose derived from target-task demos; target-directed action objective differentiated through frozen decoder; direction added to action-stream representation; proprioceptive thresholds govern intervention + handoff. No param updates, no new head, no external action generation. [V]
- VLAs: π0.5, OpenVLA-OFT, GR00T N1.5 on LIBERO-Goal ("parallel, flow-matching, and diffusion-based decoders"). 71 cross-object pairs × 3 switch timings; success 3–26% → 47–65%; handoff-neighbourhood rate +42–72 pp. LIBERO-Object + real xArm in Sec. VI. [V]

## W2 (6000–12000)
- Related work: SwitchVLA [7] (trained forward/rollback/advance), ReSteer [6], DeLock [17] (contrastive prompt guidance), activation steering [18–20], Recovery Chaining [22] (learned recovery policy into initiation set). Causeway positions itself "between language-only guidance and external control". [V]
- Formalism: ρ_{A→B}(s) = Pr[G_B(τ)=1 | s, ℓB] (Eq. 1), reference ρ_B from scratch. Task island = state where ρ_{A→B}(s) low while ρ_B high; defined relative to target task, policy, rollout horizon. [V]
- => Task-switch success = goal predicate G_B holds at some step after permanent switch to ℓB from state s (within horizon). [V]
- Fig. 2: entry-basin tolerance under position/axial-tilt/roll perturbations; bare-switch success after A completes vs exit approach-axis error r = −0.80; A3 hand exits inside the drawer. [V] (figure text partially garbled in extraction)
- Fig. 3-ish escape map: instruction issued at states "Start", "250", "180", "pre", "far pre" for sources A0–A9 vs targets B0–B9 (numbers likely step indices; exact meaning TBD next window). [V partial / interpretation U]
- Object-centric state ξ_B = (p_EE − p_rB, R_EE, g); reference r_B = object before contact, destination after grasp. Orientation world frame since object orientations fixed. [V]

## W3 (12000–18000)
- Fig. 3 escape map (OpenVLA-OFT, LIBERO-Goal): states labelled 250, 180 = hand–object distance in mm; "pre" = pre-grasp; far/pre for the two drawer tasks. Cells = fraction of trials reaching the object of ℓ. |F(s)| = number of instructions with escape rate ≥ 0.5; |F(s)|=1 = "committed" state. [V]
- Entry basin S_B(g): approach segment up to first contact (gripper open) or start of placement segment (holding o_B), expanded with measured tolerances. Executable set F(s) = {ℓ : ξ_ℓ(s) ∈ M_ℓ} (Eq. 3). [V]
- Validation: placing EE directly at pose in S_B and issuing ℓB recovers nominal ρ_B ("Placement", Table I). Returns evaluated against nominal ρ_B, not 100%. [V]
- Tolerances (10 tasks × 4 trials/point): position within 30 mm OK; approach axis ~±20°; roll asymmetric (+0.5 rad no loss, −0.15 rad costs 20 pp); closed gripper at pre-grasp is outside basin. [V]
- Escape map method: roll out closed loop for a fixed horizon under each ℓ, record whether EE reaches target object; "short-horizon reachability agrees with full-length rollouts" in all tested cases. [V]
- At shared initial pose all 10 instructions executable; cross-object instructions drop out as A executes; survivors structured by object identity; non-monotone (A3: 10→2→4) → executability follows state not time. [V]
- Same-object pairs: may survive grasp while grasp/early transport overlap, fail as transport diverges. [V]
- After completion: bare-switch success 3–50% across source tasks, r = −0.80 vs mean exit approach-axis error (31°–98°); A3 hand inside drawer; A7 ends gripper closed. [V]

## W4 (18000–24000)
- "The gate": ‖Δa‖ (mean translational difference between action chunks under ℓA vs ℓB) drops by 1–2 orders of magnitude before contact on all three architectures (Fig. 4a); text-token representation still changes. Gradient direction still produces motion toward B (Fig. 4b, cos ≈ +0.9/+0.95). [V]
- Causeway consumes only proprioception + precomputed re-entry pose T* (from B's demos); every action decoded by frozen policy. [V]
- Write location: one layer L on π0.5 and GR00T N1.5; multiple layers on OpenVLA-OFT. Perturbation δ broadcast to all N action tokens at every decoding step k (Eq. 6); same δ shared across steps/layers. [V]
- Action chunk a ∈ R^{H×7} (xyz + rot increments + gripper). T* chosen by a fixed rule for all pairs/models, no pair-specific tuning. [V]
- Errors e_p = p* − p, e_r = log(R* R^{-1})^∨ (Eq. 5). Per-channel objective J_c, direction ĝ_c = normalized ∇_δ J_c at δ=0 (Eq. 7); position J_p = ⟨ā_xyz, u_p⟩ (Eq. 9). Separate channels: position, approach axis, roll, gripper. On OFT one forward–backward pass. [V]
- Requires white-box gradient access through decoder (inference: needs model internals; relevant for SmolVLA/ACT reuse). [inference]

## W5 (24000–30000)
- Orientation split: e_⊥ (approach direction) and r (signed roll about approach axis); roll gain tapered with proportional band κ and dead-band ε (Eq. 14). Gripper channel: if holding o_A ≠ o_B, open gripper first; if holding o_B use closed-gripper branch. Composition Eq. 15: gripper-only during release, else α_p ĝ_p + α_⊥ ĝ_⊥ + α_r(r) ĝ_r. [V]
- Schedule: write starts AT the instruction switch; pre-pose T0 = p* − d0 ẑ*; switch to p* when |r|<γ or after Nγ steps; dwell ≤ Nd steps in neighborhood (roll off); handoff after dwell or earlier if gripper closed around non-empty grasp 2 consecutive steps inside neighborhood; closure outside neighborhood → reopen. Schedule issues no motor commands. [V]
- Hypotheses H1 islands occur across models/timings; H2 restores via re-entry; H3 neither instruction contrast nor action-level steering sufficient; H4 extends beyond cross-object. [V]
- Benchmark: LIBERO-Goal 90 ordered pairs: 71 cross-object (main), 14 same-object (H4), 5 excluded (A displaces B's target config). Plus LIBERO-Object. [V]
- Policies: benchmark-fine-tuned OpenVLA-OFT (parallel decoding; write layers {8,12,16,20,24,28,30}), π0.5 (flow matching; layer 15), GR00T N1.5 (diffusion; DiT block 16). OFT/GR00T single gain profile; π0.5 three fixed geometry-driven profiles. γ=0.3 rad, Nγ=20, Nd=15 shared. [V]
- **Three switch timings (sim)**: ℓB at step 30 (approach), step 60 (object held in 58–61% of trials), or post-completion ("done"). [V]
- **Trials**: 71 pairs × 3 timings × 8 initial states × 3 rollouts = 5,112 trials/model (arithmetic checked). [V]
- **Metric**: ρ_{A→B}^{(τ)} = E_{s_τ∼p_A^π}[ρ_{A→B}(s_τ)] under standard LIBERO success criteria; i.e., success = B's LIBERO goal predicate after the permanent switch, averaged over the switch-state distribution induced by A at timing τ. All models near-perfect from scratch on targets. Extra metrics: Reach (fraction reaching handoff neighborhood of T*), Fin|R (completion given reach). [V]
- Inference cost (A100-80GB): per-chunk latency 2.5–2.8× (102/75/128 → 253/187/362 ms OFT/π0.5/GR00T), replanning 4.0/5.3/2.8 Hz, +≤4.3 GiB peak; only during re-entry. [V]
- Baselines: Bare switch; CPG (DeLock-style v_A + w(v_B − v_A)); CAA (online activation difference via same write machinery); Action-space steering (Cartesian residual; π0.5 only). Privileged references on OFT: state placement, single-point servo, wrist-first servo. [V]
- "Paired" design here = same ordered A→B pairs, same initial states/timings, bare vs. method. There is no with/without-interruption control arm in this text so far (that design belongs to LIBERO-MAX per our novelty note). [V for what's present; inference re attribution]

## W6 (30000–36000)
- Table I (parse checked by recomputing averages, outputs/.notes/causeway-table-checks.txt): Step30/Step60/After/Avg
  - π0.5: Bare 29.9/22.9/25.1/26.0 (Reach 18.7, Fin|R 58.7); CPG 27.6 avg; CAA 25.0; Action 37.5/21.3/26.6/28.5; Ours 60.9/60.4/63.4/61.6 (Reach 61.0, Fin|R 74.0)
  - OFT: Bare 5.1/2.9/2.2/3.4 (9.3, 25.3); CPG 7.0; CAA 0.8; Ours 77.2/60.5/55.9/64.5 (81.3, 73.7)
  - GR00T: Bare 14.6/11.8/3.4/9.9 (8.7, 45.0); CPG 10.3; CAA 4.6; Ours 67.2/43.3/32.0/47.5 (79.0, 59.3)
  - Privileged (OFT): single-point servo 47.2 avg; wrist-first 73.7; placement 79.2. [V]
- Gains positive for every model/timing/target; +28.6 (GR00T after) to +72.1 (OFT step 30). CPG ≤ +3.6 pp; CAA ≤ bare on average. [V]
- LIBERO-Object: committed-state switch 0% → 57.5% on evaluated pairs. [V]
- **Real xArm**: xArm 6, π0.5 fine-tuned on 30 teleop demos/task, frozen. 4 tasks (button, plate, shelf, corn; solo 80/100/100/80%). 7 ordered pairs (5 cross-object, 2 same-object bowl). **Three real switch points: mid-approach, pre-grasp, post-completion.** 5 trials/cell (→ 210 trials total incl. bare+ours, computed). Pooled bare/ours: approach 42.9/100; pre-grasp 14.3/94.3; after 17.1/82.9; every cell ≥60% with Causeway. Bare failures: stalling or continuing toward source object (Fig. 6). [V]
- Held objects: closed-gripper branch reroutes held bowl plate→shelf without put-down. [V]

## W7 (36000–41225)
- Fig. 6: real chained switching. Top row: each instruction interrupts the previous task mid-execution; last switch reroutes held bowl plate→shelf. Bottom row: instructions issued after each completion. Insets show bare switch failing from same state. [V]
- Conclusion/limitations: depends on task-relative coordinates ξ and demonstration coverage; degrades under unmodeled factors (large scene shifts, in-grasp dynamics); needs per-architecture calibration. Future: embed accessibility into training. [V]
- Refs incl. ReSteer [6], SwitchVLA [7], YAY robot [12], DeLock [17] arXiv:2604.23121, Recovery Chaining [22]. [V]
- **Code release**: no GitHub/project URL anywhere in PDF text; arXiv abs page has no Comments field and no github string (grep, 0 hits). → "no code link found in paper or abs page". External GitHub search not performed (single-source rule). [V absence in these two pages; release status otherwise U]
- No human participants, no speech/audio, no latency-from-instruction metric beyond compute latency, no residual-motion/retraction metric. [V absence in full text]
