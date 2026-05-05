#!/usr/bin/env python3
"""Create a new week skeleton."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def clean_slug(slug: str) -> str:
    slug = slug.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-") or "untitled"


def week_id(week: int, slug: str) -> str:
    return f"week{week:02d}-{clean_slug(slug)}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a reusable week skeleton.")
    parser.add_argument("--week", type=int, required=True, help="Week number, e.g. 1")
    parser.add_argument("--slug", required=True, help="Short lowercase slug, e.g. foundations")
    parser.add_argument("--title", default=None, help="Human title. Defaults to slug title-case.")
    args = parser.parse_args()

    wid = week_id(args.week, args.slug)
    title = args.title or clean_slug(args.slug).replace("-", " ").title()
    week_num = f"week{args.week:02d}"

    paths = [
        ROOT / "notes" / week_num,
        ROOT / "exercises" / week_num,
        ROOT / "labs" / week_num,
    ]
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

    week_file = ROOT / "curriculum" / "weeks" / f"{wid}.yaml"
    review_file = ROOT / "review" / "weekly_reviews" / f"{wid}.md"

    if not week_file.exists():
        week_file.write_text(
            f"""week_id: "{wid}"
title: "{title}"
purpose: "TODO: Explain why this week matters for long-term TCS goals."
prerequisites: []
learning_goals: []
days:
  - day_id: "day01-topic"
    title: "TODO"
    purpose: "TODO"
    topics: []
    outputs:
      note: "notes/{week_num}/day01-topic.md"
      exercises: "exercises/{week_num}/day01-topic.md"
      lab: null
    quality_focus: []
resources: []
exercises:
  problem_set: "exercises/{week_num}/problem_set.tex"
  solution_set: "exercises/{week_num}/solutions.tex"
  difficulty_mix:
    warmup: 0.3
    core: 0.5
    challenge: 0.2
labs: []
review:
  weekly_review: "review/weekly_reviews/{wid}.md"
  flashcard_tags: []
links_to_future_modules: []
difficulty_profile:
  conceptual: "medium"
  proof: "medium"
  coding: "low"
expected_outputs: []
created_on: "{date.today().isoformat()}"
""",
            encoding="utf-8",
        )

    if not review_file.exists():
        review_file.write_text(
            f"""# Weekly Review: {wid}

## Definitions I Can State

- TODO

## Proofs I Can Reconstruct

- TODO

## Mistakes That Repeated

- TODO

## Open Questions

- TODO

## Next Actions

- TODO
""",
            encoding="utf-8",
        )

    print(f"Created or verified skeleton for {wid}.")
    print(f"- {week_file.relative_to(ROOT)}")
    print(f"- {review_file.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

