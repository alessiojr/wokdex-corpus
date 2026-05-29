#!/usr/bin/env python3
"""
WOKDEX Corpus Extractor
========================
Reads exercise directories from the corpus (organized by CS level)
and generates static JSON files consumed by the GitHub Pages site.

Usage:
    python extract_corpus.py [--config ../config.yaml]
"""

import argparse
import html as html_module
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml


def load_config(config_path: Path) -> dict:
    """Load config.yaml and extract relevant settings."""
    if not config_path.exists():
        print(f"⚠️  Config not found at {config_path}, using defaults")
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

DIFFICULTY_LABELS = {
    "A": "Avançado",
    "B": "Especialista",
    "C": "Intermediário",
    "D": "Iniciante",
    "E": "Fundamentos",
}

DIFFICULTY_TO_CS = {
    "E": "CS1",
    "D": "CS1",
    "C": "CS2",
    "B": "CS2",
    "A": "CS3",
}


def safe_read(path: Path) -> str:
    """Read a file, returning empty string on failure."""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def sanitize_readme(readme_text: str) -> str:
    """Remove internal sync/API status lines and clean up the README."""
    lines = readme_text.split("\n")
    filtered = []
    for line in lines:
        # Skip Sync Status lines (internal info)
        if "Sync Status:" in line:
            continue
        # Skip API sync info in tables
        if "DB Sync" in line and "|" in line:
            # Remove the DB Sync column from table headers
            pass  # keep it but we'll handle in HTML
        filtered.append(line)
    return "\n".join(filtered)


def markdown_to_html(md_text: str) -> str:
    """Convert Markdown to HTML with basic formatting support.
    
    Supports: headers, bold, italic, code, code blocks, tables,
    lists, links, and horizontal rules.
    """
    md_text = sanitize_readme(md_text)
    lines = md_text.split("\n")
    html_lines = []
    in_code_block = False
    in_table = False
    in_list = False
    table_has_header = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                lang = stripped[3:].strip()
                html_lines.append(f'<pre><code class="lang-{lang}">' if lang else "<pre><code>")
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(html_module.escape(line))
            continue

        # Empty line
        if not stripped:
            if in_table:
                html_lines.append("</tbody></table></div>")
                in_table = False
                table_has_header = False
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("")
            continue

        # Tables
        if "|" in stripped and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            # Skip separator rows (|:---|:---|)
            if all(re.match(r'^[:\-]+$', c) for c in cells):
                continue

            if not in_table:
                html_lines.append('<div class="table-wrapper"><table>')
                html_lines.append("<thead><tr>")
                for cell in cells:
                    html_lines.append(f"<th>{inline_md(cell)}</th>")
                html_lines.append("</tr></thead><tbody>")
                in_table = True
                table_has_header = True
                continue
            else:
                html_lines.append("<tr>")
                for cell in cells:
                    html_lines.append(f"<td>{inline_md(cell)}</td>")
                html_lines.append("</tr>")
                continue

        # Close table if we hit a non-table line
        if in_table and not stripped.startswith("|"):
            html_lines.append("</tbody></table></div>")
            in_table = False
            table_has_header = False

        # Headers
        hdr_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if hdr_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            level = len(hdr_match.group(1))
            # Bump all headers by 1 level since we show title separately
            level = min(level + 1, 6)
            text = inline_md(hdr_match.group(2))
            html_lines.append(f"<h{level}>{text}</h{level}>")
            continue

        # Unordered lists
        list_match = re.match(r'^\s*[-*+]\s+(.+)$', stripped)
        if list_match:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{inline_md(list_match.group(1))}</li>")
            continue

        # Indented sub-list items
        sub_list_match = re.match(r'^\s{2,}[-*+]\s+(.+)$', line)
        if sub_list_match:
            html_lines.append(f"<li style='margin-left:1.5rem;'>{inline_md(sub_list_match.group(1))}</li>")
            continue

        # Horizontal rule
        if re.match(r'^---+$', stripped):
            html_lines.append("<hr>")
            continue

        # Close list if paragraph
        if in_list:
            html_lines.append("</ul>")
            in_list = False

        # Paragraph
        html_lines.append(f"<p>{inline_md(stripped)}</p>")

    # Close open elements
    if in_code_block:
        html_lines.append("</code></pre>")
    if in_table:
        html_lines.append("</tbody></table></div>")
    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def inline_md(text: str) -> str:
    """Convert inline markdown elements to HTML."""
    # Escape HTML entities first (except our own tags)
    # Code (backticks) - do this before other replacements
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold + Italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # Checkmarks (emoji-like)
    text = text.replace("✅", '<span style="color:var(--accent-green)">✅</span>')
    text = text.replace("❌", '<span style="color:var(--accent-red)">❌</span>')
    return text


def extract_overview(readme_text: str) -> str:
    """Extract the Overview section from a README.md file."""
    match = re.search(
        r"## Overview\s*\n(.*?)(?=\n## |\Z)", readme_text, re.DOTALL
    )
    if match:
        return match.group(1).strip()
    return ""


def count_test_files(test_cases_dir: Path) -> dict:
    """Count .in/.out files in each scenario subdirectory."""
    counts = {}
    if not test_cases_dir.is_dir():
        return counts
    for scenario_dir in sorted(test_cases_dir.iterdir()):
        if scenario_dir.is_dir():
            in_files = list(scenario_dir.glob("*.in"))
            counts[scenario_dir.name] = len(in_files)
    return counts


def count_solutions(solutions_dir: Path) -> list:
    """List solution languages found in solutions/ subdirs."""
    langs = set()
    if not solutions_dir.is_dir():
        return []
    for sol_dir in solutions_dir.iterdir():
        if sol_dir.is_dir():
            for f in sol_dir.iterdir():
                ext = f.suffix.lower()
                lang_map = {
                    ".java": "java",
                    ".py": "python",
                    ".cpp": "cpp",
                    ".c": "c",
                    ".js": "javascript",
                    ".cs": "csharp",
                    ".pas": "pascal",
                    ".lua": "lua",
                    ".php": "php",
                    ".sh": "bash",
                    ".rb": "ruby",
                    ".go": "go",
                }
                if ext in lang_map:
                    langs.add(lang_map[ext])
    return sorted(langs)


def count_statements_languages(statements_dir: Path) -> list:
    """Detect natural languages from statement files."""
    langs = set()
    if not statements_dir.is_dir():
        return []
    for stmt_dir in statements_dir.iterdir():
        if stmt_dir.is_dir():
            for f in stmt_dir.iterdir():
                name = f.name.lower()
                if "_pt_" in name or "_pt." in name:
                    langs.add("pt")
                if "_en_" in name or "_en." in name:
                    langs.add("en")
                if "_es_" in name or "_es." in name:
                    langs.add("es")
    return sorted(langs)


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

def extract_exercise(exercise_dir: Path) -> dict | None:
    """Extract all relevant data from a single exercise directory."""
    metadata_path = exercise_dir / "metadata.yaml"
    readme_path = exercise_dir / "README.md"
    analysis_path = exercise_dir / "ANALYSIS.md"
    test_cases_dir = exercise_dir / "test-cases"
    solutions_dir = exercise_dir / "solutions"
    statements_dir = exercise_dir / "statements"

    if not metadata_path.exists():
        print(f"  ⚠️  Skipping {exercise_dir.name}: no metadata.yaml")
        return None

    # Parse YAML
    try:
        with open(metadata_path, "r", encoding="utf-8") as f:
            meta = yaml.safe_load(f)
    except Exception as e:
        print(f"  ❌ Error parsing {metadata_path}: {e}")
        return None

    if not meta:
        print(f"  ⚠️  Skipping {exercise_dir.name}: empty metadata.yaml")
        return None

    # Extract README overview and full HTML
    readme_text = safe_read(readme_path)
    overview = extract_overview(readme_text)
    readme_html = markdown_to_html(readme_text) if readme_text else ""

    # Extract ANALYSIS validation status
    analysis_text = safe_read(analysis_path)
    validation = {
        "statements_ok": "statements" in analysis_text.lower()
        and "✅" in analysis_text.split("statements")[0:2][-1]
        if "statements" in analysis_text.lower()
        else False,
        "solutions_ok": "solutions" in analysis_text.lower()
        and "FOUND" in analysis_text
        if "solutions" in analysis_text.lower()
        else False,
        "test_cases_ok": "test-cases" in analysis_text.lower()
        and "FOUND" in analysis_text
        if "test-cases" in analysis_text.lower()
        else False,
    }

    # Count physical test files
    tc_counts = count_test_files(test_cases_dir)
    total_test_cases = sum(tc_counts.values())

    # Process test scenarios from YAML
    scenarios = []
    type_dist = {}
    level_dist = {}
    yaml_scenarios = meta.get("testScenarios", []) or []

    for sc in yaml_scenarios:
        if not isinstance(sc, dict):
            continue
        sc_id = sc.get("id", "unknown")
        test_type = sc.get("testType", "TDD")
        level = sc.get("level", "C")

        # Normalize test type names
        test_type_normalized = test_type.upper().replace("-", "_")
        if "FALSE" in test_type_normalized and "GREEN" in test_type_normalized:
            test_type_normalized = "TDD_FALSE_GREEN"
        elif test_type_normalized in ("FALSE-GREEN", "FALSE_GREEN", "FALSEGREEN"):
            test_type_normalized = "TDD_FALSE_GREEN"

        type_dist[test_type_normalized] = type_dist.get(test_type_normalized, 0) + 1
        level_dist[level] = level_dist.get(level, 0) + 1

        scenario_data = {
            "id": sc_id,
            "name": sc.get("name", sc_id),
            "description": sc.get("description", ""),
            "level": level,
            "test_type": test_type_normalized,
            "help_tip": sc.get("helpTip", ""),
            "skills": sc.get("skills", []),
            "test_case_count": tc_counts.get(sc_id, 0),
        }
        scenarios.append(scenario_data)

    # Process solutions from YAML
    yaml_solutions = meta.get("solutions", []) or []
    solutions_data = []
    for sol in yaml_solutions:
        if not isinstance(sol, dict):
            continue
        impl_langs = []
        for impl in sol.get("implementations", []):
            if isinstance(impl, dict):
                impl_langs.append(impl.get("language", "unknown"))
        solutions_data.append(
            {
                "id": sol.get("id", "unknown"),
                "name": sol.get("name", ""),
                "description": sol.get("description", ""),
                "level": sol.get("level", "C"),
                "languages": impl_langs,
            }
        )

    # Process statements from YAML
    yaml_statements = meta.get("statements", []) or []
    statements_data = []
    for stmt in yaml_statements:
        if not isinstance(stmt, dict):
            continue
        stmt_skills = []
        for ts in stmt.get("thematicSkills", []):
            if isinstance(ts, dict):
                stmt_skills.append(ts.get("skill", ""))
        statements_data.append(
            {
                "id": stmt.get("id", "unknown"),
                "level": stmt.get("testScenarioLevel", "A"),
                "thematic_skills": stmt_skills,
            }
        )

    # Detect languages from file system
    solution_languages = count_solutions(solutions_dir)
    natural_languages = count_statements_languages(statements_dir)

    # Skills
    skills = meta.get("skills", []) or []

    # Difficulty
    difficulty = meta.get("difficultyLevelId", "E")

    # Build exercise object
    exercise = {
        "id": exercise_dir.name,
        "numeric_id": meta.get("id", 0),
        "name": meta.get("name", exercise_dir.name),
        "slug": meta.get("slug", exercise_dir.name),
        "version": str(meta.get("version", "1.0")),
        "difficulty": difficulty,
        "difficulty_label": DIFFICULTY_LABELS.get(difficulty, "Desconhecido"),
        "cs_level": DIFFICULTY_TO_CS.get(difficulty, "CS1"),
        "origin": meta.get("origin", "unknown"),
        "author": meta.get("authorSlugProblem", meta.get("author", "unknown")),
        "time_complexity": meta.get("timeComplexity", "N/A"),
        "space_complexity": meta.get("spaceComplexity", "N/A"),
        "time_limit_secs": meta.get("timeLimitSegs", meta.get("timelimit", 1)),
        "memory_limit_mb": meta.get("memoryLimitMb", meta.get("memlimit", 128)),
        "skills": skills,
        "description": meta.get("description", ""),
        "editorial": meta.get("editorial", ""),
        "success_msg": meta.get("successmsg", ""),
        "overview": overview,
        "readme_html": readme_html,
        "github_url": "",  # set by caller with CS level path
        "scenarios": scenarios,
        "solutions": solutions_data,
        "statements": statements_data,
        "solution_languages": solution_languages,
        "natural_languages": natural_languages,
        "stats": {
            "total_scenarios": len(scenarios),
            "total_test_cases": total_test_cases,
            "types": type_dist,
            "levels": level_dist,
            "has_false_green": "TDD_FALSE_GREEN" in type_dist,
            "has_performance": "PERFORMANCE" in type_dist,
            "solution_count": len(solutions_data),
            "statement_count": len(statements_data),
        },
        "validation": validation,
    }

    return exercise


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract WOKDEX corpus data into JSON files."
    )
    parser.add_argument(
        "--config", default="config.yaml",
        help="Path to config.yaml (default: config.yaml in project root)"
    )
    args = parser.parse_args()

    # Load config
    config_path = Path(args.config).resolve()
    config = load_config(config_path)
    project_root = config_path.parent

    corpus_path = project_root / "corpus"
    output_path = project_root / "data"

    # GitHub URLs from config
    github_url = config.get("repositories", {}).get("github", {}).get("url", "")
    github_branch = config.get("repositories", {}).get("github", {}).get("branch", "master")
    github_corpus_base = f"{github_url}/tree/{github_branch}/corpus" if github_url else ""

    # Article metadata from config
    article_config = config.get("article", {})

    if not corpus_path.is_dir():
        print(f"❌ Corpus directory not found: {corpus_path}")
        sys.exit(1)

    # Create output directories
    exercises_output = output_path / "exercises"
    exercises_output.mkdir(parents=True, exist_ok=True)

    # Discover exercise directories inside cs1/, cs2/, cs3/
    exercise_dirs = []
    cs_levels = ["cs1", "cs2", "cs3"]
    exercise_cs_map = {}  # exercise_dir_name -> cs_level

    for cs_level in cs_levels:
        cs_dir = corpus_path / cs_level
        if not cs_dir.is_dir():
            continue
        for d in sorted(cs_dir.iterdir()):
            if d.is_dir() and re.match(r"^\d{4}-", d.name):
                exercise_dirs.append(d)
                exercise_cs_map[d.name] = cs_level

    # Also scan flat corpus/ for backward compatibility
    for d in sorted(corpus_path.iterdir()):
        if d.is_dir() and re.match(r"^\d{4}-", d.name):
            if d.name not in exercise_cs_map:
                exercise_dirs.append(d)
                exercise_cs_map[d.name] = "flat"

    exercise_dirs.sort(key=lambda d: d.name)

    print(f"🔍 Found {len(exercise_dirs)} exercise(s) in {corpus_path}")
    print()

    # Extract each exercise
    exercises = []
    all_skills = set()
    all_types = set()

    for ex_dir in exercise_dirs:
        cs = exercise_cs_map.get(ex_dir.name, "flat")
        print(f"📄 Processing {cs}/{ex_dir.name}...")
        exercise = extract_exercise(ex_dir)
        if exercise:
            # Set GitHub URL with CS level path
            if github_corpus_base and cs != "flat":
                exercise["github_url"] = f"{github_corpus_base}/{cs}/{ex_dir.name}"
            elif github_corpus_base:
                exercise["github_url"] = f"{github_corpus_base}/{ex_dir.name}"

            exercises.append(exercise)
            all_skills.update(exercise["skills"])
            all_types.update(exercise["stats"]["types"].keys())

            # Write individual JSON
            ex_json_path = exercises_output / f"{exercise['id']}.json"
            with open(ex_json_path, "w", encoding="utf-8") as f:
                json.dump(exercise, f, ensure_ascii=False, indent=2)
            print(f"  ✅ → {ex_json_path.name}")

    print()

    # Compute summary
    total_scenarios = sum(e["stats"]["total_scenarios"] for e in exercises)
    total_test_cases = sum(e["stats"]["total_test_cases"] for e in exercises)

    # Aggregate type distribution
    agg_types = {}
    for e in exercises:
        for t, c in e["stats"]["types"].items():
            agg_types[t] = agg_types.get(t, 0) + c

    # Aggregate difficulty distribution
    agg_difficulty = {}
    for e in exercises:
        d = e["difficulty"]
        agg_difficulty[d] = agg_difficulty.get(d, 0) + 1

    # Aggregate CS level distribution
    agg_cs_level = {}
    for e in exercises:
        cs = e["cs_level"]
        agg_cs_level[cs] = agg_cs_level.get(cs, 0) + 1

    # Aggregate skills frequency
    skills_freq = {}
    for e in exercises:
        for s in e["skills"]:
            skills_freq[s] = skills_freq.get(s, 0) + 1
        for sc in e["scenarios"]:
            for sk in sc.get("skills", []):
                if isinstance(sk, dict):
                    skill_name = sk.get("skill", "")
                    if skill_name:
                        skills_freq[skill_name] = skills_freq.get(skill_name, 0) + 1

    # Build corpus index
    corpus_index = {
        "generated_at": datetime.now().isoformat(),
        "github_repo_url": github_url,
        "github_corpus_base": github_corpus_base,
        "article": {
            "title": article_config.get("title", "WOKDEX Corpus"),
            "title_en": article_config.get("title_en", ""),
            "venue": article_config.get("venue", ""),
            "track": article_config.get("track", ""),
            "year": article_config.get("year", 2026),
            "authors": article_config.get("authors", ""),
        },
        "summary": {
            "total_exercises": len(exercises),
            "total_scenarios": total_scenarios,
            "total_test_cases": total_test_cases,
            "difficulty_distribution": agg_difficulty,
            "cs_level_distribution": agg_cs_level,
            "test_type_distribution": agg_types,
            "false_green_count": sum(
                1 for e in exercises if e["stats"]["has_false_green"]
            ),
            "performance_count": sum(
                1 for e in exercises if e["stats"]["has_performance"]
            ),
            "all_skills": sorted(skills_freq.keys()),
            "skills_frequency": dict(
                sorted(skills_freq.items(), key=lambda x: -x[1])
            ),
        },
        "exercises": [
            {
                "id": e["id"],
                "name": e["name"],
                "slug": e["slug"],
                "difficulty": e["difficulty"],
                "difficulty_label": e["difficulty_label"],
                "cs_level": e["cs_level"],
                "time_complexity": e["time_complexity"],
                "skills": e["skills"],
                "overview": e["overview"][:200] + ("..." if len(e["overview"]) > 200 else ""),
                "scenarios_count": e["stats"]["total_scenarios"],
                "test_cases_count": e["stats"]["total_test_cases"],
                "has_false_green": e["stats"]["has_false_green"],
                "has_performance": e["stats"]["has_performance"],
                "solution_languages": e["solution_languages"],
            }
            for e in exercises
        ],
    }

    # Write corpus.json
    corpus_json_path = output_path / "corpus.json"
    with open(corpus_json_path, "w", encoding="utf-8") as f:
        json.dump(corpus_index, f, ensure_ascii=False, indent=2)
    print(f"📦 Corpus index: {corpus_json_path}")

    # Print summary
    print()
    print("=" * 60)
    print(f"✅ Extraction complete!")
    print(f"   Exercises:   {len(exercises)}")
    print(f"   Scenarios:   {total_scenarios}")
    print(f"   Test Cases:  {total_test_cases}")
    print(f"   Skills:      {len(skills_freq)}")
    print(f"   Types:       {agg_types}")
    print(f"   FALSE_GREEN: {corpus_index['summary']['false_green_count']} exercises")
    print(f"   PERFORMANCE: {corpus_index['summary']['performance_count']} exercises")
    print("=" * 60)


if __name__ == "__main__":
    main()
