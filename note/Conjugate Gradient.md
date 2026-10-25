::: definition:Krylov Sequence
Let $A \in \mathbb{R}^{n, n}$ and $p_0, p_1, \ldots$ be a finite sequence of vectors in $\mathbb{R}^n$. The sequence is a Krylov sequence for $A$ if $Ap_i \in \operatorname{span}\{p_0, \ldots, p_i, p_{i+1}\}$ whenever $p_{i+1}$ is present.
:::

::: definition:$A$-Orthogonal Krylov Sequence
Let $A \in \mathbb{R}^{n, n}$ and $p_0, p_1, \ldots$ be a finite sequence of vectors in $\mathbb{R}^n$. Assume $A \succ 0$ and the sequence is a Krylov sequence for $A$. The sequence is an $A$-orthogonal Krylov sequence if $\langle p_i, p_j\rangle_A = 0$ for $i\neq j$.
:::

::: lemma
Let $A \in \mathbb{R}^{n, n}$ and $p_0, p_1, \ldots$ be a finite sequence of vectors in $\mathbb{R}^n$. Assume the sequence is an $A$-orthogonal Krylov sequence. Whenever $p_{i+1}$ is present, $Ap_0 \in \operatorname{span}\{p_0, p_1\}$ for $i = 0$, and $Ap_i \in \operatorname{span}\{p_{i-1}, p_i, p_{i+1}\}$ for $i \geq 1$.
::: ^krylov-three-term

::: theorem:Krylov Recursion
Let $A \in \mathbb{R}^{n, n}$ and $p_0 \in \mathbb{R}^n$. Assume $A \succ 0$ and $p_0 \neq 0$. Set $\widetilde p_0 = p_0$. At step $k$, assume $p_0, \ldots, p_k$ is an $A$-orthogonal Krylov sequence and $\langle\widetilde p_k, p_i\rangle = 0$ for $i = 0, \ldots, k - 1$. Set
$$
a_k = -\frac{\langle\widetilde p_k, p_k\rangle}{\langle p_k, p_k\rangle_A},
\qquad
\widetilde p_{k+1} = \widetilde p_k + a_kAp_k.
$$
$\langle\widetilde p_{k+1}, p_i\rangle = 0$ for $i = 0, \ldots, k$. 
::: ^krylov-recursion

*Proof.*
The initial hypotheses hold at $k = 0$. For $i < k$, $\langle\widetilde p_{k+1}, p_i\rangle = \langle\widetilde p_k, p_i\rangle + a_k\langle p_k, p_i\rangle_A = 0$. For $i = k$, $\langle\widetilde p_{k+1}, p_k\rangle = \langle\widetilde p_k, p_k\rangle + a_k\langle p_k, p_k\rangle_A = 0$ by the choice of $a_k$.

::: note
Any nonzero $p_{k+1}$ extending $p_0, \ldots, p_k$ to an $A$-orthogonal Krylov sequence preserves both induction hypotheses. It need not be constructed from $\widetilde p_{k+1}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$, and let $p_0, \ldots, p_k$ and $\widetilde p_0, \ldots, \widetilde p_{k+1}$ be two finite sequences of vectors in $\mathbb{R}^n$. Assume the sequences are generated through step $k$ of [[#^krylov-recursion|Krylov Recursion]] and $\widetilde p_{k+1} \neq 0$. Set
$$
p_{k+1}
= \widetilde p_{k+1}
- \frac{\langle\widetilde p_{k+1}, p_k\rangle_A}{\langle p_k, p_k\rangle_A}p_k.
$$
The sequence $p_0, \ldots, p_{k+1}$ is an $A$-orthogonal Krylov sequence.
::: ^krylov-direction-construction

*Proof.*
Combining [[#^krylov-three-term|Lemma 3]] with the second induction condition at step $k + 1$ gives $\langle\widetilde p_{k+1}, Ap_i\rangle = 0$ for $i < k$, so $\langle\widetilde p_{k+1}, p_i\rangle_A = 0$. To obtain $p_{k+1}$, subtract the components of $\widetilde p_{k+1}$ along $p_0, \ldots, p_k$ with respect to the $A$-inner product:
$$
\begin{aligned}
p_{k+1}
&= \widetilde p_{k+1} - \sum_{i=0}^{k}\frac{\langle\widetilde p_{k+1}, p_i\rangle_A}{\langle p_i, p_i\rangle_A}p_i\\
&= \widetilde p_{k+1} - \frac{\langle\widetilde p_{k+1}, p_k\rangle_A}{\langle p_k, p_k\rangle_A}p_k.
\end{aligned}
$$
Finally, $Ap_k = \frac{\widetilde p_{k+1} - \widetilde p_k}{a_k} \in \operatorname{span}\{p_0, \ldots, p_{k+1}\}$, so the extended sequence retains the Krylov property. 

::: note
[[#^krylov-direction-construction|Proposition 5]] maintains two bases: $\langle p_i, p_j\rangle_A = 0$ and $\langle\widetilde p_i, \widetilde p_j\rangle = 0$ for $i \neq j$. Since $\widetilde p_0 = p_0$ and $\widetilde p_k = p_k + \frac{\langle\widetilde p_k, p_{k-1}\rangle_A}{\langle p_{k-1}, p_{k-1}\rangle_A}p_{k-1}$ for $k \geq 1$, the two bases satisfy $\operatorname{span}\{p_0, \ldots, p_k\} = \operatorname{span}\{\widetilde p_0, \ldots, \widetilde p_k\}$. In particular, $\widetilde p_k \in \operatorname{span}\{p_{k-1}, p_k\}$ for $k \geq 1$, and $p_k \in \operatorname{span}\{\widetilde p_0, \ldots, \widetilde p_k\}$ for $k \geq 0$.
:::

::: definition:Fletcher–Reeves Form of Krylov Recursion
Let $A \in \mathbb{R}^{n, n}$ and $p_0 \in \mathbb{R}^n$. Assume $A \succ 0$ and $p_0 \neq 0$. Set $\widetilde p_0 = p_0$. The Fletcher–Reeves form of the recursion computes
$$
\begin{aligned}
a_k &= -\frac{\langle\widetilde p_k, \widetilde p_k\rangle}{\langle p_k, p_k\rangle_A},\\
\widetilde p_{k+1} &= \widetilde p_k + a_kAp_k,\\
\beta_{k+1} &= \frac{\langle\widetilde p_{k+1}, \widetilde p_{k+1}\rangle}{\langle\widetilde p_k, \widetilde p_k\rangle},\\
p_{k+1} &= \widetilde p_{k+1} + \beta_{k+1}p_k.
\end{aligned}
$$
Stop when $\widetilde p_{k+1} = 0$.
::: ^krylov-fr-construction

::: note
Each iteration of the [[#^krylov-fr-construction|Fletcher–Reeves construction]] requires one matrix-vector product $Ap_k$ and $O(n)$ additional operations.
:::

::: note
The [[#^krylov-fr-construction|Fletcher–Reeves form]] generates the same sequences as [[#^krylov-recursion|Krylov Recursion]] with every subsequent direction chosen by [[#^krylov-direction-construction|Proposition 5]]. The formula for $a_k$ is obvious. Substituting $Ap_k = \frac{\widetilde p_{k+1} - \widetilde p_k}{a_k}$ gives $-\frac{\langle\widetilde p_{k+1}, p_k\rangle_A}{\langle p_k, p_k\rangle_A} = -\frac{\langle\widetilde p_{k+1}, \widetilde p_{k+1}\rangle}{a_k\langle p_k, p_k\rangle_A} = \frac{\langle\widetilde p_{k+1}, \widetilde p_{k+1}\rangle}{\langle\widetilde p_k, \widetilde p_k\rangle}$.
:::

::: definition:Conjugate Gradient Method
Let $A \in \mathbb{R}^{n, n}$ and $b, x_0 \in \mathbb{R}^n$. Assume $A \succ 0$. Set $\widetilde p_0 = p_0 = b - Ax_0$. The conjugate gradient method for $Ax = b$ uses the [[#^krylov-fr-construction|Fletcher–Reeves construction]] to compute
$$
\begin{aligned}
a_k &= -\frac{\langle\widetilde p_k, \widetilde p_k\rangle}{\langle p_k, p_k\rangle_A},\\
x_{k+1} &= x_k - a_kp_k,\\
\widetilde p_{k+1} &= \widetilde p_k + a_kAp_k = b - Ax_{k+1}, \\
\beta_{k+1} &= \frac{\langle\widetilde p_{k+1}, \widetilde p_{k+1}\rangle}{\langle\widetilde p_k, \widetilde p_k\rangle},\\
p_{k+1} &= \widetilde p_{k+1} + \beta_{k+1}p_k.
\end{aligned}
$$
Stop as soon as $\widetilde p_j = 0$ and return $x_j$, since $Ax_j = b$. Keep subsequent iterates equal to $x_j$.
::: ^conjugate-gradient-method

::: note
For $i = 0, \ldots, k$, $\langle\widetilde p_{k+1}, p_i\rangle = 0 \;\Longrightarrow\; \langle b - Ax_{k+1}, p_i\rangle = 0 \;\Longrightarrow\; \langle x_{k+1} - x^*, p_i\rangle_A = 0$. Thus $x_k = \underset{x \in x_0 + \operatorname{span}\{b - Ax_0, A(b - Ax_0), \ldots, A^{k-1}(b - Ax_0)\}}{\operatorname{argmin}}\lVert x - x^*\rVert_A$.
::: ^cg-subspace-optimality

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b, x_0 \in \mathbb{R}^n$. Assume $A \succ 0$ and $x_0 \neq A^{-1}b$. Set $(x_k)$ to be the iterates of [[#^conjugate-gradient-method|Conjugate Gradient Method]], $x^* = A^{-1}b$, and $\mathcal P_k = \{q \in \mathbb{R}[t] : \deg q \leq k,\ q(0) = 1\}$. $\frac{\lVert x_k - x^*\rVert_A}{\lVert x_0 - x^*\rVert_A} \leq \underset{q \in \mathcal P_k}{\min}\underset{\lambda \in \sigma(A)}{\max}|q(\lambda)|$.
::: ^cg-polynomial-bound

*Proof.*
The candidate errors are $x - x^* = [I - AP(A)](x_0 - x^*) = q(A)(x_0 - x^*)$, where $q(t) = 1 - tP(t)$ ranges over $\mathcal P_k$. Write $x_0 - x^* = \sum_i c_i v_i$ in an orthonormal eigenbasis of $A$. Then $\lVert q(A)(x_0 - x^*)\rVert_A^2 = \sum_i\lambda_i c_i^2q(\lambda_i)^2 \leq \bigl(\underset{i}{\max}|q(\lambda_i)|^2\bigr)\lVert x_0 - x^*\rVert_A^2$. Apply [[#^cg-subspace-optimality|subspace optimality]] and minimize the bound over $q \in \mathcal P_k$.

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b, x_0 \in \mathbb{R}^n$. Assume $A \succ 0$ has $s$ distinct eigenvalues. [[#^conjugate-gradient-method|Conjugate Gradient Method]] terminates in at most $s \leq n$ steps.
:::

*Proof.*
For the distinct eigenvalues $\mu_1, \ldots, \mu_s$, choose $q(t) = \prod_{j=1}^s(1 - \frac{t}{\mu_j})$. This admissible polynomial vanishes on the spectrum, so the [[#^cg-polynomial-bound|polynomial error bound]] gives termination by step $s$.

::: theorem:Chebyshev Convergence Bound
Let $A \in \mathbb{R}^{n, n}$, $b, x_0 \in \mathbb{R}^n$, and $m, L \in \mathbb{R}$. Assume $A \succ 0$, $0 < m < L$, and $mI \preceq A \preceq LI$. Set $(x_k)$ to be the iterates of [[#^conjugate-gradient-method|Conjugate Gradient Method]], $x^* = A^{-1}b$, $\kappa = \frac{L}{m}$, and $\rho = \frac{\sqrt\kappa-1}{\sqrt\kappa+1}$. The error satisfies $\lVert x_k - x^*\rVert_A \leq 2\rho^k\lVert x_0 - x^*\rVert_A$.
::: ^cg-chebyshev-bound

*Proof.*
Set $z(t) = \frac{L+m-2t}{L-m}$ and choose $q_k(t) = \frac{T_k(z(t))}{T_k(z(0))}$, so $\deg q_k \leq k$ and $q_k(0) = 1$. Since $z([m,L]) = [-1,1]$, $|T_k(z(t))| \leq 1$ on $[m,L]$. Using $T_k(z(0)) = \frac{\rho^{-k}+\rho^k}{2}$ gives $\underset{t \in [m,L]}{\max}|q_k(t)| \leq \frac{2\rho^k}{1+\rho^{2k}} \leq 2\rho^k$. Apply the [[#^cg-polynomial-bound|polynomial error bound]].

::: definition:Preconditioned Conjugate Gradient Method
Let $A, M \in \mathbb{R}^{n, n}$ and $b, x_0 \in \mathbb{R}^n$. Assume $A \succ 0$ and $M \succ 0$. Set $\widetilde p_0 = b - Ax_0$ and $d_0 = M^{-1}\widetilde p_0$. The preconditioned conjugate gradient method for $Ax = b$ computes
$$
\begin{aligned}
a_k &= -\frac{\langle\widetilde p_k, M^{-1}\widetilde p_k\rangle}{\langle d_k, Ad_k\rangle},\\
x_{k+1} &= x_k - a_kd_k,\\
\widetilde p_{k+1} &= \widetilde p_k + a_kAd_k = b - Ax_{k+1},\\
\beta_{k+1} &= \frac{\langle\widetilde p_{k+1}, M^{-1}\widetilde p_{k+1}\rangle}{\langle\widetilde p_k, M^{-1}\widetilde p_k\rangle},\\
d_{k+1} &= M^{-1}\widetilde p_{k+1} + \beta_{k+1}d_k.
\end{aligned}
$$
Stop whenever $\widetilde p_j = 0$ and return $x_j$.
:::

::: note
Choose an invertible $C$ with $M = C^\top C$, and set $\widehat A = C^{-T}AC^{-1}$, $\widehat b = C^{-T}b$, and $\widehat x_0 = Cx_0$. [[#^conjugate-gradient-method|Conjugate Gradient Method]] applied to $\widehat A\widehat x = \widehat b$ initializes $\widehat p_0 = \widehat{\widetilde p}_0 = \widehat b - \widehat A\widehat x_0$. Make the substitutions $\widehat a_k = a_k$, $\widehat x_k = Cx_k$, $\widehat{\widetilde p}_k = C^{-T}\widetilde p_k$, $\widehat\beta_k = \beta_k$, and $\widehat p_k = Cd_k$. Thus $\widetilde p_0 = b - Ax_0$, $d_0 = M^{-1}\widetilde p_0$, and
$$
\begin{aligned}
\widehat a_k
= -\frac{\langle\widehat{\widetilde p}_k,\widehat{\widetilde p}_k\rangle}
{\langle\widehat p_k,\widehat A\widehat p_k\rangle}
&\quad\Longrightarrow\quad
a_k = -\frac{\langle\widetilde p_k,M^{-1}\widetilde p_k\rangle}{\langle d_k,Ad_k\rangle},\\
\widehat x_{k+1}
= \widehat x_k - \widehat a_k\widehat p_k
&\quad\Longrightarrow\quad
x_{k+1} = x_k - a_kd_k,\\
\widehat{\widetilde p}_{k+1}
= \widehat{\widetilde p}_k + \widehat a_k\widehat A\widehat p_k
&\quad\Longrightarrow\quad
\widetilde p_{k+1} = \widetilde p_k + a_kAd_k,\\
\widehat\beta_{k+1}
= \frac{\langle\widehat{\widetilde p}_{k+1},\widehat{\widetilde p}_{k+1}\rangle}
{\langle\widehat{\widetilde p}_k,\widehat{\widetilde p}_k\rangle}
&\quad\Longrightarrow\quad
\beta_{k+1} = \frac{\langle\widetilde p_{k+1},M^{-1}\widetilde p_{k+1}\rangle}{\langle\widetilde p_k,M^{-1}\widetilde p_k\rangle},\\
\widehat p_{k+1}
= \widehat{\widetilde p}_{k+1} + \widehat\beta_{k+1}\widehat p_k
&\quad\Longrightarrow\quad
d_{k+1} = M^{-1}\widetilde p_{k+1} + \beta_{k+1}d_k.
\end{aligned}
$$
Since $\lVert\widehat x_k - \widehat x^*\rVert_{\widehat A} = \lVert x_k - x^*\rVert_A$ for $\widehat x^* = Cx^*$, the [[#^cg-chebyshev-bound|Chebyshev convergence bound]] applies with $\kappa = \frac{\lambda_{\max}(\widehat A)}{\lambda_{\min}(\widehat A)}$.
:::
