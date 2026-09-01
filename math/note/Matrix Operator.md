---
id: hphjgp5mjz4dr00c
title: Matrix Operator
tags: []
refs: []
backrefs: []
---
## Projection Matrix
::: definition:Projection Matrix of Vector
Let $v \in \mathbb{R}^n$. Assume $\|v\| = 1$. The projection matrix of vector $v$ is $vv^T$, whose rank is $1$. For any $x \in \mathbb{R}^n$, the component of $x$ along $v$ is $vv^T x$.
:::

::: definition:Orthogonal Projection Matrix of Vector
Let $v \in \mathbb{R}^n$. Assume $\|v\| = 1$. The orthogonal projection matrix onto the subspace orthogonal to $v$ is $I - vv^T$, whose rank is $n - 1$.
:::

::: proposition
Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If $\{v_1, v_2, \dots, v_k\}$ is an orthonormal set, then the matrix $P = v_1 v_1^T + \cdots + v_k v_k^T$ is the projection matrix onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$.
:::

::: note
Let $V = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n, k}$. The projection matrix $P$ in [[:3]] admits the factorization $P = VV^T$, whose rank is $k$. For any $x \in \mathbb{R}^n$, the vector $V^T x$ gives the coefficients of the projection of $x$ onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$. The complementary projection matrix is $I - VV^T$, whose rank is $n - k$.
:::

::: definition:Projection Matrix of Matrix
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full rank. The projection matrix of matrix $A$ is $P = A(A^T A)^{-1} A^T$. For any $x \in \mathbb{R}^n$, the component of $x$ in $\text{range}(A)$ is $Px$.
:::

## Householder Reflection Matrix
::: definition:Householder Reflection Matrix
Let $v \in \mathbb{R}^n$. Assume $\|v\| = 1$. The Householder reflection matrix associated with $v$ is $H := I - 2vv^T$.
:::

::: note
Let $a, b \in \mathbb{R}^n$. If $v = \frac{a - b}{\|a - b\|}$ and $\|a\| = \|b\|$, then $Ha = b$ and $Hb = a$.
:::

::: note
For [[:5]], the Householder reflection matrix is an orthogonal matrix.
:::

## Pseudoinverse
::: definition:Pseudoinverse
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full rank. The pseudoinverse of $A$ is $A^+ := (A^T A)^{-1} A^T$.
:::
