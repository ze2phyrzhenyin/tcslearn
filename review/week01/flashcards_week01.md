# Week 1 Flashcards

Q: What is a proposition?
A: A statement with a definite truth value.
Tag: logic

Q: What is a predicate?
A: A statement template whose truth depends on variables and their domain.
Tag: logic

Q: How do you negate `forall x exists y P(x,y)`?
A: `exists x forall y not P(x,y)`, with the same domains.
Tag: logic

Q: Why is `P -> Q` not the same as `Q -> P`?
A: `P -> Q` can be true while its converse fails; for example divisible by 4 implies even, but even does not imply divisible by 4.
Tag: proof

Q: What is the contrapositive of `P -> Q`?
A: `not Q -> not P`, and it is logically equivalent to the original implication.
Tag: proof

Q: What is the standard way to prove two sets are equal?
A: Prove both inclusions: `A subseteq B` and `B subseteq A`.
Tag: sets

Q: What does `A subseteq B` mean?
A: For every `x`, if `x in A` then `x in B`.
Tag: sets

Q: What is a Cartesian product?
A: `A x B` is the set of ordered pairs `(a,b)` with `a in A` and `b in B`.
Tag: sets

Q: What is an equivalence relation?
A: A relation that is reflexive, symmetric, and transitive.
Tag: logic

Q: What is a partial order?
A: A relation that is reflexive, antisymmetric, and transitive.
Tag: logic

Q: What does injective mean?
A: Equal outputs imply equal inputs.
Tag: functions

Q: What does surjective mean?
A: Every element of the codomain is hit by at least one input.
Tag: functions

Q: What is the preimage of a set?
A: `f^{-1}(T)` is the set of inputs whose outputs lie in `T`.
Tag: functions

Q: Does preimage require an inverse function?
A: No; preimage is defined for any function.
Tag: functions

Q: What makes a counterexample valid?
A: It must satisfy the domain and assumptions while falsifying the conclusion.
Tag: proof

Q: What are the parts of ordinary induction?
A: Base case, induction hypothesis, induction step, and conclusion.
Tag: induction

Q: What is the induction hypothesis?
A: The exact statement assumed for a previous or smaller case.
Tag: induction

Q: When is strong induction useful?
A: When the next case depends on multiple or arbitrary smaller cases.
Tag: induction

Q: What is structural induction for?
A: Proving properties of recursively defined objects by checking base constructors and recursive constructors.
Tag: induction

Q: Why can the base case not be skipped?
A: Without it, the implication chain has no starting point.
Tag: induction

Q: What are the three invariant proof obligations?
A: Initialization, maintenance, and termination.
Tag: invariants

Q: What is a loop invariant?
A: A statement that remains true at a specified point of every loop iteration.
Tag: invariants

Q: What is a termination argument?
A: A proof that a computation stops, often using a decreasing measure with a lower bound.
Tag: invariants

Q: Why are correctness and running time different?
A: Correctness proves the output specification; running time bounds resource usage.
Tag: invariants

Q: What invariant supports Euclidean algorithm correctness?
A: The gcd of the current pair equals the gcd of the original pair.
Tag: invariants

Q: What does `f in O(g)` mean?
A: Eventually `f(n) <= c g(n)` for constants `c>0` and `n0`.
Tag: asymptotics

Q: What does `f in Omega(g)` mean?
A: Eventually `f(n) >= c g(n)` for constants `c>0` and `n0`.
Tag: asymptotics

Q: What must be proved for `Theta`?
A: Both an upper bound and a lower bound.
Tag: asymptotics

Q: What is the common mistake with Big-O?
A: Treating it as approximate equality instead of an eventual upper bound.
Tag: asymptotics

Q: Why must the variable be stated in asymptotic notation?
A: The limit process depends on which parameter tends to infinity.
Tag: asymptotics

Q: What is a recurrence?
A: A definition of a quantity using its values on smaller inputs.
Tag: recurrences

Q: Why does a recurrence need a base case?
A: Without a base case it is not a complete definition.
Tag: recurrences

Q: What does a recursion tree show?
A: The work contributed by recursive calls level by level.
Tag: recurrences

Q: What is the substitution method?
A: Guess a bound and prove it by induction.
Tag: recurrences

Q: What is the RAM model?
A: A simplified cost model where basic operations are treated as constant time.
Tag: asymptotics

Q: What is the sum rule?
A: Disjoint cases are counted by adding their sizes.
Tag: counting

Q: What is the product rule?
A: Sequential choices are counted by multiplying the number of choices at each step.
Tag: counting

Q: What does `binom(n,k)` count?
A: Unordered `k`-element subsets of an `n`-element set.
Tag: counting

Q: What question should you ask before a counting problem?
A: Are the objects ordered, and is repetition allowed?
Tag: counting

Q: What does inclusion-exclusion fix?
A: It corrects double-counting of overlaps.
Tag: counting

Q: What is the pigeonhole principle?
A: More objects than boxes implies some box contains at least two objects.
Tag: counting

Q: What is a graph?
A: A set of vertices together with edges connecting vertices.
Tag: graphs

Q: What is a tree?
A: A connected acyclic undirected graph.
Tag: graphs

Q: How many edges does a tree with `n` vertices have?
A: `n-1`.
Tag: graphs

Q: What is a bipartite graph?
A: A graph whose vertices split into two sides with every edge crossing sides.
Tag: graphs

Q: What is a state graph?
A: A graph whose vertices are states and whose edges are allowed transitions.
Tag: graphs

Q: What is a sample space?
A: The set of all possible outcomes of a random experiment.
Tag: probability

Q: What is an event?
A: A subset of the sample space.
Tag: probability

Q: What is a random variable?
A: A function from outcomes to numerical values.
Tag: probability

Q: What is conditional probability?
A: `Pr[A | B] = Pr[A cap B] / Pr[B]` when `Pr[B] > 0`.
Tag: probability

Q: Are disjoint nonzero events independent?
A: No, because their intersection probability is zero but the product of probabilities is positive.
Tag: probability

Q: Does linearity of expectation require independence?
A: No.
Tag: probability

Q: What is an indicator random variable?
A: A 0-1 random variable representing whether an event occurs.
Tag: probability

Q: What is the expectation of an indicator variable?
A: The probability of the event it indicates.
Tag: probability

Q: What does the union bound say?
A: The probability of a union is at most the sum of event probabilities.
Tag: concentration

Q: What condition does Markov inequality require?
A: The random variable must be nonnegative.
Tag: concentration

Q: What does Chebyshev inequality use?
A: Variance to bound deviation from the mean.
Tag: concentration

Q: What does Hoeffding require?
A: Independent bounded random variables.
Tag: concentration

Q: What is failure probability?
A: The probability, over algorithmic randomness, that a randomized algorithm gives a bad result.
Tag: probability

Q: In learning theory, what is probability often over?
A: The random training sample.
Tag: probability

Q: What is a vector?
A: An ordered tuple such as an element of `R^d`.
Tag: linear_algebra

Q: What is an inner product?
A: A scalar-valued operation measuring alignment between vectors.
Tag: linear_algebra

Q: What is a norm?
A: A length function satisfying nonnegativity, definiteness, homogeneity, and triangle inequality.
Tag: linear_algebra

Q: What is the `L1` norm?
A: The sum of absolute coordinate values.
Tag: linear_algebra

Q: What is the `L2` norm?
A: The Euclidean norm, square root of sum of squared coordinates.
Tag: linear_algebra

Q: What is the `Linf` norm?
A: The maximum absolute coordinate value.
Tag: linear_algebra

Q: State Cauchy-Schwarz.
A: `|<x,y>| <= ||x||_2 ||y||_2`.
Tag: linear_algebra

Q: What is a linear map?
A: A map preserving addition and scalar multiplication.
Tag: linear_algebra

Q: What is a convex set?
A: A set containing the line segment between any two of its points.
Tag: convexity

Q: What is a convex function?
A: A function whose value at a convex combination is at most the convex combination of values.
Tag: convexity

Q: What does Jensen inequality say intuitively?
A: For convex functions, function of the average is at most average of function values.
Tag: convexity

Q: What is Lipschitz continuity?
A: A uniform bound on how much output can change relative to input change.
Tag: convexity

Q: Why does convexity matter in learning theory?
A: It makes many optimization and generalization arguments controllable.
Tag: convexity

Q: What is an alphabet?
A: A finite set of symbols.
Tag: models

Q: What is a string?
A: A finite sequence of symbols from an alphabet.
Tag: models

Q: What is a language?
A: A set of strings.
Tag: models

Q: What is a decision problem?
A: A problem with yes/no output.
Tag: models

Q: What is the difference between a problem and an algorithm?
A: A problem specifies input-output behavior; an algorithm is a method for solving it.
Tag: models

Q: What is a DFA?
A: A deterministic finite automaton with finite states, transitions, a start state, and accepting states.
Tag: models

Q: What is a reduction?
A: A transformation showing how solving one problem can solve another.
Tag: reductions

Q: In a many-one reduction `A <= B`, what does the mapping prove?
A: It maps instances so `x in A` iff `f(x) in B`.
Tag: reductions

Q: Why is reduction direction important?
A: To prove `B` is hard from `A`, the reduction usually goes from known-hard `A` to `B`.
Tag: reductions

Q: Why does encoding matter?
A: Complexity is measured in input length, and different encodings can change that length.
Tag: models

Q: What should a theorem statement include?
A: Objects, assumptions, variables, conclusion, and relevant model.
Tag: proof

