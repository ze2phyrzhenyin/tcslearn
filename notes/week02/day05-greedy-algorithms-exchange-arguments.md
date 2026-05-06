# Greedy Algorithms and Exchange Arguments

## 1. 今日目标

学习证明 greedy choice is safe，而不是只记策略。

## 2. 为什么这个主题对 TCS 重要

Greedy algorithms 的代码通常短，证明通常是核心。Exchange argument 训练你改造最优解。 本周始终区分 problem、algorithm、model、proof 和 experiment。

## 3. Week 1 依赖概念

sets, order, proof by contradiction, induction, graph cut intuition。如果这些概念还不稳定，先复习 Week 1 对应 note，再开始证明题。

## 4. 核心定义

- **greedy algorithm:** 反复做局部选择且不回溯。
- **locally optimal choice:** 当前局部最优。
- **globally optimal solution:** 完整解达到目标最优。
- **exchange argument:** 改造任意最优解使其包含 greedy choice。
- **stays-ahead argument:** 每步不落后于任意最优 partial solution。
- **cut property:** MST 中 crossing cut 的 light edge 是 safe。
- **interval scheduling:** 选最多互不重叠 intervals。
- **fractional knapsack:** 物品可拆分。
- **0/1 knapsack:** 物品不可拆分。


    ## 5. 最小例子

    Interval scheduling 选择 finish time 最早的 compatible interval。

    ## 6. 反例或 non-example

    coin system {1,3,4}, amount 6 中最大 coin greedy 给 4+1+1，最优是 3+3。

    ## 7. 关键算法

    ### Algorithm: Earliest-Finish Interval Scheduling

- **Problem:** maximum number of non-overlapping intervals
- **Input:** intervals [s_i,f_i)
- **Output:** largest compatible subset
- **Assumptions:** interval endpoints comparable
- **Algorithm idea:** 每次选 finish time 最早且与已选兼容的 interval。
- **Pseudocode:** `sort by finish; scan and select compatible intervals`
- **Invariant or proof structure:** exchange proof: 存在最优解包含 greedy 的第一个选择。
- **Correctness proof:** 把任意最优解的第一个 interval 替换为 greedy interval，不减少可接续空间；递归应用。
- **Time complexity:** O(n log n) sorting, then O(n) scan。
- **Space complexity:** O(n) output。
- **Edge cases:** touching intervals convention, equal finish times
- **Common mistakes:** 只说“结束越早越好”而不证明 safe。

### Algorithm: Fractional Knapsack

- **Problem:** maximize value with divisible items
- **Input:** items with weight/value, capacity W
- **Output:** fractions maximizing value
- **Assumptions:** weights positive, fractions allowed
- **Algorithm idea:** 按 value/weight density 从高到低填充。
- **Pseudocode:** `sort by density; take full items then one fraction`
- **Invariant or proof structure:** exchange argument on density。
- **Correctness proof:** 若解取了低 density 而没取满高 density，可交换同重量，价值不降。
- **Time complexity:** O(n log n) sorting。
- **Space complexity:** O(n) output。
- **Edge cases:** zero weight disallowed, equal densities
- **Common mistakes:** 把证明套到 0/1 knapsack。

### Algorithm: Kruskal MST High-Level

- **Problem:** minimum spanning tree
- **Input:** connected undirected weighted graph
- **Output:** minimum-weight spanning tree
- **Assumptions:** edge weights comparable
- **Algorithm idea:** 按权重递增考虑 edge，若不形成 cycle 则加入。
- **Pseudocode:** `sort edges; add if endpoints in different components`
- **Invariant or proof structure:** cut property and acyclicity invariant。
- **Correctness proof:** 每次选的是某个 cut 上的 light edge，可加入某个 MST；不形成 cycle 保持 forest。
- **Time complexity:** O(|E| log |E|) plus union-find costs。
- **Space complexity:** O(|V|+|E|)。
- **Edge cases:** disconnected graph gives forest
- **Common mistakes:** 未说明 cut property 就声称 greedy 正确。

    ## 8. 正确性证明模板

    1. **Statement:** 写清 problem、input、output、precondition、postcondition。
    2. **Invariant / induction variable:** loop 用 invariant，recursive algorithm 用 input size induction，data structure 用 representation invariant，DP 用 state order。
    3. **Initialization / base case:** 说明最小状态或第一轮循环满足条件。
    4. **Maintenance / induction step:** 假设之前状态满足 specification，证明一步操作后仍满足。
    5. **Termination:** 说明算法会停止，并把 invariant 转化成 postcondition。
    6. **Edge cases:** 空输入、单元素、重复元素、不可达状态、ties、invalid precondition。

    ## 9. 复杂度分析模板

    - 声明变量，例如 \(n\) 是元素数，\(|V|\) 是 vertices 数，\(|E|\) 是 edges 数。
    - 分清 preprocessing、single operation、query、total running time 和 space。
    - Worst-case 要对所有输入取最大；expected time 要说明随机性；amortized time 要说明操作序列。
    - Recurrence 必须包含 base case；randomized analysis 必须定义 sample space 和 random variable。

    ## 10. 常见错误

1. greedy 缺少 exchange proof。
2. fractional 与 0/1 knapsack 混淆。
3. coin change 反例忽略。
4. cut property 方向说错。


## 11. 与 string algorithms / learning theory / complexity theory 的联系

Greedy proof patterns 会出现在 MST、interval problems 和 future approximation algorithms。

## 12. 必做练习

- 阅读本 note 的所有 algorithm blocks，并手写每个 algorithm 的 Problem/Input/Output。
- 完成 `exercises/week02/day05_exercises.tex` 的前 8 到 10 题。
- 在 `state/mistakes_log.md` 中记录至少一个容易犯错点，即使你还没有做错。

## 13. 选做练习

- 把本日一个 correctness proof 改写成 Statement/Definitions/Assumptions/Goal/Strategy/Proof/Check。
- 找一个 small input，手算 algorithm 的中间状态，并标注 invariant。

## 14. 自测问题

- 今天的 problem specification 是什么？
- 哪个 invariant 或 induction hypothesis 支撑 correctness proof？
- 复杂度里的变量是什么？
- 哪个 conclusion 依赖模型假设或随机性假设？

## 15. 明天复习什么

明天开始前，用 10 分钟复述今天的 specification、proof template 和最容易犯的错误。


## 完整证明：interval scheduling earliest-finish-time greedy correctness

**Statement.** 对 half-open intervals \([s_i,f_i)\)，按 finish time 从小到大扫描并选择第一个与已选 intervals 兼容的 interval，得到 maximum-cardinality compatible subset。

**Definitions used.** 两个 intervals compatible 指它们不重叠；half-open 约定下 \([s_i,f_i)\) 与 \([s_j,f_j)\) 在 \(f_i\le s_j\) 时兼容。Optimal solution 指 compatible set 中 cardinality 最大者。

**Assumptions.** 所有 intervals 有 \(s_i < f_i\)；目标是最大化选择数量；算法先选择 finish time 最早的 interval \(g\)。

**Goal.** 证明 greedy 输出的 interval 数量等于 optimal value。

**Strategy.** Exchange argument。证明存在一个 optimal solution 包含 greedy 的第一个选择 \(g\)。然后删去所有与 \(g\) 冲突的 intervals，问题缩小到从 \(f_g\) 之后开始的剩余 intervals，对剩余问题递归应用同一论证。

**Proof.** 令 \(g\) 是所有 intervals 中 finish time 最早者。取一个 optimal solution \(O\)，并令 \(o\) 是 \(O\) 中 finish time 最早的 interval。因为 \(g\) 是全体 intervals 中 finish time 最早者，所以 \(f_g \le f_o\)。构造集合 \(O' = (O \setminus \{o\}) \cup \{g\}\)。

需要证明 \(O'\) 仍 compatible 且大小与 \(O\) 相同。大小相同来自删除一个 interval 并加入一个 interval。对 compatibility，考虑 \(O\) 中除 \(o\) 外任意 interval \(x\)。由于 \(o\) 是 \(O\) 中最早结束的 interval，且 \(O\) compatible，所有在 \(O\) 中排在 \(o\) 之后的 interval 都满足 \(s_x \ge f_o\)。又因为 \(f_g \le f_o\)，得到 \(s_x \ge f_g\)，所以 \(g\) 与每个这样的 \(x\) compatible。因此 \(O'\) 是与 \(O\) 同样大的 compatible solution，并且包含 \(g\)。

现在把所有与 \(g\) 冲突的 intervals 删除，只保留开始时间至少为 \(f_g\) 的 intervals。任何包含 \(g\) 的最优解，其余部分必须是这个剩余子问题的最优解；否则用更大的剩余解替换会得到比最优解更大的整体解。Greedy 在剩余子问题上做同样的 earliest-finish 选择。对剩余 intervals 数量做 induction，得到 greedy 在每个子问题上都达到 optimal value。因此整体 greedy solution optimal。

**Check.** Exchange step 没有声称所有 optimal solutions 都包含 \(g\)，只证明至少存在一个 optimal solution 可以包含 \(g\)。这正是 greedy choice is safe 的含义。

**Common mistake.** 只写“结束越早留给后面的时间越多”，但没有把任意最优解改造成包含 greedy choice 的最优解。
