# Next Codex Prompt

Copy this for the next web-focused pass:

```text
请读取：
- AGENTS.md
- docs/WEB_DESIGN_SYSTEM.md
- docs/WEB_DEV_GUIDE.md
- docs/CONTENT_SYNC.md
- site/astro.config.mjs
- site/src/styles/custom.css
- site/src/content/docs/index.mdx
- site/src/content/docs/week01/overview.mdx
- site/src/content/docs/week01/day01.mdx
- site/src/content/docs/exercises/week01-problem-set.mdx
- site/src/content/docs/labs/week01-asymptotics.mdx
- context/current_context.md

目标：
运行视觉 polish pass，并在浏览器中检查首页、Week 1 overview、Day 1、Problem Set、Lab 页面。

要求：
- 使用 prompts/13_visual_polish_pass.md。
- 不重做设计。
- 只修复间距、排版层级、移动端、暗色模式、长文可读性和导航清晰度。
- 遵守 docs/WEB_DESIGN_SYSTEM.md。
- 不引入新视觉风格、随机颜色、随机图标、复杂动画、Tailwind 或重型 UI 库。

验证：
- python3 scripts/sync_site_content.py
- python3 scripts/validate_site_content.py
- cd site && npm run build
- 如实际使用浏览器或截图工具检查，请明确列出检查页面；否则不要声称完成截图检查。

结束后更新：
- context/last_codex_summary.md
- context/next_codex_prompt.md
- state/next_actions.md
```
