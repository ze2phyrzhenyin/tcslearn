# Next Codex Prompt

```text
请读取：
- context/current_context.md
- AGENTS.md
- {{additional_file}}

使用 prompt template：
- {{prompt_template_path}}

目标：
{{specific_goal}}

范围：
- week: {{week_id_or_none}}
- day: {{day_id_or_none}}
- topic: {{topic}}
- output files: {{output_files}}

质量要求：
- 遵守 docs/CONTENT_STYLE_GUIDE.md。
- 遵守 docs/QUALITY_CHECKS.md。
- 遵守 config/resource_policy.yaml。
- 不大段复制任何来源。

结束后必须更新：
- context/last_codex_summary.md
- context/next_codex_prompt.md
- state/next_actions.md
- 必要时更新 state/open_questions.md 和 state/mistakes_log.md
```

