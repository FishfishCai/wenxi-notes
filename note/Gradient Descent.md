::: definition:Gradient descent method
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha_k > 0$ for $k \geq 0$. Assume $f \in \mathcal{C}^1$. The gradient descent method generates the iterates $x_{k + 1} = x_k - \alpha_k\nabla f(x_k)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\alpha > 0$. Assume $f$ is $L$-smooth and $\alpha \leq \frac{1}{L}$. Set $x_{k + 1} = x_k - \alpha\nabla f(x_k)$. $f(x_{k + 1}) \leq f(x_k) - \alpha\left(1 - \frac{L\alpha}{2}\right)\|\nabla f(x_k)\|^2 \leq f(x_k) - \frac{\alpha}{2}\|\nabla f(x_k)\|^2$. The sequence has the sufficient decrease property with constant $\beta = \alpha$.
::: ^lemma-0fb324

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is convex and $L$-smooth, and $x^*$ is its global minimizer. Set $x_{k + 1} = x_k - \frac{1}{L}\nabla f(x_k)$. $f(x_k) - f(x^*) \leq \frac{L}{2k}\|x_0 - x^*\|^2$ for any integer $k \geq 1$.
::: ^gradient-descent-convex-rate

*Proof.*
Smoothness and convexity give
$$
\begin{aligned}
f(x_{k + 1}) &\leq f(x_k) + \nabla f(x_k)^T(x_{k + 1} - x_k) + \frac{L}{2}\|x_{k + 1} - x_k\|^2, \\
f(x_k) &\leq f(x^*) + \nabla f(x_k)^T(x_k - x^*).
\end{aligned}
$$
Adding them, with $\nabla f(x_k) = L(x_k - x_{k + 1})$, gives
$$
\begin{aligned}
f(x_{k + 1}) - f(x^*) &\leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*) + \frac{L}{2}\|x_{k + 1} - x_k\|^2 \\
&= \frac{L}{2}\left(\|x_k - x^*\|^2 - \|x_{k + 1} - x^*\|^2\right).
\end{aligned}
$$
By [[#^lemma-0fb324|Proposition 2]], $f(x_k)$ is nonincreasing, so summing over $0, \ldots, k - 1$ gives
$$
k(f(x_k) - f(x^*)) \leq \sum_{j = 0}^{k - 1}(f(x_{j + 1}) - f(x^*)) \leq \frac{L}{2}\|x_0 - x^*\|^2.
$$

::: note
With $\beta = \frac{1}{L}$ and the same radius, [[#^gradient-descent-convex-rate|Proposition 3]] has $\frac{1}{4}$ of the constant in [[Sufficient Descent#^sufficient-decrease-convex-rate|Proposition 5]], which uses the Cauchy-Schwarz inequality.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ is its global minimizer. Set $x_{k + 1} = x_k - \frac{1}{L}\nabla f(x_k)$. $\|x_k - x^*\|^2 \leq \left(1 - \frac{m}{L}\right)^k\|x_0 - x^*\|^2$ for any integer $k \geq 0$.
:::

*Proof.*
Smoothness and strong convexity give
$$
\begin{aligned}
f(x_{k + 1}) &\leq f(x_k) + \nabla f(x_k)^T(x_{k + 1} - x_k) + \frac{L}{2}\|x_{k + 1} - x_k\|^2, \\
f(x_k) &\leq f(x^*) + \nabla f(x_k)^T(x_k - x^*) - \frac{m}{2}\|x_k - x^*\|^2.
\end{aligned}
$$
Adding them, with $\nabla f(x_k) = L(x_k - x_{k + 1})$, gives
$$
\begin{aligned}
0 \leq f(x_{k + 1}) - f(x^*) &\leq L(x_k - x_{k + 1})^T(x_{k + 1} - x^*) + \frac{L}{2}\|x_{k + 1} - x_k\|^2 - \frac{m}{2}\|x_k - x^*\|^2 \\
&= \frac{L - m}{2}\|x_k - x^*\|^2 - \frac{L}{2}\|x_{k + 1} - x^*\|^2,
\end{aligned}
$$
so $\|x_{k + 1} - x^*\|^2 \leq \left(1 - \frac{m}{L}\right)\|x_k - x^*\|^2$.

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ is its global minimizer. Set $x_{k + 1} = x_k - \frac{1}{L}\nabla f(x_k)$. $f(x_k) - f(x^*) \leq \left(1 - \frac{m}{L}\right)^k(f(x_0) - f(x^*))$ for any integer $k \geq 0$.
:::

*Proof.*
Smoothness gives
$$
f(x_{k + 1}) \leq f(x_k) + \nabla f(x_k)^T(x_{k + 1} - x_k) + \frac{L}{2}\|x_{k + 1} - x_k\|^2 = f(x_k) - \frac{1}{2L}\|\nabla f(x_k)\|^2.
$$
Strong convexity and completing the square give
$$
\begin{aligned}
f(x^*) &\geq f(x_k) + \nabla f(x_k)^T(x^* - x_k) + \frac{m}{2}\|x^* - x_k\|^2 \\
&= f(x_k) + \frac{m}{2}\left\|x^* - x_k + \frac{1}{m}\nabla f(x_k)\right\|^2 - \frac{1}{2m}\|\nabla f(x_k)\|^2 \\
&\geq f(x_k) - \frac{1}{2m}\|\nabla f(x_k)\|^2.
\end{aligned}
$$
Substituting $\|\nabla f(x_k)\|^2 \geq 2m(f(x_k) - f(x^*))$ into the first inequality gives $f(x_{k + 1}) - f(x^*) \leq \left(1 - \frac{m}{L}\right)(f(x_k) - f(x^*))$.

::: definition:Approximate second-order necessary point
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$. $x$ is an approximate second-order necessary point if $\|\nabla f(x)\| \leq \varepsilon_g$ and $\lambda_{\min}(\nabla^2 f(x)) \geq -\varepsilon_H$.
:::

::: definition:Gradient and negative-curvature descent
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth and its Hessian is Lipschitz continuous with constant $M$. Gradient and negative-curvature descent takes $x_{k + 1} = x_k - \frac{1}{L}\nabla f(x_k)$ if $\|\nabla f(x_k)\| > \varepsilon_g$. Otherwise, compute $\lambda_k = \lambda_{\min}(\nabla^2 f(x_k))$. If $\lambda_k < -\varepsilon_H$, choose $p_k$ s.t. $\|p_k\| = 1$, $\nabla^2 f(x_k)p_k = \lambda_k p_k$, and $\nabla f(x_k)^T p_k \leq 0$, and take $x_{k + 1} = x_k + \frac{2|\lambda_k|}{M}p_k$. Otherwise, it stops at $x_k$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, $\bar{f} \in \mathbb{R}$, and $\varepsilon_g, \varepsilon_H > 0$. Assume $f \in \mathcal{C}^2$ is $L$-smooth, its Hessian is Lipschitz continuous with constant $M$, and $f(x) \geq \bar{f}$ for any $x \in \mathbb{R}^n$. Set $\{x_k\}$ as the gradient and negative-curvature descent iterates with tolerances $\varepsilon_g, \varepsilon_H$. $x_k$ is an approximate second-order necessary point for some integer $k \leq \frac{f(x_0) - \bar{f}}{\min\left\{\frac{\varepsilon_g^2}{2L}, \frac{2\varepsilon_H^3}{3M^2}\right\}}$.
::: ^negative-curvature-decrease

*Proof.*
If iteration $k$ takes a gradient step, [[#^lemma-0fb324|Proposition 2]] with $\alpha = \frac{1}{L}$ gives
$$
f(x_{k + 1}) \leq f(x_k) - \frac{1}{2L}\|\nabla f(x_k)\|^2 \leq f(x_k) - \frac{\varepsilon_g^2}{2L}.
$$
If it takes a negative-curvature step, set $\alpha_k = \frac{2|\lambda_k|}{M}$. [[Lipschitz Continuity#^lipschitz-hessian-cubic-bound|Proposition 12]] with $\|p_k\| = 1$, $\nabla f(x_k)^T p_k \leq 0$, and $\nabla^2 f(x_k)p_k = \lambda_k p_k$ gives
$$
\begin{aligned}
f(x_{k + 1}) &\leq f(x_k) + \alpha_k\nabla f(x_k)^T p_k + \frac{\alpha_k^2}{2}\lambda_k + \frac{M}{6}\alpha_k^3 \\
&\leq f(x_k) - \frac{\alpha_k^2}{2}|\lambda_k| + \frac{M}{6}\alpha_k^3 = f(x_k) - \frac{2|\lambda_k|^3}{3M^2} \leq f(x_k) - \frac{2\varepsilon_H^3}{3M^2}.
\end{aligned}
$$
Each step before stopping decreases $f$ by at least $\min\left\{\frac{\varepsilon_g^2}{2L}, \frac{2\varepsilon_H^3}{3M^2}\right\}$. Since $f(x) \geq \bar{f}$, the method stops within the stated number of steps, and it stops only at an approximate second-order necessary point.

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
$f(x^*)$ is between $L_k(x^*)$ and $f(u_k)$. To obtain $f(x^*)$, we can accumulate $L_k$ using $V_k = (1 - q_k)V_{k - 1} + q_kL_k$ with decreasing $q_k \in (0, 1]$. Suppose $V_{-1}(t) = \frac{\gamma_{-1}}{2}\|t - x_0\|^2 + f(x_0)$ and $V_{k - 1}(t) = \frac{\gamma_{k - 1}}{2}\|t - v_{k - 1}\|^2 + c_{k - 1}$ and let $\gamma_k = (1 - q_k)\gamma_{k - 1}$.
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

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathbb{R}^n$, and $R, \varepsilon > 0$. Assume $f$ is convex and $L$-smooth, $x^*$ is its global minimizer, and $\|x_0 - x^*\| \leq R$. Set $\mu = \frac{\varepsilon}{R^2}$, $F_\mu(x) = f(x) + \frac{\mu}{2}\|x - x_0\|^2$, $\kappa_\mu = \frac{L + \mu}{\mu}$, and $\{x_k\}$ as the accelerated gradient descent iterates for $F_\mu$ with $\alpha_k = \frac{1}{L + \mu}$ and $\beta_k = \frac{\sqrt{\kappa_\mu} - 1}{\sqrt{\kappa_\mu} + 1}$. $f(x_k) - f(x^*) \leq \frac{L + 2\mu}{2}R^2\left(1 - \frac{1}{\sqrt{\kappa_\mu}}\right)^k + \frac{\varepsilon}{2}$ for any integer $k \geq 1$, and $f(x_k) - f(x^*) \leq \varepsilon$ for any integer $k \geq \sqrt{1 + \frac{LR^2}{\varepsilon}}\ln\left(2 + \frac{LR^2}{\varepsilon}\right)$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^*, x_0 \in \mathbb{R}^n$. Assume $f$ is $L$-smooth and strongly convex with modulus $m$, and $x^*$ is its global minimizer. Set $N = \left\lceil\sqrt{\frac{8L}{m}}\right\rceil$, $z_0 = x_0$, and $z_{t + 1}$ as the $N$th accelerated gradient descent iterate started from $z_t$ with $\alpha_k = \frac{1}{L}$, $\beta_0 = 0$, and $\beta_k = \frac{\lambda_k - 1}{\lambda_{k + 1}}$, where $\lambda_0 = 0$ and $\lambda_{k + 1} = \frac{1 + \sqrt{1 + 4\lambda_k^2}}{2}$. $f(z_t) - f(x^*) \leq 2^{-t}(f(x_0) - f(x^*))$ for any integer $t \geq 0$, and $f(z_T) - f(x^*) \leq \varepsilon$ after $NT$ gradient evaluations for any $\varepsilon > 0$ and integer $T \geq \log_2\frac{f(x_0) - f(x^*)}{\varepsilon}$.
:::

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
