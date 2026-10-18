# ELLSA GitHub (bytedance/SALMONN, branch ELLSA) — snapshot pasted by the user, 2026-10-18

Provenance: copied by the user from the GitHub page (the agent is blocked by robots.txt, D-007). Trimmed to the facts relevant to us; status flag [V-user].

- Branch is "3 commits ahead of and 87 commits behind main"; latest commit "Update README.md" (b2d6d1a) "last week". GitHub Releases: none; Packages: none.
- Released (links in README): **ELLSA checkpoint (HuggingFace)**, **train data (HuggingFace; only dialogue TRANSCRIPTS, speech must be synthesized with a TTS model)**, **test data (HuggingFace)**, training scripts (speech-only, mix MoE, TTS-only) and evaluation scripts under `reference/RoboVLMs/scripts` (`run_eval_speech_only.sh`, `run_eval_libero_contemporary.sh`).
- Requires: Llama-3.1-8B-Instruct, Emu3-vision, UniVLA-LIBERO, CosyVoice2-0.5B, SPEAR speech encoder. Python 3.10, flash-attn, kaldifeat.
- README TODO list: speech-interaction eval, LIBERO eval, training data, training (these items appear in the TODO list; the README does not show which are ticked) and **CALVIN eval (not yet)**.
- Capabilities named: speaking-while-acting, context-grounded VQA, instruction rejection, **action barge-in**.
- Reported: LIBERO average 89.4% (SPATIAL 90.8, OBJECT 95.8, GOAL 86.4, LONG 84.4).
- NOT stated in the README: any dedicated barge-in evaluation script or barge-in test set, and any real-robot or SO-101 support.
