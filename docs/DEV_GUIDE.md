# Developer Guide

This repository is maintained as a reusable learning system. Prefer small, reviewable changes that improve future Codex runs.

## Directory Responsibilities

- `config/`: editable learner profile, study preferences, curriculum defaults, and source policy.
- `docs/`: operating rules for humans and Codex.
- `prompts/`: reusable prompt templates for recurring tasks.
- `curriculum/`: long-term roadmap, module definitions, and weekly YAML plans.
- `resources/`: vetted source index and short source notes.
- `notes/`: generated daily learning notes.
- `exercises/`: problem sets, informal drills, and exercise indexes.
- `labs/`: Python experiments tied to learning goals.
- `review/`: glossary, flashcards, and weekly retrospectives.
- `state/`: current progress, open questions, mistakes, proof weaknesses, and next actions.
- `templates/`: reusable Markdown, LaTeX, YAML, and Python templates.
- `scripts/`: small standard-library automation.
- `context/`: compact context for the next Codex session.

## Naming Rules

- Weeks: `weekXX-slug`, for example `week01-foundations`.
- Days: `dayDD-slug`, for example `day03-probability`.
- Notes: `notes/weekXX/dayDD-slug.md`.
- Exercises: `exercises/weekXX/dayDD-slug.md` or `exercises/weekXX/problem_set.tex`.
- Labs: `labs/weekXX/dayDD-slug.py` or `labs/weekXX/lab_slug.py`.
- Weekly plans: `curriculum/weeks/weekXX-slug.yaml`.
- Weekly reviews: `review/weekly_reviews/weekXX-slug.md`.

Use lowercase slugs with hyphens. Keep titles human-readable inside files.

## Add a New Week

Run:

```bash
python scripts/new_week.py --week 2 --slug randomized-algorithms
```

Then ask Codex to use `prompts/01_generate_week.md`. The week YAML must follow `docs/CURRICULUM_SCHEMA.md` and include resources, expected outputs, review tasks, and links to future modules.

## Add a New Day

Run:

```bash
python scripts/new_day.py --week 2 --day 3 --slug concentration
```

Then ask Codex to use `prompts/02_generate_day.md`. A day note should include definitions, examples, proof work, exercises, self-test, and state updates.

## Add a Module

1. Create `curriculum/modules/module_name.yaml`.
2. Include purpose, prerequisites, core_topics, typical_outputs, and depends_on.
3. Add it to `curriculum/roadmap.yaml`.
4. If the module introduces new rigor requirements, update `docs/CONTENT_STYLE_GUIDE.md`.

## Add a Resource

1. Check `config/resource_policy.yaml`.
2. Add an entry to `resources/sources.yaml`.
3. Add notes in `resources/source_notes/` only if useful.
4. Run:

```bash
python scripts/validate_sources.py
```

Never use pirated scans, unauthorized mirrors, or copied solution dumps.

## Generate a Problem Set

Use `prompts/03_generate_problem_set.md` and `templates/problem_set_template.tex`. A problem set should list prerequisites, difficulty, allowed references, and what each problem tests. Include warmup, core, and challenge problems.

## Generate a Lab

Use `prompts/05_generate_lab.md` and `templates/lab_template.py`. A lab must be directly runnable, use standard library unless justified, include asserts, and explain what intuition it probes.

## Update Context

After any meaningful task:

1. Summarize modified files in `context/last_codex_summary.md`.
2. Write the next useful prompt in `context/next_codex_prompt.md`.
3. Update `state/next_actions.md`.
4. Run:

```bash
python scripts/export_context_pack.py
```

## Quality Checks

Before ending a task, use `docs/QUALITY_CHECKS.md`. At minimum:

```bash
python scripts/validate_structure.py
python scripts/build_flashcards.py
```

If sources changed, also run `python scripts/validate_sources.py`. If Python labs changed, run them directly.

