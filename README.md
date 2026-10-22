<div align="center">

# Awesome Autoloop

**A curated map of automatic environment reset, failure recovery, reset-free learning, and closed-loop policy improvement for real-world robots.**

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

## About

Robot learning rarely ends when a rollout ends. The scene may need to be restored, a local failure may need to be repaired, another task may need to be selected from the resulting state, and new experience may need to be verified before it can improve the policy. **Awesome Autoloop** indexes work on this complete physical loop.

The list is organized by *mechanism*, not by whether a paper uses the label “reset-free.” It covers learned reset policies, forward–backward learning, task chaining, agentic and compositional reset, failure recovery, autonomous evaluation and data collection, VLA post-training, and reversibility benchmarks.

Last updated: **October 2026**. Papers marked **preprint** have not necessarily completed peer review.

## Contents

- [Scope and terminology](#scope-and-terminology)
- [Field map](#field-map)
- [Core systems at a glance](#core-systems-at-a-glance)
- [Foundations of reset-free and autonomous RL](#foundations-of-reset-free-and-autonomous-rl)
- [Learned reset and do–undo policies](#learned-reset-and-doundo-policies)
- [Task chaining and avoiding reset](#task-chaining-and-avoiding-reset)
- [Autonomous evaluation and data collection](#autonomous-evaluation-and-data-collection)
- [Agentic and compositional reset](#agentic-and-compositional-reset)
- [Failure recovery for VLA systems](#failure-recovery-for-vla-systems)
- [Closed-loop VLA post-training](#closed-loop-vla-post-training)
- [Reversibility, safety, and benchmarks](#reversibility-safety-and-benchmarks)
- [Software and infrastructure](#software-and-infrastructure)
- [Surveys and perspectives](#surveys-and-perspectives)
- [Contributing](#contributing)

## Scope and terminology

| Term | Meaning in this repository |
| --- | --- |
| **Reset** | Return the world to a specified initial state or to the support of an initial-state distribution. |
| **Recovery** | Return from a failure state to a region where the task policy can continue; the original scene need not be restored. |
| **Reset-free learning** | Continue learning in a persistent world by alternating goals, changing tasks, or tolerating a changing state distribution. It does not necessarily mean that no human reset ever occurs. |
| **Task chaining** | Select a task whose terminal state makes another task feasible, so tasks functionally reset one another. |
| **Procedural reset** | Restore the environment with scripts, motion planning, fixtures, or deterministic controllers rather than a learned reset policy. |
| **Compositional reset** | Plan a reset by sequencing reusable atomic skills instead of training one monolithic reset policy per terminal configuration. |
| **Autoloop** | A persistent loop that executes, verifies, resets or recovers, collects experience, and optionally updates the policy with limited human involvement. |

Included works must make reset, recovery, persistent practice, autonomous verification, or closed-loop improvement a material part of the method. Generic VLA, RL, planning, and sim-to-real papers are out of scope unless they directly address one of those functions.

## Field map

```text
rollout
  ├─ success ──► verify ──► reset scene ──► next rollout
  │                           ├─ learned reset policy
  │                           ├─ causal inverse plan
  │                           ├─ composed atomic skills
  │                           └─ procedural controller / fixture
  │
  └─ failure ──► detect
                  ├─ retry or local recovery ──► resume task
                  ├─ full reset ───────────────► next rollout
                  ├─ choose another feasible task (no reset)
                  └─ external or human rescue

verified experience ──► policy / skill / agent update ──► deployment
```

The branches are complementary. A system may use a learned local recovery, a procedural scene reset, and human escalation in the same run.

## Core systems at a glance

`Real` indicates physical-robot evidence in the paper. “Online improvement” means that physical interaction is fed back into policy or system improvement, not merely logged.

| Work | Primary mechanism | Real | Learned reset / recovery | Automatic verification | Online improvement | Main limitation |
| --- | --- | :---: | :---: | :---: | :---: | --- |
| [Leave No Trace](https://arxiv.org/abs/1711.06782) (2018) | Forward + reset policies with early abort | — | ✓ | Value-based | ✓ | Simulation and narrow task distributions |
| [MEDAL++](https://arxiv.org/abs/2303.01488) (2023) | Distribution-matching do/undo learning | ✓ | ✓ | Learned reward | ✓ | Task-specific forward/backward practice |
| [AutoEval](https://arxiv.org/abs/2503.24278) (2025) | Autonomous evaluation cell | ✓ | ✓ | ✓ | — | Per-scene reset training; short-horizon tasks |
| [RADAR](https://arxiv.org/abs/2603.11811) (2026, preprint) | Causal inverse planning | ✓ | Planned | ✓ | Data generation | Requires an invertible causal plan |
| [ENPIRE](https://arxiv.org/abs/2606.19980) (2026, preprint) | Agentic reset–execute–verify–refine loop | ✓ | Procedural interface | ✓ | ✓ | Reset implementations remain environment-specific |
| [Zero2Skill](https://arxiv.org/abs/2607.14047) (2026, preprint) | Verification-gated collection with corrective memory | ✓ | Automatic routines | ✓ | Across rounds | Escalates after a retry budget |
| [FLARE](https://arxiv.org/abs/2608.26645) (2026, preprint) | Retry + learned reset-skill routing | ✓ | ✓ | MLLM monitor | — | Small task-specific reset library |
| [REVOLVE](https://arxiv.org/abs/2609.14633) (2026, preprint) | Automated reset/collection + dual-loop evolution | ✓ | Deterministic reset | ✓ | ✓ | Reset is infrastructure, not a general learned capability |
| [HALTER](https://arxiv.org/abs/2609.19413) (2026, preprint) | LLM plans over atomic reset skills | ✓ | ✓ | ✓ | — | Depends on a predefined skill library |
| [FIND](https://arxiv.org/abs/2609.32069) (2026, preprint) | Scene-conditioned task selection instead of reset | ✓ | — | ✓ | ✓ | Still needs recovery interventions for bad states |
| [Kintsugi-VLA](https://arxiv.org/abs/2609.31048) (2026, preprint) | Recoverability-guided recovery data | — | ✓ | Simulator oracle | Offline | Simulation-only study |
| [Recova](https://arxiv.org/abs/2610.01178) (2026, preprint) | Agent-guided learned/programmatic recovery | ✓ | ✓ | ✓ | ✓ | Human demonstration remains the fallback |

## Foundations of reset-free and autonomous RL

- **[Reset-Free Guided Policy Search: Efficient Deep Reinforcement Learning with Stochastic Initial States](https://arxiv.org/abs/1610.01112)** (ICRA 2017) — Extends guided policy search to stochastic initial states, reducing dependence on deterministic resets; includes PR2 experiments.
- **[Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning](https://arxiv.org/abs/1711.06782)** (ICLR 2018) — Jointly learns forward and reset policies and uses reset value to abort actions before entering non-reversible regions.
- **[The Ingredients of Real-World Robotic Reinforcement Learning](https://arxiv.org/abs/2004.12570)** (ICLR 2020) — R3L combines self-supervised representation learning, example-based rewards, and perturbation-based persistent practice on real robots. [Project](https://sites.google.com/view/realworld-rl/)
- **[Autonomous Reinforcement Learning: Formalism and Benchmarking](https://arxiv.org/abs/2112.09605)** (ICLR 2022) — Formalizes autonomous RL in a persistent environment and introduces the EARL benchmark.
- **[Autonomous Reinforcement Learning via Subgoal Curricula](https://arxiv.org/abs/2107.12931)** (NeurIPS 2021) — VaPRL learns a curriculum of reachable initial states and reduces intervention frequency in simulated persistent tasks. [Project](https://sites.google.com/view/vaprl/home)
- **[Intelligent Switching for Reset-Free RL](https://arxiv.org/abs/2405.01684)** (ICLR 2024) — RISC switches between forward and backward policies according to learned confidence rather than a fixed schedule.

## Learned reset and do–undo policies

- **[A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning](https://arxiv.org/abs/2205.05212)** (ICML 2022) — MEDAL trains a backward policy to match the state distribution in a small demonstration set instead of targeting one exact reset state. [Proceedings](https://proceedings.mlr.press/v162/sharma22a.html)
- **[Automating Reinforcement Learning with Example-based Resets](https://arxiv.org/abs/2204.02041)** (RA-L 2022) — Learns a self-supervised reset agent from examples of valid initial states and evaluates it in simulation and on real continuous-control tasks.
- **[Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning](https://arxiv.org/abs/2303.01488)** (CoRL 2023) — MEDAL++ learns image-based forward and undo behaviors plus visual rewards from a small number of demonstrations. [Project](https://architsharma97.github.io/self-improving-robots/)
- **[REBOOT: Reuse Data for Bootstrapping Efficient Real-World Dexterous Manipulation](https://proceedings.mlr.press/v229/hu23a.html)** (CoRL 2023) — Reuses prior task and reset data to bootstrap new real-world dexterous RL runs. [Project](https://sites.google.com/view/reboot-dexterous/)

## Task chaining and avoiding reset

- **[Reset-Free Reinforcement Learning via Multi-Task Learning](https://arxiv.org/abs/2104.11203)** (ICRA 2021) — Learns a set of dexterous tasks whose goals return the real environment to states useful for other tasks. [Project](https://sites.google.com/view/mtrf)
- **[Demonstration-Bootstrapped Autonomous Practicing via Multi-Task Reinforcement Learning](https://arxiv.org/abs/2203.15755)** (ICRA 2023) — Builds a task graph from prior data and chooses tasks that permit long periods of autonomous practice with occasional resets. [Project](https://dbap-rl.github.io/)
- **[Fully Autonomous Real-World Reinforcement Learning with Applications to Mobile Manipulation](https://arxiv.org/abs/2107.13545)** (CoRL 2021) — ReLMM uses outcomes of grasp attempts as functional pseudo-resets for continuous mobile-manipulation learning. [Proceedings](https://proceedings.mlr.press/v164/sun22a.html)
- **[Autonomous Robotic Reinforcement Learning with Asynchronous Human Feedback](https://arxiv.org/abs/2310.20608)** (CoRL 2023) — GEAR uses goal generation, reachability, and occasional asynchronous feedback to sustain reset-free real-robot practice. [Project](https://guided-exploration-autonomous-rl.github.io/GEAR/)
- **[Find Something You Can't Do: Agentic Real-World Reinforcement Learning for Self-Improving VLA Models](https://arxiv.org/abs/2609.32069)** (2026, preprint) — FIND treats the post-rollout scene as the initial state for a feasible weak skill selected by a VLM agent, rather than restoring a fixed scene.

## Autonomous evaluation and data collection

- **[AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](https://arxiv.org/abs/2503.24278)** (CoRL 2025) — Couples learned success classifiers and foundation-policy resetters to run queued real-robot evaluations with minimal supervision. [Project](https://auto-eval.github.io/) · [Code](https://github.com/zhouzypaul/auto_eval)
- **[RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset](https://arxiv.org/abs/2603.11811)** (2026, preprint) — Generates forward and reverse plans together, verifies execution with a VLM, and restores scenes in causal LIFO order.
- **[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)** (2026, preprint) — Exposes reset, rollout, verification, policy improvement, and experiment analysis as a harness for coding agents. [Project](https://research.nvidia.com/labs/gear/enpire/) · [Code](https://github.com/NVlabs/ENPIRE)
- **[Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047)** (2026, preprint) — Runs a collect–verify–reset loop and stores remote natural-language corrections in persistent memory. [Project](https://open-gigaai.github.io/Zero2Skill/) · [Code](https://github.com/open-gigaai/Zero2Skill)
- **[REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention](https://arxiv.org/abs/2609.14633)** (2026, preprint) — Combines deterministic automatic reset and corrective collection with continual updates of both the manipulation policy and supervisory agent.
- **[Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids](https://openreview.net/forum?id=oRwcxFuN25)** (2025) — Uses an external teacher robot to support, detect falls, and reset a humanoid during real-world policy adaptation. [Project](https://robot-trains-robot.github.io/) · [Code](https://github.com/hukz18/Robot-Trains-Robot)

## Agentic and compositional reset

- **[From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413)** (2026, preprint) — HALTER builds an online scene graph and has an LLM compose learned atomic reset skills, score rollouts, and verify restoration.
- **[InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884)** (2026, preprint) — Makes VLA primitives explicitly steerable and uses a VLM-guided data flywheel to acquire missing primitives that can be composed into longer behaviors. [Project](https://insight-vla.github.io/)
- **[ASPIRE: Agentic Skill Discovery for Robotics](https://arxiv.org/abs/2607.00272)** (2026, preprint) — Iteratively diagnoses and repairs robot programs while accumulating validated fixes in a reusable skill library; safe physical reset remains outside its central contribution. [Project](https://research.nvidia.com/labs/gear/aspire/)
- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** (2026, preprint) — Treats a frozen VLA as a retryable contact-rich primitive and learns its operating envelope from execution traces and failure memory.
- **[Recover, Discover, Plan: Learning Skills and Concepts from Robot Failures](https://arxiv.org/abs/2606.18328)** (2026, preprint) — ReSYNC learns recovery skills and relational predicates from failures, then uses them for failure-aware planning and sim-to-real transfer.

## Failure recovery for VLA systems

- **[FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645)** (2026, preprint) — Separates ordinary deviations handled by retry behavior from state-breaking failures routed by an MLLM to learned object-centric reset skills.
- **[Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048)** (2026, preprint) — Estimates recoverability by restoring simulator states and branching Monte Carlo continuations, then targets informative failed states for VLA recovery training.
- **[Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178)** (2026, preprint) — Discovers task and recovery behavior in digital twins, validates it on real robots, and routes unresolved failures to human demonstrations. [Project](https://research.nvidia.com/labs/gear/recova/)
- **[RecoveryChaining: Learning Local Recovery Policies for Robust Manipulation](https://arxiv.org/abs/2410.13979)** (IROS 2025) — Detects execution failures and chains a learned recovery policy back into nominal model-based controllers. [Code](https://github.com/shivamvats/recovery-chaining)
- **[Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](https://arxiv.org/abs/2010.15920)** (RA-L 2021) — Uses a safety critic and recovery policy to keep exploration within recoverable regions; includes physical surgical-robot experiments. [Project](https://sites.google.com/berkeley.edu/recovery-rl/)

## Closed-loop VLA post-training

These works improve policies from autonomous or on-policy interaction. They are included because an autoloop needs an update mechanism, but they do **not** all solve physical environment reset.

- **[Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091)** (ICLR 2026) — Probe–Learn–Distill (PLD) trains residual RL specialists in VLA failure regions, gathers deployment-aligned recovery trajectories, and distills them back into the VLA. [Project](https://wenlixiao.com/self-improve-VLA-PLD)
- **[$\pi^{*}_{0.6}$: A VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** (2025, preprint) — RECAP combines demonstrations, on-policy data, and expert interventions through advantage-conditioned policies for real-world VLA specialization.
- **[RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)** (2026, preprint) — Exposes a compact task-relevant VLA representation to a lightweight actor–critic for sample-efficient real-robot RL.
- **[EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)** (2026, preprint) — Uses a VLM to orchestrate exploration, imitates the collected data, and then applies residual off-policy RL.
- **[Robot Fine-Tuning Made Easy](https://arxiv.org/abs/2310.15145)** (ICRA 2024) — RoboFuME combines a pretrained multitask policy, VLM-derived reward, and reset-free online fine-tuning. [Project](https://robofume.github.io/)
- **[SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](https://arxiv.org/abs/2401.16013)** (ICRA 2024) — Provides a real-world RL stack with demonstrations, reward classifiers, scripted reset support, and distributed data collection. [Project](https://serl-robot.github.io/) · [Code](https://github.com/rail-berkeley/serl)
- **[Continuously Improving Mobile Manipulation with Autonomous Real-World RL](https://arxiv.org/abs/2409.20568)** (CoRL 2024) — Sustains autonomous Spot practice using complementary goals, behavioral priors, and generic rewards. [Project](https://continual-mobile-manip.github.io/)
- **[World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/abs/2602.06508)** (2026, preprint) — Co-trains a video world model and VLA, moving much of RL post-training into a learned virtual environment. [Project](https://showlab.github.io/World-VLA-Loop/)
- **[World Action Models Are Zero-Shot Policies](https://arxiv.org/abs/2602.15922)** (2026, preprint) — DreamZero learns a world-action model from video and robot trajectories; it is relevant as a broad action prior, but the paper does not demonstrate autonomous scene reset. [Project](https://dreamzero0.github.io/) · [Code](https://github.com/dreamzero0/dreamzero)

## Reversibility, safety, and benchmarks

- **[REVERSAL-BENCH: A Reversibility Axis and Reset Oracle for Measuring the Reset-Free RL Cliff](https://arxiv.org/abs/2609.17745)** (2026, preprint) — Controls irreversibility continuously across manipulation environments and supplies an oracle for whether a state is recoverable.
- **[CRONOS: Benchmarking Multi-Task Robotic Manipulation for Reset-Free Reinforcement Learning at Scale](https://github.com/EmbodiedAI-NTU/CRONOS)** (2026, preprint) — A large-scale simulated benchmark for multi-task persistent manipulation; the official repository currently provides the public project entry point.
- **[Back to Base: Towards Hands-Off Learning via Safe Resets with Reach-Avoid Safety Filters](https://arxiv.org/abs/2501.02620)** (L4DC 2025) — Uses reach-avoid safety filtering to keep simulated learning trajectories able to return safely to base states.
- **[Reset-free Trial-and-Error Learning for Robot Damage Recovery](https://arxiv.org/abs/1610.04213)** (Robotics and Autonomous Systems 2018) — Adapts a physical robot after damage using a precomputed behavioral repertoire without returning to an undamaged condition. [Code](https://github.com/resibots/chatzilygeroudis_2018_rte)

## Software and infrastructure

- **[AutoEval](https://github.com/zhouzypaul/auto_eval)** — Autonomous real-robot evaluation queue, policy clients, reset policies, and success classifiers.
- **[ENPIRE](https://github.com/NVlabs/ENPIRE)** — Harness for agent-driven physical policy experiments and environment-specific reset/verification modules.
- **[Zero2Skill](https://github.com/open-gigaai/Zero2Skill)** — Collection, verification, reset, corrective-memory, and dataset-quality tooling.
- **[SERL](https://github.com/rail-berkeley/serl)** — Sample-efficient real-world RL software with actor–learner infrastructure and reset hooks.
- **[EARL benchmark](https://github.com/architsharma97/earl_benchmark)** — Persistent, non-episodic RL environments used by autonomous-RL methods.
- **[REVERSAL-BENCH](https://arxiv.org/abs/2609.17745)** — Paper entry for the reversibility benchmark and reset oracle; follow the paper for the latest release links.

## Surveys and perspectives

- **[Towards Universal Post-Training for Robotics](https://pd-perry.github.io/posts/post-training.html)** (2026) — Perspective on the missing systems recipe around reward, reset, intervention, initialization, and stable RL post-training.
- **[Autonomous Reinforcement Learning: Formalism and Benchmarking](https://arxiv.org/abs/2112.09605)** (2022) — Formal treatment of learning with minimal extrinsic intervention in a persistent world.
- **[Awesome Reset and Recovery Robot RL](https://github.com/liaohr9/awesome-reset-recovery-robot-rl)** — Evidence-focused companion survey covering reset, recovery, safety, re-exploration, maintenance, and physical-system reporting.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Each entry should link to a primary source and state:

- the reset or recovery mechanism;
- whether evidence is simulated or physical;
- whether reset and verification are automatic at runtime;
- what human work remains after setup;
- whether the system improves a policy online.

## License

This curated list is released under [CC0 1.0](LICENSE). Papers, code, images, and linked resources remain under their respective licenses.
