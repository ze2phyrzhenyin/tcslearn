# TCS Selfstudy OS

这是一个长期复用的“理论计算机科学自学操作系统”，不是普通笔记库。它的目标是让你通过 Codex 反复迭代生成、检查和改进学习材料，包括每周学习计划、每日笔记、证明练习、problem set、LaTeX 解答、Python 小实验、复盘、闪卡、资源索引和下一轮 Codex 提示词。

默认学习语言是中文解释，数学符号、定理名、算法名和核心术语保留英文。所有资源必须来自官方开放网页、作者公开讲义、arXiv、OCW、课程主页或会议官网。笔记必须改写、总结和组织，不能大段复制教材或讲义原文。

## 第一次使用

1. 阅读 [AGENTS.md](AGENTS.md)，这是 Codex 每次进入仓库必须遵守的规则。
2. 修改 [config/learner_profile.yaml](config/learner_profile.yaml)，把你的背景、弱项、每日时间和近期目标改准确。
3. 阅读 [docs/STUDY_WORKFLOW.md](docs/STUDY_WORKFLOW.md)，了解每天如何学习和复盘。
4. 运行结构检查：

```bash
python scripts/validate_structure.py
```

5. 生成给下一轮 Codex 使用的上下文包：

```bash
python scripts/export_context_pack.py
```

6. 打开 [context/next_codex_prompt.md](context/next_codex_prompt.md)，复制其中的第二轮提示词，让 Codex 生成 Week 1 内容。

## 仓库如何被使用

每次学习迭代都围绕四类文件推进：

- `curriculum/`：长期路线图、模块定义和每周 schema。
- `notes/`、`exercises/`、`labs/`：实际学习材料、题目和实验。
- `review/`、`state/`：复盘、闪卡、进度、错误、未懂问题和下一步行动。
- `context/`、`prompts/`：给 Codex 的上下文和下一轮提示词。

Codex 完成任何任务后，都必须更新：

- [context/last_codex_summary.md](context/last_codex_summary.md)
- [context/next_codex_prompt.md](context/next_codex_prompt.md)
- [state/next_actions.md](state/next_actions.md)
- 必要时更新 [state/open_questions.md](state/open_questions.md) 和 [state/mistakes_log.md](state/mistakes_log.md)

## 每周学习流程

1. 用 [prompts/01_generate_week.md](prompts/01_generate_week.md) 生成某一周，例如“生成 Week 1：Mathematical foundations for TCS”。
2. Codex 应创建或更新：
   - `curriculum/weeks/weekXX-*.yaml`
   - `notes/weekXX/`
   - `exercises/weekXX/`
   - `labs/weekXX/`
   - `review/weekly_reviews/weekXX-*.md`
3. 每周必须包含：
   - precise definition
   - intuition
   - example 和 non-example
   - theorem / lemma / claim
   - proof idea 和必要的 full proof
   - common mistakes
   - exercises 和 self-test
   - connection to larger TCS goals
4. 周末运行复盘提示词 [prompts/09_weekly_retrospective.md](prompts/09_weekly_retrospective.md)，把弱项写进 `state/`。

## 每日学习流程

每天不要直接读完材料就结束。按这个顺序做：

1. 打开当日 note，先读 learning goals 和 prerequisites。
2. 手写本日所有 definition，确保每个定义都能说出 example 和 non-example。
3. 读 theorem 或 claim，把 assumptions、goal、strategy 分开。
4. 先自己补 proof skeleton，再看完整证明或 solution。
5. 做 examples，再做 exercises。
6. 对错题写入 [state/mistakes_log.md](state/mistakes_log.md)。
7. 对未懂问题写入 [state/open_questions.md](state/open_questions.md)。
8. 把需要反复记忆的内容加入 [review/flashcards.md](review/flashcards.md)。
9. 用 [prompts/02_generate_day.md](prompts/02_generate_day.md) 或 [prompts/06_generate_review_pack.md](prompts/06_generate_review_pack.md) 让 Codex 生成下一轮反馈。

详细流程见 [docs/STUDY_WORKFLOW.md](docs/STUDY_WORKFLOW.md)。

## 如何让 Codex 继续生成下一周

推荐每次开始新任务前先运行：

```bash
python scripts/export_context_pack.py
```

然后复制 [context/current_context.md](context/current_context.md) 和你要使用的 prompt。例如：

```text
请读取 context/current_context.md，并使用 prompts/01_generate_week.md。
生成 Week 2：随机算法基础。
要求遵守 AGENTS.md、docs/CONTENT_STYLE_GUIDE.md 和 docs/QUALITY_CHECKS.md。
不要复制教材原文。结束后更新 context 和 state。
```

如果只想生成某一天，使用 [prompts/02_generate_day.md](prompts/02_generate_day.md)。如果只想生成题集或解答，使用 [prompts/03_generate_problem_set.md](prompts/03_generate_problem_set.md) 和 [prompts/04_generate_solutions.md](prompts/04_generate_solutions.md)。

## 错误、复盘和未懂问题

- 错题写入 `state/mistakes_log.md`，格式包含 topic、mistake、correct idea、repair exercise。
- 证明弱项写入 `state/proof_weaknesses.md`，尤其记录“缺少量词”“把 intuition 当 proof”“没有说明 sample space”等问题。
- 未懂问题写入 `state/open_questions.md`，每个问题要有 source、blocking level 和 next action。
- 周复盘写入 `review/weekly_reviews/`，并同步更新 `state/progress.yaml`。

## 扩展方向

这个框架从 mathematical foundations 开始，但已经预留长期模块：

- `string_algorithms`：suffix array、suffix tree、pattern matching、combinatorics on words，为 CPM/string 暑校做准备。
- `learning_theory`：PAC learning、VC dimension、generalization bounds、ERM，为 learning theory 暑校做准备。
- `complexity_theory`：reductions、P/NP、space complexity、randomized complexity。
- `differential_privacy`：neighboring relation、sensitivity、Laplace/Gaussian mechanism、privacy proof sketch。

新增模块时，在 `curriculum/modules/` 添加 YAML，并把依赖关系写入 [curriculum/roadmap.yaml](curriculum/roadmap.yaml)。新增资源时，先按 [config/resource_policy.yaml](config/resource_policy.yaml) 审核来源，再写入 [resources/sources.yaml](resources/sources.yaml)。

