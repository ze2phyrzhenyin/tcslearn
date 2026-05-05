# 01 Generate Week

Use this to generate a full reusable week package.

```text
请读取：
- AGENTS.md
- context/current_context.md
- config/learner_profile.yaml
- config/resource_policy.yaml
- docs/CURRICULUM_SCHEMA.md
- docs/CONTENT_STYLE_GUIDE.md
- docs/QUALITY_CHECKS.md

目标：
生成 Week {week_number}：{week_title_or_topic}

范围：
- 这是第 {week_number} 周。
- slug: {week_slug}
- 模块: {module_name}
- 难度: {difficulty_profile}
- 每天默认学习时间: {daily_time_budget}
- 不要生成超过一周可消化范围的内容。

必须创建或更新：
1. curriculum/weeks/week{XX}-{week_slug}.yaml
2. notes/week{XX}/day01-*.md 到 day05-*.md
3. exercises/week{XX}/problem_set.tex
4. exercises/week{XX}/solutions.tex 或在 next_actions 中明确安排生成
5. labs/week{XX}/ 至少一个小实验，除非本周不适合实验并说明原因
6. review/weekly_reviews/week{XX}-{week_slug}.md
7. review/flashcards.md 中新增少量高价值 cards
8. state/progress.yaml
9. context/last_codex_summary.md
10. context/next_codex_prompt.md
11. state/next_actions.md

每一天必须包含：
- precise definitions
- intuition
- minimal example
- non-example
- theorem / lemma / claim
- proof idea
- exercises
- self-test
- common mistakes
- connection to larger TCS goals

资源规则：
- 只使用 config/resource_policy.yaml 允许的来源。
- 如果需要新资源，先更新 resources/sources.yaml。
- 不大段复制教材或讲义原文。

质量检查：
- 运行 python scripts/validate_structure.py
- 运行 python scripts/build_flashcards.py
- 如果修改 resources/sources.yaml，运行 python scripts/validate_sources.py
- 如果生成 lab，运行对应 Python 文件

结束时输出：
- modified files
- what was generated
- unresolved issues
- recommended next prompt
- what I should study first
```

