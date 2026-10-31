# Provenance: g4-fluency-metrics-validity.md

- **Date:** 2026-10-18. This was the finishing pass of an interrupted run; the original run stopped at an HTTP 429 rate limit before delivery.
- **Final artifact:** `outputs/g4-fluency-metrics-validity.md`, byte-identical to `outputs/.drafts/g4-fluency-metrics-validity-revised.md` (checked with `cmp`). It overwrote the previous PARTIAL-header version.
- **Scope of this pass:** the verifier and reviewer fixes were applied to the existing draft.
  - No new literature searches were run, no subagents were spawned, and no sources were fetched.
  - Only files under `outputs/` were written.

## Files used
| File | Role |
|---|---|
| `outputs/.drafts/g4-fluency-metrics-validity-draft.md` | Base draft (already contained verifier fixes I1–I4 and H1) |
| `outputs/.drafts/g4-fluency-metrics-validity-verification.md` | Verifier findings: spot-checks (a)–(f), other [V] checks, I1–I4, H1–H2, the flag upgrade, and the blocked list |
| `outputs/.drafts/g4-fluency-metrics-validity-review.md` | Reviewer findings: FATAL W1, MAJOR W2–W11, MINOR W12–W22. Also Appendix A (power checks) and Appendix B (alphaXiv checks of SocialVLA, MICoBot, ExpressMM, Kille et al., RAPIDDS) |
| `outputs/.plans/g4-fluency-metrics-validity.md` | Plan; its verification log was empty, so there is no original search log |
| `experiments/g4-fluency-metrics-validity/power.py`, `power_results.txt` | Power numbers (read only; not modified) |
| `05-gap-analysis.md`, `06-paper-story.md` (C3), `02-iros-2027-constraints.md`, `04-literature-map.md`, `08-open-questions-and-access-needs.md` (Q8) | Read only, for the do-not-claim list, the C3 wording, deadline/freeze dates, carried-over entries and the open ethics question. Not edited |

## Fixes applied
| Finding | Severity | Action |
|---|---|---|
| I1–I4, H1 | verifier | Already present in the draft; kept |
| H2 | verifier | VITA-E and the other carried-over items are listed under Sources as project notes without a URL; the n values are flagged [S] in the §5 table |
| Synthetic TLX n=18/group | verifier upgrade | Now [V], citing the paper quote instead of the verifier |
| W1 | FATAL | §1.6 and §8 rewritten to cover the following points: Hoffman's r is a rating-level effect; analytic rmcorr power at r=0.12 for k = 8/16/32; a "beyond condition" power table; k is consistent with the design (8 per condition = 32 total; fallback 4 per condition); within-condition onset/latency variation is built in; the recommendation is downgraded to "feasible only if within-condition variance is substantial"; the full re-simulation is marked TODO |
| W2 | MAJOR | §7: institution marked unknown (Q8); timeline gives best/likely/worst cases with explicit assumptions; gates added (protocol freeze, G2 on hardware); ICRA 2028 fallback |
| W3 | MAJOR | Hoffman metrics demoted to exploratory; operational definition and concurrent-subtask option given; ringing caveat applied |
| W4 | MAJOR | Primary criterion is an item adapted from Hoffman's direct-fluency subscale; convergent and split-half checks; primary analysis restricted to correction-type episodes |
| W5 | MAJOR | One primary predictor (repair latency, or a G1 composite), one primary criterion, one model; secondaries under BH-FDR |
| W6 | MAJOR | Q3 rephrased as a non-significant single item, medians 2 vs 3 |
| W7 | MAJOR | Kille et al. and RAPIDDS added ([S]); search-log paragraph added (§2) |
| W8 | MAJOR | Kendall τ dropped; replaced by a cell-level ICC on objective metrics, TTS vs human speakers |
| W9 | MAJOR | WoZ dropped for IROS; PMQ/SUS/trust once per session; playback annotation sampled or replaced by button presses; time-budget table with TODO pilot values |
| W10 | MAJOR | "Implications for 06-paper-story" note proposing a new C3 (06 not edited) |
| W11 | MAJOR | "Most direct route" instead of "only reachable"; optional third-person rating arm added |
| W12–W22 | MINOR | Flags corrected (MAD-TN, Weiss 8 statements, Pearson, CDS affiliation, Almere "long", PACT inference); 7-item composite; Song attribution; "original validity study"; heterogeneous n table; ExpressMM precedent; G*Power attribution; Holm row; N = 20/24/40; zombies removed (Kennington, Lasota, CMU in §10, PACT U formula, WU Vienna, TU Chemnitz, duplicate EchoChain); full do-not-claim list and §9 rephrase; "widely used", IROS policy claim and DPIA-lite removed or softened |
| Factual correction | — | Blocked ACM status changed from "406" to "403" to match the verifier's observation |

## Sources: accepted / rejected
- **Accepted:**
  - All sources in the final Sources section, with the flags given there.
  - **[S] only:** Kille et al. 2025, RAPIDDS 2026, SocialVLA, MICoBot and ExpressMM. Their numbers come from the reviewer's alphaXiv full-text Q&A and were not cross-checked against the PDFs.
- **Rejected or removed:**
  - **Kennington et al. 2610.08733:** never cited in the body; only its existence was verified.
  - **Lasota & Shah 2015:** blocked and unused.
  - **WU Vienna and TU Chemnitz ethics snippets:** not linked to the team; the Chemnitz date is stale.
  - **PACT U formula:** irrelevant to G4.

## Verification status
- **Sources:** every source URL resolved, and all metadata was checked against arXiv and Crossref in the verifier run (see verification §C). Seven DOIs were blocked by ACM/IEEE; open copies or Crossref metadata were used instead.
- **Numbers:** the high-stakes numbers (a)–(f) were confirmed by the verifier against primary text.
- **`power.py`:** reproduced exactly by the reviewer. Not re-run in this pass.
- **Re-computed in this pass** (in memory, `python` with numpy/scipy; nothing written outside `outputs/`):
  - **Analytic rmcorr power at r=0.12** (Fisher z, df = N(k−1)−1):
    - N=18: 0.27 / 0.51 / 0.81
    - N=24: 0.34 / 0.63 / 0.91
    - N=39: 0.51 / 0.83 / 0.99

    The three values are for k = 8 / 16 / 32. They match the reviewer's k = 8 and k = 32 values; k = 16 is new.
  - **Holm (α = .05/6) paired-t MDE:** 0.92 / 0.77 / 0.58. Matches the reviewer.
  - **Beyond-condition simulation:** N=24, C=4, seed 0 (`np.random.default_rng(0)`), 1000 simulations. The model is the one in review Appendix A.
    - The values match the reviewer's within Monte Carlo error; for example, 0.59 vs 0.62 and 0.66 vs 0.68.
    - The k = 4 per condition rows are new.
- **Not run:**
  - A simulation with random slopes, 7-point discretisation and N = 20/40.
  - Pilot estimates of within-condition variance.
  - Any new literature verification.

## Open (see artifact §10)
- **Hoffman 2019:** item wording and the "Pearson" claim.
- **Weiss et al.:** the 8 statements and the venue.
- **Other attributes:** the CDS affiliation and the Almere length.
- **Unchecked scoop surfaces:** CMU HRI 2026 and RIAP.
- **Missing artifacts:** no systematic search log, no IROS 2027 human-subjects policy check, no preregistration thresholds (TODO), and the team's ethics committee is unknown (08 Q8).
