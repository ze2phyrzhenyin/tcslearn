# Content Style Guide

## Language

- Explanations should be in Chinese.
- Keep mathematical symbols, theorem names, algorithm names, and field names in English.
- Introduce English terms with a short Chinese explanation the first time they appear.
- Avoid decorative prose. Prefer precise, learnable structure.

## Definitions

Every definition must include:

- formal definition;
- motivation;
- minimal example;
- non-example;
- why the non-example fails;
- connection to later TCS topics.

Never use a term before defining it unless it is listed as a prerequisite.

## Proofs

Every proof must be split into:

- Statement;
- Definitions used;
- Assumptions;
- Goal;
- Strategy;
- Proof;
- Check: why each nontrivial step is valid;
- Common mistake.

Avoid “显然”. If a step is immediate, name the definition, theorem, or algebraic fact that makes it immediate.

## Algorithms

Every algorithm explanation must include:

- problem;
- input;
- output;
- invariant;
- pseudocode or Python reference implementation when useful;
- correctness argument;
- preprocessing time;
- query time if applicable;
- total running time;
- space complexity;
- edge cases.

Always state the variables used in Big-O, for example `n = |text|`, `m = |pattern|`, `sigma = alphabet size`.

## Probability and Randomization

Every probability topic must include:

- sample space;
- random variables;
- distribution assumptions;
- event definitions;
- expectation or concentration statement;
- failure probability if randomized algorithms are involved.

Do not use probability notation before defining the event or random variable.

## Learning Theory

Every learning theory note must include:

- setup;
- distribution;
- hypothesis class;
- loss;
- risk;
- empirical risk;
- sample size;
- confidence;
- bound statement;
- proof sketch or where the proof is deferred.

Make clear whether a result is realizable, agnostic, finite-class, VC-style, or stability-based.

## Differential Privacy

Every DP note must include:

- dataset model;
- neighboring relation;
- query;
- sensitivity;
- mechanism;
- privacy guarantee;
- privacy proof sketch;
- utility statement when applicable.

Never state an `(epsilon, delta)` guarantee without specifying the neighboring relation and randomness of the mechanism.

