# 14 Deploy Debug

```text
请排查 tcs-selfstudy-os 网站部署失败。

必须读取：
- docs/DEPLOYMENT.md
- docs/WEB_DEV_GUIDE.md
- .github/workflows/deploy-site.yml
- site/package.json
- site/astro.config.mjs
- scripts/sync_site_content.py
- scripts/validate_site_content.py

请检查：
1. CI logs 或用户粘贴的错误。
2. package scripts。
3. GitHub Actions working directory。
4. Astro base path。
5. generated pages 是否缺失。
6. MDX syntax。
7. math rendering errors。
8. build output directory。

要求：
- 给出最小修复。
- 不重做视觉设计。
- 不更改学习内容，除非 build 错误来自 generated MDX。
- 修复后运行 python3 scripts/validate_site_content.py 和 npm run build。

结束后更新 context 和 state。
```

