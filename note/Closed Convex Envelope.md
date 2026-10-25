::: definition:Closed Convex Envelope
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. The closed convex envelope $\overline{\operatorname{co}}f$ is defined by $\operatorname{epi}(\overline{\operatorname{co}}f) := \operatorname{cl}(\operatorname{conv}(\operatorname{epi} f)).$
:::

::: definition:Minorant
Let $f, g : \mathcal{E} \to \overline{\mathbb{R}}$. $g$ is a minorant of $f$ if $g \leq f$. An affine minorant is of the form $g(x) = \langle a,x\rangle + b$, with $a \in \mathcal{E}$ and $b \in \mathbb{R}$.
:::

::: theorem:Existence of Affine Minorants
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper. $f$ admits an affine minorant iff $\overline{\operatorname{co}}f$ is proper.
::: ^affine-minorant-existence

*Proof.*
Set $F := \overline{\operatorname{co}}f$ and $Q := \operatorname{epi} F$. If $g$ is an affine minorant, then $g \leq F \leq f$, implying $F$ is proper.
Conversely, assume $F$ is proper. Choose $x_0$ with $F(x_0) \in \mathbb{R}$ and $r_0 < F(x_0)$. By [[Projection and Separation#^strict-separation|Strict Separation]], there exist $a \in \mathcal{E}$ and $\mu, \beta \in \mathbb{R}$ s.t.
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
:::

*Proof.*
Every affine minorant $g \leq f$ satisfies $g \leq F$, so $F(x) \geq \underset{g \leq f,\ g\ \mathrm{affine}}{\sup} g(x)$.
Set $h(x) := \underset{g \leq f,\ g\ \mathrm{affine}}{\sup} g(x)$ and $Q := \operatorname{epi} F$.
By [[#^affine-minorant-existence|Existence of Affine Minorants]], choose $g_1(x) = \langle a_1,x\rangle + b_1 \leq F(x)$. For any $(x_0,r_0) \notin Q$, [[Projection and Separation#^strict-separation|Strict Separation]] gives
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
