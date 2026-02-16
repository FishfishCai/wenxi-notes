## Symmetric Positive Definite Matrix
> [!definition|] Symmetric Positive Definite Matrix
> Let $A\in \mathbb{R}^{n,n}$. $A$ is a symmetic positive definite matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.
> > 

> [!remark|]
> If $A$ is a symmetic positive definite matrix, then $\langle x, y \rangle :=y^{\top}Ax$ is an inner product.

## Orthogonal Matrix
> [!definition|] Orthogonal Matrix
> Let $Q \in \mathbb{R}^{n,n}$. Q is an orthonormal matrix if columns of $Q$ are orthonormal.

> [!Lemma|]
> $Q$ is an orthogonal matrix iff $Q^{\top}Q=I$.

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. $Q$ is an orthogonal matrix iff $\|Qx\|=\|x\|$ for all $x\in \mathbb{R}^{n}$.

^727a78

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, then $\|Qx-Qy\|=\|x-y\|$ for all $x, y\in \mathbb{R}^{n}$.

> [!lemma|] 
> Let $f:\mathbb{R}^{n}\to \mathbb{R}^{n}$. If $f(0)=0$ and $\|f(x)-f(y)\|=\|x-y\|$, then there exists an orthogonal matrix $Q$ s.t. $f(x)=Qx$.

`\begin{proof}`
Let $e_{1}, e_{2}, \cdots , e_{n}$ be the standard basis of $\mathbb{R}^{n}$. 
$$
\begin{align}
\|f(e_{i})-f(e_{j})\|=\|e_{i}-e_{j}\|&\implies(f(e_{i}))-f(e_{j})^{\top}(f(e_{i}))-f(e_{j})=(e_{i}-e_{j})^{\top}(e_{i}-e_{j})\\
&\implies f(e_{i})^{\top}f(e_{i})+f(e_{j})^{\top}f(e_{j})-2f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{i}+e_{j}^{\top}e_{j}-2e_{i}^{\top}e_{j}\\
&\implies f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{j}\\
\end{align}.
$$
This emplies that $f(e_{1}), f(e_{2}), \cdots , f(e_{n})$ form an orthonormal basis. And it is obvious that $Q=[f(e_{1}) \, f(e_{2}) \,\cdots \, f(e_{n})]$.
`\end{proof}`

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $|\lambda| = 1$.

^a712cb

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $e^{i\theta}$ is an eigenvalue of $Q$, then $e^{-i\theta}$ is an eigenvalue of $Q^{\top}$.

^f47e7a

> [!Lemma|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, $\lambda_{i}$ and $\lambda_{j}$ are two different eigenvalue of $Q$ and $v, w \in \mathbb{C}^{n}$ are two eigenvectors s.t. $Qv = \lambda_{i}v$ and $Qw=\lambda_{j}w$, then $v^{*}w=w^{*}v=0$.

^b5daf5

`\begin{proof}`
$\lambda_{i}w^{*}v=w^{*}\lambda_{i}v=w^{*}Qv=(Q^{\top}w)^{*}v=(\lambda_{j}^{-1}w)^{*}v=\lambda_{j}w^{*}v$, implying that $v^{*}w=w^{*}v=0$.
`\end{proof}`

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, then $\det(Q)=\pm1$.

^f982d8

> [!remark|]
> In [[#^f982d8]], if $\det(Q)=1$, then the columns of $Q$ have +ve orientation. And if $\det(Q)=-1$, then the columns of $Q$ have -ve orientation.

> [!Remark|] 
> Let  $A\in \mathbb{R}^{n,n}$, $\det(A)$ can be interp as the signed volume of the parallelepiped formed by the columns of $A$.

`\begin{proof}`
Following [[#^4b5424]], $\det(A)=\det(Q)\det(R)=\pm \prod r_{ii}$. The sign depends on the orientation of the $Q$.
`\end{proof}`

## Spectral Theorem
> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, then A has $n$ real eigenvalues.

`\begin{proof}`
Let $R(x)=\frac{x^{\top}Ax}{x^{\top}x}$  and $S^{n-1}=\{x\in \mathbb{R}^{n}:\|x\|=1\}$. Since $S^{n-1}$ is a compact set, there exists $x^{*}$ such that $x^{*\top}Ax^{*}=\underset{\|x\|=1}{\max}x^{\top}Ax$. Let $L(x,\lambda)=x^{\top}Ax-\lambda(x^{\top}x-1)$. By the method of Lagrange multipliers, $\nabla_{x}L(x^{*},\lambda)=0$, which implies $Ax^{*}=\lambda x^{*}$. Then we consider the subspace orthogonal to $x^*$ and iterate the argument.
`\end{proof}`

> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, $\lambda_{i}$ and $\lambda_{j}$ are two eigenvalue of $A$ and $v,\,w\in \mathbb{R}^{n}$ are two different eigenvectors s.t. $Av = \lambda_{i}v$ and $Aw=\lambda_{j}w$, then $v^{\top}w=w^{\top}v=0$.

`\begin{proof}`
$\lambda_{i}w^{\top}v=w^{\top}\lambda_{i}v=w^{\top}Av=(A^{\top}w)^{\top}v=(\lambda_{j}w)^{\top}v=\lambda_{j}w^{\top}v$, implying that $v^{\top}w=w^{\top}v=0$.
`\end{proof}`

> [!theorem|] Spectral Theorem
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, then $A$ admits an orthonormal basis consisting of eigenvectors.

`\begin{proof}`
This follows from [[#^6e7882]] and [[#^0a7023]].
`\end{proof}`
