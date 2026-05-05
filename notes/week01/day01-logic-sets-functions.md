# Day 1 - Logic, Sets, Functions, Relations, Proof Language

## 1. 今日目标

今天的目标不是“见过这些词”，而是能写出可检查的数学句子。学习结束后你应该能：

- 正确使用 `forall`、`exists`、implication、contrapositive 和 contradiction；
- 否定含多个量词的命题；
- 证明两个集合相等；
- 判断 relation 是否为 equivalence relation 或 partial order；
- 证明 function 是 injective、surjective 或 bijective；
- 构造反例来否定过强命题。

## 2. 为什么这个主题对 TCS 重要

TCS 的对象通常是集合、字符串、函数、关系、图、语言、算法和概率空间。若量词、定义域、条件和结论写不清，后面的 theorem statement、algorithm correctness、reduction 和 generalization bound 都会失去意义。严谨证明首先是严谨语言。

## 3. 预备概念

需要能读懂基本符号：`in`、`notin`、`subseteq`、`emptyset`、`N`、`Z`、`R`、`->`。本日默认所有变量都必须有 domain。例如不要写“对所有 x”，要写“对所有 `x in R`”或“对所有 binary string `x`”。

## 4. 核心定义

### Logic and Proof Language

- **proposition**：有确定 truth value 的陈述句。例如“`2` is even”。Non-example：“`x` is even”，除非指定 `x`。
- **predicate**：含变量的命题模板。例如 `P(x): x^2 >= 0` over `R`。
- **quantifier**：`forall x in S, P(x)` 表示所有元素满足；`exists x in S, P(x)` 表示至少一个元素满足。
- **implication**：`P -> Q` 表示只要 `P` 为真，`Q` 必须为真。它不声称 `P` 一定发生。
- **converse**：`Q -> P`。通常不等价于原命题。
- **inverse**：`not P -> not Q`。通常也不等价于原命题。
- **contrapositive**：`not Q -> not P`。它与 `P -> Q` 逻辑等价。
- **direct proof**：从 assumptions 和 definitions 出发推出 goal。
- **proof by contraposition**：证明 `not Q -> not P` 来证明 `P -> Q`。
- **proof by contradiction**：假设 claim 为假，推出与 assumption、定义或已知定理矛盾。

### Sets and Relations

- **set**：对象的集合，元素是否属于集合必须明确。
- **subset**：`A subseteq B` 表示 `forall x, x in A -> x in B`。
- **power set**：`P(A)` 是 `A` 所有 subset 的集合。
- **union**：`A union B = {x: x in A or x in B}`。
- **intersection**：`A cap B = {x: x in A and x in B}`。
- **complement**：相对于 universe `U`，`A^c = {x in U: x notin A}`。
- **Cartesian product**：`A x B = {(a,b): a in A, b in B}`。
- **relation**：从 `A` 到 `B` 的 relation 是 `A x B` 的 subset。二元 relation on `A` 是 `A x A` 的 subset。
- **equivalence relation**：reflexive、symmetric、transitive 的 relation。
- **partial order**：reflexive、antisymmetric、transitive 的 relation。

### Functions

- **function**：`f: A -> B` 给每个 `a in A` 分配唯一的 `f(a) in B`。`A` 是 domain，`B` 是 codomain。
- **injective**：`f(a)=f(a') -> a=a'`。不同输入不会撞到同一输出。
- **surjective**：`forall b in B, exists a in A such that f(a)=b`。codomain 中每个元素都被命中。
- **bijective**：既 injective 又 surjective。
- **image**：`f(S) = {f(x): x in S}`。
- **preimage**：`f^{-1}(T) = {x in A: f(x) in T}`，这里不要求 `f` 有 inverse function。

## 5. 最小例子

设 `f: Z -> Z`，`f(x)=x+1`。

- injective：若 `f(a)=f(b)`，则 `a+1=b+1`，所以 `a=b`。
- surjective：对任意 `y in Z`，取 `x=y-1`，则 `f(x)=y`。
- 所以 `f` 是 bijection。

集合相等例子：证明 `A cap B subseteq A`。任取 `x in A cap B`，由 intersection 定义得到 `x in A and x in B`，因此 `x in A`。

## 6. 反例或 non-example

- `f: Z -> Z, f(x)=x^2` 不是 injective，因为 `f(1)=f(-1)=1` 但 `1 != -1`。
- `f: Z -> Z, f(x)=x^2` 不是 surjective，因为 `-1 in Z`，不存在整数 `x` 使 `x^2=-1`。
- “若 `n` 是 4 的倍数，则 `n` 是偶数”的 converse 是“若 `n` 是偶数，则 `n` 是 4 的倍数”，反例 `n=2`。
- Relation `R` on integers defined by `a R b` iff `a < b` 不是 equivalence relation，因为不 reflexive。

## 7. 关键定理或命题

**Claim 1: Implication is equivalent to contrapositive.**

Assumptions: `P` 和 `Q` 是 propositions。  
Goal: `P -> Q` 与 `not Q -> not P` truth value 相同。  
Proof idea: 分析 `P` 和 `Q` 的四种 truth assignments。唯一让 `P -> Q` 为假的情况是 `P` true 且 `Q` false；这也正是 `not Q -> not P` 为假的情况。

**Claim 2: Set equality by double inclusion.**

Assumptions: `A` 和 `B` 是同一 universe 中的 sets。  
Goal: `A = B` iff `A subseteq B` and `B subseteq A`。  
Proof idea: 元素属于集合只看 membership。若两个方向 inclusion 都成立，则任意元素在 `A` 中当且仅当在 `B` 中。

## 8. 证明模板

### 否定量词命题

Statement: `forall x in S, exists y in T, P(x,y)`。  
Negation: `exists x in S such that forall y in T, not P(x,y)`。  
Check: 否定时每个 quantifier 翻转，predicate 取否定，变量 domain 保留。

### 证明集合相等

1. Prove `A subseteq B`: 任取 `x in A`，用 definitions 推出 `x in B`。
2. Prove `B subseteq A`: 任取 `x in B`，用 definitions 推出 `x in A`。
3. Conclude `A=B` by extensionality of sets。

### 证明 injective / surjective

Injective: 假设 `f(a)=f(a')`，推出 `a=a'`。  
Surjective: 任取 `b in codomain`，构造 `a in domain` 使 `f(a)=b`。

## 9. 常见错误

- 把 `P -> Q` 当成 `Q -> P`。
- 否定 `forall x exists y` 时忘记交换 quantifier。
- 证明 set equality 只证了一个 inclusion。
- 证明 surjective 时忘记目标是 codomain 的每个元素。
- 把 `f^{-1}(T)` 当成 inverse function；preimage 对任何 function 都有定义。
- 反例没有满足原命题的 domain。

## 10. 与 algorithms / strings / learning theory 的联系

- Algorithms correctness 几乎总是 implication：如果输入满足 precondition，则输出满足 postcondition。
- String algorithms 中 language 是 string 的 set，pattern matching 可写成 relation。
- Learning theory 中 hypothesis 是 function，loss 是 function，generalization statement 充满 quantifier。

## 11. 必做练习

见 `exercises/week01/day01_exercises.tex`：1-9。重点完成量词否定、集合恒等式、injective/surjective 和反例。

## 12. 选做练习

见 `exercises/week01/day01_exercises.tex`：10-12。把每题 proof strategy 写在证明前。

## 13. 自测问题

- 如何否定 `forall x exists y forall z P(x,y,z)`？
- `P -> Q` 的 contrapositive、converse、inverse 分别是什么？
- 证明 `A=B` 为什么通常要两个方向？
- 证明 surjective 时为什么必须看 codomain？
- 给出一个 relation 是 equivalence relation 但不是 partial order 的例子。

## 14. 明天复习什么

明天开始 induction。复习今天的 implication、predicate、function 和 relation，因为 induction statement 本身就是一个带 `forall n` 的 predicate family。

