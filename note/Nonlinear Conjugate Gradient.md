::: definition:Nonlinear Conjugate Gradient Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. Set $\widetilde p_k = -\nabla f(x_k)$ and $p_0 = \widetilde p_0$. The nonlinear conjugate gradient method generates $x_{k+1} = x_k + \alpha_kp_k$ and $p_{k+1} = \widetilde p_{k+1} + \beta_{k+1}p_k$, where $\alpha_k > 0$ is chosen by a line search and $\beta_{k+1}$ by an update rule, and stops when $\widetilde p_k = 0$.
::: ^nonlinear-cg

::: definition:Fletcher–Reeves Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The Fletcher–Reeves method is [[#^nonlinear-cg|Definition 1 (Nonlinear Conjugate Gradient Method)]] with $\beta_{k+1} = \frac{\lVert\widetilde p_{k+1}\rVert^2}{\lVert\widetilde p_k\rVert^2}$.
::: ^nonlinear-fr

::: definition:Strong Wolfe Conditions
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_k, p_k \in \mathbb{R}^n$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$ and $\langle\widetilde p_k,p_k\rangle > 0$. Set $x_{k+1} = x_k + \alpha_kp_k$ and $\widetilde p_j = -\nabla f(x_j)$. $\alpha_k > 0$ satisfies the strong Wolfe conditions if $f(x_{k+1}) \leq f(x_k) - c_1\alpha_k\langle\widetilde p_k,p_k\rangle$ and $|\langle\widetilde p_{k+1},p_k\rangle| \leq c_2\langle\widetilde p_k,p_k\rangle$.
::: ^nonlinear-strong-wolfe

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $0 < c_1 < c_2 < \frac{1}{2}$. Assume $f \in \mathcal{C}^1$. Set $\{x_k\}$ and $\{p_k\}$ as the iterates of [[#^nonlinear-fr|Definition 2 (Fletcher–Reeves Method)]] with steps satisfying [[#^nonlinear-strong-wolfe|Definition 3 (Strong Wolfe Conditions)]]. $\frac{1 - 2c_2}{1 - c_2} \leq \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2} \leq \frac{1}{1 - c_2}$ for any $k$ before termination.
::: ^fr-sufficient-descent

*Proof.*
Set $s_k = \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2}$, so $s_0 = 1$. The update gives $s_{k+1} = 1 + \frac{\langle\widetilde p_{k+1},p_k\rangle}{\lVert\widetilde p_k\rVert^2}$, and strong Wolfe gives $|s_{k+1} - 1| \leq c_2s_k$. Induct on $k$.

::: definition:Polak–Ribière Method
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x_0 \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. The Polak–Ribière method is [[#^nonlinear-cg|Definition 1 (Nonlinear Conjugate Gradient Method)]] with $\beta_{k+1} = \frac{\langle\widetilde p_{k+1},\widetilde p_{k+1} - \widetilde p_k\rangle}{\lVert\widetilde p_k\rVert^2}$, and the PR+ method uses $\max\{\beta_{k+1}, 0\}$ instead.
::: ^nonlinear-pr

::: note
For $f(x) = \frac{1}{2}x^TAx - b^Tx$ with $A \succ 0$ and exact line searches, Fletcher–Reeves, Polak–Ribière, and PR+ coincide with [[Conjugate Gradient#^conjugate-gradient-method|Definition 7 (Conjugate Gradient Method)]]. For general $f$, if $\widetilde p_{k+1} \approx \widetilde p_k$, then Fletcher–Reeves gives $\beta_{k+1} \approx 1$ and keeps a poor direction, while Polak–Ribière gives $\beta_{k+1} \approx 0$ and restarts automatically.
:::

::: definition:Restart and Descent Safeguard
Let $(x_k, p_k)$ be iterates of [[#^nonlinear-cg|Definition 1 (Nonlinear Conjugate Gradient Method)]], $\eta > 0$, and $\delta \in (0, 1)$. A restart sets $p_k = \widetilde p_k$, i.e., $\beta_k = 0$. It is triggered after a fixed number of iterations, by the gradient test $|\langle\widetilde p_k,\widetilde p_{k-1}\rangle| \geq \eta\lVert\widetilde p_k\rVert^2$, or by the descent safeguard $\langle\widetilde p_k,p_k\rangle < \delta\lVert\widetilde p_k\rVert^2$.
:::

::: lemma:Zoutendijk Condition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$, $\mathcal{L} = \{x : f(x) \leq f(x_0)\}$ is bounded, $\nabla f$ is $L$-Lipschitz on a neighborhood of $\mathcal{L}$, every $p_k$ satisfies $\langle\widetilde p_k,p_k\rangle > 0$, and every $\alpha_k$ satisfies [[Sufficient Descent#^weak-wolfe-conditions|Definition 13 (Weak Wolfe conditions)]] with constants $c_1, c_2$. Set $x_{k+1} = x_k + \alpha_kp_k$. $\sum_{k=0}^{\infty}\frac{\langle\widetilde p_k,p_k\rangle^2}{\lVert p_k\rVert^2} < \infty$.
::: ^nonlinear-zoutendijk

*Proof.*
Curvature and Lipschitz continuity give $(1 - c_2)\langle\widetilde p_k,p_k\rangle \leq L\alpha_k\lVert p_k\rVert^2$, so sufficient decrease gives $f(x_k) - f(x_{k+1}) \geq \frac{c_1(1 - c_2)}{L}\frac{\langle\widetilde p_k,p_k\rangle^2}{\lVert p_k\rVert^2}$. Sum over $k$ and use that $f$ is bounded below on the compact set $\mathcal{L}$.

::: theorem:Global Convergence of Fletcher–Reeves
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $0 < c_1 < c_2 < \frac{1}{2}$. Assume $f \in \mathcal{C}^1$, $\mathcal{L} = \{x : f(x) \leq f(x_0)\}$ is bounded, and $\nabla f$ is Lipschitz continuous on a neighborhood of $\mathcal{L}$. Set $\{x_k\}$ as the iterates of [[#^nonlinear-fr|Definition 2 (Fletcher–Reeves Method)]] with steps satisfying [[#^nonlinear-strong-wolfe|Definition 3 (Strong Wolfe Conditions)]]. If the method does not terminate, then $\underset{k \to \infty}{\liminf}\lVert\nabla f(x_k)\rVert = 0$.
::: ^nonlinear-fr-convergence

*Proof.*
Suppose $\lVert\widetilde p_k\rVert \geq \varepsilon > 0$ for any $k$. Set $s_k = \frac{\langle\widetilde p_k,p_k\rangle}{\lVert\widetilde p_k\rVert^2}$ and $u_k = \frac{\lVert p_k\rVert^2}{\lVert\widetilde p_k\rVert^4}$. Expanding the update gives $u_k = u_{k-1} + \frac{2s_k - 1}{\lVert\widetilde p_k\rVert^2}$, so [[#^fr-sufficient-descent|Proposition 4]] gives $u_k \leq u_{k-1} + \frac{1 + c_2}{(1 - c_2)\varepsilon^2}$, hence $u_k \leq C(k + 1)$. Then $\frac{\langle\widetilde p_k,p_k\rangle^2}{\lVert p_k\rVert^2} = \frac{s_k^2}{u_k} \geq \left(\frac{1 - 2c_2}{1 - c_2}\right)^2\frac{1}{C(k + 1)}$, whose sum diverges, contradicting [[#^nonlinear-zoutendijk|Lemma 7 (Zoutendijk Condition)]].

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathbb{R}^n$, and $0 < c_1 < c_2 < 1$. Assume $f \in \mathcal{C}^1$, $\mathcal{L} = \{x : f(x) \leq f(x_0)\}$ is bounded, and $\nabla f$ is Lipschitz continuous on a neighborhood of $\mathcal{L}$. Set $\{x_k\}$ and $\{p_k\}$ as the iterates of [[#^nonlinear-cg|Definition 1 (Nonlinear Conjugate Gradient Method)]] s.t. every $p_k$ satisfies $\langle\widetilde p_k,p_k\rangle > 0$, every $\alpha_k$ satisfies [[Sufficient Descent#^weak-wolfe-conditions|Definition 13 (Weak Wolfe conditions)]] with constants $c_1, c_2$, and restarts occur at infinitely many indices $k_j$. $\underset{j \to \infty}{\lim}\lVert\nabla f(x_{k_j})\rVert = 0$.
:::

*Proof.*
At a restart, $p_{k_j} = \widetilde p_{k_j}$, so [[#^nonlinear-zoutendijk|Lemma 7 (Zoutendijk Condition)]] gives $\sum_j\lVert\widetilde p_{k_j}\rVert^2 < \infty$.
