---
tags:
---
#NumericalLinearAlgebra 
Prerequisite knowledge: [[Computation]], [[Real Matrix]], [[Matrix Operator]]
## QR Factorization
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

^4b5424

> [!remark|]
> For [[#^4b5424]], QR factorization via Gram-Schmidt process can also be formed as $AR_{1}R_{2}\cdots R_{k} = Q$, where $$ 
> R_i=\begin{pmatrix} 
> 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\
> 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\
> \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\
> 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\
> 0 & 0 & \cdots & 0 & \dfrac{1}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} & -\dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{i+1}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|^{2}} & \cdots & -\dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{k}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|^{2}} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\
> \vdots & \vdots &  & \vdots & \vdots &  & \ddots
> \end{pmatrix}.
> $$and $v_{j}$ is the $j$-th column of $AR_{1}R_{2}\cdots R_{i-1}$ for $j<i$. Then, 
> $$
> R_{i}^{-1}= \begin{pmatrix} 
> 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\
> 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\
> \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\
> 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\
> 0 & 0 & \cdots & 0 & \left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\| & \dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{i+1}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} & \cdots & \dfrac{\left\langle \left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i,a_{k}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\
> \vdots & \vdots &  & \vdots & \vdots &  & \ddots
> \end{pmatrix}.
> $$
> and thus $R=R_{k}^{-1}R_{k-1}^{-1}\cdots R_{1}^{-1}$ is an upper triangular matrix.

> [!theorem|] Modified Gram–Schmidt Process
> Let $a_{1}, a_{2}, ..., a_{k} \in \mathbb{R}^{n}$. If  $a_{1}, a_{2}, ..., a_{k}$ are independent, we can construct an orthonormal set $v_{1}, v_{2}, ..., v_{k}$, where 
> $$
> \begin{align*}
> v_1 &= \frac{a_1}{\|a_1\|},\\
> v_i &=
> \frac{\bigl( I - v_1 v_1^T\bigr) \bigl( I-v_{2}v_{2}^{\top}\bigr)\cdots \bigl( I-v_{i-1}v_{i-1}^{\top}\bigr)a_i}
> {\|\bigl( I - v_1 v_1^T\bigr) \bigl( I-v_{2}v_{2}^{\top}\bigr) \cdots \bigl( I-v_{i-1}v_{i-1}^{\top}\bigr)a_i\|},
> \qquad i=2,\dots,k.
> \end{align*}
> $$

^c68556

> [!theorem|]
> Operation count for [[#^c68556]] is $\sum_{j=1}^{k}(4n-1)(j-1)\sim2nk^{2}$.

> [!theorem|] QR factorization using Householder reflection matrix
> Let $A^{(0)} = [a_1\; a_2\; \cdots\; a_k] \in \mathbb{R}^{n \times k}$. For the $i$-th step, take the tail vector $a_i := A_{i:n,\,i}^{(i-1)}\in\mathbb{R}^{n-i+1}$. Define $e_1=(1,0,\dots,0)^\top\in\mathbb{R}^{n-i+1}$ and set $b := -\mathrm{sign}((a_i)_1)\,\|a_i\|\,e_1$. Let $v := \dfrac{a_i-b}{\|a_i-b\|}$ and define $H_{i} := \begin{bmatrix} I_{i-1} & 0 \\ 0 & \hat H_{i} \end{bmatrix}$ where $\hat H_{i} = I - 2vv^{\top}$. Update $A^{(i)}=H_{i}A^{(i-1)}$. $Q = H_1 H_2\cdots H_k$ and $R=A^{(k)}$. 

^857b04

> [!theorem|]
> Operation count for [[#^857b04]] is $\sum_{j=1}^{k}4(n-j-1)(k-j+1)\sim 2nk^{2}-\frac{2}{3}k^{3}$.
