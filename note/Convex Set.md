::: definition:Convex Set
Let $Q \subseteq \mathcal{E}$. $Q$ is convex if $\alpha x + \beta y \in Q$ for any $x, y \in Q$ and $\alpha, \beta \geq 0$ s.t. $\alpha + \beta = 1$.
:::

::: proposition
Nonnegative scaling, Minkowski sums, intersections, Cartesian products, linear images and linear preimages of convex sets are convex sets.
::: ^convex-set-operations

::: proposition:Scaling Identity for a Convex Set
Let $Q \subseteq \mathcal{E}$, and $\lambda_1, \lambda_2 \in \mathbb{R}$. Assume $Q$ is convex and $\lambda_1, \lambda_2 \geq 0$. $\lambda_1 Q + \lambda_2 Q = (\lambda_1 + \lambda_2)Q$.
:::

::: definition:Unit Simplex
Let $k \in \mathbb{Z}_+$. The $k$-dimensional unit simplex is $\Delta_k := \left\{\lambda \in \mathbb{R}^k : \lambda_i \geq 0 \text{ for every } i, \sum_{i=1}^k \lambda_i = 1\right\}$.
:::

::: definition:Convex Combination
Let $k \in \mathbb{Z}_+$, and $x_1, \ldots, x_k \in \mathcal{E}$. A point $x \in \mathcal{E}$ is a convex combination of $x_1, \ldots, x_k$ if there exists $\lambda \in \Delta_k$ s.t. $x = \sum_{i=1}^k \lambda_i x_i$.
:::

::: lemma:Finite Convex Combinations
Let $Q \subseteq \mathcal{E}$. $Q$ is convex iff every convex combination of points of $Q$ lies in $Q$.
:::

::: definition:Convex Hull
Let $Q \subseteq \mathcal{E}$. The convex hull of $Q$ is $\operatorname{conv}(Q) := \bigcap \{C \subseteq \mathcal{E} : C \text{ is convex and } Q \subseteq C\}$.
:::

::: theorem:Internal Description of the Convex Hull
Let $Q \subseteq \mathcal{E}$. $\operatorname{conv}(Q) = \left\{\sum_{i=1}^k \lambda_i x_i : k \in \mathbb{Z}_+, x_1, \ldots, x_k \in Q, \lambda \in \Delta_k\right\}$.
:::

::: proposition
Let $Q, S \subseteq \mathcal{E}$. If $Q \subseteq S$, then $\operatorname{conv}(Q) \subseteq \operatorname{conv}(S)$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$. $\operatorname{conv}(\operatorname{conv}(Q)) = \operatorname{conv}(Q)$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $Q, S \subseteq \mathcal{E}$. Assume $A$ is linear. $\operatorname{conv}(\lambda Q) = \lambda\operatorname{conv}(Q)$ for any $\lambda \ge 0$, $\operatorname{conv}(Q + S) = \operatorname{conv}(Q) + \operatorname{conv}(S)$, $\operatorname{conv}(Q \times S) = \operatorname{conv}(Q) \times \operatorname{conv}(S)$, and $\operatorname{conv}(AQ) = A(\operatorname{conv}(Q))$.
:::

*Proof.*
The identities follow by expanding convex combinations, using linearity and $\sum_{i,j}\alpha_i\beta_j = \left(\sum_i\alpha_i\right)\left(\sum_j\beta_j\right) = 1$ for convex weights $\alpha_i$ and $\beta_j$.

::: note
$\operatorname{conv}(Q \cap S) \subseteq \operatorname{conv}(Q) \cap \operatorname{conv}(S)$, and $\operatorname{conv}(A^{-1}T) \subseteq A^{-1}(\operatorname{conv}(T))$ for any $T \subseteq \mathcal{Y}$. If $A$ is invertible, then the last inclusion is an equality.
:::

::: theorem:Carathéodory
Let $Q \subseteq \mathcal{E}$. Every $x \in \operatorname{conv}(Q)$ is a convex combination of at most $\dim \mathcal{E} + 1$ points of $Q$.
:::

*Proof.*
For $\dim\mathcal{E}+2$, consider a convex combination $x = \sum_{i=1}^{\dim\mathcal{E}+2}\alpha_i x_i$ with $\alpha \in \Delta_{\dim\mathcal{E}+2}$. The $\dim\mathcal{E}+1$ vectors $x_i - x_{\dim\mathcal{E}+2}$ are linearly dependent, so there are scalars $\beta_i$, not all zero, with $\sum_{i=1}^{\dim\mathcal{E}+1}\beta_i(x_i - x_{\dim\mathcal{E}+2}) = 0$. Hence $x_{\dim\mathcal{E}+2} = \sum_{i=1}^{\dim\mathcal{E}+1}\beta_i x_i \big/ \sum_{i=1}^{\dim\mathcal{E}+1}\beta_i$, and substituting gives $x = \sum_{i=1}^{\dim\mathcal{E}+1}\bigl(\alpha_i + \alpha_{\dim\mathcal{E}+2}\beta_i \big/ \sum_{j=1}^{\dim\mathcal{E}+1}\beta_j\bigr)x_i$. The new coefficients are nonnegative and sum to $1$, so $\dim\mathcal{E}+1$ points suffice. Then we use induction.
