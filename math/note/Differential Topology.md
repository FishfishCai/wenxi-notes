::: definition:Smooth Map on Open Sets
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets. A map $f : U \to V$ is smooth if all partial derivatives of all orders of $f$ exist and are continuous.
:::

::: definition:Smooth Map on Subsets
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$. A map $f : M \to N$ is smooth if for each $x \in M$ there exist an open set $U \subset \mathbb{R}^k$ containing $x$ and a smooth map $F : U \to \mathbb{R}^l$ s.t. $F = f$ on $U \cap M$. Such a map $F$ is a local smooth extension of $f$ near $x$.
:::

::: proposition
Let $M$, $N$, and $P$ be subsets of Euclidean spaces and $f : M \to N$ and $g : N \to P$ be smooth maps. The composition $g \circ f$ is smooth.
:::

::: definition:Diffeomorphism
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$. A map $f : M \to N$ is a diffeomorphism if $f$ is a homeomorphism and both $f$ and $f^{-1}$ are smooth.
:::

::: definition:Smooth manifold
Let $M \subset \mathbb{R}^k$ and $m\geq 0$. $M$ is a smooth manifold of dimension $m$ if for each $x \in M$ there exists an open neighborhood $W \subset \mathbb{R}^k$ of $x$ s.t. $W \cap M$ is diffeomorphic to an open set $U \subset \mathbb{R}^m$. Here smooth manifolds are embedded in Euclidean spaces and have no boundary.
:::

::: definition:Parametrization
Let $M \subset \mathbb{R}^k$ be a smooth manifold of dimension $m$, $x \in M$, $W \subset \mathbb{R}^k$ be an open neighborhood of $x$, and $U \subset \mathbb{R}^m$ be open. A parametrization of $M$ near $x$ is a diffeomorphism $g : U \to W \cap M$.
:::

::: definition:Coordinate
Let $M \subset \mathbb{R}^k$ be a smooth manifold and $g : U \to W \cap M$ be a parametrization. The associated coordinate system is the inverse diffeomorphism $g^{-1} : W \cap M \to U$.
:::

::: definition:Derivative in Euclidean Space
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets, $f : U \to V$ be smooth, and $x \in U$. The derivative of $f$ at $x$ is the map $df_x : \mathbb{R}^k \to \mathbb{R}^l$ defined by $df_x(h) = \underset{t \to 0}{\lim} \frac{f(x + t h) - f(x)}{t}$ for any $h \in \mathbb{R}^k$.
:::

::: proposition
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets, $f : U \to V$ be smooth, and $x \in U$. The derivative $df_x : \mathbb{R}^k \to \mathbb{R}^l$ is linear.
:::

::: proposition
Let $U$, $V$, and $W$ be open sets in Euclidean spaces, $f : U \to V$ and $g : V \to W$ be smooth maps, and $x \in U$. Set $y = f(x)$. The identity $d(g \circ f)_x = dg_y \circ df_x$ holds.
:::

::: proposition
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets and $x \in U$. If there exists a diffeomorphism $f : U \to V$, then $k = l$ and $df_x$ is nonsingular.
:::

::: proposition
Let $M$ be a nonempty smooth manifold. The dimension of $M$ is uniquely determined.
:::

::: definition:Tangent space
Let $M \subset \mathbb{R}^k$ be a smooth manifold of dimension $m$, $x \in M$, $U \subset \mathbb{R}^m$ be open, $g : U \to \mathbb{R}^k$ be smooth, and $u \in U$. Assume $g$ parametrizes a neighborhood of $x$ in $M$ and $g(u) = x$. The tangent space of $M$ at $x$ is $TM_x = dg_u(\mathbb{R}^m)$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ be a smooth manifold of dimension $m$ and $x \in M$. The tangent space $TM_x$ has dimension $m$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ be a smooth manifold and $x \in M$. The tangent space $TM_x$ does not depend on the choice of parametrization.
:::

::: definition:Derivative on Manifolds
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds, $f : M \to N$ be smooth, $x \in M$, and $F$ be a local smooth extension of $f$ near $x$. Set $y = f(x)$. The derivative of $f$ at $x$ is the map $df_x : TM_x \to TN_y$ given by $df_x = \left.dF_x\right|_{TM_x}$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds, $f : M \to N$ be smooth, $x \in M$, and $F$ be a local smooth extension of $f$ near $x$. The image $dF_x(TM_x)$ is contained in $TN_{f(x)}$, and the restriction $\left.dF_x\right|_{TM_x}$ does not depend on the choice of $F$.
:::

::: proposition
Let $M$, $N$, and $P$ be smooth manifolds, $f : M \to N$ and $g : N \to P$ be smooth, and $x \in M$. Set $y = f(x)$. The identity $d(g \circ f)_x = dg_y \circ df_x$ holds.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds and $x \in M$. If $f : M \to N$ is a diffeomorphism, then $\dim M = \dim N$ and $df_x : TM_x \to TN_{f(x)}$ is an isomorphism.
:::

::: definition:Regular point
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $x \in M$. The point $x$ is a regular point of $f$ if $df_x$ is surjective.
:::

::: definition:Critical point
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $x \in M$. The point $x$ is a critical point of $f$ if $df_x$ is not surjective.
:::

::: definition:Regular value
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $y \in N$. The point $y$ is a regular value of $f$ if $f^{-1}(y)$ contains only regular points. This includes the case $y \notin f(M)$, where $f^{-1}(y)$ is empty.
:::

::: definition:Critical value
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $y \in N$. The point $y$ is a critical value of $f$ if $f^{-1}(y)$ contains at least one critical point.
:::

::: proposition
Let $M$ and $N$ be smooth manifolds of the same dimension and $f : M \to N$ be smooth. Assume $M$ is compact. If $y \in N$ is a regular value of $f$, then $f^{-1}(y)$ is finite.
:::

::: proposition
Let $M$ and $N$ be smooth manifolds of the same dimension, $f : M \to N$ be smooth, and $y \in N$. Assume $M$ is compact and $y$ is a regular value of $f$. Set $\#S$ to denote the cardinality of a set $S$. There exists an open neighborhood $V \subset N$ of $y$ s.t. $\#f^{-1}(y') = \#f^{-1}(y)$ for any $y' \in V$.
:::
