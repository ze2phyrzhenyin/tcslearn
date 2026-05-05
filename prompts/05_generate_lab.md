# 05 Generate Lab

Use this to generate a Python experiment.

```text
请读取：
- AGENTS.md
- context/current_context.md
- templates/lab_template.py
- docs/CONTENT_STYLE_GUIDE.md
- docs/QUALITY_CHECKS.md
- related notes and week YAML

目标：
为 {topic} 生成一个小型 Python lab。

输出文件：
- labs/week{XX}/{lab_slug}.py
- 可选：labs/week{XX}/{lab_slug}.md，如果需要解释实验任务

要求：
- 只用标准库，除非明确说明为什么需要 numpy。
- 文件必须可直接运行。
- 必须包含 assert 测试。
- 随机实验必须设置 seed。
- 明确说明实验验证的是 intuition 或 example，不是证明。
- 函数要短，命名清楚。

结束前：
- 运行 python labs/week{XX}/{lab_slug}.py
- 修复失败测试。
- 更新 context 和 state。
```

