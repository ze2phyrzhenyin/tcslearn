#!/usr/bin/env python3
"""Validate the Astro/Starlight site content structure."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DOCS = SITE / "src" / "content" / "docs"
SOURCE_NOTE = "This page is generated from repository learning materials."

REQUIRED_FILES = [
    "site/package.json",
    "site/astro.config.mjs",
    "site/tsconfig.json",
    "site/src/content.config.ts",
    "site/src/styles/custom.css",
    "site/src/components/StudyCard.astro",
    "site/src/components/WeekOverview.astro",
    "site/src/components/DifficultyBadge.astro",
    "site/src/components/ResourceList.astro",
    "site/src/components/ProgressPanel.astro",
    "site/public/favicon.svg",
]

REQUIRED_PAGES = [
    "index.mdx",
    "start-here.mdx",
    "learning-system/overview.mdx",
    "learning-system/daily-workflow.mdx",
    "learning-system/weekly-workflow.mdx",
    "learning-system/how-to-use-codex.mdx",
    "week01/overview.mdx",
    "week01/day01.mdx",
    "week01/day02.mdx",
    "week01/day03.mdx",
    "week01/day04.mdx",
    "week01/day05.mdx",
    "week01/day06.mdx",
    "week01/day07.mdx",
    "exercises/week01-problem-set.mdx",
    "exercises/week01-solutions.mdx",
    "labs/overview.mdx",
    "labs/week01-asymptotics.mdx",
    "labs/week01-recurrence.mdx",
    "labs/week01-probability.mdx",
    "labs/week01-automata.mdx",
    "review/week01-review.mdx",
    "review/glossary.mdx",
    "review/flashcards.mdx",
    "review/mistakes-to-watch.mdx",
    "meta/resources.mdx",
    "meta/progress.mdx",
    "meta/next-actions.mdx",
]

GENERATED_PAGES = [
    page
    for page in REQUIRED_PAGES
    if page
    not in {
        "index.mdx",
        "start-here.mdx",
        "learning-system/overview.mdx",
        "learning-system/daily-workflow.mdx",
        "learning-system/weekly-workflow.mdx",
        "learning-system/how-to-use-codex.mdx",
        "labs/overview.mdx",
    }
]


def sidebar_slugs() -> list[str]:
    config = SITE / "astro.config.mjs"
    if not config.exists():
        return []
    text = config.read_text(encoding="utf-8")
    return re.findall(r"slug:\s*['\"]([^'\"]+)['\"]", text)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not SITE.is_dir():
        errors.append("Missing site directory.")
    if not DOCS.is_dir():
        errors.append("Missing site/src/content/docs directory.")

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    for rel in REQUIRED_PAGES:
        if not (DOCS / rel).is_file():
            errors.append(f"Missing required page: site/src/content/docs/{rel}")

    for slug in sidebar_slugs():
        rel = f"{slug}.mdx"
        if not (DOCS / rel).is_file():
            errors.append(f"Sidebar slug points to missing page: {slug}")

    for rel in GENERATED_PAGES:
        path = DOCS / rel
        if path.exists() and SOURCE_NOTE not in path.read_text(encoding="utf-8"):
            errors.append(f"Generated page missing source note: {rel}")

    if (DOCS / "review/flashcards.mdx").exists():
        text = (DOCS / "review/flashcards.mdx").read_text(encoding="utf-8")
        if '<div class="qa-card">' not in text:
            warnings.append("Flashcards page exists but does not contain Q/A cards.")

    print("Site content validation report")
    print(f"Required pages checked: {len(REQUIRED_PAGES)}")
    print(f"Sidebar links checked: {len(sidebar_slugs())}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Site content validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

