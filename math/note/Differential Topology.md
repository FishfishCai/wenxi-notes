# Differential Topology
::: definition:Smooth
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets. A map $f : U \to V$ is smooth if all partial derivatives of $f$ exist and are continuous. More generally, let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be arbitrary subsets. A map $f : M \to N$ is smooth if for each $x \in M$ there exist an open set $U \subset \mathbb{R}^k$ containing $x$ and a smooth map $F : U \to \mathbb{R}^l$ that coincides with $f$ on $U \cap M$; such a map $F$ is an extension of $f$.
:::

::: proposition
Let $f$ and $g$ be smooth maps s.t. the composition $g \circ f$ is defined. Then $g \circ f$ is smooth.
:::

::: definition:Diffeomorphism
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$. A map $f : M \to N$ is a diffeomorphism if $f$ is a homeomorphism and both $f$ and $f^{-1}$ are smooth.
:::

::: definition:Smooth manifold
Let $M \subset \mathbb{R}^k$. $M$ is a smooth manifold of dimension $m$ if for each $x \in M$ there exists a neighborhood $W$ of $x$ s.t. $W \cap M$ is diffeomorphic to an open set $U \subset \mathbb{R}^m$.
:::

::: definition:Parametrization
Let $M \subset \mathbb{R}^k$ be a smooth manifold, $x \in M$, and $W$ be a neighborhood of $x$ s.t. $W \cap M$ is diffeomorphic to an open set $U \subset \mathbb{R}^m$. A parametrization of $M$ near $x$ is the diffeomorphism $g : U \to W \cap M$.
:::

::: definition:Coordinate
Let $M \subset \mathbb{R}^k$ be a smooth manifold and $g : U \to W \cap M$ be a parametrization. The associated coordinate system is the inverse diffeomorphism $g^{-1} : W \cap M \to U$.
:::

## Tangent Space
::: definition:Derivative
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets, $f : U \to V$ be smooth, and $x \in U$. The derivative of $f$ at $x$ is the map $df_x : \mathbb{R}^k \to \mathbb{R}^l$ defined by $df_x(h) = \underset{t \to 0}{\lim} \frac{f(x + t h) - f(x)}{t}$ for any $h \in \mathbb{R}^k$.
:::

::: proposition
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets, $f : U \to V$ be smooth, and $x \in U$. The derivative $df_x : \mathbb{R}^k \to \mathbb{R}^l$ is linear.
:::

::: proposition
Let $f : U \to V$ and $g : V \to W$ be smooth maps between open sets of Euclidean spaces, $x \in U$, and $y = f(x)$. Then $d(g \circ f)_x = dg_y \circ df_x$.
:::

::: proposition
Let $U \subset \mathbb{R}^k$ and $V \subset \mathbb{R}^l$ be open sets and $x \in U$. If there exists a diffeomorphism $f : U \to V$, then $k = l$ and $df_x$ is nonsingular.
:::

::: proposition
Let $M$ be a connected smooth manifold. The dimension of $M$ is well-defined.
:::

::: definition:Tangent space
Let $M \subset \mathbb{R}^k$ be a smooth manifold of dimension $m$, $x \in M$, $U \subset \mathbb{R}^m$ be open, and $g : U \to M$ be a parametrization with $g(u) = x$. The tangent space of $M$ at $x$ is $TM_x = \text{Image}\, dg_u(\mathbb{R}^m)$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ be a smooth manifold of dimension $m$ and $x \in M$. The tangent space $TM_x$ has dimension $m$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ be a smooth manifold and $x \in M$. The tangent space $TM_x$ does not depend on the choice of parametrization.
:::

::: definition:Derivative
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds, $f : M \to N$ be smooth, $x \in M$, $y = f(x)$, and $F$ be a smooth extension of $f$ near $x$. The derivative of $f$ at $x$ is the map $df_x : TM_x \to TN_y$ given by $df_x = dF_x$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds, $f : M \to N$ be smooth, and $x \in M$. The derivative $df_x$ does not depend on the choice of extension $F$.
:::

::: proposition
Let $M$, $N$, $P$ be smooth manifolds, $f : M \to N$ and $g : N \to P$ be smooth, $x \in M$, and $y = f(x)$. Then $d(g \circ f)_x = dg_y \circ df_x$.
:::

::: proposition
Let $M \subset \mathbb{R}^k$ and $N \subset \mathbb{R}^l$ be smooth manifolds and $x \in M$. If there exists a diffeomorphism $f : M \to N$, then $k = l$ and $df_x$ is an isomorphism.
:::

## Regular Value
::: definition:Regular point
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $x \in M$. The point $x$ is a regular point of $f$ if $df_x$ is surjective.
:::

::: definition:Regular value
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $y \in N$. The point $y$ is a regular value of $f$ if $f^{-1}(y)$ contains only regular points.
:::

::: proposition
Let $M$ and $N$ be smooth manifolds of the same dimension and $f : M \to N$ be smooth. Assume $M$ is compact. If $y \in N$ is a regular value of $f$, then $f^{-1}(y)$ is finite.
:::

::: note
$\#f^{-1}(y)$ denotes the number of points in $f^{-1}(y)$.
:::

::: proposition
Let $M$ and $N$ be smooth manifolds of the same dimension, $f : M \to N$ be smooth, and $y \in N$ be a regular value of $f$. Assume $M$ is compact. There exists a neighborhood $V \subset N$ of $y$ s.t. $\#f^{-1}(y') = \#f^{-1}(y)$ for any $y' \in V$.
:::

::: definition:Critical point
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $x \in M$. The point $x$ is a critical point of $f$ if $df_x$ is not surjective.
:::

::: definition:Critical value
Let $M$ and $N$ be smooth manifolds, $f : M \to N$ be smooth, and $y \in N$. The point $y$ is a critical value of $f$ if $f^{-1}(y)$ contains at least one critical point.
:::
