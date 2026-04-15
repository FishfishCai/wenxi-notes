---
tags:
---
#NumericalLinearAlgebra 
Prerequisite knowledge: [[Computation]], [[Matrix]], [[Matrix Operator]], [[Stability]]
## Gram–Schmidt QR Factorization
> [!theorem|] Classical Gram–Schmidt Process
> Let $a_{1}, a_{2}, ..., a_{k} \in \mathbb{R}^{n}$. If  $a_{1}, a_{2}, ..., a_{k}$ are independent, we can construct an orthonormal set $v_{1}, v_{2}, ..., v_{k}$, where 
> $$
> \begin{align*}
> v_1 &= \frac{a_1}{\|a_1\|},\\
> v_i &=
> \frac{\bigl(I - v_1 v_1^T - \cdots - v_{i-1} v_{i-1}^T\bigr)a_i}
> {\left\|\bigl(I - v_1 v_1^T - \cdots - v_{i-1} v_{i-1}^T\bigr)a_i\right\|},
> \qquad i=2,\dots,k.
> \end{align*}
> $$

> [!theorem|] Gram–Schmidt QR Factorization
> Let $A = [a_1\; a_2\; \cdots\; a_k] \in \mathbb{R}^{n, k}$, where $a_i$ denotes the $i$-th column of $A$. If $v_1, v_2, \dots, v_k$ is the orthonormal set constructed from $a_{1}, a_{2}, ..., a_{k}$ via the classical Gram–Schmidt process. We have
> $$
> \begin{aligned}
> a_1 &= \|a_1\|\, v_1,\\
> a_i &= \sum_{j=1}^{i-1} \langle a_i, v_j\rangle\, v_j + \left\|\bigl(I - v_1 v_1^T - \cdots - v_{i-1} v_{i-1}^T\bigr)a_i\right\| v_i, \qquad i=2,\dots,k.
> \end{aligned}
> $$
> That is, 
> $$
> A = QR
> := [v_1\; v_2\; \cdots\; v_k]
> \begin{pmatrix} \\
> \|a_1\| & \langle a_2, v_1\rangle & \cdots & \langle a_k, v_1\rangle \\
> 0 & \left\|\bigl(I - v_1 v_1^T\bigr)a_2\right\| & \cdots & \langle a_k, v_2\rangle \\
> \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & \left\|\bigl(I - v_1 v_1^T - \cdots - v_{k-1} v_{k-1}^T\bigr)a_k\right\| \\ \\
> \end{pmatrix}.
> $$

^4b5424

> [!remark|]
> For [[#^4b5424]], it can also be formed as $AR_{1}R_{2}\cdots R_{k} = Q$, where $$ 
> R_i=\begin{pmatrix} 
> 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\
> 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\
> \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\
> 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\
> 0 & 0 & \cdots & 0 & \dfrac{1}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} & -\dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{i+1}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|^{2}} & \cdots & -\dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{k}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|^{2}} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\
> \vdots & \vdots &  & \vdots & \vdots &  & \ddots
> \end{pmatrix}.
> $$and $v_{j}$ is the $j$-th column of $AR_{1}R_{2}\cdots R_{i-1}$ for $j<i$. Then, 
> $$
> R_{i}^{-1}= \begin{pmatrix} 
> 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\
> 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\
> \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\
> 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\
> 0 & 0 & \cdots & 0 & \left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\| & \dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{i+1}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} & \cdots & \dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{k}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\
> \vdots & \vdots &  & \vdots & \vdots &  & \ddots
> \end{pmatrix}.
> $$
> and thus $R=R_{k}^{-1}R_{k-1}^{-1}\cdots R_{1}^{-1}$ is an upper triangular matrix.

> [!theorem|] Modified Gram–Schmidt Process
> Let $a_{1}, a_{2}, ..., a_{k} \in \mathbb{R}^{n}$. If  $a_{1}, a_{2}, ..., a_{k}$ are independent, we can construct an orthonormal set $v_{1}, v_{2}, ..., v_{k}$, where 
> $$
> \begin{align*}
> v_1 &= \frac{a_1}{\|a_1\|},\\
> v_i &=
> \frac{\bigl( I - v_1 v_1^T\bigr) \bigl( I-v_{2}v_{2}^{\top}\bigr)\cdots \bigl( I-v_{i-1}v_{i-1}^{\top}\bigr)a_i}
> {\|\bigl( I - v_1 v_1^T\bigr) \bigl( I-v_{2}v_{2}^{\top}\bigr) \cdots \bigl( I-v_{i-1}v_{i-1}^{\top}\bigr)a_i\|},
> \qquad i=2,\dots,k.
> \end{align*}
> $$

^c68556

> [!theorem|]
> The operation count of [[#^c68556]] is $\sum_{j=1}^{k}(4n-1)(j-1)\sim2nk^{2}$.

## Householder QR Factorization
>[!theorem|] Householder QR Factorization
> Let $A=[a_1,a_2,\cdots,a_k]\in\mathbb{R}^{n,k}$. The matrix $R:=A_{k}$ is upper triangular, $Q:=H_1H_2\cdots H_k$ is orthogonal and $A=QR$ if we set $A = A_{0}$ and at the $i$-th step, we compute in the following order:
> $$
> \begin{align*}
> \hat{a}_{i}&={A_{i}}_{i:n,i}\in\mathbb{R}^{n-i+1}\\
> e_i&=(1,0,\dots,0)^\top\in\mathbb{R}^{n-i+1}\\
> b_{i}&=-\mathrm{sign}((a_i)_1)|a_i|e_i\in\mathbb{R}^{n-i+1}\\
> v_{i}&=\frac{a_i-b_{i}}{|a_i-b_{i}|}\in\mathbb{R}^{n-i+1}\\
> \hat H_i&=I-2v_{i}v_{i}^\top\in\mathbb{R}^{n-i+1,n-i+1}\\
> H_{i} &= \begin{bmatrix} I_{i-1} & 0 \\ 0 & \hat H_{i} \end{bmatrix}\in\mathbb{R}^{n,n}\\
> A_{i}&=H_iA_{i-1}
> \end{align*}
> $$

^857b04

> [!theorem|]
> The operation count of [[#^857b04]] is $\sum_{j=1}^{k}4(n-j-1)(k-j+1)\sim 2nk^{2}-\frac{2}{3}k^{3}$.

> [!theorem|]
> [[#^857b04]] is backward stable.

^cd77ab

## Gaussian Eliminiation
> [!theorem|] Gaussian Eliminiation
> Let $A=\left(\begin{matrix} a_{11} & a_{12} & \cdots & a_{1k} \\ a_{21} & a_{22} & \cdots & a_{2k} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nk} \end{matrix}\right)\in\mathbb{R}^{n,k}$. Assume $a_{ii}\neq 0$ for $i = 1,\cdots ,k$. The matrix $L:=L_kL_{k-1}\cdots L_2L_1$ is an lower triangular matrix, $U$ is an upper triangular matri and $A=LU$ if we set $A=A_{0}$ and, at the $i$-th iteration, we compute in the following order:
> $$
> \begin{align*}
> l_{ji}&=\frac{a_{ji}}{a_{ii}} \text{ for }i<j\leqslant n\\
> L_{i}&= \left(\begin{matrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & -\ell_{i+1,i} & 1 & \cdots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & -\ell_{ni} & 0 & \cdots & 1 \end{matrix}\right)\\
> A_{i}&=L_{i}A_{i-1}
> \end{align*}
> $$

^4aa81b

> [!remark|]
> For [[#^4aa81b]], $L_{i}^{-1}=\left(\begin{matrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & \ell_{i+1,i} & 1 & \cdots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \ell_{ni} & 0 & \cdots & 1 \end{matrix}\right)$ and $L=\left(\begin{matrix} 1 & 0 & 0 & \cdots & 0 \\ \ell_{21} & 1 & 0 & \cdots & 0 \\ \ell_{31} & \ell_{32} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ \ell_{k1} & \ell_{k2} & \cdots & \ell_{k,k-1} & 1 \end{matrix}\right)$.

> [!theorem|]
> The operation count of [[#^4aa81b]] is $\sim \frac{2}{3}n^{3}$.

## Pivoting

> [!definition|] Permutation Matrix
> Let $P \in \mathbb{R}^{n, n}$. The matrix $P$ is a permutation matrix if it is obtained from the identity by permuting rows or columns.

> [!theorem|] LU Factorization with Partial Pivoting
> Let $A \in \mathbb{C}^{n, n}$. There exist a permutation matrix $P \in \mathbb{R}^{n, n}$, a unit lower-triangular matrix $L \in \mathbb{C}^{n, n}$ with $|\ell_{ij}| \le 1$, and an upper-triangular matrix $U \in \mathbb{C}^{n, n}$ s.t. $PA = LU$.

^b1e2f7

> [!theorem|]
> The operation count of [[#^b1e2f7]] is $\sim \frac{2}{3}n^{3}$.

## Stability of Gaussian Elimination

> [!definition|] Growth Factor
> Let $A \in \mathbb{C}^{n, n}$, and $U \in \mathbb{C}^{n, n}$ be the upper-triangular matrix obtained from Gaussian elimination of $A$. The growth factor for $A$ is $\rho = \frac{\underset{i,j}{\max} |u_{ij}|}{\underset{i,j}{\max} |a_{ij}|}$.

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$ be a nonsingular matrix. Assume the factorization $A = LU$ is computed by Gaussian elimination without pivoting on a computer satisfying the axioms of floating point arithmetic. If $A$ has an LU factorization and the factorization completes successfully in floating point arithmetic, the computed matrices $\tilde{L}$ and $\tilde{U}$ satisfy $\tilde{L}\tilde{U} = A + \delta A$, $\frac{\|\delta A\|}{\|L\|\|U\|} = O(\epsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$.

^a3e1b2

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$. Assume the factorization $PA = LU$ is computed by Gaussian elimination with partial pivoting on a computer satisfying the axioms of floating point arithmetic. The computed matrices $\tilde{P}$, $\tilde{L}$, and $\tilde{U}$ satisfy $\tilde{L}\tilde{U} = \tilde{P}A + \delta A$, $\frac{\|\delta A\|}{\|A\|} = O(\rho \epsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$, where $\rho$ is the growth factor for $A$. If $|\ell_{ij}| < 1$ for each $i > j$, implying that there are no ties in the selection of pivots in exact arithmetic, $\tilde{P} = P$ for all sufficiently small $\epsilon_{\text{machine}}$.

^c92d4a

> [!proposition|]
> Let $A \in \mathbb{C}^{n, n}$. For Gaussian elimination with partial pivoting applied to $A$, the growth factor satisfies $\rho \le 2^{n-1}$.

> [!theorem|]
> Gaussian elimination with partial pivoting is backward stable.

> [!remark|]
> For the above, backward stability holds in the sense that for each fixed dimension $n$, the bound $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$ applies uniformly to all matrices of that dimension, but the constant involves $2^{n-1}$. In practice, large growth factors are exponentially rare among random matrices, and Gaussian elimination with partial pivoting is utterly stable in practice.

## Cholesky Factorization

> [!proposition|]
> Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian positive definite, the eigenvalues of $A$ are positive real numbers.

> [!proposition|]
> Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian positive definite, any principal submatrix of $A$ is Hermitian positive definite. In particular, every diagonal entry of $A$ is a positive real number.

> [!theorem|] Cholesky Factorization
> Let $A \in \mathbb{C}^{n, n}$. If $A$ is Hermitian positive definite, $A$ has a unique Cholesky factorization $A = R^{*}R$, where $R \in \mathbb{C}^{n, n}$ is upper-triangular with positive diagonal entries and $r_{jj} > 0$.

`\begin{proof}`
Existence: Write $A = \begin{pmatrix} a_{11} & w^{*} \\ w & K \end{pmatrix}$ with $a_{11} > 0$. Set $\alpha = \sqrt{a_{11}}$. Then $A = R_1^{*}A_1R_1$ where $R_1 = \begin{pmatrix} \alpha & w^{*}/\alpha \\ 0 & I \end{pmatrix}$ and $A_1 = \begin{pmatrix} 1 & 0 \\ 0 & K - ww^{*}/a_{11} \end{pmatrix}$. The submatrix $K - ww^{*}/a_{11}$ is positive definite since it is an $(n-1) \times (n-1)$ principal submatrix of $R_1^{-*}AR_1^{-1}$. By induction, all submatrices $A_j$ that appear are positive definite, so the process cannot break down, giving $A = R^{*}R$.
Uniqueness: At each step, $\alpha = \sqrt{a_{11}}$ is uniquely determined, which determines the first row of $R_1$. By induction, the factorization of each $A_j$ is unique, so $R$ is unique.
`\end{proof}`

^f84c21

> [!theorem|]
> The operation count of [[#^f84c21]] is $\sim \frac{1}{3}n^{3}$.

> [!theorem|]
> [[#^f84c21]] is backward stable.

