#NumericalLinearAlgebra
Prerequisite knowledge: [[Matrix]], [[Floating Point Arithmetic]]
## Singular Vector Decomposition
> [!Theorem|] Singular Vector Decomposition
> Let $A\in\mathbb{R}^{n,k}$. There exist orthogonal matrice $U\in\mathbb{R}^{n,n}$, orthogonal matrix $V\in\mathbb{R}^{k,k}$ and diagonal matrix $\Sigma=\begin{pmatrix}\sigma_1&0&\cdots&0\\0&\sigma_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\sigma_p\\0&0&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&0\end{pmatrix}\in\mathbb{R}^{n,k}$ s.t. $A=U\Sigma V^\top$, where $\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_p\ge 0$ and $p=\min(n,k)$. The singular values ${\sigma_j}$ are uniquely determined.

`\begin{proof}`
Let $\sigma_1=\|A\|$. Consider $f(v)=\|Av\|$ on $\{v\in\mathbb{R}^k:\|v\|=1\}$. Since $f$ is continuous and $\{v\in\mathbb{R}^k:\|v\|=1\}$ is compact, there exists $v_1\in\mathbb{R}^k$ with $\|v_1\|=1$ s.t. $\|Av_1\|=\sigma_1$. Define $u_1=\frac{Av_1}{\sigma_{1}}$. Then $\|u_1\|=1$ and $Av_1=\sigma_1u_1$. Extend $u_1$ to an orthonormal basis $(u_1,u_2,\dots,u_n)$ of $\mathbb{R}^n$ and extend $v_1$ to an orthonormal basis $(v_1,v_2,\dots,v_k)$ of $\mathbb{R}^k$, and set $U_1=[u_1\,u_2\,\cdots\,u_n]\in\mathbb{R}^{n,n}$ and $V_1=[v_1\,v_2\,\cdots\,v_k]\in\mathbb{R}^{k,k}$. Define $S_{1}=U_1^\top A V_1 =\begin{pmatrix}\sigma_1&w^\top\\0&B_{1}\end{pmatrix}$ for some $w\in\mathbb{R}^{k-1}$ and $B\in\mathbb{R}^{n-1,k-1}$. We now claim that $w=0$. Suppose $w\neq 0$. Then there exists $j\in\{2,\dots,k\}$ with $\alpha=u_1^\top Av_j\neq 0$. For any $t\in\mathbb{R}$, define $x_t=v_1+t v_j$. We have $\|x_t\|=\sqrt{1+t^2}$ and $u_1^\top A x_t=u_1^\top A v_1+t\,u_1^\top A v_j=\sigma_1+t\alpha$. Since $\|A x_t\|\ge |u_1^\top A x_t|$, it suffices to show that for some $t$ we have $|\sigma_1+t\alpha|>\sigma_1\sqrt{1+t^2}$. Choose $t$ with the same sign as $\alpha$ and sufficiently small. Then $\sigma_1+t\alpha>0$ and $(\sigma_1+t\alpha)^2-\sigma_1^2(1+t^2)=2\sigma_1\alpha t+(\alpha^2-\sigma_1^2)t^2>0$, so $\|A x_t\|\ge \sigma_1+t\alpha>\sigma_1\|x_t\|$. This implies $\|A\|>\sigma_1$, a contradiction. Therefore $u_1^\top Av_j=0$ for all $j\ge 2$, hence $w=0$ and $S_{1}=\begin{pmatrix}\sigma_1&0\\0&B_{1}\end{pmatrix}$. Now for the $i$-th iteration, we do the same steps on $B_{i-1}$ and get $\hat S_{i}=\hat{U}_{i}^{\top}B_{i-1}\hat{V}_{i}=\begin{pmatrix}\sigma_i&0\\0&B_{i}\end{pmatrix}$. Let $U_{i}=\begin{pmatrix}I & 0 \\ 0 & \hat{U}_{i}\end{pmatrix}$ and $V_{i}=\begin{pmatrix}I & 0 \\ 0 & \hat{V}_{i}\end{pmatrix}$. Then, $S_{i}=U_{i}^{\top}S_{i-1}V_{i}$. Therefore, $S_{i}=U_{p}^{\top}\cdots U_{1}^{\top}AV_{1}V_{p}$. Finally, $S_{p}$ is in the form same to $\Sigma$ and we get $A=U\Sigma V$, where $U=U_{1}\cdots U_{p}$ and $V=V_{p}\cdots V_{1}$.
`\end{proof}`

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. $\mathrm{rank}(A)=r$, where $r$ is the number of nonzero singular values of $A$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. $A=U\Sigma V^\top$ and $\mathrm{rank}(A)=r$. $\mathrm{range}(A)=\text{span}(u_1,\dots,u_r)$ and $\mathrm{null}(A)=\text{span}(v_{r+1},\dots,v_k)$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. $A=U\Sigma V^\top$ and $\mathrm{rank}(A)=r$. $\|A\|=\sigma_1$ and $\|A\|_F=\sqrt{\sigma_1^2+\sigma_2^2+\cdots+\sigma_r^2}$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,k}$. The square of singular values of $A$ are the eigenvalues of $A^\top A$ and $AA^\top$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,n}$. If $A=A^\top$, the singular values of $A$ are the absolute values of the eigenvalues of $A$.

> [!proposition|]
> Let $A\in\mathbb{R}^{n,n}$. $|\det(A)|=\prod_{i=1}^{n}\sigma_i$.

> [!Theorem|]
> Let $A\in\mathbb{R}^{n,k}$ and $j\in{1,2,\dots,k}$. The $j$-th singular value satisfies $\sigma_j(A)=\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}$, where $V_j$ varies over all subspaces of $\mathbb{R}^k$ with dimension $j$.
Let $A\in\mathbb{R}^{n,k}$, and let $v_1,\dots,v_k$ be right singular vectors of $A$ corresponding to singular values $\sigma_1(A)\ge \cdots \ge \sigma_k(A)\ge 0$. We prove $\sigma_j(A)=\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}$.

^e30396

`\begin{proof}`
First, we show that $\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\ge \sigma_j(A)$. Take $V_j^*=\operatorname{span}\{v_1,\dots,v_j\}$. For any $x\in V_j^*$, $x=\sum_{i=1}^j \alpha_i v_i$. Then $\|x\|^2=\sum_{i=1}^j |\alpha_i|^2$ and $\|Ax\|^2=\sum_{i=1}^j \sigma_i(A)^2 |\alpha_i|^2$. Since $\sigma_i(A)\ge \sigma_j(A)$ for all $1\le i\le j$, we have $\|Ax\|^2\ge \sigma_j(A)^2\sum_{i=1}^j |\alpha_i|^2=\sigma_j(A)^2\|x\|^2$. Hence for every nonzero $x\in V_j^*$, $\frac{\|Ax\|}{\|x\|}\ge \sigma_j(A)$. Therefore $\underset{x\in V_j^*,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\ge \sigma_j(A)$, so $\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\ge \sigma_j(A)$. On the other hand, taking $x=v_j$, we get $\frac{\|Av_j\|}{\|v_j\|}=\sigma_j(A)$, so $\underset{x\in V_j^*,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}= \sigma_j(A)$. 
Next, we show that $\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\le \sigma_j(A)$. Let $V_j\subset\mathbb{R}^k$ be any $j$-dimensional subspace, and set $W=\operatorname{span}\{v_j,\dots,v_k\}$. Then $\dim W=k-j+1$. By the dimension formula, $\dim(V_j\cap W)\ge \dim V_j+\dim W-k=j+(k-j+1)-k=1$. Hence there exists a nonzero vector $x\in V_j\cap W$. Since $x\in W$, write $x=\sum_{i=j}^k \alpha_i v_i$. Then $\|x\|^2=\sum_{i=j}^k |\alpha_i|^2$ and $\|Ax\|^2=\sum_{i=j}^k \sigma_i(A)^2 |\alpha_i|^2$. Since $\sigma_i(A)\le \sigma_j(A)$ for all $i\ge j$, we obtain $\|Ax\|^2\le \sigma_j(A)^2\sum_{i=j}^k |\alpha_i|^2=\sigma_j(A)^2\|x\|^2$. Thus $\frac{\|Ax\|}{\|x\|}\le \sigma_j(A)$. Because $x\in V_j$, it follows that $\underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\le \sigma_j(A)$. Since $V_j$ was arbitrary, $\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}\le \sigma_j(A)$. 
Combining the two inequalities gives $\sigma_j(A)=\underset{V_j}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}$.
`\end{proof}`

> [!Theorem|]
> Let $A\in\mathbb{R}^{n,k}$ and $j\in{1,2,\dots,k}$. The $j$-th singular value satisfies $\sigma_j(A)=\underset{V_{k-j+1}}{\min}\ \underset{x\in V_{k-j+1},\ x\ne 0}{\max}\frac{\|Ax\|}{\|x\|}$, where $V_{k-j+1}$ varies over all subspaces of $\mathbb{R}^k$ with dimension $k-j+1$.

^7b1b5c

> [!Theorem|]
> Let $A\in\mathbb{R}^{n,k}$ and $\hat A \in \mathbb{R}^{n,k'}$ be obtained by removing $k-k'$ columns of $A$. The singular values of $A$ and $\hat A$ satisfy the inequalities $\sigma_{j}\ge \hat\sigma_{j}\ge \sigma_{j+k-k'}$ for $j=1,\cdots ,k'$.

`\begin{proof}`
Let $H\subset \mathbb{R}^k$ be the coordinate subspace corresponding to the remaining $k'$ columns, so that $\dim H=k'$, and $\hat A$ is exactly the restriction of $A$ to $H$. Hence, for every subspace $V\subset \mathbb{R}^{k'}$, identifying $V$ with a subspace of $H$, the quotient $\frac{\|\hat A x\|}{\|x\|}$ agrees with $\frac{\|A x\|}{\|x\|}$. By [[#^e30396]], $\hat\sigma_j=\underset{V_j\subset H}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|} \geq \underset{V_j\subset \mathbb{R}^k}{\max}\ \underset{x\in V_j,\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}=\sigma_j$. By [[#^7b1b5c]], $\hat\sigma_j=\underset{W_{k'-j+1}\subset H}{\min}\ \underset{x\in W_{k'-j+1},\ x\ne 0}{\max}\frac{\|Ax\|}{\|x\|} \geq \underset{W_{k'-j+1}\subset \mathbb{R}^k}{\min}\ \underset{x\in W_{k'-j+1},\ x\ne 0}{\max}\frac{\|Ax\|}{\|x\|}=\sigma_{j+k-k'}$.
`\end{proof}`

> [!Theorem|]
> Let $A,E\in\mathbb{R}^{n,k}$ and $j\in{1,2,\dots,k}$. $E$ is a perturbation of $A$. The singular values satisfy $\sigma_j(A)-\|E\|\le \sigma_j(A+E)\le \sigma_j(A)+\|E\|$.

`\begin{proof}`
By [[#^e30396]], $\sigma_j(A+E)=\underset{V_{k-j+1}}{\min}\ \underset{x\in V_{k-j+1},\ x\ne 0}{\max}\frac{\|(A+E)x\|}{\|x\|} \le \underset{V_{k-j+1}}{\min}\ \underset{x\in V_{k-j+1},\ x\ne 0}{\max}\frac{\|Ax\|}{\|x\|}+\|E\|=\sigma_j(A)+\|E\|$. And by [[#^7b1b5c]], $\sigma_j(A+E)=\underset{V_{k-j+1}}{\max}\ \underset{x\in V_{k-j+1},\ x\ne 0}{\min}\frac{\|(A+E)x\|}{\|x\|} \ge \underset{V_{k-j+1}}{\max}\ \underset{x\in V_{k-j+1},\ x\ne 0}{\min}\frac{\|Ax\|}{\|x\|}-\|E\|=\sigma_j(A)-\|E\|$.
`\end{proof}`

> [!Theorem|] Eckart–Young Theorem
> Let $A\in\mathbb{R}^{n,k}$, $r=\operatorname{rank}(A)$, and $\nu\in{0,1,\dots,r}$. Assume $A=\sum_{j=1}^{r}\sigma_j u_j v_j^\top$ with $\sigma_1\ge\cdots\ge\sigma_r>0$, $A_\nu=\sum_{j=1}^{\nu}\sigma_j u_j v_j^\top$, and $\sigma_{r+1}=0$. The matrix $A_\nu$ satisfies $\|A-A_\nu\|=\underset{\operatorname{rank}(B)\le \nu}{\inf}\|A-B\|=\sigma_{\nu+1}$. It also satisfies $\|A-A_\nu\|_F=\underset{\operatorname{rank}(B)\le \nu}{\inf}\|A-B\|_F=\sqrt{\sigma_{\nu+1}^2+\cdots+\sigma_r^2}$.

> [!Theorem|]
> Let $A\in\mathbb{R}^{n,k}$ and $\tilde\sigma_1,\dots,\tilde\sigma_{k}$ be the computed singular values of $A$ in an idealized floating point system. There exists $\Delta A\in\mathbb{R}^{n,k}$ such that $\tilde\sigma_1,\dots,\tilde\sigma_{k}$ are the singular values of $A+\Delta A$ and $\|\Delta A\|_2\le cn^\alpha \epsilon \|A\|_2$.

## Computing the SVD

> [!definition|] Bidiagonal Matrix
> Let $B \in \mathbb{R}^{n, k}$. The matrix $B$ is a bidiagonal matrix if $b_{ij} = 0$ for all $(i, j)$ with $j \neq i$ and $j \neq i + 1$.

> [!theorem|] Golub-Kahan Bidiagonalization
> Let $A \in \mathbb{R}^{n, k}$. There exist unitary matrices $U \in \mathbb{R}^{n, n}$ and $V \in \mathbb{R}^{k, k}$ s.t. $U^{\top}AV = B$, where $B$ is upper-bidiagonal.

> [!theorem|]
> The operation count of Golub-Kahan bidiagonalization is $\sim 4nk^{2} - \frac{4}{3}k^{3}$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, k}$. A backward stable algorithm for computing singular values produces computed values $\tilde{\sigma}_k$ satisfying $\tilde{\sigma}_k = \sigma_k(A + \delta A)$, $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$ for some $\delta A \in \mathbb{R}^{n, k}$. This implies $\frac{|\tilde{\sigma}_k - \sigma_k|}{\|A\|} = O(\epsilon_{\text{machine}})$.
