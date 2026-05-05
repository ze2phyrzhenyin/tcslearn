# 08 Source Audit

```text
请读取：
- config/resource_policy.yaml
- resources/sources.yaml
- docs/RESOURCE_POLICY.md
- context/current_context.md

目标：
审计 {source_or_topic} 的资源合法性和可用性。

任务：
1. 标记 allowed、disallowed、unclear。
2. 对 unclear 来源寻找或建议官方开放替代。
3. 不要使用盗版扫描、镜像或 solution dumps。
4. 更新 resources/sources.yaml。
5. 如存在争议或不可用资源，更新 state/open_questions.md。

结束后运行：
- python scripts/validate_sources.py
- python scripts/export_context_pack.py
```

