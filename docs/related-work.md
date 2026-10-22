# Related Work

[Back to Awesome Autoloop](../README.md)

These references are preserved from earlier catalog versions. Their primary contribution is policy/skill learning, virtual rollouts or recovery-data generation, rather than physical environment management. They are not part of the main reset/recovery directory.

World models can support virtual policy training and reduce the need for physical training rollouts. They do not themselves restore physical objects. World-Gymnast uses AutoEval for physical evaluation; the reset mechanism is documented under AutoEval in the main directory. PlayWorld remains in the main directory specifically for its workspace-management behavior during collection.

Research cutoff: October 21, 2026.

<!-- literature:start -->

## World Models and Action Priors

- **[World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454)** — 2026, preprint · `Real + world model`<br>
  World-Gymnast trains policies with RL in a learned world model and refines that model using physical rollouts. Its real evaluation uses AutoEval’s reset infrastructure; simulated training does not remove the need for physical reset at collection/evaluation time. [Project](https://world-gymnast.github.io/) · [Code](https://github.com/world-gymnast/world-gymnast)

- **[World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/abs/2602.06508)** — 2026, preprint · `Sim + real`<br>
  World-VLA-Loop alternates policy learning in a video world model with world-model refinement from rollout data. Real-robot evaluation tests transferred improvements, but the virtual training loop does not establish physical reset autonomy. [Project](https://showlab.github.io/World-VLA-Loop/)

- **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922)** — 2026, preprint · `Sim + real`<br>
  DreamZero jointly predicts video and actions and evaluates generalization and cross-embodiment adaptation. Retained as an adjacent action prior, not an autoreset baseline: the inspected method and experiments do not establish autonomous scene restoration. [Project](https://dreamzero0.github.io/) · [Code](https://github.com/dreamzero0/dreamzero)

## Policy and Skill Learning

- **[Reset-Free Guided Policy Search: Efficient Deep Reinforcement Learning with Stochastic Initial States](https://arxiv.org/abs/1610.01112)** — ICRA 2017 · `Sim + real`<br>
  Relaxes deterministic initial-state assumptions in guided policy search. The PR2 pushing experiment still uses operator-placed blocks between trials; this is not a learned physical resetter.

- **[$\pi^{*}_{0.6}$: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** — 2025, preprint · `Real`<br>
  RECAP improves advantage-conditioned policies using demonstrations, on-policy experience and optional expert corrections. The paper explicitly retains human reward annotation, interventions and episode resets. Policy improvement is demonstrated; autonomous physical scene management is not. [Evidence: limitations](https://arxiv.org/pdf/2511.14759).

- **[RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)** — 2026, preprint · `Real`<br>
  RL Token trains a lightweight actor–critic over a frozen VLA representation for selected task phases. Human success labels, optional teleoperated corrections and phase-selection decisions remain in the training protocol; episode initialization is not a learned general reset contribution.

- **[InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884)** — 2026, preprint · `Sim + real`<br>
  InSight segments demonstrations into steerable primitives, collects successful missing-primitive attempts with VLM guidance and distills them into the VLA. This is supervised skill acquisition, not online RL. The limitations explicitly state that manual environment resets remain necessary. [Evidence: limitations](https://arxiv.org/pdf/2606.24884). [Project](https://insight-vla.github.io/)

- **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** — 2026, preprint · `Sim + real`<br>
  ASPIRE accumulates reusable code skills from agent debugging and execution feedback. Physical Rubik’s Cube episodes still require human scrambling and scene resets; safe reset and reliable verification are explicit deployment limitations. A growing program library is not a learned neural resetter. [Project](https://research.nvidia.com/labs/gear/aspire/)

- **[EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)** — 2026, preprint · `Sim`<br>
  EXIMO combines VLM-guided exploration, imitation and residual off-policy RL on simulated ALOHA tasks. Experiments use ground-truth success detection. VLM-based task undo/reset is explicitly future work, not an evaluated capability. [Evidence: experiments and future work](https://arxiv.org/pdf/2608.19891).

## Simulator-Based Recovery Data

- **[Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048)** — 2026, preprint · `Sim`<br>
  Kintsugi-VLA restores saved simulator states and branches a privileged expert to estimate expert-relative recoverability, then generates recovery data for offline VLA retraining. The exact restore operation belongs to the simulator; neither physical autoreset nor online deployment learning is demonstrated.

## Awaiting Verification

- **[CRONOS: Benchmarking Multi-Task Robotic Manipulation for Reset-Free Reinforcement Learning at Scale](https://github.com/EmbodiedAI-NTU/CRONOS)** — Publication status unverified · `Unverified`<br>
  CRONOS is retained from the original bibliography. The repository exposes a title, teaser and website link, but the linked website could not be retrieved during this audit. Publication date/status, method, physical evidence and runnable release remain unverified.

<!-- literature:end -->
