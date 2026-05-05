#!/usr/bin/env python3
"""Lightweight source index validation without external YAML dependencies."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "resources" / "sources.yaml"
REQUIRED_FIELDS = [
    "source_id:",
    "title:",
    "url:",
    "access_status:",
]
ALTERNATIVE_FIELDS = [
    ("author_or_owner:", "author_or_organization:"),
    ("source_type:", "type:"),
]


def main() -> int:
    text = SOURCES.read_text(encoding="utf-8")
    if "sources:" not in text:
        print("Source validation failed: missing top-level 'sources:' key.")
        return 1

    active_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]

    if active_lines in (["sources:", "[]"], ["sources: []"]):
        print("Source validation passed: no active sources yet.")
        return 0

    missing = [field for field in REQUIRED_FIELDS if field not in text]
    for old_field, new_field in ALTERNATIVE_FIELDS:
        if old_field not in text and new_field not in text:
            missing.append(f"{old_field} or {new_field}")
    if missing:
        print("Source validation warning: active source index may be missing fields.")
        for field in missing:
            print(f"  - {field}")
        return 1

    print("Source validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
