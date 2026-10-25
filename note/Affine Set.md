::: definition:Affine Set
Let $L \subseteq \mathcal{E}$. $L$ is affine if there exist $v \in \mathcal{E}$ and a linear subspace $S \subseteq \mathcal{E}$ s.t. $L = v + S$.
:::

::: proposition
Scalar multiples, Minkowski sums, Cartesian products, nonempty intersections, linear images, and nonempty linear preimages of affine sets are affine sets.
:::

::: definition:Affine Combination
Let $k \in \mathbb{Z}_+$, and $x_1, \ldots, x_k \in \mathcal{E}$. A point $x \in \mathcal{E}$ is an affine combination of $x_1, \ldots, x_k$ if there exists $\lambda \in \mathbb{R}^k$ s.t. $\sum_{i=1}^k \lambda_i = 1$ and $x = \sum_{i=1}^k \lambda_i x_i$.
:::

::: proposition
Let $L \subseteq \mathcal{E}$. Assume $L$ is nonempty. $L$ is affine iff every affine combination of points of $L$ lies in $L$.
:::

::: definition:Affine Hull
Let $Q \subseteq \mathcal{E}$. The affine hull of $Q$ is $\operatorname{aff}(Q) := \bigcap \{L \subseteq \mathcal{E} : L \text{ is affine and } Q \subseteq L\}$, with $\operatorname{aff}(\emptyset) := \emptyset$.
:::

::: lemma:Internal Description of the Affine Hull
Let $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. $\operatorname{aff}(Q) = x_0 + \operatorname{span}(Q - x_0)$ for any $x_0 \in Q$, and $\operatorname{aff}(Q) = \left\{\sum_{i=1}^k \lambda_i x_i : k \in \mathbb{Z}_+, x_1, \ldots, x_k \in Q, \lambda \in \mathbb{R}^k, \sum_{i=1}^k \lambda_i = 1\right\}$.
:::

::: proposition
Let $Q, S \subseteq \mathcal{E}$. If $Q \subseteq S$, then $\operatorname{aff}(Q) \subseteq \operatorname{aff}(S)$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$. $\operatorname{aff}(\operatorname{aff}(Q)) = \operatorname{aff}(Q)$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $Q, S \subseteq \mathcal{E}$. Assume $A$ is linear. $\operatorname{aff}(\lambda Q) = \lambda\operatorname{aff}(Q)$ for any $\lambda \in \mathbb{R}$, $\operatorname{aff}(Q + S) = \operatorname{aff}(Q) + \operatorname{aff}(S)$, $\operatorname{aff}(Q \times S) = \operatorname{aff}(Q) \times \operatorname{aff}(S)$, and $\operatorname{aff}(AQ) = A(\operatorname{aff}(Q))$.
:::

*Proof.*
The identities follow by expanding affine combinations, using linearity and $\sum_{i,j}\alpha_i\beta_j = \left(\sum_i\alpha_i\right)\left(\sum_j\beta_j\right) = 1$ for affine weights $\alpha_i$ and $\beta_j$.

::: note
$\operatorname{aff}(Q \cap S) \subseteq \operatorname{aff}(Q) \cap \operatorname{aff}(S)$, and $\operatorname{aff}(A^{-1}T) \subseteq A^{-1}(\operatorname{aff}(T))$ for any $T \subseteq \mathcal{Y}$. If $A$ is invertible, then the last inclusion is an equality.
:::
