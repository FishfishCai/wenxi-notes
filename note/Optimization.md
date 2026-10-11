## Foundations
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

## Upper Bound Tools
### Lipschitz Continuity
::: definition:Lipschitz continuous
Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $L > 0$. $f$ is Lipschitz continuous with constant $L$ if $\| f(x) - f(y) \| \leq L \| x - y \|$ for any $x, y \in \mathbb{R}^n$.
:::

### L-smooth
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

### Lipschitz Continuous Hessian
::: definition:Lipschitz continuous Hessian
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $M > 0$. For $f \in \mathcal{C}^2$, the Hessian of $f$ is Lipschitz continuous with constant $M$ if $\|\nabla^2 f(x) - \nabla^2 f(y)\| \leq M \|x - y\|$ for any $x, y \in \mathbb{R}^n$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^2$ and the Hessian of $f$ is Lipschitz continuous with constant $M$. $f(y) \leq f(x) + \nabla f(x)^T (y - x) + \frac{1}{2} (y - x)^T \nabla^2 f(x) (y - x) + \frac{1}{6}M\|y-x\|^3$.
:::

## Lower Bound Tools
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

### Polyak-Łojasiewicz Condition
::: definition:Polyak-Łojasiewicz condition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^* \in \mathbb{R}^n$ a minimizer of $f$, and $m > 0$. $f$ satisfies the Polyak-Łojasiewicz condition with constant $m$ if $f(x) - f(x^*) \leq \frac{\|\nabla f(x)\|^2}{2m}$ for any $x \in \mathbb{R}^n$.
:::

::: note
Strong convexity implies Polyak-Łojasiewicz condition, but the converse fails.
:::

## Upper Bound Method
### Descent Direction
::: definition:Descent direction
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. $d$ is a descent direction for $f$ at $x$ if $f(x + t d) < f(x)$ for all $t > 0$ sufficiently small.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$ and $d \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. If $d^T \nabla f(x) < 0$, then $d$ is a descent direction for $f$ at $x$.
:::

### Sufficient Decrease
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

### Gradient Descent
::: definition:Gradient descent method
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha_k > 0$ for $k \geq 0$. Assume $f \in \mathcal{C}^1$. The gradient descent method generates the iterates $x_{k + 1} = x_k - \alpha_k\nabla f(x_k)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_{k + 1}) \leq f(x_k) - \alpha\left(1 - \frac{L\alpha}{2}\right)\|\nabla f(x_k)\|^2 \leq f(x_k) - \frac{\alpha}{2}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \alpha$.
::: ^lemma-0fb324

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is convex and $L$-smooth, $x^*$ is its global minimizer, and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_T) - f(x^*) \leq \frac{\|x_0 - x^*\|^2}{2\alpha T}$ for $T \geq 1$. In particular, $f(x_T) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \frac{\|x_0 - x^*\|^2}{2\alpha\varepsilon}$.
::: ^gradient-descent-convex-rate

::: note
With $\beta = \alpha$ and the same radius, the gradient descent bound has $\frac{1}{4}$ of the constant in the general sufficient decrease bound, which uses the Cauchy-Schwarz inequality.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$ or has Polyak-Łojasiewicz condition with constant $m$, $x^*$ is its global minimizer, and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_{T}) - f(x^*) \leq (1 - m\alpha)^{T}(f(x_0) - f(x^*))$. In particular, $f(x_T) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \frac{1}{m\alpha}\ln\frac{f(x_0) - f(x^*)}{\varepsilon}$.
:::

### Reshaping the Upper Envelope
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

### Line Search for Guaranteed Decrease
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

### Cubic Upper Envelope
::: definition:Approximate second-order necessary point
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$. $x$ is an approximate second-order necessary point if $\|\nabla f(x)\| \leq \varepsilon_g$ and $\lambda_{\min}(\nabla^2 f(x)) \geq -\varepsilon_H$.
:::

::: definition:Gradient and negative-curvature descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth and its Hessian is Lipschitz continuous with constant $M$.
Gradient and negative-curvature descent takes $x_{k + 1} = x_k - \frac{1}{L}\nabla f(x_k)$ if $\|\nabla f(x_k)\| > \varepsilon_g$. Otherwise, compute $\lambda_k = \lambda_{\min}(\nabla^2 f(x_k))$. If $\lambda_k < -\varepsilon_H$, choose $p_k$ s.t. $\|p_k\| = 1$, $\nabla^2 f(x_k)p_k = \lambda_k p_k$, and $\nabla f(x_k)^T p_k \leq 0$, and take $x_{k + 1} = x_k + \frac{2|\lambda_k|}{M}p_k$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $\bar{f} \in \mathbb{R}$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth, its Hessian is Lipschitz continuous with constant $M$, and $f(x) \geq \bar{f}$ for any $x \in \mathbb{R}^n$. Set $\{x_k\}$ as the gradient and negative-curvature descent iterates with tolerances $\varepsilon_g, \varepsilon_H$.
If iteration $k$ takes a gradient step, then $f(x_{k + 1}) \leq f(x_k) - \frac{\|\nabla f(x_k)\|^2}{2L} \leq f(x_k) - \frac{\varepsilon_g^2}{2L}$. If it takes a negative-curvature step, then $f(x_{k + 1}) \leq f(x_k) - \frac{2|\lambda_k|^3}{3M^2} \leq f(x_k) - \frac{2\varepsilon_H^3}{3M^2}$, where $\lambda_k = \lambda_{\min}(\nabla^2 f(x_k))$. The sequence has the sufficient decrease property with constant $\beta = \min\left\{\frac{1}{L}, \frac{4\varepsilon_H^3}{3M^2\varepsilon_g^2}\right\}$. In particular, $x_k$ is an approximate second-order necessary point for some integer $k \leq \frac{f(x_0) - \bar{f}}{\min\left\{\frac{\varepsilon_g^2}{2L}, \frac{2\varepsilon_H^3}{3M^2}\right\}}$.
::: ^negative-curvature-decrease

### Decrease in Expectation
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

## Accumulating Lower Bounds
### Bregman Divergence
::: definition:Bregman divergence
Let $h : \mathbb{R}^n \to \mathbb{R}$ and $x, z \in \mathbb{R}^n$. For $h \in \mathcal{C}^1$ strongly convex, the Bregman divergence generated by $h$ is $D_h(x, z) = h(x) - h(z) - \nabla h(z)^T(x - z)$.
:::

::: proposition
Let $h : \mathbb{R}^n \to \mathbb{R}$ and $x, y, z \in \mathbb{R}^n$. Assume $h \in \mathcal{C}^1$ is strongly convex. $D_h(x, y) = D_h(x, z) + D_h(z, y) - (\nabla h(y) - \nabla h(z))^T(x - z)$.
:::

### Mirror Descent
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
Assume the hypotheses of the mirror-descent convergence theorem and $D_h(x^*, x_0) \leq R$. If $\alpha_t = \frac{\sqrt{2mR}}{L\sqrt{T + 1}}$ for $0 \leq t \leq T$, then $f(\bar{x}_T) - f(x^*) \leq \frac{L\sqrt{2R}}{\sqrt{m}\sqrt{T + 1}}$ for any integer $T \geq 1$. In particular, $f(\bar{x}_T) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $T \geq \max\left\{1, \frac{2L^2R}{m\varepsilon^2} - 1\right\}$.
:::

### Accelerated Gradient Descent
::: definition:Accelerated gradient descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $\alpha_k > 0$, and $\beta_k \geq 0$ for $k \geq 0$. Assume $f \in \mathcal{C}^1$. Set $x_{-1} = x_0$. Accelerated gradient descent generates the iterates $y_k = x_k + \beta_k(x_k - x_{k - 1})$ and $x_{k + 1} = y_k - \alpha_k\nabla f(y_k)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ is its global minimizer. Set $\kappa = \frac{L}{m}$ and $\{x_k\}$ as the accelerated gradient descent iterates with $\alpha_k = \frac{1}{L}$ and $\beta_k = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. $f(x_K) - f(x^*) \leq \frac{L + m}{2}\|x_0 - x^*\|^2\left(1 - \frac{1}{\sqrt{\kappa}}\right)^K$ for any integer $K \geq 1$. In particular, $f(x_K) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $K \geq \sqrt{\kappa}\ln\frac{(L + m)\|x_0 - x^*\|^2}{2\varepsilon}$.
:::

::: note
At $y_k$, for $t \in \mathbb{R}^n$,
$$\begin{aligned} U_k(t) &= f(y_k) + \nabla f(y_k)^T(t - y_k) + \frac{L}{2}\|t - y_k\|^2 \\ &= \frac{L}{2}\left\|t - \left(y_k - \frac{1}{L}\nabla f(y_k)\right)\right\|^2 + f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2L}. \end{aligned}$$
$U_k(t)$ reaches its minimum at $u_k = y_k - \frac{1}{L}\nabla f(y_k)$.
$$\begin{aligned} L_k(t) &= f(y_k) + \nabla f(y_k)^T(t - y_k) + \frac{m}{2}\|t - y_k\|^2 \\ &= \frac{m}{2}\left\|t - \left(y_k - \frac{1}{m}\nabla f(y_k)\right)\right\|^2 + f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2m}. \end{aligned}$$
$L_k(t)$ reaches its minimum at $l_k = y_k - \frac{1}{m}\nabla f(y_k)$.
$f(x^*)$ is between $L_k(l_k)$ and $f(u_k)$. To obtain $f(x^*)$, we can accumulate $L_k$ using $V_k = (1 - q)V_{k - 1} + qL_k$.
Suppose $V_{k - 1}(t) = \frac{m}{2}\|t - v_{k - 1}\|^2 + c_{k - 1}$.
$$\begin{aligned} V_k(t) &= (1 - q)\left[\frac{m}{2}\|t - v_{k - 1}\|^2 + c_{k - 1}\right] + q\left[\frac{m}{2}\|t - l_k\|^2 + f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2m}\right] \\ &= \frac{m}{2}\|t - ((1 - q)v_{k - 1} + ql_k)\|^2 \\ &\quad + (1 - q)c_{k - 1} + q\left[f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2m}\right] + \frac{m}{2}q(1 - q)\|v_{k - 1} - l_k\|^2. \end{aligned}$$
Set
$$\begin{aligned} v_k &= (1 - q)v_{k - 1} + ql_k, \\ c_k &= (1 - q)c_{k - 1} + q\left[f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2m}\right] + \frac{m}{2}q(1 - q)\|v_{k - 1} - l_k\|^2, \end{aligned}$$
so $V_k(t) = \frac{m}{2}\|t - v_k\|^2 + c_k$. We combine $u_k$ and $v_k$ into the new query point $y_{k + 1} = (1 - \tau)u_k + \tau v_k$.
The target is $f(u_k) - c_k \leq p[f(u_{k - 1}) - c_{k - 1}]$. If $u_{k - 1} = v_{k - 1} = x^*$ and $c_{k - 1} < f(x^*)$, then $y_k = x^*$, $c_k = (1 - q)c_{k - 1} + qf(x^*)$, and $f(u_k) - c_k = (1 - q)[f(u_{k - 1}) - c_{k - 1}]$, implying $p \geq 1 - q$.
With $p = 1 - q$, the target $f(u_k) - c_k \leq (1 - q)[f(u_{k - 1}) - c_{k - 1}]$ is equivalent to
$$f(u_k) - q\left[f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2m}\right] - \frac{m}{2}q(1 - q)\|v_{k - 1} - l_k\|^2 - (1 - q)f(u_{k - 1}) \leq 0.$$
Substituting the bounds from $L$-smoothness and strong convexity
$$\begin{aligned} f(u_k) &\leq U_k(u_k) = f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2L}, \\ f(u_{k - 1}) &\geq L_k(u_{k - 1}), \end{aligned}$$
it suffices that
$$\begin{aligned} &-\frac{\|\nabla f(y_k)\|^2}{2L} - (1 - q)\nabla f(y_k)^T(u_{k - 1} - y_k) - \frac{m}{2}(1 - q)\|u_{k - 1} - y_k\|^2 \\ &+ \frac{q}{2m}\|\nabla f(y_k)\|^2 - \frac{m}{2}q(1 - q)\|v_{k - 1} - l_k\|^2 \leq 0. \end{aligned}$$
Expanding $y_k = (1 - \tau)u_{k - 1} + \tau v_{k - 1}$ and $l_k = y_k - \frac{1}{m}\nabla f(y_k)$, and expressing everything only with $u_{k - 1}$, $v_{k - 1}$ and $\nabla f(y_k)$,
$$\begin{aligned} &\left(\frac{q^2}{2m} - \frac{1}{2L}\right)\|\nabla f(y_k)\|^2 - (1 - q)\left[\tau - q(1 - \tau)\right]\nabla f(y_k)^T(u_{k - 1} - v_{k - 1}) \\ &- \frac{m}{2}(1 - q)\left[\tau^2 + q(1 - \tau)^2\right]\|u_{k - 1} - v_{k - 1}\|^2 \leq 0. \end{aligned}$$
We have
$$q = \frac{1}{\sqrt{\kappa}}, \qquad \tau = \frac{q}{1 + q} = \frac{1}{1 + \sqrt{\kappa}},$$
where $\kappa = \frac{L}{m}$, $q$ is the largest value making the coefficient of $\|\nabla f(y_k)\|^2$ nonpositive, and $\tau$ makes the coefficient of $\nabla f(y_k)$ vanish. 
For the rate, take $v_{-1} = u_{-1}$ and $c_{-1} = f(u_{-1})$, so the contraction gives $f(u_k) \leq c_k$.
Evaluating $V_k = (1 - q)V_{k - 1} + qL_k$ at $x^*$ with $L_k(x^*) \leq f(x^*)$ shows that $V_k(x^*) - f(x^*)$ shrinks by $1 - q$ per step. With $f(u_{-1}) - f(x^*) \leq \frac{L}{2}\|u_{-1} - x^*\|^2$,
$$\begin{aligned} f(u_k) - f(x^*) &\leq V_k(x^*) - f(x^*) \leq (1 - q)^{k + 1}\left[f(u_{-1}) - f(x^*) + \frac{m}{2}\|u_{-1} - x^*\|^2\right] \\ &\leq \frac{L + m}{2}\|u_{-1} - x^*\|^2\left(1 - \frac{1}{\sqrt{\kappa}}\right)^{k + 1}. \end{aligned}$$
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is convex and $L$-smooth, and $x^*$ is its global minimizer. Set $\lambda_0 = 0$, $\lambda_{k + 1} = \frac{1 + \sqrt{1 + 4\lambda_k^2}}{2}$ for $k \geq 0$, and $\{x_k\}$ as the accelerated gradient descent iterates with $\alpha_k = \frac{1}{L}$, $\beta_0 = 0$, and $\beta_k = \frac{\lambda_k - 1}{\lambda_{k + 1}}$ for $k \geq 1$. $f(x_K) - f(x^*) \leq \frac{2L\|x_0 - x^*\|^2}{(K + 1)^2}$ for any integer $K \geq 1$. In particular, $f(x_K) - f(x^*) \leq \varepsilon$ for any $\varepsilon > 0$ and integer $K \geq \|x_0 - x^*\|\sqrt{\frac{2L}{\varepsilon}}$.
:::

::: note
At $y_k$, for $t \in \mathbb{R}^n$,
$$\begin{aligned} U_k(t) &= f(y_k) + \nabla f(y_k)^T(t - y_k) + \frac{L}{2}\|t - y_k\|^2 \\ &= \frac{L}{2}\left\|t - \left(y_k - \frac{1}{L}\nabla f(y_k)\right)\right\|^2 + f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2L}. \end{aligned}$$
$U_k(t)$ reaches its minimum at $u_k = y_k - \frac{1}{L}\nabla f(y_k)$.
$$L_k(t) = f(y_k) + \nabla f(y_k)^T(t - y_k).$$
$f(x^*)$ is between $L_k(x^*)$ and $f(u_k)$. To obtain $f(x^*)$, we can accumulate $L_k$ using $V_k = (1 - q_k)V_{k - 1} + q_kL_k$ with decreasing $q_k \in (0, 1]$. Suppose$V_{-1}(t) = \frac{\gamma_{-1}}{2}\|t - x_0\|^2 + f(x_0)$ and $V_{k - 1}(t) = \frac{\gamma_{k - 1}}{2}\|t - v_{k - 1}\|^2 + c_{k - 1}$ and let $\gamma_k = (1 - q_k)\gamma_{k - 1}$.
$$\begin{aligned} V_k(t) &= (1 - q_k)\left[\frac{\gamma_{k - 1}}{2}\|t - v_{k - 1}\|^2 + c_{k - 1}\right] + q_k\left[f(y_k) + \nabla f(y_k)^T(t - y_k)\right] \\ &= \frac{\gamma_k}{2}\left\|t - \left(v_{k - 1} - \frac{q_k}{\gamma_k}\nabla f(y_k)\right)\right\|^2 \\ &\quad + (1 - q_k)c_{k - 1} + q_k\left[f(y_k) + \nabla f(y_k)^T(v_{k - 1} - y_k)\right] - \frac{q_k^2}{2\gamma_k}\|\nabla f(y_k)\|^2. \end{aligned}$$
Set
$$\begin{aligned} v_k &= v_{k - 1} - \frac{q_k}{\gamma_k}\nabla f(y_k), \\ c_k &= (1 - q_k)c_{k - 1} + q_k\left[f(y_k) + \nabla f(y_k)^T(v_{k - 1} - y_k)\right] - \frac{q_k^2}{2\gamma_k}\|\nabla f(y_k)\|^2, \end{aligned}$$
so $V_k(t) = \frac{\gamma_k}{2}\|t - v_k\|^2 + c_k$. We combine $u_k$ and $v_k$ into the new query point $y_{k + 1} = (1 - \tau_{k + 1})u_k + \tau_{k + 1}v_k$.
The target is $f(u_k) - c_k \leq p_k[f(u_{k - 1}) - c_{k - 1}]$. If $u_{k - 1} = v_{k - 1} = x^*$ and $c_{k - 1} < f(x^*)$, then $y_k = x^*$, $c_k = (1 - q_k)c_{k - 1} + q_kf(x^*)$, and $f(u_k) - c_k = (1 - q_k)[f(u_{k - 1}) - c_{k - 1}]$, implying $p_k \geq 1 - q_k$.
With $p_k = 1 - q_k$, the target $f(u_k) - c_k \leq (1 - q_k)[f(u_{k - 1}) - c_{k - 1}]$ is equivalent to
$$f(u_k) - q_k\left[f(y_k) + \nabla f(y_k)^T(v_{k - 1} - y_k)\right] + \frac{q_k^2}{2\gamma_k}\|\nabla f(y_k)\|^2 - (1 - q_k)f(u_{k - 1}) \leq 0.$$
Substituting the bounds from $L$-smoothness and convexity
$$\begin{aligned} f(u_k) &\leq U_k(u_k) = f(y_k) - \frac{\|\nabla f(y_k)\|^2}{2L}, \\ f(u_{k - 1}) &\geq L_k(u_{k - 1}), \end{aligned}$$
it suffices that
$$\begin{aligned} &-\frac{\|\nabla f(y_k)\|^2}{2L} - (1 - q_k)\nabla f(y_k)^T(u_{k - 1} - y_k) \\ &- q_k\nabla f(y_k)^T(v_{k - 1} - y_k) + \frac{q_k^2}{2\gamma_k}\|\nabla f(y_k)\|^2 \leq 0. \end{aligned}$$
Expanding $y_k = (1 - \tau_k)u_{k - 1} + \tau_kv_{k - 1}$, and expressing everything only with $u_{k - 1}$, $v_{k - 1}$ and $\nabla f(y_k)$,
$$\left(\frac{q_k^2}{2\gamma_k} - \frac{1}{2L}\right)\|\nabla f(y_k)\|^2 - (\tau_k - q_k)\nabla f(y_k)^T(u_{k - 1} - v_{k - 1}) \leq 0.$$
We have
$$q_k^2 = \frac{\gamma_k}{L} = (1 - q_k)\frac{\gamma_{k - 1}}{L}, \qquad \tau_k = q_k,$$
where $q_k$ is the largest value making the coefficient of $\|\nabla f(y_k)\|^2$ nonpositive, which decreases in $k$ since $\gamma_k$ decreases, and $\tau_k$ makes the coefficient of $\nabla f(y_k)$ vanish.
Writing $q_k = \frac{1}{\lambda_{k + 1}}$ with $\lambda_0^2 = \frac{L}{\gamma_{-1}}$, the rule for $q_k$ becomes
$$\lambda_{k + 1}^2 - \lambda_{k + 1} = \lambda_k^2,$$
letting $\gamma_{-1} \to \infty$ gives $\lambda_0 = 0$, and eliminating $v_k$ gives $\alpha_k = \frac{1}{L}$ and $\beta_k = \frac{\lambda_k - 1}{\lambda_{k + 1}}$ with $x_{k + 1} = u_k$.
For the rate, with $v_{-1} = u_{-1}$ and $c_{-1} = f(u_{-1})$, the contraction gives $f(u_k) \leq c_k$.
Evaluating $V_k = (1 - q_k)V_{k - 1} + q_kL_k$ at $x^*$ with $L_k(x^*) \leq f(x^*)$ shows that $V_k(x^*) - f(x^*)$ shrinks by $1 - q_k$ per step, and $\prod_{i = 0}^{k}(1 - q_i) = \frac{\gamma_k}{\gamma_{-1}}$, so
$$f(u_k) - f(x^*) \leq V_k(x^*) - f(x^*) \leq \frac{\gamma_k}{\gamma_{-1}}\left[f(u_{-1}) - f(x^*)\right] + \frac{\gamma_k}{2}\|u_{-1} - x^*\|^2.$$
Letting $\gamma_{-1} \to \infty$ and using $\gamma_k = \frac{L}{\lambda_{k + 1}^2}$ and $\lambda_{k + 1} \geq \frac{k + 2}{2}$ gives $f(u_k) - f(x^*) \leq \frac{2L\|u_{-1} - x^*\|^2}{(k + 2)^2}$.
:::

### Regularization and Restarting
::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $R, \varepsilon > 0$. Assume $f$ is convex and $L$-smooth, $x^*$ is its global minimizer, and $\|x_0 - x^*\| \leq R$. Set $\mu = \frac{\varepsilon}{R^2}$, $F_\mu(x) = f(x) + \frac{\mu}{2}\|x - x_0\|^2$, $\kappa_\mu = \frac{L + \mu}{\mu}$, and $\{x_k\}$ as the accelerated gradient descent iterates for $F_\mu$ with $\alpha_k = \frac{1}{L + \mu}$ and $\beta_k = \frac{\sqrt{\kappa_\mu} - 1}{\sqrt{\kappa_\mu} + 1}$. $f(x_k) - f(x^*) \leq \frac{L + 2\mu}{2}R^2\left(1 - \frac{1}{\sqrt{\kappa_\mu}}\right)^k + \frac{\varepsilon}{2}$ for any integer $k \geq 1$, and $f(x_k) - f(x^*) \leq \varepsilon$ for any integer $k \geq \sqrt{1 + \frac{LR^2}{\varepsilon}}\ln\left(2 + \frac{LR^2}{\varepsilon}\right)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ is its global minimizer. Set $N = \left\lceil\sqrt{\frac{8L}{m}}\right\rceil$, $z_0 = x_0$, and $z_{t + 1}$ as the $N$th accelerated gradient descent iterate started from $z_t$ with $\alpha_k = \frac{1}{L}$, $\beta_0 = 0$, and $\beta_k = \frac{\lambda_k - 1}{\lambda_{k + 1}}$, where $\lambda_0 = 0$ and $\lambda_{k + 1} = \frac{1 + \sqrt{1 + 4\lambda_k^2}}{2}$. $f(z_t) - f(x^*) \leq 2^{-t}(f(x_0) - f(x^*))$ for any integer $t \geq 0$, and $f(z_T) - f(x^*) \leq \varepsilon$ after $NT$ gradient evaluations for any $\varepsilon > 0$ and integer $T \geq \log_2\frac{f(x_0) - f(x^*)}{\varepsilon}$.
:::

## Lower Complexity Bounds
::: theorem:Nesterov lower bound for convex functions
Let $L > 0$ and integers $K \geq 1$ and $n \geq 2K + 1$. There exist $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$ s.t. $f$ is convex and $L$-smooth, $x^*$ is its global minimizer, and $f(x_K) - f(x^*) \geq \frac{3L\|x_0 - x^*\|^2}{32(K + 1)^2}$ for any sequence $\{x_k\}$ with $x_0 = 0$ and $x_{k + 1} \in \operatorname{span}\{\nabla f(x_0), \ldots, \nabla f(x_k)\}$. In particular, $f(x_K) - f(x^*) \leq \varepsilon$ requires $K + 1 \geq \|x_0 - x^*\|\sqrt{\frac{3L}{32\varepsilon}}$ for any $\varepsilon > 0$.
:::

::: note
With $d = 2K + 1$ and $A_d \in \mathbb{R}^{d, d}$ tridiagonal with diagonal entries $2$ and off-diagonal entries $-1$, the bound holds for $f(x) = \frac{L}{8}x^TA_dx - \frac{L}{4}e_1^Tx$ on the first $d$ coordinates, whose minimizer is $x_i^* = 1 - \frac{i}{d + 1}$ for $1 \leq i \leq d$.
:::

::: theorem:Nesterov lower bound for strongly convex functions
Let $0 < m < L$, $\eta \in (0, 1)$, and an integer $K \geq 0$. Set $\kappa = \frac{L}{m}$ and $r = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. There exist an integer $n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^* \in \mathbb{R}^n$ s.t. $f$ is $L$-smooth and strongly convex with modulus $m$, $x^*$ is its global minimizer, and $f(x_K) - f(x^*) \geq (1 - \eta)\frac{m}{2}r^{2K}\|x_0 - x^*\|^2$ for any sequence $\{x_k\}$ with $x_0 = 0$ and $x_{k + 1} \in \operatorname{span}\{\nabla f(x_0), \ldots, \nabla f(x_k)\}$. In particular, $f(x_K) - f(x^*) \leq \varepsilon$ requires $K \geq \frac{\sqrt{\kappa} - 1}{4}\ln\frac{(1 - \eta)m\|x_0 - x^*\|^2}{2\varepsilon}$ for any $\varepsilon > 0$.
:::

::: note
With the same $A_d$ and $d$ large enough, the bound holds for $f(x) = \frac{L - m}{8}(x^TA_dx - 2e_1^Tx) + \frac{m}{2}\|x\|^2$, whose minimizer is $x_i^* = \frac{r^i - r^{2d + 2 - i}}{1 - r^{2d + 2}}$ for $1 \leq i \leq d$.
:::
