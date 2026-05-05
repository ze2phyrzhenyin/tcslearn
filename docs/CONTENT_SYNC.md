# Content Sync

The web site is generated from repository learning materials. The source of truth is not inside `site/`.

## Source of Truth

- `curriculum/`
- `notes/`
- `exercises/`
- `labs/`
- `review/`
- `resources/`
- `state/`

## Generated Pages

Generated pages live in:

```text
site/src/content/docs/
```

Every generated page must include:

```text
This page is generated from repository learning materials. Edit the source file, not this generated page.
```

## Hand-Maintained Pages

These pages may be edited directly:

- `site/src/content/docs/index.mdx`
- `site/src/content/docs/start-here.mdx`
- `site/src/content/docs/learning-system/overview.mdx`
- `site/src/content/docs/learning-system/daily-workflow.mdx`
- `site/src/content/docs/learning-system/weekly-workflow.mdx`
- `site/src/content/docs/learning-system/how-to-use-codex.mdx`
- `site/src/content/docs/labs/overview.mdx`

## Do Not Hand-Edit

Do not hand-edit generated pages for Week 1 notes, exercises, labs, review, resources, progress, or next actions. Edit their source files and run sync.

## Sync Flow

```bash
python3 scripts/sync_site_content.py
python3 scripts/validate_site_content.py
cd site && npm run build
```

## Conflict Handling

If a generated page has manual edits, move those edits back to the source file first. Then rerun sync.

## Extending to Week 2 and Later

1. Generate Week 2 source content.
2. Extend `scripts/sync_site_content.py`.
3. Add new sidebar links in `site/astro.config.mjs`.
4. Validate and build.
5. Keep visual style unchanged unless `docs/WEB_DESIGN_SYSTEM.md` is updated deliberately.

