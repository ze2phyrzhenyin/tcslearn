# Quality Checks

Use this checklist before ending any Codex task.

## Source Legality Check

- All sources are allowed by `config/resource_policy.yaml`.
- No pirated scans, mirrors, or copied solution dumps were used.
- `resources/sources.yaml` includes title, owner, URL, source type, and access status.
- Notes are rewritten and organized, not copied.

## Definition Completeness Check

- Every new term has a definition.
- Every definition has an example and non-example.
- Quantifiers, domains, and variables are explicit.
- Prerequisites are listed.

## Proof Rigor Check

- Each theorem has assumptions and a goal.
- Each proof has a strategy.
- No step relies only on intuition.
- Induction, contradiction, probability, and asymptotic arguments name their required conditions.
- Full proof is included when the result is central or assigned as an exercise solution.

## Exercise Solvability Check

- Every exercise is tied to material already introduced or explicitly marked as challenge.
- Difficulty is labeled.
- Hints are included when appropriate.
- Solutions exist or are scheduled in `state/next_actions.md`.

## LaTeX Syntax Check

- LaTeX files compile in principle with standard packages.
- Environments are closed.
- Math delimiters are balanced.
- Problem and solution numbering match.

## Python Test Check

- Every lab can be run directly.
- Every lab includes `assert` tests.
- Randomness is seeded or explained.
- The lab states what intuition it tests.

## Dependency Check

- Standard library is preferred.
- `numpy` is allowed for numerical experiments.
- Any extra dependency is justified in the file and `pyproject.toml`.

## File Structure Check

- New files follow naming rules in `docs/DEV_GUIDE.md`.
- Weekly YAML follows `docs/CURRICULUM_SCHEMA.md`.
- No duplicate near-identical files were created.
- Run:

```bash
python scripts/validate_structure.py
```

## Context Update Check

- `context/last_codex_summary.md` was updated.
- `context/next_codex_prompt.md` contains an immediately usable prompt.
- `state/next_actions.md` was updated.
- `state/open_questions.md` and `state/mistakes_log.md` were updated if relevant.

