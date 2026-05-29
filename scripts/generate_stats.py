#!/usr/bin/env python3
"""
WOKDEX Stats Generator
=======================
Reads corpus.json and generates aggregated stats.json for the dashboard.

Usage:
    python generate_stats.py <data_dir>

Example:
    python generate_stats.py ../data/
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate aggregated statistics from corpus.json."
    )
    parser.add_argument("data_dir", help="Path to the data directory containing corpus.json")
    args = parser.parse_args()

    data_path = Path(args.data_dir).resolve()
    corpus_path = data_path / "corpus.json"
    exercises_dir = data_path / "exercises"

    if not corpus_path.exists():
        print(f"❌ corpus.json not found at {corpus_path}")
        sys.exit(1)

    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    exercises = corpus.get("exercises", [])
    summary = corpus.get("summary", {})

    # Load individual exercise JSONs for deeper stats
    detailed_exercises = []
    if exercises_dir.is_dir():
        for ex_file in sorted(exercises_dir.glob("*.json")):
            with open(ex_file, "r", encoding="utf-8") as f:
                detailed_exercises.append(json.load(f))

    # --- Aggregate Statistics ---

    # 1. Difficulty distribution
    difficulty_dist = summary.get("difficulty_distribution", {})

    # 2. Test type distribution
    test_type_dist = summary.get("test_type_distribution", {})

    # 3. Skills frequency
    skills_freq = summary.get("skills_frequency", {})

    # 4. Scenarios per level (A–D) — requires detailed data
    scenario_levels = {}
    for ex in detailed_exercises:
        for sc in ex.get("scenarios", []):
            lvl = sc.get("level", "C")
            scenario_levels[lvl] = scenario_levels.get(lvl, 0) + 1

    # 5. FALSE_GREEN coverage
    fg_with = sum(1 for e in exercises if e.get("has_false_green"))
    fg_without = len(exercises) - fg_with

    # 6. PERFORMANCE coverage
    perf_with = sum(1 for e in exercises if e.get("has_performance"))
    perf_without = len(exercises) - perf_with

    # 7. Average test cases per exercise
    total_tc = summary.get("total_test_cases", 0)
    avg_tc = round(total_tc / len(exercises), 1) if exercises else 0

    # 8. Average scenarios per exercise
    total_sc = summary.get("total_scenarios", 0)
    avg_sc = round(total_sc / len(exercises), 1) if exercises else 0

    # 9. CS level distribution
    cs_level_dist = summary.get("cs_level_distribution", {})

    # 10. Languages in solutions
    lang_freq = {}
    for ex in detailed_exercises:
        for lang in ex.get("solution_languages", []):
            lang_freq[lang] = lang_freq.get(lang, 0) + 1

    # 11. helpTip presence
    tips_total = 0
    tips_present = 0
    for ex in detailed_exercises:
        for sc in ex.get("scenarios", []):
            tips_total += 1
            if sc.get("help_tip"):
                tips_present += 1

    # 12. Test type per difficulty level
    type_by_difficulty = {}
    for ex in detailed_exercises:
        diff = ex.get("difficulty", "E")
        for t, c in ex.get("stats", {}).get("types", {}).items():
            key = f"{diff}"
            if key not in type_by_difficulty:
                type_by_difficulty[key] = {}
            type_by_difficulty[key][t] = type_by_difficulty[key].get(t, 0) + c

    # Build stats object
    stats = {
        "generated_at": corpus.get("generated_at", ""),
        "totals": {
            "exercises": len(exercises),
            "scenarios": total_sc,
            "test_cases": total_tc,
            "skills": len(skills_freq),
            "avg_test_cases_per_exercise": avg_tc,
            "avg_scenarios_per_exercise": avg_sc,
        },
        "distribution_by_difficulty": dict(
            sorted(difficulty_dist.items(), key=lambda x: x[0])
        ),
        "distribution_by_cs_level": cs_level_dist,
        "distribution_by_test_type": dict(
            sorted(test_type_dist.items(), key=lambda x: -x[1])
        ),
        "scenarios_per_level": dict(
            sorted(scenario_levels.items(), key=lambda x: x[0])
        ),
        "skills_frequency": dict(
            sorted(skills_freq.items(), key=lambda x: -x[1])
        ),
        "false_green_coverage": {
            "with_false_green": fg_with,
            "without_false_green": fg_without,
            "percentage": round(fg_with / len(exercises) * 100, 1) if exercises else 0,
        },
        "performance_coverage": {
            "with_performance": perf_with,
            "without_performance": perf_without,
            "percentage": round(perf_with / len(exercises) * 100, 1) if exercises else 0,
        },
        "solution_languages": dict(
            sorted(lang_freq.items(), key=lambda x: -x[1])
        ),
        "help_tips": {
            "total_scenarios": tips_total,
            "with_tip": tips_present,
            "coverage_pct": round(tips_present / tips_total * 100, 1) if tips_total else 0,
        },
        "type_by_difficulty": type_by_difficulty,
    }

    # Write stats.json
    stats_path = data_path / "stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print(f"📊 Stats generated: {stats_path}")
    print(f"   Exercises: {stats['totals']['exercises']}")
    print(f"   Scenarios: {stats['totals']['scenarios']}")
    print(f"   Test Cases: {stats['totals']['test_cases']}")
    print(f"   Skills: {stats['totals']['skills']}")
    print(f"   FALSE_GREEN coverage: {stats['false_green_coverage']['percentage']}%")
    print(f"   PERFORMANCE coverage: {stats['performance_coverage']['percentage']}%")
    print(f"   HelpTip coverage: {stats['help_tips']['coverage_pct']}%")


if __name__ == "__main__":
    main()
