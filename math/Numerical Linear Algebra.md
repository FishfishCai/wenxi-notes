# Basic Definition
## Real Vector
> [!definition| of Inner Product, Norm, and Outer Product] $a,b \in \mathbb{R}^n$
> - The (Euclidean) inner product is $\langle a, b \rangle := a^\top b = \sum_{i=1}^n a_i b_i$.<br>
> - The (Euclidean) norm is  $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^\top a}$.<br>
> - The outer product is $ab^\top$.

> [!lemma|*]   $a,b\in\mathbb{R}^n$
> - $\|a+b\|^2=\|a\|^2+\|b\|^2$ iff. $a^\top b=0$.<br>
> - If $\|a\|=\|b\|$, then $(a+b)\perp(a-b)$. <br>
> - If $s\neq0$, then there exist $\beta\in\mathbb{R}$ and $\delta\in\mathbb{R}^n$ such that $b=\beta a+\delta$ and $a^\top\delta=0$, with $\beta=\frac{a^\top b}{a^\top a}$ and $\delta=b-\beta a$.

> [!thm|: Cauchy-Schwarz Inequality] $a,b\in\mathbb{R}^n$
> $|a^\top b|\le\|a\|\|b\|$. Equality holds if and only if there exists $\lambda\in\mathbb{R}$ such that $b=\lambda a$, or $a=0$, or $b=0$.<br>
> >Proof: If $a=0$ or $b=0$, then $|a^\top b|=0=\|a\|\|b\|$. Assume $a\ne0$ and write $b=\beta a+\delta$ with $a^\top\delta=0$ and $\beta=\frac{a^\top b}{a^\top a}$. Then,  $(a^\top b)^2=(a^\top(\beta a+\delta))^2=(\beta\|a\|^2)^2=\beta^2\|a\|^4\le  \|a\|^{2}(\beta^2\|a\|^2+\|\delta\|^2) = \|a\|^{2}(\|\beta a+\delta\|^2)= \|a\|^2\|b\|^2$,
> and taking square roots gives $|a^\top b|\le\|a\|\|b\|$. Equality holds if and only if $\|\delta\|=0$, i.e., $b=\beta a$.

> [!definition| of Angle] $a,b\in\mathbb{R}^n$
> $cos \theta = \frac{a^{\top}b}{\|a\|\|b\|}$. <br>
> > Cauchy-Schwarz inequality ensures that $\|cos \theta\| < 1$. 

## Complex Vector
> [!definition| of Inner Product, and Norm] $a,b\in\mathbb{C}^n$
> - The inner product is $\langle a, b \rangle = b^{*}a$.<br>
> - The norm is $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^{*}a}$.
 
> [!lemma|*] $a,b \in \mathbb{C}^n$
> If $a\perp b$, then  $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$. <br>
> > The reverse is wrong. If $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$, then $Re(a^{*}b)=Re(b^{*}a)=0$.<br>
Parallelogram law is wrong in $\mathbb{C^{n}}$.

## Matrix
> [!definition| of General Inner Product] 
> A general inner product satisfies:
> - $\langle a, b \rangle = \langle b, a \rangle$.
> - $\langle a , a \rangle \ge 0$ and the equality holds when $a=0$.
> - $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$
>  

> [!definition| of Symmetric Positive Definite Matrix] $A\in \mathbb{R}^{n,n}$
> $A$ is a symmetic positive def matrix if $A=A^{\top}$ and $x^{\top}Ax>0$ for all $x\neq 0$.
> > $y^{\top}Ax$ is an inner product.

> [!definition| of Orthogonal Matrix] $Q \in \mathbb{R}^{n,n}$
> $Q$ is an orthogonal matrix if each colomun is a unit vector and $\langle v_{i}, v_{j}\rangle = 0$ for all $i\neq j$.
> > $Q$ is an orthogonal matrix iff. $Q^{\top}Q=I$.

> [!theorem|: Spectral Theorem] $A \in \mathbb{R}^{n,n}$
> If $A=A^{\top}$, then it has an orthomornal basis composed of eigenvectors.

> [!definition| of Projection Matrix] $a,q \in \mathbb{R}^n$
> Projection matrix of $q$ is $qq^{\top}$, whose rank is $1$.<br>
> Component of $a$ along $q$ is equal to $qq^{\top} * a$.
>  > Orthogonal projection matrix is $(I - qq^{\top})$, whose rank is $n-1$.
  
> [!lemma|*] $v_1, v_2, ..., v_k \in \mathbb{R}^n$
> If $v_{1}, v_{2}, ..., v_{k}$ is an orthonormal set, then the matrix $v_{1}v_{1}^{\top}+...+v_{k}v_{k}^{\top}$ projects to $\langle v_{1}, v_{2}, ..., v_{k} \rangle$.
> > Let $Q=(v_{1},v_{2},..., v_{k})$, then projection matrix to $\langle v_{1}, v_{2}, ..., v_{k} \rangle$ is $P = QQ^{\top} = v_{1}v_{1}^{\top}+...+v_{k}v_{k}^{\top}$, whose rank is k.<br>
> > $Q^{\top}x$ gives the coefficients when $x$ is projected to the $Range(Q)$.<br>
> > $I-QQ^{\top}$ is the complementary projection, whose rank is $n-k$.<br>

