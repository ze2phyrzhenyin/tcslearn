#!/usr/bin/env python3
"""Create a new day skeleton."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def clean_slug(slug: str) -> str:
    slug = slug.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-") or "topic"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a day note and exercise skeleton.")
    parser.add_argument("--week", type=int, required=True)
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", default=None)
    args = parser.parse_args()

    week_dir = f"week{args.week:02d}"
    day_id = f"day{args.day:02d}-{clean_slug(args.slug)}"
    title = args.title or clean_slug(args.slug).replace("-", " ").title()

    notes_dir = ROOT / "notes" / week_dir
    exercises_dir = ROOT / "exercises" / week_dir
    notes_dir.mkdir(parents=True, exist_ok=True)
    exercises_dir.mkdir(parents=True, exist_ok=True)

    note_file = notes_dir / f"{day_id}.md"
    exercise_file = exercises_dir / f"{day_id}.md"

    if not note_file.exists():
        note_file.write_text(
            f"""# {day_id} - {title}

Week: {week_dir}
Date generated: {date.today().isoformat()}

## Learning Goals

- TODO

## Prerequisites

- TODO

## Precise Definitions

### TODO Term

Formal definition:

> TODO

Motivation:

TODO

Minimal example:

TODO

Non-example:

TODO

Why the non-example fails:

TODO

## Intuition

TODO

## Theorem / Lemma / Claim

Statement:

TODO

Assumptions:

- TODO

Proof idea:

TODO

## Worked Examples

TODO

## Common Mistakes

- TODO

## Exercises

See `exercises/{week_dir}/{day_id}.md`.

## Self-test

- TODO

## Connection to Larger TCS Goals

TODO
""",
            encoding="utf-8",
        )

    if not exercise_file.exists():
        exercise_file.write_text(
            f"""# Exercises: {day_id}

## Warmup

1. TODO

## Core

1. TODO

## Challenge

1. TODO

## Hints

- TODO
""",
            encoding="utf-8",
        )

    print(f"Created or verified {day_id}.")
    print(f"- {note_file.relative_to(ROOT)}")
    print(f"- {exercise_file.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

