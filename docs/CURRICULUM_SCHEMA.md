# Curriculum Schema

Weekly plans live in `curriculum/weeks/weekXX-slug.yaml`. They are the contract between roadmap, notes, exercises, labs, review, and Codex.

## Required Fields

```yaml
week_id: "week02-randomized-algorithms"
title: "Randomized Algorithms Basics"
purpose: "What this week prepares the learner to do."
prerequisites:
  - "Precise prerequisite topic"
learning_goals:
  - "Observable goal"
days:
  - day_id: "day01-random-variables"
    title: "Random variables for algorithm analysis"
    purpose: "Why this day exists"
    topics:
      - "Random variable"
    outputs:
      note: "notes/week02/day01-random-variables.md"
      exercises: "exercises/week02/day01-random-variables.md"
      lab: null
    quality_focus:
      - "sample space"
resources:
  - source_id: "source-key-from-resources"
    use: "reading / reference / optional"
exercises:
  problem_set: "exercises/week02/problem_set.tex"
  solution_set: "exercises/week02/solutions.tex"
  difficulty_mix:
    warmup: 0.3
    core: 0.5
    challenge: 0.2
labs:
  - path: "labs/week02/random_trials.py"
    purpose: "Empirical check of intuition"
review:
  weekly_review: "review/weekly_reviews/week02-randomized-algorithms.md"
  flashcard_tags:
    - "randomized-algorithms"
links_to_future_modules:
  - module: "learning_theory"
    connection: "Generalization bounds need concentration."
difficulty_profile:
  conceptual: "medium"
  proof: "medium"
  coding: "low"
expected_outputs:
  - "5 daily notes"
  - "1 formal problem set"
  - "1 solution set"
```

## Field Notes

- `week_id`: must match filename without `.yaml`.
- `title`: human-readable.
- `purpose`: explain why the week matters for long-term TCS goals.
- `prerequisites`: list only what should already be known.
- `learning_goals`: observable outcomes, not vague topics.
- `days`: each day must point to expected note, exercise, and optional lab files.
- `resources`: reference entries in `resources/sources.yaml`.
- `exercises`: formal problem set outputs.
- `labs`: runnable Python experiments.
- `review`: weekly review and flashcard tags.
- `links_to_future_modules`: connect foundations to string algorithms, learning theory, DP, complexity, or paper reading.
- `difficulty_profile`: helps Codex decide explanation depth.
- `expected_outputs`: prevents uncontrolled file creation.

## Validation Expectations

A week is incomplete if it lacks resources, review output, or expected outputs. If solutions are deferred, the week must say where they will be generated.

