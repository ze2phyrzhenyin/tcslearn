# 02 Generate Day

Use this to generate or repair a single day.

```text
请读取：
- AGENTS.md
- context/current_context.md
- curriculum/weeks/week{XX}-{week_slug}.yaml
- docs/CONTENT_STYLE_GUIDE.md
- docs/QUALITY_CHECKS.md
- state/open_questions.md
- state/mistakes_log.md
- state/proof_weaknesses.md

目标：
生成 Week {week_number}, Day {day_number}：{day_topic}

输出：
- notes/week{XX}/day{DD}-{day_slug}.md
- exercises/week{XX}/day{DD}-{day_slug}.md
- 如适合，labs/week{XX}/day{DD}-{day_slug}.py
- 更新 review/flashcards.md
- 更新 state 和 context

内容结构：
1. Learning goals
2. Prerequisites
3. Definitions with example and non-example
4. Intuition
5. Theorem / lemma / claim
6. Proof sketch and full proof when appropriate
7. Worked examples
8. Common traps
9. Exercises
10. Self-check
11. Connections to future modules

特殊要求：
- 不要假设我已经掌握高级概念。
- 每个证明拆 assumptions、goal、strategy、proof、check。
- 如果是概率内容，说明 sample space。
- 如果是算法内容，说明 input、output、invariant、correctness、complexity。

结束前：
- 运行相关脚本或说明未运行原因。
- 更新 context/last_codex_summary.md。
- 更新 context/next_codex_prompt.md。
- 更新 state/next_actions.md。
```

