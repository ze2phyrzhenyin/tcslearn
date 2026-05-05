# TCS Self-Study OS Site

This is the Astro + Starlight documentation site for the TCS Self-Study OS.

## Local Development

From the repository root:

```bash
make site-sync
make site-dev
```

Or from this directory:

```bash
npm run sync
npm run dev
```

## Build

```bash
npm run build
```

The build runs content sync and site validation before Astro builds the static site.

## Source of Truth

Learning content remains in the repository root:

- `notes/`
- `exercises/`
- `labs/`
- `review/`
- `resources/`
- `state/`

Generated web pages live in `site/src/content/docs/`. Do not edit generated pages directly; edit the source file and rerun sync.

