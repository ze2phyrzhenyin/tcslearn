# Day 7 - Models, Languages, Reductions, Synthesis

## 1. 今日目标

今天把第一周基础连接到真正的 TCS。学完后你应该能：

- 区分 problem、algorithm、input encoding 和 computational model；
- 定义 alphabet、string、language、decision/search/optimization problem；
- 解释 deterministic algorithm、randomized algorithm、finite automaton 和 Turing machine intuition；
- 写出 correctness specification、theorem statement 和 proof roadmap；
- 理解 many-one reduction 的方向和 lower-bound intuition。

## 2. 为什么这个主题对 TCS 重要

理论计算机科学不是只研究某段代码，而是研究形式化问题在模型中的可计算性和复杂度。Language 把 decision problem 变成 string set。Reduction 把问题之间的难度关系变成可证明的 statement。Formal model 是为了让 theorem 有对象。

## 3. 预备概念

需要 sets、functions、relations、graphs、asymptotics、probability 和 proof language。DFA 可看成一个带状态集合和 transition function 的数学对象。

## 4. 核心定义

- **alphabet**：有限符号集合，常写 `Sigma`。
- **string**：alphabet 上的有限序列。
- **language**：`Sigma*` 的 subset，即一组 strings。
- **decision problem**：输出 yes/no 的问题，可对应 language。
- **search problem**：要求找 witness 或 solution。
- **optimization problem**：要求最优值或最优 solution。
- **computational model**：规定算法可执行操作和成本的数学模型。
- **deterministic algorithm**：同一输入总有同一路径和输出。
- **randomized algorithm**：使用内部随机性；输出和运行路径可能随机。
- **finite automaton**：有限状态、transition function、start state、accepting states 的模型。
- **Turing machine intuition**：更强的抽象计算模型，可读写 tape；本周只需知道它提供可计算性的形式对象。
- **reduction**：把 problem `A` 的实例有效转换成 problem `B` 的实例，使得解 `B` 能解 `A`。
- **many-one reduction intuition**：用 computable function `f` 使 `x in A iff f(x) in B`。
- **lower bound via reduction**：若 `A` 已知难，且 `A` reduces to `B`，则 `B` 至少和 `A` 一样难。
- **correctness specification**：precondition、output condition、success probability、complexity target。
- **theorem statement design**：明确对象、assumptions、conclusion、variables。
- **proof roadmap**：definition setup -> key lemmas -> main proof -> edge cases。

## 5. 最小例子

Alphabet `Sigma={0,1}`。Language `L_even={w in Sigma*: w has an even number of 1s}`。一个 DFA 可以用两个 states：`even` 和 `odd`。读到 `1` 切换状态，读到 `0` 保持状态；start 和 accept state 是 `even`。

Decision problem：给定 binary string `w`，问 `w in L_even` 吗？Algorithm 是实际判断方法；problem 是输入输出关系。

## 6. 反例或 non-example

- “排序算法”不是一个 decision problem；但“给定数组是否已排序”是 decision problem。
- “这个问题看起来难”不是 lower bound。
- Reduction 方向反了会得出错误结论。要证明 `B` 难，通常从已知难的 `A` reduce 到 `B`。
- Language 是 strings 的 set，不是 natural language。
- DFA 只有有限 memory，不能代表所有计算。

## 7. 关键定理或命题

**Claim 1: Every decision problem over encoded inputs can be viewed as a language.**

Assumptions: 每个 input 有 string encoding，yes-instances 被明确规定。  
Goal: yes-instances 构成 `Sigma*` 的 subset。  
Proof idea: 定义 `L={enc(x): x is a yes-instance}`。这就是 language。重点是 encoding 必须固定。

**Claim 2: Correct many-one reduction transfers algorithms backward.**

Assumptions: `A <=_m B` via computable `f` and `x in A iff f(x) in B`；有算法 solves `B`。  
Goal: 有算法 solves `A`。  
Proof idea: 输入 `x`，计算 `f(x)`，运行 `B` 的算法，返回同一 yes/no。Correctness 来自 iff condition。

## 8. 证明模板

### Formalizing a problem

1. Define input type and encoding.
2. Define output type.
3. State yes/no condition or objective.
4. Define size parameter.
5. State assumptions and edge cases.

### Reduction proof

1. Name source problem `A` and target problem `B`.
2. Define mapping `f`.
3. Prove `f` computable within required resource bound.
4. Prove forward direction: `x in A -> f(x) in B`.
5. Prove backward direction: `f(x) in B -> x in A`.
6. State consequence.

## 9. 常见错误

- 把 problem 和 algorithm 混为一谈。
- 不说明 input encoding。
- 把 search problem 当 decision problem 却不解释转换。
- Reduction 方向写反。
- 只证明 reduction 的一个方向。
- 把 randomized algorithm 的一次成功运行当 deterministic correctness。
- Formal model 用词很多但没有可检查定义。

## 10. 与 algorithms / strings / learning theory 的联系

- String algorithms 的基本对象就是 alphabet、string 和 language。
- Learning theory 中 hypothesis class 是 functions 的 set，learning problem 需要明确 sample space 和 loss。
- Complexity theory 以 decision problem、language、model 和 reduction 为核心。
- DP proof 也需要 model：dataset、neighboring relation、mechanism、output event。

## 11. 必做练习

见 `exercises/week01/day07_exercises.tex`：1-9，并运行：

```bash
python3 labs/week01/finite_automata_toy.py
```

## 12. 选做练习

见 `exercises/week01/day07_exercises.tex`：10-12。选做题要求写出 formal theorem statement 和 proof roadmap。

## 13. 自测问题

- Language 为什么是 strings 的 set？
- Problem 和 algorithm 的区别是什么？
- Reduction 的 source 和 target 分别是什么？
- Lower bound 为什么不能来自“看起来难”？
- DFA 为什么只能表示有限状态信息？

## 14. 明天复习什么

明天不进入新主题。复习 Week 1 的 definitions、proof templates、problem set 错题和 labs。优先修复：量词、induction hypothesis、Big-O 变量、sample space、reduction direction。

