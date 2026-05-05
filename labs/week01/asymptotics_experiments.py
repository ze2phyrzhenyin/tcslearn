"""Asymptotics experiments for Week 1 Day 3.

Mathematical meaning:
    This script prints values of several growth-rate functions on the same
    input sizes. It supports intuition for asymptotic dominance. It is not a
    proof of Big-O, Big-Omega, or Big-Theta statements.

Run:
    python3 labs/week01/asymptotics_experiments.py
"""

from __future__ import annotations

import math


def growth_values(n: int) -> dict[str, float]:
    if n <= 0:
        raise ValueError("n must be positive")
    return {
        "log2 n": math.log2(n),
        "n": float(n),
        "n log2 n": n * math.log2(n),
        "n^2": float(n * n),
        "2^n": float(2**n),
    }


def format_row(n: int) -> str:
    values = growth_values(n)
    return (
        f"{n:>5} | "
        f"{values['log2 n']:>8.2f} | "
        f"{values['n']:>8.0f} | "
        f"{values['n log2 n']:>10.2f} | "
        f"{values['n^2']:>10.0f} | "
        f"{values['2^n']:>12.0f}"
    )


def ratio_tends_down_for_log_over_n(ns: list[int]) -> bool:
    ratios = [math.log2(n) / n for n in ns]
    return all(left > right for left, right in zip(ratios, ratios[1:]))


def main() -> None:
    sizes = [2, 4, 8, 16, 32, 64]
    print("This table is intuition only; asymptotic claims need definitions and proofs.")
    print("    n |   log2 n |        n |   n log2 n |        n^2 |          2^n")
    print("-" * 72)
    for n in sizes:
        print(format_row(n))

    assert growth_values(4)["n^2"] == 16.0
    assert growth_values(8)["2^n"] == 256.0
    assert ratio_tends_down_for_log_over_n([16, 32, 64, 128])


if __name__ == "__main__":
    main()

