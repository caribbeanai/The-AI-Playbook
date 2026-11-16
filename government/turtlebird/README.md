# TurtleBird

![TurtleBird AI Safety Toolkit banner with a Jamaican doctor bird perched on a Caribbean sea turtle](assets/turtlebird.jpg)

**Prepared by [Adrian Dunkley](https://adriandunkley.net/).**

TurtleBird helps Caribbean public bodies decide when an AI pilot is ready for human review and when a live service needs investigation. Start with one service, agree on the conditions that would stop a release, then test against the way staff do the work today. The public starter kit pairs a field guide with a Python tool that scores reviewed cases offline.

| Start here | What you get |
| --- | --- |
| [Field guide](framework.md) | A release framework, monitoring rules, a stop-and-restart procedure and two process diagrams |
| [Working records](records.md) | Copyable pilot, risk, test, incident and decision records |
| [Python assessor](assess.py) | JSON reports for validation and monitoring, with overall and per-slice results |
| [Fictional examples](examples/) | A sample policy and two test windows for a public-service FAQ |

## Run the example

From the repository root, use Python 3.10 or later. The assessor uses the standard library and runs without an API key, model endpoint or internet connection.

```bash
cd government/turtlebird
python3 assess.py validate --policy examples/policy.json --cases examples/validation.csv
python3 assess.py monitor --policy examples/policy.json --cases examples/monitoring.csv
```

The validation example yields `ready_for_human_review`. The monitoring example yields `escalate_and_consider_pause` because a fictional critical failure overrides the aggregate pass rate. That second command exits with status 1 as designed.

| Exit code | What it means |
| --- | --- |
| 0 | The submitted evidence meets the configured checks for that mode |
| 1 | A threshold, coverage check or critical-failure rule requires attention |
| 2 | The input could not be evaluated. Correct it before using the report |

## Bring your own reviewed cases

Use these four CSV columns in this order: `case_id,slice,model_result,baseline_result`. Use a unique opaque ID per row. The slice is a named test condition such as language, source availability or device class. Score the model and the current service on the same case as `pass`, `fail` or `critical`, using a rubric agreed before testing. Record outcomes in a protected workspace. This public repository accepts synthetic examples.

The policy sets minimum case counts and pass rates overall and for each required slice. A pass rate is the share of reviewed cases marked `pass`. An empty slice has no rate. An unplanned slice triggers review so it cannot disappear into the overall average. The CLI reports baseline performance for comparison. The accountable reviewer decides whether the difference supports release.

A report describes the cases supplied to the tool. Reviewers still need to assess sampling, evidence quality, potential harm and the service's ability to fall back to its manual process. Use the [field guide](framework.md) and [decision record](records.md) for that review.

## Project background

The original [TurtleBird project article](https://starappleai.org/blog-turtlebird-ai-safety-toolkit-caribbean-2026.html) describes the toolkit's public-sector purpose and its connection to Maestro AI Labs and Section 9. This starter kit sits alongside the [Caribbean government implementation playbook](../README.md). Reuse it under the repository's [MIT licence](../../LICENSE).
