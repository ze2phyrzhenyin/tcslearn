# Web Development Guide

The web site lives in `site/` and uses Astro + Starlight. It is a static documentation front-end for the repository. The source of truth remains outside `site/`.

## Directory Responsibilities

- `site/astro.config.mjs`: Starlight configuration, sidebar, search, CSS, and math plugins.
- `site/src/content/docs/`: Starlight content pages.
- `site/src/components/`: small reusable Astro components.
- `site/src/styles/custom.css`: light design-system overrides.
- `site/public/`: static assets.
- `scripts/sync_site_content.py`: generates web pages from repository content.
- `scripts/validate_site_content.py`: validates site structure and generated-page rules.

## Local Start

From the repository root:

```bash
make site-sync
make site-dev
```

Or from `site/`:

```bash
npm run sync
npm run dev
```

## Content Sync

Run:

```bash
python3 scripts/sync_site_content.py
```

Generated pages must contain:

```text
This page is generated from repository learning materials. Edit the source file, not this generated page.
```

Do not hand-edit generated pages. Edit source files in `notes/`, `exercises/`, `labs/`, `review/`, `resources/`, or `state/`, then sync again.

## Add a New Week

1. Generate the week in `curriculum/weeks/`, `notes/`, `exercises/`, `labs/`, and `review/`.
2. Extend `scripts/sync_site_content.py` with the new week mapping.
3. Add sidebar entries in `site/astro.config.mjs`.
4. Run:

```bash
python3 scripts/sync_site_content.py
python3 scripts/validate_site_content.py
cd site && npm run build
```

## Add a New Day

1. Add the source note in `notes/weekXX/`.
2. Add the exercise sheet or problem-set section.
3. Extend the sync script day map.
4. Add the sidebar link if needed.

## Add a Lab

1. Put runnable Python in `labs/weekXX/`.
2. Include `main` and `assert` tests.
3. Add a lab entry in the sync script.
4. The generated web page must include purpose, concept, command, expected output, code, interpretation, limitations, and extensions.

## Add a Review Page

Review sources live in `review/`. Generated review pages live in `site/src/content/docs/review/`.

Use review pages for:

- weekly review;
- glossary;
- flashcards;
- mistakes;
- self-tests when useful.

## MDX Debugging

Common MDX problems:

- unescaped `{` or `}` in prose;
- raw `<` in text;
- invalid JSX attributes;
- unclosed code fences;
- LaTeX commands that are not valid KaTeX.

The sync script escapes common MDX hazards in generated Markdown. If build fails, inspect the generated file and the source file.

## Math Rendering

Math rendering is configured with:

- `remark-math`
- `rehype-katex`
- `katex`

KaTeX CSS is imported in `site/src/styles/custom.css`. If a formula fails, simplify the source expression or wrap unsupported LaTeX in a code block with a note for manual review.

## LaTeX Exercises

The sync script converts common LaTeX problem-set structures into MDX. It supports:

- sections;
- enumerated items;
- difficulty and concept labels;
- common inline math;
- display math delimiters.

Unsupported environments should be shown as code blocks and marked for manual review.

