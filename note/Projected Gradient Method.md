::: definition:Projected gradient method
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, and $\alpha_k > 0$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, closed, and convex, and $f \in \mathcal{C}^1$. The projected gradient method generates the iterates $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha_k\nabla f(x_k))$.
:::

::: lemma
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_k \in \mathcal{X}$, and $\alpha > 0$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is $L$-smooth, and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha\nabla f(x_k))$. $f(x_{k + 1}) \leq f(x_k) - \frac{1}{2\alpha}\|x_{k + 1} - x_k\|^2$.
::: ^projected-gradient-decrease

*Proof.*
Set $d = x_{k + 1} - x_k$. [[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] with comparison point $x_k$ gives $\nabla f(x_k)^T d \leq -\frac{1}{\alpha}\|d\|^2$. Smoothness then yields
$$
f(x_{k + 1}) \leq f(x_k) + \nabla f(x_k)^T d + \frac{L}{2}\|d\|^2 \leq f(x_k) - \left(\frac{1}{\alpha} - \frac{L}{2}\right)\|d\|^2 \leq f(x_k) - \frac{1}{2\alpha}\|d\|^2.
$$

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, and $\bar{f} \in \mathbb{R}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is $L$-smooth, and $f(x) \geq \bar{f}$ for any $x \in \mathcal{X}$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}\left(x_k - \frac{1}{L}\nabla f(x_k)\right)$. $\underset{0 \leq k \leq T - 1}{\min}L\|x_k - x_{k + 1}\| \leq \sqrt{\frac{2L(f(x_0) - \bar{f})}{T}}$ for any integer $T \geq 1$.
:::

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is convex and $L$-smooth, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}\left(x_k - \frac{1}{L}\nabla f(x_k)\right)$. $f(x_k) - f(x^*) \leq \frac{L}{2k}\|x_0 - x^*\|^2$ for any integer $k \geq 1$.
:::

*Proof.*
Smoothness and convexity give
$$
\begin{aligned}
f(x_{k + 1}) &\leq f(x_k) + \nabla f(x_k)^T(x_{k + 1} - x_k) + \frac{L}{2}\|x_{k + 1} - x_k\|^2, \\
f(x_k) &\leq f(x^*) + \nabla f(x_k)^T(x_k - x^*).
\end{aligned}
$$
[[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] with comparison point $x^*$ gives $\nabla f(x_k)^T(x_{k + 1} - x^*) \leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*)$. Adding the two inequalities and using this bound gives
$$
\begin{aligned}
f(x_{k + 1}) - f(x^*) &\leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*) + \frac{L}{2}\|x_{k + 1} - x_k\|^2 \\
&= \frac{L}{2}\left(\|x_k - x^*\|^2 - \|x_{k + 1} - x^*\|^2\right).
\end{aligned}
$$
By [[#^projected-gradient-decrease|Lemma 2]], $f(x_k)$ is nonincreasing, so summing over $0, \ldots, k - 1$ gives
$$
k(f(x_k) - f(x^*)) \leq \sum_{j = 0}^{k - 1}(f(x_{j + 1}) - f(x^*)) \leq \frac{L}{2}\|x_0 - x^*\|^2.
$$

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}\left(x_k - \frac{1}{L}\nabla f(x_k)\right)$. $\|x_k - x^*\|^2 \leq \left(1 - \frac{m}{L}\right)^k\|x_0 - x^*\|^2$ for any integer $k \geq 0$.
:::

*Proof.*
Smoothness and strong convexity give
$$
\begin{aligned}
f(x_{k + 1}) &\leq f(x_k) + \nabla f(x_k)^T(x_{k + 1} - x_k) + \frac{L}{2}\|x_{k + 1} - x_k\|^2, \\
f(x_k) &\leq f(x^*) + \nabla f(x_k)^T(x_k - x^*) - \frac{m}{2}\|x_k - x^*\|^2.
\end{aligned}
$$
[[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] with comparison point $x^*$ gives $\nabla f(x_k)^T(x_{k + 1} - x^*) \leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*)$. Adding the two inequalities and using this bound, with $f(x_{k + 1}) \geq f(x^*)$ since $x_{k + 1} \in \mathcal{X}$, gives
$$
\begin{aligned}
0 \leq f(x_{k + 1}) - f(x^*) &\leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*) + \frac{L}{2}\|x_{k + 1} - x_k\|^2 - \frac{m}{2}\|x_k - x^*\|^2 \\
&= \frac{L - m}{2}\|x_k - x^*\|^2 - \frac{L}{2}\|x_{k + 1} - x^*\|^2,
\end{aligned}
$$
so $\|x_{k + 1} - x^*\|^2 \leq \left(1 - \frac{m}{L}\right)\|x_k - x^*\|^2$.

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}\left(x_k - \frac{1}{L}\nabla f(x_k)\right)$. $f(x_k) - f(x^*) \leq \left(1 - \frac{m}{L}\right)^k(f(x_0) - f(x^*))$ for any integer $k \geq 0$.
:::

*Proof.*
Set $g = \nabla f(x_k)$ and $s = x_k - x_{k + 1}$. Smoothness and strong convexity give
$$
\begin{aligned}
f(x_k) - f(x_{k + 1}) &\geq g^Ts - \frac{L}{2}\|s\|^2, \\
f(x_k) - f(x^*) &\leq g^T(x_k - x^*) - \frac{m}{2}\|x_k - x^*\|^2.
\end{aligned}
$$
[[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] with comparison points $x^*$ and $x_k$ gives
$$
g^T(x_{k + 1} - x^*) \leq Ls^T(x_{k + 1} - x^*), \qquad g^Ts \geq L\|s\|^2.
$$
Using the first bound in the second inequality, with $x_k - x^* = s + (x_{k + 1} - x^*)$, and completing the square give
$$
\begin{aligned}
f(x_k) - f(x^*) &\leq g^Ts - L\|s\|^2 + Ls^T(x_k - x^*) - \frac{m}{2}\|x_k - x^*\|^2 \\
&\leq g^Ts + \left(\frac{L^2}{2m} - L\right)\|s\|^2.
\end{aligned}
$$
Since $\left(1 - \frac{m}{L}\right)\left(g^Ts - L\|s\|^2\right) \geq 0$, the first inequality gives
$$
\frac{m}{L}(f(x_k) - f(x^*)) \leq \frac{m}{L}g^Ts + \left(\frac{L}{2} - m\right)\|s\|^2 \leq g^Ts - \frac{L}{2}\|s\|^2 \leq f(x_k) - f(x_{k + 1}),
$$
so $f(x_{k + 1}) - f(x^*) \leq \left(1 - \frac{m}{L}\right)(f(x_k) - f(x^*))$.

::: definition:Projected backtracking line search
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_k \in \mathcal{X}$, $\bar{\alpha} > 0$, $\rho \in (0, 1)$, and $c \in (0, 1)$. Assume $\mathcal{X}$ is nonempty, closed, and convex, and $f \in \mathcal{C}^1$. Set $z(\alpha) = \operatorname{proj}_{\mathcal{X}}(x_k - \alpha\nabla f(x_k))$. Projected backtracking line search chooses $\alpha_k$ as the first value in $\bar{\alpha}, \rho\bar{\alpha}, \rho^2\bar{\alpha}, \ldots$ satisfying $f(z(\alpha_k)) \leq f(x_k) + c\nabla f(x_k)^T(z(\alpha_k) - x_k)$.
:::

::: note
Projected backtracking line search terminates. Since [[Projection and Separation#^projection-onto-a-closed-convex-set|Theorem 4 (Projection onto a Closed Convex Set)]] gives $\nabla f(x_k)^T(z(\alpha) - x_k) \leq -\frac{1}{\alpha}\|z(\alpha) - x_k\|^2$, the $L$-smoothness of $f$ makes the test hold whenever $\alpha \leq \frac{2(1 - c)}{L}$, so $\alpha_k \geq \min\left\{\bar{\alpha}, \frac{2\rho(1 - c)}{L}\right\}$.
:::

::: definition:Accelerated projected gradient method
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, $\alpha_k > 0$, and $\beta_k \geq 0$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, closed, and convex, and $f \in \mathcal{C}^1$. Set $x_{-1} = x_0$. The accelerated projected gradient method generates the iterates $y_k = x_k + \beta_k(x_k - x_{k - 1})$ and $x_{k + 1} = \operatorname{proj}_{\mathcal{X}}(y_k - \alpha_k\nabla f(y_k))$.
:::

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, closed, and convex, $f$ is convex and $L$-smooth, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $\lambda_0 = 0$, $\lambda_{k + 1} = \frac{1 + \sqrt{1 + 4\lambda_k^2}}{2}$ for $k \geq 0$, and $\{x_k\}$ as the accelerated projected gradient iterates with $\alpha_k = \frac{1}{L}$, $\beta_0 = 0$, and $\beta_k = \frac{\lambda_k - 1}{\lambda_{k + 1}}$ for $k \geq 1$. $f(x_K) - f(x^*) \leq \frac{2L\|x_0 - x^*\|^2}{(K + 1)^2}$ for any integer $K \geq 1$.
:::
