#LinearAlgebra 
Prerequisite knowledge: [[Structure]]
## Real Vector
> [!definition|] Inner Product in $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The inner product in $\mathbb{R}^{n}$ is $\langle a, b \rangle := a^\top b = \sum_{i=1}^n a_i b_i$.

> [!definition|] Norm in  $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The norm in  $\mathbb{R}^{n}$ is  $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^\top a}$.

> [!definition|] Outer Product in  $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The outer product  in  $\mathbb{R}^{n}$ is $ab^\top$.

> [!lemma|]
> Let $a,b\in\mathbb{R}^n$. $\|a+b\|^2=\|a\|^2+\|b\|^2$ iff. $\langle a, b \rangle =0$.

> [!lemma|]
>  Let $a,b\in\mathbb{R}^n$. If $\|a\|=\|b\|$, then $\langle a+b, a-b\rangle = 0$.

^9fece5

> [!lemma|]
> Let $a,b\in\mathbb{R}^n$. If $a\neq0$, then there exist $\beta\in\mathbb{R}$ and $\delta\in\mathbb{R}^n$ such that $b=\beta a+\delta$ and $a^\top\delta=0$, with $\beta=\frac{a^\top b}{a^\top a}$ and $\delta=b-\beta a$.

> [!thm|] Cauchy-Schwarz Inequality
> Let $a,b\in\mathbb{R}^n$. $|a^\top b|\le\|a\|\|b\|$. Equality holds iff. there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$, or $a=0$, or $b=0$.

`\begin{proof}`
If $a=0$ or $b=0$, then $|a^\top b|=0=\|a\|\|b\|$. Assume $a\ne0$ and write $b=\beta a+\delta$ with $a^\top\delta=0$. Then,  $(a^\top b)^2=(a^\top(\beta a+\delta))^2=(\beta\|a\|^2)^2\le  \|a\|^{2}(\beta^2\|a\|^2+\|\delta\|^2) = \|a\|^{2}\|\beta a+\delta\|^2= \|a\|^2\|b\|^2$,
and thus $|a^\top b|\le\|a\|\|b\|$. Equality holds iff. $\|\delta\|=0$, i.e., there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$.
`\end{proof}`

> [!definition| 5] $\cos \theta$
> Let $a,b\in\mathbb{R}^n$. $\cos \theta := \frac{a^{\top}b}{\|a\|\|b\|}$.

> [!remark|]
> Cauchy-Schwarz inequality ensures that $\|\cos \theta\| < 1$. 
