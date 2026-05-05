# Deployment

The site is a static Astro + Starlight project in `site/`.

## Local Build

From the repository root:

```bash
make site-sync
make site-validate
make site-build
```

From `site/`:

```bash
npm install
npm run build
```

The build output is `site/dist/`.

## GitHub Pages

The workflow is `.github/workflows/deploy-site.yml`.

It:

1. checks out the repository;
2. sets up Node;
3. installs dependencies in `site/`;
4. runs content sync from the repository root;
5. builds the Astro site;
6. uploads `site/dist`;
7. deploys to GitHub Pages.

### Base Path

If the site is deployed at `https://username.github.io/repository-name/`, Astro may need a base path. This project does not hard-code a base path. If assets fail on GitHub Pages, set `base` in `site/astro.config.mjs` or provide an environment-based config.

Do not hard-code a username or repository name in the workflow.

## Vercel

Recommended settings:

- Root Directory: `site/`
- Install Command: `npm install`
- Build Command: `npm run build`
- Output Directory: `dist`

Because Vercel runs from `site/`, the `sync` script uses `../scripts/sync_site_content.py` and expects the full repository to be present.

## Common Errors

### Missing Generated Pages

Run:

```bash
python3 scripts/sync_site_content.py
python3 scripts/validate_site_content.py
```

### Failed MDX Build

Check for:

- raw `{` or `}` in generated prose;
- raw `<` in text;
- unclosed code fences;
- unsupported LaTeX commands.

### Math Rendering Errors

Math uses `remark-math`, `rehype-katex`, and `katex`. If KaTeX cannot render an expression, simplify the source or wrap the unsupported expression in a code block.

### GitHub Pages CSS or Asset Path Errors

Check whether a base path is needed for repository-subdirectory deployment.

## Verify Deployment

After deployment, open:

- homepage;
- Week 1 overview;
- Day 1;
- Week 1 problem set;
- one lab page;
- resources page.

Confirm navigation, search, dark mode, and code blocks work.

