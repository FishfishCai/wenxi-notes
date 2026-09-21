## Eigenvalue and Eigenspace
::: definition:Eigenspace
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The eigenspace corresponding to $\lambda$ is $E_{\lambda} = \{x \in \mathbb{C}^{n} : Ax = \lambda x\}$.
:::

::: definition:Characteristic Polynomial
Let $A \in \mathbb{C}^{n, n}$. The characteristic polynomial of $A$ is $p_A(z) = \det(zI - A)$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. $\lambda$ is an eigenvalue of $A$ iff $p_A(\lambda) = 0$.
:::

::: definition:Algebraic Multiplicity
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The algebraic multiplicity of $\lambda$ is its multiplicity as a root of $p_A(z) = \det(zI - A)$.
:::

::: definition:Geometric Multiplicity
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The geometric multiplicity of $\lambda$ is $\dim E_\lambda = \dim\operatorname{null}(A - \lambda I)$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. $A$ has $n$ eigenvalues, counted with algebraic multiplicity. In particular, if the roots of $p_A$ are simple, then $A$ has $n$ distinct eigenvalues.
:::

::: definition:Simple Eigenvalue
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. $\lambda$ is a simple eigenvalue if its algebraic multiplicity is $1$.
:::

::: definition:Defective Eigenvalue
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. $\lambda$ is a defective eigenvalue if its algebraic multiplicity exceeds its geometric multiplicity.
:::

::: definition:Defective Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a defective matrix if it has at least one defective eigenvalues.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda_1, \ldots, \lambda_n$ be the eigenvalues of $A$, counted with algebraic multiplicity. $\det(A) = \prod_{j = 1}^{n} \lambda_j$ and $\operatorname{tr}(A) = \sum_{j = 1}^{n} \lambda_j$.
:::

::: proof
From the characteristic polynomial $p_A(z) = \det(zI - A)$ and its factorization $p_A(z) = \prod_{j = 1}^{n}(z - \lambda_j)$, setting $z = 0$ gives $\det(-A) = (-1)^n\det(A) = (-1)^n\prod_{j = 1}^{n}\lambda_j$, so $\det(A) = \prod_{j = 1}^{n}\lambda_j$. For the trace, the coefficient of $z^{n - 1}$ in $p_A(z) = \det(zI - A)$ is $-\sum_{j = 1}^{n}a_{jj} = -\operatorname{tr}(A)$. From the factored form, the coefficient of $z^{n - 1}$ is $-\sum_{j = 1}^{n}\lambda_j$. Thus $\operatorname{tr}(A) = \sum_{j = 1}^{n}\lambda_j$.
:::

::: definition:Orthogonal Matrix
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix if the columns of $Q$ are orthonormal.
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix iff $Q^T Q = I$.
::: ^orthogonal-qtq-characterization

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix iff $\|Qx\|_2 = \|x\|_2$ for any $x \in \mathbb{R}^n$.
::: ^orthogonal-norm-preservation

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. If $Q$ is an orthogonal matrix, then $\|Qx - Qy\|_2 = \|x - y\|_2$ for any $x, y \in \mathbb{R}^n$.
::: ^orthogonal-distance-preservation

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}^n$. Assume $f(0) = 0$ and $\|f(x) - f(y)\|_2 = \|x - y\|_2$ for any $x, y \in \mathbb{R}^n$. There exists an orthogonal matrix $Q$ s.t. $f(x) = Qx$ for any $x \in \mathbb{R}^n$.
::: ^proposition-cba0f1

::: proof
Let $e_{1}, e_{2}, \cdots , e_{n}$ be the standard basis of $\mathbb{R}^{n}$.
$$
\begin{align}
\|f(e_{i}) - f(e_{j})\| = \|e_{i} - e_{j}\|& \implies (f(e_{i}) - f(e_{j}))^T(f(e_{i}) - f(e_{j})) = (e_{i} - e_{j})^T(e_{i} - e_{j})\\
& \implies f(e_{i})^Tf(e_{i}) + f(e_{j})^Tf(e_{j}) - 2f(e_{i})^Tf(e_{j}) = e_{i}^Te_{i} + e_{j}^Te_{j} - 2e_{i}^Te_{j}\\
& \implies f(e_{i})^Tf(e_{j}) = e_{i}^Te_{j}\\
\end{align}.
$$
This implies that $f(e_{1}), f(e_{2}), \cdots , f(e_{n})$ form an orthonormal basis. And it is obvious that $Q = [f(e_{1}) \, f(e_{2}) \, \cdots \, f(e_{n})]$.
:::

::: note
[[#^proposition-cba0f1|Proposition 15]] is a stronger converse to [[#^orthogonal-distance-preservation|Proposition 14]].
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. If $Q$ is an orthogonal matrix, then $\det(Q) = \pm 1$.
::: ^orthogonal-determinant

::: note
For [[#^orthogonal-determinant|Proposition 16]], if $\det(Q) = 1$, the columns of $Q$ have positive orientation; if $\det(Q) = -1$, the columns of $Q$ have negative orientation.
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$ and $\lambda \in \mathbb{C}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $|\lambda| = 1$.
::: ^orthogonal-eigenvalue-modulus

::: proposition
Let $Q \in \mathbb{R}^{n, n}$ and $\lambda \in \mathbb{C}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $\frac{1}{\lambda}$ is an eigenvalue of $Q^T$.
::: ^orthogonal-transpose-reciprocal-eigenvalue

::: proposition
Let $Q \in \mathbb{R}^{n, n}$, $\lambda_{i}, \lambda_{j} \in \mathbb{C}$, and $v, w \in \mathbb{C}^{n}$. If $Q$ is an orthogonal matrix, $\lambda_{i}$ and $\lambda_{j}$ are distinct eigenvalues of $Q$, and $v, w$ are eigenvectors corresponding to $\lambda_{i}$ and $\lambda_{j}$, then $v^H w = w^H v = 0$.
::: ^orthogonal-distinct-eigenvectors

::: proof
$\lambda_{i}w^Hv = w^H\lambda_{i}v = w^HQv = (Q^Tw)^Hv = (\lambda_{j}^{-1}w)^Hv = \lambda_{j}w^Hv$, implying that $v^Hw = w^Hv = 0$.
:::

::: definition:Unitary Matrix
Let $Q \in \mathbb{C}^{n, n}$. $Q$ is a unitary matrix if the columns of $Q$ are orthonormal.
:::

::: note
[[#^orthogonal-qtq-characterization|Proposition 12]], [[#^orthogonal-norm-preservation|Proposition 13]], [[#^orthogonal-distance-preservation|Proposition 14]], [[#^orthogonal-eigenvalue-modulus|Proposition 17]], [[#^orthogonal-transpose-reciprocal-eigenvalue|Proposition 18]], and [[#^orthogonal-distinct-eigenvectors|Proposition 19]] follow if $^T$ is changed to $^H$.
:::

::: definition:Similarity Transformation
Let $A, X \in \mathbb{C}^{n, n}$. Assume $X$ is nonsingular. The similarity transformation of $A$ by $X$ is the map $A \mapsto X^{-1} A X$.
:::

::: proposition
Let $A, X \in \mathbb{C}^{n, n}$. Assume $X$ is nonsingular. The matrices $A$ and $X^{-1} A X$ have the same characteristic polynomial, eigenvalues, algebraic multiplicities and geometric multiplicities.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The algebraic multiplicity of $\lambda$ is at least as great as its geometric multiplicity.
:::

::: proof
Let $m$ be the geometric multiplicity of $\lambda$ for $A$. Form a matrix $\hat{V} \in \mathbb{C}^{n, m}$ whose $m$ columns constitute an orthonormal basis of the eigenspace $\{x : Ax = \lambda x\}$. Extend $\hat{V}$ to a square unitary matrix $V \in \mathbb{C}^{n, n}$. Then $B = V^H A V = \begin{bmatrix} \lambda I_m & C \\ 0 & D \end{bmatrix}$, where $C \in \mathbb{C}^{m, n - m}$ and $D \in \mathbb{C}^{n - m, n - m}$. $\det(zI_n - B) = \det(zI_m - \lambda I_m)\det(zI_{n - m} - D) = (z - \lambda)^m \det(zI_{n - m} - D)$. Therefore the algebraic multiplicity of $\lambda$ as an eigenvalue of $B$ is at least $m$. Since similarity transformations preserve multiplicities, the same is true for $A$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. $A$ is nondefective iff there exist a nonsingular matrix $X \in \mathbb{C}^{n, n}$ and a diagonal matrix $\Lambda \in \mathbb{C}^{n, n}$ s.t. $A = X \Lambda X^{-1}$.
:::

::: proof
$\Longleftarrow$: Given $A = X\Lambda X^{-1}$, $\Lambda$ is diagonal and therefore nondefective. Since similarity transformations preserve eigenvalues and multiplicities, $A$ is nondefective. $\Longrightarrow$: A nondefective matrix has $n$ linearly independent eigenvectors, since each eigenvalue contributes as many independent eigenvectors as its algebraic multiplicity. Form $X$ from these $n$ eigenvectors. Then $X$ is nonsingular and $A = X\Lambda X^{-1}$.
:::

::: theorem:Schur Factorization
Let $A \in \mathbb{C}^{n, n}$. There exist a unitary matrix $Q$ and an upper-triangular matrix $T$ s.t. $A = Q T Q^H$, and the eigenvalues of $A$ appear on the diagonal of $T$.
:::

::: proof
By induction on $n$. The case $n = 1$ is trivial. Suppose $n \ge 2$. Let $x$ be an eigenvector of $A$ with eigenvalue $\lambda$. Normalize $x$ and let it be the first column of a unitary matrix $U$. Then $U^HAU = \begin{pmatrix} \lambda & B \\ 0 & C \end{pmatrix}$. By the inductive hypothesis, $C$ has a Schur factorization $C = VTV^H$. Set $Q = U\begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$. Then $Q^HAQ = \begin{pmatrix} \lambda & BV \\ 0 & T \end{pmatrix}$, which is upper-triangular.
:::

::: definition:Hermitian Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is Hermitian if $A = A^H$.
:::

::: definition:Symmetric Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is symmetric if $A = A^T$.
:::

::: definition:Normal Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a normal matrix if $A^H A = A A^H$.
:::

::: note
For real matrices, symmetry and Hermitian symmetry coincide. Every Hermitian matrix is normal since $A^H A = A^2 = AA^H$.
:::

::: theorem:Spectral Theorem
Let $A \in \mathbb{C}^{n, n}$. $A$ is normal iff there exist a unitary matrix $Q \in \mathbb{C}^{n, n}$ and a diagonal matrix $\Lambda \in \mathbb{C}^{n, n}$ s.t. $A = Q\Lambda Q^H$.
:::

::: proof
If $A = Q\Lambda Q^H$, then $A^H A = Q\Lambda^H\Lambda Q^H = Q\Lambda\Lambda^H Q^H = AA^H$.
Conversely, assume $A$ is normal. By Schur factorization, $A = QTQ^H$ with $Q$ unitary and $T$ upper-triangular. Since $T^H T = Q^H A^H A Q = Q^H AA^H Q = TT^H$, comparison of the $(1,1)$ entries gives $|t_{11}|^2 = \sum_{j = 1}^n |t_{1j}|^2$. Hence $t_{1j} = 0$ for $j > 1$, so $T = \operatorname{diag}(t_{11},T_1)$ with $T_1$ upper-triangular and normal. Induction on $n$ shows that $T$ is diagonal, giving the required factorization.
:::

::: lemma
Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian, then all eigenvalues of $A$ are real.
::: ^symmetric-real-eigenvalues

::: proof
If $Av = \lambda v$ and $v \neq 0$, then $\lambda = \frac{v^H A v}{v^H v}$. Since $\overline{v^H A v} = v^H A^H v = v^H A v$, the numerator is real, so $\lambda \in \mathbb{R}$.
:::

::: lemma
Let $A \in \mathbb{C}^{n, n}$, $\lambda,\mu \in \mathbb{R}$, and $u,v \in \mathbb{C}^n$. Assume $A$ is Hermitian, $\lambda \neq \mu$, and $u,v$ are eigenvectors corresponding to $\lambda,\mu$, respectively. $u^H v = v^H u = 0$.
::: ^symmetric-distinct-eigenvectors

::: proof
$\lambda u^H v = (Au)^H v = u^H Av = \mu u^H v$. Since $\lambda \neq \mu$, $u^H v = v^H u = 0$.
:::

::: corollary
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$. There exist a real orthogonal matrix $Q \in \mathbb{R}^{n, n}$ and a real diagonal matrix $\Lambda \in \mathbb{R}^{n, n}$ s.t. $A = Q\Lambda Q^T$.
:::
::: proof
Regard $A$ as a complex Hermitian matrix. The spectral theorem, together with [[#^symmetric-real-eigenvalues|Lemma 30]] and [[#^symmetric-distinct-eigenvectors|Lemma 31]], gives the required real orthogonal factorization.
:::

::: theorem:Rayleigh–Ritz Theorem
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and its eigenvalues satisfy $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$. $\lambda_n \leq \frac{x^T A x}{x^T x} \leq \lambda_1$ for any $x \in \mathbb{R}^n \setminus \{0\}$. Moreover, $\lambda_1 = \underset{\|x\| = 1}{\max}x^T A x$ and $\lambda_n = \underset{\|x\| = 1}{\min}x^T A x$.
:::

::: proof
Set $r(x) = \frac{x^T A x}{x^T x}$ for $x \neq 0$, the Rayleigh quotient. By the spectral theorem, choose an orthonormal eigenbasis $q_1,\ldots,q_n$ and write $x = \sum_{j = 1}^n c_jq_j$. Then
$$
r(x) = \frac{\sum_{j = 1}^n \lambda_j c_j^2}{\sum_{j = 1}^n c_j^2}.
$$
This is a weighted average of the eigenvalues, so $\lambda_n \leq r(x) \leq \lambda_1$. Taking $x = q_1$ and $x = q_n$ attains the upper and lower bounds, respectively. On the unit sphere, $r(x) = x^T A x$, proving both extremal formulas.
In particular, $r(q) = \lambda$ whenever $Aq = \lambda q$ and $q \neq 0$. Differentiation gives $\nabla r(x) = \frac{2}{x^T x}(Ax - r(x)x)$, so $\nabla r(q) = 0$ at every eigenvector. Since $r$ is smooth near any nonzero eigenvector $q$, Taylor expansion gives $r(x) - r(q) = O(\|x - q\|_2^2)$ as $x \to q$.
::: ^rayleigh-quotient

::: definition:Definiteness of Symmetric Matrices
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$. $A$ is positive definite if $x^T A x > 0$ for any $x \in \mathbb{R}^n \setminus \{0\}$, and positive semidefinite if $x^T A x \geq 0$ for any $x \in \mathbb{R}^n$. $A$ is negative definite or negative semidefinite if $-A$ is positive definite or positive semidefinite, respectively. $A$ is indefinite if there exist $x, y \in \mathbb{R}^n$ s.t. $x^T A x > 0$ and $y^T A y < 0$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$. $A$ is positive semidefinite iff all eigenvalues of $A$ are nonnegative.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. $A$ is symmetric positive semidefinite iff there exists $B \in \mathbb{R}^{n, n}$ s.t. $A = B^T B$. In this case, $A$ has a unique symmetric positive semidefinite square root $A^{\frac{1}{2}}$.
:::

::: proof
If $A = B^T B$, then $A = A^T$ and $x^T A x = \|Bx\|_2^2 \geq 0$ for any $x \in \mathbb{R}^n$. Conversely, if $A$ is symmetric positive semidefinite, its spectral decomposition is $A = U\Lambda U^T$ with $\Lambda = \operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ and $\lambda_j \geq 0$. Set $C = U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})U^T.$ Then $C$ is symmetric positive semidefinite and $C^2 = A$. Taking $B = C$ gives $A = B^T B$.
For uniqueness, let $D$ be any symmetric positive semidefinite matrix with $D^2 = A$. Since $DA = D^3 = AD$, each eigenspace $E_\lambda$ of $A$ is invariant under $D$. The restriction of $D$ to $E_\lambda$ is symmetric positive semidefinite, and its eigenvalues $\mu$ satisfy $\mu^2 = \lambda$. Hence it equals $\sqrt{\lambda}I$ on $E_\lambda$. This determines $D$ uniquely and gives $D = C = A^{\frac{1}{2}}$.
:::

::: definition:Definiteness of Hermitian Matrices
Let $A \in \mathbb{C}^{n, n}$. Assume $A = A^H$. $A$ is positive definite if $x^H A x > 0$ for any $x \in \mathbb{C}^n \setminus \{0\}$, and positive semidefinite if $x^H A x \geq 0$ for any $x \in \mathbb{C}^n$. $A$ is negative definite or negative semidefinite if $-A$ is positive definite or positive semidefinite, respectively. $A$ is indefinite if there exist $x, y \in \mathbb{C}^n$ s.t. $x^H A x > 0$ and $y^H A y < 0$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian positive definite, then the eigenvalues of $A$ are positive real numbers.
:::

::: theorem:Cholesky Factorization
Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian positive definite, then $A$ has a unique Cholesky factorization $A = R^HR$, where $R \in \mathbb{C}^{n, n}$ is upper-triangular with positive diagonal entries $r_{jj} > 0$.
::: ^cholesky-factorization

::: proof
Existence: Write $A = \begin{pmatrix} a_{11} & w^H \\ w & K \end{pmatrix}$ with $a_{11} > 0$. Set $\alpha = \sqrt{a_{11}}$. Then $A = R_1^HA_1R_1$ where $R_1 = \begin{pmatrix} \alpha & \frac{w^H}{\alpha} \\ 0 & I \end{pmatrix}$ and $A_1 = \begin{pmatrix} 1 & 0 \\ 0 & K - \frac{ww^H}{a_{11}} \end{pmatrix}$. The submatrix $K - \frac{ww^H}{a_{11}}$ is positive definite since it is an $(n - 1) \times (n - 1)$ principal submatrix of $R_1^{-H}AR_1^{-1}$. By induction, all submatrices $A_j$ that appear are positive definite, so the process cannot break down, giving $A = R^HR$.
Uniqueness: At each step, $\alpha = \sqrt{a_{11}}$ is uniquely determined, which determines the first row of $R_1$. By induction, the factorization of each $A_j$ is unique, so $R$ is unique.
:::

## Singular Value Decomposition
::: theorem:Singular Value Decomposition
Let $A \in \mathbb{R}^{n, k}$. There exist orthogonal matrices $U \in \mathbb{R}^{n, n}$, orthogonal matrix $V \in \mathbb{R}^{k, k}$ and diagonal matrix $\Sigma = \begin{pmatrix}\sigma_1&0&\cdots&0\\0&\sigma_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\sigma_p\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&0\end{pmatrix} \in \mathbb{R}^{n, k}$ s.t. $A = U\Sigma V^T$, where $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_p \ge 0$ and $p = \min(n, k)$. The singular values $\sigma_j$ are uniquely determined. For $p < j \le k$, set $\sigma_j = 0$.
::: ^singular-value-decomposition

::: proof
Let $\sigma_1 = \|A\|$. Consider $f(v) = \|Av\|$ on $\{v \in \mathbb{R}^k:\|v\| = 1\}$. Since $f$ is continuous and $\{v \in \mathbb{R}^k:\|v\| = 1\}$ is compact, there exists $v_1 \in \mathbb{R}^k$ with $\|v_1\| = 1$ s.t. $\|Av_1\| = \sigma_1$. If $\sigma_1 = 0$, then $A = 0$ and the result follows by taking $U = I_n$, $V = I_k$, and $\Sigma = 0$. Assume $\sigma_1 > 0$. Define $u_1 = \frac{Av_1}{\sigma_{1}}$. Then $\|u_1\| = 1$ and $Av_1 = \sigma_1u_1$. Extend $u_1$ to an orthonormal basis $(u_1, u_2, \dots, u_n)$ of $\mathbb{R}^n$ and extend $v_1$ to an orthonormal basis $(v_1, v_2, \dots, v_k)$ of $\mathbb{R}^k$, and set $U_1 = [u_1\, u_2\, \cdots\, u_n] \in \mathbb{R}^{n, n}$ and $V_1 = [v_1\, v_2\, \cdots\, v_k] \in \mathbb{R}^{k, k}$. Define $S_{1} = U_1^T A V_1 = \begin{pmatrix}\sigma_1&w^T\\0&B_{1}\end{pmatrix}$ for some $w \in \mathbb{R}^{k - 1}$ and $B_1 \in \mathbb{R}^{n - 1, k - 1}$. We now claim that $w = 0$. Suppose $w \neq 0$. Then there exists $j \in \{2, \dots, k\}$ with $\alpha = u_1^T Av_j \neq 0$. For any $t \in \mathbb{R}$, define $x_t = v_1 + t v_j$. We have $\|x_t\| = \sqrt{1 + t^2}$ and $u_1^T A x_t = u_1^T A v_1 + t\, u_1^T A v_j = \sigma_1 + t\alpha$. Since $\|A x_t\| \ge |u_1^T A x_t|$, it suffices to show that for some $t$ we have $|\sigma_1 + t\alpha| > \sigma_1\sqrt{1 + t^2}$. Choose $t$ with the same sign as $\alpha$ and sufficiently small. Then $\sigma_1 + t\alpha > 0$ and $(\sigma_1 + t\alpha)^2 - \sigma_1^2(1 + t^2) = 2\sigma_1\alpha t + (\alpha^2 - \sigma_1^2)t^2 > 0$, so $\|A x_t\| \ge \sigma_1 + t\alpha > \sigma_1\|x_t\|$. This implies $\|A\| > \sigma_1$, a contradiction. Therefore $u_1^T Av_j = 0$ for all $j \ge 2$, hence $w = 0$ and $S_{1} = \begin{pmatrix}\sigma_1&0\\0&B_{1}\end{pmatrix}$. Now for the $i$-th iteration, let $\sigma_i = \|B_{i - 1}\|$. If $\sigma_i = 0$, then $B_{i - 1} = 0$; set $U_\ell$ and $V_\ell$ to identity matrices and $\sigma_\ell = 0$ for all $\ell \ge i$, and terminate the iteration. Otherwise, we do the same steps on $B_{i - 1}$ and get $\hat S_{i} = \hat{U}_{i}^TB_{i - 1}\hat{V}_{i} = \begin{pmatrix}\sigma_i&0\\0&B_{i}\end{pmatrix}$. Let $U_{i} = \begin{pmatrix}I & 0 \\ 0 & \hat{U}_{i}\end{pmatrix}$ and $V_{i} = \begin{pmatrix}I & 0 \\ 0 & \hat{V}_{i}\end{pmatrix}$. Then, $S_{i} = U_{i}^TS_{i - 1}V_{i}$. Therefore, $S_i = U_i^T\cdots U_1^T A V_1\cdots V_i$. Finally, $S_p$ has the same form as $\Sigma$ and we get $A = U\Sigma V^T$, where $U = U_1\cdots U_p$ and $V = V_1\cdots V_p$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $A = U\Sigma V^T$ is a singular value decomposition. Set $p = \min(n, k)$ and denote the $i$-th columns of $U$ and $V$ by $u_i$ and $v_i$, respectively. $Av_i = \sigma_i u_i$ and $A^T u_i = \sigma_i v_i$ for any $i \in \{1, \ldots, p\}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $A = U\Sigma V^T$ is a singular value decomposition. Set $r = \mathrm{rank}(A)$, denote the columns of $U, V$ by $u_i, v_i$, and denote the singular values by $\sigma_i$. $\|A\|_2 = \sigma_1$, $\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2}$, and $\|A\|_2 \leq \|A\|_F \leq \sqrt{r}\|A\|_2$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. The nonzero eigenvalues of $A^T A$ and $AA^T$ are the squares of the nonzero singular values of $A$, with the same multiplicities.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. If $A = A^T$, then the singular values of $A$ are the absolute values of the eigenvalues of $A$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. $|\det(A)| = \prod_{i = 1}^{n}\sigma_i$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $j \in \{1, 2, \dots, k\}$. The $j$-th singular value satisfies $\sigma_j(A) = \underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|}$, where $V_j$ varies over all subspaces of $\mathbb{R}^k$ with dimension $j$.
::: ^singular-value-max-min

::: proof
Let $A \in \mathbb{R}^{n, k}$, and let $v_1, \dots, v_k$ be right singular vectors of $A$ corresponding to singular values $\sigma_1(A) \ge \cdots \ge \sigma_k(A) \ge 0$. We prove $\sigma_j(A) = \underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|}$.
First, we show that $\underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \ge \sigma_j(A)$. Take $\widehat V_j = \operatorname{span}\{v_1, \dots, v_j\}$. For any $x \in \widehat V_j$, $x = \sum_{i = 1}^j \alpha_i v_i$. Then $\|x\|^2 = \sum_{i = 1}^j |\alpha_i|^2$ and $\|Ax\|^2 = \sum_{i = 1}^j \sigma_i(A)^2 |\alpha_i|^2$. Since $\sigma_i(A) \ge \sigma_j(A)$ for all $1 \le i \le j$, we have $\|Ax\|^2 \ge \sigma_j(A)^2\sum_{i = 1}^j |\alpha_i|^2 = \sigma_j(A)^2\|x\|^2$. Hence for every nonzero $x \in \widehat V_j$, $\frac{\|Ax\|}{\|x\|} \ge \sigma_j(A)$. Therefore $\underset{x \in \widehat V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \ge \sigma_j(A)$, so $\underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \ge \sigma_j(A)$. On the other hand, taking $x = v_j$, we get $\frac{\|Av_j\|}{\|v_j\|} = \sigma_j(A)$, so $\underset{x \in \widehat V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} = \sigma_j(A)$.
Next, we show that $\underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \le \sigma_j(A)$. Let $V_j \subset \mathbb{R}^k$ be any $j$-dimensional subspace, and set $W = \operatorname{span}\{v_j, \dots, v_k\}$. Then $\dim W = k - j + 1$. By the dimension formula, $\dim(V_j\cap W) \ge \dim V_j + \dim W - k = j + (k - j + 1) - k = 1$. Hence there exists a nonzero vector $x \in V_j\cap W$. Since $x \in W$, write $x = \sum_{i = j}^k \alpha_i v_i$. Then $\|x\|^2 = \sum_{i = j}^k |\alpha_i|^2$ and $\|Ax\|^2 = \sum_{i = j}^k \sigma_i(A)^2 |\alpha_i|^2$. Since $\sigma_i(A) \le \sigma_j(A)$ for all $i \ge j$, we obtain $\|Ax\|^2 \le \sigma_j(A)^2\sum_{i = j}^k |\alpha_i|^2 = \sigma_j(A)^2\|x\|^2$. Thus $\frac{\|Ax\|}{\|x\|} \le \sigma_j(A)$. Because $x \in V_j$, it follows that $\underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \le \sigma_j(A)$. Since $V_j$ was arbitrary, $\underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \le \sigma_j(A)$.
Combining the two inequalities gives $\sigma_j(A) = \underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $j \in \{1, 2, \dots, k\}$. The $j$-th singular value satisfies $\sigma_j(A) = \underset{V_{k - j + 1}}{\min}\ \underset{x \in V_{k - j + 1}, \ x \ne 0}{\max}\frac{\|Ax\|}{\|x\|}$, where $V_{k - j + 1}$ varies over all subspaces of $\mathbb{R}^k$ with dimension $k - j + 1$.
::: ^singular-value-min-max

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $1 \leq k' \leq k$. Set $\hat A \in \mathbb{R}^{n, k'}$ to be obtained by removing $k - k'$ columns of $A$, and denote the singular values of $A, \hat A$ by $\sigma_j, \hat\sigma_j$, with zeros appended through indices $k, k'$, respectively. The singular values of $A$ and $\hat A$ satisfy the inequalities $\sigma_{j} \ge \hat\sigma_{j} \ge \sigma_{j + k - k'}$ for $j = 1, \cdots , k'$.
:::

::: proof
Let $H \subset \mathbb{R}^k$ be the coordinate subspace corresponding to the remaining $k'$ columns, so that $\dim H = k'$, and $\hat A$ is exactly the restriction of $A$ to $H$. Hence, for every subspace $V \subset \mathbb{R}^{k'}$, identifying $V$ with a subspace of $H$, the quotient $\frac{\|\hat A x\|}{\|x\|}$ agrees with $\frac{\|A x\|}{\|x\|}$. By [[#^singular-value-max-min|Proposition 46]], $\hat\sigma_j = \underset{V_j \subset H}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} \leq \underset{V_j \subset \mathbb{R}^k}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|}{\|x\|} = \sigma_j$. By [[#^singular-value-min-max|Proposition 47]], $\hat\sigma_j = \underset{W_{k'-j + 1} \subset H}{\min}\ \underset{x \in W_{k'-j + 1}, \ x \ne 0}{\max}\frac{\|Ax\|}{\|x\|} \geq \underset{W_{k'-j + 1} \subset \mathbb{R}^k}{\min}\ \underset{x \in W_{k'-j + 1}, \ x \ne 0}{\max}\frac{\|Ax\|}{\|x\|} = \sigma_{j + k - k'}$.
:::

::: proposition
Let $A, E \in \mathbb{R}^{n, k}$ and $j \in \{1, 2, \dots, k\}$. The singular values satisfy $\sigma_j(A) - \|E\|_2 \le \sigma_j(A + E) \le \sigma_j(A) + \|E\|_2$.
:::

::: proof
By [[#^singular-value-min-max|Proposition 47]], $\sigma_j(A + E) = \underset{V_{k - j + 1}}{\min}\ \underset{x \in V_{k - j + 1}, \ x \ne 0}{\max}\frac{\|(A + E)x\|_2}{\|x\|_2} \le \underset{V_{k - j + 1}}{\min}\ \underset{x \in V_{k - j + 1}, \ x \ne 0}{\max}\frac{\|Ax\|_2}{\|x\|_2} + \|E\|_2 = \sigma_j(A) + \|E\|_2$. And by [[#^singular-value-max-min|Proposition 46]], $\sigma_j(A + E) = \underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|(A + E)x\|_2}{\|x\|_2} \ge \underset{V_j}{\max}\ \underset{x \in V_j, \ x \ne 0}{\min}\frac{\|Ax\|_2}{\|x\|_2} - \|E\|_2 = \sigma_j(A) - \|E\|_2$.
:::

::: theorem:Eckart–Young Theorem
Let $A \in \mathbb{R}^{n, k}$. Assume $A = \sum_{j = 1}^{r}\sigma_j u_j v_j^T$ is a singular value decomposition with $r = \operatorname{rank}(A)$ and $\sigma_1 \geq \cdots \geq \sigma_r > 0$. Set $A_\nu = \sum_{j = 1}^{\nu}\sigma_j u_j v_j^T$ for $\nu \in \{0, 1, \dots, r\}$ and $\sigma_{r + 1} = 0$. The matrix $A_\nu$ satisfies $\|A - A_\nu\| = \underset{\operatorname{rank}(B) \le \nu}{\inf}\|A - B\| = \sigma_{\nu + 1}$. It also satisfies $\|A - A_\nu\|_F = \underset{\operatorname{rank}(B) \le \nu}{\inf}\|A - B\|_F = \sqrt{\sigma_{\nu + 1}^2 + \cdots + \sigma_r^2}$.
:::

## Projection
::: definition:Projection Matrix of Vector
Let $v \in \mathbb{R}^n$. Assume $\|v\|_2 = 1$. The projection matrix of vector $v$ is $vv^T$, whose rank is $1$. For any $x \in \mathbb{R}^n$, the component of $x$ along $v$ is $vv^T x$.
:::

::: definition:Orthogonal Projection Matrix of Vector
Let $v \in \mathbb{R}^n$. Assume $\|v\|_2 = 1$. The orthogonal projection matrix onto the subspace orthogonal to $v$ is $I - vv^T$, whose rank is $n - 1$.
:::

::: proposition
Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If $\{v_1, v_2, \dots, v_k\}$ is an orthonormal set, then the matrix $P = v_1 v_1^T + \cdots + v_k v_k^T$ is the projection matrix onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$.
::: ^orthonormal-subspace-projection

::: note
Let $V = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n, k}$. The projection matrix $P$ in [[#^orthonormal-subspace-projection|Proposition 53]] admits the factorization $P = VV^T$, whose rank is $k$. For any $x \in \mathbb{R}^n$, the vector $V^T x$ gives the coefficients of the projection of $x$ onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$. The complementary projection matrix is $I - VV^T$, whose rank is $n - k$.
:::

::: theorem:QR Factorization
Let $A \in \mathbb{R}^{n, k}$. Assume $n \geq k$ and $A$ has full column rank. There exist a matrix $Q \in \mathbb{R}^{n, k}$ with $Q^TQ = I_k$ and an upper-triangular matrix $R \in \mathbb{R}^{k, k}$ with positive diagonal entries s.t. $A = QR$. The factorization is unique under this sign convention.
::: ^qr-factorization

::: definition:Projection Matrix of Matrix
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. The projection matrix of matrix $A$ is $P = A(A^T A)^{-1} A^T$. For any $x \in \mathbb{R}^n$, the component of $x$ in $\text{range}(A)$ is $Px$.
:::

::: note
Let $A \in \mathbb{R}^{n, n}$. $\det(A)$ can be interpreted as the signed volume of the parallelepiped formed by the columns of $A$.
:::

::: proof
Following [[#^qr-factorization|Theorem 54 (QR Factorization)]], $\det(A) = \det(Q)\det(R) = \pm \prod r_{ii}$. The sign depends on the orientation of $Q$.
:::

::: definition:Pseudoinverse
Let $A \in \mathbb{R}^{n,k}$. Set $A = U\Sigma V^T$ to be a singular value decomposition, and construct $\Sigma^+ \in \mathbb{R}^{k,n}$ by transposing $\Sigma$ and replacing each nonzero diagonal entry by its reciprocal. The pseudoinverse of $A$ is $A^+ := V\Sigma^+U^T$. If $A$ has full column rank, then $A^+ = (A^T A)^{-1}A^T$.
::: ^pseudoinverse

::: theorem:Least Square
Let $A \in \mathbb{R}^{n, k}$, $b \in \mathbb{R}^n$ and $x \in \mathbb{R}^k$. $x$ minimizes $\|b - Ax\|_2$ iff $A^T A x = A^T b$.
::: ^least-square

::: proof
Let $P$ be the projection matrix onto $\mathrm{range}(A)$. $\|b - b'\|^2 = \|b - Pb\|^2 + \|Pb - b'\|^2 \geq \|b - Pb\|^2$, implying $b'$ minimizes $\|b - b'\|$ iff $b' = Pb$. Since $Ax \in \mathrm{range}(A)$, $x$ minimizes $\|b - Ax\|$ iff $Ax = b'$. $Ax = b'$ is equivalent to $A^T(b - Ax) = 0$.
:::

::: note
For [[#^least-square|Theorem 57 (Least Square)]], if $A$ is full column rank, $x = A^{+} b$.
:::
