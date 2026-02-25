#NumericalLinearAlgebra 
Prerequisite knowledge: [[Real Vector Space]], [[Real Matrix]]
## Projection Matrix
> [!definition|] Projection Matrix of Vector
> Let $v \in \mathbb{R}^n$. $\|v\| = 1$. The projection matrix of vector $v$ is $vv^{\top}$, whose rank is $1$. For any $x \in \mathbb{R}^n$, the component of $x$ along $v$ is given by $vv^{\top} x$.

> [!definition|] Orthogonal Projection Matrix of Vector
> Let $v \in \mathbb{R}^n$. $\|v\| = 1$. The orthogonal projection matrix onto the subspace orthogonal to $v$ is $I - vv^{\top}$, whose rank is $n - 1$.

> [!proposition|]
> Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If ${v_1, v_2, \dots, v_k}$ is an orthonormal set, the matrix $P = v_1 v_1^{\top} + \cdots + v_k v_k^{\top}$ is the projection matrix onto the subspace $\text{span}(v_{1}, v_{2}, \cdots , v_{k})$.

^c331b4

> [!remark|]
> Let $V = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n, k}$. The projection matrix $P$ in [[#^c331b4]] admits the factorization $P = VV^{\top}$, whose rank is $k$. For any $x \in \mathbb{R}^n$, the vector $V^{\top} x$ gives the coefficients of the projection of $x$ onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$. The complementary projection matrix is $I - VV^{\top}$, whose rank is $n - k$.

> [!Definition|] Projection Matrix of Matrix 
> Let $A\in \mathbb{R}^{n\times k}$. $A$ is full-rank. The projection matrix of matrix $A$ is $P=A(A^{\top}A)^{-1}A^{\top}$. For any $x\in \mathbb{R}^{n}$, the component of $x$ in $\mathrm{range}(A)$ is given by $Px$.

## Householder Reflection Matrix
> [!definition|] Householder Reflection Matrix
> Let $v \in \mathbb{R}^{n}$. $\|v\|=1$. The Householder reflection matrix associated with $v$ is $H:=I-2vv^{\top}$.

^58bf6d

> [!Remark|] 
> Let $a,b \in \mathbb{R}^{n}$. If $v=\frac{a-b}{\|a-b\|}$ and $\|a\|=\|b\|$, $Ha=b$ and $Hb=a$.

> [!remark|]
> For [[#^58bf6d]], Householder reflection matrix is an orthogonal matrix.

## Pseudoinverse
> [!definition|] Pseudoinverse
> Let $A\in R^{n,k}$. $A$ is full-rank. The pseudoinverse of $A$ is $A^{+}:=(A^{\top}A)^{-1}A^{\top}$.
