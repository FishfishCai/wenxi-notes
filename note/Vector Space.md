## Vector Space
::: definition:Vector Space
Let $\mathbb{F}$ be a field and $V$ be a set. $V$ is a vector space over $\mathbb{F}$ if there are operations $ + : V \times V \to V$ and $\cdot : \mathbb{F} \times V \to V$ s.t.:
- $a + b = b + a$ for any $a, b \in V$.
- $(a + b) + c = a + (b + c)$ for any $a, b, c \in V$.
- There exists $0 \in V$ s.t. $a + 0 = a$ for any $a \in V$.
- For any $a \in V$, there exists $-a \in V$ s.t. $a + (-a) = 0$.
- $\lambda(a + b) = \lambda a + \lambda b$ for any $a, b \in V$ and $\lambda \in \mathbb{F}$.
- $(\lambda + \mu)a = \lambda a + \mu a$ for any $a \in V$ and $\lambda, \mu \in \mathbb{F}$.
- $(\lambda\mu)a = \lambda(\mu a)$ for any $a \in V$ and $\lambda, \mu \in \mathbb{F}$.
- $1a = a$ for any $a \in V$.
:::

::: definition:Subspace
Let $V$ be a vector space over $\mathbb{F}$ and $M \subseteq V$. The set $M$ is a linear subspace if $M$ is nonempty and $\alpha x + \beta y \in M$ for any $x,y \in M$ and $\alpha,\beta \in \mathbb{F}$.
:::

::: definition:Finite-Dimensional Vector Space
Let $V$ be a vector space over a field $\mathbb{F}$. $V$ is finite-dimensional if it has a finite basis. If a basis has $n$ vectors, the dimension of $V$ is $\dim V = n$, with $\dim\{0\} = 0$.
:::

::: definition:Linear Map
Let $V$ and $W$ be vector spaces over the same field $\mathbb{F}$. A map $A : V \to W$ is linear if $A(\lambda x + y) = \lambda Ax + Ay$ for any $x, y \in V$ and $\lambda \in \mathbb{F}$.
:::

::: definition:Vector Space of Linear Maps
Let $V$ and $W$ be vector spaces over the same field $\mathbb{F}$. The vector space of linear maps from $V$ to $W$ is $\mathcal{L}(V, W) := \{A : V \to W : A \text{ is linear}\}$, with $(A + B)(x) := Ax + Bx$ and $(\lambda A)(x) := \lambda Ax$ for any $A, B \in \mathcal{L}(V, W)$, $x \in V$, and $\lambda \in \mathbb{F}$.
:::

::: definition:Linear Functional
Let $V$ be a vector space over $\mathbb{F}$. A linear functional on $V$ is a linear map $f : V \to \mathbb{F}$.
:::

::: definition:Algebraic Dual Space
Let $V$ be a vector space over $\mathbb{F}$. The algebraic dual space of $V$ is $V^\# := \mathcal{L}(V, \mathbb{F})$, with $(f + g)(x) := f(x) + g(x)$ and $(\lambda f)(x) := \lambda f(x)$ for any $f, g \in V^\#$, $x \in V$, and $\lambda \in \mathbb{F}$.
:::

## Normed Vector Space
::: definition:Real Norm
Let $V$ be a vector space over $\mathbb{R}$. A map $\|\cdot\| : V \to [0, \infty)$ is a real norm if the following hold for any $a,b \in V$ and $\lambda \in \mathbb{R}$:
- $\|a\| \geq 0$, and the equality holds iff $a = 0$.
- $\|\lambda a\| = |\lambda| \|a\|$.
- $\|a + b\| \leq \|a\| + \|b\|$.
:::

::: definition:Complex Norm
Let $V$ be a vector space over $\mathbb{C}$. A map $\|\cdot\| : V \to [0, \infty)$ is a complex norm if the following hold for any $a,b \in V$ and $\lambda \in \mathbb{C}$:
- $\|a\| \geq 0$, and the equality holds iff $a = 0$.
- $\|\lambda a\| = |\lambda| \|a\|$.
- $\|a + b\| \leq \|a\| + \|b\|$.
:::

::: definition:Normed Vector Space
Let $V$ be a vector space over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $\|\cdot\|$ be a norm on $V$. The pair $(V, \|\cdot\|)$ is a normed vector space.
:::

::: theorem:Norm Equivalence in Finite Dimensions
Let $V$ be a finite-dimensional real or complex vector space and $\|\cdot\|_a$, $\|\cdot\|_b$ be two norms on $V$. There exist constants $c, C > 0$ s.t. $c\|x\|_a \leq \|x\|_b \leq C\|x\|_a$ for any $x \in V$. Thus, any two norms on $V$ are equivalent.
:::

::: definition:Banach Space
Let $(V, \|\cdot\|)$ be a normed vector space. The space is a Banach space if it is [[Topology#^complete-metric-space|complete]] under its norm.
:::

::: definition:Bounded Linear Operator
Let $V$ and $W$ be normed vector spaces over the same field and $A : V \to W$ be a linear map. The operator $A$ is bounded if there exists $C \geq 0$ s.t. $\|Ax\|_W \leq C\|x\|_V$ for any $x \in V$. The vector space of bounded linear operators from $V$ to $W$ is denoted by $\mathcal{B}(V, W)$.
:::

::: definition:Operator Norm
Let $V$ and $W$ be normed vector spaces over the same field and $A \in \mathcal{B}(V, W)$. The operator norm of $A$ is $\|A\| := \underset{\|x\|_V \leq 1}{\sup}\|Ax\|_W$.
:::

::: proposition
Let $V$ and $W$ be normed vector spaces over the same field and $A : V \to W$ be linear. The map $A$ is continuous iff it is bounded.
:::

::: definition:Continuous Dual Space
Let $V$ be a normed vector space over $\mathbb{F}$. The continuous dual space of $V$ is $V^* := \mathcal{B}(V, \mathbb{F})$.
:::

::: definition:Dual Norm
Let $V$ be a normed vector space and $f \in V^*$. The dual norm of $f$ is $\|f\|_{V^*} := \underset{\|x\|_V \leq 1}{\sup}|f(x)|$.
:::

::: proposition
Let $V$ be a normed vector space. $|f(x)| \leq \|f\|_{V^*}\|x\|_V$ for any $f \in V^*$ and $x \in V$.
:::

::: proposition
Let $V$ be a normed vector space. The space $V^*$ is a Banach space under the dual norm, even if $V$ is not complete.
:::

::: note
The algebraic dual $V^\#$ contains all linear functionals, whereas $V^*$ contains only continuous linear functionals. They coincide in finite dimensions, but may differ in infinite dimensions. The supremum in the dual norm need not be attained.
:::

::: definition:Dual Operator
Let $V$ and $W$ be normed vector spaces over the same field and $A \in \mathcal{B}(V, W)$. The dual operator of $A$ is $A' : W^* \to V^*$ defined by $A'f := f \circ A$ for any $f \in W^*$.
:::

::: proposition
Let $V$ and $W$ be normed vector spaces over the same field and $A \in \mathcal{B}(V, W)$. The dual operator $A'$ is bounded and linear, and $\|A'\| = \|A\|$.
:::

## Inner Product Space
::: definition:Real Inner Product
Let $V$ be a vector space over $\mathbb{R}$. A map $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$ is a real inner product if the following hold for any $a,b,c \in V$ and $\lambda \in \mathbb{R}$:
- $\langle a, b \rangle = \langle b, a \rangle$.
- $\langle a, a \rangle \geq 0$, and the equality holds iff $a = 0$.
- $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$.
:::

::: definition:Complex Inner Product
Let $V$ be a vector space over $\mathbb{C}$. A map $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{C}$ is a complex inner product if the following hold for any $a,b,c \in V$ and $\lambda \in \mathbb{C}$:
- $\langle a, b \rangle = \overline{\langle b, a \rangle}$.
- $\langle a, a \rangle \geq 0$, and the equality holds iff $a = 0$.
- $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$.
:::

::: definition:Inner Product Space
Let $V$ be a vector space over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $\langle \cdot, \cdot \rangle$ be an inner product on $V$. The pair $(V, \langle \cdot, \cdot \rangle)$ is an inner product space.
:::

::: definition:Orthogonality
Let $V$ be an inner product space and $x, y \in V$. The vectors $x$ and $y$ are orthogonal, denoted by $x \perp y$, if $\langle x, y\rangle = 0$.
:::

::: definition:Orthogonal Complement of a Vector
Let $V$ be an inner product space and $x \in V$. The orthogonal complement of $x$ is $x^ \perp := \{y \in V : \langle x,y\rangle = 0\}$.
:::

::: definition:Orthogonal Complement
Let $V$ be an inner product space and $M \subseteq V$. The orthogonal complement of $M$ is $M^ \perp := \{y \in V : \langle x,y\rangle = 0\text{ for any }x \in M\}$.
:::

::: definition:Induced Norm
Let $V$ be an inner product space. The norm induced by the inner product is $\|x\| := \sqrt{\langle x, x\rangle}$ for any $x \in V$.
:::

::: theorem:Cauchy-Schwarz Inequality
Let $V$ be a real or complex inner product space and $a, b \in V$. With the induced norm, $|\langle a, b\rangle| \leq \|a\|\|b\|$. Equality holds iff $a$ and $b$ are linearly dependent.
:::

::: proof
If $a = 0$ or $b = 0$, the equality holds. Assume $a \neq 0$ and write $b = \beta a + \delta$, where $\beta = \frac{\langle a, b\rangle}{\langle a, a\rangle}$ and $\delta = b - \beta a$. Then $\langle a, \delta\rangle = 0$ and $\|b\|^2 = |\beta|^2\|a\|^2 + \|\delta\|^2$. Thus, $|\langle a, b\rangle|^2 = |\beta|^2\|a\|^4 \leq \|a\|^2\|b\|^2$. Equality holds iff $\delta = 0$, i.e., $b = \beta a$.
:::

::: proposition
Let $V$ be a real or complex inner product space. The induced norm satisfies the norm axioms and $\|a + b\| \leq \|a\| + \|b\|$ for any $a, b \in V$.
:::

::: theorem:Parallelogram Identity
Let $V$ be a real or complex inner product space and $a, b \in V$. With the induced norm, $\|a + b\|^2 + \|a - b\|^2 = 2\|a\|^2 + 2\|b\|^2$.
:::

::: definition:Hilbert Space
Let $H$ be a real or complex inner product space. The space is a Hilbert space if it is complete under its induced norm $\|x\| := \sqrt{\langle x, x\rangle}$.
:::

::: proposition
Let $V$ be a finite-dimensional real or complex inner product space. $V$ is a Hilbert space under its induced norm.
:::

::: proposition
Let $H$ be a Hilbert space. The maps $(x,y) \mapsto \langle x,y\rangle$ and $x \mapsto \|x\|$ are continuous in the norm topology.
:::

::: proposition
Let $V$ be an inner product space and $M \subseteq V$. The set $M^ \perp$ is a closed linear subspace of $V$ under the induced norm.
:::

::: definition:Convex Set
Let $V$ be a real or complex vector space and $E \subseteq V$. The set $E$ is convex if $(1 - t)x + ty \in E$ for any $x,y \in E$ and $t \in [0,1]$.
:::

::: proposition
Let $H$ be a Hilbert space and $E \subseteq H$ be a nonempty closed convex set. There exists a unique $z \in E$ s.t. $\|z\| = \underset{x \in E}{\min}\|x\|$.
:::

::: theorem:Orthogonal Projection Theorem
Let $H$ be a Hilbert space and $M \subseteq H$ be a closed linear subspace. For any $x \in H$, there exist unique $Px \in M$ and $Qx \in M^ \perp$ s.t. $x = Px + Qx$. The vectors $Px$ and $Qx$ are the unique nearest points to $x$ in $M$ and $M^ \perp$, respectively. The maps $P,Q : H \to H$ are linear and $\|x\|^2 = \|Px\|^2 + \|Qx\|^2$ for any $x \in H$.
:::

::: corollary
Let $H$ be a Hilbert space and $M \subseteq H$ be a closed linear subspace. If $M \neq H$, then $M^ \perp$ contains a nonzero vector.
:::

::: theorem:Riesz Representation Theorem
Let $H$ be a real or complex Hilbert space and $f \in H^*$. There exists a unique $y \in H$ s.t. $f(x) = \langle y, x\rangle$ for any $x \in H$ and $\|f\|_{H^*} = \|y\|_H$.
:::

::: definition:Riesz Map
Let $H$ be a real or complex Hilbert space. The Riesz map $R_H : H \to H^*$ is defined by $(R_H y)(x) := \langle y, x\rangle$ for any $x, y \in H$.
:::

::: proposition
Let $H$ be a real or complex Hilbert space. The Riesz map $R_H$ is bijective and $\|R_H y\|_{H^*} = \|y\|_H$ for any $y \in H$. It is linear over $\mathbb{R}$ and conjugate-linear over $\mathbb{C}$, with $R_H(\lambda y + z) = \overline{\lambda}R_H y + R_H z$ in the complex case.
:::

::: definition:Adjoint Operator
Let $H$ and $K$ be Hilbert spaces over the same field and $A \in \mathcal{B}(H, K)$. The adjoint operator of $A$ is the unique bounded linear map $A^* : K \to H$ s.t. $\langle Ax, y\rangle_K = \langle x, A^*y\rangle_H$ for any $x \in H$ and $y \in K$.
:::

::: proposition
Let $H$ and $K$ be Hilbert spaces over the same field and $A \in \mathcal{B}(H, K)$. The adjoint exists by the Riesz representation theorem and satisfies $R_H A^* = A' R_K$, or equivalently $A^* = R_H^{-1} A' R_K$.
:::

::: proposition
Let $H$, $K$, and $L$ be Hilbert spaces over the same field $\mathbb{F}$, $A, B \in \mathcal{B}(H, K)$, $C \in \mathcal{B}(K, L)$, and $\alpha \in \mathbb{F}$. $(A + B)^* = A^* + B^*$, $(\alpha A)^* = \overline{\alpha}A^*$, $(CA)^* = A^*C^*$, $(A^*)^* = A$, and $\|A^*\| = \|A\|$. For $\mathbb{F} = \mathbb{R}$, $\overline{\alpha} = \alpha$.
:::

::: definition:Self-Adjoint Operator
Let $H$ be a real or complex Hilbert space and $A \in \mathcal{B}(H, H)$. The operator $A$ is self-adjoint if $A = A^*$.
:::

::: definition:Positive Semidefinite Operator
Let $H$ be a real or complex Hilbert space and $A \in \mathcal{B}(H, H)$ be self-adjoint. The operator $A$ is positive semidefinite, denoted by $A \succeq 0$, if $\langle Ax, x\rangle \geq 0$ for any $x \in H$.
:::

::: note
For a self-adjoint operator $A$ on a complex Hilbert space, $\langle Ax, x\rangle$ is real for every $x$, so the inequality in the definition of positive semidefiniteness is well-defined.
:::

::: definition:Loewner Order
Let $H$ be a real or complex Hilbert space and $A, B \in \mathcal{B}(H, H)$ be self-adjoint. The Loewner order is $A \succeq B$ if $A - B \succeq 0$.
:::

::: note
The Loewner order is a partial order on bounded self-adjoint operators. It is not a total order in general.
:::

## Example
### Real Vector Space
::: definition:$l_{p}$-norm in $\mathbb{R}^{n}$
Let $a \in \mathbb{R}^n$. The $l_{p}$-norm in $\mathbb{R}^{n}$ is $\|a\|_{p} := \left(\sum_{i = 1}^{n}|a_{i}|^{p}\right)^{\frac{1}{p}}$ for $1 \leqslant p < \infty$, and $\|a\|_{\infty} := \underset{1 \leqslant i \leqslant n}{\max}|a_i|$.
:::

::: definition:Standard Inner Product in $\mathbb{R}^{n}$
Let $a,b \in \mathbb{R}^n$. The standard inner product in $\mathbb{R}^{n}$ is $\langle a, b \rangle := a^T b = \sum_{i = 1}^n a_i b_i$.
:::

::: note
The standard inner product makes $\mathbb{R}^n$ a Hilbert space, with induced norm $\|\cdot\|_2$. In the geometric statements below, $\|\cdot\|$ denotes $\|\cdot\|_2$.
:::

::: definition:Outer Product in $\mathbb{R}^{n}$
Let $a,b \in \mathbb{R}^n$. The outer product in $\mathbb{R}^{n}$ is $ab^T$.
:::

::: proposition
Let $a,b \in \mathbb{R}^n$. $\|a + b\|^2 = \|a\|^2 + \|b\|^2$ iff $\langle a, b \rangle = 0$.
:::

::: proposition
Let $a,b \in \mathbb{R}^n$. If $\|a\| = \|b\|$, then $\langle a + b, a - b\rangle = 0$.
::: ^equal-norm-orthogonality

::: proposition
Let $a,b \in \mathbb{R}^n$. If $a \neq 0$, then there exist $\beta \in \mathbb{R}$ and $\delta \in \mathbb{R}^n$ s.t. $b = \beta a + \delta$ and $a^T\delta = 0$, where $\beta = \frac{a^T b}{a^T a}$ and $\delta = b - \beta a$.
:::

::: definition:$\cos \theta$
Let $a,b \in \mathbb{R}^n\setminus\{0\}$. $\cos \theta := \frac{a^T b}{\|a\|\|b\|}$.
:::

::: note
Cauchy-Schwarz inequality ensures that $|\cos \theta| \leq 1$.
:::

::: definition:Dual Norm in $\mathbb{R}^n$
Let $\mathbb{R}^n$ be equipped with a norm $\|\cdot\|$. Every continuous linear functional has the form $f_v(x) = v^T x$ for a unique $v \in \mathbb{R}^n$. Under this identification, the dual norm is expressed as $\|v\|_* := \|f_v\|_{(\mathbb{R}^n)^*} = \underset{\|x\| \leq 1}{\sup}|v^T x| = \underset{\|x\| \leq 1}{\max}|v^T x|$.
:::

::: proposition
Let $p, q \in [1, \infty]$ and $z \in \mathbb{R}^n$. Assume $\frac{1}{p} + \frac{1}{q} = 1$, with $\frac{1}{\infty} := 0$. $\|z\|_{p,*} = \|z\|_q$.
:::

::: proposition
Let $\|\cdot\|$ be a norm on $\mathbb{R}^n$ and $\|\cdot\|_*$ be its dual norm. $|v^T x| \leq \|v\|_*\|x\|$ for any $v, x \in \mathbb{R}^n$.
:::

::: proposition
Let $\|\cdot\|$ be a norm on $\mathbb{R}^n$, $\|\cdot\|_*$ be its dual norm, and $\|\cdot\|_{**}$ be the dual norm of $\|\cdot\|_*$. $\|x\|_{**} = \|x\|$ for any $x \in \mathbb{R}^n$.
:::

::: proposition
Let $A \in \mathbb{R}^{m, n}$. With the standard inner products, the adjoint operator of $A$ is represented by $A^T$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. With the standard inner product, $A$ is self-adjoint iff $A = A^T$.
:::

### Complex Vector Space
::: definition:$l_{p}$-norm in $\mathbb{C}^{n}$
Let $a \in \mathbb{C}^n$. The $l_{p}$-norm in $\mathbb{C}^{n}$ is $\|a\|_{p} := \left(\sum_{i = 1}^{n}|a_{i}|^{p}\right)^{\frac{1}{p}}$ for $1 \leqslant p < \infty$, and $\|a\|_{\infty} := \underset{1 \leqslant i \leqslant n}{\max}|a_i|$.
:::

::: definition:Standard Inner Product in $\mathbb{C}^{n}$
Let $a,b \in \mathbb{C}^n$. The standard inner product in $\mathbb{C}^{n}$ is $\langle a, b \rangle := a^* b = \sum_{i = 1}^n \overline{a_i}b_i$.
:::

::: note
The standard inner product makes $\mathbb{C}^n$ a Hilbert space, with induced norm $\|\cdot\|_2$. In the geometric statements below, $\|\cdot\|$ denotes $\|\cdot\|_2$.
:::

::: definition:Outer Product in $\mathbb{C}^{n}$
Let $a,b \in \mathbb{C}^n$. The outer product in $\mathbb{C}^{n}$ is $ab^*$.
:::

::: proposition
Let $a,b \in \mathbb{C}^n$. If $\langle a, b \rangle = 0$, then $\|a + b\|^{2} = \|a\|^{2} + \|b\|^{2}$.
::: ^complex-orthogonal-pythagorean

::: note
The reverse of [[#^complex-orthogonal-pythagorean|the orthogonal Pythagorean identity]] is incorrect. If $\|a + b\|^{2} = \|a\|^{2} + \|b\|^{2}$, then $\Re(a^{*}b) = \Re(b^{*}a) = 0$.
:::

::: note
[[#^equal-norm-orthogonality|The equal-norm orthogonality statement]] is incorrect in $\mathbb{C}^{n}$. If $\|a\| = \|b\|$, then $\langle a + b, a - b\rangle = 0$ does not always hold.
:::

::: definition:Dual Norm in $\mathbb{C}^n$
Let $\mathbb{C}^n$ be equipped with a norm $\|\cdot\|$. Every continuous complex-linear functional has the form $f_v(x) = v^*x$ for a unique $v \in \mathbb{C}^n$. Under this identification, the dual norm is expressed as $\|v\|_* := \|f_v\|_{(\mathbb{C}^n)^*} = \underset{\|x\| \leq 1}{\sup}|v^*x| = \underset{\|x\| \leq 1}{\max}|v^*x|$.
:::

::: proposition
Let $p, q \in [1, \infty]$ and $z \in \mathbb{C}^n$. Assume $\frac{1}{p} + \frac{1}{q} = 1$, with $\frac{1}{\infty} := 0$. $\|z\|_{p,*} = \|z\|_q$.
:::

::: proposition
Let $A \in \mathbb{C}^{m, n}$. With the standard inner products, the adjoint operator of $A$ is represented by its conjugate transpose $A^* = \overline{A}^{T}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. With the standard inner product, $A$ is self-adjoint iff $A = A^*$, i.e., $A$ is Hermitian.
:::

### Matrix Space
::: definition:Trace Inner Product
Let $X, Y \in \mathbb{R}^{n, k}$. The trace inner product on $\mathbb{R}^{n, k}$ is $\langle X, Y\rangle := \operatorname{tr}(X^T Y) = \sum_{i = 1}^{n}\sum_{j = 1}^{k}X_{ij}Y_{ij}$. For $\mathbb{S}^n := \{X \in \mathbb{R}^{n, n} : X = X^T\}$, the trace inner product is $\langle A, B\rangle = \operatorname{tr}(AB)$ for any $A, B \in \mathbb{S}^n$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$, $B \in \mathbb{R}^{k, n}$, and $C, D \in \mathbb{R}^{n, n}$. $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$, and $\operatorname{tr}(D) = \operatorname{tr}(D^T)$.
:::

::: definition:Complex Trace Inner Product
Let $X, Y \in \mathbb{C}^{n, k}$. The trace inner product on $\mathbb{C}^{n, k}$ is $\langle X, Y\rangle := \operatorname{tr}(X^*Y) = \sum_{i = 1}^n\sum_{j = 1}^k \overline{X_{ij}}Y_{ij}$.
:::

::: proposition
Let $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. The matrix space $\mathbb{F}^{n, k}$ with its trace inner product is a Hilbert space. Its induced norm is the Frobenius norm $\|X\|_F := \left(\sum_{i = 1}^n\sum_{j = 1}^k |X_{ij}|^2\right)^{\frac{1}{2}}$.
:::
