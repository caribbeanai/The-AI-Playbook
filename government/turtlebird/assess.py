#!/usr/bin/env python3
"""Evaluate reviewed AI safety cases against a policy. Prepared by Adrian Dunkley."""

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

COLUMNS = ["case_id", "slice", "model_result", "baseline_result"]
RESULTS = {"pass", "fail", "critical"}


def unique_keys(pairs):
    values = {}
    for key, value in pairs:
        if key in values:
            raise ValueError(f"Duplicate policy key: {key}")
        values[key] = value
    return values


def validate_thresholds(value, label):
    if not isinstance(value, dict) or value.keys() != {"min_cases", "min_pass_rate"}:
        raise ValueError(f"{label} needs min_cases and min_pass_rate")
    count, rate = value["min_cases"], value["min_pass_rate"]
    if type(count) is not int or count < 1:
        raise ValueError(f"{label}.min_cases must be a positive integer")
    if type(rate) not in (float, int) or not 0 < rate <= 1:
        raise ValueError(f"{label}.min_pass_rate must be greater than 0 and at most 1")


def load_policy(path):
    policy = json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_keys)
    if not isinstance(policy, dict) or policy.keys() != {"overall", "slices"}:
        raise ValueError("Policy needs overall and slices")
    validate_thresholds(policy["overall"], "overall")
    slices = policy["slices"]
    if not isinstance(slices, dict) or not slices:
        raise ValueError("Policy needs at least one named slice")
    for name, thresholds in slices.items():
        if not name or name != name.strip():
            raise ValueError("Slice names must be nonempty and trimmed")
        validate_thresholds(thresholds, f"slice {name}")
    return policy


def load_cases(path):
    cases = []
    seen = set()
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"CSV columns must be: {', '.join(COLUMNS)}")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"CSV line {reader.line_num} has the wrong number of fields")
            case_id, group, model, baseline = (row[key].strip() for key in COLUMNS)
            if not case_id or case_id in seen:
                raise ValueError(f"CSV line {reader.line_num} has a missing or duplicate case ID")
            if not group or model not in RESULTS or baseline not in RESULTS:
                raise ValueError(f"CSV line {reader.line_num} has a missing slice or invalid result")
            seen.add(case_id)
            cases.append((group, model, baseline))
    return cases


def summarise(cases, thresholds):
    count = len(cases)
    model_pass = sum(model == "pass" for _, model, _ in cases)
    baseline_pass = sum(baseline == "pass" for _, _, baseline in cases)
    critical = sum(model == "critical" for _, model, _ in cases)
    rate = model_pass / count if count else None
    baseline_rate = baseline_pass / count if count else None
    reasons = []
    if thresholds is None:
        reasons.append("slice_not_in_policy")
    else:
        if count < thresholds["min_cases"]:
            reasons.append("too_few_cases")
        if rate is not None and rate < thresholds["min_pass_rate"]:
            reasons.append("pass_rate_below_floor")
    if critical:
        reasons.append("critical_failure")
    return {
        "cases": count,
        "model_passes": model_pass,
        "model_pass_rate": rate,
        "baseline_passes": baseline_pass,
        "baseline_pass_rate": baseline_rate,
        "model_critical_failures": critical,
        "baseline_critical_failures": sum(baseline == "critical" for _, _, baseline in cases),
        "thresholds": thresholds,
        "reasons": reasons,
    }


def assess(cases, policy, mode):
    grouped = defaultdict(list)
    for case in cases:
        grouped[case[0]].append(case)
    slices = {
        name: summarise(grouped[name], policy["slices"].get(name))
        for name in sorted(policy["slices"].keys() | grouped.keys())
    }
    overall = summarise(cases, policy["overall"])
    threshold_miss = bool(overall["reasons"] or any(row["reasons"] for row in slices.values()))
    if mode == "validate":
        status = "hold" if threshold_miss else "ready_for_human_review"
    elif overall["model_critical_failures"]:
        status = "escalate_and_consider_pause"
    else:
        status = "investigate" if threshold_miss else "continue_monitoring"
    return {"mode": mode, "status": status, "overall": overall, "slices": slices}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["validate", "monitor"])
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--cases", required=True, type=Path)
    args = parser.parse_args()
    try:
        policy = load_policy(args.policy)
        cases = load_cases(args.cases)
    except (OSError, ValueError, csv.Error) as error:
        print(f"TurtleBird input error: {error}", file=sys.stderr)
        return 2
    report = assess(cases, policy, args.mode)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] in {"ready_for_human_review", "continue_monitoring"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
