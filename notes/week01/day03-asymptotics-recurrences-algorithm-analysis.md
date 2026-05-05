# Day 3 - Asymptotics, Recurrences, Algorithm Analysis

## 1. 今日目标

今天建立算法分析语言。学完后你应该能：

- 用定义证明 `O`、`Omega`、`Theta`、`o`、`omega`；
- 明确说明变量趋向，例如 `n -> infinity`；
- 区分 worst-case、average-case 和 amortized intuition；
- 用 recursion tree、substitution method 和 basic Master theorem 解简单 recurrence；
- 写出算法复杂度分析中的 input size、model、correctness 和 complexity。

## 2. 为什么这个主题对 TCS 重要

TCS 关心问题能否被高效计算。Asymptotic notation 把实现细节中的常数和机器噪声抽离出来，但这不是“随便忽略”。它是关于函数集合的严格定义。Recurrence 是递归算法、divide and conquer 和 dynamic programming 的基础语言。

## 3. 预备概念

需要函数、quantifier、induction。默认 `n` 是 input size，且 `n` 趋向 infinity。若有多个变量，例如 text 长度 `n` 和 pattern 长度 `m`，必须同时声明。

## 4. 核心定义

- **Big-O**：`f(n) in O(g(n))` iff 存在常数 `c>0` 和 `n0`，使所有 `n>=n0` 有 `0 <= f(n) <= c g(n)`。
- **Big-Omega**：`f(n) in Omega(g(n))` iff 存在 `c>0,n0`，使所有 `n>=n0` 有 `0 <= c g(n) <= f(n)`。
- **Big-Theta**：`Theta(g)=O(g) cap Omega(g)`。
- **little-o**：`f in o(g)` iff 对任意 `c>0`，存在 `n0`，使 `n>=n0` 时 `0<=f(n)<c g(n)`；等价直觉是 `f/g -> 0`。
- **little-omega**：`f in omega(g)` iff 对任意 `c>0`，最终 `f(n)>c g(n)`；直觉是 `f/g -> infinity`。
- **worst-case**：固定 input size，取所有输入中最大 running time。
- **average-case**：需要明确 input distribution，不是“平均感觉”。
- **amortized intuition**：一串 operations 的总成本低，单次坏情况可被其他便宜操作分摊。
- **recurrence**：用较小规模值定义当前规模值，例如 `T(n)=2T(n/2)+n`。
- **recursion tree**：把递归调用展开成 tree，按 level 估计总成本。
- **substitution method**：猜一个 bound，再用 induction 证明。
- **Master theorem basic form**：对 `T(n)=aT(n/b)+f(n)` 比较 `f(n)` 与 `n^{log_b a}`。
- **RAM model intuition**：把基本算术、比较、数组访问视作常数时间；这是分析模型，不是硬件事实。

## 5. 最小例子

证明 `3n^2+5n+7 in O(n^2)`。

令 `n>=1`，则 `5n <= 5n^2`，`7 <= 7n^2`，所以 `3n^2+5n+7 <= 15n^2`。取 `c=15,n0=1`，由 Big-O 定义得到结论。

Recurrence 例子：`T(n)=2T(n/2)+n`。每层总 work 约为 `n`，深度 `log_2 n`，所以 recursion tree 提示 `T(n) in Theta(n log n)`。这是猜测；严格证明可用 substitution。

## 6. 反例或 non-example

- `2^n in O(n^10)` 是假的，因为 exponential eventually dominates polynomial。
- `f(n)=O(g(n))` 不表示 `f(n)` 与 `g(n)` 约等于；`n in O(n^2)` 也成立。
- Average-case 没有 input distribution 就没有定义。
- Recurrence 没有 base case 不是完整定义，例如 `T(1)=1`。

## 7. 关键定理或命题

**Claim 1: If `f in O(g)` and `g in O(h)`, then `f in O(h)`.**

Assumptions: 函数最终非负。  
Goal: Big-O transitivity。  
Proof idea: 取两个 Big-O 定义中的常数和阈值，把不等式相乘，并取较大阈值。

**Claim 2: For `T(n)=2T(n/2)+n` with `T(1)=1` and `n` power of 2, `T(n) in Theta(n log n)`.**

Assumptions: `n=2^k`。  
Goal: `T(n)` 上下界。  
Proof idea: recursion tree 每层 `n`，共有 `log_2 n + 1` 层；也可用 induction 验证。

## 8. 证明模板

### Big-O proof

Statement: `f(n) in O(g(n))` as `n -> infinity`。  
Assumptions: `g(n)` eventually positive。  
Goal: find `c,n0`。  
Proof: 对 `n>=n0`，把低阶项界到主项上。  
Check: 常数必须不依赖 `n`。

### Recurrence substitution

1. Guess `T(n) <= C h(n)`。
2. Verify base cases by choosing `C` large enough。
3. Substitute recurrence。
4. Use induction hypothesis on smaller inputs。
5. Finish inequality and state domain restrictions。

## 9. 常见错误

- 写 `O(n^2)` 时不说明变量。
- 把 Big-O 当 equality 使用。
- 只证明 upper bound 却声称 `Theta`。
- Recurrence 忘记 base case 和整数取整。
- Master theorem 条件不满足还硬套。
- 把 Python 实测时间当作复杂度证明。
- 混淆 algorithm 的 complexity 和某个 implementation 的 overhead。

## 10. 与 algorithms / strings / learning theory 的联系

- String matching 需要同时声明 `n=|text|` 和 `m=|pattern|`。
- Learning theory 的 sample complexity 也使用 asymptotic notation，但变量可能是 `epsilon`、`delta`、hypothesis class size。
- Lower bound mindset 帮你区分“我没想到快算法”和“任何算法都必须付出某种成本”。

## 11. 必做练习

见 `exercises/week01/day03_exercises.tex`：1-10，并运行：

```bash
python3 labs/week01/asymptotics_experiments.py
python3 labs/week01/recurrence_solver_sandbox.py
```

## 12. 选做练习

见 `exercises/week01/day03_exercises.tex`：11-14。选做题偏 proof rigor 和 lower-bound intuition。

## 13. 自测问题

- `f in O(g)` 的 `c` 和 `n0` 能依赖 `n` 吗？
- `Theta` 需要证明哪两个方向？
- 为什么 average-case 必须给 distribution？
- Recursion tree 给的是 proof 还是 proof idea？
- Master theorem 的比较对象是什么？

## 14. 明天复习什么

明天进入 counting 和 graphs。复习 product rule 和 recursive decomposition，因为很多 counting proof 与 recurrence proof 共享“拆成子问题”的思路。

