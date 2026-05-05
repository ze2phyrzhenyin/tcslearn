"""Lab: {{lab_title}}

Purpose:
    {{what_intuition_this_lab_tests}}

Important:
    This experiment supports intuition. It is not a proof.

Run:
    python {{path}}
"""

from __future__ import annotations

import random


def experiment(seed: int = 0) -> dict[str, float]:
    """Run a small deterministic experiment using a fixed seed."""
    rng = random.Random(seed)
    trials = 100
    successes = 0
    for _ in range(trials):
        value = rng.random()
        if value < 0.5:
            successes += 1
    return {"trials": float(trials), "success_rate": successes / trials}


def main() -> None:
    result = experiment(seed=0)
    print(result)
    assert result["trials"] == 100.0
    assert 0.0 <= result["success_rate"] <= 1.0


if __name__ == "__main__":
    main()

