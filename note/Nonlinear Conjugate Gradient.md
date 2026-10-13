::: definition:Nonlinear Conjugate Gradient Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. Set $\widetilde p_0 = p_0 = -\nabla f(x_0)$. The nonlinear conjugate gradient method minimizes $f$ using a line search and a choice of $\beta_{k+1}$:
$$
\begin{aligned}
\alpha_k &> 0 \quad\text{chosen by line search along }p_k,\\
x_{k+1} &= x_k + \alpha_kp_k,\\
\widetilde p_{k+1} &= -\nabla f(x_{k+1}),\\
\beta_{k+1} &\quad\text{chosen by a direction update rule},\\
p_{k+1} &= \widetilde p_{k+1} + \beta_{k+1}p_k.
\end{aligned}
$$
Stop whenever $\widetilde p_j = 0$ and return $x_j$, before forming further ratios. A numerical stopping rule replaces this by $\lVert\widetilde p_j\rVert \leq \varepsilon$ for a tolerance $\varepsilon > 0$.
::: ^nonlinear-cg

::: note
For $f(x) = \frac12x^TAx - b^Tx$ with $A \succ 0$, $\widetilde p_k = b - Ax_k$ and $\widetilde p_{k+1} = \widetilde p_k - \alpha_kAp_k$. For a general objective there is no fixed $A$ providing this relation or an $A$-inner product for all directions. The two orthogonal bases, subspace optimality, and finite termination of [[Conjugate Gradient#^conjugate-gradient-method|Conjugate Gradient Method]] do not generally persist. The positive step $\alpha_k$ corresponds to $-a_k$ in that definition.
:::

::: definition:Fletcher–Reeves Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The Fletcher–Reeves (FR) method is [[#^nonlinear-cg|Nonlinear Conjugate Gradient Method]] with $\beta_{k+1} = \frac{\langle\widetilde p_{k+1},\widetilde p_{k+1}\rangle}{\langle\widetilde p_k,\widetilde p_k\rangle}$. For a quadratic objective with Hessian $A \succ 0$ and exact line searches, it coincides with [[Conjugate Gradient#^conjugate-gradient-method|Conjugate Gradient Method]].
::: ^nonlinear-fr

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_k,p_k \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ and an exact line search attains an interior minimizer $\alpha_k > 0$ of $f(x_k + \alpha p_k)$ over $\alpha \geq 0$. Set $x_{k+1} = x_k + \alpha_kp_k$, $\widetilde p_{k+1} = -\nabla f(x_{k+1})$, and $p_{k+1} = \widetilde p_{k+1} + \beta_{k+1}p_k$. $\langle\widetilde p_{k+1},p_k\rangle = 0$ and $\langle\widetilde p_{k+1},p_{k+1}\rangle = \lVert\widetilde p_{k+1}\rVert^2$ for any $\beta_{k+1} \in \mathbb{R}$. Thus $p_{k+1}$ is a descent direction whenever $\widetilde p_{k+1} \neq 0$.
:::

*Proof.*
The line-search first-order condition gives $\langle\nabla f(x_{k+1}),p_k\rangle = 0$. Hence $\langle\widetilde p_{k+1},p_{k+1}\rangle = \lVert\widetilde p_{k+1}\rVert^2 + \beta_{k+1}\langle\widetilde p_{k+1},p_k\rangle = \lVert\widetilde p_{k+1}\rVert^2$.

::: note
The descent condition is $\langle\nabla f(x_k),p_k\rangle < 0$, equivalently $\langle\widetilde p_k,p_k\rangle > 0$, since $f(x_k + tp_k) = f(x_k) + t\langle\nabla f(x_k),p_k\rangle + o(t)$. Exact line search makes the new negative gradient orthogonal to the direction just used; it does not generally preserve $\langle\widetilde p_{k+1},p_i\rangle = 0$ for $i < k$.
:::

::: definition:Strong Wolfe Conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k,p_k \in \mathbb{R}^n$, and $c_1,c_2 \in \mathbb{R}$. Assume $f \in \mathcal{C}^1$, $0 < c_1 < c_2 < 1$, and $\langle\nabla f(x_k),p_k\rangle < 0$. Set $x_{k+1} = x_k + \alpha_kp_k$ and $\widetilde p_j = -\nabla f(x_j)$. A step $\alpha_k > 0$ satisfies the strong Wolfe conditions if
$$
\begin{aligned}
f(x_{k+1}) &\leq f(x_k) - c_1\alpha_k\langle\widetilde p_k,p_k\rangle,\\
|\langle\widetilde p_{k+1},p_k\rangle| &\leq c_2\langle\widetilde p_k,p_k\rangle.
\end{aligned}
$$
The ordinary Wolfe conditions replace the second inequality by $\langle\widetilde p_{k+1},p_k\rangle \leq c_2\langle\widetilde p_k,p_k\rangle$.
::: ^nonlinear-strong-wolfe

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$ and the iterates of [[#^nonlinear-fr|Fletcher–Reeves Method]] use [[#^nonlinear-strong-wolfe|strong Wolfe steps]] with $0 < c_1 < c_2 < \frac12$. Set $\delta_* = \frac{1-2c_2}{1-c_2}$. Before termination, $\delta_* \leq \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2} \leq \frac1{1-c_2}$, so every direction satisfies $\langle\widetilde p_k,p_k\rangle \geq \delta_*\lVert\widetilde p_k\rVert^2 > 0$.
::: ^fr-sufficient-descent

*Proof.*
Set $s_k = \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2}$. The FR update gives $s_{k+1} = 1 + \frac{\langle\widetilde p_{k+1},p_k\rangle}{\lVert\widetilde p_k\rVert^2}$, so strong Wolfe gives $1-c_2s_k \leq s_{k+1} \leq 1+c_2s_k$. Starting from $s_0 = 1$, induction yields $\delta_* \leq s_{k+1} \leq \frac1{1-c_2}$ whenever $\delta_* \leq s_k \leq \frac1{1-c_2}$.

::: note
The [[#^fr-sufficient-descent|sufficient descent bound]] needs no Lipschitz-gradient assumption. It does not bound the angle away from $90^\circ$: $\cos\theta_k = \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert\lVert p_k\rVert} \geq \delta_*\frac{\lVert\widetilde p_k\rVert}{\lVert p_k\rVert}$, and $\lVert p_k\rVert$ may be large.
:::

::: definition:Polak–Ribière Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The Polak–Ribière (PR) method is [[#^nonlinear-cg|Nonlinear Conjugate Gradient Method]] with $\beta_{k+1} = \frac{\langle\widetilde p_{k+1},\widetilde p_{k+1}-\widetilde p_k\rangle}{\lVert\widetilde p_k\rVert^2}$. The PR+ method replaces this coefficient by its maximum with zero.
::: ^nonlinear-pr

::: note
For a quadratic objective with Hessian $A \succ 0$ and exact line searches, successive negative gradients are orthogonal, so FR, PR, and PR+ coincide. If $\widetilde p_{k+1} \approx \widetilde p_k$, FR gives $\beta_{k+1} \approx 1$, whereas PR gives $\beta_{k+1} \approx 0$. FR may retain a poor direction when $\lVert p_k\rVert \gg \lVert\widetilde p_k\rVert$; PR tends toward the negative gradient. PR+ alone does not guarantee descent with an arbitrary strong Wolfe line search.
:::

::: definition:Restart and Descent Safeguard
Let $(x_k,p_k)$ be iterates and directions of [[#^nonlinear-cg|Nonlinear Conjugate Gradient Method]], and let $\delta \in (0,1)$ and $\eta > 0$. A restart replaces $p_k$ by $\widetilde p_k$, equivalently setting $\beta_k = 0$ for $k \geq 1$. Periodic restarts occur at fixed iteration intervals. A gradient test restarts when $\frac{|\langle\widetilde p_k,\widetilde p_{k-1}\rangle|}{\lVert\widetilde p_k\rVert^2} \geq \eta$. A descent safeguard restarts before line search whenever $\langle\widetilde p_k,p_k\rangle < \delta\lVert\widetilde p_k\rVert^2$. Apply these tests only while $\widetilde p_k \neq 0$.
:::

::: note
Denote the FR and PR coefficients by $\beta_{k,\mathrm{FR}}$ and $\beta_{k,\mathrm{PR}}$. The clipped choice $\beta_k = \max\{-\beta_{k,\mathrm{FR}},\min\{\beta_{k,\mathrm{PR}},\beta_{k,\mathrm{FR}}\}\}$ satisfies $|\beta_k| \leq \beta_{k,\mathrm{FR}}$. The proof of the [[#^fr-sufficient-descent|sufficient descent bound]] still applies, since this bound on $|\beta_k|$ gives the same inequalities for $s_k$.
:::

::: lemma:Zoutendijk Condition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume the initial level set $\mathcal L = \{x : f(x) \leq f(x_0)\}$ is bounded and $f \in \mathcal{C}^1$ has an $L$-Lipschitz gradient on a neighborhood of $\mathcal L$, with $L > 0$. Set $x_{k+1} = x_k + \alpha_kp_k$ and $\widetilde p_k = -\nabla f(x_k)$. If every $p_k$ is a descent direction and every $\alpha_k$ satisfies the [[#^nonlinear-strong-wolfe|Wolfe conditions]] with fixed $0 < c_1 < c_2 < 1$, then $\sum_{k=0}^{\infty}\frac{\langle\widetilde p_k,p_k\rangle^2}{\lVert p_k\rVert^2} < \infty$.
::: ^nonlinear-zoutendijk

*Proof.*
Set $D_k = \langle\widetilde p_k,p_k\rangle > 0$. Curvature and Lipschitz continuity give $(1-c_2)D_k \leq \langle\nabla f(x_{k+1})-\nabla f(x_k),p_k\rangle \leq L\alpha_k\lVert p_k\rVert^2$. Sufficient decrease gives $f(x_k)-f(x_{k+1}) \geq \frac{c_1(1-c_2)}{L}\frac{D_k^2}{\lVert p_k\rVert^2}$. Sum over $k$ and use the lower bound of $f$ on the compact set $\mathcal L$.

::: theorem:Global Convergence of Fletcher–Reeves
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume the level-set and smoothness hypotheses of the [[#^nonlinear-zoutendijk|Zoutendijk Condition]]. The [[#^nonlinear-fr|Fletcher–Reeves Method]] with [[#^nonlinear-strong-wolfe|strong Wolfe steps]] and $0 < c_1 < c_2 < \frac12$ either terminates at a stationary point or satisfies $\underset{k\to\infty}{\liminf}\lVert\nabla f(x_k)\rVert = 0$.
::: ^nonlinear-fr-convergence

*Proof.*
Suppose instead $\lVert\widetilde p_k\rVert \geq \varepsilon > 0$ for all $k$. Set $s_k = \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2}$ and $u_k = \frac{\lVert p_k\rVert^2}{\lVert\widetilde p_k\rVert^4}$. Expanding the FR update gives $u_k = u_{k-1} + \frac{2s_k-1}{\lVert\widetilde p_k\rVert^2}$. By the [[#^fr-sufficient-descent|sufficient descent bound]], $u_k \leq u_{k-1} + \frac{1+c_2}{(1-c_2)\varepsilon^2}$, hence $u_k \leq C(k+1)$ for some $C > 0$. But $\frac{\langle\widetilde p_k,p_k\rangle^2}{\lVert p_k\rVert^2} = \frac{s_k^2}{u_k} \geq \frac{\delta_*^2}{C(k+1)}$, contradicting the [[#^nonlinear-zoutendijk|Zoutendijk Condition]].

::: note
The [[#^nonlinear-fr-convergence|convergence conclusion]] provides a subsequence with gradients tending to zero. It does not assert convergence of every gradient or convergence to a global minimizer; convexity is not assumed.
:::

::: example
With $c_1 = 10^{-4}$, $c_2 = 0.1$, no periodic restarts, and the stopping test $\lVert\nabla f(x_k)\rVert_\infty < 10^{-5}(1+|f(x_k)|)$, the slides report iteration counts $(\mathrm{FR},\mathrm{PR},\mathrm{PR+})$ of $(\mathrm{failure},1068,1067)$ for GENROS, $(533,212,97)$ for XPOWSING, $(264,262,262)$ for TRIDIA1, and $(231,40,40)$ for TRIGON. Failure means the test was not met within $10{,}000$ iterations. FR took many small, unproductive steps on GENROS; asymptotic convergence does not give a fixed iteration budget.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume the hypotheses of the [[#^nonlinear-zoutendijk|Zoutendijk Condition]] hold throughout an infinite run, and restarts occur at infinitely many indices $k_j$. $\lVert\nabla f(x_{k_j})\rVert \to 0$, hence $\underset{k\to\infty}{\liminf}\lVert\nabla f(x_k)\rVert = 0$.
:::

*Proof.*
At every restart, $p_{k_j} = \widetilde p_{k_j}$, so the [[#^nonlinear-zoutendijk|Zoutendijk Condition]] gives $\sum_j\lVert\widetilde p_{k_j}\rVert^2 < \infty$. Thus $\lVert\widetilde p_{k_j}\rVert \to 0$.

::: note
Each restart step is gradient descent with a Wolfe line search. A fixed upper bound on restart intervals ensures infinitely many restarts in an infinite run; intervening steps must still satisfy descent and Wolfe conditions.
:::

::: note
For an objective that is exactly quadratic with Hessian $A \succ 0$ near a minimizer, restarting there with exact line searches recovers linear CG and termination within $n$ steps, provided the steps stay in that region. For nonlinear objectives, classical local results for suitable periodically restarted CG methods, under additional regularity and exact-line-search assumptions near $x^*$ with $\nabla^2f(x^*) \succ 0$, give $\lVert x_{k+n}-x^*\rVert = O(\lVert x_k-x^*\rVert^2)$ over restart cycles. This is an $n$-step rate, not a one-step quadratic rate, and does not follow from strong Wolfe alone.
:::
