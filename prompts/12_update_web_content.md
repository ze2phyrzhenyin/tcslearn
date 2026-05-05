# 12 Update Web Content

```text
请更新 tcs-selfstudy-os 的网页内容，以纳入 {week_id_or_topic}。

必须读取：
- AGENTS.md
- docs/CONTENT_SYNC.md
- docs/WEB_DESIGN_SYSTEM.md
- docs/WEB_DEV_GUIDE.md
- curriculum/weeks/{week_file}
- state/progress.yaml
- context/current_context.md

任务：
1. 读取新 week 的 notes、exercises、labs、review、resources、state。
2. 扩展 scripts/sync_site_content.py，让它生成新 week 页面。
3. 更新 site/astro.config.mjs sidebar。
4. 运行 python3 scripts/sync_site_content.py。
5. 运行 python3 scripts/validate_site_content.py。
6. 在 site/ 中运行 npm run build。

要求：
- 保持现有设计系统不变。
- 不覆盖 hand-maintained core pages。
- generated 页面必须写 source note。
- 不把 exercises 和 solutions 混在一起。
- labs 页面必须说明实验不是证明。

结束后更新 context 和 state。
```

