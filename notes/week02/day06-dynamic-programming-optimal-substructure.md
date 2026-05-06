# Dynamic Programming and Optimal Substructure

## 1. 今日目标

把 DP 理解为 state definition + recurrence + computation order + proof。

## 2. 为什么这个主题对 TCS 重要

DP 是 string algorithms、sequence alignment、shortest paths、knapsack 和很多 optimization routines 的基础。 本周始终区分 problem、algorithm、model、proof 和 experiment。

## 3. Week 1 依赖概念

induction, recursion, functions, Cartesian product states, asymptotics。如果这些概念还不稳定，先复习 Week 1 对应 note，再开始证明题。

## 4. 核心定义

- **dynamic programming:** 缓存重叠子问题。
- **optimal substructure:** 最优解由子问题最优解组成。
- **state:** table 索引，必须含足够信息。
- **transition:** 由依赖状态计算当前状态。
- **base case:** 最小状态值。
- **memoization:** top-down with cache。
- **tabulation:** bottom-up table filling。
- **computation order:** 依赖先算完。
- **reconstruction:** 从 choices 恢复解。
- **edit distance:** string 转换最小编辑数。


    ## 5. 最小例子

    Edit distance state dp[i][j] 表示 x[:i] 到 y[:j] 的最小 edit count。

    ## 6. 反例或 non-example

    只用 dp[i] 表示 edit distance 缺少第二个字符串前缀长度。

    ## 7. 关键算法

    ### Algorithm: Longest Increasing Subsequence DP

- **Problem:** find LIS length
- **Input:** sequence A[0..n-1]
- **Output:** length of LIS
- **Assumptions:** elements comparable
- **Algorithm idea:** dp[i] = length of LIS ending at i。
- **Pseudocode:** `dp[i]=1+max(dp[j] for j<i and A[j]<A[i], default 0)`
- **Invariant or proof structure:** induction over i。
- **Correctness proof:** 任意以 i 结尾的 LIS 的前一个元素必须是某个 j<i 且 A[j]<A[i]；取最大覆盖所有情况。
- **Time complexity:** O(n^2)。
- **Space complexity:** O(n), plus parent for reconstruction。
- **Edge cases:** duplicates and strict vs non-strict
- **Common mistakes:** 把 ending at i 与 within prefix i 混淆。

### Algorithm: Edit Distance DP

- **Problem:** minimum edit operations between strings
- **Input:** strings x length n, y length m
- **Output:** minimum edit count
- **Assumptions:** unit costs unless stated
- **Algorithm idea:** dp[i][j] 处理 prefixes x[:i], y[:j]。
- **Pseudocode:** `dp[i][j]=min(delete, insert, substitute/match)`
- **Invariant or proof structure:** induction over i+j。
- **Correctness proof:** 最后一步必为 delete、insert、match/substitute；这些情况穷尽且递归到更小 prefixes。
- **Time complexity:** O(nm)。
- **Space complexity:** O(nm), reducible for value only。
- **Edge cases:** empty strings, equal last chars
- **Common mistakes:** 没有说明 base cases。

### Algorithm: 0/1 Knapsack DP

- **Problem:** maximize value with indivisible items
- **Input:** weights, values, capacity W
- **Output:** maximum value
- **Assumptions:** integer capacities
- **Algorithm idea:** dp[i][w] = best using first i items and capacity w。
- **Pseudocode:** `dp[i][w]=max(skip item i, take item i if feasible)`
- **Invariant or proof structure:** induction over i。
- **Correctness proof:** 最优解要么不用第 i 个 item，要么用它并消耗 weight_i；两类互斥且覆盖所有 feasible solutions。
- **Time complexity:** O(nW), pseudo-polynomial。
- **Space complexity:** O(nW) or O(W)。
- **Edge cases:** capacity 0, item too heavy
- **Common mistakes:** 不讨论 W 的 encoding。

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

1. state definition 不完整。
2. recurrence 漏情况。
3. base case 省略。
4. reconstruction 与 value 混淆。


## 11. 与 string algorithms / learning theory / complexity theory 的联系

Edit distance 是 string algorithms 的核心入口；DP state proof 是算法理论基本功。

## 12. 必做练习

- 阅读本 note 的所有 algorithm blocks，并手写每个 algorithm 的 Problem/Input/Output。
- 完成 `exercises/week02/day06_exercises.tex` 的前 8 到 10 题。
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
