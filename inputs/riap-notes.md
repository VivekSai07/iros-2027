# RIAP full text — notes from the PDF the user supplied (63_RIAP_Risk_Aware_Incremental.pdf), 2026-10-18
Status flags: [V-user] = read in the full text supplied by the user. The PDF itself is not committed.

**What it is.** Banerjee and Krishna (IIIT Hyderabad; TCS Research), *RIAP: Risk-Aware Incremental Action Policy for Physical Commitment from Partial Speech*. It is a **NeurIPS 2026 workshop paper** (Real-Time Conversational Agents), not a main-track paper [V-user].

**Method.** A hand-specified decision policy (no learned model) that picks ACT / WAIT / DEFER from a belief over 16 actions and a state-dependent false-commitment cost. Each ACT is a *one-shot motor command* (9 mobile, 7 arm actions) [V-user].

**Evidence.**
- The 8,160 trials are **controlled semantic-evidence replay**: synthetic traces, **no recorded speech, no physics simulation, no human participants** (§4) [V-user]. So "8,160 simulation replays" in the abstract does NOT mean physical manipulation.
- Unsafe commits 27.5% -> 1.6% is RIAP vs the **State-threshold** baseline on those synthetic traces; revision recovery 60.6% is also replay (self-corrections that arrive *before* a commit) [V-user].
- The 30-participant study: browser PyBullet **mobile-base** tasks, voluntary lab colleagues, no compensation, no IRB. It compares **system bundles** (RIAP has a Silero VAD gate; State-threshold does not), so it does not isolate the commitment rule. Ratings only (1-7 scale, six items); no metric-to-rating analysis [V-user].
- Code and reproduction scripts: "planned to be released ... post internal permissions", i.e. not released [V-user].
- Authors' own limitations: no recorded speech or hardware validation yet; **WAIT only defers new command initiation, it does not brake motion already in progress**; "dynamic command preemption" is listed as future work [V-user].
- The authors state that Gemini 3.1 Pro was used for coding, editing and polishing.

**Consequences for us.**
1. RIAP does **not** handle a correction that arrives after motion has started, so it does not scoop G1 or G2. The earlier worry (G1 §6: "top-3 competitor if it simulates manipulation physics with spoken revisions") is resolved: it does not.
2. It still covers "commit timing as a decision variable" (G3, already invalidated) and a hazard-cost formulation we can cite.
3. Reusable ideas: false-commit cost with reversibility and state hazard features; metrics AAT (anticipation time), unsafe-commit rate, revision recovery; matched-risk comparison against threshold sweeps.
4. Our positioning table must not say RIAP has "N=30 with revision recovery in manipulation": the human study measures only subjective ratings of a mobile-base browser task.
