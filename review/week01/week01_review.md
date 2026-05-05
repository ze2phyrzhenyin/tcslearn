# Week 1 Review - Foundations

## Purpose

Week 1 建立 TCS 的基础语言：definition、proof、algorithm analysis、discrete structures、probability、linear algebra intuition 和 formal models。不要把这一周当作“看完概念列表”，要把它当作证明和形式化训练周。

## Daily Review Plan

### Day 1

- 默写 quantifier negation rules。
- 重做一个 set equality proof。
- 证明一个 function injective / surjective。

### Day 2

- 对一个 induction proof 写出 base、hypothesis、step。
- 对一个 loop 写出 initialization、maintenance、termination。
- 解释 correctness 与 running time 为什么不同。

### Day 3

- 用定义证明一个 Big-O 和一个 Big-Omega。
- 展开一个 recurrence tree。
- 说明 input size 和 model。

### Day 4

- 对 counting problem 先标 ordered/unordered、repetition/no repetition。
- 证明 tree edge count。
- 把一个自然语言过程建模为 graph。

### Day 5

- 每题概率先写 sample space。
- 练习 indicator random variable。
- 区分 independent 和 disjoint。

### Day 6

- 默写 norm axioms。
- 用 Cauchy-Schwarz 做一个不等式。
- 用 convexity definition 判断 set/function。

### Day 7

- 把 problem 和 algorithm 分开写。
- 写一个 language。
- 对 reduction 标 source、target、mapping、two directions。

## Definitions That Must Be Stable

- proposition, predicate, quantifier, implication, contrapositive
- set, subset, Cartesian product, relation, equivalence relation, partial order
- function, injective, surjective, image, preimage
- induction, strong induction, structural induction, loop invariant, termination
- Big-O, Big-Omega, Big-Theta, recurrence, RAM model
- permutation, combination, graph, path, cycle, tree, bipartite graph
- sample space, event, random variable, expectation, variance, union bound
- vector, matrix, inner product, norm, convex set, convex function
- alphabet, string, language, decision problem, DFA, reduction

## Proofs to Reconstruct Without Looking

1. Implication equivalent to contrapositive by truth table.
2. Set equality by double inclusion.
3. Sum formula by ordinary induction.
4. Prime factorization by strong induction.
5. Prefix-sum loop invariant.
6. Big-O transitivity.
7. Tree has `n-1` edges.
8. Linearity of expectation.
9. Union bound by indicators.
10. DFA parity correctness by prefix invariant.

## Labs to Run

```bash
python3 labs/week01/asymptotics_experiments.py
python3 labs/week01/recurrence_solver_sandbox.py
python3 labs/week01/probability_simulations.py
python3 labs/week01/finite_automata_toy.py
```

For each lab, write one sentence beginning with: “This experiment suggests ..., but it does not prove ...”.

## Repair Priorities

1. Quantifier order.
2. Induction hypothesis precision.
3. Invariant strength.
4. Big-O variable and direction.
5. Sample space and independence assumptions.
6. Reduction direction.

## Weekly Retrospective Questions

- Which definitions can I write exactly?
- Which proof template still feels mechanical?
- Which exercise did I get wrong because of a missing assumption?
- Which lab intuition can I now turn into a theorem statement?
- What should Codex diagnose next: Day 1 only, or whole Week 1?

