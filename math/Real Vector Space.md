#LinearAlgebra 
Prerequisite knowledge: [[Structure]]
## Real Vector Space
> [!definition|] Inner Product in $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The inner product in $\mathbb{R}^{n}$ is $\langle a, b \rangle := a^\top b = \sum_{i=1}^n a_i b_i$.

> [!definition|] $l_{p}$-norm in  $\mathbb{R}^{n}$
> Let $a\in \mathbb{R}^n$. The $l_{p}$-norm in  $\mathbb{R}^{n}$ is  $\|a\|_{p}:=\left(\sum_{i=1}^{n}|a_{i}|^{p}\right)^{\frac{1}{p}}$ for $1\leqslant p < \infty$ and $\max_{1 \leqslant i\leqslant n}|a_{i}|$ for $p=\infty$. 

> [!definition|] Outer Product in  $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The outer product  in  $\mathbb{R}^{n}$ is $ab^\top$.

> [!proposition|]
> Let $a,b\in\mathbb{R}^n$. $\|a+b\|^2=\|a\|^2+\|b\|^2$ iff $\langle a, b \rangle =0$.

> [!proposition|]
>  Let $a,b\in\mathbb{R}^n$. If $\|a\|=\|b\|$,  $\langle a+b, a-b\rangle = 0$.

^9fece5

> [!proposition|]
> Let $a,b\in\mathbb{R}^n$. If $a\neq0$, then there exist $\beta\in\mathbb{R}$ and $\delta\in\mathbb{R}^n$ such that $b=\beta a+\delta$ and $a^\top\delta=0$, where $\beta=\frac{a^\top b}{a^\top a}$ and $\delta=b-\beta a$.

> [!thm|] Cauchy-Schwarz Inequality
> Let $a,b\in\mathbb{R}^n$. $|a^\top b|\le\|a\|\|b\|$. Equality holds iff. there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$, or $a=0$, or $b=0$.

`\begin{proof}`
If $a=0$ or $b=0$, $|a^\top b|=0=\|a\|\|b\|$. Assume $a\ne0$ and write $b=\beta a+\delta$ with $a^\top\delta=0$. Then,  $(a^\top b)^2=(a^\top(\beta a+\delta))^2=(\beta\|a\|^2)^2\le  \|a\|^{2}(\beta^2\|a\|^2+\|\delta\|^2) = \|a\|^{2}\|\beta a+\delta\|^2= \|a\|^2\|b\|^2$,
and thus $|a^\top b|\le\|a\|\|b\|$. Equality holds iff $\|\delta\|=0$, i.e., there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$.
`\end{proof}`

> [!definition| 5] $\cos \theta$
> Let $a,b\in\mathbb{R}^n$. $\cos \theta := \frac{a^{\top}b}{\|a\|\|b\|}$.

> [!remark|]
> Cauchy-Schwarz inequality ensures that $\|\cos \theta\| < 1$. 
