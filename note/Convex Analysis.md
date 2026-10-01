## Convex Set
::: definition:Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. $Q$ is convex if $[x, y] \subseteq Q$ for any $x, y \in Q$.
:::

::: proposition
Nonnegative scaling, Minkowski sums, intersections, Cartesian products, linear images and linear preimages of convex sets are convex sets.
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

## Euclidean Projection and Separation
::: definition:Distance and Projection
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}$. Assume $Q$ is nonempty. Set $\operatorname{dist}_Q(y) := \underset{x \in Q}{\inf}\|x - y\|$. The projection set is $\operatorname{proj}_Q(y) := \{z \in Q : \|z - y\| = \operatorname{dist}_Q(y)\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. $|\operatorname{dist}_Q(y) - \operatorname{dist}_Q(w)| \leq \|y - w\|$ for any $y, w \in \mathcal{E}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and closed, then $\operatorname{proj}_Q(y) \neq \emptyset$ for any $y \in \mathcal{E}$.
:::

::: theorem:Projection onto a Closed Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The set $\operatorname{proj}_Q(y)$ consists of exactly one point for any $y \in \mathcal{E}$. For $y \in \mathcal{E}$ and $z \in Q$, $z = \operatorname{proj}_Q(y)$ iff $\langle y - z, x - z\rangle \leq 0$ for any $x \in Q$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. $\|\operatorname{proj}_Q(y) - \operatorname{proj}_Q(w)\|^2 \leq \langle \operatorname{proj}_Q(y) - \operatorname{proj}_Q(w), y - w\rangle$ for any $y, w \in \mathcal{E}$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. $\|\operatorname{proj}_Q(y) - \operatorname{proj}_Q(w)\| \leq \|y - w\|$ for any $y, w \in \mathcal{E}$.
:::

::: definition:Strict Separation of a Point and a Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}$. A hyperplane $\{x \in \mathcal{E} : \langle a, x\rangle = b\}$ strictly separates $y$ from $Q$ if $a \in \mathcal{E}\setminus\{0\}$, $b \in \mathbb{R}$, and $\langle a, x\rangle \leq b < \langle a, y\rangle$ for any $x \in Q$.
:::

::: theorem:Strict Separation
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}\setminus Q$. Assume $Q$ is nonempty, closed, and convex. There exist $a \in \mathcal{E}\setminus\{0\}$ and $b \in \mathbb{R}$ s.t. $\langle a, x\rangle \leq b < \langle a, y\rangle$ for any $x \in Q$.
:::

::: definition:Supporting Halfspace
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $x \in \operatorname{cl}(Q)$. A halfspace $H = \{z \in \mathcal{E} : \langle a, z\rangle \leq b\}$ supports $Q$ at $x$ if $a \in \mathcal{E}\setminus\{0\}$, $b \in \mathbb{R}$, $Q \subseteq H$, and $\langle a, x\rangle = b$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $x \in \operatorname{cl}(Q)$. Assume $Q$ is convex. A supporting halfspace to $Q$ at $x$ exists iff $x \in \operatorname{bd}(Q)$.
:::

::: theorem:Dual Description of the Closed Convex Hull
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. Set $F_Q := \{(a, b) \in \mathcal{E} \times \mathbb{R} : \langle a, x\rangle \leq b \text{ for any } x \in Q\}$. $\operatorname{cl}(\operatorname{conv}(Q)) = \bigcap_{(a,b) \in F_Q}\{x \in \mathcal{E} : \langle a, x\rangle \leq b\}$.
:::

## Cones and Polarity
::: definition:Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. $K$ is a cone if $\lambda K \subseteq K$ for any $\lambda \geq 0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. $K$ is a convex cone iff $\lambda x + \mu y \in K$ for any $x, y \in K$ and $\lambda, \mu \geq 0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. If $K$ is a convex cone, then $\operatorname{aff}(K) = K - K$.
:::

::: proposition
Intersections, Cartesian products, linear images, linear preimages, and Minkowski sums of convex cones are convex cones.
:::

::: definition:Polar Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. Assume $K$ is a cone. The polar cone of $K$ is $K^\circ := \{v \in \mathcal{E} : \langle v, x\rangle \leq 0 \text{ for any } x \in K\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. Assume $K$ is a cone. $K^\circ$ is a closed convex cone.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. Assume $K$ is a cone. $K \subseteq (K^\circ)^\circ$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K_1, K_2 \subseteq \mathcal{E}$. Assume $K_1$ and $K_2$ are cones. If $K_1 \subseteq K_2$, then $K_2^\circ \subseteq K_1^\circ$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $L \subseteq \mathcal{E}$. Assume $L$ is a linear subspace. $L^\circ = L^\perp$.
:::

::: theorem:Double Polar Theorem for Cones
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. Assume $K$ is a nonempty cone. $(K^\circ)^\circ = \operatorname{cl}(\operatorname{conv}(K))$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$. Assume $K$ is a nonempty cone. $K = (K^\circ)^\circ$ iff $K$ is closed and convex.
:::

::: lemma:Polar of a Product
Let $\mathcal{E}_1$ and $\mathcal{E}_2$ be finite-dimensional real Euclidean spaces, and $K_i \subseteq \mathcal{E}_i$ for $i \in \{1, 2\}$. Assume $K_1$ and $K_2$ are nonempty cones. $(K_1 \times K_2)^\circ = K_1^\circ \times K_2^\circ$.
:::

::: theorem:Polarity under a Linear Map
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, $A : \mathcal{E} \to \mathcal{Y}$, and $K \subseteq \mathcal{E}$. Assume $A$ is linear and $K$ is a nonempty cone. Set $A^*$ to be the adjoint of $A$. $(AK)^\circ = (A^*)^{-1}(K^\circ)$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K_1, K_2 \subseteq \mathcal{E}$. Assume $K_1, K_2$ are nonempty cones. $(K_1 + K_2)^\circ = K_1^\circ \cap K_2^\circ$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $C_1, C_2 \subseteq \mathcal{E}$. Assume $C_1, C_2$ are nonempty closed convex cones. $(C_1 \cap C_2)^\circ = \operatorname{cl}(C_1^\circ + C_2^\circ)$.
:::

::: definition:Polar Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $0 \in Q$. Set $K := \{(\lambda x, \lambda) \in \mathcal{E} \times \mathbb{R} : x \in Q, \lambda \geq 0\}$. The polar set of $Q$ is $Q^\circ := \{v \in \mathcal{E} : (v, -1) \in K^\circ\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $0 \in Q$. $Q^\circ = \{v \in \mathcal{E} : \langle v, x\rangle \leq 1 \text{ for any } x \in Q\}$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $0 \in Q$. $Q^\circ$ is closed and convex and contains $0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q_1, Q_2 \subseteq \mathcal{E}$. Assume $0 \in Q_1 \cap Q_2$. If $Q_1 \subseteq Q_2$, then $Q_2^\circ \subseteq Q_1^\circ$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $0 \in Q$. If $Q$ is a cone, then its polar set equals its polar cone.
:::

::: theorem:Double Polar Theorem for Sets
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $0 \in Q$. $(Q^\circ)^\circ = \operatorname{cl}(\operatorname{conv}(Q))$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $\rho$ be a norm on $\mathcal{E}$. Set $B_\rho := \{x \in \mathcal{E} : \rho(x) \leq 1\}$ and $B_{\rho^*} := \{v \in \mathcal{E} : \rho^*(v) \leq 1\}$. $B_\rho^\circ = B_{\rho^*}$.
:::

## Tangent and Normal Cones
::: definition:Tangent Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. The tangent cone to $Q$ at $\bar{x}$ is $T_Q(\bar{x}) := \{w \in \mathcal{E} : \text{there exist } x_i \to \bar{x} \text{ in } Q \text{ and } \tau_i \downarrow 0 \text{ s.t. } \tau_i^{-1}(x_i - \bar{x}) \to w\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $T_Q(\bar{x})$ is a closed cone.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. If $Q$ is convex, then $T_Q(\bar{x}) = \operatorname{cl}(\mathbb{R}_+(Q - \bar{x}))$, which is a convex cone.
:::

::: definition:Normal Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. The normal cone to $Q$ at $\bar{x}$ is
$$
N_Q(\bar{x}) := \left\{v \in \mathcal{E} : \underset{\substack{x \to \bar{x} \\ x \in Q,\ x \neq \bar{x}}}{\limsup}\left\langle v, \frac{x - \bar{x}}{\|x - \bar{x}\|}\right\rangle \leq 0\right\}.
$$
:::

::: lemma:Tangent-Normal Polarity
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x}) = T_Q(\bar{x})^\circ$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x})$ is a closed convex cone.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x})^\circ = \operatorname{cl}(\operatorname{conv}(T_Q(\bar{x})))$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $T_Q(\bar{x}) = N_Q(\bar{x})^\circ$ iff $T_Q(\bar{x})$ is convex.
:::

::: lemma:Normal Cone to a Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. $N_Q(\bar{x}) = \{v \in \mathcal{E} : \langle v, x - \bar{x}\rangle \leq 0 \text{ for any } x \in Q\}$.
:::

::: lemma:Normals and Projections
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, $\bar{x} \in Q$, and $v \in \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The following are equivalent: $v \in N_Q(\bar{x})$; $\bar{x} \in \underset{x \in Q}{\operatorname{argmax}}\langle v, x\rangle$; $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for any $\lambda \geq 0$; and $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for some $\lambda > 0$.
:::

::: lemma:Normal Cone to a Convex Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $K \subseteq \mathcal{E}$, and $x \in K$. Assume $K$ is a convex cone. $N_K(x) = K^\circ \cap \{x\}^\perp$.
:::

::: lemma:Normal Cone of an Interior Point
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $x \in Q$. Assume $Q$ is convex. $x \in \operatorname{int}(Q)$ iff $N_Q(x) = \{0\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $x \in Q$. Assume $Q$ is convex. Set $S := \operatorname{aff}(Q) - x$. $x \in \operatorname{ri}(Q)$ iff $N_Q(x) = S^\perp$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $x \in Q$. Assume $Q$ is convex. The halfspaces supporting $Q$ at $x$ are exactly $\{y \in \mathcal{E} : \langle v, y\rangle \leq \langle v, x\rangle\}$ for $v \in N_Q(x)\setminus\{0\}$.
:::

## Convex Functions
::: definition:Effective Domain
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \mathbb{R} \cup \{-\infty, +\infty\}$. Set $\overline{\mathbb{R}} := \mathbb{R} \cup \{-\infty, +\infty\}$. The effective domain of $f$ is $\operatorname{dom} f := \{x \in \mathcal{E} : f(x) < +\infty\}$.
:::

::: definition:Epigraph
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. The epigraph of $f$ is $\operatorname{epi} f := \{(x, r) \in \mathcal{E} \times \mathbb{R} : f(x) \leq r\}$.
:::

::: definition:Proper Function
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is proper if $\operatorname{dom} f \neq \emptyset$ and $f(x) > -\infty$ for any $x \in \mathcal{E}$.
:::

::: definition:Convex Function
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is convex if $\operatorname{epi} f$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper. The function $f$ is convex iff $f(tx + (1 - t)y) \leq t f(x) + (1 - t)f(y)$ for any $x, y \in \mathcal{E}$ and $t \in [0, 1]$, with $0 \cdot (+\infty) = 0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. $\operatorname{dom} f$ is convex.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. The sublevel set $\{x \in \mathcal{E} : f(x) \leq \alpha\}$ is convex for any $\alpha \in \mathbb{R}$.
:::

::: definition:Quasiconvex Function
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. The function $f$ is quasiconvex if $\{x \in \mathcal{E} : f(x) \leq \alpha\}$ is convex for any $\alpha \in \mathbb{R}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. If $f$ is convex, then $f$ is quasiconvex. The converse does not hold in general.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. If there exists $\bar{x} \in \operatorname{ri}(\operatorname{dom} f)$ s.t. $f(\bar{x}) > -\infty$, then $f$ is proper.
:::

::: proposition:Jensen's Inequality
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper and convex. $f\left(\sum_{i=1}^k \lambda_i x_i\right) \leq \sum_{i=1}^k \lambda_i f(x_i)$ for any $k \in \mathbb{Z}_+$, $x_1, \ldots, x_k \in \mathcal{E}$, and $\lambda \in \Delta_k$, with $0 \cdot (+\infty) = 0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $I$ be an index set, and $f_i : \mathcal{E} \to \overline{\mathbb{R}}$ for $i \in I$. Assume each $f_i$ is convex. Set $f(x) := \underset{i \in I}{\sup} f_i(x)$ for $x \in \mathcal{E}$, with $\sup \emptyset = -\infty$. The function $f$ is convex.
:::

::: definition:Positive Homogeneity
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $h : \mathcal{E} \to \overline{\mathbb{R}}$. The function $h$ is positively homogeneous if $\operatorname{epi} h$ is a cone.
:::

::: definition:Sublinear Function
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $h : \mathcal{E} \to \overline{\mathbb{R}}$. The function $h$ is sublinear if it is convex and positively homogeneous.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $h : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $h$ is proper. The function $h$ is sublinear iff $h(\lambda x + \mu y) \leq \lambda h(x) + \mu h(y)$ for any $x, y \in \mathcal{E}$ and $\lambda, \mu \geq 0$, with $0 \cdot (+\infty) = 0$.
:::
