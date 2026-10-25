::: definition:Affine Map
Let $T : \mathcal{E} \to \mathcal{Y}$. $T$ is affine if $T(\alpha x + \beta y) = \alpha T(x) + \beta T(y)$ for any $x, y \in \mathcal{E}$ and $\alpha, \beta \geq 0$ s.t. $\alpha + \beta = 1$.
:::

::: proposition
Let $f : \mathcal{Y} \to \overline{\mathbb{R}}$ and $T : \mathcal{E} \to \mathcal{Y}$. Assume $f$ is convex and $T$ is affine. $f \circ T$ is convex.
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$ and $\lambda \in \mathbb{R}$. Assume $f$ is convex and $\lambda > 0$. Set $h(x) := \lambda f\left(\frac{x}{\lambda}\right)$. $h$ is convex and $\operatorname{epi} h = \lambda \operatorname{epi} f$.
:::

::: proposition
Let $I$ be an index set and $f_i : \mathcal{E} \to \overline{\mathbb{R}}$ for $i \in I$. Assume each $f_i$ is convex. Set $h(x) := \underset{i \in I}{\sup} f_i(x)$. $h$ is convex and $\operatorname{epi} h = \bigcap_{i \in I}\operatorname{epi} f_i$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{Y} \to \overline{\mathbb{R}}$. Assume $A$ is linear and $f$ is convex. Set $h(x) := f(Ax)$. $h$ is convex and $\operatorname{epi} h = (A \times I)^{-1}(\operatorname{epi} f)$.
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
Let $g : \mathcal{E} \times \mathcal{Y} \to \overline{\mathbb{R}}$. The infimum projection of $g$ is $h(x) := \underset{y \in \mathcal{Y}}{\inf} g(x,y)$.
:::

::: proposition
Let $g : \mathcal{E} \times \mathcal{Y} \to \overline{\mathbb{R}}$. Assume $g$ is convex. Set $h(x) := \underset{y \in \mathcal{Y}}{\inf} g(x,y)$ and $Q := \pi_{x,r}(\operatorname{epi} g)$. $h$ is convex. If the infimum is attained whenever $h(x) \in \mathbb{R}$, then $\operatorname{epi} h = Q$.
::: ^infimum-projection-convexity

*Proof.*
By [[Convex Set#^convex-set-operations|convexity-preserving set operations]],
$$
Q = \pi_{x,r}(\operatorname{epi} g) = \{(x,r) \in \mathcal{E} \times \mathbb{R} : \exists y \in \mathcal{Y},\ g(x,y) \leq r\}
$$
is convex. Since
$$
E_Q(x) = \underset{y \in \mathcal{Y}}{\inf} g(x,y) = h(x),
$$
$h$ is convex by [[#^lower-envelope-convexity|convexity of lower envelopes]]. Under attainment, $\operatorname{epi} h = Q + (\{0\} \times \mathbb{R}_+) = Q$ by [[#^lower-envelope-epigraph|the lower-envelope epigraph identity]].

::: definition:Value Function under a Linear Constraint
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $A$ is linear. The value function is $v(b) := \underset{y : Ay = b}{\inf} f(y)$.
:::

::: proposition
Let $A : \mathcal{E} \to \mathcal{Y}$ and $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $A$ is linear and $f$ is convex. Set $v(b) := \underset{y : Ay = b}{\inf} f(y)$. $v$ is convex. If the infimum is attained whenever $v(b) \in \mathbb{R}$, then $\operatorname{epi} v = (A \times I)(\operatorname{epi} f)$.
::: ^value-function-convexity

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
::: ^infimal-convolution-convexity

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

::: note
[[#^infimum-projection-convexity|Proposition 10]], [[#^value-function-convexity|Proposition 12]], and [[#^infimal-convolution-convexity|Proposition 14]] correspond to the projection, linear image, and Minkowski sum of convex sets, respectively. Convexity is always preserved, but each epigraph identity requires attainment.
:::

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
