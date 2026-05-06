
# Next Codex Prompt

Copy this for the next diagnostic pass:

```text
请读取：
- AGENTS.md
- context/current_context.md
- state/progress.yaml
- state/mistakes_log.md
- state/proof_weaknesses.md
- notes/week02/day01-specifications-sorting-lower-bounds.md
- exercises/week02/day01_exercises.tex
- exercises/week02/week02_problem_set.tex
- exercises/week02/week02_solutions.tex
- review/week02/proof_patterns_week02.md
- review/week02/mistakes_to_watch.md

目标：
根据我完成 Week 2 Day 1 的情况，为 sorting lower bound、loop invariant、merge sort recurrence 生成诊断反馈和补弱题。

请先问我提供：
1. 我写的 sorting specification；
2. 我写的 insertion sort loop invariant proof；
3. 我写的 comparison sorting lower bound proof skeleton；
4. 我做错或不确定的 Day 1 exercises 题号。

反馈要求：
- 不直接重写成标准答案，先定位错误类型。
- 按 specification、invariant、lower-bound model、recurrence 四类诊断。
- 对每个弱点给 2-3 道补弱题。
- 对证明问题指出缺失的 assumptions、goal、strategy 或 step validation。
- 更新 state/mistakes_log.md、state/proof_weaknesses.md、state/next_actions.md。
- 结束后更新 context/last_codex_summary.md 和 context/next_codex_prompt.md。
```
