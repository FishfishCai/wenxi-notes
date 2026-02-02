# Real Vector
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

# Complex Vector
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

# Projection
> [!definition|] Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The projection matrix onto the direction of $q$ is $qq^{\top}$, which has rank $1$. For any $a \in \mathbb{R}^n$, the component of $a$ along $q$ is given by $qq^{\top} a$.

> [!definition|] Orthogonal Projection Matrix
> Let $q \in \mathbb{R}^n$ with $\|q\| = 1$. The orthogonal projection matrix onto the subspace orthogonal to $q$ is $I - qq^{\top}$, which has rank $n - 1$.

> [!lemma|]
> Let $v_1, v_2, \dots, v_k \in \mathbb{R}^n$. If ${v_1, v_2, \dots, v_k}$ is an orthonormal set, then the matrix $P = v_1 v_1^{\top} + \cdots + v_k v_k^{\top}$ is the projection matrix onto the subspace $\text{span}(v_{1}, v_{2}, \cdots , v_{k})$.

^c331b4

> [!remark|]
> Let $Q = [v_1\ v_2\ \cdots\ v_k] \in \mathbb{R}^{n \times k}$. The projection matrix $P$ in [[#^c331b4]] admits the factorization $P = QQ^{\top}$, and the rank of $P$ is $k$. For any $x \in \mathbb{R}^n$, the vector $Q^{\top} x$ gives the coefficients of the projection of $x$ onto the subspace $\text{span}(v_1, v_2, \dots, v_k)$. The complementary projection matrix is $I - QQ^{\top}$, whose rank is $n - k$.

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
> Gram-Schmidt process can also be formed as $AR_{1}R_{2}\cdots R_{k}$, where $$
R_i=\begin{pmatrix}
1 & 0 & \cdots & 0 & 0 & \cdots & 0\\
0 & 1 & \cdots & 0 & 0 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\
0 & 0 & \cdots & 1 & 0 & \cdots & 0\\
0 & 0 & \cdots & 0 & \dfrac{1}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} &
-\dfrac{\left\langle v_i,\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_{i+1}\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|} & \cdots &
-\dfrac{\left\langle v_i,\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_k\right\rangle}{\left\|\left(I-v_1v_1^T-\cdots-v_{i-1}v_{i-1}^T\right)a_i\right\|}\\
0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\
\vdots & \vdots &  & \vdots & \vdots &  & \ddots
\end{pmatrix}.
$$


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

# Real Matrix
> [!definition|] Symmetric Positive Definite Matrix
> Let $A\in \mathbb{R}^{n,n}$. $A$ is a symmetic positive definite matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.
> > 

> [!remark|]
> If $A$ is a symmetic positive definite matrix, then $\langle x, y \rangle :=y^{\top}Ax$ is an inner product.

> [!definition|] Orthogonal Matrix
> Let $Q \in \mathbb{R}^{n,n}$. Q is an orthonormal matrix if columns of $Q$ are orthonormal.

> [!Lemma|]
> $Q$ is an orthogonal matrix iff $Q^{\top}Q=I$.

^8f1e27

`\begin{proof}`
This follows from [[#^c331b4]]. 
`\end{proof}`

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. $Q$ is an orthogonal matrix iff $\|Qx\|=\|x\|$ for all $x\in \mathbb{R}^{n}$.

^3b00f3

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, then $\|Qx-Qy\|=\|x-y\|$ for all $x, y\in \mathbb{R}^{n}$.

^a25c0d

> [!lemma|] 
> Let $f:\mathbb{R}^{n}\to \mathbb{R}^{n}$. If $f(0)=0$ and $\|f(x)-f(y)\|=\|x-y\|$, then there exists an orthogonal matrix $Q$ s.t. $f(x)=Qx$.

`\begin{proof}`
Let $e_{1}, e_{2}, \cdots , e_{n}$ be the standard basis of $\mathbb{R}^{n}$. 
$$
\begin{align}
\|f(e_{i})-f(e_{j})\|=\|e_{i}-e_{j}\|&\implies(f(e_{i}))-f(e_{j})^{\top}(f(e_{i}))-f(e_{j})=(e_{i}-e_{j})^{\top}(e_{i}-e_{j})\\
&\implies f(e_{i})^{\top}f(e_{i})+f(e_{j})^{\top}f(e_{j})-2f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{i}+e_{j}^{\top}e_{j}-2e_{i}^{\top}e_{j}\\
&\implies f(e_{i})^{\top}f(e_{j})=e_{i}^{\top}e_{j}\\
\end{align}.
$$
This emplies that $f(e_{1}), f(e_{2}), \cdots , f(e_{n})$ form an orthonormal basis. And it is obvious that $Q=[f(e_{1}) \, f(e_{2}) \,\cdots \, f(e_{n})]$.
`\end{proof}`


> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $\lambda$ is an eigenvalue of $Q$, then $|\lambda| = e^{i\theta} = 1$.

^d83a9a

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix and $e^{i\theta}$ is an eigenvalue of $Q$, then $e^{-i\theta}$ is an eigenvalue of $Q^{\top}$.

^e92a78

> [!Lemma|]
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, $\lambda_{i}$ and $\lambda_{j}$ are two different eigenvalue of $Q$ and $v, w \in \mathbb{C}^{n}$ are two eigenvectors s.t. $Qv = \lambda_{i}v$ and $Qw=\lambda_{j}w$, then $v^{*}w=w^{*}v=0$.

^bb6200

`\begin{proof}`
$\lambda_{i}w^{*}v=w^{*}\lambda_{i}v=w^{*}Qv=(Q^{\top}w)^{*}v=(\lambda_{j}^{-1}w)^{*}v=\lambda_{j}w^{*}v$, implying that $v^{*}w=w^{*}v=0$.
`\end{proof}`

> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, then A has n real eigenvalues.

^6e7882

`\begin{proof}`
Let $R(x)=\frac{x^{\top}Ax}{x^{\top}x}$  and $S^{n-1}=\{x\in \mathbb{R}^{n}:\|x\|=1\}$. Since $S^{n-1}$ is a compact set, there exists $x^{*}$ such that $x^{*\top}Ax^{*}=\underset{\|x\|=1}{\max}x^{\top}Ax$. Let $L(x,\lambda)=x^{\top}Ax-\lambda(x^{\top}x-1)$. By the method of Lagrange multipliers, $\nabla_{x}L(x^{*},\lambda)=0$, which implies $Ax^{*}=\lambda x^{*}$. Then we consider the subspace orthogonal to $x^*$ and iterate the argument.
`\end{proof}`


> [!lemma|] 
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, $\lambda_{i}$ and $\lambda_{j}$ are two eigenvalue of $A$ and $v,\,w\in \mathbb{R}^{n}$ are two different eigenvectors s.t. $Av = \lambda_{i}v$ and $Aw=\lambda_{j}w$, then $v^{\top}w=w^{\top}v=0$.

^0a7023

`\begin{proof}`
$\lambda_{i}w^{\top}v=w^{\top}\lambda_{i}v=w^{\top}Av=(A^{\top}w)^{\top}v=(\lambda_{j}w)^{\top}v=\lambda_{j}w^{\top}v$, implying that $v^{\top}w=w^{\top}v=0$.
`\end{proof}`

> [!theorem|] Spectral Theorem
> Let $A \in \mathbb{R}^{n,n}$. If $A = A^{\top}$, then $A$ admits an orthonormal basis consisting of eigenvectors.

`\begin{proof}`
This follows from [[#^6e7882]] and [[#^0a7023]].
`\end{proof}`

> [!lemma|] 
> Let $Q\in \mathbb{R}^{n,n}$. If $Q$ is an orthogonal matrix, then $\det(Q)=\pm1$.

^f982d8

> [!remark|]
> In [[#^f982d8]], if $\det(Q)=1$, then the columns of $Q$ have +ve orientation. And if $\det(Q)=-1$, then the columns of $Q$ have -ve orientation.

> [!lemma|] 
> Let  $A\in \mathbb{R}^{n,n}$, $\det(A)$ can be interp as the signed volume of the parallelepiped formed by the columns of $A$.

`\begin{proof}`
Following [[#^4b5424]], $\det(A)=\det(Q)\det(R)=\pm \prod r_{ii}$. The sign depends on the orientation of the $Q$.
`\end{proof}`

# Complex Matrix
> [!definition|] Unitary Matrix
> Let $Q\in \mathbb{C}^{n}$. Q is an unitary matrix if columns of $Q$ are orthonormal.

> [!remark|]
> The eigenvectors of an orthogonal matrix form an unitary matrix.

> [!remark|]
> [[#^8f1e27]], [[#^3b00f3]], [[#^a25c0d]], [[#^d83a9a]], [[#^e92a78]] and [[#^bb6200]] follow if we change $^{\top}$ to $^{*}$.

# Computation
> [!lemma|] 
> Operation count for $a^{\top}b$ is $2n-1$.

`\begin{proof}`
$n$ multiplication and $n-1$ addition.
`\end{proof}`

> [!lemma|] 
> Operation count for $a-b$ is $n$.

^ed7e9f

> [!lemma|] 
> Operation count for $\alpha a$ is $n$.

^592ada

> [!lemma|] 
> Operation count for $(I-P)x$ where $P=qq^{\top}$ is $4n-1$.

^dd24b3

`\begin{proof}`
$(I-P)x=x-q(q^{\top}x)$, which is the combinition of [[#^ed7e9f]], [[#^592ada]] and [[#^dd24b3]].
`\end{proof}`

> [!theorem|]
> Operation count for [[#^c68556]] is $\sum_{j=1}^{k}(4n-1)(j-1)+(2n-1)\sim2nk^{2}$.

# Machine Learning
> [!theorem|] Novikov's Analysis
> Assume that the training data are linearly separable. That is, there exists a vector $w_N$ with $\|w_N\| = 1$ s.t. for all training samples $(x_i, y_i)$, $y_i \, w_N^\top x_i \ge \varepsilon > 0.$ Assume further that the input vectors are bounded, i.e., $\|x_i\| \le R \text{ for all } i.$ Then the perceptron algorithm makes only finitely many classification mistakes.

`\begin{proof}`
If there is no misclassification, $w_{j}^{\top}w_{j}=w_{j-1}^{\top}w_{j-1}$ and if there is misclassification, $w_{j}^{\top}w_{j}=(w_{j-1}+x_{j}y_{j})^{\top}(w_{j-1}+x_{j}y_{j}) = w_{j-1}^{\top}w_{j-1}+ y_{j}^{2}x_{j}^{\top}x_{j}+2y_{j}w_{j-1}^{\top}x_{j}$, implying $w_{j}^{\top}w_{j}\leqslant w_{j-1}^{\top}w_{j-1}+ x_{j}^{\top}x_{j}$. Since $x_{j}^{\top}x_{j}$ is bounded, then $\|w_{j}\|\leqslant \sqrt{m_{j}}R$. Besides, if there's no misclassification, $w_{N}^{\top}w_{j}=w_{N}^{\top}w_{j-1}$ and if there is misclassification, $w_{N}^{\top}w_{j}=w_{N}^{\top}(w_{j-1}+x_{i}y_{j})=w_{N}^{\top}w_{j-1} + y_i \, w_N^\top x_i$, implying $w_{N}^{\top}w_{j}\geq y_i \, w_N^\top x_i$. Since $\|w_{N}\|\|w_{j}\|\geq |w_{N}^{\top}w_{j}|$, then $\|w_{j}\|\geq m_{j}\varepsilon$. Therefore, $m_{j}\leqslant(\frac{R}{\varepsilon})^{2}$ 
`\end{proof}`

# Reflection
> [!definition|] Householder Reflection Operator
> Let $\|v\|=1$. The Householder reflection operator associated with v is $H(x):=(I-2vv^{\top})x$.

> [!lemma|] 
> Let $a,b \in \mathbb{R}^{n}$. If $v=\frac{a-b}{\|a-b\|}$ and $\|a\|=\|b\|$, then $H(a)=b$ and $H(b)=a$.

> [!theorem|] QR factorization using Householder reflection operator
> Let $A^{(0)} = [a_1\; a_2\; \cdots\; a_k] \in \mathbb{R}^{n \times k}$. For the $i$-th step, take the tail vector $a_i := A_{i:n,\,i}^{(i-1)}\in\mathbb{R}^{n-i+1}$. Define $e_1=(1,0,\dots,0)^\top\in\mathbb{R}^{n-i+1}$ and set $b := -\mathrm{sign}((a_i)_1)\,\|a_i\|\,e_1$. Let $v := \dfrac{a_i-b}{\|a_i-b\|}$ and define $H_{i} := \begin{bmatrix} I_{i-1} & 0 \\ 0 & \hat H_{i} \end{bmatrix}$ where $\hat H_{i} = I - 2vv^{\top}$. Update $A^{(i)}=H_{i}A^{(i-1)}$. $Q = H_1 H_2\cdots H_k$ and $R=A^{(k)}$. 
