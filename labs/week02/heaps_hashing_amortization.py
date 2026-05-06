#!/usr/bin/env python3
"""Week 2 Day 3 lab: heaps, hashing, and amortized analysis.

Mathematical meaning: asserts check representation invariants on examples.
They do not prove heap operation correctness, expected hashing bounds, or
amortized dynamic-array bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional


class MinHeap:
    def __init__(self) -> None:
        self.data: List[int] = []

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def push(self, x: int) -> None:
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0 and self.data[self._parent(i)] > self.data[i]:
            p = self._parent(i)
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p

    def pop_min(self) -> int:
        if not self.data:
            raise IndexError("empty heap")
        result = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return result

    def _sift_down(self, i: int) -> None:
        n = len(self.data)
        while True:
            left = self._left(i)
            right = left + 1
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                return
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def is_heap(self) -> bool:
        return all(self.data[(i - 1) // 2] <= self.data[i] for i in range(1, len(self.data)))


class ChainedHashTable:
    def __init__(self, buckets: int = 8) -> None:
        self.buckets: List[list[tuple[str, Any]]] = [[] for _ in range(buckets)]

    def _index(self, key: str) -> int:
        return sum(ord(ch) for ch in key) % len(self.buckets)

    def set(self, key: str, value: Any) -> None:
        bucket = self.buckets[self._index(key)]
        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str) -> Optional[Any]:
        for old_key, value in self.buckets[self._index(key)]:
            if old_key == key:
                return value
        return None

    def load_factor(self) -> float:
        items = sum(len(bucket) for bucket in self.buckets)
        return items / len(self.buckets)


@dataclass
class DynamicArrayStats:
    appends: int
    copies: int
    final_capacity: int


def simulate_dynamic_array(appends: int) -> DynamicArrayStats:
    capacity = 0
    size = 0
    copies = 0
    for _ in range(appends):
        if size == capacity:
            new_capacity = 1 if capacity == 0 else 2 * capacity
            copies += size
            capacity = new_capacity
        size += 1
    return DynamicArrayStats(appends, copies, capacity)


def run_tests() -> None:
    heap = MinHeap()
    for x in [5, 3, 7, 1, 4]:
        heap.push(x)
        assert heap.is_heap()
    assert [heap.pop_min() for _ in range(5)] == [1, 3, 4, 5, 7]
    table = ChainedHashTable(4)
    table.set("ab", 1)
    table.set("ba", 2)  # deliberate collision under this toy hash
    assert table.get("ab") == 1
    assert table.get("ba") == 2
    assert table.get("missing") is None
    stats = simulate_dynamic_array(17)
    assert stats.copies < 2 * stats.appends


def main() -> None:
    run_tests()
    print("Week 2 Day 3: heaps, hashing, amortization")
    print("Experiment is not a proof: invariants and assumptions still need proofs.")
    for m in [1, 2, 4, 8, 16, 32, 64]:
        stats = simulate_dynamic_array(m)
        print(f"appends={m:2d}, copies={stats.copies:3d}, final_capacity={stats.final_capacity:3d}")


if __name__ == "__main__":
    main()
