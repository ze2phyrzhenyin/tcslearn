#!/usr/bin/env python3
"""Validate that the TCS Selfstudy OS repository skeleton exists."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "config",
    "docs",
    "prompts",
    "curriculum/modules",
    "curriculum/weeks",
    "resources/source_notes",
    "notes",
    "exercises",
    "labs",
    "review/weekly_reviews",
    "state",
    "templates",
    "scripts",
    "context",
]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "Makefile",
    "pyproject.toml",
    ".gitignore",
    "config/learner_profile.yaml",
    "config/study_preferences.yaml",
    "config/curriculum_defaults.yaml",
    "config/resource_policy.yaml",
    "docs/DEV_GUIDE.md",
    "docs/AGENT_PROTOCOL.md",
    "docs/STUDY_WORKFLOW.md",
    "docs/CONTENT_STYLE_GUIDE.md",
    "docs/QUALITY_CHECKS.md",
    "docs/RESOURCE_POLICY.md",
    "docs/CURRICULUM_SCHEMA.md",
    "docs/PROMPTING_GUIDE.md",
    "prompts/README.md",
    "prompts/00_bootstrap_framework.md",
    "prompts/01_generate_week.md",
    "prompts/02_generate_day.md",
    "prompts/03_generate_problem_set.md",
    "prompts/04_generate_solutions.md",
    "prompts/05_generate_lab.md",
    "prompts/06_generate_review_pack.md",
    "prompts/07_refactor_notes.md",
    "prompts/08_source_audit.md",
    "prompts/09_weekly_retrospective.md",
    "prompts/10_next_prompt_builder.md",
    "curriculum/README.md",
    "curriculum/roadmap.yaml",
    "curriculum/modules/mathematical_foundations.yaml",
    "curriculum/modules/algorithms_foundations.yaml",
    "curriculum/modules/string_algorithms.yaml",
    "curriculum/modules/learning_theory.yaml",
    "curriculum/modules/differential_privacy.yaml",
    "curriculum/modules/complexity_theory.yaml",
    "resources/sources.yaml",
    "labs/README.md",
    "review/glossary.md",
    "review/flashcards.md",
    "state/progress.yaml",
    "state/open_questions.md",
    "state/mistakes_log.md",
    "state/proof_weaknesses.md",
    "state/next_actions.md",
    "templates/daily_note_template.md",
    "templates/theorem_note_template.tex",
    "templates/proof_template.md",
    "templates/algorithm_analysis_template.md",
    "templates/problem_set_template.tex",
    "templates/solution_template.tex",
    "templates/lab_template.py",
    "templates/weekly_plan_template.md",
    "templates/weekly_review_template.md",
    "templates/source_entry_template.yaml",
    "templates/next_codex_prompt_template.md",
    "scripts/new_week.py",
    "scripts/new_day.py",
    "scripts/validate_structure.py",
    "scripts/validate_sources.py",
    "scripts/export_context_pack.py",
    "scripts/build_flashcards.py",
    "context/current_context.md",
    "context/next_codex_prompt.md",
    "context/last_codex_summary.md",
]


def main() -> int:
    missing_dirs = [path for path in REQUIRED_DIRS if not (ROOT / path).is_dir()]
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]

    if missing_dirs or missing_files:
        print("Structure validation failed.")
        if missing_dirs:
            print("Missing directories:")
            for path in missing_dirs:
                print(f"  - {path}")
        if missing_files:
            print("Missing files:")
            for path in missing_files:
                print(f"  - {path}")
        return 1

    print(f"Structure validation passed: {len(REQUIRED_DIRS)} dirs, {len(REQUIRED_FILES)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

