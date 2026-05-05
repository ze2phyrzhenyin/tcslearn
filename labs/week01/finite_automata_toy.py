"""Finite automata toy examples for Week 1 Day 7.

Mathematical meaning:
    A deterministic finite automaton (DFA) is a finite-state model for
    recognizing some languages. These examples introduce the model; DFAs do
    not represent all possible computation.

Run:
    python3 labs/week01/finite_automata_toy.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


State = str
Symbol = str


@dataclass(frozen=True)
class DFA:
    alphabet: frozenset[Symbol]
    start: State
    accept: frozenset[State]
    transition: Callable[[State, Symbol], State]

    def accepts(self, word: str) -> bool:
        state = self.start
        for symbol in word:
            if symbol not in self.alphabet:
                raise ValueError(f"symbol {symbol!r} not in alphabet")
            state = self.transition(state, symbol)
        return state in self.accept


def even_number_of_ones_dfa() -> DFA:
    def delta(state: State, symbol: Symbol) -> State:
        if symbol == "0":
            return state
        return "odd" if state == "even" else "even"

    return DFA(
        alphabet=frozenset({"0", "1"}),
        start="even",
        accept=frozenset({"even"}),
        transition=delta,
    )


def ends_with_pattern_dfa(pattern: str) -> DFA:
    if not pattern:
        raise ValueError("pattern must be nonempty")
    alphabet = frozenset(set(pattern) | {"0", "1"})

    def longest_suffix_state(text: str) -> int:
        max_len = min(len(pattern), len(text))
        for length in range(max_len, -1, -1):
            if text.endswith(pattern[:length]):
                return length
        return 0

    def delta(state: State, symbol: Symbol) -> State:
        current = pattern[: int(state)] + symbol
        return str(longest_suffix_state(current))

    return DFA(
        alphabet=alphabet,
        start="0",
        accept=frozenset({str(len(pattern))}),
        transition=delta,
    )


def main() -> None:
    even_ones = even_number_of_ones_dfa()
    ends_101 = ends_with_pattern_dfa("101")

    print("DFA examples. A DFA is finite-state; it is not a model of all computation.")
    print(f"Even number of ones accepts '1010'? {even_ones.accepts('1010')}")
    print(f"Ends with 101 accepts '00101'? {ends_101.accepts('00101')}")

    assert even_ones.accepts("")
    assert even_ones.accepts("11")
    assert not even_ones.accepts("1")
    assert even_ones.accepts("1010")
    assert ends_101.accepts("101")
    assert ends_101.accepts("00101")
    assert not ends_101.accepts("1010")
    assert not ends_101.accepts("10")


if __name__ == "__main__":
    main()

