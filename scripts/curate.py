#!/usr/bin/env python3
"""
WOKDEX Corpus Curator
======================
Imports exercises from pack-tecnicas workspace into the corpus,
organized by CS level, with sanitization of internal data.

Usage:
    python curate.py [--config ../config.yaml]
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml


def load_config(config_path: Path) -> dict:
    """Load and validate config.yaml."""
    if not config_path.exists():
        print(f"❌ Config not found: {config_path}")
        sys.exit(1)
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def sanitize_readme(readme_path: Path, config: dict) -> None:
    """Remove internal/private information from README.md."""
    if not readme_path.exists():
        return

    text = readme_path.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    filtered = []

    publish = config.get("publish", {})
    strip_sync = publish.get("strip_sync_status", True)
    strip_api = publish.get("strip_api_info", True)

    for line in lines:
        # Skip Sync Status lines
        if strip_sync and "Sync Status:" in line:
            continue
        # Skip DB Sync column in tables (remove last column)
        if strip_api and "DB Sync" in line and "|" in line:
            # Remove the last column from the table line
            parts = line.split("|")
            if len(parts) > 3:
                line = "|".join(parts[:-2]) + "|"
        filtered.append(line)

    # Also strip DB Sync data column from table rows that follow
    final = []
    in_scenario_table = False
    db_sync_col_count = 0
    for line in filtered:
        stripped = line.strip()
        if "Name" in stripped and "Description" in stripped and "Type" in stripped and "|" in stripped:
            # Count columns to detect if DB Sync was in header
            cols = [c.strip() for c in stripped.split("|") if c.strip()]
            db_sync_col_count = len(cols)
            in_scenario_table = True
        elif in_scenario_table and stripped and not stripped.startswith("|"):
            in_scenario_table = False

        if strip_api and in_scenario_table and "|" in stripped:
            parts = line.split("|")
            # If the row has more columns than expected (has DB Sync), trim last
            if len(parts) > db_sync_col_count + 1:
                line = "|".join(parts[:-2]) + "|"

        final.append(line)

    readme_path.write_text("\n".join(final), encoding="utf-8")


def curate_exercise(
    exercise_id: str,
    cs_level: str,
    source_dir: Path,
    corpus_dir: Path,
    config: dict,
) -> bool:
    """Copy and sanitize a single exercise from source to corpus."""
    src = source_dir / exercise_id
    dest = corpus_dir / cs_level / exercise_id

    if not src.exists():
        print(f"  ⚠️  Source not found: {src}")
        return False

    # Remove existing destination
    if dest.exists():
        shutil.rmtree(dest)

    # Copy structure
    dest.mkdir(parents=True, exist_ok=True)

    publish = config.get("publish", {})

    # Copy metadata.yaml (always)
    src_meta = src / "metadata.yaml"
    if src_meta.exists():
        shutil.copy2(src_meta, dest / "metadata.yaml")

    # Copy README.md and sanitize
    src_readme = src / "README.md"
    if src_readme.exists():
        shutil.copy2(src_readme, dest / "README.md")
        sanitize_readme(dest / "README.md", config)

    # Copy ANALYSIS.md
    src_analysis = src / "ANALYSIS.md"
    if src_analysis.exists():
        shutil.copy2(src_analysis, dest / "ANALYSIS.md")

    # Copy statements/
    src_stmts = src / "statements"
    if src_stmts.exists():
        shutil.copytree(src_stmts, dest / "statements", dirs_exist_ok=True)

    # Copy test-cases/ (if configured)
    if publish.get("include_test_cases", True):
        src_tc = src / "test-cases"
        if src_tc.exists():
            shutil.copytree(src_tc, dest / "test-cases", dirs_exist_ok=True)

    # Copy solutions/ (if configured)
    if publish.get("include_solutions", True):
        src_sol = src / "solutions"
        if src_sol.exists():
            shutil.copytree(src_sol, dest / "solutions", dirs_exist_ok=True)

    # Copy editorial/ (if configured)
    if publish.get("include_editorial", True):
        src_ed = src / "editorial"
        if src_ed.exists():
            shutil.copytree(src_ed, dest / "editorial", dirs_exist_ok=True)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Curate exercises from pack-tecnicas into the WOKDEX corpus."
    )
    parser.add_argument(
        "--config", default="config.yaml",
        help="Path to config.yaml (default: config.yaml in project root)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be done without actually copying"
    )
    args = parser.parse_args()

    # Resolve config path
    config_path = Path(args.config).resolve()
    config = load_config(config_path)
    project_root = config_path.parent

    # Source and corpus paths
    source_path = Path(config["source"]["pack_tecnicas_path"]).resolve()
    corpus_path = project_root / "corpus"

    if not source_path.is_dir():
        print(f"❌ Source workspace not found: {source_path}")
        sys.exit(1)

    print(f"🔍 WOKDEX Corpus Curator")
    print(f"   Config: {config_path}")
    print(f"   Source: {source_path}")
    print(f"   Corpus: {corpus_path}")
    print()

    # Ensure CS directories exist
    for cs in ["cs1", "cs2", "cs3"]:
        (corpus_path / cs).mkdir(parents=True, exist_ok=True)

    # Track what's in the corpus
    existing = set()
    for cs_dir in corpus_path.iterdir():
        if cs_dir.is_dir() and cs_dir.name.startswith("cs"):
            for ex_dir in cs_dir.iterdir():
                if ex_dir.is_dir() and re.match(r"^\d{4}-", ex_dir.name):
                    existing.add((cs_dir.name, ex_dir.name))

    # Track what should be in the corpus
    desired = set()
    exercises_config = config.get("exercises", {})
    for cs_level, exercise_ids in exercises_config.items():
        for eid in (exercise_ids or []):
            desired.add((cs_level, eid))

    # Compute diff
    to_add = desired - existing
    to_remove = existing - desired
    to_update = desired & existing

    print(f"📊 Diff:")
    print(f"   Existentes: {len(existing)}")
    print(f"   Desejados:  {len(desired)}")
    print(f"   Adicionar:  {len(to_add)}")
    print(f"   Remover:    {len(to_remove)}")
    print(f"   Atualizar:  {len(to_update)}")
    print()

    if args.dry_run:
        if to_add:
            print("  Seriam adicionados:")
            for cs, eid in sorted(to_add):
                print(f"    + {cs}/{eid}")
        if to_remove:
            print("  Seriam removidos:")
            for cs, eid in sorted(to_remove):
                print(f"    - {cs}/{eid}")
        if to_update:
            print("  Seriam atualizados:")
            for cs, eid in sorted(to_update):
                print(f"    ~ {cs}/{eid}")
        print()
        print("(dry-run: nenhuma ação executada)")
        return

    # Remove exercises not in config
    for cs, eid in sorted(to_remove):
        path = corpus_path / cs / eid
        print(f"  🗑️  Removendo {cs}/{eid}...")
        shutil.rmtree(path)

    # Add/Update exercises
    total_ok = 0
    total_fail = 0
    for cs, eid in sorted(to_add | to_update):
        action = "+" if (cs, eid) in to_add else "~"
        print(f"  {action} {cs}/{eid}...")
        ok = curate_exercise(eid, cs, source_path, corpus_path, config)
        if ok:
            total_ok += 1
            print(f"    ✅ OK")
        else:
            total_fail += 1

    print()
    print("=" * 50)
    print(f"✅ Curadoria completa!")
    print(f"   Processados: {total_ok}")
    print(f"   Falhas:      {total_fail}")
    print(f"   Removidos:   {len(to_remove)}")
    print("=" * 50)


if __name__ == "__main__":
    main()
