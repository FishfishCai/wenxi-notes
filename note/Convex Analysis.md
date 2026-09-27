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

## Euclidean Projection and Separation
::: definition:Distance and Projection
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$ be nonempty, and $y \in \mathcal{E}$. Set $\operatorname{dist}_Q(y) := \underset{x \in Q}{\inf}\|x - y\|$. The projection set is $\operatorname{proj}_Q(y) := \{z \in Q : \|z - y\| = \operatorname{dist}_Q(y)\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$ be nonempty. $|\operatorname{dist}_Q(y) - \operatorname{dist}_Q(w)| \leq \|y - w\|$ for any $y, w \in \mathcal{E}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and closed, then $\operatorname{proj}_Q(y) \neq \emptyset$ for any $y \in \mathcal{E}$.
:::

::: theorem:Projection onto a Closed Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The set $\operatorname{proj}_Q(y)$ consists of exactly one point for any $y \in \mathcal{E}$. For $y \in \mathcal{E}$ and $z \in Q$, $z = \operatorname{proj}_Q(y)$ iff $\langle y - z, x - z\rangle \leq 0$ for any $x \in Q$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. Set $p := \operatorname{proj}_Q(y)$ and $q := \operatorname{proj}_Q(w)$ for $y, w \in \mathcal{E}$. $\|p - q\|^2 \leq \langle p - q, y - w\rangle$ and $\|p - q\| \leq \|y - w\|$.
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
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$ be nonempty. Set $F_Q := \{(a, b) \in \mathcal{E} \times \mathbb{R} : \langle a, x\rangle \leq b \text{ for any } x \in Q\}$. $\operatorname{cl}(\operatorname{conv}(Q)) = \bigcap_{(a,b) \in F_Q}\{x \in \mathcal{E} : \langle a, x\rangle \leq b\}$.
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
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$ be a cone. The polar cone of $K$ is $K^\circ := \{v \in \mathcal{E} : \langle v, x\rangle \leq 0 \text{ for any } x \in K\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K, K_1, K_2 \subseteq \mathcal{E}$ be cones. $K^\circ$ is a closed convex cone, $K \subseteq (K^\circ)^\circ$, and $K_1 \subseteq K_2$ implies $K_2^\circ \subseteq K_1^\circ$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $L \subseteq \mathcal{E}$ be a linear subspace. $L^\circ = L^\perp$.
:::

::: theorem:Double Polar Theorem for Cones
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$ be a nonempty cone. $(K^\circ)^\circ = \operatorname{cl}(\operatorname{conv}(K))$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K \subseteq \mathcal{E}$ be a nonempty cone. $K = (K^\circ)^\circ$ iff $K$ is closed and convex.
:::

::: lemma:Polar of a Product
Let $\mathcal{E}_1$ and $\mathcal{E}_2$ be finite-dimensional real Euclidean spaces, and let $K_i \subseteq \mathcal{E}_i$ be nonempty cones for $i \in \{1, 2\}$. $(K_1 \times K_2)^\circ = K_1^\circ \times K_2^\circ$.
:::

::: theorem:Polarity under a Linear Map
Let $\mathcal{E}$ and $\mathcal{Y}$ be finite-dimensional real Euclidean spaces, $A : \mathcal{E} \to \mathcal{Y}$ be linear, and $K \subseteq \mathcal{E}$ be a nonempty cone. Set $A^*$ to be the adjoint of $A$. $(AK)^\circ = (A^*)^{-1}(K^\circ)$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $K_1, K_2 \subseteq \mathcal{E}$ be nonempty cones. $(K_1 + K_2)^\circ = K_1^\circ \cap K_2^\circ$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $C_1, C_2 \subseteq \mathcal{E}$ be nonempty closed convex cones. $(C_1 \cap C_2)^\circ = \operatorname{cl}(C_1^\circ + C_2^\circ)$.
:::

::: definition:Polar Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$ contain $0$. Set $K := \{(\lambda x, \lambda) \in \mathcal{E} \times \mathbb{R} : x \in Q, \lambda \geq 0\}$. The polar set of $Q$ is $Q^\circ := \{v \in \mathcal{E} : (v, -1) \in K^\circ\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$ contain $0$. $Q^\circ = \{v \in \mathcal{E} : \langle v, x\rangle \leq 1 \text{ for any } x \in Q\}$. In particular, $Q^\circ$ is closed and convex and contains $0$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q_1, Q_2 \subseteq \mathcal{E}$ contain $0$. If $Q_1 \subseteq Q_2$, then $Q_2^\circ \subseteq Q_1^\circ$. If $Q_1$ is a cone, its polar set equals its polar cone.
:::

::: theorem:Double Polar Theorem for Sets
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $Q \subseteq \mathcal{E}$ contain $0$. $(Q^\circ)^\circ = \operatorname{cl}(\operatorname{conv}(Q))$.
:::

::: definition:Dual Norm
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space and $\rho$ be a norm on $\mathcal{E}$. The dual norm is $\rho^*(v) := \underset{\rho(x) \leq 1}{\sup}\langle v, x\rangle$ for any $v \in \mathcal{E}$.
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
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. The normal cone to $Q$ at $\bar{x}$ is $N_Q(\bar{x}) := \{v \in \mathcal{E} : \langle v, x - \bar{x}\rangle \leq o(\|x - \bar{x}\|) \text{ as } x \to \bar{x} \text{ in } Q\}$.
:::

::: lemma:Tangent-Normal Polarity
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x}) = T_Q(\bar{x})^\circ$.
:::

::: corollary
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x})$ is a closed convex cone and $N_Q(\bar{x})^\circ = \operatorname{cl}(\operatorname{conv}(T_Q(\bar{x})))$. Hence $T_Q(\bar{x}) = N_Q(\bar{x})^\circ$ iff $T_Q(\bar{x})$ is convex.
:::

::: lemma:Normal Cone to a Convex Set
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. $N_Q(\bar{x}) = \{v \in \mathcal{E} : \langle v, x - \bar{x}\rangle \leq 0 \text{ for any } x \in Q\}$.
:::

::: lemma:Normals and Projections
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$, $\bar{x} \in Q$, and $v \in \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The following are equivalent: $v \in N_Q(\bar{x})$; $\bar{x} \in \underset{x \in Q}{\operatorname{argmax}}\langle v, x\rangle$; $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for any $\lambda \geq 0$; and $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for some $\lambda > 0$.
:::

::: lemma:Normal Cone to a Convex Cone
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $K \subseteq \mathcal{E}$ be a convex cone, and $x \in K$. $N_K(x) = K^\circ \cap \{x\}^\perp$.
:::

::: lemma:Normal Cone of an Interior Point
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$ be convex, and $x \in Q$. $x \in \operatorname{int}(Q)$ iff $N_Q(x) = \{0\}$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$ be convex, and $x \in Q$. Set $S := \operatorname{aff}(Q) - x$. $x \in \operatorname{ri}(Q)$ iff $N_Q(x) = S^\perp$.
:::

::: proposition
Let $\mathcal{E}$ be a finite-dimensional real Euclidean space, $Q \subseteq \mathcal{E}$ be convex, and $x \in Q$. The halfspaces supporting $Q$ at $x$ are exactly $\{y \in \mathcal{E} : \langle v, y\rangle \leq \langle v, x\rangle\}$ for $v \in N_Q(x)\setminus\{0\}$.
:::
