# Agent Protocol

This protocol tells Codex how to work inside this repository.

## Startup Reading Order

When entering the repository, read these files first:

1. `AGENTS.md`
2. `config/learner_profile.yaml`
3. `config/resource_policy.yaml`
4. `state/progress.yaml`
5. `state/next_actions.md`
6. `context/last_codex_summary.md`
7. The prompt file named by the user, if any

For content generation, also read:

- `docs/CONTENT_STYLE_GUIDE.md`
- `docs/QUALITY_CHECKS.md`
- `docs/CURRICULUM_SCHEMA.md` when editing weekly plans

## Before Generating Content

Check:

- Current week and active module in `state/progress.yaml`.
- Open blockers in `state/open_questions.md`.
- Repeated mistakes in `state/mistakes_log.md`.
- Proof weaknesses in `state/proof_weaknesses.md`.
- Source legality in `config/resource_policy.yaml`.

If a blocker affects the requested content, either repair it first or create a small prerequisite note.

## Creating New Files

Create a new file only when it has a stable role:

- A new week plan belongs in `curriculum/weeks/`.
- A daily lesson belongs in `notes/weekXX/`.
- Formal problems belong in `exercises/weekXX/`.
- Runnable code belongs in `labs/weekXX/`.
- Reviews belong in `review/weekly_reviews/`.

Do not create throwaway files for temporary reasoning. Prefer updating existing state or context files.

## Avoiding Duplicates

Before creating a file:

1. Search for the week, day, slug, or topic.
2. If a file exists, update it instead of creating a sibling with a near-duplicate name.
3. If replacing stale content, summarize what changed in `context/last_codex_summary.md`.

## Handling Unfinished Content

If content cannot be completed:

- Mark it explicitly as `TODO` with a reason.
- Add the blocker to `state/open_questions.md`.
- Add a concrete repair action to `state/next_actions.md`.
- Do not pretend the section is finished.

## Writing `last_codex_summary.md`

Use this structure:

```markdown
# Last Codex Summary

Date: YYYY-MM-DD

## Modified Files
- path: short description

## Generated
- What was created or updated.

## Checks Run
- Command and result.

## Unresolved Issues
- Issue or "None".
```

Keep it factual and short.

## Writing `next_codex_prompt.md`

The next prompt should be immediately usable. Include:

- Which context file to read.
- Which prompt template to follow.
- The exact week/day/topic.
- Required outputs.
- Reminder to update context and state.

Do not write a vague prompt like “continue learning”.

