## Real Vector Space
::: definition:$l_{p}$-norm in $\mathbb{R}^{n}$
Let $a\in \mathbb{R}^n$. The $l_{p}$-norm in $\mathbb{R}^{n}$ is $\|a\|_{p}:=\left(\sum_{i=1}^{n}|a_{i}|^{p}\right)^{\frac{1}{p}}$ for $1\leqslant p<\infty$, and $\|a\|_{\infty}:=\underset{1\leqslant i\leqslant n}{\max}|a_i|$.
:::

::: definition:Standard Inner Product in $\mathbb{R}^{n}$
Let $a,b \in \mathbb{R}^n$. The standard inner product in $\mathbb{R}^{n}$ is $\langle a, b \rangle := a^T b = \sum_{i=1}^n a_i b_i$.
:::

::: definition:Outer Product in $\mathbb{R}^{n}$
Let $a,b \in \mathbb{R}^n$. The outer product in $\mathbb{R}^{n}$ is $ab^T$.
:::

::: proposition
Let $a,b\in\mathbb{R}^n$. $\|a+b\|^2=\|a\|^2+\|b\|^2$ iff $\langle a, b \rangle = 0$.
:::

::: proposition
Let $a,b\in\mathbb{R}^n$. If $\|a\|=\|b\|$, then $\langle a+b, a-b\rangle = 0$.
::: ^equal-norm-orthogonality

::: proposition
Let $a,b\in\mathbb{R}^n$. If $a\neq 0$, then there exist $\beta\in\mathbb{R}$ and $\delta\in\mathbb{R}^n$ s.t. $b=\beta a+\delta$ and $a^T\delta=0$, where $\beta=\frac{a^T b}{a^T a}$ and $\delta=b-\beta a$.
:::

::: theorem:Cauchy-Schwarz Inequality
Let $a,b\in\mathbb{R}^n$. $|a^T b|\leq\|a\|\|b\|$. Equality holds iff there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$, or $a=0$, or $b=0$.
:::

::: proof
If $a=0$ or $b=0$, $|a^T b|=0=\|a\|\|b\|$. Assume $a\neq 0$ and write $b=\beta a+\delta$ with $a^T\delta=0$. Then, $(a^T b)^2=(a^T(\beta a+\delta))^2=(\beta\|a\|^2)^2\leq \|a\|^{2}(\beta^2\|a\|^2+\|\delta\|^2) = \|a\|^{2}\|\beta a+\delta\|^2= \|a\|^2\|b\|^2$, and thus $|a^T b|\leq\|a\|\|b\|$. Equality holds iff $\|\delta\|=0$, i.e., there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$.
:::

::: definition:$\cos \theta$
Let $a,b\in\mathbb{R}^n$. $\cos \theta := \frac{a^T b}{\|a\|\|b\|}$.
:::

::: note
Cauchy-Schwarz inequality ensures that $|\cos \theta| < 1$.
:::

## Complex Vector Space
::: definition:$l_{p}$-norm in $\mathbb{C}^{n}$
Let $a\in \mathbb{C}^n$. The $l_{p}$-norm in $\mathbb{C}^{n}$ is $\|a\|_{p}:=\left(\sum_{i=1}^{n}|a_{i}|^{p}\right)^{\frac{1}{p}}$ for $1\leqslant p<\infty$, and $\|a\|_{\infty}:=\underset{1\leqslant i\leqslant n}{\max}|a_i|$.
:::

::: definition:Standard Inner Product in $\mathbb{C}^{n}$
Let $a,b \in \mathbb{C}^n$. The standard inner product in $\mathbb{C}^{n}$ is $\langle a, b \rangle := a^T b = \sum_{i=1}^n a_i b_i$.
:::

::: definition:Outer Product in $\mathbb{C}^{n}$
Let $a,b \in \mathbb{C}^n$. The outer product in $\mathbb{C}^{n}$ is $ab^*$.
:::

::: proposition
Let $a,b \in \mathbb{C}^n$. If $\langle a, b \rangle = 0$, then $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$.
::: ^complex-orthogonal-pythagorean

::: note
The reverse of [[#^complex-orthogonal-pythagorean|Proposition 12]] is incorrect. If $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$, then $\Re(a^{*}b)=\Re(b^{*}a)=0$.
:::

::: note
[[#^equal-norm-orthogonality|Proposition 5]] is incorrect in $\mathbb{C}^{n}$. If $\|a\|=\|b\|$, then $\langle a+b, a-b\rangle = 0$ does not always hold.
:::
