# 00 Bootstrap Framework

Use this prompt when rebuilding or auditing the repository framework itself.

```text
你现在是在维护 tcs-selfstudy-os 框架，不是在生成完整课程内容。

请读取：
- AGENTS.md
- docs/DEV_GUIDE.md
- docs/QUALITY_CHECKS.md
- config/learner_profile.yaml
- config/resource_policy.yaml

任务：
1. 检查目录结构是否符合 README 和 DEV_GUIDE。
2. 修复缺失的框架文件、模板、脚本或文档。
3. 不生成完整 Week 内容。
4. 只保留少量示例，示例必须可复用。
5. 运行：
   - python scripts/validate_structure.py
   - python scripts/export_context_pack.py
   - python scripts/build_flashcards.py

结束后更新：
- context/last_codex_summary.md
- context/next_codex_prompt.md
- state/next_actions.md
```

