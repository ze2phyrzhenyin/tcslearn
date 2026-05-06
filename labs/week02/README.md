# Week 2 Labs

These labs build intuition for algorithmic thinking, data structures, and proof patterns. They are not proofs. A passing assert or a timing-like table only checks examples; the theorem still needs a specification, invariant, and proof.

## How to Run

Run from the repository root:

```bash
python3 labs/week02/sorting_and_lower_bounds.py
python3 labs/week02/divide_and_conquer_sandbox.py
python3 labs/week02/heaps_hashing_amortization.py
python3 labs/week02/graph_algorithms.py
python3 labs/week02/greedy_vs_dp_examples.py
python3 labs/week02/randomized_algorithms.py
```

## Lab Map

- Day 1: `sorting_and_lower_bounds.py` compares growth and decision-tree leaves for comparison sorting.
- Day 2: `divide_and_conquer_sandbox.py` runs binary search, merge sort, quickselect, and recurrence expansion.
- Day 3: `heaps_hashing_amortization.py` checks heap invariants, chained hashing, and dynamic-array resizing.
- Day 4: `graph_algorithms.py` implements BFS, DFS, connected components, shortest paths, and topological sort.
- Day 6: `greedy_vs_dp_examples.py` contrasts interval scheduling greedy with coin-change greedy failure and DP examples.
- Day 7: `randomized_algorithms.py` simulates randomized quicksort, quickselect, and amplification.

## How to Use Results

After running a lab, write one sentence in `review/week02/week02_review.md`:

> The experiment suggests ..., but it does not prove ... because ...

If an output surprises you, record it in `state/open_questions.md` or `state/mistakes_log.md`.
