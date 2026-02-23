#NumericalLinearAlgebra 
Prerequisite knowledge: [[Computation]], [[Matrix Operator]], [[QR Factorization]]
## Least Square
> [!Theorem|] 
> Let $A\in\mathbb{R}^{n\times k}$, $b\in \mathbb{R}^{n}$ and $x\in\mathbb{R}^{k}$. $x$ minimizes  $\|b-Ax\|$ iff $A^{\top}Ax=A^{\top}b$.

^d827c8

`\begin{proof}`
Let $P$ be the projection matrix onto $\mathrm{range}(A)$. $\|b-b'\|^{2}=\|b-Pb\|^{2}+\|Pb-b'\|^{2}\geq\|b-Pb\|^{2}$, implying $b'$ minimizes $\|b-b'\|$ iff $b=Pb$. Since $Ax\in \mathrm{range}(A)$, $x$ minimizes $\|b-Ax\|$ iff $Ax=b'$. $Ax=b'$ is equivalent to $A^{\top}(b-Ax)=0$.
`\end{proof}`
> [!remark|]
> In [[#^d827c8]], if $A$ is full-rank, $x=A^{+}b$.

> [!theorem|] Least Square via Normal Equations
> - Form $A^{\top} A$ and $A^{\top} b$.
> - Compute the Cholesky factorization $A^{\top} A = R^{\top} R$.
> - Solve $R^{\top} w = A^{\top} b$ for $w$.
> - Solve $R x = w$ for $x$.

^9dd356

> [!remark|]
> Since the computation of $A^{\top}A$ is $nk^{2}$ and the computation of Cholesky factorization is $\frac{1}{3}k^{3}$, the computation of [[#^9dd356]] is $~nk^{2}+\frac{1}{3}k^{3}$. 

> [!theorem|] Least Square via QR Factorization

> [!theorem|] Least Square via SVD

