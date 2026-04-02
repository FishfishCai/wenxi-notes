#LinearAlgebra 
Prerequisite knowledge: [[Vector Space]]
## Orthogonal Matrix
> [!definition|] Orthogonal Matrix
> Let $Q \in \mathbb{R}^{n,n}$. Q is an orthogonal matrix if columns of $Q$ are orthonormal.

^39be3e

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. $Q$ is an orthogonal matrix iff $Q^{\top}Q=I$.

^03854c

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. $Q$ is an orthogonal matrix iff $\|Qx\|=\|x\|$ for all $x\in \mathbb{R}^{n}$.

^727a78

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, $\|Qx-Qy\|=\|x-y\|$ for all $x, y\in \mathbb{R}^{n}$.

^4c69c4

> [!proposition|]
> Let $f:\mathbb{R}^{n}\to \mathbb{R}^{n}$. If $f(0)=0$ and $\|f(x)-f(y)\|=\|x-y\|$, there exists an orthogonal matrix $Q$ s.t. $f(x)=Qx$.

`\begin{proof}`
Let $e_{1}, e_{2}, \cdots , e_{n}$ be the standard basis of $\mathbb{R}^{n}$. 
$$
\begin{align}
\|f(e_{i})-f(e_{j})\|=\|e_{i}-e_{j}\|&\implies(f(e_{i})-f(e_{j}))^{\top}(f(e_{i})-f(e_{j}))=(e_{i}-e_{j})^{\top}(e_{i}-e_{j})\\
&\implies f(e_{i})^{\top}f(e_{i})+f(e_{j})^{\top}f(e_{j})-2f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{i}+e_{j}^{\top}e_{j}-2e_{i}^{\top}e_{j}\\
&\implies f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{j}\\
\end{align}.
$$
This emplies that $f(e_{1}), f(e_{2}), \cdots , f(e_{n})$ form an orthonormal basis. And it is obvious that $Q=[f(e_{1}) \, f(e_{2}) \,\cdots \, f(e_{n})]$.
`\end{proof}`

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, $|\lambda| = 1$.

^a712cb

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $\frac{1}{\lambda}$ is an eigenvalue of $Q^{\top}$.

^f47e7a

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, $\lambda_{i}$ and $\lambda_{j}$ are two different eigenvalue of $Q$ and $v, w \in \mathbb{C}^{n}$ are two eigenvectors corresponding to $\lambda_{i}$ and $\lambda_{j}$, $v^{*}w=w^{*}v=0$.

^b5daf5

`\begin{proof}`
$\lambda_{i}w^{*}v=w^{*}\lambda_{i}v=w^{*}Qv=(Q^{\top}w)^{*}v=(\lambda_{j}^{-1}w)^{*}v=\lambda_{j}w^{*}v$, implying that $v^{*}w=w^{*}v=0$.
`\end{proof}`

> [!proposition|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, $\det(Q)=\pm1$.

^f982d8

> [!remark|]
> For [[#^f982d8]], if $\det(Q)=1$,  the columns of $Q$ have +ve orientation. And if $\det(Q)=-1$, the columns of $Q$ have -ve orientation.

> [!Remark|] 
> Let  $A\in \mathbb{R}^{n,n}$. $\det(A)$ can be interperated as the signed volume of the parallelepiped formed by the columns of $A$.

`\begin{proof}`
Following [[Matrix Factorization#^4b5424]], $\det(A)=\det(Q)\det(R)=\pm \prod r_{ii}$. The sign depends on the orientation of the $Q$.
`\end{proof}`

## Spectral Theorem
> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, A has $n$ real eigenvalues.

^909e8b

`\begin{proof}`
Let $S^{n-1}=\{x\in \mathbb{R}^{n}:\|x\|=1\}$. Since $S^{n-1}$ is a compact set, there exists $x^{*}$ such that $x^{*\top}Ax^{*}=\underset{\|x\|=1}{\max}x^{\top}Ax$. Let $L(x,\lambda)=x^{\top}Ax-\lambda(x^{\top}x-1)$. By the method of Lagrange multipliers, $\nabla_{x}L(x^{*},\lambda)=0$, implying that $Ax^{*}=\lambda x^{*}$. Then we consider the subspace orthogonal to $x^*$ and iterate the argument.
`\end{proof}`

> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, $\lambda_{i}$ and $\lambda_{j}$ are two different eigenvalue of $A$ and $v,\,w\in \mathbb{R}^{n}$ are two eigenvectors corresponding to $\lambda_{i}$ and $\lambda_{j}$, $v^{\top}w=w^{\top}v=0$.

^81eb66

`\begin{proof}`
$\lambda_{i}w^{\top}v=w^{\top}\lambda_{i}v=w^{\top}Av=(A^{\top}w)^{\top}v=(\lambda_{j}w)^{\top}v=\lambda_{j}w^{\top}v$, implying that $v^{\top}w=w^{\top}v=0$.
`\end{proof}`

> [!theorem|] Spectral Theorem
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, $A$ admits an orthonormal basis consisting of eigenvectors.

`\begin{proof}`
This follows from [[#^909e8b]] and [[#^81eb66]] .
`\end{proof}`

## Unitary Matrix
> [!definition|] Unitary Matrix
> Let $Q\in \mathbb{C}^{n,n}$. Q is an unitary matrix if columns of $Q$ are orthonormal.

> [!remark|]
> The eigenvectors of an orthogonal matrix form an unitary matrix.

> [!remark|]
> [[#^03854c]], [[#^727a78]], [[#^4c69c4]], [[#^a712cb]], [[#^f47e7a]] and [[#^b5daf5]] follow if $^{\top}$ is changed to $^{*}$.

## Eigenvalue
> [!theorem|]
> Let $A, X \in \mathbb{C}^{n, n}$. Assume $X$ is nonsingular. The matrices $A$ and $X^{-1}AX$ have the same characteristic polynomial, eigenvalues, and algebraic and geometric multiplicities.

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$. The algebraic multiplicity of the eigenvalue $\lambda$ is at least as great as its geometric multiplicity.

`\begin{proof}`
Let $n$ be the geometric multiplicity of $\lambda$ for $A$. Form a matrix $\hat{V} \in \mathbb{C}^{m, n}$ whose $n$ columns constitute an orthonormal basis of the eigenspace $\{x : Ax = \lambda x\}$. Extend $\hat{V}$ to a square unitary matrix $V \in \mathbb{C}^{m, m}$. Then $B = V^* A V = \begin{bmatrix} \lambda I & C \\ 0 & D \end{bmatrix}$, where $I \in \mathbb{F}^{n, n}$ is the identity matrix, $C \in \mathbb{F}^{n, m-n}$, and $D \in \mathbb{F}^{m-n, m-n}$. $\det(zI - B) = \det(zI - \lambda I)\det(zI - D) = (z-\lambda)^n \det(zI - D)$. Therefore the algebraic multiplicity of $\lambda$ as an eigenvalue of $B$ is at least $n$. Since similarity transformations preserve multiplicities, the same is true for $A$.
`\end{proof}`

> [!Definition|] Defective Eigenvalue
> Let $A \in \mathbb{C}^{n, n}$ and $\lambda \in \mathbb{F}$. The eigenvalue $\lambda$ is a defective eigenvalue if its algebraic multiplicity exceeds its geometric multiplicity. 

> [!definition|] Defective Matrix
> Let $A \in \mathbb{C}^{n, n}$. The matrix $A$ is a defective matrix if it has one or more defective eigenvalues.

> [!theorem|]
> Let $A, X, \Lambda \in \mathbb{C}^{n, n}$. $\Lambda$ is a diagnol matrix. The matrix $A$ is nondefective iff it has an eigenvalue decomposition $A = X \Lambda X^{-1}$.

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$. Let $\lambda_1, \ldots, \lambda_n$ be the eigenvalues of $A$, counted with algebraic multiplicity. $\det(A) = \prod_{j=1}^{n} \lambda_j$ and $\operatorname{tr}(A) = \sum_{j=1}^{n} \lambda_j$.

> [!Definition|] Normal Matrix
> Let $A \in \mathbb{C}^{n, n}$. The matrix $A$ is a normal matrix if $A^*A = AA^*$.

> [!Theorem|]
> Let $A \in \mathbb{C}^{n, n}$. The matrix $A$ is unitarily diagonalizable iff it is normal.

> [!Theorem|] Schur Factorization
> Let $A \in \mathbb{C}^{n, n}$. There exists a unitary matrix $Q$ and an upper-triangular matrix $T$ s.t. $A = Q T Q^*$. Moreover, the eigenvalues of $A$ appear on the diagonal of $T$.

## Definiteness
> [!definition|] Symmetric Positive Definite Matrix
> Let $A\in \mathbb{R}^{n\times n}$. $A$ is a symmetric positive definite matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.

> [!definition|] Symmetric Positive Semidefinite Matrix
> Let $A\in \mathbb{R}^{n\times n}$. $A$ is a symmetric positive semidefinite matrix if $A=A^{\top}$ and $x^{\top}Ax\geq 0$ for all $x\in\mathbb{R}^n$.

> [!definition|] Symmetric Negative Definite Matrix
> Let $A\in \mathbb{R}^{n\times n}$. $A$ is a symmetric negative definite matrix if $A=A^{\top}$ and $x^{\top}Ax<0$ for all $x\neq 0$.

> [!definition|] Symmetric Negative Semidefinite Matrix
> Let $A\in \mathbb{R}^{n\times n}$. $A$ is a symmetric negative semidefinite matrix if $A=A^{\top}$ and $x^{\top}Ax\leq 0$ for all $x\in\mathbb{R}^n$.

> [!definition|] Symmetric Indefinite Matrix
> Let $A\in \mathbb{R}^{n\times n}$. $A$ is a symmetric indefinite matrix if $A=A^{\top}$ and there exist $x,y\in\mathbb{R}^n$ such that $x^{\top}Ax>0$ and $y^{\top}Ay<0$.

> [!definition|] Hermitian Positive Definite Matrix
> Let $A\in \mathbb{C}^{n\times n}$. $A$ is a Hermitian positive definite matrix if $A=A^{*}$ and $x^{*}Ax>0$ for all $x\neq 0$.

> [!definition|] Hermitian Positive Semidefinite Matrix
> Let $A\in \mathbb{C}^{n\times n}$. $A$ is a Hermitian positive semidefinite matrix if $A=A^{*}$ and $x^{*}Ax\geq 0$ for all $x\in\mathbb{C}^n$.

> [!definition|] Hermitian Negative Definite Matrix
> Let $A\in \mathbb{C}^{n\times n}$. $A$ is a Hermitian negative definite matrix if $A=A^{*}$ and $x^{*}Ax<0$ for all $x\neq 0$.

> [!definition|] Hermitian Negative Semidefinite Matrix
> Let $A\in \mathbb{C}^{n\times n}$. $A$ is a Hermitian negative semidefinite matrix if $A=A^{*}$ and $x^{*}Ax\leq 0$ for all $x\in\mathbb{C}^n$.

> [!definition|] Hermitian Indefinite Matrix
> Let $A\in \mathbb{C}^{n\times n}$. $A$ is a Hermitian indefinite matrix if $A=A^{*}$ and there exist $x,y\in\mathbb{C}^n$ such that $x^{*}Ax>0$ and $y^{*}Ay<0$.

> [!remark|]
> If $A$ is a symmetic positive definite matrix, then $\langle x, y \rangle :=y^{\top}Ax$ is an inner product.
