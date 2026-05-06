# Algorithm Specifications, Sorting, and Comparison Lower Bounds

## 1. 今日目标

建立 algorithmic problem、input/output specification、correctness 和 lower bound 的基本语言。

## 2. 为什么这个主题对 TCS 重要

Sorting 是第一个能完整展示 specification、correctness、upper bound 与 lower bound 的例子。 本周始终区分 problem、algorithm、model、proof 和 experiment。

## 3. Week 1 依赖概念

sets, functions, quantifiers, permutations, asymptotics, recurrence, proof by contradiction。如果这些概念还不稳定，先复习 Week 1 对应 note，再开始证明题。

## 4. 核心定义

- **algorithmic problem:** 一族实例到合法输出的关系。
- **instance:** 问题的一次具体输入。
- **input size:** 复杂度变量，排序中通常为 n。
- **output specification:** 合法输出必须满足的数学条件。
- **precondition/postcondition:** 算法前后必须声明的条件。
- **stability:** 相等 key 的相对顺序保持。
- **in-place:** 辅助空间受限，约定要写清。
- **comparison model:** 只能通过比较获得顺序信息。
- **decision tree model:** 把比较过程表示为树。


    ## 5. 最小例子

    Sorting specification: input 是序列 A，output 是序列 B，要求 B 是 A 的 permutation 且非降序。

    ## 6. 反例或 non-example

    “把数组排好”没有说明 permutation、重复元素、顺序和规模变量。

    ## 7. 关键算法

    ### Algorithm: Insertion Sort

- **Problem:** sorting problem
- **Input:** array A[0..n-1]
- **Output:** sorted permutation of A
- **Assumptions:** elements are comparable
- **Algorithm idea:** 维护前缀 A[0..i) 已排序，把 A[i] 插入正确位置。
- **Pseudocode:** `for i=1..n-1: key=A[i]; shift larger elements right; insert key`
- **Invariant or proof structure:** loop invariant: 每轮开始时 A[0..i) 是原前缀的 sorted permutation。
- **Correctness proof:** 初始化 i=1 时单元素前缀已排序；maintenance 由 while 把大于 key 的元素右移且不改变多重集合；termination 时前缀长度为 n。
- **Time complexity:** worst-case O(n^2), best-case O(n); n 是元素个数。
- **Space complexity:** O(1) extra space。
- **Edge cases:** empty array, one element, duplicates
- **Common mistakes:** 把测试几个数组当成 correctness proof。

### Algorithm: Merge Sort

- **Problem:** sorting problem
- **Input:** array A[0..n-1]
- **Output:** sorted permutation of A
- **Assumptions:** elements are comparable
- **Algorithm idea:** 递归排序左右两半，再线性 merge。
- **Pseudocode:** `if n<=1 return A; sort left; sort right; merge`
- **Invariant or proof structure:** induction on n, merge correctness as lemma。
- **Correctness proof:** base n<=1；假设小于 n 的输入能正确排序；左右递归正确，merge 保持 permutation 并输出有序序列。
- **Time complexity:** T(n)=2T(n/2)+O(n)=O(n log n)。
- **Space complexity:** O(n) auxiliary space。
- **Edge cases:** duplicates, uneven split, n not power of two
- **Common mistakes:** 只写 recurrence，不证明 merge 的 postcondition。

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

1. problem 和 algorithm 混淆。
2. correctness specification 晚于 algorithm。
3. stable 与 in-place 混淆。
4. lower bound 没说明 model。


## 11. 与 string algorithms / learning theory / complexity theory 的联系

String algorithms 中 suffix array 排序依赖清晰 ordering specification；complexity theory 中 lower bound 必须绑定 model。

## 12. 必做练习

- 阅读本 note 的所有 algorithm blocks，并手写每个 algorithm 的 Problem/Input/Output。
- 完成 `exercises/week02/day01_exercises.tex` 的前 8 到 10 题。
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


## 完整证明：comparison sorting lower bound via decision tree

**Statement.** 在 comparison model 中，任何 deterministic comparison sorting algorithm 在 worst case 至少需要 \(\Omega(n\log n)\) 次比较。

**Definitions used.** comparison model 只允许通过形如 \(a_i \le a_j\) 的比较获得顺序信息。Decision tree 的 internal node 是一次比较，edge 是比较结果，leaf 对应算法停机并输出一个 permutation。

**Assumptions.** 输入元素两两不同；算法必须对所有 \(n!\) 种相对顺序正确；算法 deterministic；每次比较只有两个结果。

**Goal.** 证明存在某个输入使算法至少做 \(c n\log n\) 次比较，其中 \(c>0\) 为常数且 \(n\) 足够大。

**Strategy.** 把算法的所有可能执行路径表示成 binary decision tree。正确算法必须能区分所有 \(n!\) 个输入排列，所以树至少有 \(n!\) 个 leaves。高度为 \(h\) 的 binary tree 至多有 \(2^h\) 个 leaves，因此 \(2^h \ge n!\)，从而 \(h \ge \log_2(n!) = \Omega(n\log n)\)。

**Proof.** 固定任意 deterministic comparison sorting algorithm A。对所有可能输入运行 A。因为 A 的分支只由比较结果决定，每一次比较对应 binary decision tree 中的一个 internal node。一个从 root 到 leaf 的路径就是某个输入相对顺序触发的比较结果序列，路径长度等于该输入上的比较次数。设这棵树高度为 \(h\)。

对于任意两个不同排列 \(\pi\ne\sigma\)，若它们到达同一个 leaf，则 A 在两个输入上输出同一个排列。但排序正确性要求对排列 \(\pi\) 和 \(\sigma\) 输出不同的相对顺序，因此至少一个输入会被错误排序。这与 A 对所有输入正确矛盾。所以不同排列必须到达不同 leaves，树的 leaves 数 \(L\) 满足 \(L\ge n!\)。

一棵高度为 \(h\) 的 binary tree 至多有 \(2^h\) 个 leaves，因此 \(2^h\ge L\ge n!\)。取对数得 \(h\ge \log_2(n!)\)。使用乘积下界 \(n! \ge (n/2)^{n/2}\)，因为后 \(n/2\) 个因子每个至少为 \(n/2\)。于是
\[
\log_2(n!) \ge \frac n2 \log_2(n/2) = \Omega(n\log n).
\]
高度 \(h\) 是某条执行路径的比较次数，也是 worst-case 比较次数的下界，所以 A 的 worst-case comparison complexity 至少为 \(\Omega(n\log n)\)。由于 A 任意，模型中所有 deterministic comparison sorting algorithms 都满足该下界。

**Check.** 下界没有说非 comparison sorting 也受限；也没有说 insertion sort 的每个输入都慢。它只说明在指定模型中，任何总是正确的 deterministic sorting algorithm 都有某个输入需要 \(\Omega(n\log n)\) comparisons。

**Common mistake.** 把 \(n!\) 个排列说成 \(n^n\) 个输入，或者忘记说明为什么不同排列必须到达不同 leaves。
