# 11 Build Web Site

```text
请在已有 tcs-selfstudy-os 仓库中构建或修复 Astro + Starlight 文档站。

必须读取：
- AGENTS.md
- docs/WEB_DESIGN_SYSTEM.md
- docs/WEB_DEV_GUIDE.md
- docs/CONTENT_SYNC.md
- state/progress.yaml
- context/current_context.md

目标：
- 确保 site/ 是专业、简洁、长期可维护的 Starlight 文档站。
- 不重写原始学习内容。
- 原始内容仍以 notes/、exercises/、labs/、review/、resources/、state/ 为 source of truth。

任务：
1. 检查 site/ 配置、sidebar、CSS、组件。
2. 运行 python3 scripts/sync_site_content.py。
3. 运行 python3 scripts/validate_site_content.py。
4. 在 site/ 中运行 npm run build。
5. 修复所有 build 或 MDX 问题。
6. 更新 context/last_codex_summary.md、context/next_codex_prompt.md、state/next_actions.md。

限制：
- 遵守 docs/WEB_DESIGN_SYSTEM.md。
- 不做营销页风格。
- 不添加花哨动画、随机颜色、随机图标或复杂 UI 库。
```

