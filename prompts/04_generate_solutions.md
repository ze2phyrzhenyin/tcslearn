# 04 Generate Solutions

Use this to generate detailed LaTeX solutions.

```text
请读取：
- AGENTS.md
- context/current_context.md
- templates/solution_template.tex
- docs/CONTENT_STYLE_GUIDE.md
- docs/QUALITY_CHECKS.md
- exercises/week{XX}/problem_set.tex
- related notes

目标：
为 {problem_set_path} 生成详细 solutions。

输出文件：
- exercises/week{XX}/solutions.tex

每题解答必须包含：
- Restatement
- Definitions used
- Assumptions
- Solution strategy
- Full solution
- Why each key step is valid
- Common mistakes
- Repair drill when useful

数学要求：
- 不写“显然”跳步。
- Big-O 写明变量。
- 概率题写明 sample space 和 events。
- learning theory 题写明 distribution、hypothesis class、loss、confidence。
- DP 题写明 neighboring relation、sensitivity、mechanism。

结束后：
- 如发现题目不可解，更新 state/open_questions.md。
- 如发现常见错误，更新 state/mistakes_log.md 或 state/proof_weaknesses.md。
- 更新 context 和 state。
```

