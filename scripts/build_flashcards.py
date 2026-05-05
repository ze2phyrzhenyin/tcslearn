#!/usr/bin/env python3
"""Validate and summarize flashcard Markdown files."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FLASHCARD_FILES = [ROOT / "review" / "flashcards.md"]


def validate_file(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    cards = 0
    errors: list[str] = []

    in_fence = False
    for index, line in enumerate(lines):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("- Q:"):
            answer_prefix = "  A:"
            tag_prefix = "  Tags:"
        elif line.startswith("Q:"):
            answer_prefix = "A:"
            tag_prefix = "Tag:"
        else:
            continue
        cards += 1
        window = [item.strip() for item in lines[index + 1 : index + 5]]
        if not any(item.startswith(answer_prefix.strip()) for item in window):
            errors.append(f"{path.relative_to(ROOT)}:{index + 1}: missing answer")
        if not any(item.startswith(tag_prefix.strip()) for item in window):
            errors.append(f"{path.relative_to(ROOT)}:{index + 1}: missing tag")

    return cards, errors


def main() -> int:
    files = FLASHCARD_FILES + sorted((ROOT / "review").glob("week*/flashcards_*.md"))
    total_cards = 0
    all_errors: list[str] = []

    for path in files:
        if not path.exists():
            continue
        cards, errors = validate_file(path)
        total_cards += cards
        all_errors.extend(errors)

    if all_errors:
        print("Flashcard validation failed.")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print(f"Flashcard validation passed: {total_cards} cards across {len(files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
