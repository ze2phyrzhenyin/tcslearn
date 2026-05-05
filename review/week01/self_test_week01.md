# Week 1 Self-Test - 90 Minutes

Do not look at `week01_solutions.tex` while taking this test. Answers and repair references belong in `exercises/week01/week01_solutions.tex`.

## Timing

- Short answer: 20 minutes
- Proofs: 35 minutes
- Calculations: 15 minutes
- Modeling: 10 minutes
- Integrated problem: 10 minutes

## Short Answer - 10 Questions

1. State the negation of `forall x exists y P(x,y)`.
2. Explain why `P -> Q` is not the same as `Q -> P`.
3. Define injective and surjective.
4. What are the three parts of a loop invariant proof?
5. What does `f in O(g)` mean, including constants?
6. State the difference between ordered and unordered counting.
7. Define sample space and random variable.
8. Why does linearity of expectation not require independence?
9. State Cauchy-Schwarz in `R^d`.
10. What is a language in TCS?

## Proofs - 6 Questions

1. Prove `A cap (B union C) = (A cap B) union (A cap C)`.
2. Prove by induction that `sum_{i=1}^n i = n(n+1)/2`.
3. Prove by strong induction that every `n >= 2` is a product of primes.
4. Prove that every finite tree with `n` vertices has `n-1` edges.
5. Prove union bound for two events.
6. Prove correctness of the DFA accepting binary strings with even number of `1`s.

## Calculations - 4 Questions

1. Compute `||x||_1`, `||x||_2`, `||x||_infty` for `x=(2,-1,2)`.
2. Solve `T(n)=2T(n/2)+n`, `T(1)=1`, for powers of two.
3. Count length-6 strings over `{0,1,2,3}` with no restriction.
4. Roll two dice. Compute `Pr[sum=8 | first die is 2]`.

## Modeling - 2 Questions

1. Formalize: given text `t` and pattern `p`, decide whether `p` appears in `t`.
2. Model binary strings of length at most 2 as a rooted tree.

## Integrated Problem - 1 Question

Design a theorem statement and proof roadmap for binary search correctness. Include input assumptions, output specification, invariant, termination argument, and running time.

## Scoring Rubric

- Short answer: 20 points, 2 each. Full credit requires exact definitions and domains when relevant.
- Proofs: 36 points, 6 each. Award 1 point for assumptions, 1 for strategy, 3 for correct proof, 1 for checking edge cases.
- Calculations: 16 points, 4 each. Award partial credit for correct setup.
- Modeling: 12 points, 6 each. Award credit for input, output, encoding or object definition, and edge cases.
- Integrated problem: 16 points. Award 4 for statement, 4 for invariant, 4 for correctness roadmap, 2 for termination, 2 for complexity.

Score interpretation:

- 85-100: proceed after reviewing mistakes.
- 70-84: request Codex diagnostic feedback for weak sections.
- Below 70: redo Day 1-Day 3 foundations before starting Week 2.

