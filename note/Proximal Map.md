::: definition:Moreau Envelope
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $\alpha > 0$. The Moreau envelope of $f$ is $f_\alpha(x) := \underset{z \in \mathcal{E}}{\inf}\left\{f(z) + \frac{1}{2\alpha}\|z - x\|^2\right\}$.
:::

::: definition:Proximal Map
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $\alpha > 0$. The proximal map of $f$ is $\operatorname{prox}_{\alpha f}(x) := \underset{z \in \mathcal{E}}{\operatorname{argmin}}\left\{f(z) + \frac{1}{2\alpha}\|z - x\|^2\right\}$.
:::

::: theorem:Nonexpansiveness of the Proximal Map
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $\alpha > 0$. Assume $f$ is proper, closed, and convex. $\|\operatorname{prox}_{\alpha f}(x) - \operatorname{prox}_{\alpha f}(y)\| \leq \|x - y\|$ for any $x, y \in \mathcal{E}$.
:::

*Proof.*
Set $p := \operatorname{prox}_{\alpha f}(x)$ and $q := \operatorname{prox}_{\alpha f}(y)$. Since $\frac{x - p}{\alpha} \in \partial f(p)$ and $\frac{y - q}{\alpha} \in \partial f(q)$,
$$
f(q) \geq f(p) + \left\langle\frac{x - p}{\alpha}, q - p\right\rangle,
\qquad
f(p) \geq f(q) + \left\langle\frac{y - q}{\alpha}, p - q\right\rangle.
$$
Adding the two inequalities gives
$$
\|p - q\|^2 \leq \langle p - q, x - y\rangle \leq \|p - q\|\|x - y\|.
$$

::: theorem:Moreau Decomposition
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $\alpha > 0$. Assume $f$ is proper, closed, and convex. $\operatorname{prox}_f(x) + \operatorname{prox}_{f^*}(x) = x$ for any $x \in \mathcal{E}$. More generally, $\operatorname{prox}_{\alpha f}(x) + \alpha\operatorname{prox}_{\alpha^{-1}f^*}(\alpha^{-1}x) = x$ for any $x \in \mathcal{E}$.
::: ^moreau-decomposition

*Proof.*
Set $p := \operatorname{prox}_{\alpha f}(x)$ and $q := \frac{x - p}{\alpha} \in \partial f(p)$, so $p \in \partial f^*(q)$, i.e.,
$$
0 \in \alpha^{-1}\partial f^*(q) + q - \alpha^{-1}x,
$$
which is exactly the optimality condition of $q = \operatorname{prox}_{\alpha^{-1}f^*}(\alpha^{-1}x)$.

::: theorem:Smoothness of the Moreau Envelope
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$, and $\alpha > 0$. Assume $f$ is proper, closed, and convex. $f_\alpha \in \mathcal{C}^1$, $\nabla f_\alpha$ is $\alpha^{-1}$-Lipschitz continuous on $\mathcal{E}$, and
$$
\nabla f_\alpha(x) = \alpha^{-1}(x - \operatorname{prox}_{\alpha f}(x)) = \operatorname{prox}_{\alpha^{-1}f^*}(\alpha^{-1}x)
\quad\text{for any }x \in \mathcal{E}.
$$
::: ^smoothness-of-the-moreau-envelope

*Proof.*
Fix $x \in \mathcal{E}$. Since $f_\alpha = f \square \frac{1}{2\alpha}\|\cdot\|^2$, $(f_\alpha)^* = f^* + \frac{\alpha}{2}\|\cdot\|^2$, and [[#^moreau-decomposition|Theorem 4 (Moreau Decomposition)]] gives
$$
\begin{aligned}
z \in \partial f_\alpha(x)
&\iff x \in \partial f^*(z) + \alpha z\\
&\iff 0 \in \partial\left(f^* + \frac{\alpha}{2}\|\cdot - \alpha^{-1}x\|^2\right)(z)\\
&\iff z = \operatorname{prox}_{\alpha^{-1}f^*}(\alpha^{-1}x) = \alpha^{-1}(x - \operatorname{prox}_{\alpha f}(x)).
\end{aligned}
$$
Thus $\partial f_\alpha(x)$ is a singleton, so $f_\alpha$ is differentiable with the stated gradient. Expanding $\|\nabla f_\alpha(x) - \nabla f_\alpha(y)\|^2$ gives the $\alpha^{-1}$-Lipschitz continuity.

::: theorem:Baillon-Haddad Duality
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper, closed, and convex. $f$ is strongly convex with modulus $\mu$ iff $f^*$ is $\mu^{-1}$-smooth.
:::

*Proof.*
If $f$ is strongly convex with modulus $\mu$, set $g := f - \frac{\mu}{2}\|\cdot\|^2$, which is proper, closed, and convex, so
$$
f^* = \left(g + \frac{\mu}{2}\|\cdot\|^2\right)^* = g^* \square \frac{1}{2\mu}\|\cdot\|^2 = (g^*)_\mu,
$$
which is $\mu^{-1}$-smooth by [[#^smoothness-of-the-moreau-envelope|Theorem 5 (Smoothness of the Moreau Envelope)]].
Conversely, assume $h := f^*$ is $\beta$-smooth with $\beta := \mu^{-1}$. Since $f = f^{**} = h^*$, it suffices to show that $h^* - \frac{1}{2\beta}\|\cdot\|^2$ is convex. Set $g := \frac{\beta}{2}\|\cdot\|^2 - h$, which is finite and convex since $\langle\nabla g(y) - \nabla g(x), y - x\rangle \geq \beta\|y - x\|^2 - \|\nabla h(y) - \nabla h(x)\|\|y - x\| \geq 0$. With $g = g^{**}$,
$$
h(y) = \frac{\beta}{2}\|y\|^2 - g^{**}(y) = \underset{u \in \mathcal{E}}{\inf}\left\{\frac{\beta}{2}\|y\|^2 - \langle y, u\rangle + g^*(u)\right\}.
$$
Hence
$$
h^*(z) = \underset{u \in \mathcal{E}}{\sup}\ \underset{y \in \mathcal{E}}{\sup}\left\{\langle z + u, y\rangle - \frac{\beta}{2}\|y\|^2 - g^*(u)\right\} = \underset{u \in \mathcal{E}}{\sup}\left\{\frac{1}{2\beta}\|z + u\|^2 - g^*(u)\right\},
$$
so
$$
h^*(z) - \frac{1}{2\beta}\|z\|^2 = \underset{u \in \mathcal{E}}{\sup}\left\{\frac{1}{\beta}\langle z, u\rangle + \frac{1}{2\beta}\|u\|^2 - g^*(u)\right\}
$$
is convex as a supremum of affine functions of $z$.

::: theorem:Smooth Convex Functions are Moreau Envelopes
Let $h : \mathcal{E} \to \mathbb{R}$. Assume $h$ is convex and $\beta$-smooth. There exists $f : \mathcal{E} \to \overline{\mathbb{R}}$ s.t. $f$ is proper, closed, and convex, and $h = f_{\beta^{-1}}$.
:::

::: theorem:Subgradient Domination
Let $f : \mathcal{E} \to \overline{\mathbb{R}}$. Assume $f$ is proper, closed, and strongly convex with modulus $\alpha$. $f(x) - \underset{y \in \mathcal{E}}{\min} f(y) \leq \frac{1}{2\alpha}\|v\|^2$ for any $x \in \mathcal{E}$ and $v \in \partial f(x)$.
:::

*Proof.*
Set $x^* := \nabla f^*(0)$, the minimizer of $f$. Strong convexity gives
$$
\begin{aligned}
f(x) - f(x^*) &\leq \langle v, x - x^*\rangle - \frac{\alpha}{2}\|x - x^*\|^2\\
&= \frac{1}{2\alpha}\|v\|^2 - \frac{1}{2\alpha}\|\alpha(x - x^*) - v\|^2\\
&\leq \frac{1}{2\alpha}\|v\|^2.
\end{aligned}
$$
