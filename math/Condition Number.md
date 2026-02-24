#NumericalLinearAlgebra 
Prerequisite knowledge: [[Structure]], [[Matrix Operator]]
## Condition Number
> [!definition|] Condition Number
> Let $X$ and $Y$ be normed vector space and $f:X\to Y$.  $f$ is continuous. The condition number of $f$ at $x$ is $\hat\kappa(x):=\underset{\delta\to0}{\lim}\underset{\|\delta x\|\leqslant\delta}{\sup}\frac{\|\delta f\|}{\|\delta x\|}$.

^ead79c

> [!remark|]
> For [[#^ead79c]], if $f$ is differentiable, $\hat\kappa = \|J(x)\|$.

> [!definition|] Relative Condition Number
> Let $X$ and $Y$ be normed vector space and $f:X\to Y$.  $f$ is continuous. The relative condition number of $f$ at $x$ is $\kappa(x):=\underset{\delta\to0}{\lim}\underset{\|\delta x\|\leqslant\delta}{\sup}\frac{\frac{\|\delta f\|}{\|f(x)\|}}{\frac{\|\delta x\|}{\|x\|}}$.

^887783

> [!remark|]
> For [[#^887783]], if $f$ is differentiable, $\kappa = \frac{\|J(x)\|\|x\|}{\|f(x)\|}$.

> [!Theorem|]
> Let $A \in \mathbb{R}^{n,n}$ and $x,b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $A$, the  condition number of computing $b$ with $Ax=b$ is $\kappa(x)=\|A\|\frac{\|x\|}{\|b\|}\le \|A\|\|A^{-1}\|$. If $\|\cdot\|=\|\cdot\|_2$, the equality holds if $x$ is a multiple of a right singular vector of $A$ corresponding to the minimal singular value $\sigma_n$

> [!theorem|]
> Let $A \in \mathbb{R}^{n,n}$ and $x,b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $A$, the  condition number of computing $x$ with $Ax=b$ is $\kappa(b)=\|A^{-1}\|\frac{\|b\|}{\|x\|}\le \|A\|\|A^{-1}\|$. If $\|\cdot\|=\|\cdot\|_2$, the equality holds if $b$ is a multiple of a left singular vector of $A$ corresponding to the maximal singular value $\sigma_1$.

> [!definition|] Condition Number of Matrix
> Let $A\in \mathbb{R}^{n,k}$. $A$ is full-rank. The condition number of $A$ is $\kappa(A):=\|A\|\|A^{+}\|$.

> [!remark|]
> If $\kappa(A)$ is small, $A$ is said to be well-conditioned. If $\kappa(A)$ is large, $A$ is said to be ill-conditioned. If $\|\cdot\| = \|\cdot\|_{2}$, $\kappa(A)=\frac{\sigma_{1}}{\sigma_{n}}$, where $\sigma_{1}$ is the maximal eigenvalue of $A$ and $\sigma_{n}$ is the minimal eigenvalue of $A$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n,n}$ and $x,b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $b$, the  condition number of computing $x$ with $x=A^{-1}b$ is $\kappa(A)=\|A\|\|A^{-1}\|$. 
