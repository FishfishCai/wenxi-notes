## Projection Matrix
> [!definition|] Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The projection matrix onto the direction of $q$ is $qq^{\top}$, which has rank $1$. For any $a \in \mathbb{R}^n$, the component of $a$ along $q$ is given by $qq^{\top} a$.

> [!definition|] Orthogonal Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The orthogonal projection matrix onto the subspace orthogonal to $q$ is $I - qq^{\top}$, which has rank $n - 1$.

> [!lemma|]
> Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If ${v_1, v_2, \dots, v_k}$ is an orthonormal set, then the matrix $P = v_1 v_1^{\top} + \cdots + v_k v_k^{\top}$ is the projection matrix onto the subspace $\text{span}(v_{1}, v_{2}, \cdots , v_{k})$.

^c331b4

> [!remark|]
> Let $Q = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n \times k}$. The projection matrix $P$ in [[#^c331b4]] admits the factorization $P = QQ^{\top}$, and the rank of $P$ is $k$. For any $x \in \mathbb{R}^n$, the vector $Q^{\top} x$ gives the coefficients of the projection of $x$ onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$. The complementary projection matrix is $I - QQ^{\top}$, whose rank is $n - k$.

## Householder Reflection Matrix
> [!definition|] Householder Reflection Matrix
> Let $\|v\|=1$. The Householder reflection matrix associated with $v$ is $H(x):=(I-2vv^{\top})x$.

^58bf6d

> [!Remark|] 
> Let $a,b \in \mathbb{R}^{n}$. If $v=\frac{a-b}{\|a-b\|}$ and $\|a\|=\|b\|$, then $H(a)=b$ and $H(b)=a$.

> [!remark|]
> For [[#^58bf6d]], Householder reflection operator is an orthonormal matrix.

## Pseudoinverse
> [!definition|] Pseudoinverse
> Let $A\in R^{n,n}$. The pseudoinverse of $A$ is $A^{+}:=(A^{\top}A)^{-1}A^{\top}$
