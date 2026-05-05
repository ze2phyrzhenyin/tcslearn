# 10 Next Prompt Builder

```text
请读取：
- AGENTS.md
- context/current_context.md
- context/last_codex_summary.md
- state/progress.yaml
- state/next_actions.md
- state/open_questions.md
- state/mistakes_log.md
- state/proof_weaknesses.md

目标：
根据当前 state 自动写下一轮 Codex 提示词。

输出：
- 更新 context/next_codex_prompt.md

提示词必须包含：
- 应读取的上下文文件；
- 应使用的 prompt template；
- 具体 week/day/topic；
- 要创建或修改的文件；
- 质量要求；
- 结束后必须更新的 context 和 state；
- 如果存在 blocker，先处理 blocker。

不要写泛泛的“继续学习”。下一轮提示词必须可以直接复制使用。
```

