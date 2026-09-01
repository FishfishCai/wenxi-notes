## Orthogonal Matrix
::: definition:Orthogonal Matrix
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix if the columns of $Q$ are orthonormal.
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix iff $Q^T Q = I$.
::: ^orthogonal-qtq-characterization

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. $Q$ is an orthogonal matrix iff $\|Qx\| = \|x\|$ for any $x \in \mathbb{R}^n$.
::: ^orthogonal-norm-preservation

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. If $Q$ is an orthogonal matrix, then $\|Qx - Qy\| = \|x - y\|$ for any $x, y \in \mathbb{R}^n$.
::: ^orthogonal-distance-preservation

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}^n$. Assume $f(0) = 0$ and $\|f(x) - f(y)\| = \|x - y\|$ for any $x, y \in \mathbb{R}^n$. There exists an orthogonal matrix $Q$ s.t. $f(x) = Qx$ for any $x \in \mathbb{R}^n$.
:::

::: proof
Let $e_{1}, e_{2}, \cdots , e_{n}$ be the standard basis of $\mathbb{R}^{n}$.
$$
\begin{align}
\|f(e_{i})-f(e_{j})\|=\|e_{i}-e_{j}\|&\implies(f(e_{i})-f(e_{j}))^T(f(e_{i})-f(e_{j}))=(e_{i}-e_{j})^T(e_{i}-e_{j})\\
&\implies f(e_{i})^Tf(e_{i})+f(e_{j})^Tf(e_{j})-2f(e_{i})^Tf(e_{j})=e_{i}^Te_{i}+e_{j}^Te_{j}-2e_{i}^Te_{j}\\
&\implies f(e_{i})^Tf(e_{j})=e_{i}^Te_{j}\\
\end{align}.
$$
This implies that $f(e_{1}), f(e_{2}), \cdots , f(e_{n})$ form an orthonormal basis. And it is obvious that $Q=[f(e_{1}) \, f(e_{2}) \,\cdots \, f(e_{n})]$.
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$ and $\lambda \in \mathbb{C}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $|\lambda| = 1$.
::: ^orthogonal-eigenvalue-modulus

::: proposition
Let $Q \in \mathbb{R}^{n, n}$ and $\lambda \in \mathbb{C}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $\frac{1}{\lambda}$ is an eigenvalue of $Q^T$.
::: ^orthogonal-transpose-reciprocal-eigenvalue

::: proposition
Let $Q \in \mathbb{R}^{n, n}$, $\lambda_{i}, \lambda_{j} \in \mathbb{C}$, and $v, w \in \mathbb{C}^{n}$. If $Q$ is an orthogonal matrix, $\lambda_{i}$ and $\lambda_{j}$ are distinct eigenvalues of $Q$, and $v, w$ are eigenvectors corresponding to $\lambda_{i}$ and $\lambda_{j}$, then $v^{*} w = w^{*} v = 0$.
::: ^orthogonal-distinct-eigenvectors

::: proof
$\lambda_{i}w^{*}v=w^{*}\lambda_{i}v=w^{*}Qv=(Q^Tw)^{*}v=(\lambda_{j}^{-1}w)^{*}v=\lambda_{j}w^{*}v$, implying that $v^{*}w=w^{*}v=0$.
:::

::: proposition
Let $Q \in \mathbb{R}^{n, n}$. If $Q$ is an orthogonal matrix, then $\det(Q) = \pm 1$.
::: ^orthogonal-determinant

::: note
For [[#^orthogonal-determinant|the determinant of an orthogonal matrix]], if $\det(Q) = 1$, the columns of $Q$ have positive orientation; if $\det(Q) = -1$, the columns of $Q$ have negative orientation.
:::

::: note
Let $A \in \mathbb{R}^{n, n}$. $\det(A)$ can be interpreted as the signed volume of the parallelepiped formed by the columns of $A$.
:::

::: proof
Following [[Matrix Factorization#^gram-schmidt-qr|Gram–Schmidt QR Factorization]], $\det(A)=\det(Q)\det(R)=\pm \prod r_{ii}$. The sign depends on the orientation of $Q$.
:::

## Spectral Theorem
::: lemma
Let $A \in \mathbb{R}^{n, n}$. If $A = A^T$, then $A$ has $n$ real eigenvalues.
::: ^symmetric-real-eigenvalues

::: proof
Let $S^{n-1}=\{x\in \mathbb{R}^{n}:\|x\|=1\}$. Since $S^{n-1}$ is a compact set, there exists $x^{*}$ s.t. $x^{*T}Ax^{*}=\underset{\|x\|=1}{\max}x^TAx$. Let $L(x,\lambda)=x^TAx-\lambda(x^Tx-1)$. By the method of Lagrange multipliers, $\nabla_{x}L(x^{*},\lambda)=0$, implying that $Ax^{*}=\lambda x^{*}$. Then we consider the subspace orthogonal to $x^*$ and iterate the argument.
:::

::: lemma
Let $A \in \mathbb{R}^{n, n}$, $\lambda_{i}, \lambda_{j} \in \mathbb{R}$, and $v, w \in \mathbb{R}^{n}$. If $A = A^T$, $\lambda_{i}$ and $\lambda_{j}$ are distinct eigenvalues of $A$, and $v, w$ are eigenvectors corresponding to $\lambda_{i}$ and $\lambda_{j}$, then $v^T w = w^T v = 0$.
::: ^symmetric-distinct-eigenvectors

::: proof
$\lambda_{i}w^Tv=w^T\lambda_{i}v=w^TAv=(A^Tw)^Tv=(\lambda_{j}w)^Tv=\lambda_{j}w^Tv$, implying that $v^Tw=w^Tv=0$.
:::

::: theorem:Spectral Theorem
Let $A \in \mathbb{R}^{n, n}$. If $A = A^T$, then $A$ admits an orthonormal basis consisting of eigenvectors.
:::

::: proof
This follows from [[#^symmetric-real-eigenvalues|the real-eigenvalue lemma]] and [[#^symmetric-distinct-eigenvectors|the orthogonality lemma]].
:::

## Unitary Matrix
::: definition:Unitary Matrix
Let $Q \in \mathbb{C}^{n, n}$. $Q$ is a unitary matrix if the columns of $Q$ are orthonormal.
:::

::: note
The eigenvectors of an orthogonal matrix form a unitary matrix.
:::

::: note
[[#^orthogonal-qtq-characterization|The $Q^TQ$ characterization]], [[#^orthogonal-norm-preservation|norm preservation]], [[#^orthogonal-distance-preservation|distance preservation]], [[#^orthogonal-eigenvalue-modulus|the eigenvalue-modulus result]], [[#^orthogonal-transpose-reciprocal-eigenvalue|the reciprocal-eigenvalue result]], and [[#^orthogonal-distinct-eigenvectors|the distinct-eigenvector orthogonality result]] follow if $^T$ is changed to $^{*}$.
:::

## Eigenvalue

::: definition:Eigenspace
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The eigenspace corresponding to $\lambda$ is $E_{\lambda} = \{x \in \mathbb{C}^{n} : Ax = \lambda x\}$.
:::

::: definition:Characteristic Polynomial
Let $A \in \mathbb{C}^{n, n}$. The characteristic polynomial of $A$ is $p_A(z) = \det(zI - A)$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. $\lambda$ is an eigenvalue of $A$ iff $p_A(\lambda) = 0$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. $A$ has $n$ eigenvalues, counted with algebraic multiplicity. In particular, if the roots of $p_A$ are simple, then $A$ has $n$ distinct eigenvalues.
:::

::: definition:Simple Eigenvalue
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. $\lambda$ is a simple eigenvalue if its algebraic multiplicity is $1$.
:::

::: definition:Similarity Transformation
Let $A, X \in \mathbb{C}^{n, n}$. Assume $X$ is nonsingular. The similarity transformation of $A$ by $X$ is the map $A \mapsto X^{-1} A X$.
:::

::: proposition
Let $A, X \in \mathbb{C}^{n, n}$. Assume $X$ is nonsingular. The matrices $A$ and $X^{-1} A X$ have the same characteristic polynomial, eigenvalues, and algebraic and geometric multiplicities.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. The algebraic multiplicity of $\lambda$ is at least as great as its geometric multiplicity.
:::

::: proof
Let $n$ be the geometric multiplicity of $\lambda$ for $A$. Form a matrix $\hat{V} \in \mathbb{C}^{m, n}$ whose $n$ columns constitute an orthonormal basis of the eigenspace $\{x : Ax = \lambda x\}$. Extend $\hat{V}$ to a square unitary matrix $V \in \mathbb{C}^{m, m}$. Then $B = V^* A V = \begin{bmatrix} \lambda I & C \\ 0 & D \end{bmatrix}$, where $I \in \mathbb{F}^{n, n}$ is the identity matrix, $C \in \mathbb{F}^{n, m-n}$, and $D \in \mathbb{F}^{m-n, m-n}$. $\det(zI - B) = \det(zI - \lambda I)\det(zI - D) = (z-\lambda)^n \det(zI - D)$. Therefore the algebraic multiplicity of $\lambda$ as an eigenvalue of $B$ is at least $n$. Since similarity transformations preserve multiplicities, the same is true for $A$.
:::

::: definition:Defective Eigenvalue
Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{C}$. Assume $\lambda$ is an eigenvalue of $A$. $\lambda$ is a defective eigenvalue if its algebraic multiplicity exceeds its geometric multiplicity.
:::

::: definition:Defective Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a defective matrix if it has one or more defective eigenvalues.
:::

::: proposition
Let $A, X, \Lambda \in \mathbb{C}^{n, n}$. Assume $\Lambda$ is a diagonal matrix. $A$ is nondefective iff it has an eigenvalue decomposition $A = X \Lambda X^{-1}$.
:::

::: proof
($\Longleftarrow$) Given $A = X\Lambda X^{-1}$, $\Lambda$ is diagonal and therefore nondefective. Since similarity transformations preserve eigenvalues and multiplicities, $A$ is nondefective.
($\Longrightarrow$) A nondefective matrix has $n$ linearly independent eigenvectors, since each eigenvalue contributes as many independent eigenvectors as its algebraic multiplicity. Form $X$ from these $n$ eigenvectors. Then $X$ is nonsingular and $A = X\Lambda X^{-1}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $\lambda_1, \ldots, \lambda_n$ be the eigenvalues of $A$, counted with algebraic multiplicity. $\det(A) = \prod_{j=1}^{n} \lambda_j$ and $\operatorname{tr}(A) = \sum_{j=1}^{n} \lambda_j$.
:::

::: proof
From the characteristic polynomial $p_A(z) = \det(zI - A)$ and its factorization $p_A(z) = \prod_{j=1}^{n}(z - \lambda_j)$, setting $z = 0$ gives $\det(-A) = (-1)^n\det(A) = (-1)^n\prod_{j=1}^{n}\lambda_j$, so $\det(A) = \prod_{j=1}^{n}\lambda_j$. For the trace, the coefficient of $z^{n-1}$ in $p_A(z) = \det(zI - A)$ is $-\sum_{j=1}^{n}a_{jj} = -\operatorname{tr}(A)$. From the factored form, the coefficient of $z^{n-1}$ is $-\sum_{j=1}^{n}\lambda_j$. Thus $\operatorname{tr}(A) = \sum_{j=1}^{n}\lambda_j$.
:::

::: definition:Normal Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a normal matrix if $A^* A = A A^*$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. $A$ is unitarily diagonalizable iff it is normal.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian, then $A$ is unitarily diagonalizable and its eigenvalues are real.
:::

::: theorem:Schur Factorization
Let $A \in \mathbb{C}^{n, n}$. There exist a unitary matrix $Q$ and an upper-triangular matrix $T$ s.t. $A = Q T Q^*$, and the eigenvalues of $A$ appear on the diagonal of $T$.
:::

::: proof
By induction on $n$. The case $n = 1$ is trivial. Suppose $n \ge 2$. Let $x$ be an eigenvector of $A$ with eigenvalue $\lambda$. Normalize $x$ and let it be the first column of a unitary matrix $U$. Then $U^{*}AU = \begin{pmatrix} \lambda & B \\ 0 & C \end{pmatrix}$. By the inductive hypothesis, $C$ has a Schur factorization $C = VTV^{*}$. Set $Q = U\begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$. Then $Q^{*}AQ = \begin{pmatrix} \lambda & BV \\ 0 & T \end{pmatrix}$, which is upper-triangular.
:::

## Definiteness
::: definition:Symmetric Positive Definite Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is a symmetric positive definite matrix if $A = A^T$ and $x^T A x > 0$ for any $x \neq 0$.
:::

::: definition:Symmetric Positive Semidefinite Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is a symmetric positive semidefinite matrix if $A = A^T$ and $x^T A x \geq 0$ for any $x \in \mathbb{R}^n$.
:::

::: definition:Symmetric Negative Definite Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is a symmetric negative definite matrix if $A = A^T$ and $x^T A x < 0$ for any $x \neq 0$.
:::

::: definition:Symmetric Negative Semidefinite Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is a symmetric negative semidefinite matrix if $A = A^T$ and $x^T A x \leq 0$ for any $x \in \mathbb{R}^n$.
:::

::: definition:Symmetric Indefinite Matrix
Let $A \in \mathbb{R}^{n, n}$. $A$ is a symmetric indefinite matrix if $A = A^T$ and there exist $x, y \in \mathbb{R}^n$ s.t. $x^T A x > 0$ and $y^T A y < 0$.
:::

::: definition:Hermitian Positive Definite Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a Hermitian positive definite matrix if $A = A^{*}$ and $x^{*} A x > 0$ for any $x \neq 0$.
:::

::: definition:Hermitian Positive Semidefinite Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a Hermitian positive semidefinite matrix if $A = A^{*}$ and $x^{*} A x \geq 0$ for any $x \in \mathbb{C}^n$.
:::

::: definition:Hermitian Negative Definite Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a Hermitian negative definite matrix if $A = A^{*}$ and $x^{*} A x < 0$ for any $x \neq 0$.
:::

::: definition:Hermitian Negative Semidefinite Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a Hermitian negative semidefinite matrix if $A = A^{*}$ and $x^{*} A x \leq 0$ for any $x \in \mathbb{C}^n$.
:::

::: definition:Hermitian Indefinite Matrix
Let $A \in \mathbb{C}^{n, n}$. $A$ is a Hermitian indefinite matrix if $A = A^{*}$ and there exist $x, y \in \mathbb{C}^n$ s.t. $x^{*} A x > 0$ and $y^{*} A y < 0$.
:::

::: note
If $A$ is a symmetric positive definite matrix, then $\langle x, y \rangle := y^T A x$ is an inner product.
:::
