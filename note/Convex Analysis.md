## Convex Set
::: definition:Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. $Q$ is convex if $[x, y] \subseteq Q$ for any $x, y \in Q$.
:::

::: definition:Minkowski Sum
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $A, B \subseteq \mathcal{E}$. $A + B := \{a + b : a \in A, b \in B\}$.
:::

::: definition:Nonnegative Scaling
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $A \subseteq \mathcal{E}$. $\mathbb{R}_+ A := \{\alpha a : a \in A, \alpha \geq 0\}$.
:::

::: definition:Image and Preimage
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, $A : \mathcal{E} \to \mathcal{Y}$, $Q \subseteq \mathcal{E}$, and $L \subseteq \mathcal{Y}$. $AQ := \{Ax : x \in Q\}$ and $A^{-1}L := \{x \in \mathcal{E} : Ax \in L\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $C \subseteq \mathcal{E}$. If $C$ is convex, then $\mathbb{R}_+ C$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q_1, Q_2 \subseteq \mathcal{E}$. If $Q_1$ and $Q_2$ are convex, then $Q_1 + Q_2$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $I$ be an index set, and $\{Q_i\}_{i \in I}$ be a family of subsets of $\mathcal{E}$. If $Q_i$ is convex for every $i \in I$, then $\bigcap_{i \in I} Q_i$ is convex.
:::

::: proposition
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, $A : \mathcal{E} \to \mathcal{Y}$, $Q \subseteq \mathcal{E}$, and $L \subseteq \mathcal{Y}$. If $A$ is linear and $Q$ and $L$ are convex, then $AQ$ and $A^{-1}L$ are convex.
:::

::: proposition:Scaling Identity for a Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\lambda_1, \lambda_2 \in \mathbb{R}$. Assume $Q$ is convex and $\lambda_1, \lambda_2 \geq 0$. $\lambda_1 Q + \lambda_2 Q = (\lambda_1 + \lambda_2)Q$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{cl}(Q)$ is convex.
:::

::: definition:Unit Simplex
Let $k \in \mathbb{Z}_+$. The $k$-dimensional unit simplex is $\Delta_k := \left\{\lambda \in \mathbb{R}^k : \lambda_i \geq 0 \text{ for every } i, \sum_{i=1}^k \lambda_i = 1\right\}$.
:::

::: definition:Convex Combination
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $k \in \mathbb{Z}_+$, and $x_1, \ldots, x_k \in \mathcal{E}$. A point $x \in \mathcal{E}$ is a convex combination of $x_1, \ldots, x_k$ if there exists $\lambda \in \Delta_k$ s.t. $x = \sum_{i=1}^k \lambda_i x_i$.
:::

::: lemma:Finite Convex Combinations
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. $Q$ is convex iff every convex combination of points of $Q$ lies in $Q$.
:::

::: definition:Convex Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. The convex hull of $Q$ is $\operatorname{conv}(Q) := \bigcap \{C \subseteq \mathcal{E} : C \text{ is convex and } Q \subseteq C\}$.
:::

::: lemma:Internal Description of the Convex Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. $\operatorname{conv}(Q) = \left\{\sum_{i=1}^k \lambda_i x_i : k \in \mathbb{Z}_+, x_1, \ldots, x_k \in Q, \lambda \in \Delta_k\right\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q, S \subseteq \mathcal{E}$. If $Q \subseteq S$, then $\operatorname{conv}(Q) \subseteq \operatorname{conv}(S)$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. $\operatorname{conv}(\operatorname{conv}(Q)) = \operatorname{conv}(Q)$.
:::

::: proposition
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, $A : \mathcal{E} \to \mathcal{Y}$, and $Q \subseteq \mathcal{E}$. Assume $A$ is linear. $A(\operatorname{conv}(Q)) = \operatorname{conv}(AQ)$.
:::

::: theorem:Carathéodory
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Every $x \in \operatorname{conv}(Q)$ is a convex combination of at most $\dim \mathcal{E} + 1$ points of $Q$.
:::

## Affine Hull
::: definition:Affine Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $L \subseteq \mathcal{E}$. $L$ is affine if there exist $v \in \mathcal{E}$ and a linear subspace $S \subseteq \mathcal{E}$ s.t. $L = v + S$.
:::

::: definition:Affine Combination
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $k \in \mathbb{Z}_+$, and $x_1, \ldots, x_k \in \mathcal{E}$. A point $x \in \mathcal{E}$ is an affine combination of $x_1, \ldots, x_k$ if there exists $\lambda \in \mathbb{R}^k$ s.t. $\sum_{i=1}^k \lambda_i = 1$ and $x = \sum_{i=1}^k \lambda_i x_i$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $L \subseteq \mathcal{E}$. Assume $L$ is nonempty. $L$ is affine iff every affine combination of points of $L$ lies in $L$.
:::

::: definition:Affine Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. The affine hull of $Q$ is $\operatorname{aff}(Q) := \bigcap \{L \subseteq \mathcal{E} : L \text{ is affine and } Q \subseteq L\}$.
:::

::: lemma:Internal Description of the Affine Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. $\operatorname{aff}(Q) = x_0 + \operatorname{span}(Q - x_0)$ for any $x_0 \in Q$, and $\operatorname{aff}(Q) = \left\{\sum_{i=1}^k \lambda_i x_i : k \in \mathbb{Z}_+, x_1, \ldots, x_k \in Q, \lambda \in \mathbb{R}^k, \sum_{i=1}^k \lambda_i = 1\right\}$.
:::

## Relative Interior
::: definition:Relative Interior
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. The relative interior of $Q$ is $\operatorname{ri}(Q) := \{x \in Q : \text{there exists } \epsilon > 0 \text{ s.t. } B_\epsilon(x) \cap \operatorname{aff}(Q) \subseteq Q\}$.
:::

::: definition:Relative Boundary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. The relative boundary of $Q$ is $\operatorname{rb}(Q) := \operatorname{cl}(Q) \setminus \operatorname{ri}(Q)$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $\operatorname{aff}(Q) = \mathcal{E}$, then $\operatorname{ri}(Q) = \operatorname{int}(Q)$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $L \subseteq \mathcal{E}$. If $L$ is affine, then $\operatorname{ri}(L) = L$ and $\operatorname{rb}(L) = \emptyset$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $x \in \mathcal{E}$. $\operatorname{ri}(\{x\}) = \{x\}$.
:::

::: theorem:Nonempty Relative Interior under Convexity
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and convex, then $\operatorname{ri}(Q) \neq \emptyset$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{ri}(Q)$ is convex.
:::

::: proposition:Affine Hull of Closure and Relative Interior
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{aff}(\operatorname{cl}(Q)) = \operatorname{aff}(Q) = \operatorname{aff}(\operatorname{ri}(Q))$.
:::

::: theorem:Accessibility
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is convex. $[x, y) \subseteq \operatorname{ri}(Q)$ for any $x \in \operatorname{ri}(Q)$ and $y \in \operatorname{cl}(Q)$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and convex, then $\operatorname{cl}(\operatorname{ri}(Q)) = \operatorname{cl}(Q)$ and $\operatorname{ri}(\operatorname{cl}(Q)) = \operatorname{ri}(Q)$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is nonempty, closed, and convex, then $Q = \operatorname{cl}(\operatorname{ri}(Q))$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q_1, Q_2 \subseteq \mathcal{E}$. Assume $Q_1$ and $Q_2$ are convex. If $\operatorname{cl}(Q_1) = \operatorname{cl}(Q_2)$, then $\operatorname{ri}(Q_1) = \operatorname{ri}(Q_2)$.
:::
