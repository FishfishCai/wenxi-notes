#NumericalLinearAlgebra 
Prerequisite knowledge: [[Computation]], [[Matrix Operator]], [[QR Factorization]], [[Stability]]
## Least Square
> [!Theorem|] Least Square
> Let $A\in\mathbb{R}^{n, k}$, $b\in \mathbb{R}^{n}$ and $x\in\mathbb{R}^{k}$. $x$ minimizes  $\|b-Ax\|$ iff $A^{\top}Ax=A^{\top}b$.

^d827c8

`\begin{proof}`
Let $P$ be the projection matrix onto $\mathrm{range}(A)$. $\|b-b'\|^{2}=\|b-Pb\|^{2}+\|Pb-b'\|^{2}\geq\|b-Pb\|^{2}$, implying $b'$ minimizes $\|b-b'\|$ iff $b'=Pb$. Since $Ax\in \mathrm{range}(A)$, $x$ minimizes $\|b-Ax\|$ iff $Ax=b'$. $Ax=b'$ is equivalent to $A^{\top}(b-Ax)=0$.
`\end{proof}`

> [!remark|]
> For [[#^d827c8]], if $A$ is full-rank, $x=A^{+}b$.

> [!theorem|] Least Square via Normal Equations
> The solution $x$ of [[#^d827c8]] can be solved in the following way:
> - Form $A^{\top} A$ and $A^{\top} b$.
> - Compute the Cholesky factorization $A^{\top} A = R^{\top} R$.
> - Solve $R^{\top} w = A^{\top} b$ for $w$.
> - Solve $R x = w$ for $x$.

^9dd356

> [!proposition|]
> Since the computation of $A^{\top}A$ is $nk^{2}$ and the computation of Cholesky factorization is $\frac{1}{3}k^{3}$, the computation of [[#^9dd356]] is $~nk^{2}+\frac{1}{3}k^{3}$. 

> [!theorem|] Least Square via QR Factorization
> The solution $x$ of [[#^d827c8]] can be solved in the following way:
> - Compute the reduced QR factorization $A=\hat{Q}\hat{R}$.
> - Compute the vector $\hat{Q}^{*}b$.
> - Solve the upper-triangular system $\hat{R}x=\hat{Q}^{*}b$ for $x$.

^c1790f

> [!proposition|]
> The computation of [[#^c1790f]] is $~2nk^{2}-\frac{2}{3}k^{3}$. 

> [!theorem|] Least Square via SVD
> The solution $x$ of [[#^d827c8]] can be solved in the following way:
> - Compute the reduced SVD $A=\hat U \hat\Sigma V^*$.
> - Compute the vector $\hat U^* b$.
> - Solve the diagonal system $\hat\Sigma w=\hat U^* b$ for $w$.
> - Set $x=Vw$.

^70060a

> [!proposition|]
> The computation of [[#^70060a]] is $~2nk^{2}+11k^{3}$. 

> [!theorem|]
> [[#^c1790f]] is backward stable.

`\begin{proof}`
$b=(\tilde Q+\delta Q)(\tilde R+\delta R)\tilde x=\bigl[\tilde Q\tilde R+(\delta Q)\tilde R+\tilde Q(\delta R)+(\delta Q)(\delta R)\bigr]\tilde x.$ By [[QR Factorization#^cd77ab]], $b=\bigl[A+\delta A+(\delta Q)\tilde R+\tilde Q(\delta R)+(\delta Q)(\delta R)\bigr]\tilde x.$ Since $\tilde Q\tilde R=A+\delta A$ and $\tilde Q$ is unitary, we have $\frac{\|\tilde R\|}{\|A\|}\le \|\tilde Q^{*}\|\frac{\|A+\delta A\|}{\|A\|}=O(1)$ as $\epsilon_{\text{machine}}\to 0$. This gives us $\frac{\|(\delta Q)\tilde R\|}{\|A\|}\le \|\delta Q\|\frac{\|\tilde R\|}{\|A\|}=O(\epsilon_{\text{machine}})$ and $\frac{\|\tilde Q(\delta R)\|}{\|A\|}\le \|\tilde Q\|\frac{\|\delta R\|}{\|\tilde R\|}\frac{\|\tilde R\|}{\|A\|}=O(\epsilon_{\text{machine}})$. Finally, $\frac{\|(\delta Q)(\delta R)\|}{\|A\|}\le \|\delta Q\|\frac{\|\delta R\|}{\|A\|}=O(\epsilon_{\text{machine}}^{2}).$ The total perturbation $\Delta A$ thus satisfies $\frac{\|\Delta A\|}{\|A\|}\le \frac{\|\delta A\|}{\|A\|}+\frac{\|(\delta Q)\tilde R\|}{\|A\|}+\frac{\|\tilde Q(\delta R)\|}{\|A\|}+\frac{\|(\delta Q)(\delta R)\|}{\|A\|}=O(\epsilon_{\text{machine}})$.
`\end{proof}`

> [!Theorem|]
> Let $A, \Delta A \in\mathbb{R}^{n,n}$, $b\in\mathbb{R}^n$ and $x, y, b\in\mathbb{R}^n$. If $x$ minimizes $\|b-Ax\|$, $y$ minimizes $\|b+\Delta b-(A+\Delta A)y\|$, $\|\Delta A\|<\varepsilon\|A\|$, and $\|\Delta b\|<\varepsilon\|b\|$, $\frac{\|y-x\|}{\|x\|}\le \frac{2\varepsilon\kappa(A)}{1-\varepsilon\kappa(A)}+\frac{\varepsilon\kappa(A)(\kappa(A)+1)}{1-\varepsilon\kappa(A)}\frac{\|b-Ax\|}{\|A\|\|x\|}$.
