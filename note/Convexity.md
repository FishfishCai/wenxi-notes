::: definition:Effective Domain
Let $f : \mathcal{E} \to \mathbb{R} \cup \{-\infty, +\infty\}$. Set $\overline{\mathbb{R}} := \mathbb{R} \cup \{-\infty, +\infty\}$. The effective domain of $f$ is $\operatorname{dom} f := \{x \in \mathcal{E} : f(x) < +\infty\}$.
:::

::: definition:Epigraph
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The epigraph of $f$ is $\operatorname{epi} f := \{(x, r) \in \mathcal{E} \times \mathbb{R} : f(x) \leq r\}$.
:::

::: definition:Proper Function
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is proper if $\operatorname{dom} f \neq \emptyset$ and $f(x) > -\infty$ for any $x \in \mathcal{E}$.
:::

::: definition:Convex Function
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is convex if $\operatorname{epi} f$ is convex.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper. The function $f$ is convex iff $f(tx + (1 - t)y) \leq t f(x) + (1 - t)f(y)$ for any $x, y \in \mathcal{E}$ and $t \in [0, 1]$, with $0 \cdot (+\infty) = 0$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. $f$ is convex iff for any $x \in \mathcal{E}$, there exists $v \in \partial f(x)$ s.t. $f(y) \geq f(x) + \langle v, y - x\rangle$ for any $y \in \mathcal{E}$.
::: ^convex-first-order

::: note
If $f \in \mathcal{C}^1$, [[#^convex-first-order|Proposition 6]] becomes: $f$ is convex iff $f(y) \geq f(x) + \langle \nabla f(x), y - x\rangle$ for any $x, y \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$. $f$ is convex iff $\nabla^2 f(x) \succeq 0$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. $\operatorname{dom} f$ is convex.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. The sublevel set $\{x \in \mathcal{E} : f(x) \leq \alpha\}$ is convex for any $\alpha \in \mathbb{R}$.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. The set of global minimizers of $f$ is convex.
:::

::: definition:Quasiconvex Function
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is quasiconvex if $\{x \in \mathcal{E} : f(x) \leq \alpha\}$ is convex for any $\alpha \in \mathbb{R}$.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. If $f$ is convex, then $f$ is quasiconvex. The converse does not hold in general.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. If there exists $\bar{x} \in \operatorname{ri}(\operatorname{dom} f)$ s.t. $f(\bar{x}) > -\infty$, then $f$ is proper.
:::
