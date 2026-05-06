# Week 2 Self-Test

Time limit: 120 minutes. Do not use solutions during the test. Answers belong in `exercises/week02/week02_solutions.tex`; this file contains prompts and grading standards only.

## Short Answer (10 questions, 20 points)

1. Define algorithmic problem and explain how it differs from an algorithm.
2. Define precondition and postcondition for binary search.
3. What does comparison model allow and forbid?
4. State the difference between stable and in-place sorting.
5. What is a representation invariant?
6. Why is amortized analysis not average-case analysis?
7. State the BFS shortest-path invariant in an unweighted graph.
8. What does greedy choice is safe mean?
9. Define DP state for edit distance.
10. Distinguish Las Vegas and Monte Carlo algorithms.

## Algorithm Correctness Proofs (5 questions, 35 points)

1. Prove insertion sort correctness using a loop invariant.
2. Prove merge sort correctness using induction and a merge lemma.
3. Prove heap insert preserves the heap invariant.
4. Prove BFS computes shortest path distances in an unweighted graph.
5. Prove earliest-finish-time interval scheduling is optimal using exchange argument.

## Complexity Analysis (4 questions, 20 points)

1. Solve T(n)=2T(n/2)+n with a recursion tree.
2. Analyze binary search worst-case comparisons.
3. Analyze chained hash table search under simple uniform hashing and state the worst case.
4. Prove dynamic array append is amortized O(1) by aggregate method.

## Design Questions (3 questions, 24 points)

1. Design a divide-and-conquer algorithm for min/max pair and prove correctness.
2. Design a DP for longest increasing subsequence and include reconstruction.
3. Design graph traversal to find connected components and analyze complexity.

## Randomized / Amortized Questions (2 questions, 16 points)

1. Define sample space and expected running time random variable for randomized quickselect.
2. A Monte Carlo algorithm fails with probability at most 1/4 per independent run. Give an amplification scheme and bound the probability all runs fail.

## Comprehensive Question (1 question, 25 points)

Formalize, solve, and analyze the following problem: given a directed acyclic graph with edge weights, compute a shortest path from s to every reachable vertex. Your answer must include problem specification, algorithm idea, pseudocode, correctness proof by state/order induction, and time complexity with variables.

## Grading Standards

- Specification clarity: 20%.
- Correct proof pattern and explicit assumptions: 30%.
- Step-by-step proof details: 25%.
- Complexity variables and model assumptions: 15%.
- Edge cases and common mistakes: 10%.

Do not grade yourself by final answer only. A correct numeric bound with a missing specification should lose credit.
