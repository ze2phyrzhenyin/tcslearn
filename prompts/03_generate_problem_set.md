# 03 Generate Problem Set

Use this to generate a formal LaTeX problem set.

```text
请读取：
- AGENTS.md
- context/current_context.md
- templates/problem_set_template.tex
- docs/CONTENT_STYLE_GUIDE.md
- docs/QUALITY_CHECKS.md
- 相关 notes 和 curriculum week YAML

目标：
为 {week_or_topic} 生成正式 problem set。

输出文件：
- exercises/week{XX}/problem_set.tex
- 如需要，exercises/week{XX}/problem_set_notes.md

题目要求：
- warmup: {warmup_count}
- core: {core_count}
- challenge: {challenge_count}
- 每题标注 topic、difficulty、prerequisites、tested skill。
- 证明题必须可由已给材料解决，challenge 可明确标注需要额外思考。
- 包含定义题、例子/反例题、证明题、算法分析题，按主题需要调整。

不要生成解答，除非用户明确要求。只在每题后写短 hint。

结束后：
- 更新 state/next_actions.md，安排生成 solutions。
- 更新 context/last_codex_summary.md。
- 更新 context/next_codex_prompt.md，推荐使用 prompts/04_generate_solutions.md。
```

