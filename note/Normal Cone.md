::: definition:Tangent Cone
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. The tangent cone to $Q$ at $\bar{x}$ is $T_Q(\bar{x}) := \{w \in \mathcal{E} : \text{there exist } x_i \to \bar{x} \text{ in } Q \text{ and } \tau_i \downarrow 0 \text{ s.t. } \frac{x_i - \bar{x}}{\tau_i} \to w\}$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $T_Q(\bar{x})$ is a closed cone.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. If $Q$ is convex, then $T_Q(\bar{x}) = \operatorname{cl}(\mathbb{R}_+(Q - \bar{x}))$, which is a convex cone.
::: ^tangent-cone-of-a-convex-set

::: definition:Normal Cone
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. The normal cone to $Q$ at $\bar{x}$ is
$$
N_Q(\bar{x}) := \left\{v \in \mathcal{E} : \underset{\substack{x \to \bar{x} \\ x \in Q,\ x \neq \bar{x}}}{\limsup}\left\langle v, \frac{x - \bar{x}}{\|x - \bar{x}\|}\right\rangle \leq 0\right\}.
$$
:::

::: lemma:Tangent-Normal Polarity
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x}) = T_Q(\bar{x})^\circ$.
:::

::: corollary
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x})$ is a closed convex cone.
:::

::: corollary
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $N_Q(\bar{x})^\circ = \operatorname{cl}(\operatorname{conv}(T_Q(\bar{x})))$.
:::

::: corollary
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. $T_Q(\bar{x}) = N_Q(\bar{x})^\circ$ iff $T_Q(\bar{x})$ is convex.
:::

::: lemma:Normal Cone to a Convex Set
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. $N_Q(\bar{x}) = \{v \in \mathcal{E} : \langle v, x - \bar{x}\rangle \leq 0 \text{ for any } x \in Q\}$.
:::

*Proof.*
Take the polar of [[#^tangent-cone-of-a-convex-set|Proposition 3]].

::: lemma:Normals and Projections
Let $Q \subseteq \mathcal{E}$, $\bar{x} \in Q$, and $v \in \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The following are equivalent:
- $v \in N_Q(\bar{x})$.
- $\bar{x} \in \underset{x \in Q}{\operatorname{argmax}}\langle v, x\rangle$.
- $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for any $\lambda \geq 0$.
- $\operatorname{proj}_Q(\bar{x} + \lambda v) = \bar{x}$ for some $\lambda > 0$.
:::

::: lemma:Normal Cone to a Convex Cone
Let $K \subseteq \mathcal{E}$, and $\bar{x} \in K$. Assume $K$ is a convex cone. $N_K(\bar{x}) = K^\circ \cap \{\bar{x}\}^\perp$.
:::

::: lemma:Normal Cone of an Interior Point
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. $\bar{x} \in \operatorname{int}(Q)$ iff $N_Q(\bar{x}) = \{0\}$.
::: ^normal-cone-of-an-interior-point

::: corollary
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. Set $S := \operatorname{aff}(Q) - \bar{x}$. $\bar{x} \in \operatorname{ri}(Q)$ iff $N_Q(\bar{x}) = S^\perp$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$, and $\bar{x} \in Q$. Assume $Q$ is convex. A halfspace $H$ supports $Q$ at $\bar{x}$ iff $H = \{y \in \mathcal{E} : \langle v, y\rangle \leq \langle v, \bar{x}\rangle\}$ for some $v \in N_Q(\bar{x})\setminus\{0\}$.
:::
