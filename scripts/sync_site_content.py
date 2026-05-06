#!/usr/bin/env python3
"""Sync repository learning materials into the Astro/Starlight site.

The source of truth remains in notes/, exercises/, labs/, review/, resources/,
and state/. This script generates browser-readable MDX pages without requiring
third-party Python packages.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "site" / "src" / "content" / "docs"

SOURCE_NOTE = (
    "This page is generated from repository learning materials. "
    "Edit the source file, not this generated page."
)

HAND_MAINTAINED = {
    "index.mdx",
    "start-here.mdx",
    "learning-system/overview.mdx",
    "learning-system/daily-workflow.mdx",
    "learning-system/weekly-workflow.mdx",
    "learning-system/how-to-use-codex.mdx",
    "labs/overview.mdx",
}

DAY_PAGES = [
    {
        "day": "Day 1",
        "slug": "day01",
        "title": "Logic, Sets, Functions",
        "source": "notes/week01/day01-logic-sets-functions.md",
        "exercise": "/exercises/week01-problem-set/#day-1-logic-sets-functions-relations",
        "hardest": "Quantifier order, converse versus contrapositive, and set equality proofs.",
        "output": "Definitions, proof templates, and Day 1 exercises.",
    },
    {
        "day": "Day 2",
        "slug": "day02",
        "title": "Induction and Invariants",
        "source": "notes/week01/day02-induction-recursion-invariants.md",
        "exercise": "/exercises/week01-problem-set/#day-2-induction-recursion-invariants",
        "hardest": "Writing the induction hypothesis and choosing an invariant strong enough for termination.",
        "output": "Induction proofs and invariant arguments.",
    },
    {
        "day": "Day 3",
        "slug": "day03",
        "title": "Asymptotics and Recurrences",
        "source": "notes/week01/day03-asymptotics-recurrences-algorithm-analysis.md",
        "exercise": "/exercises/week01-problem-set/#day-3-asymptotics-recurrences-algorithm-analysis",
        "hardest": "Separating upper bounds, lower bounds, and variables tending to infinity.",
        "output": "Asymptotic proofs, recurrence solutions, and two labs.",
    },
    {
        "day": "Day 4",
        "slug": "day04",
        "title": "Counting and Graphs",
        "source": "notes/week01/day04-counting-discrete-structures-graphs.md",
        "exercise": "/exercises/week01-problem-set/#day-4-counting-discrete-structures-graphs",
        "hardest": "Avoiding double-counting and proving tree properties from definitions.",
        "output": "Counting exercises and graph modeling.",
    },
    {
        "day": "Day 5",
        "slug": "day05",
        "title": "Probability",
        "source": "notes/week01/day05-probability-random-variables-concentration.md",
        "exercise": "/exercises/week01-problem-set/#day-5-probability-random-variables-concentration",
        "hardest": "Defining sample spaces and distinguishing independence from disjointness.",
        "output": "Probability exercises and simulation lab.",
    },
    {
        "day": "Day 6",
        "slug": "day06",
        "title": "Linear Algebra and Convexity",
        "source": "notes/week01/day06-linear-algebra-convexity-for-tcs.md",
        "exercise": "/exercises/week01-problem-set/#day-6-linear-algebra-and-convexity",
        "hardest": "Using norm and convexity definitions rather than geometric intuition alone.",
        "output": "Geometry exercises for learning theory preparation.",
    },
    {
        "day": "Day 7",
        "slug": "day07",
        "title": "Models and Reductions",
        "source": "notes/week01/day07-models-reductions-synthesis.md",
        "exercise": "/exercises/week01-problem-set/#day-7-models-languages-reductions",
        "hardest": "Separating problem, algorithm, language, encoding, and reduction direction.",
        "output": "Formalization exercises and DFA lab.",
    },
]

LAB_PAGES = [
    {
        "slug": "week01-asymptotics",
        "title": "Week 1 Lab: Asymptotics",
        "source": "labs/week01/asymptotics_experiments.py",
        "concept": "Growth-rate comparison for asymptotic intuition.",
        "command": "python3 labs/week01/asymptotics_experiments.py",
        "expected": "A text table comparing log n, n, n log n, n^2, and 2^n.",
    },
    {
        "slug": "week01-recurrence",
        "title": "Week 1 Lab: Recurrences",
        "source": "labs/week01/recurrence_solver_sandbox.py",
        "concept": "Numerical expansion of simple divide-and-conquer recurrences.",
        "command": "python3 labs/week01/recurrence_solver_sandbox.py",
        "expected": "A text table of recurrence values and normalized ratios.",
    },
    {
        "slug": "week01-probability",
        "title": "Week 1 Lab: Probability",
        "source": "labs/week01/probability_simulations.py",
        "concept": "Coin flips, balls into bins, and empirical mean concentration.",
        "command": "python3 labs/week01/probability_simulations.py",
        "expected": "A deterministic simulation summary using fixed seeds.",
    },
    {
        "slug": "week01-automata",
        "title": "Week 1 Lab: Automata",
        "source": "labs/week01/finite_automata_toy.py",
        "concept": "Simple deterministic finite automata for language recognition.",
        "command": "python3 labs/week01/finite_automata_toy.py",
        "expected": "Acceptance checks for parity and suffix-pattern DFAs.",
    },
]

WEEK2_DAY_PAGES = [
    {
        "day": "Day 1",
        "slug": "day01",
        "title": "Specifications, Sorting, Lower Bounds",
        "source": "notes/week02/day01-specifications-sorting-lower-bounds.md",
        "exercise": "/exercises/week02-problem-set/#day-1-algorithm-specifications-sorting-and-comparison-lower-bounds",
        "hardest": "Separating problem specification from algorithm and proving the comparison sorting lower bound.",
        "output": "Sorting specification, insertion-sort invariant, merge-sort recurrence, and lower-bound proof.",
    },
    {
        "day": "Day 2",
        "slug": "day02",
        "title": "Divide and Conquer, Selection",
        "source": "notes/week02/day02-divide-and-conquer-selection.md",
        "exercise": "/exercises/week02-problem-set/#day-2-divide-and-conquer-recurrence-proofs-and-selection",
        "hardest": "Recursive correctness proofs and expected versus worst-case quickselect analysis.",
        "output": "Binary search, merge sort, quickselect, recurrences, and divide-and-conquer lab.",
    },
    {
        "day": "Day 3",
        "slug": "day03",
        "title": "Data Structures and Amortization",
        "source": "notes/week02/day03-data-structures-heaps-hashing-amortization.md",
        "exercise": "/exercises/week02-problem-set/#day-3-data-structures-heaps-hashing-and-amortized-analysis",
        "hardest": "Keeping interface, representation invariant, expected time, and amortized time separate.",
        "output": "Heap, hashing, and dynamic-array amortization proof practice.",
    },
    {
        "day": "Day 4",
        "slug": "day04",
        "title": "Graph Algorithms",
        "source": "notes/week02/day04-graph-algorithms-bfs-dfs-shortest-paths.md",
        "exercise": "/exercises/week02-problem-set/#day-4-graph-algorithms-i-bfs-dfs-shortest-paths",
        "hardest": "BFS shortest-path invariant and graph representation complexity.",
        "output": "BFS, DFS, components, topological order, and graph lab.",
    },
    {
        "day": "Day 5",
        "slug": "day05",
        "title": "Greedy Algorithms",
        "source": "notes/week02/day05-greedy-algorithms-exchange-arguments.md",
        "exercise": "/exercises/week02-problem-set/#day-5-greedy-algorithms-and-exchange-arguments",
        "hardest": "Writing exchange arguments instead of relying on local-choice intuition.",
        "output": "Interval scheduling proof, fractional knapsack, coin-change counterexamples, and MST intuition.",
    },
    {
        "day": "Day 6",
        "slug": "day06",
        "title": "Dynamic Programming",
        "source": "notes/week02/day06-dynamic-programming-optimal-substructure.md",
        "exercise": "/exercises/week02-problem-set/#day-6-dynamic-programming-and-optimal-substructure",
        "hardest": "Choosing state definitions and proving recurrences by induction over state order.",
        "output": "LIS, edit distance, knapsack, reconstruction, and greedy-versus-DP lab.",
    },
    {
        "day": "Day 7",
        "slug": "day07",
        "title": "Randomized Algorithms",
        "source": "notes/week02/day07-randomized-algorithms-synthesis.md",
        "exercise": "/exercises/week02-problem-set/#day-7-randomized-algorithms-and-synthesis",
        "hardest": "Sample spaces, expected running time, failure probability, and amplification.",
        "output": "Randomized quicksort/quickselect, Monte Carlo toy tests, amplification, and proof synthesis.",
    },
]

WEEK2_LAB_PAGES = [
    {
        "slug": "week02-sorting",
        "title": "Week 2 Lab: Sorting and Lower Bounds",
        "source": "labs/week02/sorting_and_lower_bounds.py",
        "concept": "Growth rates and decision-tree lower-bound intuition for comparison sorting.",
        "command": "python3 labs/week02/sorting_and_lower_bounds.py",
        "expected": "A text table comparing n log n, n^2, and log2(n!).",
    },
    {
        "slug": "week02-divide-and-conquer",
        "title": "Week 2 Lab: Divide and Conquer",
        "source": "labs/week02/divide_and_conquer_sandbox.py",
        "concept": "Binary search, merge sort, quickselect, and recurrence expansion examples.",
        "command": "python3 labs/week02/divide_and_conquer_sandbox.py",
        "expected": "Text output for recurrence values and a quickselect median.",
    },
    {
        "slug": "week02-data-structures",
        "title": "Week 2 Lab: Data Structures",
        "source": "labs/week02/heaps_hashing_amortization.py",
        "concept": "Heap invariants, chained hash table collisions, and dynamic-array resize costs.",
        "command": "python3 labs/week02/heaps_hashing_amortization.py",
        "expected": "Assertions plus dynamic-array copy counts.",
    },
    {
        "slug": "week02-graphs",
        "title": "Week 2 Lab: Graph Algorithms",
        "source": "labs/week02/graph_algorithms.py",
        "concept": "BFS, DFS, connected components, unweighted shortest paths, and topological sort.",
        "command": "python3 labs/week02/graph_algorithms.py",
        "expected": "BFS distance and DFS order summaries.",
    },
    {
        "slug": "week02-greedy-dp",
        "title": "Week 2 Lab: Greedy and DP",
        "source": "labs/week02/greedy_vs_dp_examples.py",
        "concept": "Greedy successes, greedy counterexamples, and dynamic-programming examples.",
        "command": "python3 labs/week02/greedy_vs_dp_examples.py",
        "expected": "Coin-change counterexample, LIS length, and edit distance output.",
    },
    {
        "slug": "week02-randomized",
        "title": "Week 2 Lab: Randomized Algorithms",
        "source": "labs/week02/randomized_algorithms.py",
        "concept": "Randomized quicksort, quickselect, Monte Carlo failure, and amplification simulation.",
        "command": "python3 labs/week02/randomized_algorithms.py",
        "expected": "Sorted output and toy failure-rate statistics.",
    },
]


def quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def frontmatter(title: str, description: str) -> str:
    return f'---\ntitle: "{quote(title)}"\ndescription: "{quote(description)}"\n---\n\n'


def generated_notice(source: str) -> str:
    return (
        f'> **Generated page.** {SOURCE_NOTE}\n'
        f'>\n'
        f'> Source: `{source}`\n\n'
    )


def sanitize_mdx(text: str) -> str:
    """Escape characters that MDX treats as JSX/expression syntax in prose."""
    out: list[str] = []
    in_fence = False
    in_display_math = False

    def escape_prose_with_inline_math(line: str) -> str:
        result: list[str] = []
        index = 0
        while index < len(line):
            start = line.find("\\(", index)
            if start == -1:
                result.append(line[index:].replace("{", "\\{").replace("}", "\\}").replace("<", "&lt;"))
                break
            result.append(line[index:start].replace("{", "\\{").replace("}", "\\}").replace("<", "&lt;"))
            end = line.find("\\)", start + 2)
            if end == -1:
                result.append(line[start:].replace("{", "\\{").replace("}", "\\}").replace("<", "&lt;"))
                break
            result.append("$" + line[start + 2 : end] + "$")
            index = end + 2
        return "".join(result)

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if line.strip() == "\\[":
            in_display_math = True
            out.append("$$")
            continue
        if line.strip() == "\\]":
            in_display_math = False
            out.append("$$")
            continue
        if in_display_math:
            out.append(line)
            continue
        if line.startswith(">"):
            out.append(escape_prose_with_inline_math(line))
            continue
        out.append(escape_prose_with_inline_math(line))
    return "\n".join(out).strip() + "\n"


def write_generated(rel_path: str, title: str, description: str, body: str, source: str, report: dict[str, list[str]]) -> None:
    if rel_path in HAND_MAINTAINED:
        report["skipped"].append(rel_path)
        return
    target = DOCS / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    content = frontmatter(title, description) + generated_notice(source) + body.rstrip() + "\n"
    old = target.read_text(encoding="utf-8") if target.exists() else None
    if old == content:
        report["skipped"].append(rel_path)
        return
    target.write_text(content, encoding="utf-8")
    report["modified"].append(rel_path) if old is not None else report["generated"].append(rel_path)


def read_or_placeholder(path: Path, label: str) -> str:
    if path.exists():
        return sanitize_mdx(path.read_text(encoding="utf-8"))
    return (
        f'<div class="generated-note">\n\n'
        f'Content source not found yet. Generate Week 1 content first.\n\n'
        f'Missing source: `{label}`\n\n'
        f'</div>\n'
    )


def strip_tex_document(text: str) -> str:
    if "\\begin{document}" in text:
        text = text.split("\\begin{document}", 1)[1]
    if "\\end{document}" in text:
        text = text.split("\\end{document}", 1)[0]
    return text


def convert_tex_inline(line: str) -> str:
    line = line.strip()
    replacements = {
        "\\maketitle": "",
        "\\section*": "\\section",
        "\\begin{enumerate}": "",
        "\\end{enumerate}": "",
        "\\begin{itemize}": "",
        "\\end{itemize}": "",
    }
    for old, new in replacements.items():
        line = line.replace(old, new)
    line = re.sub(r"\\section\{([^}]*)\}", r"## \1", line)
    line = re.sub(r"\\subsection\*\{([^}]*)\}", r"### \1", line)
    line = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", line)
    line = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", line)
    line = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", line)
    line = line.replace("\\[", "$$").replace("\\]", "$$")
    line = line.replace("\\(", "$").replace("\\)", "$")
    return line


def tex_to_mdx(path: Path) -> str:
    if not path.exists():
        return read_or_placeholder(path, str(path.relative_to(ROOT)))
    text = strip_tex_document(path.read_text(encoding="utf-8"))
    lines: list[str] = []
    item_count = 0
    in_display = False
    for raw in text.splitlines():
        line = convert_tex_inline(raw)
        if not line:
            continue
        if line == "$$":
            in_display = not in_display
            lines.append("$$")
            continue
        if line.startswith("\\item"):
            item_count += 1
            line = line.replace("\\item", "", 1).strip()
            difficulty = re.match(r"\*\*(Basic|Medium|Challenge|Hard)\. Concepts: ([^*]+)\.\*\*\s*(.*)", line)
            if difficulty:
                level, concepts, rest = difficulty.groups()
                lines.append(f"### Problem {item_count}")
                lines.append("")
                lines.append(f"**Difficulty:** {level}")
                lines.append("")
                lines.append(f"**Concepts:** {concepts}")
                lines.append("")
                lines.append(rest)
                continue
            solution = re.match(r"\*\*Strategy\.\*\*\s*(.*)", line)
            if solution:
                lines.append(f"### Solution {item_count}")
                lines.append("")
                lines.append(f"**Strategy.** {solution.group(1)}")
                continue
            lines.append(f"### Item {item_count}")
            lines.append("")
            lines.append(line)
            continue
        if line.startswith("\\title") or line.startswith("\\author") or line.startswith("\\date"):
            continue
        lines.append(line)
    return sanitize_mdx("\n".join(lines).replace("\\_", "_"))


def parse_source_blocks(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    sources: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    list_key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or raw.strip() == "sources:":
            continue
        if raw.startswith("  - source_id:"):
            if current:
                sources.append(current)
            current = {"source_id": raw.split(":", 1)[1].strip().strip('"')}
            list_key = None
            continue
        if current is None:
            continue
        stripped = raw.strip()
        if stripped.startswith("- ") and list_key:
            current.setdefault(list_key, [])
            assert isinstance(current[list_key], list)
            current[list_key].append(stripped[2:].strip().strip('"'))
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            value = value.strip()
            if value:
                current[key] = value.strip('"')
                list_key = None
            else:
                current[key] = []
                list_key = key
    if current:
        sources.append(current)
    return sources


def resources_mdx() -> str:
    sources = parse_source_blocks(ROOT / "resources" / "sources.yaml")
    if not sources:
        return "No resources are indexed yet.\n"
    parts = ["## Vetted Sources", ""]
    for source in sources:
        title = str(source.get("title", "Untitled"))
        url = str(source.get("url", ""))
        parts.append(f"### {title}")
        parts.append("")
        parts.append(f"- **Author or organization:** {source.get('author_or_organization', 'Not specified')}")
        parts.append(f"- **Type:** {source.get('type', 'Not specified')}")
        parts.append(f"- **Access status:** {source.get('access_status', 'Not specified')}")
        topics = source.get("topics", [])
        if isinstance(topics, list):
            parts.append(f"- **Topics:** {', '.join(str(item) for item in topics)}")
        days = source.get("used_for_days", [])
        if isinstance(days, list):
            parts.append(f"- **Used for days:** {', '.join(str(item) for item in days)}")
        parts.append(f"- **Legal access note:** {source.get('legal_access_note', 'Not specified')}")
        if url:
            parts.append(f"- **URL:** [{url}]({url})")
        parts.append("")
    return "\n".join(parts)


def progress_mdx() -> str:
    progress = ROOT / "state" / "progress.yaml"
    next_actions = ROOT / "state" / "next_actions.md"
    progress_text = progress.read_text(encoding="utf-8") if progress.exists() else "Missing progress.yaml"
    next_text = next_actions.read_text(encoding="utf-8") if next_actions.exists() else "Missing next_actions.md"
    current = re.search(r'current_week:\s*"([^"]*)"', progress_text)
    phase = re.search(r'current_phase:\s*"([^"]*)"', progress_text)
    target = re.search(r'next_target:\s*"([^"]*)"', progress_text)
    parts = [
        "## Current Status",
        "",
        f"- **Current week:** {current.group(1) if current else 'Not set'}",
        f"- **Current phase:** {phase.group(1) if phase else 'Not set'}",
        "- **Content generation completed:** Week 1, Week 2",
        "- **Study completed:** None recorded yet",
        "- **Pending:** Study Week 2 Day 1 and record sorting-specification, invariant, lower-bound, and recurrence mistakes",
        "- **Weak areas:** Quantifiers, proof rigor, induction, probability sample spaces, asymptotic variables, algorithm specification, loop invariants, lower-bound models",
        f"- **Next target:** {target.group(1) if target else 'Not set'}",
        "",
        "## Raw Progress",
        "",
        "```yaml",
        progress_text.strip(),
        "```",
        "",
        "## Next Actions",
        "",
        sanitize_mdx(next_text),
    ]
    return "\n".join(parts)


def flashcards_mdx(path: Path) -> str:
    if not path.exists():
        return read_or_placeholder(path, str(path.relative_to(ROOT)))
    cards: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("Q:"):
            if current:
                cards.append(current)
            current = {"q": line[2:].strip(), "a": "", "tag": ""}
        elif line.startswith("A:"):
            current["a"] = line[2:].strip()
        elif line.startswith("Tag:"):
            current["tag"] = line[4:].strip()
    if current:
        cards.append(current)
    parts = ["## Flashcards", ""]
    for card in cards:
        parts.append('<div class="qa-card">')
        parts.append("")
        parts.append(f"**Q:** {sanitize_mdx(card.get('q', '')).strip()}")
        parts.append("")
        parts.append(f"**A:** {sanitize_mdx(card.get('a', '')).strip()}")
        parts.append("")
        parts.append(f"**Tag:** `{card.get('tag', '')}`")
        parts.append("")
        parts.append("</div>")
        parts.append("")
    return "\n".join(parts)


def grouped_mistakes_mdx(path: Path) -> str:
    if not path.exists():
        return read_or_placeholder(path, str(path.relative_to(ROOT)))
    items = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"(\d+)\.\s+(.*)", raw.strip())
        if match:
            items.append((int(match.group(1)), match.group(2)))
    groups = {
        "logic": range(1, 14),
        "proof": range(14, 15),
        "induction": range(15, 23),
        "asymptotics": range(23, 30),
        "probability": range(36, 43),
        "models": range(47, 49),
        "reductions": range(49, 51),
    }
    parts = [
        '<div class="mistake-callout">',
        "",
        "Use this page as an error log map. After exercises, copy the relevant mistake type into `state/mistakes_log.md` and add a repair exercise.",
        "",
        "</div>",
        "",
    ]
    for label, nums in groups.items():
        parts.append(f"## {label.replace('_', ' ').title()}")
        parts.append("")
        for num, text in items:
            if num in nums:
                parts.append(f"{num}. {sanitize_mdx(text).strip()}")
        parts.append("")
    parts.append("## Other Week 1 Mistakes")
    parts.append("")
    covered = {n for nums in groups.values() for n in nums}
    for num, text in items:
        if num not in covered:
            parts.append(f"{num}. {sanitize_mdx(text).strip()}")
    return "\n".join(parts)


def lab_mdx(lab: dict[str, str]) -> str:
    source_path = ROOT / lab["source"]
    code = source_path.read_text(encoding="utf-8") if source_path.exists() else "# Content source not found yet."
    return f"""<div class="lab-callout">
This lab supports intuition. It is not a proof.
</div>

## Purpose

{lab["concept"]}

## Mathematical Concept

The lab gives concrete outputs that can suggest a pattern. The corresponding theorem still needs definitions and proof.

## Command to Run

```bash
{lab["command"]}
```

## Expected Output

{lab["expected"]}

## Code

```python
{code.rstrip()}
```

## Interpretation

After running the lab, write one sentence of the form: "This experiment suggests ..., but it does not prove ...".

## Limitations

The program checks examples and assertions. It does not prove an asymptotic bound, probability inequality, or language-recognition theorem.

## Extension Exercises

1. Change one input size or seed and rerun.
2. Predict the output before running.
3. State a theorem that would explain the observed behavior.
"""


def week_overview_mdx() -> str:
    parts = [
        "## Week Title",
        "",
        "Mathematical and Conceptual Foundations for Theoretical Computer Science",
        "",
        "## Purpose",
        "",
        "建立 TCS 自学的基础语言：精确定义、证明结构、算法分析、离散结构、概率、几何直觉和形式化模型。",
        "",
        "## Prerequisites",
        "",
        "- Basic algebra",
        "- Basic Python reading ability",
        "- Willingness to write definitions and proofs carefully",
        "",
        "## 7-Day Learning Path",
        "",
    ]
    for day in DAY_PAGES:
        parts.extend(
            [
                f"### [{day['day']}: {day['title']}](/week01/{day['slug']}/)",
                "",
                f"- **Goal:** {day['output']}",
                f"- **Hardest point:** {day['hardest']}",
                f"- **Output:** {day['output']}",
                f"- **Exercises:** [Problem set section]({day['exercise']})",
                "",
            ]
        )
    parts.extend(
        [
            "## Labs",
            "",
            "- [Asymptotics](/labs/week01-asymptotics/)",
            "- [Recurrences](/labs/week01-recurrence/)",
            "- [Probability](/labs/week01-probability/)",
            "- [Automata](/labs/week01-automata/)",
            "",
            "## Review Checklist",
            "",
            "- Can I state definitions without looking?",
            "- Can I write a proof strategy before proof details?",
            "- Can I separate correctness from running time?",
            "- Can I define the sample space before probability calculations?",
            "- Can I distinguish problem, algorithm, language, and reduction?",
        ]
    )
    return "\n".join(parts)


def week2_overview_mdx() -> str:
    parts = [
        "## Week Title",
        "",
        "Algorithmic Thinking, Data Structures, and Proof Patterns",
        "",
        "## Purpose",
        "",
        "建立理论计算机科学视角下的算法基础：formal specification、correctness proof、worst-case/expected/amortized analysis、algorithmic paradigms，以及后续 string algorithms、learning theory、randomized algorithms 和 complexity theory 需要的证明模式。",
        "",
        "## Prerequisites",
        "",
        "- Week 1 definitions, induction, loop invariants, graphs, probability, and asymptotics.",
        "- Basic Python ability for small labs.",
        "- Willingness to write specifications before algorithms.",
        "",
        "## 7-Day Learning Path",
        "",
    ]
    for day in WEEK2_DAY_PAGES:
        parts.extend(
            [
                f"### [{day['day']}: {day['title']}](/week02/{day['slug']}/)",
                "",
                f"- **Goal:** {day['output']}",
                f"- **Hardest point:** {day['hardest']}",
                f"- **Output:** {day['output']}",
                f"- **Exercises:** [Problem set section]({day['exercise']})",
                "",
            ]
        )
    parts.extend(
        [
            "## Labs",
            "",
            "- [Sorting and Lower Bounds](/labs/week02-sorting/)",
            "- [Divide and Conquer](/labs/week02-divide-and-conquer/)",
            "- [Data Structures](/labs/week02-data-structures/)",
            "- [Graph Algorithms](/labs/week02-graphs/)",
            "- [Greedy and DP](/labs/week02-greedy-dp/)",
            "- [Randomized Algorithms](/labs/week02-randomized/)",
            "",
            "## Review Checklist",
            "",
            "- Can I write a problem specification before an algorithm?",
            "- Can I choose the right proof pattern for correctness?",
            "- Can I separate worst-case, expected, and amortized claims?",
            "- Can I state model assumptions for lower bounds and randomized algorithms?",
            "- Can I explain why a lab result is not a proof?",
        ]
    )
    return "\n".join(parts)


def sync(report: dict[str, list[str]]) -> None:
    write_generated(
        "week01/overview.mdx",
        "Week 1 Overview",
        "Seven-day path for mathematical and conceptual TCS foundations.",
        week_overview_mdx(),
        "curriculum/weeks/week01-foundations.yaml",
        report,
    )

    for index, day in enumerate(DAY_PAGES):
        source = ROOT / day["source"]
        body = read_or_placeholder(source, day["source"])
        prev_link = "/start-here/" if index == 0 else f"/week01/{DAY_PAGES[index - 1]['slug']}/"
        next_link = "/review/week01-review/" if index == len(DAY_PAGES) - 1 else f"/week01/{DAY_PAGES[index + 1]['slug']}/"
        body += f"""

## Page Navigation

<div class="page-nav-grid">
  <a class="button-link" href="{prev_link}">Previous</a>
  <a class="button-link" href="{next_link}">Next</a>
  <a class="button-link" href="/review/week01-review/">Review</a>
  <a class="button-link" href="/exercises/week01-problem-set/">Exercises</a>
</div>
"""
        write_generated(
            f"week01/{day['slug']}.mdx",
            f"{day['day']}: {day['title']}",
            f"Week 1 {day['day']} study note.",
            body,
            day["source"],
            report,
        )

    write_generated(
        "exercises/week01-problem-set.mdx",
        "Week 1 Problem Set",
        "Browser-readable Week 1 problem set without solutions.",
        tex_to_mdx(ROOT / "exercises/week01/week01_problem_set.tex"),
        "exercises/week01/week01_problem_set.tex",
        report,
    )
    write_generated(
        "exercises/week01-solutions.mdx",
        "Week 1 Solutions",
        "Browser-readable Week 1 solutions with proof strategies and common mistakes.",
        tex_to_mdx(ROOT / "exercises/week01/week01_solutions.tex"),
        "exercises/week01/week01_solutions.tex",
        report,
    )

    for lab in LAB_PAGES:
        write_generated(
            f"labs/{lab['slug']}.mdx",
            lab["title"],
            lab["concept"],
            lab_mdx(lab),
            lab["source"],
            report,
        )

    review_pages = [
        ("review/week01-review.mdx", "Week 1 Review", "Weekly review and repair checklist.", "review/week01/week01_review.md"),
        ("review/glossary.mdx", "Glossary", "Week 1 glossary.", "review/week01/glossary_week01.md"),
    ]
    for rel, title, desc, source in review_pages:
        write_generated(rel, title, desc, read_or_placeholder(ROOT / source, source), source, report)
    write_generated(
        "review/flashcards.mdx",
        "Flashcards",
        "Week 1 flashcards in Q/A format.",
        flashcards_mdx(ROOT / "review/week01/flashcards_week01.md"),
        "review/week01/flashcards_week01.md",
        report,
    )
    write_generated(
        "review/mistakes-to-watch.mdx",
        "Mistakes to Watch",
        "Week 1 mistakes grouped by topic.",
        grouped_mistakes_mdx(ROOT / "review/week01/mistakes_to_watch.md"),
        "review/week01/mistakes_to_watch.md",
        report,
    )

    write_generated(
        "week02/overview.mdx",
        "Week 2 Overview",
        "Seven-day path for algorithmic thinking, data structures, and proof patterns.",
        week2_overview_mdx(),
        "curriculum/weeks/week02-algorithms-foundations.yaml",
        report,
    )

    for index, day in enumerate(WEEK2_DAY_PAGES):
        source = ROOT / day["source"]
        body = read_or_placeholder(source, day["source"]).replace(
            "Generate Week 1 content first.", "Generate Week 2 content first."
        )
        prev_link = "/week02/overview/" if index == 0 else f"/week02/{WEEK2_DAY_PAGES[index - 1]['slug']}/"
        next_link = "/review/week02-review/" if index == len(WEEK2_DAY_PAGES) - 1 else f"/week02/{WEEK2_DAY_PAGES[index + 1]['slug']}/"
        body += f"""

## Page Navigation

<div class="page-nav-grid">
  <a class="button-link" href="{prev_link}">Previous</a>
  <a class="button-link" href="{next_link}">Next</a>
  <a class="button-link" href="/review/week02-review/">Review</a>
  <a class="button-link" href="/exercises/week02-problem-set/">Exercises</a>
</div>
"""
        write_generated(
            f"week02/{day['slug']}.mdx",
            f"{day['day']}: {day['title']}",
            f"Week 2 {day['day']} study note.",
            body,
            day["source"],
            report,
        )

    write_generated(
        "exercises/week02-problem-set.mdx",
        "Week 2 Problem Set",
        "Browser-readable Week 2 problem set without solutions.",
        tex_to_mdx(ROOT / "exercises/week02/week02_problem_set.tex"),
        "exercises/week02/week02_problem_set.tex",
        report,
    )
    write_generated(
        "exercises/week02-solutions.mdx",
        "Week 2 Solutions",
        "Browser-readable Week 2 solutions with proof strategies and common mistakes.",
        tex_to_mdx(ROOT / "exercises/week02/week02_solutions.tex"),
        "exercises/week02/week02_solutions.tex",
        report,
    )

    write_generated(
        "labs/week02-overview.mdx",
        "Week 2 Labs Overview",
        "How to run and interpret Week 2 algorithm labs.",
        read_or_placeholder(ROOT / "labs/week02/README.md", "labs/week02/README.md"),
        "labs/week02/README.md",
        report,
    )
    for lab in WEEK2_LAB_PAGES:
        write_generated(
            f"labs/{lab['slug']}.mdx",
            lab["title"],
            lab["concept"],
            lab_mdx(lab),
            lab["source"],
            report,
        )

    week2_review_pages = [
        ("review/week02-review.mdx", "Week 2 Review", "Week 2 review and repair checklist.", "review/week02/week02_review.md"),
        ("review/glossary-week02.mdx", "Week 2 Glossary", "Week 2 glossary.", "review/week02/glossary_week02.md"),
        ("review/mistakes-week02.mdx", "Week 2 Mistakes", "Week 2 mistakes grouped by topic.", "review/week02/mistakes_to_watch.md"),
        ("review/proof-patterns-week02.mdx", "Week 2 Proof Patterns", "Proof patterns for Week 2 algorithms.", "review/week02/proof_patterns_week02.md"),
    ]
    for rel, title, desc, source in week2_review_pages:
        write_generated(rel, title, desc, read_or_placeholder(ROOT / source, source), source, report)
    write_generated(
        "review/flashcards-week02.mdx",
        "Week 2 Flashcards",
        "Week 2 flashcards in Q/A format.",
        flashcards_mdx(ROOT / "review/week02/flashcards_week02.md"),
        "review/week02/flashcards_week02.md",
        report,
    )

    write_generated(
        "meta/resources.mdx",
        "Resources",
        "Official and legal sources used by the self-study system.",
        resources_mdx(),
        "resources/sources.yaml",
        report,
    )
    write_generated(
        "meta/progress.mdx",
        "Progress",
        "Current learning progress and state.",
        progress_mdx(),
        "state/progress.yaml",
        report,
    )
    write_generated(
        "meta/next-actions.mdx",
        "Next Actions",
        "Concrete next actions for study and Codex feedback.",
        read_or_placeholder(ROOT / "state/next_actions.md", "state/next_actions.md"),
        "state/next_actions.md",
        report,
    )


def main() -> int:
    if not DOCS.exists():
        print(f"Missing docs directory: {DOCS}")
        return 1
    report = {"generated": [], "modified": [], "skipped": []}
    sync(report)
    print("Site content sync complete.")
    for key in ("generated", "modified", "skipped"):
        print(f"{key}: {len(report[key])}")
        for item in report[key]:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
