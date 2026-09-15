## Optimization Foundations
### Minimizer
::: definition:Local minimizer
Let $D \subset \mathbb{R}^n$, $f : D \to \mathbb{R}$ and $x^* \in D$. $x^*$ is a local minimizer of $f$ if there is a neighborhood $N$ of $x^*$ s.t. $f(x) \geq f(x^*)$ for any $x \in N \cap D$.
:::

::: definition:Global minimizer
Let $D \subset \mathbb{R}^n$, $f : D \to \mathbb{R}$ and $x^* \in D$. $x^*$ is a global minimizer of $f$ if $f(x) \geq f(x^*)$ for any $x \in D$.
:::

::: definition:Strict local minimizer
Let $D \subset \mathbb{R}^n$, $f : D \to \mathbb{R}$ and $x^* \in D$. $x^*$ is a strict local minimizer of $f$ if there is a neighborhood $N$ of $x^*$ s.t. $f(x) > f(x^*)$ for any $x \in N \cap D$ and $x \neq x^*$.
:::

::: definition:Isolated local minimizer
Let $D \subset \mathbb{R}^n$, $f : D \to \mathbb{R}$ and $x^* \in D$. $x^*$ is an isolated local minimizer of $f$ if it is a local minimizer and some neighborhood of $x^*$ contains no other local minimizer.
:::

::: definition:Unique minimizer
Let $D \subset \mathbb{R}^n$, $f : D \to \mathbb{R}$ and $x^* \in D$. $x^*$ is the unique minimizer of $f$ if it is the only global minimizer.
:::

### Taylor's Theorem
::: theorem:Taylor
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$.
$$f(x + p) = f(x) + \int_0^1 \nabla f(x + t p)^T p \, dt$$
and
$$f(x + p) = f(x) + \nabla f(x + t p)^T p \text{ for some } t \in (0, 1).$$
Assume $f \in \mathcal{C}^2$.
$$\nabla f(x + p) = \nabla f(x) + \int_0^1 \nabla^2 f(x + t p) p \, dt,$$
$$f(x + p) = f(x) + \nabla f(x)^T p + \frac{1}{2} p^T \nabla^2 f(x + t p) p \text{ for some } t \in (0, 1)$$
and
$$f(x + p) = f(x) + \nabla f(x)^T p + \int_0^1 (1 - t)p^T \nabla^2 f(x + tp)p \, dt.$$
:::

::: corollary
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$.  
$$f(x + p) = f(x) + \nabla f(x)^T p + o(\| p \|).$$
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. If $x^*$ is a local minimizer of $f$, then $\nabla f(x^*) = 0$. Assume $f \in \mathcal{C}^2$, then $\nabla^2 f(x^*) \succeq 0$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^2$. If $\nabla f(x^*) = 0$ and $\nabla^2 f(x^*) \succ 0$, then $x^*$ is a strict local minimizer of $f$.
:::

### L-smooth
::: definition:Lipschitz continuous
Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $L > 0$. $f$ is Lipschitz continuous with constant $L$ if $\| f(x) - f(y) \| \leq L \| x - y \|$ for any $x, y \in \mathbb{R}^n$.
:::

::: definition:L-smooth
Let $f : \mathbb{R}^n \to \mathbb{R}$. Assume $f \in \mathcal{C}^1$. $f$ is L-smooth if $\| \nabla f(x) - \nabla f(y) \|_{*} \leq L \| x - y \|$ for any $x, y \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, y \in \mathbb{R}^n$. If $f$ is L-smooth, then $| f(y) - f(x) - \nabla f(x)^T (y - x) | \leq \frac{L}{2} \| y - x \|^2$.
::: ^l-smooth-first-order-bound

::: note
The converse of [[#^l-smooth-first-order-bound|Proposition 12]] may hold, but it is hard to prove.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $L > 0$. Assume $f \in \mathcal{C}^2$. $f$ is L-smooth iff $- L I \preceq \nabla^2 f(x) \preceq L I$ for any $x \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and $x^*$ is its global minimizer. $\frac{\|\nabla f(x)\|_2^2}{2L} \le f(x) - f(x^*) \le \frac{L}{2}\|x - x^*\|_2^2$ for any $x \in \mathbb{R}^n$.
:::

::: definition:Lipschitz continuous Hessian
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $M > 0$. For $f \in \mathcal{C}^2$, the Hessian of $f$ is Lipschitz continuous with constant $M$ if $\|\nabla^2 f(x) - \nabla^2 f(y)\| \leq M \|x - y\|$ for any $x, y \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^2$ and the Hessian of $f$ is Lipschitz continuous with constant $M$. $f(y) \leq f(x) + \nabla f(x)^T (y - x) + \frac{1}{2} (y - x)^T \nabla^2 f(x) (y - x) + \frac{1}{6}M\|y-x\|^3$.
:::

### Convex
::: definition:Convex function
Let $f : \mathbb{R}^n \to \mathbb{R}$. $f$ is convex if $f( (1 - \alpha) x + \alpha y ) \leq (1 - \alpha) f(x) + \alpha f(y)$ for any $x, y \in \mathbb{R}^n$ and $\alpha \in [0, 1]$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$. Assume $f \in \mathcal{C}^1$. $f$ is convex iff $f(y) \geq f(x) + \nabla f(x)^T (y - x)$ for any $x, y \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$. $f$ is convex iff $\nabla^2 f(x) \succeq 0$ for any $x \in \mathbb{R}^n$.
:::

::: proposition
Let $D \subseteq \mathbb{R}^n$ and $f : D \to \mathbb{R}$. Assume $f$ is convex and $D$ is convex. Then the set of global minimizers of $f$ is convex.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ and $f$ is convex. If $\nabla f(x^*) = 0$, then $x^*$ is a global minimizer of $f$.
:::

### Strongly Convex
::: definition:Strongly convex
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $m > 0$. $f$ is strongly convex with modulus $m$ if $f( (1 - \alpha) x + \alpha y ) \leq (1 - \alpha) f(x) + \alpha f(y) - \frac{1}{2} m \alpha (1 - \alpha) \| x - y \|^2$ for any $x, y \in \mathbb{R}^n$ and $\alpha \in [0, 1]$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$. Assume $f \in \mathcal{C}^1$. $f$ is strongly convex with modulus $m$ iff $f(y) \geq f(x) + \nabla f(x)^T (y - x) + \frac{m}{2} \| y - x \|^2$ for any $x, y \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$. Assume $f \in \mathcal{C}^2$. $f$ is strongly convex with modulus $m$ iff $\nabla^2 f(x) \succeq m I$ for any $x \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ and $f$ is strongly convex. If $\nabla f(x^*) = 0$, then $x^*$ is the unique global minimizer of $f$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ is strongly convex with modulus $m$ and $x^*$ is its global minimizer. $\frac{m}{2}\|x-x^{*}\|^{2}_{x} \leqslant f(x)-f(x^{*}) \leqslant \frac{\|\nabla f(x)\|^2}{2m}$.
:::

::: definition:Polyak-Łojasiewicz condition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$ a minimizer of $f$, and $m > 0$. $f$ satisfies the Polyak-Łojasiewicz condition with constant $m$ if $f(x) - f(x^*) \leq \frac{\|\nabla f(x)\|^2}{2m}$ for any $x \in \mathbb{R}^n$.
:::

::: note
Strong convexity implies Polyak-Łojasiewicz condition, but the converse fails.
:::

## Sufficient Gradient Descent
::: definition:Sufficient decrease property
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The sequence has the sufficient decrease property with constant $\beta > 0$ if $f(x_{k + 1}) \leq f(x_k) - \frac{\beta}{2}\|\nabla f(x_k)\|^2$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $\bar{f} \in \mathbb{R}$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$, $f(x) \geq \bar{f}$ for any $x \in \mathbb{R}^n$, and $\{x_k\}$ has the sufficient decrease property with constant $\beta$. $\underset{0 \leq k \leq T - 1}{\min}\|\nabla f(x_k)\| \leq \sqrt{\frac{2(f(x_0) - \bar{f})}{\beta T}}$ and $\underset{k \to \infty}{\lim}\|\nabla f(x_k)\| = 0$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ is convex, $x^*$ is its global minimizer, $\{x_k\}$ has the sufficient decrease property with constant $\beta$, and $R_0 = \underset{f(x) \leq f(x_0)}{\sup}\|x - x^*\| > 0$.  $f(x_T) - f(x^*) \leq \frac{2R_0^2}{\beta T}$ for $T \geq 1$.
::: ^sufficient-decrease-convex-rate

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$, and $\{x_k\}$ be a sequence in $\mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ has Polyak-Łojasiewicz condition with constant $m$, $x^*$ is its global minimizer, $\{x_k\}$ has the sufficient decrease property with constant $\beta$, and $0 < m\beta \leq 1$. $f(x_T) - f(x^*) \leq (1 - m\beta)^T(f(x_0) - f(x^*))$.
:::

### Gradient Descent
::: definition:Descent direction
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. $d$ is a descent direction for $f$ at $x$ if $f(x + t d) < f(x)$ for all $t > 0$ sufficiently small.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. If $d^T \nabla f(x) < 0$, then $d$ is a descent direction for $f$ at $x$.
:::

::: definition:Gradient descent method
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha_k > 0$ for $k \geq 0$. Assume $f \in \mathcal{C}^1$. The gradient descent method generates the iterates $x_{k + 1} = x_k - \alpha_k\nabla f(x_k)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_{k + 1}) \leq f(x_k) - \alpha\left(1 - \frac{L\alpha}{2}\right)\|\nabla f(x_k)\|^2 \leq f(x_k) - \frac{\alpha}{2}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \alpha$.
::: ^lemma-0fb324

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is convex and $L$-smooth, $x^*$ is its global minimizer, and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_T) - f(x^*) \leq \frac{\|x_0 - x^*\|^2}{2\alpha T}$ for $T \geq 1$.
::: ^gradient-descent-convex-rate

::: note
With $\beta = \alpha$ and the same radius, the gradient descent bound has $\frac{1}{4}$ of the constant in the general sufficient decrease bound, which uses the Cauchy-Schwarz inequality.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, $x^*$ is its global minimizer, and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_{k}) - f(x^*) \leq (1 - m\alpha)^{T}(f(x_0) - f(x^*))$.
:::

### Other Descent Methods
::: definition:Preconditioned gradient descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $S_k \in \mathbb{R}^{n, n}$, and $\alpha_k > 0$. Assume $f \in \mathcal{C}^1$ and $S_k = S_k^T \succ 0$. Preconditioned gradient descent generates the iterates $x_{k + 1} = x_k - \alpha_k S_k\nabla f(x_k)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $S_k \in \mathbb{R}^{n, n}$, and $s_{\min}, s_{\max}, \alpha > 0$. Assume $f$ is $L$-smooth, $S_k = S_k^T$ and $s_{\min}I \preceq S_k \preceq s_{\max}I$, and $\alpha \leq \frac{s_{\min}}{Ls_{\max}^2}$. Set $x_{k + 1} = x_k - \alpha S_k\nabla f(x_k)$. $f(x_{k + 1}) \leq f(x_k) - \left(\alpha s_{\min} - \frac{L\alpha^2s_{\max}^2}{2}\right)\|\nabla f(x_k)\|^2 \leq f(x_k) - \frac{\alpha s_{\min}}{2}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \alpha s_{\min}$.
:::

::: note
When $\nabla^2 f(x_k) \succ 0$, the Newton direction is the preconditioned gradient direction with $S_k = (\nabla^2 f(x_k))^{-1}$.
:::

::: definition:Gauss-Southwell coordinate descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $e_i$ be the $i$th standard basis vector, and $\alpha_k > 0$. Assume $f \in \mathcal{C}^1$. Gauss-Southwell coordinate descent chooses $i_k \in \underset{1 \leq i \leq n}{\arg\max}|\partial_i f(x_k)|$ and generates $x_{k + 1} = x_k - \alpha_k\partial_{i_k}f(x_k)e_{i_k}$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth. Set $\{x_k\}$ as the Gauss-Southwell coordinate descent iterates with $\alpha_k = \frac{1}{L}$. $f(x_{k + 1}) \leq f(x_k) - \frac{|\partial_{i_k}f(x_k)|^2}{2L} \leq f(x_k) - \frac{1}{2Ln}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \frac{1}{Ln}$.
:::

::: definition:Uniform coordinate sampling
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $e_i$ be the $i$th standard basis vector, and $\alpha_k > 0$. Assume $f \in \mathcal{C}^1$. Uniform coordinate sampling draws $i_k$ uniformly from $\{1, \ldots, n\}$ independently of previous draws and generates $x_{k + 1} = x_k - \alpha_k\partial_{i_k}f(x_k)e_{i_k}$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth. Set $\{x_k\}$ as the uniform coordinate sampling iterates with $\alpha_k = \frac{1}{L}$. The sequence satisfies sufficient decrease in conditional expectation: $\mathbb{E}[f(x_{k + 1}) \mid x_k] \leq f(x_k) - \frac{1}{2Ln}\|\nabla f(x_k)\|^2$.
:::

::: definition:Stochastic gradient descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $v_k$ be random vectors in $\mathbb{R}^n$, and $\alpha_k > 0$. Assume $f \in \mathcal{C}^1$ and $\mathbb{E}[v_k \mid x_k] = \nabla f(x_k)$. Stochastic gradient descent generates the iterates $x_{k + 1} = x_k - \alpha_k v_k$.
:::

::: note
Stochastic gradient descent does not generally satisfy the sufficient decrease property. If $f$ is $L$-smooth, $\alpha_k = \alpha > 0$, and $\mathbb{E}[\|v_k - \nabla f(x_k)\|^2 \mid x_k] \leq \sigma^2$, then $\mathbb{E}[f(x_{k + 1}) \mid x_k] \leq f(x_k) - \alpha\left(1 - \frac{L\alpha}{2}\right)\|\nabla f(x_k)\|^2 + \frac{L\alpha^2\sigma^2}{2}.$ The variance term also prevents a general sufficient decrease guarantee in expectation.
:::

### Steplength Selection
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
:::

::: definition:Extrapolation and bisection for weak Wolfe conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$, $\nabla f(x_k)^T d_k < 0$, and $f$ is bounded below along the ray $x_k + \alpha d_k$ for $\alpha > 0$. Set $\ell = 0$, $u = +\infty$, and $\alpha = 1$. If $f(x_k + \alpha d_k) > f(x_k) + c_1\alpha\nabla f(x_k)^T d_k$, replace $u$ by $\alpha$ and replace $\alpha$ by $\frac{\ell + u}{2}$. Otherwise, if $\nabla f(x_k + \alpha d_k)^T d_k < c_2\nabla f(x_k)^T d_k$, replace $\ell$ by $\alpha$ and replace $\alpha$ by $2\ell$ if $u = +\infty$, or by $\frac{\ell + u}{2}$ if $u < +\infty$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, d_k \in \mathbb{R}^n$, and $\alpha_k > 0$. Assume $f$ is $L$-smooth, $d_k$ satisfies the line-search direction conditions with constants $\varepsilon, \gamma_1, \gamma_2$, and $\alpha_k$ satisfies the weak Wolfe conditions with constants $c_1, c_2$. Set $x_{k + 1} = x_k + \alpha_k d_k$. $f(x_{k + 1}) \leq f(x_k) - \frac{c_1(1 - c_2)\varepsilon^2}{L}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \frac{2c_1(1 - c_2)\varepsilon^2}{L}$.
:::

### Second-Order Descent
::: definition:Approximate second-order necessary point
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$. $x$ is an approximate second-order necessary point if $\|\nabla f(x)\| \leq \varepsilon_g$ and $\lambda_{\min}(\nabla^2 f(x)) \geq -\varepsilon_H$.
:::

::: definition:Gradient and negative-curvature descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth and its Hessian is Lipschitz continuous with constant $M$. Set $g_k = \nabla f(x_k)$ and $H_k = \nabla^2 f(x_k)$.
Gradient and negative-curvature descent takes $x_{k + 1} = x_k - \frac{1}{L}g_k$ if $\|g_k\| > \varepsilon_g$. Otherwise, compute $\lambda_k = \lambda_{\min}(H_k)$. If $\lambda_k < -\varepsilon_H$, choose $p_k$ s.t. $\|p_k\| = 1$, $H_k p_k = \lambda_k p_k$, and $g_k^T p_k \leq 0$, and take $x_{k + 1} = x_k + \frac{2|\lambda_k|}{M}p_k$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $\bar{f} \in \mathbb{R}$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth and its Hessian is Lipschitz continuous with constant $M$. Set $\{x_k\}$ as the gradient and negative-curvature descent iterates with tolerances $\varepsilon_g, \varepsilon_H$.
If iteration $k$ takes a gradient step, then $f(x_{k + 1}) \leq f(x_k) - \frac{\|\nabla f(x_k)\|^2}{2L} \leq f(x_k) - \frac{\varepsilon_g^2}{2L}$. If it takes a negative-curvature step, then $f(x_{k + 1}) \leq f(x_k) - \frac{2|\lambda_k|^3}{3M^2} \leq f(x_k) - \frac{2\varepsilon_H^3}{3M^2}$, where $\lambda_k = \lambda_{\min}(\nabla^2 f(x_k))$. The sequence has the sufficient decrease property with constant $\beta = \min\left\{\frac{1}{L}, \frac{4\varepsilon_H^3}{3M^2\varepsilon_g^2}\right\}$.
::: ^negative-curvature-decrease

### Mirror Descent
::: definition:Bregman divergence
Let $h : \mathbb{R}^n \to \mathbb{R}$ and $x, z \in \mathbb{R}^n$. For $h \in \mathcal{C}^1$ strongly convex, the Bregman divergence generated by $h$ is $D_h(x, z) = h(x) - h(z) - \nabla h(z)^T(x - z)$.
:::

::: proposition
Let $h : \mathbb{R}^n \to \mathbb{R}$ and $x, y, z \in \mathbb{R}^n$. Assume $h \in \mathcal{C}^1$ is strongly convex. $D_h(x, y) = D_h(x, z) + D_h(z, y) - (\nabla h(y) - \nabla h(z))^T(x - z)$.
:::

::: definition:Mirror descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $h : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha_k > 0$. For $h \in \mathcal{C}^1$ strongly convex, mirror descent generates the iterates $x_{k + 1} = \underset{x \in \mathbb{R}^n}{\arg\min} \left[f(x_k) + \nabla f(x_k)^T(x - x_k) + \frac{1}{\alpha_k}D_h(x, x_k)\right]$, equivalently $x_{k + 1} = (\nabla h)^{-1}(\nabla h(x_k) - \alpha_k \nabla f(x_k))$.
:::

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathcal{X} \to \mathbb{R}$, $h : \mathcal{X} \to \mathbb{R}$, $x_k \in \mathcal{X}$, and $\alpha_k > 0$. Assume $\mathcal{X}$ is convex, $f \in \mathcal{C}^1$, and $h \in \mathcal{C}^1$ is strongly convex. Set $x_{k + 1} = \underset{x \in \mathcal{X}}{\arg\min} \left[f(x_k) + \nabla f(x_k)^T(x - x_k) + \frac{1}{\alpha_k}D_h(x, x_k)\right]$. $\left(\nabla f(x_k) + \frac{1}{\alpha_k}\nabla h(x_{k + 1}) - \frac{1}{\alpha_k}\nabla h(x_k)\right)^T(x - x_{k + 1}) \geq 0$ for any $x \in \mathcal{X}$.
:::

::: proposition
Let $f : \mathcal{X} \to \mathbb{R}$, $\mathcal{X} \subseteq \mathbb{R}^n$, $\|\cdot\|$ be a norm on $\mathcal{X}$, $h : \mathcal{X} \to \mathbb{R}$, $x^* \in \mathcal{X}$, $x_0 \in \mathcal{X}$, and $\{\alpha_t\}$ be a steplength sequence. Assume $\mathcal{X}$ is convex, $\alpha_t > 0$ for any $t$, $h$ is strongly convex with modulus $m$ w.r.t. $\|\cdot\|$, $f$ is convex and $L$-Lipschitz continuous w.r.t. $\|\cdot\|$, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $\{x_t\}$ as the mirror-descent iterates confined to $\mathcal{X}$. $f(\bar{x}_T) - f(x^*) \leq \frac{D_h(x^*, x_0) + \frac{L^2}{2m}\sum_{t = 0}^{T} \alpha_t^2}{\sum_{t = 0}^{T} \alpha_t}$ where $\bar{x}_T = \left(\sum_{t = 0}^{T} \alpha_t\right)^{-1}\sum_{t = 0}^{T} \alpha_t x_t$ for any integer $T \geq 1$.
:::

::: corollary
Assume the hypotheses of the mirror-descent convergence theorem and $D_h(x^*, x_0) \leq R$. If $\alpha_t = \frac{\sqrt{2mR}}{L\sqrt{T + 1}}$ for $0 \leq t \leq T$, then $f(\bar{x}_T) - f(x^*) \leq \frac{L\sqrt{2R}}{\sqrt{m}\sqrt{T + 1}}$ for any integer $T \geq 1$.
:::
