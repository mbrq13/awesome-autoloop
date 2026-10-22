# Awesome Autoloop

Awesome Autoloop is a curated, research-focused collection of methods, papers, and open-source systems that enable robots to autonomously restore, recover, or manage their physical environments to sustain repeated execution, data collection, and learning with minimal human intervention.

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

**Research cutoff:** October 21, 2026.

## Contents

- [Learned Reset Policies](#learned-reset-policies)
- [Planned and Compositional Reset](#planned-and-compositional-reset)
- [Reset and Collection Systems](#reset-and-collection-systems)
- [Task Chaining and Persistent Practice](#task-chaining-and-persistent-practice)
- [Failure Recovery](#failure-recovery)
- [Reset-Free Learning Foundations](#reset-free-learning-foundations)
- [Safety and Recoverability](#safety-and-recoverability)
- [Code and Benchmarks](#code-and-benchmarks)
- [Further Reading](#further-reading)
- [Contributing](#contributing)

**Reset** prepares a new rollout. **Recovery** resumes the current task. **Persistent practice** continues from the current state by choosing what to do next.

Entries identify the mechanism, learning process and remaining human dependencies. `Sim` / `Real` labels describe the experimental setting, not every module or human-free operation. Within each section, entries follow the displayed venue/publication year.

<details>
<summary><strong>Compare Representative Systems</strong></summary>

| System / evidence | Scene-management objective and mechanism | Learning / remaining boundary |
| --- | --- | --- |
| [MEDAL++](https://arxiv.org/abs/2303.01488) · Sim + real | Do/undo: learned backward policy targets demonstration states. | Joint online RL; demonstrations and intermittent human resets. |
| [SERL](https://arxiv.org/abs/2401.16013) · Real | Learned forward/backward relocation; task-specific resets elsewhere. | Online RL; reset and reward setup differ by task. |
| [AutoEval](https://arxiv.org/abs/2503.24278) · Real | Episodic reset: imitation-trained resetters **and** scripts. | Evaluates fixed policies; demonstrations, classifiers and rescue. |
| [HALTER](https://arxiv.org/abs/2609.19413) · Real | Episodic reset: LLM composes learned atomic skills. | Fixed evaluation policies; skill demonstrations and failed-reset fallback. |
| [ENPIRE](https://arxiv.org/abs/2606.19980) · Real setups | Procedural reset to task/critical-phase initial conditions. | Agent-driven policy/code optimization; human-guided environment construction. |
| [RADAR](https://arxiv.org/abs/2603.11811) · Sim + qualitative real | Planned causal inverse; quantitative tests use simulator resets. | Data generation; physical reset endurance not established. |
| [REVOLVE](https://arxiv.org/abs/2609.14633) · Real | Deterministic episodic reset and corrective controllers. | Policy retraining plus supervisor memory; human-reviewed judgments and program refinement. |
| [FIND](https://arxiv.org/abs/2609.32069) · Real | Avoids episodic reset through feasible-task selection. | Online residual RL; manual scene recovery remains. |
| [Recova](https://arxiv.org/abs/2610.01178) · Sim + real | **Local recovery**, using learned policies or programs; then resume. | DAgger across rounds, not online RL; human fallback. |
| [PLD](https://arxiv.org/abs/2511.00091) · Sim + real | Task-dependent fixtures, manual placement or learned task cycles. | Residual RL then distillation; not a general reset solution. |

</details>

<!-- literature:start -->
## Learned Reset Policies

Learn backward behaviors that return the environment to usable starting states.

- **[Automating Reinforcement Learning with Example-based Resets](https://arxiv.org/abs/2204.02041)** — RA-L 2022 · `Sim + real`<br>
  Learns a reset policy and success classifier from initial-state examples; switches early to preserve reset feasibility. UR3 experiments retain manual rescue for irrecoverable states.

- **[A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning](https://arxiv.org/abs/2205.05212)** — ICML 2022 · `Sim`<br>
  MEDAL learns backward behavior by matching demonstration-state distributions, alongside forward RL. Requires demonstrations and intermittent external resets. [Proceedings](https://proceedings.mlr.press/v162/sharma22a.html)

- **[Don’t Start From Scratch: Leveraging Prior Data to Automate Robotic Reinforcement Learning](https://proceedings.mlr.press/v205/walke23a.html)** — CoRL 2022; proceedings 2023 · `Sim + real`<br>
  ARIEL adapts task/backward policies and task embeddings with online RL, initialized from prior multi-task data. Requires task rewards and occasional external resets. [Project](https://sites.google.com/view/ariel-berkeley)

- **[Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning](https://arxiv.org/abs/2303.01488)** — CoRL 2023 · `Sim + real`<br>
  MEDAL++ jointly learns visual task/undo policies and reward classifiers from demonstrations. Reports 10–30 hours of practice with roughly hourly interventions and scripted arm resets. [Evidence: experiments and setup appendix](https://arxiv.org/pdf/2303.01488) · [Project](https://architsharma97.github.io/self-improving-robots/)

- **[REBOOT: Reuse Data for Bootstrapping Efficient Real-World Dexterous Manipulation](https://proceedings.mlr.press/v229/hu23a.html)** — CoRL 2023 · `Real`<br>
  REBOOT uses a demonstration-trained object-retrieval resetter to sustain dexterous RL. The task policy learns through RL; the resetter is trained by behavioral cloning. [Project](https://sites.google.com/view/reboot-dexterous/)

- **[Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning](https://arxiv.org/abs/2310.15145)** — ICRA 2024 · `Sim + real`<br>
  RoboFuME alternates task/reset instructions while fine-tuning a shared policy online. Uses demonstrations and VLM rewards; real scenes still need manual resets every 15–35 episodes, depending on task. [Project](https://robofume.github.io/)

- **[SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](https://arxiv.org/abs/2401.16013)** — ICRA 2024 · `Real`<br>
  SERL jointly trains forward/backward RL agents for object relocation; other tasks use simpler resets. Requires task-specific reward, demonstration and controller setup. [Evidence: §4.3 and §5](https://arxiv.org/pdf/2401.16013) · [Project](https://serl-robot.github.io/) · [Code](https://github.com/rail-berkeley/serl)

## Planned and Compositional Reset

Restore scene relations by planning inverse actions or composing reset skills.

- **[RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset](https://arxiv.org/abs/2603.11811)** — IROS 2026 (acceptance reported on arXiv) · `Sim + real (qualitative)`<br>
  RADAR plans causal inverse actions in a collection loop. Quantitative RLBench tests use simulator resets; real-arm demonstrations are qualitative, with physical reset endurance unreported. [Evidence: §IV-A and §IV-D](https://arxiv.org/pdf/2603.11811) · [Project](https://radar-iros.netlify.app/)

- **[From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413)** — 2026, preprint · `Real`<br>
  HALTER composes demonstration-trained reset skills using scene graphs and an LLM, then verifies target relations. Held-out tasks reuse objects/skills; task policies stay fixed and failed resets request human assistance.

## Reset and Collection Systems

Repeat physical trials using reset controllers, workspace management or external hardware.

- **[AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](https://arxiv.org/abs/2503.24278)** — CoRL 2025 · `Real`<br>
  AutoEval repeats physical evaluations using imitation-trained resetters, scripts and success/reset classifiers. Reset demonstrations cover successful and failed rollouts; failed resets or hardware faults require assistance. [Project](https://auto-eval.github.io/) · [Code](https://github.com/zhouzypaul/auto_eval)

- **[Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids](https://arxiv.org/abs/2508.12252)** — CoRL 2025 · `Real`<br>
  RTR uses a force-sensing UR5 teacher and treadmill to support and reposition a ToddlerBot during PPO learning. Reset depends on dedicated hardware and controllers. [Project](https://robot-trains-robot.github.io/) · [Code](https://github.com/hukz18/Robot-Trains-Robot) · [OpenReview record; browser check may be required](https://openreview.net/forum?id=oRwcxFuN25)

- **[PlayWorld: Learning Robot World Models from Autonomous Play](https://arxiv.org/abs/2603.09030)** — CoRL 2026 · `Real`<br>
  PlayWorld uses VLM-guided VLA play and returns drifting objects to the reachable workspace, sustaining data collection for world-model training. Human monitoring and occasional scene resets remain. [Project](https://robot-playworld.github.io/) · [Code](https://github.com/irom-princeton/open-world) · [Data preview](https://huggingface.co/datasets/tennyyyin/playworld_dataset_preview)

- **[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)** — CoRL 2026 · `Sim + real`<br>
  ENPIRE uses agent-built, human-refined reset/verification procedures, fixed during policy optimization. Resets are task-specific and may restore only critical-phase starting conditions. [Evidence: §2.1 and Appendix A.1](https://arxiv.org/pdf/2606.19980) · [Project](https://research.nvidia.com/labs/gear/enpire/) · [Code](https://github.com/NVlabs/ENPIRE)

- **[Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047)** — 2026, preprint · `Real`<br>
  Zero2Skill composes perception, grasping and motion tools into collect–verify–reset routines. Bounded retries escalate to remote human corrections, stored in memory; collected data later trains policies. [Project](https://open-gigaai.github.io/Zero2Skill/) · [Code](https://github.com/open-gigaai/Zero2Skill)

- **[REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention](https://arxiv.org/abs/2609.14633)** — 2026, preprint · `Real`<br>
  REVOLVE uses geometry/IK-based reset and correction controllers to collect data for policy retraining. Programs require manual refinement; supervisor memory uses human-reviewed judgments.

## Task Chaining and Persistent Practice

Keep practicing by switching goals, redistributing objects or cycling complementary tasks.

- **[The Ingredients of Real-World Robotic Reinforcement Learning](https://arxiv.org/abs/2004.12570)** — ICLR 2020 · `Sim + real`<br>
  R3L alternates task execution with novelty-seeking perturbations to diversify physical practice. Requires goal-image examples and a workable setup rather than a prescribed scene reset. [Project](https://sites.google.com/view/realworld-rl/)

- **[Reset-Free Reinforcement Learning via Multi-Task Learning: Learning Dexterous Manipulation Behaviors without Human Intervention](https://arxiv.org/abs/2104.11203)** — ICRA 2021 · `Sim + real`<br>
  MTRF learns complementary dexterous behaviors that reset one another. A designer-specified task graph and task rewards organize sustained practice. [Project](https://sites.google.com/view/mtrf)

- **[Fully Autonomous Real-World Reinforcement Learning with Applications to Mobile Manipulation](https://arxiv.org/abs/2107.13545)** — CoRL 2021 · `Sim + real`<br>
  ReLMM redistributes objects through random navigation, release and retreat after grasps, supporting navigation/grasping RL. These procedural pseudo-resets still require occasional intervention. [Proceedings](https://proceedings.mlr.press/v164/sun22a.html)

- **[Demonstration-Bootstrapped Autonomous Practicing via Multi-Task Reinforcement Learning](https://arxiv.org/abs/2203.15755)** — ICRA 2023 · `Sim + real`<br>
  DBAP builds a task-transition graph from demonstrations and bootstraps multi-task RL. Complementary tasks sustain practice with occasional external resets. [Project](https://dbap-rl.github.io/)

- **[Autonomous Robotic Reinforcement Learning with Asynchronous Human Feedback](https://arxiv.org/abs/2310.20608)** — CoRL 2023 · `Sim + real`<br>
  GEAR selects reachable goals using asynchronous human comparisons. Physical pusher training needs occasional object nudges, approximately every 30 minutes. [Project](https://guided-exploration-autonomous-rl.github.io/GEAR/)

- **[Continuously Improving Mobile Manipulation with Autonomous Real-World RL](https://arxiv.org/abs/2409.20568)** — CoRL 2024 · `Real`<br>
  Alternates complementary goals for Spot manipulation with online RL. Sweeping uses a second robot's fixed grasp procedure to return the bag; mapping and behavioral priors require upfront setup. [Project](https://continual-mobile-manip.github.io/)

- **[Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091)** — ICLR 2026 · `Sim + real`<br>
  PLD combines residual RL and distillation with task-specific practice setups: a shaped desk, human peg repositioning, or a learned GPU insertion/unplugging cycle. [Evidence: §5 and Appendix D.1](https://arxiv.org/pdf/2511.00091) · [Project](https://wenlixiao.com/self-improve-VLA-PLD)

- **[Find Something You Can't Do: Agentic Real-World Reinforcement Learning for Self-Improving VLA Models](https://arxiv.org/abs/2609.32069)** — 2026, preprint · `Real`<br>
  FIND chooses feasible, underperforming tasks from the current scene and learns a residual policy over a frozen VLA. Its representative six-hour, 456-episode run includes 30 manual scene recoveries and a longest uninterrupted run of 48 minutes. [Evidence: Table II](https://arxiv.org/pdf/2609.32069).

## Failure Recovery

Restore a task-valid state and resume execution, rather than start a new episode.

- **[FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](https://proceedings.mlr.press/v229/stachowicz23a.html)** — CoRL 2023 · `Sim + real`<br>
  FastRLAP uses a scripted state machine to escape collisions and resume driving RL. Requires a configured course, prior navigation data and a slow demonstration lap. [Project](https://sites.google.com/view/fastrlap)

- **[RecoveryChaining: Learning Local Recovery Policies for Robust Manipulation](https://arxiv.org/abs/2410.13979)** — IROS 2025 · `Sim + real`<br>
  RecoveryChaining learns local RL policies that return execution to nominal controllers or complete the task. Trained in simulation with physical transfer tests; controllers and failure detection are supplied. [Code](https://github.com/shivamvats/recovery-chaining)

- **[Recover, Discover, Plan: Learning Skills and Concepts from Robot Failures](https://arxiv.org/abs/2606.18328)** — CoRL 2026 · `Sim + real`<br>
  ReSYNC learns recovery skills and relational concepts to repair failed plans. Physical experiments transfer simulator-trained recovery; training assumes a resettable dynamics model.

- **[One Demonstration Is Enough for Real-World Robotic Reinforcement Learning](https://arxiv.org/abs/2607.01651)** — 2026, preprint · `Real`<br>
  AutoSERL uses demonstration-guided motion planning and predefined recovery points to replace operator corrections during RL. Evaluated on six contact-rich tasks with task-specific setup. [Project](https://autoserl.github.io/) · [Code](https://github.com/autoserl/AutoSERL)

- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** — 2026, preprint · `Sim + real`<br>
  Harness VLA combines frozen VLA actions, analytic motion primitives and execution memory for retries and replanning. Requires calibrated tools and prepared procedures; model weights stay fixed.

- **[FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645)** — CVPR 2026 (acceptance reported on arXiv) · `Sim + real`<br>
  FLARE trains recovery adapters from targeted human demonstrations. A multimodal monitor selects adapters to restore task-valid states and resume execution; training occurs before deployment.

- **[Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178)** — 2026, preprint · `Sim + real`<br>
  Recova detects failures, invokes learned or programmed recovery and resumes execution. Task/recovery policies receive DAgger updates between rounds; unresolved cases need human demonstrations. [Evidence: §3.1–3.4](https://arxiv.org/pdf/2610.01178) · [Project](https://research.nvidia.com/labs/gear/recova/)

## Reset-Free Learning Foundations

Algorithms and formulations for learning with limited external resets.

- **[Leave no Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning](https://arxiv.org/abs/1711.06782)** — ICLR 2018 · `Sim`<br>
  Leave No Trace jointly learns task/reset policies with off-policy RL and aborts risky actions using reset-value estimates. Failed learned resets invoke a hard-reset oracle.

- **[Autonomous Reinforcement Learning via Subgoal Curricula](https://arxiv.org/abs/2107.12931)** — NeurIPS 2021 · `Sim`<br>
  VaPRL learns to reach useful practice states through a value-based curriculum. Simulated reversible environments use prior demonstrations and sparse external resets. [Project](https://sites.google.com/view/vaprl/home)

- **[Autonomous Reinforcement Learning: Formalism and Benchmarking](https://arxiv.org/abs/2112.09605)** — ICLR 2022 · `Sim`<br>
  EARL formalizes non-episodic learning and separates continuing from deployed-policy performance. Its simulated benchmark makes intervention budgets explicit.

- **[Demonstration-free Autonomous Reinforcement Learning via Implicit and Bidirectional Curriculum](https://proceedings.mlr.press/v202/kim23d.html)** — ICML 2023 · `Sim`<br>
  IBC uses an auxiliary agent and optimal-transport bidirectional curricula for non-episodic RL without demonstrations. Evaluated on simulated sparse-reward tasks. [Code](https://github.com/snu-larr/ibc_official)

- **[Intelligent Switching for Reset-Free RL](https://arxiv.org/abs/2405.01684)** — ICLR 2024 · `Sim`<br>
  RISC switches forward/backward policies using learned confidence. Simulated EARL/gridworld experiments retain explicit hard-reset budgets.

## Safety and Recoverability

Preserve recoverable states and evaluate the limits of continued practice.

- **[Reset-free Trial-and-Error Learning for Robot Damage Recovery](https://arxiv.org/abs/1610.04213)** — Robotics and Autonomous Systems 2018 · `Sim + real`<br>
  RTE combines behavior repertoires, adaptation and planning so damaged robots continue navigation trials from their current position, without returning to a fixed start. [Code](https://github.com/resibots/chatzilygeroudis_2018_rte)

- **[Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](https://arxiv.org/abs/2010.15920)** — RA-L 2021 · `Sim + real`<br>
  Recovery RL learns a safety critic and recovery controller from offline constraint data, then updates during task learning. Restores nearby safe states; training retains environment resets. [Project](https://sites.google.com/berkeley.edu/recovery-rl/)

- **[Back to Base: Towards Hands-Off Learning via Safe Resets with Reach-Avoid Safety Filters](https://arxiv.org/abs/2501.02620)** — L4DC 2025 · `Sim`<br>
  Back to Base uses reach-avoid safety filters to preserve a path to a reset region. Evaluated in modified cartpole with specified dynamics and targets.

- **[REVERSAL-BENCH: A Reversibility Axis and Reset Oracle for Measuring the Reset-Free RL Cliff](https://arxiv.org/abs/2609.17745)** — 2026, preprint · `Sim`<br>
  REVERSAL-BENCH studies irreversibility using simulator checkpoints and recovery-search oracles. Provides a recoverability evaluation framework; a runnable release was not verified.

<!-- literature:end -->

## Code and Benchmarks

Official code is linked beside papers. Selected starting points:

| Resource | Use |
| --- | --- |
| [AutoEval](https://github.com/zhouzypaul/auto_eval) | Physical evaluation, resetters and classifiers. |
| [SERL](https://github.com/rail-berkeley/serl) | Robot RL stack and forward/backward task examples. |
| [Zero2Skill](https://github.com/open-gigaai/Zero2Skill) | Collection, verification and reset orchestration. |
| [EARL](https://github.com/architsharma97/earl_benchmark) | Non-episodic simulation and evaluation protocols. |

## Further Reading

- [Towards Universal Post-Training for Robotics](https://pd-perry.github.io/posts/post-training.html) — Perspective on reset, reward and intervention in robot learning.
- [Awesome Reset and Recovery Robot RL](https://github.com/liaohr9/awesome-reset-recovery-robot-rl) — Related literature collection.
- [Related Work](docs/related-work.md) — Previously catalogued world models, general policy/skill learning and unverified references, kept separate from the reset and recovery directory.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope, evidence requirements and the entry template. Check structure with `python3 scripts/check_catalog.py`; add `--online` to probe links.

## License

The curated list is [CC0 1.0](LICENSE). Linked papers, code and datasets retain their own licenses.
