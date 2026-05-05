"""Probability simulations for Week 1 Day 5.

Mathematical meaning:
    This script simulates coin flips, balls into bins, and empirical mean
    concentration. The output can suggest why expectation and concentration
    statements are plausible. It cannot replace probability proofs.

Run:
    python3 labs/week01/probability_simulations.py
"""

from __future__ import annotations

import random
from statistics import mean, variance


def coin_flip_heads(trials: int, seed: int = 0) -> int:
    rng = random.Random(seed)
    return sum(1 for _ in range(trials) if rng.random() < 0.5)


def balls_into_bins(balls: int, bins: int, seed: int = 0) -> list[int]:
    if balls < 0 or bins <= 0:
        raise ValueError("balls must be nonnegative and bins must be positive")
    rng = random.Random(seed)
    loads = [0] * bins
    for _ in range(balls):
        loads[rng.randrange(bins)] += 1
    return loads


def empirical_means(samples: int, repetitions: int, seed: int = 0) -> list[float]:
    rng = random.Random(seed)
    means: list[float] = []
    for _ in range(repetitions):
        values = [1.0 if rng.random() < 0.5 else 0.0 for _ in range(samples)]
        means.append(mean(values))
    return means


def main() -> None:
    heads = coin_flip_heads(1000, seed=1)
    loads = balls_into_bins(1000, 20, seed=2)
    means_20 = empirical_means(20, 200, seed=3)
    means_200 = empirical_means(200, 200, seed=3)

    print("Simulation only; probability proofs require sample spaces and inequalities.")
    print(f"Coin flips: heads in 1000 fair flips = {heads}")
    print(f"Balls into bins: min load = {min(loads)}, max load = {max(loads)}")
    print(f"Empirical mean variance, sample size 20:  {variance(means_20):.5f}")
    print(f"Empirical mean variance, sample size 200: {variance(means_200):.5f}")

    assert 0 <= heads <= 1000
    assert sum(loads) == 1000
    assert len(loads) == 20
    assert all(0.0 <= value <= 1.0 for value in means_20)
    assert variance(means_200) < variance(means_20)


if __name__ == "__main__":
    main()

