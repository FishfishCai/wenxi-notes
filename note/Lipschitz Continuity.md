::: definition:Lipschitz Continuity
Let $S \subseteq \mathcal{E}$, $f : S \to \mathcal{Y}$, and $L \geq 0$. $f$ is $L$-Lipschitz continuous on $S$ if $\|f(x) - f(y)\| \leq L\|x - y\|$ for any $x, y \in S$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $U \subseteq \mathcal{E}$. Assume $f$ is proper and convex, and $U \subseteq \operatorname{dom} f$ is open. $\underset{x, y \in U,\ x \neq y}{\sup}\frac{|f(x) - f(y)|}{\|x - y\|} = \underset{x \in U,\ v \in \partial f(x)}{\sup}\|v\|$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$. Assume $f$ is proper, closed, and convex. $f$ is $L$-Lipschitz continuous on $\mathcal{E}$ iff $\operatorname{dom} f^* \subseteq \{v \in \mathcal{E} : \|v\| \leq L\}$.
:::

::: theorem:Lipschitz Continuity on Compact Subsets of the Relative Interior
Let $f : \mathcal{E} \to \mathbb{R} \cup \{+\infty\}$, and $K \subseteq \operatorname{ri}(\operatorname{dom} f)$. Assume $f$ is proper and convex, and $K$ is compact. There exists $L_K \geq 0$ s.t. $f$ is $L_K$-Lipschitz continuous on $K$.
:::

::: definition:L-Smoothness
Let $f : \mathcal{E} \to \mathbb{R}$, and $L > 0$. Assume $f \in \mathcal{C}^1$. $f$ is $L$-smooth if $\|\nabla f(x) - \nabla f(y)\| \leq L\|x - y\|$ for any $x, y \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. If $f$ is $L$-smooth, then $|f(y) - f(x) - \langle \nabla f(x), y - x\rangle| \leq \frac{L}{2}\|y - x\|^2$ for any $x, y \in \mathcal{E}$.
::: ^l-smooth-first-order-bound

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. Assume $f$ is convex. $f$ is $L$-smooth iff $f(y) \leq f(x) + \langle v, y - x\rangle + \frac{L}{2}\|y - x\|^2$ for any $x, y \in \mathcal{E}$ and $v \in \partial f(x)$.
::: ^l-smooth-convex-upper-bound

::: note
If $f \in \mathcal{C}^1$, [[#^l-smooth-convex-upper-bound|Proposition 7]] becomes: $f$ is $L$-smooth iff $f(y) \leq f(x) + \langle \nabla f(x), y - x\rangle + \frac{L}{2}\|y - x\|^2$ for any $x, y \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$. $f$ is $L$-smooth iff $-LI \preceq \nabla^2 f(x) \preceq LI$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$, and $x^* \in \mathcal{E}$. Assume $f$ is $L$-smooth and $x^*$ is a global minimizer of $f$. $f(x) - f(x^*) \leq \frac{L}{2}\|x - x^*\|^2$ for any $x \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$, and $x^* \in \mathcal{E}$. Assume $f$ is $L$-smooth and $x^*$ is a global minimizer of $f$. $f(x) - f(x^*) \geq \frac{\|v\|^2}{2L}$ for any $x \in \mathcal{E}$ and $v \in \partial f(x)$.
::: ^l-smooth-subgradient-bound

::: note
If $f \in \mathcal{C}^1$, [[#^l-smooth-subgradient-bound|Proposition 10]] becomes $f(x) - f(x^*) \geq \frac{\|\nabla f(x)\|^2}{2L}$ for any $x \in \mathcal{E}$.
:::

::: definition:Lipschitz Continuous Hessian
Let $f : \mathcal{E} \to \mathbb{R}$, and $M > 0$. Assume $f \in \mathcal{C}^2$. The Hessian of $f$ is Lipschitz continuous with constant $M$ if $\|\nabla^2 f(x) - \nabla^2 f(y)\| \leq M\|x - y\|$ for any $x, y \in \mathcal{E}$.
:::

::: proposition
Let $f : \mathcal{E} \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$ and the Hessian of $f$ is Lipschitz continuous with constant $M$. $f(y) \leq f(x) + \langle \nabla f(x), y - x\rangle + \frac{1}{2}\langle \nabla^2 f(x)(y - x), y - x\rangle + \frac{M}{6}\|y - x\|^3$ for any $x, y \in \mathcal{E}$.
:::
