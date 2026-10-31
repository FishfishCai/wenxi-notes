::: definition:Strong Convexity
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $m > 0$. $f$ is strongly convex with modulus $m$ if $f((1 - \alpha)x + \alpha y) \leq (1 - \alpha)f(x) + \alpha f(y) - \frac{m}{2}\alpha(1 - \alpha)\|x - y\|^2$ for any $x, y \in \mathcal{E}$ and $\alpha \in [0, 1]$, with $0 \cdot (+\infty) = 0$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. $f$ is strongly convex with modulus $m$ iff $f(x) - \frac{m}{2}\|x\|^2$ is convex.
:::

::: theorem:Strengthened Subgradient Inequality
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $f$ is proper, closed, and convex. $f$ is strongly convex with modulus $m$ iff $f(y) \geq f(x) + \langle v, y - x\rangle + \frac{m}{2}\|y - x\|^2$ for any $x, y \in \mathcal{E}$ and $v \in \partial f(x)$.
::: ^strengthened-subgradient-inequality

::: note
If $f \in \mathcal{C}^1$, [[#^strengthened-subgradient-inequality|Theorem 3 (Strengthened Subgradient Inequality)]] becomes: $f$ is strongly convex with modulus $m$ iff $f(y) \geq f(x) + \langle \nabla f(x), y - x\rangle + \frac{m}{2}\|y - x\|^2$ for any $x, y \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$. $f$ is strongly convex with modulus $m$ iff $\nabla^2 f(x) \succeq mI$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $f$ is proper, closed, and strongly convex with modulus $m$. $f$ has a unique global minimizer.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x^* \in \mathcal{E}$. Assume $f$ is proper and strongly convex with modulus $m$, and $x^*$ is a global minimizer of $f$. $f(x) - f(x^*) \geq \frac{m}{2}\|x - x^*\|^2$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $x^* \in \mathcal{E}$. Assume $f$ is proper and strongly convex with modulus $m$, and $x^*$ is a global minimizer of $f$. $f(x) - f(x^*) \leq \frac{\|v\|^2}{2m}$ for any $x \in \mathcal{E}$ and $v \in \partial f(x)$.
::: ^strong-convexity-subgradient-bound

::: note
If $f \in \mathcal{C}^1$, [[#^strong-convexity-subgradient-bound|Proposition 7]] becomes $f(x) - f(x^*) \leq \frac{\|\nabla f(x)\|^2}{2m}$ for any $x \in \mathcal{E}$.
:::

::: definition:Polyak-Łojasiewicz Condition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, $x^* \in \mathcal{E}$, and $m > 0$. Assume $x^*$ is a global minimizer of $f$. $f$ satisfies the Polyak-Łojasiewicz condition with constant $m$ if $f(x) - f(x^*) \leq \frac{\|v\|^2}{2m}$ for any $x \in \mathcal{E}$ and $v \in \partial f(x)$.
:::

::: note
The Polyak-Łojasiewicz condition keeps only [[#^strong-convexity-subgradient-bound|Proposition 7]], so strong convexity implies it, but the converse fails.
:::
