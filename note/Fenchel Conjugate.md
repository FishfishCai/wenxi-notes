::: definition:Fenchel Conjugate
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The Fenchel conjugate of $f$ is $f^*(y) := \underset{x \in \mathcal{E}}{\sup}\{\langle y,x\rangle - f(x)\}.$
:::

::: note
For a fixed slope $y$ with $f^*(y) \in \mathbb{R}$, $f^*(y)$ is the smallest signed shift $c$ s.t. $\langle y,x\rangle - c \leq f(x)$ for any $x$.
:::

::: lemma
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$. If $g \leq f$, then $g^* \geq f^*$.
::: ^conjugacy-order-reversal

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. $(y,r) \in \operatorname{epi} f^* \iff \langle y,x\rangle - r \leq f(x)\text{ for any }x \in \mathcal{E}.$
:::

::: proposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. $f^*(y) = \sigma_{\operatorname{epi} f}(y,-1)$ for any $y \in \mathcal{E}$.
:::

::: lemma
Let $a \in \mathcal{E}$ and $b \in \mathbb{R}$. Set $g(x) := \langle a,x\rangle + b$. $g^{**} = g$.
::: ^affine-biconjugacy

::: theorem:Biconjugacy
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ and $\overline{\operatorname{co}}f$ are proper. $f^{**} = \overline{\operatorname{co}}f$. If $f$ is closed and convex, then $f^{**} = f$.
:::

*Proof.*
Set $F := \overline{\operatorname{co}}f$. For any $x \in \mathcal{E}$,
$$
\begin{aligned}
f^{**}(x)
&= \underset{y \in \mathcal{E}}{\sup}
\left\{\langle x,y\rangle -
\underset{z \in \mathcal{E}}{\sup}\{\langle y,z\rangle - f(z)\}\right\}\\
&\leq \underset{y \in \mathcal{E}}{\sup}
\{\langle x,y\rangle - (\langle y,x\rangle - f(x))\}
= f(x).
\end{aligned}
$$
Since $f^{**}$ is closed and convex, $f^{**} \leq F$.
Reversely, for any affine minorant $g \leq f$, [[#^conjugacy-order-reversal|order reversal]] applied twice and [[#^affine-biconjugacy|affine biconjugacy]] give $g = g^{**} \leq f^{**}$.这里还要用到closed copnvex envelope那个性质

::: example
Let $Q \subseteq \mathcal{E}$, $a \in \mathcal{E}$, $b \in \mathbb{R}$, and $p, q \in \mathbb{R}$. Assume $Q$ is nonempty, $p, q > 1$, and $\frac{1}{p} + \frac{1}{q} = 1$.

$$
\begin{array}{c|c|c|c}
\qquad f(x) \qquad & \quad \operatorname{dom} f \quad & \qquad f^*(y) \qquad & \quad \operatorname{dom} f^* \quad \\
\hline
\delta_Q(x) & Q & \sigma_Q(y) & \operatorname{dom}\sigma_Q \\
\langle a,x\rangle + b & \mathcal{E} & -b + \delta_{\{a\}}(y) & \{a\} \\
\lvert x\rvert & \mathbb{R} & 0 & [-1,1] \\
\frac{1}{p}\lvert x\rvert^p & \mathbb{R} & \frac{1}{q}\lvert y\rvert^q & \mathbb{R} \\
\sqrt{1 + x^2} & \mathbb{R} & -\sqrt{1 - y^2} & [-1,1] \\
-\log x & (0,+\infty) & -1 - \log(-y) & (-\infty,0) \\
e^x & \mathbb{R} & y\log y - y & [0,+\infty) \\
x\log x & (0,+\infty) & e^{y - 1} & \mathbb{R} \\
\log(1 + e^x) & \mathbb{R} & \quad y\log y + (1 - y)\log(1 - y) \quad & [0,1]
\end{array}
$$
:::

::: example
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$, $\varphi : \mathcal{E} \times \mathcal{Y} \to \overline{\mathbb{R}}$, $A : \mathcal{E} \to \mathcal{Y}$, $b \in \mathcal{E}$, and $\lambda \in \mathbb{R}$. Assume $f$, $g$, and $\varphi$ are proper and convex, $A$ is linear, and $\lambda > 0$.

$$
\begin{array}{c|c}
\qquad\qquad h(x) \qquad\qquad & \qquad\qquad h^*(y) \qquad\qquad \\
\hline
\lambda f(x) & \lambda f^*\left(\frac{y}{\lambda}\right) \\
f(x + b) & f^*(y) - \langle b,y\rangle \\
\underset{z \in \mathcal{Y}}{\inf}\varphi(x,z) & \varphi^*(y,0) \\
(f \square g)(x) & f^*(y) + g^*(y) \\
\underset{u : Au = x}{\inf} f(u) & f^*(A^*y)
\end{array}
$$
:::
