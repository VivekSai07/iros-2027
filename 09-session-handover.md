# Session handover (chat → VS Code / next agent)

Written 2026-10-18 from the Claude chat session that started 2026-10-08. The chat history does not transfer; this file plus 00–08 is the full state.

## 1. Who and what
- Team of 3 (robotics), contact.sparclab@gmail.com, Europe/Berlin. SO-101 arm(s), one shared 48 GB RTX 6000 Ada, others 8 GB GPUs. Strong in Isaac Sim/Lab, Newton, MuJoCo.
- Target: IROS 2027 (Florence, 26 Sep–1 Oct 2027), deadline 1 Mar 2027. Fallback ICRA 2028 (~16 Aug 2027).
- Wants: unique, understandable, application paper (else systematic study), best-paper aspiration, no copying of existing papers.

## 2. Timeline of the session
| Date | Event |
|---|---|
| 10-08 | Goal, hardware, constraints captured (D-001–D-003) |
| 10-10 | Friends' ideas recorded: Rakesh (full-duplex speech HRI), Vivek ("DUM-E", Karcini position paper) (D-004) |
| 10-13 | Claude Project "IROS 27" attached; 5 literature iterations run (D-005–D-009); documents 00–08 written and uploaded to the project under `claude/` |
| 10-18 | Feynman install attempted (blocked, see §5); folder packaged for VS Code; this handover added (D-010–D-011) |

## 3. Current conclusions (see 05, 06 for detail)
- Leading direction: **H1-benchmark+method** — spoken-interruption benchmark for manipulation with a physical failure taxonomy, mid-motion repair without stop/retract (chunk truncation + RTC-style inpainting on SmolVLA/ACT, cascaded streaming speech stack), and a human study linking benchmark metrics to Hoffman fluency metrics (n≈18–39).
- **Invalidated:** "commit timing as a decision variable" (RIAP, Premover) and "first interruption user study" (SocialVLA, CMU HRI 2026, MICoBot, ExpressMM). Do not claim these.
- Alternatives: H2 (knows when NOT to help; partly covered, heavy) and A+B (precision plug-in + endurance; least crowded, needs hardware go/no-go).
- **Direction not yet chosen by the team.** Proposed sprint to ~24 Oct: SO-101 repeatability test, minimal H1 interruption demo, novelty re-check.

## 4. What the next agent should do first
1. Read 00 → 08 in order.
2. Ask the user for the pending items in `08-open-questions-and-access-needs.md` (ELLSA release check, direction choice, ownership, hardware, ethics route, paywalled papers).
3. If the user picks H1: draft the benchmark spec (failure taxonomy, interruption types incl. backchannel and self-correction, metrics) and a minimal LeRobot async + streaming-ASR demo. Re-run a novelty search on arXiv for any new interruption benchmarks before committing.
4. If the user installs Feynman: ingest its `outputs/` provenance files into `04-literature-map.md` with [V]/[S]/[U] flags.
5. Append every decision to `01-decision-log.md`.

## 5. Environment and tooling notes (learned the hard way)
- Cloud sandbox: npm registry blocked by egress policy (403 on CONNECT, `registry.npmjs.org`); do not route around. Public GitHub clones work through the git proxy.
- The linked-computer shell is a Linux VM, not the user's Windows PC ("ms"); it only sees connected folders and cannot install apps on Windows. The user must install local tools themselves.
- ELLSA GitHub page returned ROBOTS_DISALLOWED — user must check manually.
- WebFetch returns full page text (costly); prefer abstract pages. WebSearch is US-only.
- Feynman (github.com/companion-inc/feynman, v0.5.49, MIT): research agent CLI (`/lit`, `/deepresearch`, `/review`, `/audit`). Cloned in the cloud sandbox only; **not installed anywhere**. Install on Windows: `npm install -g @companion-ai/feynman` then `feynman setup`; telemetry off with `FEYNMAN_TELEMETRY=off`.
- Project sync: the Claude Project "IROS 27" copies and the VS Code folder are separate; after editing locally, re-upload or tell Claude.

## 6. Open risks
Scoop risk (medium-high, rising); ethics/participant timeline; SO-101 specs are secondary-source until measured; some claims are abstract-only (paywalled IEEE/ACM, RIAP status, NIABench details).
