# Lead notes (checked directly by lead agent via alpha_ask_paper full text, 2026-10-18)

| Paper | Repaired | Trigger | Robot/sim | Base policy | Code | Instruction change mid-chunk? | Speech? |
|---|---|---|---|---|---|---|---|
| RTC, Black/Galliker/Levine, arXiv 2506.07339 (NeurIPS 2025) | Next chunk generated while current executes; first d actions frozen, overlap region soft-masked (exp. decay guidance), rest inpainted via ΠGDM guidance; inference-time only | New observation (periodic async loop) | Kinetix sim (12 dynamic tasks) + real bimanual 6-DoF arms, 6 tasks (480 episodes) | π0.5 | Sim code: github.com/Physical-Intelligence/real-time-chunking-kinetix | Not evaluated / not discussed | No |
| πR², Park & Tulsiani (CMU), arXiv 2607.26055 | Diffusion-forcing per-position noise; in-flight actions as inpainting conditioning; fast proprio channel every tick, slow VLM (vision+language) channel async | Proprioception (fast), vision-language features (slow, asynchronously refreshed) | Sim + real xArm6+XHand, 4 tasks | GR00T-N1.7 fine-tune | Project page pi-r2-flow.github.io (code status not stated in text seen) | Not evaluated; language sits in slow channel — would be picked up asynchronously, but no experiment | No |
| FutureRTC, Jiang et al., arXiv 2607.24008 | Plug-and-play adapter predicts execution-time visual latent + corrected proprio state; policy frozen | Observation/state staleness | Kinetix + LIBERO sim + real (Hang Cups, π0.5) | π0.5 and **SmolVLA-450M** (LeRobot LIBERO weights) | "Project Website" (URL not extracted) | No | No |
| DiscreteRTC, Wang et al., arXiv 2604.25050 | Discrete-diffusion unmasking natively inpaints committed prefix; early exit | Observation (async loop) | Kinetix + real UR5e (dynamic pick/place, hockey) | Qwen2.5-VL-3B + discrete diffusion head (custom) | website (URL not extracted) | No | No |

Key RTC quote (2506.07339): "generates the next action chunk while executing the current one, 'freezing' actions guaranteed to execute and 'inpainting' the rest."
πR² limitation note: RTC "struggles to recover from failures because previously generated in-flight actions bias the policy toward continuing its recent motion" — relevant to G2: prefix-conditioning biases toward OLD intent after an instruction change.
FutureRTC table shows SmolVLA-450M LIBERO with RTC baseline (69.7% at d=5) — RTC already runs on SmolVLA in sim.
