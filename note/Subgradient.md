::: definition:Fréchet Subgradient
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $x \in \mathcal{E}$. A vector $v \in \mathcal{E}$ is a Fréchet subgradient of $f$ at $x$ if $f(x) \in \mathbb{R}$ and $f(y) \geq f(x) + \langle v, y - x\rangle + o(\|y - x\|)$ as $y \to x$.
:::

::: definition:Subdifferential
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $x \in \mathcal{E}$. The subdifferential $\partial f(x)$ of $f$ at $x$ is the set of Fréchet subgradients of $f$ at $x$.
:::

::: lemma:Global Subgradient Inequality
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, $x \in \mathcal{E}$, and $v \in \mathcal{E}$. Assume $f$ is convex and $f(x) \in \mathbb{R}$. $v \in \partial f(x)$ iff $f(y) \geq f(x) + \langle v, y - x\rangle$ for any $y \in \mathcal{E}$.
::: ^global-subgradient-inequality

*Proof.*
With $x_t := x + t(y - x)$ for $t \in (0, 1)$,
$$
\begin{aligned}
f(x_t) &\leq (1 - t)f(x) + tf(y),\\
f(x_t) &\geq f(x) + t\langle v, y - x\rangle + o(t\|y - x\|).
\end{aligned}
$$
Combine the two inequalities, divide by $t$, and let $t \downarrow 0$.

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x \in \mathcal{E}$. If $f$ is differentiable at $x$, then $\partial f(x) = \{\nabla f(x)\}$.
::: ^differentiable-subdifferential

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x \in \mathcal{E}$. Assume $f$ is proper and convex. If $\partial f(x)$ is a singleton, then $f$ is differentiable at $x$.
::: ^singleton-subdifferential

::: note
[[#^singleton-subdifferential|Proposition 5]] is the converse of [[#^differentiable-subdifferential|Proposition 4]], which requires $f$ to be proper and convex.
:::

::: proposition
Let $f_i : \mathcal{E}_i \to \mathbb{R} \cup \{+\infty\}$ for $i \in \{1, \ldots, k\}$. Assume each $f_i$ is proper. Set $F(x_1, \ldots, x_k) := \sum_{i=1}^k f_i(x_i)$. $\partial F(x_1, \ldots, x_k) = \partial f_1(x_1) \times \cdots \times \partial f_k(x_k)$ for any $x_i \in \mathcal{E}_i$.
:::

::: proposition
Let $f_i : \mathcal{E} \to \mathbb{R}$ for $i \in \{1,\ldots,k\}$. Assume each $f_i$ is convex and differentiable. Set $f(x) := \underset{1 \le i \le k}{\max} f_i(x)$ and $I(x) := \{i \in \{1,\ldots,k\} : f_i(x) = f(x)\}$. $\partial f(x) = \operatorname{conv}\{\nabla f_i(x) : i \in I(x)\}$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f, g : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x \in \mathcal{E}$. Assume $f$ and $g$ are proper. If $f$ is differentiable at $x$, then $\partial(f + g)(x) = \{\nabla f(x)\} + \partial g(x)$.
:::

::: theorem:Epigraph-Normal Characterization
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, $x \in \mathcal{E}$, and $v \in \mathcal{E}$. Assume $f(x) \in \mathbb{R}$. $v \in \partial f(x)$ iff $(v, -1) \in N_{\operatorname{epi} f}((x, f(x)))$.
::: ^epigraph-normal-characterization

::: theorem:Existence of Subgradients
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $f$ is proper and convex. $\partial f(x) \neq \emptyset$ for any $x \in \operatorname{ri}(\operatorname{dom} f)$.
:::

*Proof.*
First assume $\operatorname{int}(\operatorname{dom} f) \neq \emptyset$, and take $x \in \operatorname{int}(\operatorname{dom} f)$. Since $(x, f(x)) \notin \operatorname{int}(\operatorname{epi} f)$, [[Normal Cone#^normal-cone-of-an-interior-point|Lemma 12 (Normal Cone of an Interior Point)]] gives $(v, \alpha) \in N_{\operatorname{epi} f}((x, f(x)))\setminus\{0\}$, where clearly $\alpha < 0$. Thus $\left(-\frac{v}{\alpha}, -1\right) \in N_{\operatorname{epi} f}((x, f(x)))$, so $-\frac{v}{\alpha} \in \partial f(x)$ by [[#^epigraph-normal-characterization|Theorem 8 (Epigraph-Normal Characterization)]].
Now assume $\operatorname{int}(\operatorname{dom} f) = \emptyset$ and, without loss of generality, $0 \in \operatorname{dom} f$. Set $L := \operatorname{aff}(\operatorname{dom} f)$ and write $\mathcal{E} = L \times L^\perp$, which regroups a basis of $\mathcal{E}$ into bases of $L$ and $L^\perp$. Set $\hat{f}(\hat{y}) := f(\hat{y}, 0)$, the restriction of $f$ to $L$. For $x = (\hat{x}, 0) \in \operatorname{ri}(\operatorname{dom} f)$, we have $\hat{x} \in \operatorname{int}(\operatorname{dom} \hat{f})$, so the first case applied to $\hat{f}$ gives $u \in \partial \hat{f}(\hat{x})$, i.e.,
$$
\hat{f}(\hat{y}) \geq \hat{f}(\hat{x}) + \langle u, \hat{y} - \hat{x}\rangle \quad\text{for any } \hat{y} \in L.
$$
Back in $\mathcal{E}$, this reads
$$
f(\hat{y}, 0) \geq f(\hat{x}, 0) + \langle (u, 0), (\hat{y}, 0) - (\hat{x}, 0)\rangle \quad\text{for any } \hat{y} \in L,
$$
while $f(y) = +\infty$ for $y \notin L$. Hence the desired inequality $f(y) \geq f(x) + \langle (u, 0), y - x\rangle$ holds for any $y \in \mathcal{E}$, and $(u, 0) \in \partial f(x)$ by [[#^global-subgradient-inequality|Lemma 3 (Global Subgradient Inequality)]].

::: lemma:Necessary Condition for Local Optimality
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $x \in \mathcal{E}$. Assume $f(x) \in \mathbb{R}$. If $x$ is a local minimizer of $f$, then $0 \in \partial f(x)$.
:::

::: corollary:Global Optimality of Convex Functions
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x \in \mathcal{E}$. Assume $f$ is proper and convex. $x \in \underset{y \in \mathcal{E}}{\operatorname{argmin}} f(y)$ iff $0 \in \partial f(x)$.
:::

::: theorem:Fenchel-Young Equality
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper. $f(x) + f^*(v) \geq \langle x, v\rangle$ for any $x, v \in \mathcal{E}$. For $x, v \in \mathcal{E}$, $f(x) + f^*(v) = \langle x, v\rangle$ iff $v \in \partial f(x)$.
:::

::: corollary:Subdifferential Inversion
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $x, v \in \mathcal{E}$. Assume $f$ is proper, closed, and convex. $v \in \partial f(x)$ iff $x \in \partial f^*(v)$.
:::

::: example
Let $Q \subseteq \mathcal{E}$, $\rho$ be a norm on $\mathcal{E}$ with dual norm $\rho_*$, $x \in \mathcal{E}$, $z \in \mathbb{R}^n$, and $t \in \mathbb{R}$. Assume $Q$ is nonempty, closed, and convex.

$$
\begin{array}{c|c}
\qquad f \qquad & \qquad \partial f \qquad \\
\hline
\delta_Q(x) & N_Q(x) \\
\sigma_Q(x) & \underset{y \in Q}{\operatorname{argmax}}\langle x, y\rangle \\
\operatorname{dist}_Q(x) & \begin{cases} \left\{\frac{x - \operatorname{proj}_Q(x)}{\operatorname{dist}_Q(x)}\right\}, & x \notin Q \\ N_Q(x) \cap \mathcal{B}, & x \in Q \end{cases} \\
|t| & \begin{cases} \{\operatorname{sign}(t)\}, & t \neq 0 \\ [-1, 1], & t = 0 \end{cases} \\
\max\{0, t\} & \begin{cases} \{0\}, & t < 0 \\ [0, 1], & t = 0 \\ \{1\}, & t > 0 \end{cases} \\
\underset{1 \leq i \leq n}{\max} z_i & \operatorname{conv}(\{e_i : z_i = \underset{1 \leq j \leq n}{\max} z_j\}) \\
\rho(x) & \{v \in \mathcal{E} : \rho_*(v) \leq 1, \langle v, x\rangle = \rho(x)\} \\
\|x\| & \begin{cases} \left\{\frac{x}{\|x\|}\right\}, & x \neq 0 \\ \mathcal{B}, & x = 0 \end{cases} \\
\|z\|_1 & \partial|z_1| \times \cdots \times \partial|z_n| \\
\|z\|_\infty & \begin{cases} \operatorname{conv}(\{\operatorname{sign}(z_i)e_i : |z_i| = \|z\|_\infty\}), & z \neq 0 \\ \operatorname{conv}(\{\pm e_i : 1 \leq i \leq n\}), & z = 0 \end{cases}
\end{array}
$$
:::
