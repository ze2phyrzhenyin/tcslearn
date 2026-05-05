# Study Workflow

Use this process each study day. The goal is active recall and repair, not passive reading.

## 1. Read Today's Plan

Open the current week YAML in `curriculum/weeks/` and identify today's `day_id`, topic, prerequisites, outputs, and exercises. If the day depends on a definition you do not remember, mark it in `state/open_questions.md` before starting.

## 2. Read Notes Once

Read the daily note in `notes/weekXX/dayDD-slug.md` once from top to bottom. Do not edit yet. Mark three things:

- definitions you must memorize exactly;
- examples that explain the definition;
- claims or theorems that require proof.

## 3. Handwrite Definitions

Close the note and write each definition by hand. For each definition, write:

- the formal statement;
- one example;
- one non-example;
- why the non-example fails.

Then reopen the note and correct missing quantifiers, domain restrictions, or notation.

## 4. Work Through Examples

Redo the minimal examples without looking. If the topic is algorithmic, run through the input, output, invariant, and complexity variables. If the topic is probabilistic, write the sample space before computing anything.

## 5. Do Exercises

Attempt exercises before reading solutions. For each proof exercise:

1. Restate the claim.
2. List assumptions.
3. Write the goal.
4. Choose a proof strategy.
5. Fill in the proof.
6. Check each step against a definition or previous result.

If stuck for more than 20 minutes, write exactly where the proof fails and move to the hint or solution.

## 6. Read Solutions

Compare your work with the solution. Do not just mark correct or wrong. Identify:

- missing assumption;
- invalid inference;
- undefined term;
- wrong variable in Big-O;
- probability space error;
- intuition used as proof.

## 7. Repair Mistakes

Write every important mistake in `state/mistakes_log.md` using this pattern:

```markdown
## YYYY-MM-DD - Topic

- Mistake:
- Why it was wrong:
- Correct idea:
- Repair exercise:
- Status: open
```

For proof-specific issues, also update `state/proof_weaknesses.md`.

## 8. Update Open Questions

If a concept is still unclear, write it in `state/open_questions.md` with:

- question;
- source or file;
- why it blocks progress;
- next action.

## 9. Make Flashcards

Add only cards worth reviewing. Use `review/flashcards.md`:

```markdown
- Q: What does it mean for a set family to be shattered?
  A: ...
  Tags: learning-theory, vc-dimension
```

Then run:

```bash
python scripts/build_flashcards.py
```

## 10. Ask Codex for Feedback

At the end of the day, run:

```bash
python scripts/export_context_pack.py
```

Then ask Codex to use one of:

- `prompts/06_generate_review_pack.md` for review.
- `prompts/07_refactor_notes.md` for cleanup.
- `prompts/10_next_prompt_builder.md` for the next action prompt.

