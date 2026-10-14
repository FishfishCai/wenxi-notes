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

::: note
Value functions under linear constraints and infimal convolutions are special cases of infimum projection.
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

## Closed Convex Envelopes
::: definition:Closed Convex Envelope
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The closed convex envelope $\overline{\operatorname{co}}f$ is defined by $\operatorname{epi}(\overline{\operatorname{co}}f) := \operatorname{cl}(\operatorname{conv}(\operatorname{epi} f)).$
::: ^closed-convex-envelope

::: definition:Minorant
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$. $g$ is a minorant of $f$ if $g \leq f$. An affine minorant is of the form $g(x) = \langle a,x\rangle + b$, with $a \in \mathcal{E}$ and $b \in \mathbb{R}$.
:::

::: theorem:Existence of Affine Minorants
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper. $f$ admits an affine minorant iff $\overline{\operatorname{co}}f$ is proper.
::: ^affine-minorant-existence

*Proof.*
Set $F := \overline{\operatorname{co}}f$ and $Q := \operatorname{epi} F$. If $g$ is an affine minorant, then $g \leq F \leq f$, implying $F$ is proper.
Conversely, assume $F$ is proper. Choose $x_0$ with $F(x_0) \in \mathbb{R}$ and $r_0 < F(x_0)$. By [[Convex Set#^strict-separation|Strict Separation]], there exist $a \in \mathcal{E}$ and $\mu, \beta \in \mathbb{R}$ s.t.
$$
\langle a,x\rangle + \mu r \leq \beta < \langle a,x_0\rangle + \mu r_0
\quad\text{for any }(x,r) \in Q.
$$
If $\mu > 0$, upward unboundedness of $Q$ contradicts the first inequality. If $\mu = 0$, the point $(x_0,F(x_0)) \in Q$ gives $\langle a,x_0\rangle \leq \beta < \langle a,x_0\rangle$. Hence $\mu < 0$, and
$$
g(x) := \left\langle\frac{a}{-\mu},x\right\rangle - \frac{\beta}{-\mu}
\leq F(x) \leq f(x).
$$

::: theorem:Affine Representation of the Closed Convex Envelope
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ and $\overline{\operatorname{co}}f$ are proper. Set $F := \overline{\operatorname{co}}f$.
$$
F(x) = \underset{g \leq f,\ g\ \mathrm{affine}}{\sup} g(x)
\quad\text{for any }x \in \mathcal{E}.
$$
::: ^affine-envelope-representation

*Proof.*
Every affine minorant $g \leq f$ satisfies $g \leq F$, so $F(x) \geq \underset{g \leq f,\ g\ \mathrm{affine}}{\sup} g(x)$.
Set $h(x) := \underset{g \leq f,\ g\ \mathrm{affine}}{\sup} g(x)$ and $Q := \operatorname{epi} F$.
By [[#^affine-minorant-existence|Existence of Affine Minorants]], choose $g_1(x) = \langle a_1,x\rangle + b_1 \leq F(x)$. For any $(x_0,r_0) \notin Q$, [[Convex Set#^strict-separation|Strict Separation]] gives
$$
\langle a,x\rangle + \mu r \leq \beta < \langle a,x_0\rangle + \mu r_0
\quad\text{for any }(x,r) \in Q.
$$
Upward unboundedness of $Q$ rules out $\mu > 0$. If $\mu < 0$, the affine minorant
$$
g(x) := \left\langle\frac{a}{-\mu},x\right\rangle - \frac{\beta}{-\mu}
\leq F(x) \leq f(x)
$$
satisfies $g(x_0) > r_0$, hence $h(x_0) > r_0$.
If $\mu = 0$, set $\ell(x) := \langle a,x\rangle - \beta$. Here $\ell(x) \leq 0$ for any $(x,r) \in Q$, while $\ell(x_0) > 0$. Choose
$$
\lambda > \max\left\{0,\frac{r_0 - g_1(x_0)}{\ell(x_0)}\right\},
\qquad
g_\lambda(x) := g_1(x) + \lambda\ell(x)
= \langle a_1 + \lambda a,x\rangle + b_1 - \lambda\beta.
$$
For any $(x,r) \in Q$, $g_\lambda(x) \leq g_1(x) \leq F(x) \leq r,$ so $g_\lambda \leq F \leq f$, whereas $g_\lambda(x_0) > r_0$. Thus $h(x_0) > r_0$ in both cases, giving $\operatorname{epi} h \subseteq Q$.

## Fenchel Conjugacy
::: definition:Fenchel Conjugate
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The Fenchel conjugate of $f$ is
$$
f^*(y) := \underset{x \in \mathcal{E}}{\sup}\{\langle y,x\rangle - f(x)\}.
$$
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
Let $g : \mathcal{E} \to \mathbb{R}$. Assume $g$ is affine. $g^{**} = g$.
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
Reversely, for any affine minorant $g \leq f$, [[#^conjugacy-order-reversal|order reversal]] applied twice and [[#^affine-biconjugacy|affine biconjugacy]] give $g = g^{**} \leq f^{**}$.

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
