::: definition:Relative Interior
Let $Q \subseteq \mathcal{E}$. The relative interior of $Q$ is $\operatorname{ri}(Q) := \{x \in Q : \text{there exists } \varepsilon > 0 \text{ s.t. } B_\varepsilon(x) \cap \operatorname{aff}(Q) \subseteq Q\}$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$. If $\operatorname{aff}(Q) = \mathcal{E}$, then $\operatorname{ri}(Q) = \operatorname{int}(Q)$.
:::

::: definition:Relative Boundary
Let $Q \subseteq \mathcal{E}$. The relative boundary of $Q$ is $\operatorname{rb}(Q) := \operatorname{cl}(Q) \setminus \operatorname{ri}(Q)$.
:::

::: proposition
Let $L \subseteq \mathcal{E}$. If $L$ is affine, then $\operatorname{ri}(L) = L$ and $\operatorname{rb}(L) = \emptyset$.
::: ^affine-relative-interior

::: proposition
Let $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{cl}(Q)$ is convex.
::: ^closure-convexity

::: theorem:Nonempty Relative Interior under Convexity
Let $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and convex, then $\operatorname{ri}(Q) \neq \emptyset$.
::: ^nonempty-relative-interior-under-convexity

*Proof.*
Assume $0 \in Q$ and choose a basis of $\operatorname{span}(Q)$ from $Q$. Consider the simplex spanned by these points and $0$.

::: proposition
Let $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{ri}(Q)$ is convex.
::: ^relative-interior-convexity

::: note
[[#^affine-relative-interior|Proposition 4]], [[#^closure-convexity|Proposition 5]], [[#^nonempty-relative-interior-under-convexity|Theorem 6 (Nonempty Relative Interior under Convexity)]], and [[#^relative-interior-convexity|Proposition 7]] describe the relative interior and closure of affine and convex sets. Affine sets are trivially convex.
:::

::: proposition:Affine Hull of Closure and Relative Interior
Let $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $\operatorname{aff}(\operatorname{cl}(Q)) = \operatorname{aff}(Q) = \operatorname{aff}(\operatorname{ri}(Q))$.
::: ^affine-hull-of-closure-and-relative-interior

::: note
[[#^affine-hull-of-closure-and-relative-interior|Proposition 8 (Affine Hull of Closure and Relative Interior)]] compares the affine hulls of $\operatorname{cl}(Q)$, $Q$, and $\operatorname{ri}(Q)$. The analogous comparison of convex hulls is trivial.
:::

::: theorem:Accessibility
Let $Q \subseteq \mathcal{E}$. If $Q$ is convex, then $(1 - t)x + ty \in \operatorname{ri}(Q)$ for any $x \in \operatorname{ri}(Q)$, $y \in \operatorname{cl}(Q)$, and $t \in [0, 1)$.
:::

::: corollary
Let $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and convex, then $\operatorname{cl}(\operatorname{ri}(Q)) = \operatorname{cl}(Q)$ and $\operatorname{ri}(\operatorname{cl}(Q)) = \operatorname{ri}(Q)$.
::: ^closure-and-relative-interior-composition

::: corollary
Let $Q \subseteq \mathcal{E}$. If $Q$ is nonempty, closed, and convex, then $Q = \operatorname{cl}(\operatorname{ri}(Q))$.
::: ^closed-convex-set-from-relative-interior

::: corollary
Let $Q_1, Q_2 \subseteq \mathcal{E}$. Assume $Q_1$ and $Q_2$ are convex. If $\operatorname{cl}(Q_1) = \operatorname{cl}(Q_2)$, then $\operatorname{ri}(Q_1) = \operatorname{ri}(Q_2)$.
::: ^equal-closures-equal-relative-interiors

::: note
[[#^closure-and-relative-interior-composition|Corollary 10]], [[#^closed-convex-set-from-relative-interior|Corollary 11]], and [[#^equal-closures-equal-relative-interiors|Corollary 12]] describe how $\operatorname{ri}$ and $\operatorname{cl}$ compose. For affine sets they are trivial.
:::
