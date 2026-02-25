#LinearAlgebra 
Prerequisite knowledge: [[Real Vector Space]]
## Symmetric Positive Definite Matrix
> [!definition|] Symmetric Positive Definite Matrix
> Let $A\in \mathbb{R}^{n,n}$. $A$ is a symmetic positive definite matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.
> > 

> [!remark|]
> If $A$ is a symmetic positive definite matrix, then $\langle x, y \rangle :=y^{\top}Ax$ is an inner product.

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
\|f(e_{i})-f(e_{j})\|=\|e_{i}-e_{j}\|&\implies(f(e_{i}))-f(e_{j})^{\top}(f(e_{i}))-f(e_{j})=(e_{i}-e_{j})^{\top}(e_{i}-e_{j})\\
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
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $e^{i\theta}$ is an eigenvalue of $Q$, then $e^{-i\theta}$ is an eigenvalue of $Q^{\top}$.

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
Following [[QR Factorization#^4b5424]], $\det(A)=\det(Q)\det(R)=\pm \prod r_{ii}$. The sign depends on the orientation of the $Q$.
`\end{proof}`

## Spectral Theorem
> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, A has $n$ real eigenvalues.

^909e8b

`\begin{proof}`
Let $R(x)=\frac{x^{\top}Ax}{x^{\top}x}$  and $S^{n-1}=\{x\in \mathbb{R}^{n}:\|x\|=1\}$. Since $S^{n-1}$ is a compact set, there exists $x^{*}$ such that $x^{*\top}Ax^{*}=\underset{\|x\|=1}{\max}x^{\top}Ax$. Let $L(x,\lambda)=x^{\top}Ax-\lambda(x^{\top}x-1)$. By the method of Lagrange multipliers, $\nabla_{x}L(x^{*},\lambda)=0$, implying that $Ax^{*}=\lambda x^{*}$. Then we consider the subspace orthogonal to $x^*$ and iterate the argument.
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

## Singular Vector Decomposition
> [!Theorem|] Singular Vector Decomposition
> Let $A\in\mathbb{R}^{n,k}$. There exist orthogonal matrice $U\in\mathbb{R}^{n,n}$, orthogonal matrix $V\in\mathbb{R}^{k,k}$ and diagonal matrix $\Sigma=\begin{pmatrix}\sigma_1&0&\cdots&0\\0&\sigma_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\sigma_p\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&0\end{pmatrix}\in\mathbb{R}^{n,k}$ s.t. $A=U\Sigma V^\top$, where $\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_p\ge 0$ and $p=\min(n,k)$. The singular values ${\sigma_j}$ are uniquely determined.

`\begin{proof}`
Let $\sigma_1=\|A\|$. Consider $f(v)=\|Av\|$ on $\{v\in\mathbb{R}^k:\|v\|=1\}$. Since $f$ is continuous and $\{v\in\mathbb{R}^k:\|v\|=1\}$ is compact, there exists $v_1\in\mathbb{R}^k$ with $\|v_1\|=1$ s.t. $\|Av_1\|=\sigma_1$. Define $u_1=\frac{Av_1}{\sigma_{1}}$. Then $\|u_1\|=1$ and $Av_1=\sigma_1u_1$. Extend $u_1$ to an orthonormal basis $(u_1,u_2,\dots,u_n)$ of $\mathbb{R}^n$ and extend $v_1$ to an orthonormal basis $(v_1,v_2,\dots,v_k)$ of $\mathbb{R}^k$, and set $U_1=[u_1\,u_2\,\cdots\,u_n]\in\mathbb{R}^{n,n}$ and $V_1=[v_1\,v_2\,\cdots\,v_k]\in\mathbb{R}^{k,k}$. Define $S_{1}=U_1^\top A V_1 =\begin{pmatrix}\sigma_1&w^\top\\0&B_{1}\end{pmatrix}$ for some $w\in\mathbb{R}^{k-1}$ and $B\in\mathbb{R}^{n-1,k-1}$.
We now claim that $w=0$. Suppose $w\neq 0$. Then there exists $j\in\{2,\dots,k\}$ with $\alpha=u_1^\top Av_j\neq 0$. For any $t\in\mathbb{R}$, define $x_t=v_1+t v_j$. We have $\|x_t\|=\sqrt{1+t^2}$ and $u_1^\top A x_t=u_1^\top A v_1+t\,u_1^\top A v_j=\sigma_1+t\alpha$. Since $\|A x_t\|\ge |u_1^\top A x_t|$, it suffices to show that for some $t$ we have $|\sigma_1+t\alpha|>\sigma_1\sqrt{1+t^2}$. Choose $t$ with the same sign as $\alpha$ and sufficiently small. Then $\sigma_1+t\alpha>0$ and $(\sigma_1+t\alpha)^2-\sigma_1^2(1+t^2)=2\sigma_1\alpha t+(\alpha^2-\sigma_1^2)t^2>0$, so $\|A x_t\|\ge \sigma_1+t\alpha>\sigma_1\|x_t\|$. This implies $\|A\|>\sigma_1$, a contradiction. Therefore $u_1^\top Av_j=0$ for all $j\ge 2$, hence $w=0$ and $S_{1}=\begin{pmatrix}\sigma_1&0\\0&B_{1}\end{pmatrix}$.
Now for the $i$-th iteration, we do the same steps on $B_{i-1}$ and get $\hat S_{i}=\hat{U}_{i}^{\top}B_{i-1}\hat{V}_{i}=\begin{pmatrix}\sigma_i&0\\0&B_{i}\end{pmatrix}$. Let $U_{i}=\begin{pmatrix}I & 0 \\ 0 & \hat{U}_{i}\end{pmatrix}$ and $V_{i}=\begin{pmatrix}I & 0 \\ 0 & \hat{V}_{i}\end{pmatrix}$. Then, $S_{i}=U_{i}^{\top}S_{i-1}V_{i}$. Therefore, $S_{i}=U_{p}^{\top}\cdots U_{1}^{\top}AV_{1}V_{p}$. Finally, $S_{p}$ is in the form same to $\Sigma$ and we get $A=U\Sigma V$, where $U=U_{1}\cdots U_{p}$ and $V=V_{p}\cdots V_{1}$.
`\end{proof}`

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. The rank of $A$ is $r$, the number of nonzero singular values of $A$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. $A=U\Sigma V^\top$ and $\mathrm{rank}(A)=r$. $\mathrm{range}(A)=\langle u_1,\dots,u_r\rangle$ and $\mathrm{null}(A)=\langle v_{r+1},\dots,v_k\rangle$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. $A=U\Sigma V^\top$ and $\mathrm{rank}(A)=r$. $\|A\|=\sigma_1$ and $\|A\|_F=\sqrt{\sigma_1^2+\sigma_2^2+\cdots+\sigma_r^2}$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. The square of singular values of $A$ are theeigenvalues of $A^\top A$ and $AA^\top$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,n}$. Assume $A=A^\top$. The singular values of $A$ are the absolute values of the eigenvalues of $A$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,n}$. $|\det(A)|=\prod_{i=1}^{n}\sigma_i$.

> [!Theorem|] Eckart–Young–Mirsky
> Let $A\in\mathbb{R}^{n,k}$. $A=\sum_{j=1}^{r}\sigma_j u_j v_j^\top$ with $\sigma_1\ge\cdots\ge\sigma_r>0$. For any $\nu$ with $0\le \nu\le r$, define $A_\nu=\sum_{j=1}^{\nu}\sigma_j u_j v_j^\top$ and $\sigma_{r+1}=0$. $|A-A_\nu|=\inf_{\mathrm{rank}(B)\le \nu}|A-B|=\sigma_{\nu+1}$ and $|A-A_\nu|_F=\inf_{\mathrm{rank}(B)\le \nu}|A-B|_F=\sqrt{\sigma_{\nu+1}^2+\cdots+\sigma_r^2}$.
