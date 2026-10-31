::: definition:Descent direction
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. $d$ is a descent direction for $f$ at $x$ if $f(x + t d) < f(x)$ for all $t > 0$ sufficiently small.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. If $d^T \nabla f(x) < 0$, then $d$ is a descent direction for $f$ at $x$.
:::

::: definition:Sufficient decrease property
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The sequence has the sufficient decrease property with constant $\beta > 0$ if $f(x_{k + 1}) \leq f(x_k) - \frac{\beta}{2}\|\nabla f(x_k)\|^2$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $\bar{f} \in \mathbb{R}$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$, $f(x) \geq \bar{f}$ for any $x \in \mathbb{R}^n$, and $\{x_k\}$ has the sufficient decrease property with constant $\beta$. $\underset{0 \leq k \leq T - 1}{\min}\|\nabla f(x_k)\| \leq \sqrt{\frac{2(f(x_0) - \bar{f})}{\beta T}}$ and $\underset{k \to \infty}{\lim}\|\nabla f(x_k)\| = 0$. In particular, $\underset{0 \leq k \leq T - 1}{\min}\|\nabla f(x_k)\| \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \max\left\{1, \frac{2(f(x_0) - \bar{f})}{\beta\varepsilon^2}\right\}$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ is convex, $x^*$ is its global minimizer, $\{x_k\}$ has the sufficient decrease property with constant $\beta$, and $R_0 = \underset{f(x) \leq f(x_0)}{\sup}\|x - x^*\| > 0$.  $f(x_T) - f(x^*) \leq \frac{2R_0^2}{\beta T}$ for $T \geq 1$. In particular, $f(x_T) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \frac{2R_0^2}{\beta\varepsilon}$.
::: ^sufficient-decrease-convex-rate

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ has Polyak-Łojasiewicz condition with constant $m$, $x^*$ is its global minimizer, $\{x_k\}$ has the sufficient decrease property with constant $\beta$, and $0 < m\beta \leq 1$. $f(x_T) - f(x^*) \leq (1 - m\beta)^T(f(x_0) - f(x^*))$. In particular, $f(x_T) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \frac{1}{m\beta}\ln\frac{f(x_0) - f(x^*)}{\varepsilon}$.
:::

::: definition:Line-search direction conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $\varepsilon, \gamma_1, \gamma_2 > 0$. Assume $f \in \mathcal{C}^1$. $d_k$ satisfies the line-search direction conditions if $\nabla f(x_k) \neq 0$, $d_k \neq 0$, $\varepsilon \leq \frac{-d_k^T\nabla f(x_k)}{\|\nabla f(x_k)\|\|d_k\|}$, and $\gamma_1 \leq \frac{\|d_k\|}{\|\nabla f(x_k)\|} \leq \gamma_2$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and $d_k$ satisfies the line-search direction conditions with constants $\varepsilon, \gamma_1, \gamma_2$. Set $x_{k + 1} = x_k + \alpha d_k$. $f(x_{k + 1}) \leq f(x_k) - \alpha\left(\varepsilon - \frac{L\alpha\gamma_2}{2}\right)\|\nabla f(x_k)\|\|d_k\|$. If $0 < \alpha < \frac{2\varepsilon}{L\gamma_2}$, then $f(x_{k + 1}) \leq f(x_k) - \alpha\gamma_1\left(\varepsilon - \frac{L\alpha\gamma_2}{2}\right)\|\nabla f(x_k)\|^2.$ The sequence has the sufficient decrease property with constant $\beta = 2\alpha\gamma_1\left(\varepsilon - \frac{L\alpha\gamma_2}{2}\right)$.
:::

::: definition:Fixed steplength
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_k, d_k \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and $d_k$ satisfies the line-search direction conditions with constants $\varepsilon, \gamma_1, \gamma_2$. Fixed-steplength line search chooses $\alpha_k = \frac{\varepsilon}{L\gamma_2}$.
:::

::: definition:Exact line search
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_k, d_k \in \mathbb{R}^n$. Assume the minimum along the ray is attained at a positive steplength. Exact line search chooses $\alpha_k \in \underset{\alpha > 0}{\arg\min}f(x_k + \alpha d_k)$.
:::

::: definition:Backtracking line search
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, $\bar{\alpha} > 0$, $\rho \in (0, 1)$, and $c_1 \in (0, 1)$. Assume $f \in \mathcal{C}^1$ and $\nabla f(x_k)^T d_k < 0$. Backtracking line search chooses $\alpha_k$ as the first value in $\bar{\alpha}, \rho\bar{\alpha}, \rho^2\bar{\alpha}, \ldots$ satisfying $f(x_k + \alpha_k d_k) \leq f(x_k) + c_1\alpha_k\nabla f(x_k)^T d_k$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_k, d_k \in \mathbb{R}^n$. Assume $f$ is $L$-smooth, $d_k$ satisfies the line-search direction conditions with constants $\varepsilon, \gamma_1, \gamma_2$, and $\alpha_k$ is chosen by backtracking line search with parameters $\bar{\alpha}, \rho, c_1$. Set $x_{k + 1} = x_k + \alpha_k d_k$. If $\alpha_k = \bar{\alpha}$, then $f(x_{k + 1}) \leq f(x_k) - c_1\bar{\alpha}\varepsilon\gamma_1\|\nabla f(x_k)\|^2$. Otherwise $f(x_{k + 1}) \leq f(x_k) - \frac{2\rho c_1(1 - c_1)\varepsilon^2}{L}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = 2\min\left\{c_1\bar{\alpha}\varepsilon\gamma_1, \frac{2\rho c_1(1 - c_1)\varepsilon^2}{L}\right\}$.
:::

::: definition:Weak Wolfe conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, $\alpha > 0$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$ and $\nabla f(x_k)^T d_k < 0$. $\alpha$ satisfies the weak Wolfe conditions if $f(x_k + \alpha d_k) \leq f(x_k) + c_1\alpha\nabla f(x_k)^T d_k$ and $\nabla f(x_k + \alpha d_k)^T d_k \geq c_2\nabla f(x_k)^T d_k$.
::: ^weak-wolfe-conditions

::: definition:Extrapolation and bisection for weak Wolfe conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$, $\nabla f(x_k)^T d_k < 0$, and $f$ is bounded below along the ray $x_k + \alpha d_k$ for $\alpha > 0$. Set $\ell = 0$, $u = +\infty$, and $\alpha = 1$. If $f(x_k + \alpha d_k) > f(x_k) + c_1\alpha\nabla f(x_k)^T d_k$, replace $u$ by $\alpha$ and replace $\alpha$ by $\frac{\ell + u}{2}$. Otherwise, if $\nabla f(x_k + \alpha d_k)^T d_k < c_2\nabla f(x_k)^T d_k$, replace $\ell$ by $\alpha$ and replace $\alpha$ by $2\ell$ if $u = +\infty$, or by $\frac{\ell + u}{2}$ if $u < +\infty$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $\alpha_k > 0$. Assume $f$ is $L$-smooth, $d_k$ satisfies the line-search direction conditions with constants $\varepsilon, \gamma_1, \gamma_2$, and $\alpha_k$ satisfies the weak Wolfe conditions with constants $c_1, c_2$. Set $x_{k + 1} = x_k + \alpha_k d_k$. $f(x_{k + 1}) \leq f(x_k) - \frac{c_1(1 - c_2)\varepsilon^2}{L}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \frac{2c_1(1 - c_2)\varepsilon^2}{L}$.
:::
