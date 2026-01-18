# Basic Definition
## Real Vector
> [!definition|] Inner Product
>  $\langle a, b \rangle$ is an inner products if:
> - $\langle a, b \rangle = \langle b, a \rangle$.
> - $\langle a , a \rangle \ge 0$ and the equality holds when $a=0$.
> - $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$

> [!definition|] Inner Product in $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The inner product in $\mathbb{R}^{n}$ is $\langle a, b \rangle := a^\top b = \sum_{i=1}^n a_i b_i$.

> [!definition|]  Norm in  $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The norm in  $\mathbb{R}^{n}$ is  $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^\top a}$.

> [!definition|] Outer Product in  $\mathbb{R}^{n}$
> Let $a,b \in \mathbb{R}^n$. The outer product  in  $\mathbb{R}^{n}$ is $ab^\top$.

> [!lemma|]
> Let $a,b\in\mathbb{R}^n$. $\|a+b\|^2=\|a\|^2+\|b\|^2$ iff $\langle a, b \rangle =0$.

> [!lemma|]
>  Let $a,b\in\mathbb{R}^n$. If $\|a\|=\|b\|$, then $\langle a+b, a-b\rangle = 0$.

^845c0b

> [!lemma|]
> Let $a,b\in\mathbb{R}^n$. If $a\neq0$, then there exist $\beta\in\mathbb{R}$ and $\delta\in\mathbb{R}^n$ such that $b=\beta a+\delta$ and $a^\top\delta=0$, with $\beta=\frac{a^\top b}{a^\top a}$ and $\delta=b-\beta a$.

> [!thm|] Cauchy-Schwarz Inequality
> Let $a,b\in\mathbb{R}^n$. $|a^\top b|\le\|a\|\|b\|$. Equality holds iff. there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$, or $a=0$, or $b=0$.

`\begin{proof}`
If $a=0$ or $b=0$, then $|a^\top b|=0=\|a\|\|b\|$. Assume $a\ne0$ and write $b=\beta a+\delta$ with $a^\top\delta=0$. Then,  $(a^\top b)^2=(a^\top(\beta a+\delta))^2=(\beta\|a\|^2)^2\le  \|a\|^{2}(\beta^2\|a\|^2+\|\delta\|^2) = \|a\|^{2}\|\beta a+\delta\|^2= \|a\|^2\|b\|^2$,
and thus $|a^\top b|\le\|a\|\|b\|$. Equality holds iff $\|\delta\|=0$, i.e., there exists $\lambda\in\mathbb{R}$ s.t. $b=\lambda a$.
`\end{proof}`

> [!definition| 5] $\cos \theta$
> Let $a,b\in\mathbb{R}^n$. $\cos \theta := \frac{a^{\top}b}{\|a\|\|b\|}$.

> [!remark|]
> Cauchy-Schwarz inequality ensures that $\|\cos \theta\| < 1$. 

## Complex Vector
> [!definition|] Inner Product in $\mathbb{C}^{n}$
> Let $a,b\in\mathbb{C}^n$. The inner product  in $\mathbb{C}^{n}$ is $\langle a, b \rangle := b^{*}a$.

> [!definition|] Norm in $\mathbb{C}^{n}$
> Let $a,b\in\mathbb{C}^n$.  The norm in $\mathbb{C}^{n}$ is $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^{*}a}$.
 
> [!lemma|] 
> Let $a,b \in \mathbb{C}^n$. If $\langle a, b \rangle$, then  $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$.


^8c734c

> [!remark|]
> The reverse of [[#^8c734c]] is incorrect. If $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$, then $\Re(a^{*}b)=\Re(b^{*}a)=0$.

> [!remark|]
> [[#^845c0b]] is incorrect in $\mathbb{C}^{n}$. If $\|a\|=\|b\|$, $\langle a+b , a-b \rangle = 0$ not always holds.

## Matrix
> [!definition|] Symmetric Positive Definite Matrix
> Let $A\in \mathbb{R}^{n,n}$. $A$ is a symmetic positive definite matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.
> > 

> [!remark|]
> If $A$ is a symmetic positive definite matrix, then $\langle x, y \rangle :=y^{\top}Ax$ is an inner product.

> [!definition|] Orthogonal Matrix
> Let $Q \in \mathbb{R}^{n,n}$, and $v_i$ for $i \in {1,2,\dots,n}$ denotes the $i$-th column of $Q$. $Q$ is an orthogonal matrix if all $v_i$ are unit vectors and $\langle v_i, v_j\rangle = 0$ for all $i \neq j$.

> [!lemma|] Lemma
> $Q$ is an orthogonal matrix iff. $Q^{\top}Q=I$.

> [!theorem|] Spectral Theorem
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, then $A$ admits an orthonormal basis consisting of eigenvectors.

## Projection
> [!definition|] Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The projection matrix onto the direction of $q$ is $qq^{\top}$, which has rank $1$. For any $a \in \mathbb{R}^n$, the component of $a$ along $q$ is given by $qq^{\top} a$.

> [!definition|] Orthogonal Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The orthogonal projection matrix onto the subspace orthogonal to $q$ is $I - qq^{\top}$, which has rank $n - 1$.

> [!lemma|]
> Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If ${v_1, v_2, \dots, v_k}$ is an orthonormal set, then the matrix $P = v_1 v_1^{\top} + \cdots + v_k v_k^{\top}$ is the projection matrix onto the subspace $\langle v_1, v_2, \dots, v_k \rangle$.

^c331b4

> [!remark|]
> Let $Q = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n \times k}$. The projection matrix $P$ in [[#^c331b4]] admits the factorization $P = QQ^{\top}$, and the rank of $P$ is $k$. For any $x \in \mathbb{R}^n$, the vector $Q^{\top} x$ gives the coefficients of the projection of $x$ onto the subspace $\langle v_1, v_2, \dots, v_k \rangle$. The complementary projection matrix is $I - QQ^{\top}$, whose rank is $n - k$.

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

> [!theorem|] QR Factorization
> Let $A = [a_1\; a_2\; \cdots\; a_k] \in \mathbb{R}^{n \times k}$, where $a_i$ denotes the $i$-th column of $A$. If $v_1, v_2, \dots, v_k$ is the orthonormal set constructed from $a_{i}$, via the classical Gram–Schmidt process. We have
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
