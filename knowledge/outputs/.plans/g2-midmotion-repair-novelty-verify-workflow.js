const base = "Working dir: the repository root. Date 2026-10-18. Do NOT edit the draft or any other existing file; write ONLY your bound output file. Never write secrets. If a source is blocked (robots.txt, paywall, login) record it, do not work around it. Supporting evidence files: outputs/.drafts/g2-midmotion-repair-novelty-research-A.md, -research-B.md, -research-C.md, -research-D.md and notes/g2-midmotion-repair-novelty-lead-notes.md. ";

const v = await runs.run("verify", {
  agent: "verifier",
  task: base + "Verify citations in outputs/.drafts/g2-midmotion-repair-novelty-draft.md. For EVERY arXiv ID cited, confirm via feynman_science_database_search (source=arxiv, arxiv_get_papers) or alpha tools that ID matches title and date; list mismatches. Spot-check against primary text (alpha_get_paper / alpha_ask_paper) at least these high-stakes claims: SwitchVLA advance interpolates toward canonical start pose; VITA-E retracts to initial pose; Causeway real-robot pooled numbers and 'without put-down or re-grasp'; ReSteer real steering 33% vs 73% on pi0.5 DROID; Reflex instruction pinned in KV cache; DREAM-Chunk SmolVLA on SO-101 numbers; FutureRTC SmolVLA LIBERO numbers; MIRA 466 ms; SocialVLA 336 ms hold; ELLSA 'Action Cancelled'. Check the LeRobot quote at https://github.com/huggingface/lerobot/blob/main/docs/source/inference.mdx if reachable. Output: a table claim -> status (confirmed / corrected / unverifiable) with the corrected text, plus a list of every source URL and whether it resolved.",
  output: "outputs/.drafts/g2-midmotion-repair-novelty-verification.md"
});

const r = await runs.run("review", {
  agent: "reviewer",
  task: base + "Critically review outputs/.drafts/g2-midmotion-repair-novelty-draft.md (and the verification report outputs/.drafts/g2-midmotion-repair-novelty-verification.md if present) as a skeptical IROS reviewer and research lead. Classify issues as FATAL / MAJOR / MINOR. Check: unsupported or overstated claims; claims resting on a single source that drive the conclusion (e.g., 'no paper combines all four elements', LeRobot stop semantics); whether the 'narrowest surviving wedge' is actually distinct from Causeway, ReSteer, SwitchVLA, RoboPrompt, Flow Control, Premover; whether baselines list is sufficient for an IROS reviewer; zombie sections or internal contradictions; status-flag misuse ([V] used for abstract-only or inference). Do not invent new sources; you may run a few alpha_search queries to test whether the wedge is already scooped and report any hits with arXiv IDs.",
  output: "outputs/.drafts/g2-midmotion-repair-novelty-review.md"
});
return [v.ok, r.ok];
