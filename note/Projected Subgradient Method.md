::: definition:Projected subgradient method
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, and $\alpha_k > 0$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, closed, and convex, and $f$ is convex. The projected subgradient method generates the iterates $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha_kg_k)$ with $g_k \in \partial f(x_k)$, and outputs $\bar{x}_T = \frac{1}{A_T}\sum_{k = 0}^{T - 1}\alpha_kx_k$ with $A_T = \sum_{k = 0}^{T - 1}\alpha_k$, computed online by $\bar{x}_1 = x_0$ and $\bar{x}_{T + 1} = \frac{A_T}{A_{T + 1}}\bar{x}_T + \frac{\alpha_T}{A_{T + 1}}x_T$.
:::

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is convex and $L$-Lipschitz continuous, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha_kg_k)$ with $\alpha_k > 0$ and $g_k \in \partial f(x_k)$, $A_T = \sum_{k = 0}^{T - 1}\alpha_k$, and $\bar{x}_T = \frac{1}{A_T}\sum_{k = 0}^{T - 1}\alpha_kx_k$. $f(\bar{x}_T) - f(x^*) \leq \frac{\|x_0 - x^*\|^2 + L^2\sum_{k = 0}^{T - 1}\alpha_k^2}{2A_T}$ for any integer $T \geq 1$.
::: ^subgradient-convergence

*Proof.*
[[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] with comparison point $x^*$ gives
$$
\begin{aligned}
\|x_{k + 1} - x^*\|^2 &\leq \|x_k - \alpha_kg_k - x^*\|^2 \\
&= \|x_k - x^*\|^2 - 2\alpha_kg_k^T(x_k - x^*) + \alpha_k^2\|g_k\|^2.
\end{aligned}
$$
[[Subgradient#^global-subgradient-inequality|Lemma 3 (Global Subgradient Inequality)]] gives
$$
f(x^*) \geq f(x_k) + g_k^T(x^* - x_k).
$$
Multiplying it by $\alpha_k$ and combining it with the inequality above and $\|g_k\| \leq L$ from Lipschitz continuity give
$$
\begin{aligned}
\alpha_k(f(x_k) - f(x^*)) &\leq \alpha_kg_k^T(x_k - x^*) \\
&\leq \frac{1}{2}\left(\|x_k - x^*\|^2 - \|x_{k + 1} - x^*\|^2\right) + \frac{\alpha_k^2}{2}\|g_k\|^2 \\
&\leq \frac{1}{2}\left(\|x_k - x^*\|^2 - \|x_{k + 1} - x^*\|^2\right) + \frac{L^2}{2}\alpha_k^2.
\end{aligned}
$$
By convexity, summing over $0, \ldots, T - 1$ gives
$$
A_T(f(\bar{x}_T) - f(x^*)) \leq \sum_{k = 0}^{T - 1}\alpha_k(f(x_k) - f(x^*)) \leq \frac{1}{2}\|x_0 - x^*\|^2 + \frac{L^2}{2}\sum_{k = 0}^{T - 1}\alpha_k^2.
$$

::: note
Assume the hypotheses of [[#^subgradient-convergence|Proposition 2]] and $\|x_0 - x^*\| \leq R$. If $\alpha_k = \frac{R}{L\sqrt{T}}$ for $0 \leq k \leq T - 1$, then $f(\bar{x}_T) - f(x^*) \leq \frac{LR}{\sqrt{T}}$. In particular, for any $\varepsilon > 0$, $f(\bar{x}_T) - f(x^*) \leq \varepsilon$ if $T \geq \frac{L^2R^2}{\varepsilon^2}$.
:::

::: note
Assume the hypotheses of [[#^subgradient-convergence|Proposition 2]] and $\|x_0 - x^*\| \leq R$. If $\alpha_k = \frac{R}{L\sqrt{k + 1}}$ for $k \geq 0$, then $A_T \geq \frac{R\sqrt{T}}{L}$ and $\sum_{k = 0}^{T - 1}\alpha_k^2 \leq \frac{R^2}{L^2}(1 + \ln T)$ for any integer $T \geq 1$. Substituting them into [[#^subgradient-convergence|Proposition 2]] gives $f(\bar{x}_T) - f(x^*) \leq \frac{LR(2 + \ln T)}{2\sqrt{T}}$.
:::

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is convex and $L$-Lipschitz continuous, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha_kg_k)$ with $\alpha_k > 0$ and $g_k \in \partial f(x_k)$, $A_T = \sum_{k = 0}^{T - 1}\alpha_k$, $\bar{x}_T = \frac{1}{A_T}\sum_{k = 0}^{T - 1}\alpha_kx_k$, $U_T = \frac{1}{A_T}\sum_{k = 0}^{T - 1}\alpha_kf(x_k)$, and $B_T = \frac{1}{A_T}\sum_{k = 0}^{T - 1}\alpha_k\left(f(x_k) + g_k^T(x^* - x_k)\right)$. $B_T \leq f(x^*) \leq f(\bar{x}_T) \leq U_T$ and $U_T - B_T \leq \frac{\|x_0 - x^*\|^2 + L^2\sum_{k = 0}^{T - 1}\alpha_k^2}{2A_T}$ for any integer $T \geq 1$.
:::

*Proof.*
[[Subgradient#^global-subgradient-inequality|Lemma 3 (Global Subgradient Inequality)]] gives $B_T \leq f(x^*)$, $\bar{x}_T \in \mathcal{X}$ gives $f(x^*) \leq f(\bar{x}_T)$, and convexity gives $f(\bar{x}_T) \leq U_T$. Summing the bound on $\alpha_kg_k^T(x_k - x^*)$ in the proof of [[#^subgradient-convergence|Proposition 2]] bounds $A_T(U_T - B_T) = \sum_{k = 0}^{T - 1}\alpha_kg_k^T(x_k - x^*)$.
