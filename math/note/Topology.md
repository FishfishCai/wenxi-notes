## Topological Structure
::: definition:Topology
Let $X$ be a set and $\mathcal{T} \subseteq \mathcal{P}(X)$. The family $\mathcal{T}$ is a topology on $X$ if:
- $\emptyset \in \mathcal{T}$ and $X \in \mathcal{T}$.
- $\bigcap_{j = 1}^n U_j \in \mathcal{T}$ for any finite family $U_1,\ldots,U_n \in \mathcal{T}$.
- $\bigcup_{\alpha \in A}U_\alpha \in \mathcal{T}$ for any family $(U_\alpha)_{\alpha \in A}$ in $\mathcal{T}$.
The pair $(X,\mathcal{T})$ is a topological space.
:::

::: definition:Open set
Let $X$ be a topological space. The open sets in $X$ are the members of the topology.
:::

::: definition:Closed set
Let $X$ be a topological space and $E \subset X$. $E$ is closed if its complement is open.
:::

::: definition:Closure
Let $X$ be a topological space and $E \subset X$. The closure $\overline{E}$ is the smallest closed set in $X$ which contains $E$.
:::

::: definition:F-sigma set
Let $X$ be a topological space. A subset of $X$ is an $F_\sigma$ set if it is a countable union of closed sets.
:::

::: definition:G-delta set
Let $X$ be a topological space. A subset of $X$ is a $G_\delta$ set if it is a countable intersection of open sets.
:::

::: definition:Continuous function
Let $X$ and $Y$ be topological spaces and $f : X \to Y$. $f$ is continuous if $f^{-1}(V)$ is open in $X$ for every open $V$ in $Y$.
:::

::: definition:Continuity at a Point
Let $X$ and $Y$ be topological spaces, $f : X \to Y$ and $x_0 \in X$. $f$ is continuous at $x_0$ if for every open $V$ containing $f(x_0)$ in $Y$, there is an open $W$ containing $x_0$ in $X$ s.t. $W \subset f^{-1}(V)$.
:::

::: proposition
Let $X$ and $Y$ be topological spaces and $f : X \to Y$. $f$ is continuous iff $f$ is continuous at every point of $X$.
:::

::: proposition
Let $X,Y,Z$ be topological spaces and $f : X \to Y$ and $g : Y \to Z$ be continuous. The composition $g \circ f$ is continuous.
:::

::: definition:Hausdorff space
Let $X$ be a topological space. $X$ is a Hausdorff space if for any $p, q \in X$ with $p \neq q$, $p$ has a neighborhood $U$ and $q$ has a neighborhood $V$ s.t. $U \cap V = \emptyset$.
:::

::: definition:Compact set
Let $X$ be a topological space and $K \subset X$. $K$ is compact if every open cover of $K$ contains a finite subcover.
:::

::: definition:Locally Compact Space
Let $X$ be a topological space. The space $X$ is locally compact if every point has a compact neighborhood.
:::

::: proposition
Let $X$ be a Hausdorff space. The space $X$ is locally compact iff every point has an open neighborhood with compact closure.
:::

::: definition:Sigma-Compact Set
Let $X$ be a topological space and $E \subseteq X$. The set $E$ is $\sigma$-compact if it is a countable union of compact subsets of $X$.
:::

::: proposition
Let $X$ be a topological space, $K \subset X$ compact and $F \subset X$ closed. If $F \subset K$, then $F$ is compact.
:::

::: proposition
Let $X$ be a topological space and $A \subset B \subset X$. If $B$ has a compact closure, then $A$ has a compact closure.
:::

::: proposition
Let $X$ be a Hausdorff space and $K \subseteq X$ be compact. The set $K$ is closed in $X$.
:::

::: proposition
Let $X$ be a Hausdorff space, $K \subseteq X$ be compact, and $F \subseteq X$ be closed. The set $F \cap K$ is compact.
:::

::: proposition
Let $X$ be a Hausdorff space, $K \subseteq X$ be compact, and $p \in X\setminus K$. There exist disjoint open sets $U,W \subseteq X$ s.t. $p \in U$ and $K \subseteq W$.
:::

::: proposition
Let $X$ be a Hausdorff space and $(K_\alpha)_{\alpha \in A}$ be a nonempty family of compact subsets of $X$. If $\bigcap_{\alpha \in A}K_\alpha = \emptyset$, then there exists a finite nonempty $F \subseteq A$ s.t. $\bigcap_{\alpha \in F}K_\alpha = \emptyset$.
:::

::: proposition
Let $X$ be a locally compact Hausdorff space, $U \subset X$ open and $K \subset X$ compact. If $K \subset U$, then there is an open set $V$ s.t. $\overline{V}$ is compact and $K \subset V \subset \overline{V} \subset U$.
:::

::: proposition
Let $X$ and $Y$ be topological spaces and $K \subset X$ compact. If $f : X \to Y$ is continuous, then $f(K)$ is compact.
:::

## Semicontinuity
::: definition:Lower semicontinuous function
Let $X$ be a topological space and $f : X \to [-\infty, \infty]$. $f$ is lower semicontinuous if $\{x : f(x) > \alpha\}$ is open for every real $\alpha$.
:::

::: note
The indicator of an open set is lower semicontinuous. The pointwise supremum of any family of lower semicontinuous functions is lower semicontinuous.
:::

::: definition:Upper semicontinuous function
Let $X$ be a topological space and $f : X \to [-\infty, \infty]$. $f$ is upper semicontinuous if $\{x : f(x) < \alpha\}$ is open for every real $\alpha$.
:::

::: note
The indicator of a closed set is upper semicontinuous. The pointwise infimum of any family of upper semicontinuous functions is upper semicontinuous.
:::

::: proposition
Let $X$ be a topological space and $f : X \to [-\infty, \infty]$. The function $f$ is continuous iff it is both lower semicontinuous and upper semicontinuous.
:::

## Metric Spaces
::: definition:Metric
Let $X$ be a set and $\rho : X\times X \to [0,\infty)$. The map $\rho$ is a metric if the following hold for any $x,y,z \in X$:
- $\rho(x,y) = 0$ iff $x = y$.
- $\rho(x,y) = \rho(y,x)$.
- $\rho(x,y) \leq \rho(x,z) + \rho(z,y)$.
:::

::: definition:Metric Space
Let $X$ be a set and $\rho$ be a metric on $X$. The pair $(X,\rho)$ is a metric space. Its topology is generated by the open balls $B_\rho(x,r) := \{y \in X:\rho(x,y) < r\}$ for $x \in X$ and $r > 0$.
:::

::: definition:Convergence in a Metric Space
Let $(X, \rho)$ be a metric space, $(x_n)_{n \geq 1}$ be a sequence in $X$, and $x \in X$. The sequence converges to $x$, denoted by $x_n \to x$, if $\rho(x_n, x) \to 0$ as $n \to \infty$.
:::

::: definition:Cauchy Sequence
Let $(X, \rho)$ be a metric space and $(x_n)_{n \geq 1}$ be a sequence in $X$. The sequence is Cauchy if for any $\epsilon > 0$, there exists $N \geq 1$ s.t. $\rho(x_m, x_n) < \epsilon$ for any $m, n \geq N$.
:::

::: definition:Complete Metric Space
Let $(X, \rho)$ be a metric space. The space is complete if every Cauchy sequence in $X$ converges to an element of $X$.
::: ^complete-metric-space

::: note
Every metric space is Hausdorff under its metric topology. In particular, $\mathbb{R}^n$ with its Euclidean topology is a locally compact Hausdorff space.
:::

::: proposition
Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces, $f : X \to Y$ be continuous, and $X_0 \subseteq X$. Assume $X$ is complete, $X_0$ is dense in $X$, $f(X_0)$ is dense in $Y$, and $d_Y(f(x),f(x')) = d_X(x,x')$ for any $x,x' \in X_0$. The map $f$ is surjective and $d_Y(f(x),f(x')) = d_X(x,x')$ for any $x,x' \in X$.
:::
