# Contributing to Awesome Autoloop

Thank you for helping keep the map accurate and useful.

## Inclusion criteria

A submission should satisfy at least one of these conditions:

- reset or scene restoration is a material part of the method;
- the robot learns or composes failure-recovery behavior;
- persistent or reset-free practice is evaluated explicitly;
- autonomous evaluation or data collection closes an execute–verify–reset loop;
- policy improvement is demonstrated inside a physical closed loop;
- a benchmark measures reversibility, recoverability, intervention, or sustained autonomy.

Generic manipulation, VLA, RL, planning, and sim-to-real papers are out of scope unless they directly support one of those functions.

## Evidence standard

Use a primary source: proceedings page, DOI, arXiv record, official project page, or official repository. Do not use a news article or model-generated summary as the main link.

Descriptions should report what the paper demonstrates, not what the method might enable. Keep these distinctions explicit:

- simulation vs. physical-robot evidence;
- learned vs. procedural reset;
- reset vs. local recovery;
- automatic runtime behavior vs. manual setup;
- autonomous data collection vs. online policy improvement;
- peer-reviewed publication vs. preprint.

## Entry format

```markdown
- **[Paper title](primary-paper-url)** (Venue YEAR or YEAR, preprint) — One sentence explaining the reset, recovery, or autoloop mechanism. [Project](official-project-url) · [Code](official-code-url)
```

Omit Project or Code when no official public resource is available. Add a work to its primary mechanism section; avoid duplicating it across the detailed paper lists.

For a core-system comparison row, include:

| Field | Allowed values |
| --- | --- |
| Physical evidence | `✓` or `—` |
| Learned reset/recovery | `✓`, `—`, `Planned`, `Procedural`, or a short precise phrase |
| Automatic verification | `✓`, `—`, or the verifier type |
| Online improvement | `✓`, `—`, `Data generation`, `Across rounds`, or a short precise phrase |
| Limitation | One bounded caveat supported by the paper |

## Pull-request checklist

- [ ] The primary paper link resolves.
- [ ] Project and code links are official.
- [ ] The year and venue are verified.
- [ ] The description identifies the actual mechanism.
- [ ] Simulation and real-world evidence are not conflated.
- [ ] A preprint is labeled as such.
- [ ] The entry does not claim that “reset-free” means zero human labor unless the paper measures it.
- [ ] Entries within a section remain approximately chronological.
