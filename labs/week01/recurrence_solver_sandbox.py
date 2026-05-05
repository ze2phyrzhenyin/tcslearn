"""Recurrence solver sandbox for Week 1 Day 3.

Mathematical meaning:
    This script expands several recurrences numerically to help guess growth
    rates. A numerical pattern is not a proof; prove recurrence bounds with
    induction, recursion trees, or a theorem whose assumptions are checked.

Run:
    python3 labs/week01/recurrence_solver_sandbox.py
"""

from __future__ import annotations

import functools
import math


@functools.lru_cache(maxsize=None)
def merge_sort_like(n: int) -> int:
    """T(n)=2T(n/2)+n for powers of two, T(1)=1."""
    if n <= 1:
        return 1
    return 2 * merge_sort_like(n // 2) + n


@functools.lru_cache(maxsize=None)
def binary_search_like(n: int) -> int:
    """T(n)=T(n/2)+1, T(1)=1."""
    if n <= 1:
        return 1
    return binary_search_like(n // 2) + 1


@functools.lru_cache(maxsize=None)
def quadratic_split(n: int) -> int:
    """T(n)=4T(n/2)+n, T(1)=1."""
    if n <= 1:
        return 1
    return 4 * quadratic_split(n // 2) + n


def powers_of_two(max_power: int) -> list[int]:
    return [2**k for k in range(max_power + 1)]


def main() -> None:
    print("Numerical recurrence expansion. Use it for guesses, not proof.")
    print("    n | T_merge | T/(n log2 n) | T_binary | T_quad | T_quad/n^2")
    print("-" * 74)
    for n in powers_of_two(8)[1:]:
        merge = merge_sort_like(n)
        binary = binary_search_like(n)
        quad = quadratic_split(n)
        n_log_n = n * math.log2(n)
        ratio_merge = merge / n_log_n if n_log_n else float("nan")
        ratio_quad = quad / (n * n)
        print(
            f"{n:>5} | {merge:>7} | {ratio_merge:>12.3f} | "
            f"{binary:>8} | {quad:>6} | {ratio_quad:>10.3f}"
        )

    assert merge_sort_like(1) == 1
    assert merge_sort_like(8) == 32
    assert binary_search_like(8) == 4
    assert quadratic_split(4) == 28


if __name__ == "__main__":
    main()
