#!/usr/bin/env python3
"""Week 2 Day 7 lab: randomized algorithms.

Mathematical meaning: fixed-seed simulations expose random variables and bad
 events. They do not prove expected time or failure-probability bounds.
"""

from __future__ import annotations

import random
from collections import Counter
from typing import List


def randomized_quicksort(values: List[int], rng: random.Random) -> List[int]:
    if len(values) <= 1:
        return values[:]
    pivot = rng.choice(values)
    lows = [x for x in values if x < pivot]
    equals = [x for x in values if x == pivot]
    highs = [x for x in values if x > pivot]
    return randomized_quicksort(lows, rng) + equals + randomized_quicksort(highs, rng)


def randomized_quickselect(values: List[int], k: int, rng: random.Random) -> int:
    if not 0 <= k < len(values):
        raise ValueError("k out of range")
    arr = values[:]
    while True:
        pivot = rng.choice(arr)
        lows = [x for x in arr if x < pivot]
        equals = [x for x in arr if x == pivot]
        highs = [x for x in arr if x > pivot]
        if k < len(lows):
            arr = lows
        elif k < len(lows) + len(equals):
            return pivot
        else:
            k -= len(lows) + len(equals)
            arr = highs


def monte_carlo_majority_contains(values: List[int], candidate: int, trials: int, rng: random.Random) -> bool:
    """Accepts if candidate is seen in sampled positions; can falsely reject."""
    if not values:
        return False
    for _ in range(trials):
        if values[rng.randrange(len(values))] == candidate:
            return True
    return False


def amplification_failure_rate(values: List[int], candidate: int, trials: int, repetitions: int) -> float:
    failures = 0
    for seed in range(repetitions):
        rng = random.Random(seed)
        if not monte_carlo_majority_contains(values, candidate, trials, rng):
            failures += 1
    return failures / repetitions


def run_tests() -> None:
    data = [5, 1, 4, 2, 3, 3]
    assert randomized_quicksort(data, random.Random(0)) == sorted(data)
    assert randomized_quickselect(data, 0, random.Random(1)) == 1
    assert randomized_quickselect(data, 3, random.Random(1)) == sorted(data)[3]
    majority = [1] * 7 + [0] * 3
    assert amplification_failure_rate(majority, 1, 10, 50) < 0.1


def main() -> None:
    run_tests()
    print("Week 2 Day 7: randomized algorithms")
    print("Experiment is not a proof: define sample space and bad events.")
    data = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print("randomized quicksort:", randomized_quicksort(data, random.Random(42)))
    majority = [1] * 6 + [0] * 4
    for trials in [1, 2, 4, 8]:
        rate = amplification_failure_rate(majority, 1, trials, 200)
        print(f"toy failure rate over 200 seeds with trials={trials}: {rate:.3f}")


if __name__ == "__main__":
    main()
