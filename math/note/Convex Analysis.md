## Convex Set
::: definition:Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q \subseteq \mathcal{E}$. $Q$ is convex if $[x, y] \subseteq Q$ for any $x, y \in Q$.
:::

::: definition:Minkowski Sum
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $A, B \subseteq \mathcal{E}$. $A + B := \{a + b : a \in A, b \in B\}$.
:::

::: definition:Nonnegative Scaling
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $A \subseteq \mathcal{E}$. $\mathbb{R}_+ A := \{\alpha a : a \in A, \alpha \geq 0\}$.
:::

::: definition:Image and Preimage
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, let $A : \mathcal{E} \to \mathcal{Y}$, and let $Q \subseteq \mathcal{E}$ and $L \subseteq \mathcal{Y}$. $AQ := \{Ax : x \in Q\}$ and $A^{-1}L := \{x \in \mathcal{E} : Ax \in L\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $C \subseteq \mathcal{E}$. If $C$ is convex, then $\mathbb{R}_+ C$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q_1, Q_2 \subseteq \mathcal{E}$. If $Q_1$ and $Q_2$ are convex, then $Q_1 + Q_2$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, let $I$ be an index set, and let $\{Q_i\}_{i \in I}$ be a family of subsets of $\mathcal{E}$. If $Q_i$ is convex for every $i \in I$, then $\bigcap_{i \in I} Q_i$ is convex.
:::

::: proposition
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, let $A : \mathcal{E} \to \mathcal{Y}$, and let $Q \subseteq \mathcal{E}$ and $L \subseteq \mathcal{Y}$. If $A$ is linear and $Q$ and $L$ are convex, then $AQ$ and $A^{-1}L$ are convex.
:::

::: proposition:Scaling Identity for a Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, let $Q \subseteq \mathcal{E}$, and let $\lambda_1, \lambda_2 \in \mathbb{R}$. Assume $Q$ is convex and $\lambda_1, \lambda_2 \geq 0$. $\lambda_1 Q + \lambda_2 Q = (\lambda_1 + \lambda_2)Q$.
:::

::: definition:Unit Simplex
Let $k \in \mathbb{Z}_+$. The $k$-dimensional unit simplex is $\Delta_k := \left\{\lambda \in \mathbb{R}^k : \lambda_i \geq 0 \text{ for every } i, \sum_{i=1}^k \lambda_i = 1\right\}$.
:::

::: definition:Convex Combination
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, let $k \in \mathbb{Z}_+$, and let $x_1, \ldots, x_k \in \mathcal{E}$. A point $x \in \mathcal{E}$ is a convex combination of $x_1, \ldots, x_k$ if $x = \sum_{i=1}^k \lambda_i x_i$ for some $\lambda \in \Delta_k$.
:::

::: lemma:Finite Convex Combinations
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, let $Q \subseteq \mathcal{E}$, and let $k \in \mathbb{Z}_+$. Assume $Q$ is convex. Every convex combination of points $x_1, \ldots, x_k \in Q$ lies in $Q$.
:::

::: definition:Convex Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q \subseteq \mathcal{E}$. The convex hull of $Q$ is $\operatorname{conv}(Q) := \bigcap \{C \subseteq \mathcal{E} : C \text{ is convex and } Q \subseteq C\}$.
:::

::: lemma:Internal Description of the Convex Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q \subseteq \mathcal{E}$. $\operatorname{conv}(Q) = \left\{\sum_{i=1}^k \lambda_i x_i : k \in \mathbb{Z}_+, x_1, \ldots, x_k \in Q, \lambda \in \Delta_k\right\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q, S \subseteq \mathcal{E}$. If $Q \subseteq S$, then $\operatorname{conv}(Q) \subseteq \operatorname{conv}(S)$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q \subseteq \mathcal{E}$. $\operatorname{conv}(\operatorname{conv}(Q)) = \operatorname{conv}(Q)$.
:::

::: proposition
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, let $A : \mathcal{E} \to \mathcal{Y}$, and let $Q \subseteq \mathcal{E}$. Assume $A$ is linear. $A(\operatorname{conv}(Q)) = \operatorname{conv}(AQ)$.
:::

::: theorem:Carathéodory
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and let $Q \subseteq \mathcal{E}$. Every $x \in \operatorname{conv}(Q)$ is a convex combination of at most $\dim \mathcal{E} + 1$ points of $Q$.
:::
