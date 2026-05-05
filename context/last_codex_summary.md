# Last Codex Summary

Date: 2026-05-06

## Modified Files

- `.gitignore`: ignored Vercel local project metadata.
- `vercel.json`: added root-level Vercel config for building the Astro site from `site/`.
- `site/package-lock.json`: repaired the incomplete Pagefind optional package entry that caused Vercel `npm install` to fail with `Invalid Version`.
- `state/progress.yaml`: marked the web site as deployed and recorded the production URL.
- `state/next_actions.md`: added deployment maintenance notes.
- `context/current_context.md`: refreshed by `scripts/export_context_pack.py`.
- `context/next_codex_prompt.md`: updated with the next recommended visual QA prompt.

## Generated Or Deployed

- GitHub repository pushed to `git@github.com:ze2phyrzhenyin/tcslearn.git`.
- Vercel production deployment completed for project `tcs-selfstudy-os`.
- Production URL: `https://tcs-selfstudy-os.vercel.app`.

## Checks Run

- `python3 scripts/validate_site_content.py` passed.
- `cd site && npm run build` passed.
- `npx vercel deploy --prod --yes` completed with `READY`.
- `curl -I https://tcs-selfstudy-os.vercel.app/` returned HTTP 200.
- `curl -I https://tcs-selfstudy-os.vercel.app/week01/day01/` returned HTTP 200.
- `curl -I https://tcs-selfstudy-os.vercel.app/exercises/week01-problem-set/` returned HTTP 200.

## Deployment Notes

- The first root Vercel deployment failed because Vercel initially treated the repository root as a Python project due to root `pyproject.toml`.
- Adding root `vercel.json` moved the build to `site/`, but the next deployment failed because `site/package-lock.json` had an incomplete optional Pagefind package entry.
- After repairing the lock file, the root Vercel production deployment succeeded and was aliased to `https://tcs-selfstudy-os.vercel.app`.

## Unresolved Issues

- No browser screenshot or visual QA pass has been run yet.
- npm reports 5 moderate audit findings in the site dependency tree; no forced dependency upgrade was applied because that may introduce breaking changes.
