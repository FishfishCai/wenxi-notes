::: definition:Distance and Projection
Let $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}$. Assume $Q$ is nonempty. Set $\operatorname{dist}_Q(y) := \underset{x \in Q}{\inf}\|x - y\|$. The projection set is $\operatorname{proj}_Q(y) := \{z \in Q : \|z - y\| = \operatorname{dist}_Q(y)\}$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. $|\operatorname{dist}_Q(y) - \operatorname{dist}_Q(w)| \leq \|y - w\|$ for any $y, w \in \mathcal{E}$.
::: ^distance-lipschitz

::: proposition
Let $Q \subseteq \mathcal{E}$. If $Q$ is nonempty and closed, then $\operatorname{proj}_Q(y) \neq \emptyset$ for any $y \in \mathcal{E}$.
::: ^projection-existence

*Proof.*
Both [[#^distance-lipschitz|Proposition 2]] and [[#^projection-existence|Proposition 3]] use $x_\varepsilon \in Q$ s.t. $\|x_\varepsilon - y\| < \operatorname{dist}_Q(y) + \varepsilon$.

::: theorem:Projection onto a Closed Convex Set
Let $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. The set $\operatorname{proj}_Q(y)$ consists of exactly one point for any $y \in \mathcal{E}$. For $y \in \mathcal{E}$ and $z \in Q$, $z = \operatorname{proj}_Q(y)$ iff $\langle y - z, x - z\rangle \leq 0$ for any $x \in Q$.
::: ^projection-onto-a-closed-convex-set

*Proof.*
Consider $\phi(t) := \frac{1}{2}\|y - x_t\|^2$ with $x_t := z + t(x - z)$, whose right derivative satisfies $0 \leq \phi'(0) = -\langle y - z, x - z\rangle$. Conversely, use
$$
\begin{aligned}
\|y - x\|^2 &= \|(y - z) - (x - z)\|^2\\
&= \|y - z\|^2 + \|x - z\|^2 - 2\langle y - z, x - z\rangle\\
&\geq \|y - z\|^2.
\end{aligned}
$$

::: corollary
Let $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty, closed, and convex. $\|\operatorname{proj}_Q(y) - \operatorname{proj}_Q(w)\|^2 \leq \langle \operatorname{proj}_Q(y) - \operatorname{proj}_Q(w), y - w\rangle$ for any $y, w \in \mathcal{E}$, implying $\|\operatorname{proj}_Q(y) - \operatorname{proj}_Q(w)\| \leq \|y - w\|$ for any $y, w \in \mathcal{E}$. 
:::

::: definition:Strict Separation of a Point and a Set
Let $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}$. A hyperplane $\{x \in \mathcal{E} : \langle a, x\rangle = b\}$ strictly separates $y$ from $Q$ if $a \in \mathcal{E}\setminus\{0\}$, $b \in \mathbb{R}$, and $\langle a, x\rangle \leq b < \langle a, y\rangle$ for any $x \in Q$.
:::

::: note
If $p \in \mathcal{E}$ lies on the hyperplane $\{x \in \mathcal{E} : \langle a, x\rangle = b\}$, then the hyperplane equals $\{x \in \mathcal{E} : \langle a, x - p\rangle = 0\}$. Thus, to construct a hyperplane through $p$, it suffices to construct $a$.
:::

::: theorem:Strict Separation
Let $Q \subseteq \mathcal{E}$, and $y \in \mathcal{E}\setminus Q$. Assume $Q$ is nonempty, closed, and convex. There exist $a \in \mathcal{E}\setminus\{0\}$ and $b \in \mathbb{R}$ s.t. $\langle a, x\rangle \leq b < \langle a, y\rangle$ for any $x \in Q$.
::: ^strict-separation

*Proof.*
Use the projection $z$ of $y$ onto $Q$ to construct the hyperplane through $z$ perpendicular to $y - z$.

::: definition:Supporting Halfspace
Let $Q \subseteq \mathcal{E}$, and $x \in \operatorname{cl}(Q)$. A halfspace $H = \{z \in \mathcal{E} : \langle a, z\rangle \leq b\}$ supports $Q$ at $x$ if $a \in \mathcal{E}\setminus\{0\}$, $b \in \mathbb{R}$, $Q \subseteq H$, and $\langle a, x\rangle = b$.
:::

::: proposition
Let $Q \subseteq \mathcal{E}$, and $x \in \operatorname{cl}(Q)$. Assume $Q$ is convex. A supporting halfspace to $Q$ at $x$ exists iff $x \in \operatorname{bd}(Q)$.
:::

*Proof.*
For $x \in \operatorname{int}(Q)$, $x + ta$ violates the hyperplane for sufficiently small $t > 0$. Conversely, consider $p_k \to x$ and use the projections $z_k$ to take the limit of $\frac{p_k - z_k}{\|p_k - z_k\|}$ as $a$.

::: theorem:Dual Description of the Closed Convex Hull
Let $Q \subseteq \mathcal{E}$. Assume $Q$ is nonempty. Set $F_Q := \{(a, b) \in \mathcal{E} \times \mathbb{R} : \langle a, x\rangle \leq b \text{ for any } x \in Q\}$. $\operatorname{cl}(\operatorname{conv}(Q)) = \bigcap_{(a,b) \in F_Q}\{x \in \mathcal{E} : \langle a, x\rangle \leq b\}$.
::: ^dual-description-of-the-closed-convex-hull
