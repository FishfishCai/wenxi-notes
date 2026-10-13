## Convex Functions
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
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. $\operatorname{dom} f$ is convex.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is convex. The sublevel set $\{x \in \mathcal{E} : f(x) \leq \alpha\}$ is convex for any $\alpha \in \mathbb{R}$.
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

::: definition:Positive Homogeneity
Let $h : \mathcal{E} \to \overline{\mathbb{R}}$. The function $h$ is positively homogeneous if $\operatorname{epi} h$ is a cone.
:::

::: definition:Sublinear Function
Let $h : \mathcal{E} \to \overline{\mathbb{R}}$. The function $h$ is sublinear if it is convex and positively homogeneous.
:::

::: proposition
Let $h : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $h$ is proper. The function $h$ is sublinear iff $h(\lambda x + \mu y) \leq \lambda h(x) + \mu h(y)$ for any $x, y \in \mathcal{E}$ and $\lambda, \mu \geq 0$, with $0 \cdot (+\infty) = 0$.
:::

## Convexity Preserving Operations
::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$ and $\lambda \in \mathbb{R}$. Assume $f$ is convex and $\lambda > 0$. Set $h(x) := \lambda f\left(\frac{x}{\lambda}\right)$. $h$ is convex and $\operatorname{epi} h = \lambda \operatorname{epi} f$.
:::

::: proposition
Let $I$ be an index set and $f_i : \mathcal{E} \to \overline{\mathbb{R}}$ for $i \in I$. Assume each $f_i$ is convex. Set $h(x) := \underset{i \in I}{\sup} f_i(x)$. $h$ is convex and $\operatorname{epi} h = \bigcap_{i \in I}\operatorname{epi} f_i$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{Y} \to \overline{\mathbb{R}}$. Assume $A$ is linear and $f$ is convex. Set $h(x) := f(Ax)$. $h$ is convex and $\operatorname{epi} h = (A \times I)^{-1}(\operatorname{epi} f)$.
:::

::: definition:Affine Map
Let $T : \mathcal{E} \to \mathcal{Y}$. $T$ is affine if there exist a linear map $A : \mathcal{E} \to \mathcal{Y}$ and $b \in \mathcal{Y}$ s.t. $T(x) = Ax + b$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{Y} \to \overline{\mathbb{R}}$ and $T : \mathcal{E} \to \mathcal{Y}$. Assume $f$ is convex and $T$ is affine. $f \circ T$ is convex.
:::

::: definition:Lower Envelope
Let $Q \subseteq \mathcal{E} \times \mathbb{R}$. The lower envelope of $Q$ is $E_Q(x) := \underset{r : (x,r) \in Q}{\inf} r$.
:::

::: proposition
Let $Q \subseteq \mathcal{E} \times \mathbb{R}$. If the infimum defining $E_Q(x)$ is attained whenever $E_Q(x) \in \mathbb{R}$, then $\operatorname{epi} E_Q = Q + (\{0\} \times \mathbb{R}_+)$.
::: ^lower-envelope-epigraph

::: proposition
Let $Q \subseteq \mathcal{E} \times \mathbb{R}$. If $Q$ is convex, then $E_Q$ is convex.
::: ^lower-envelope-convexity

::: definition:Infimum Projection
Let $f : \mathcal{E} \times \mathcal{Y} \to \overline{\mathbb{R}}$. The infimum projection of $f$ is $g(x) := \underset{y \in \mathcal{Y}}{\inf} f(x,y)$.
:::

::: proposition
Let $f : \mathcal{E} \times \mathcal{Y} \to \overline{\mathbb{R}}$. Assume $f$ is convex. Set $g(x) := \underset{y \in \mathcal{Y}}{\inf} f(x,y)$ and $Q := \pi_{x,r}(\operatorname{epi} f)$. $g$ is convex. If the infimum is attained whenever $g(x) \in \mathbb{R}$, then $\operatorname{epi} g = Q$.
::: ^infimum-projection-convexity

*Proof.*
By [[Convex Set#^convex-set-operations|convexity-preserving set operations]],
$$
Q = \pi_{x,r}(\operatorname{epi} f) = \{(x,r) \in \mathcal{E} \times \mathbb{R} : \exists y \in \mathcal{Y},\ f(x,y) \leq r\}
$$
is convex. Since
$$
E_Q(x) = \underset{y \in \mathcal{Y}}{\inf} f(x,y) = g(x),
$$
$g$ is convex by [[#^lower-envelope-convexity|convexity of lower envelopes]]. Under attainment, $\operatorname{epi} g = Q + (\{0\} \times \mathbb{R}_+) = Q$ by [[#^lower-envelope-epigraph|the lower-envelope epigraph identity]].

::: definition:Value Function under a Linear Constraint
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $A$ is linear. The value function is $v(b) := \underset{y : Ay = b}{\inf} f(y)$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $A$ is linear and $f$ is convex. Set $v(b) := \underset{y : Ay = b}{\inf} f(y)$. $v$ is convex. If the infimum is attained whenever $v(b) \in \mathbb{R}$, then $\operatorname{epi} v = (A \times I)(\operatorname{epi} f)$.
:::

*Proof.*
Write
$$
v(b) = \underset{y \in \mathcal{E}}{\inf}\{f(y) + \delta_{\{0\}}(b - Ay)\}.
$$
The objective is convex in $(b,y)$, so $v$ is convex by [[#^infimum-projection-convexity|partial minimization]]. Set
$$
Q := \{(b,r) \in \mathcal{Y} \times \mathbb{R} : \exists y \in \mathcal{E},\ b = Ay,\ f(y) \leq r\} = (A \times I)(\operatorname{epi} f).
$$
Since $E_Q = v$, under attainment $\operatorname{epi} v = Q + (\{0\} \times \mathbb{R}_+) = Q$ by [[#^lower-envelope-epigraph|the lower-envelope epigraph identity]].

::: definition:Infimal Convolution
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ and $g$ are proper. Their infimal convolution is
$$
(f \square g)(x) := \underset{y \in \mathcal{E}}{\inf}\{f(y) + g(x - y)\}.
$$
:::

::: proposition
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ and $g$ are proper and convex. Set $h := f \square g$. $h$ is convex. If the infimum defining $h(x)$ is attained whenever $h(x) \in \mathbb{R}$, then $\operatorname{epi} h = \operatorname{epi} f + \operatorname{epi} g$.
:::

*Proof.*
Write
$$
h(x) = \underset{y \in \mathcal{E}}{\inf}\{f(y) + g(x - y)\}.
$$
The objective is convex in $(x,y)$, so $h$ is convex by [[#^infimum-projection-convexity|partial minimization]]. Set
$$
Q := \{(x,r) \in \mathcal{E} \times \mathbb{R} : \exists y \in \mathcal{E},\ f(y) + g(x - y) \leq r\} = \operatorname{epi} f + \operatorname{epi} g.
$$
Since $E_Q = h$, under attainment $\operatorname{epi} h = Q + (\{0\} \times \mathbb{R}_+) = Q$ by [[#^lower-envelope-epigraph|the lower-envelope epigraph identity]].

::: definition:Perspective
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The perspective of $f$ is
$$
f_\pi(\lambda,x) :=
\begin{cases}
\lambda f\left(\frac{x}{\lambda}\right), & \lambda > 0, \\
+\infty, & \lambda \leq 0.
\end{cases}
$$
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$.
$$
\operatorname{epi} f_\pi = \{\alpha(1,x,r) : \alpha > 0,\ (x,r) \in \operatorname{epi} f\}.
$$
If $f$ is convex, then $f_\pi$ is convex.
:::
