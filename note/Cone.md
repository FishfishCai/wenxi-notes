::: definition:Cone
Let $K \subseteq \mathcal{E}$. $K$ is a cone if $\lambda K \subseteq K$ for any $\lambda \geq 0$.
:::

::: proposition
Let $K \subseteq \mathcal{E}$. $K$ is a convex cone iff $\lambda x + \mu y \in K$ for any $x, y \in K$ and $\lambda, \mu \geq 0$.
:::

::: proposition
Let $K \subseteq \mathcal{E}$. If $K$ is a convex cone, then $\operatorname{aff}(K) = K - K$.
:::

::: proposition
Minkowski sums, intersections, Cartesian products, linear images and linear preimages of convex cones are convex cones.
:::

::: definition:Polar Cone
Let $K \subseteq \mathcal{E}$. Assume $K$ is a cone. The polar cone of $K$ is $K^\circ := \{v \in \mathcal{E} : \langle v, x\rangle \leq 0 \text{ for any } x \in K\}$.
:::

::: proposition
Let $K \subseteq \mathcal{E}$. Assume $K$ is a cone. $K^\circ$ is a closed convex cone.
:::

::: proposition
Let $L \subseteq \mathcal{E}$. Assume $L$ is a linear subspace. $L^\circ = L^\perp$.
:::

::: proposition
Let $K_1, K_2 \subseteq \mathcal{E}$. Assume $K_1$ and $K_2$ are cones. If $K_1 \subseteq K_2$, then $K_2^\circ \subseteq K_1^\circ$.
:::

::: theorem:Double Polar Theorem for Cones
Let $K \subseteq \mathcal{E}$. Assume $K$ is a nonempty cone. $(K^\circ)^\circ = \operatorname{cl}(\operatorname{conv}(K))$.
:::

*Proof.*
$$
\begin{aligned}
(K^\circ)^\circ &= \{y \in \mathcal{E} : \langle y, a\rangle \leq 0 \text{ for any } a \in K^\circ\}\\
&= \bigcap_{a \in K^\circ}\{y \in \mathcal{E} : \langle y, a\rangle \leq 0\}\\
&= \bigcap_{a : \langle a, x\rangle \leq 0 \text{ for any } x \in K}\{y \in \mathcal{E} : \langle y, a\rangle \leq 0\}\\
&= \bigcap_{(a, b) : \langle a, x\rangle \leq b \text{ for any } x \in K}\{y \in \mathcal{E} : \langle y, a\rangle \leq b\}\\
&= \operatorname{cl}(\operatorname{conv}(K)),
\end{aligned}
$$
where the last equality follows from [[Projection and Separation#^dual-description-of-the-closed-convex-hull|Theorem 10 (Dual Description of the Closed Convex Hull)]].

::: lemma:Polar of a Product
Let $K_i \subseteq \mathcal{E}_i$ for $i \in \{1, 2\}$. Assume $K_1$ and $K_2$ are nonempty cones. $(K_1 \times K_2)^\circ = K_1^\circ \times K_2^\circ$.
:::

::: theorem:Polarity under a Linear Map
Let $A : \mathcal{E} \to \mathcal{Y}$, and $K \subseteq \mathcal{E}$. Assume $A$ is linear and $K$ is a nonempty cone. Set $A^*$ to be the adjoint of $A$. $(AK)^\circ = (A^*)^{-1}(K^\circ)$.
:::

::: corollary
Let $K_1, K_2 \subseteq \mathcal{E}$. Assume $K_1$ and $K_2$ are nonempty cones. $(K_1 + K_2)^\circ = K_1^\circ \cap K_2^\circ$.
:::

::: corollary
Let $K_1, K_2 \subseteq \mathcal{E}$. Assume $K_1$ and $K_2$ are nonempty closed convex cones. $(K_1 \cap K_2)^\circ = \operatorname{cl}(K_1^\circ + K_2^\circ)$.
:::
