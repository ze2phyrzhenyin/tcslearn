#!/usr/bin/env python3
"""Week 2 Days 5-6 lab: greedy versus dynamic programming examples.

Mathematical meaning: examples show why some greedy strategies need exchange
proofs and why DP needs state definitions. The program is not a proof.
"""

from __future__ import annotations

from typing import List, Tuple

Interval = Tuple[int, int]


def interval_scheduling(intervals: List[Interval]) -> List[Interval]:
    chosen: List[Interval] = []
    current_end = -10**18
    for start, finish in sorted(intervals, key=lambda item: item[1]):
        if start >= current_end:
            chosen.append((start, finish))
            current_end = finish
    return chosen


def coin_change_greedy(coins: List[int], amount: int) -> List[int]:
    result: List[int] = []
    for coin in sorted(coins, reverse=True):
        while amount >= coin:
            result.append(coin)
            amount -= coin
    if amount != 0:
        raise ValueError("amount not representable")
    return result


def lis_length(values: List[int]) -> int:
    if not values:
        return 0
    dp = [1] * len(values)
    for i in range(len(values)):
        for j in range(i):
            if values[j] < values[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def edit_distance(x: str, y: str) -> int:
    n, m = len(x), len(y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if x[i - 1] == y[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[n][m]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], value + dp[cap - weight])
    return dp[capacity]


def run_tests() -> None:
    assert interval_scheduling([(0, 3), (1, 2), (2, 4), (3, 5)]) == [(1, 2), (2, 4)]
    assert coin_change_greedy([1, 3, 4], 6) == [4, 1, 1]
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert edit_distance("kitten", "sitting") == 3
    assert knapsack_01([2, 3, 4], [4, 5, 7], 5) == 9


def main() -> None:
    run_tests()
    print("Week 2 Days 5-6: greedy and DP examples")
    print("Experiment is not a proof: greedy needs exchange proof; DP needs state induction.")
    print("coin greedy for coins [1,3,4], amount 6:", coin_change_greedy([1, 3, 4], 6))
    print("LIS length example:", lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print("edit distance kitten->sitting:", edit_distance("kitten", "sitting"))


if __name__ == "__main__":
    main()
