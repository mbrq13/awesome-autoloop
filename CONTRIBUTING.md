# Contributing to Awesome Autoloop

Help make the directory accurate, not just longer. Corrections to existing claims are as valuable as new papers.

## Scope

Include methods that restore, recover or manage a robot's physical environment to sustain repeated execution, data collection or learning. Relevant reset-free algorithms and safety/recoverability studies are welcome, including simulation studies when clearly labeled.

For each addition, identify the concrete environment-management behavior: what is restored, how execution resumes, or how practice continues without a reset. Policy improvement, a closed-loop training diagram, a VLA or a world model alone is insufficient. A system that collects data for a world model may qualify through its physical workspace management, not through its downstream model training.

The [related-work appendix](docs/related-work.md) preserves previously catalogued contextual and unverified references. It is not a second general-purpose VLA bibliography. New main-directory entries must meet the direct relevance criterion above.

The current literature cutoff is **October 21, 2026**. A later revision should not be used to support a claim attributed to this snapshot. Propose a cutoff update explicitly when adding newer work.

## Verify before adding

1. Find the canonical paper identity (arXiv ID, DOI or proceedings record). Search the directory for duplicates and title changes.
2. Read the **method and experiments**, plus relevant appendices. Abstracts, search snippets and other lists are discovery aids, not sufficient evidence.
3. Record the source version, first-public date and confirmed venue/status in the PR. Conference edition and proceedings publication year may differ. A submission is not an acceptance; identify author-reported acceptance if no proceedings record is available.
4. Cross-check official project, code and data links against the paper or author/lab site. Distinguish an announcement, data preview or placeholder repository from a complete release. Label community implementations explicitly.
5. State what was measured, on which tasks and in simulation or hardware. Do not generalize a single task's intervention rate to the whole system.
6. If evidence is inaccessible or ambiguous, retain the reference with a precise limitation. Use **not reported**, **not established**, or **unverified**, rather than guessing or interpreting missing evidence as a negative result.

## Independent classification axes

| Axis | Required distinctions |
| --- | --- |
| Objective | Episodic initial-state restoration; local continuation; learned do/undo; task chaining; evaluation/collection; agentic composition; policy improvement; safety/recoverability. |
| Mechanism | Human, script, planning/IK/controller, learned backward policy, generalist/VLA, composed skills, agent-generated program, external robot, fixture/cell, task chaining, simulator restore. Name hybrid mechanisms. |
| Learning | Which component changes? Fixed resetter, online RL, supervised/DAgger updates between rounds, offline distillation, or textual memory. State reset demonstrations and new-skill acquisition separately. |
| Evidence | Simulation, physical robot, or both; clarify whether physical results validate the reset module itself or only task execution. |
| Human boundary | Setup, demonstrations, labels, placement, calibration, supervision and rescue. Report duration, consecutive episodes and intervention counts only when measured. |

For a reset claim, identify the target states, whether success and failure endpoints are covered, and whether a **new episode** can begin after verification. For recovery, identify how execution resumes. A safe arm pose does not necessarily restore object configurations. “Reset-free” does not mean zero human labor, and LLM orchestration does not imply a learned reset policy.

## Entry template

Place each work in **one primary section**, ordered by the displayed venue/publication year (posting year for preprints). Record the first-public date separately in the PR. Use short cross-references elsewhere; the collapsible comparison and implementation shortcuts are intentional repeat links, not new papers.

```markdown
- **[Full canonical paper title](primary-paper-url)** — Venue YEAR or YEAR, preprint · `Sim / Real / Sim + real`<br>
  Mechanism and update type. Experimental scope and remaining dependency or uncertainty. [Project](official-url) · [Code](official-url) · [Data](official-url)
```

Choose one evidence label, not the literal slash-separated template. Aim for two sentences (roughly 25–40 words, excluding links): mechanism first, then the material experimental/human dependency. Keep acronyms when absent from the title. Omit unavailable links; add a source locator for disputed classifications. Avoid repeated generic disclaimers: state the specific boundary, such as simulator-only reset, human rescue or task-specific fixtures. Never remove a material limitation merely to shorten the text.

The compact comparison is selective, not a checklist of all papers. Explain capabilities and limitations in words rather than unqualified checkmarks. Do not add wide tables or duplicate a detailed entry to increase visibility.

## Preservation and validation

- Retain useful paper, project, code and dataset links when reorganizing, including moves to the related-work appendix. Document moves, replacements or inaccessible links in the PR; never silently remove a reference.
- Run `python3 scripts/check_catalog.py` for duplicate primary links, internal anchors and local paths.
- Run `python3 scripts/check_catalog.py --online` to probe external URLs. HTTP success is not evidence of scientific correctness or a usable release; browser challenges and transient failures need manual review.
- Preview the README on GitHub, including the collapsible comparison, tables and narrow-screen wrapping.
- Keep maintenance notes local when they are not useful to readers. Prefer this README and small reusable checks over a separate website or a generated catalog stack.

## Reporting corrections

Open an issue or PR with the current statement, proposed correction, primary-source URL/version and section or table supporting it. Explain whether the change concerns reset versus recovery, evidence scope, learning, human dependence, metadata or a resource link. Preserve uncertainty when the paper does not resolve it.
