# Day 6 - Linear Algebra and Convexity for TCS / Learning Theory

## 1. 今日目标

今天不是完整线性代数课，而是建立 learning theory、optimization 和 online learning 常用的几何语言。学完后你应该能：

- 定义 vector、matrix、inner product、norm、distance；
- 区分 `L1`、`L2`、`Linf` norms；
- 使用 Cauchy-Schwarz 和 triangle inequality；
- 解释 linear map、rank 和 eigenvalue intuition；
- 定义 convex set、convex function、Jensen inequality；
- 说明 gradient、Lipschitz continuity、projection 和 separating geometry 的基本直觉。

## 2. 为什么这个主题对 TCS 重要

Learning theory 中 hypothesis space 可以是向量空间中的集合，loss 可以是 convex function，regularization 是 norm penalty。Optimization 的可控性来自 convexity。Online learning 和 OCO 更是直接用几何不等式证明 regret bounds。

## 3. 预备概念

需要 functions、sets、inequalities 和 basic calculus intuition。今天只使用有限维实向量空间 `R^d`。

## 4. 核心定义

- **vector**：`R^d` 中的 ordered tuple，例如 `x=(x_1,...,x_d)`。
- **matrix**：数字表，可表示 linear map。
- **inner product**：`<x,y>=sum_i x_i y_i`，定义长度、角度和相似度。
- **norm**：满足 nonnegativity、definiteness、homogeneity、triangle inequality 的长度函数。
- **L1 norm**：`||x||_1=sum_i |x_i|`。
- **L2 norm**：`||x||_2=sqrt(sum_i x_i^2)`。
- **Linf norm**：`||x||_infty=max_i |x_i|`。
- **distance**：由 norm 定义 `d(x,y)=||x-y||`。
- **Cauchy-Schwarz inequality**：`|<x,y>| <= ||x||_2 ||y||_2`。
- **triangle inequality**：`||x+y|| <= ||x||+||y||`。
- **linear map**：`T(ax+by)=aT(x)+bT(y)`。
- **rank intuition**：linear map 输出能覆盖的 independent directions 数量。
- **eigenvalue intuition**：某些方向只被缩放不被旋转，`Av=lambda v`。
- **convex set**：任意两点连线仍在集合中。
- **convex function**：`f(lambda x+(1-lambda)y) <= lambda f(x)+(1-lambda)f(y)`。
- **Jensen inequality**：convex function of average 不超过 average of function values。
- **gradient intuition**：局部最陡上升方向。
- **Lipschitz continuity**：输入变化不大时输出变化有统一上界。
- **projection intuition**：把点拉回约束集合中最近的位置。
- **separating geometry intuition**：convex sets 常可被 hyperplane 分开；本周只需直觉。

## 5. 最小例子

对 `x=(1,2)`，`y=(3,0)`：

- `<x,y>=3`；
- `||x||_1=3`，`||x||_2=sqrt(5)`，`||x||_infty=2`；
- `|<x,y>|=3 <= sqrt(5)*3`，符合 Cauchy-Schwarz。

Convex set 例子：`[0,1]` 是 convex；任意两点之间的线段仍在 `[0,1]`。

## 6. 反例或 non-example

- `||x||_0` 常表示非零坐标数量，但它不是 norm，因为不满足 homogeneity。
- `{0,1}` 不是 convex set，因为 `0` 和 `1` 的 midpoint `0.5` 不在集合中。
- 函数 `f(x)=-x^2` 在 `R` 上不是 convex。
- Inner product 不是普通乘法；它把两个向量映射成 scalar。

## 7. 关键定理或命题

**Claim 1: Cauchy-Schwarz inequality in `R^d`.**

Assumptions: `x,y in R^d`，使用 standard inner product。  
Goal: `|<x,y>| <= ||x||_2||y||_2`。  
Proof idea: 若 `y=0` 直接成立。否则考虑非负函数 `||x-ty||_2^2` 对所有 real `t` 都非负；其 quadratic discriminant 不大于 0，推出不等式。

**Claim 2: Convex combinations preserve convex set membership.**

Assumptions: `C` convex，`x,y in C`，`lambda in [0,1]`。  
Goal: `lambda x+(1-lambda)y in C`。  
Proof idea: 这是 convex set 定义本身；关键是检查 `lambda` 范围和两点都在 `C`。

## 8. 证明模板

### Norm proof

1. State function `||.||`.
2. Check nonnegativity.
3. Check `||x||=0 iff x=0`.
4. Check homogeneity.
5. Check triangle inequality.

### Convexity proof

1. Take arbitrary `x,y` in domain and `lambda in [0,1]`.
2. Show the convex combination stays in domain if proving set convexity.
3. Show function inequality if proving function convexity.
4. Avoid relying only on picture intuition.

## 9. 常见错误

- 把 norm 当作 coordinate-wise absolute value。
- 使用 Cauchy-Schwarz 时没有说明使用哪个 norm。
- Convex set 与 connected set 混淆。
- Convex function 与 increasing function 混淆。
- Jensen inequality 没检查 convexity。
- Gradient 直觉代替 convergence proof。

## 10. 与 algorithms / strings / learning theory 的联系

- Learning theory 中 linear classifier 是 vector `w` 定义的 function。
- Convex loss 让 optimization 问题更可控。
- Norm bound 和 Lipschitz condition 常出现在 generalization 和 regret analysis。
- String algorithms 本周联系较弱，但 edit distance、embeddings 和 kernels 会用几何语言。

## 11. 必做练习

见 `exercises/week01/day06_exercises.tex`：1-9。重点检查 norm axioms、Cauchy-Schwarz 和 convexity definition。

## 12. 选做练习

见 `exercises/week01/day06_exercises.tex`：10-12。选做题连接 learning theory 的 hypothesis space 直觉。

## 13. 自测问题

- 为什么 `L1`、`L2`、`Linf` 都是长度概念但形状不同？
- Cauchy-Schwarz 的左右两边分别是什么？
- Convex set 的定义中 `lambda` 范围是什么？
- Jensen inequality 是关于什么方向的不等式？
- Hypothesis space 为什么可以看成几何对象？

## 14. 明天复习什么

明天把本周所有内容连接到 models、languages 和 reductions。复习 set、function、graph、probability 和 proof templates，因为 formal model 会把这些全部重新组合起来。

