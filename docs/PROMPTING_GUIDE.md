# Prompting Guide

Use prompts as repeatable operating procedures. A good prompt states the target, context, output files, quality rules, and end-of-task updates.

## Standard Pattern

```text
请读取 context/current_context.md。
使用 prompts/XX_prompt_name.md。
目标：...
范围：...
输出文件：...
质量要求：遵守 AGENTS.md、docs/CONTENT_STYLE_GUIDE.md、docs/QUALITY_CHECKS.md。
结束后更新 context 和 state。
```

## Before a Prompt

Run:

```bash
python scripts/export_context_pack.py
```

Then include `context/current_context.md` or ask Codex to read it locally.

## After a Prompt

Check:

- Were only necessary files created?
- Were sources legal?
- Were context and state updated?
- Did Codex recommend the next concrete prompt?

Use `prompts/10_next_prompt_builder.md` when you are unsure what to ask next.

