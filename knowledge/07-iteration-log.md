# Iteration log (2026-10-13)

| Iter | Focus | What changed |
|---|---|---|
| 1 | Calendar, IROS 2026 stats/awards, Karcini position paper, Rakesh's reading list | Fixed list inaccuracies (Decoupling…=DuplexPO; VoxMind not robotics; "Talking Turns"); confirmed Karcini 2606.06556; set deadline 1 Mar 2027 |
| 2 | Full-duplex/interruption manipulation: ELLSA, VITA-E, EchoChain, SwitchVLA, Hi Robot, RTC, CoRe, VLA-Feedback | Identified stop/retract/wait pattern → candidate gap G2; ELLSA GitHub blocked (ROBOTS_DISALLOWED) |
| 3 | Turn-taking & speech stack: Easy Turn, Talking Turns, TurnBench, Skantze & Irfan, Duplex* family | Feasible cascaded stack found; backchannel handling available off-the-shelf |
| 4 | Incremental HRI & H2 prior art: Tufts/TUW, Kennington survey, NIABench, PACT, Attentive Support, MICoBot | Mapped H2 coverage; benchmark gap G1 emerged |
| 5 | Novelty re-check against Oct 2026 arXiv: Premover, RIAP, SocialVLA, CMU HRI, ExpressMM, One Word | **Invalidated G3**; narrowed to G1+G2+G4 |

## Tool notes
- WebFetch returns full text (not prompt-targeted) — prefer abstract pages/targeted searches.
- WebSearch is US-only.
- Blocked: ELLSA GitHub (robots). Paywalled: IEEE Xplore/ACM DL versions.

## Iteration 6 — 2026-10-18 — G1 novelty re-check (Feynman deep research, direct mode)
- 23 paper-index queries (alphaXiv, Semantic Scholar, OpenAlex, arXiv API) + 3 web queries; terms in `outputs/.drafts/g1-interruption-benchmark-novelty-research-direct.md`.
- Result: G1 **still open only as a conjunction** (spoken × phase-anchored × manipulation × physical repair taxonomy × human validation). 11 adjacent papers appeared 2026-09-21 → 2026-10-14. Nearest competitor SocialVLA (2610.02360); nearest protocol Causeway (2609.30913) + LIBERO-MAX (2609.36518).
- Correction: RIAP unsafe commitments 27.5% → 1.6% (not 0%).
- Output: `outputs/g1-interruption-benchmark-novelty.md` (+ provenance). Blocked: OpenReview RTCA (JS), ELLSA GitHub (robots).

## Iteration 7 — 2026-10-18 — G2, G4, strategy comparison, SocialVLA and Causeway full texts
- G2: broad claim closed (SwitchVLA, ReSteer, Causeway); narrow wedge kept (speech-triggered, prefix-aware in-flight retargeting on SmolVLA). G4: narrowed (Song 2607.00530). Causeway "task islands" -> add a state-placement control.
- G2, G4 and comparison runs stopped at an Anthropic rate limit (429). Resumed one at a time from the saved drafts: G2 (verifier fixes applied by hand), G4 (verifier+reviewer fixes), comparison (13/13 arXiv IDs and 12/12 URLs resolve) are now COMPLETE with provenance files. SocialVLA and Causeway summaries complete. `/review` of 06-paper-story.md: `outputs/paper-story-review.md` (major revision needed).
- Feynman spend this day about $56.6 at list price (from ~/.feynman/sessions logs); the three resumed runs cost about $0.8 to $1.3 each versus about $39 for the first wave.
- Diagrams: `10-research-map-and-implementation.md`.

## Iteration 8 — 2026-10-18 — RTC audit and story rewrite
- `/audit` RTC paper vs LeRobot main: `outputs/rtc-smolvla-lerobot-audit.md` (feasible; 3 material default mismatches; missing hooks listed).
- `/draft` story rewrite applying all review points: `outputs/paper-story-v2.md`, adopted as `06-paper-story.md` (D-014).
- Cumulative Feynman spend about $60.4 at list price.

## Pass 9 — 2026-10-31 — Repository and research-workflow setup
- Infrastructure/tooling pass only; no new scientific search, novelty re-check, paid model run, or change to gap/story conclusions. The direction remains open (D-019).
- Reviewed the five requested upstream repositories and relevant installation/CLI documentation [V documentation], resolved immutable source revisions [V Git metadata], and pinned Feynman/REA npm versions and dependencies [V registry metadata]. These flags do not mean live client workflows or research reproductions were verified.
- Preserved and relocated prior research; added a current-state index, shared agent policy, literature/reproduction/RQ/data/experiment/paper workflows, record templates, local Git safeguards, and offline tests/CI.
- claude-obsidian additive adoption plus doctor/contract verification completed. Its source/claim ledgers are empty; legacy reports were not ingested or newly verified.
- Found and documented Understand-Anything's worktree-to-primary graph redirect [V pinned skill]; repository routing explicitly disables it. Graph generation itself was not run.
- npm audit reported 10 affected package entries, including 3 high severity [V audit output]; Feynman/REA activation is gated for human review rather than forced dependency changes. No credentials were read or stored. No native analysis provider was installed.
- Setup and verification details: `../logs/2026-10-31-repository-setup.md`, `../tools/README.md`, and `../docs/plans/2026-10-31-repository.md`.

## Pass 10 — 2026-10-31 — Tool activation
- Infrastructure only; no scientific search or change to conclusions. Feynman and REA runtimes activated under the D-020 exception; REA MCP handshake verified (229 tools); Feynman unauthenticated. Reverse-engineering catalog removed. Details: `../logs/2026-10-31-repository-setup.md`.
