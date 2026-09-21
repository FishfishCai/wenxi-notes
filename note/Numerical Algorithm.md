## Numerical Foundations
### Operation Counts
::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a^T b$ is $2n - 1$.
::: ^dot-product-operation-count

::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a - b$ is $n$.
::: ^vector-subtraction-operation-count

::: proposition
Let $\alpha \in \mathbb{R}$ and $a \in \mathbb{R}^n$. The operation count for $\alpha a$ is $n$.
::: ^scalar-vector-operation-count

::: proposition
Let $p, x \in \mathbb{R}^n$. The operation count for computing $(I - pp^T)x$ is $4n - 1$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $B \in \mathbb{R}^{k, m}$. The operation count for $AB$ is $nm(2k - 1)$.
:::

### Floating Point Arithmetic
::: definition:Idealized Floating Point Number System
Let $\beta, t \in \mathbb{Z}$. Assume the radix satisfies $\beta \geq 2$ and the precision satisfies $t \geq 1$. The idealized floating point system is $F = \{0\} \cup \left\{ x \in \mathbb{R} : x = \pm \frac{m}{\beta^t} \beta^e, \ \beta^{t - 1} \leq m \leq \beta^t - 1, \ e, m \in \mathbb{Z} \right\}$. The fraction (or mantissa) of $x$ is $\pm \frac{m}{\beta^t}$, and $e$ is the exponent.
:::

::: definition:Machine Epsilon
Let $F$ be an idealized floating point system. The machine epsilon is $\varepsilon_{\text{machine}} = \beta^{1 - t}$.
:::

::: proposition
Let $F$ be an idealized floating point system. For any $x \in \mathbb{R}$, there exists $x' \in F$ s.t. $|x - x'| \leq \frac{1}{2}\varepsilon_{\text{machine}} |x|$.
:::

::: definition:Rounding Map
Let $F$ be an idealized floating point system. The rounding map $\mathrm{fl} : \mathbb{R} \to F$ sends each $x \in \mathbb{R}$ to a nearest element of $F$, using a fixed rule to resolve ties. For $A = \mathbb{R}^d$, write $F_A := \mathrm{fl}(A) = F^d$, where $\mathrm{fl}$ acts coordinatewise.
:::

::: definition:Floating Point Operation
Let $F$ be an idealized floating point system, $x, y \in F$, and $* \in \{+, -, \times, \div\}$. Assume $y \neq 0$ when $* = \div$. The floating point operation is $x \circledast y := \mathrm{fl}(x * y)$.
:::

::: theorem:Fundamental Axiom of Floating Point Arithmetic
Let $F$ be an idealized floating point system, $x, y \in F$, and $* \in \{+, -, \times, \div\}$. Assume $y \neq 0$ when $* = \div$. There exists $\delta \in \mathbb{R}$ with $|\delta| \leq \frac{1}{2}\varepsilon_{\text{machine}}$ s.t. $x \circledast y = (x * y)(1 + \delta)$.
:::

### Accuracy
::: definition:Absolute Error
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$ and $\tilde f : F_X \to F_Y$. The absolute error of $\tilde f$ at $x$ is $\|\tilde f(x) - f(x)\|$.
:::

::: definition:Relative Error
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$ and $\tilde f : F_X \to F_Y$. Assume $f(x) \neq 0$. The relative error of $\tilde f$ at $x$ is $\frac{\|\tilde f(x) - f(x)\|}{\|f(x)\|}$.
:::

::: definition:$O(\varepsilon_{\text{machine}})$
Let $X = \mathbb{R}^n$ and $\phi_F, \psi_F : F_X \to [0, \infty)$ be families of functions indexed by idealized floating point systems $F$. The notation $\phi_F = O(\psi_F)$ as $\varepsilon_{\text{machine}} \to 0$ means that there exist $C > 0$ and $\varepsilon_0 > 0$ s.t. $\phi_F(x) \leq C\psi_F(x)$ for any $F$ with $\varepsilon_{\text{machine}} < \varepsilon_0$ and any $x \in F_X$. 
:::

::: definition:Accuracy
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$, and $\tilde f : F_X \to F_Y$. $\tilde f$ is accurate for $f$ if there exist $C > 0$ and $\varepsilon_0 > 0$ s.t. $\|\tilde f(x) - f(x)\| \leq C\varepsilon_{\text{machine}}\|f(x)\|$ for any $F$ with $\varepsilon_{\text{machine}} < \varepsilon_0$ and any $x \in F_X$.
::: ^accuracy

### Conditioning
::: definition:Condition Number
Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $x \in \mathbb{R}^n$. Assume $f$ is continuous. The condition number of $f$ at $x$ is $\hat{\kappa}(x) := \underset{\Delta \to 0,\ \Delta > 0}{\lim} \underset{0 < \|\Delta x\| \leq \Delta}{\sup} \frac{\|f(x + \Delta x) - f(x)\|}{\|\Delta x\|}$.
::: ^condition-number

::: note
For [[#^condition-number|Condition Number]], if $f$ is differentiable at $x$, then $\hat{\kappa}(x) = \|J_f(x)\|$.
:::

::: definition:Relative Condition Number
Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $x \in \mathbb{R}^n$. Assume $f$ is continuous, $x \neq 0$, and $f(x) \neq 0$. The relative condition number of $f$ at $x$ is $\kappa(x) := \underset{\Delta \to 0,\ \Delta > 0}{\lim} \underset{0 < \|\Delta x\| \leq \Delta}{\sup} \frac{\frac{\|f(x + \Delta x) - f(x)\|}{\|f(x)\|}}{\frac{\|\Delta x\|}{\|x\|}}$.
::: ^relative-condition-number

::: note
For [[#^relative-condition-number|Relative Condition Number]], if $f$ is differentiable at $x$, then $\kappa(x) = \frac{\|J_f(x)\|\|x\|}{\|f(x)\|}$.
:::

::: definition:Condition Number of Matrix
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ is full-rank. The condition number of $A$ is $\kappa(A) := \|A\|\|A^{+}\|$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A$ is nonsingular. $\kappa_2(A) := \|A\|_2\|A^{-1}\|_2 = \frac{\sigma_1(A)}{\sigma_n(A)}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $\| \cdot \|$ is the spectral norm and each entry of $A$ is i.i.d. normal with $\mu = 0$ and $\sigma^2 = 1$. $\mathbb{E}[\log \kappa(A)] \sim \log n$ as $n \to \infty$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $x, b \in \mathbb{R}^n$. Assume $A$ is nonsingular, $Ax = b$, and $b \neq 0$. Given $A$, the condition number of computing $b$ with $Ax = b$ is $\kappa(x) = \|A\|\frac{\|x\|}{\|b\|} \leq \|A\|\|A^{-1}\|$. If $\| \cdot \| = \| \cdot \|_2$, then equality holds for any $x$ that is a multiple of a right singular vector of $A$ corresponding to the minimal singular value $\sigma_n$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $x, b \in \mathbb{R}^n$. Assume $A$ is nonsingular, $Ax = b$, and $b \neq 0$. Given $A$, the condition number of computing $x$ with $Ax = b$ is $\kappa(b) = \|A^{-1}\|\frac{\|b\|}{\|x\|} \leq \|A\|\|A^{-1}\|$. If $\| \cdot \| = \| \cdot \|_2$, then equality holds for any $b$ that is a multiple of a left singular vector of $A$ corresponding to the maximal singular value $\sigma_1$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $x, b \in \mathbb{R}^n$. Assume $A$ is nonsingular, $Ax = b$, and $b \neq 0$. Given $b$, the condition number of computing $x$ with $x = A^{-1}b$ is $\kappa(A) = \|A\|\|A^{-1}\|$.
:::

### Stability
::: definition:Stability
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$, and $\tilde f : F_X \to F_Y$. $\tilde f$ is stable for $f$ if there exist $C_1, C_2 > 0$ and $\varepsilon_0 > 0$ s.t. for any $F$ with $\varepsilon_{\text{machine}} < \varepsilon_0$ and any $x \in F_X$, there exists $\tilde x \in X$ satisfying $\|\tilde x - x\| \leq C_1\varepsilon_{\text{machine}}\|x\|$ and $\|\tilde f(x) - f(\tilde x)\| \leq C_2\varepsilon_{\text{machine}}\|f(\tilde x)\|$.
::: ^stability

::: definition:Backward Stability
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$, and $\tilde f : F_X \to F_Y$. $\tilde f$ is backward stable for $f$ if there exist $C > 0$ and $\varepsilon_0 > 0$ s.t. for any $F$ with $\varepsilon_{\text{machine}} < \varepsilon_0$ and any $x \in F_X$, there exists $\tilde x \in X$ satisfying $\|\tilde x - x\| \leq C\varepsilon_{\text{machine}}\|x\|$ and $\tilde f(x) = f(\tilde x)$.
::: ^backward-stability

::: proposition
Let $* \in \{+, -, \times, \div\}$. For each idealized floating point system $F$, set $f_*(x, y) := x * y$ and $\tilde f_{F, *}(x, y) := \mathrm{fl}(x) \circledast \mathrm{fl}(y)$ on their natural domains. With the Euclidean norm on $\mathbb{R}^2$, the family $\tilde f_{F, *}$ is backward stable for $f_*$.
:::

::: note
For all sufficiently small $\varepsilon_{\text{machine}}$, [[#^accuracy|Accuracy]] implies that $f(x) = 0$ gives $\tilde f(x) = f(x)$. [[#^stability|Stability]] implies that $x = 0$ gives $\tilde x = x$ and that $f(\tilde x) = 0$ gives $\tilde f(x) = f(\tilde x)$. [[#^backward-stability|Backward Stability]] implies that $x = 0$ gives $\tilde x = x$.
:::

::: note
For fixed $n$ and $m$, [[#^accuracy|Accuracy]], [[#^stability|Stability]] and [[#^backward-stability|Backward Stability]] are unchanged if the Euclidean norms are replaced by any other norms, since all norms on finite-dimensional real spaces are equivalent.
:::

::: proposition
Let $F$ be an idealized floating point system, $X = \mathbb{R}^n$, $Y = \mathbb{R}^m$, $f : X \to Y$, $\tilde f : F_X \to F_Y$, and $x \in F_X$. Assume $f$ is differentiable at $x$, $x \neq 0$, $f(x) \neq 0$, and its relative condition number is finite and positive. Set $\kappa(x)$ to be the relative condition number of $f$ at $x$. If $\tilde f$ is backward stable for $f$, then $\frac{\|\tilde f(x) - f(x)\|}{\|f(x)\|} = O(\kappa(x) \varepsilon_{\text{machine}})$ as $\varepsilon_{\text{machine}} \to 0$ with $x$ fixed.
:::

::: proof
By the definition of backward stability, $\tilde f(x) = f(\tilde x)$ for some $\tilde x \in X$ satisfying $\frac{\|\tilde x - x\|}{\|x\|} = O(\varepsilon_{\text{machine}})$. By the definition of $\kappa(x)$, this implies $\frac{\|\tilde f(x) - f(x)\|}{\|f(x)\|} \le (\kappa(x) + o(1)) \frac{\|\tilde x - x\|}{\|x\|}$, where $o(1)$ denotes a quantity that converges to zero as $\varepsilon_{\text{machine}} \to 0$. For fixed $x$, combining these gives the proof.
:::

## Matrix Factorizations
### LU Factorization
::: theorem:Gaussian Elimination
Let $A = \left(\begin{matrix} a_{11} & a_{12} & \cdots & a_{1k} \\ a_{21} & a_{22} & \cdots & a_{2k} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nk} \end{matrix}\right) \in \mathbb{R}^{n, k}$. Assume $n \ge k$ and every pivot encountered during elimination is nonzero. Set $A = A_{0}$ and, at the $i$-th iteration, compute in order
$$
\begin{align*}
\ell_{ji}& = \frac{(A_{i - 1})_{ji}}{(A_{i - 1})_{ii}} \text{ for }i < j \leqslant n\\
L_{i}& = \left(\begin{matrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & -\ell_{i + 1, i} & 1 & \cdots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & -\ell_{ni} & 0 & \cdots & 1 \end{matrix}\right)\\
A_{i}& = L_{i}A_{i - 1}
\end{align*}
$$
Set $L = L_1^{-1}L_2^{-1}\cdots L_k^{-1}$ and $U = A_k$. $L$ is unit lower triangular, $U$ is upper trapezoidal, and $A = LU$.
::: ^gaussian-elimination

::: note
For [[#^gaussian-elimination|Gaussian Elimination]], $L_{i}^{-1} = \left(\begin{matrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & \ell_{i + 1, i} & 1 & \cdots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \ell_{ni} & 0 & \cdots & 1 \end{matrix}\right)$ and $L \in \mathbb{R}^{n, n}$ has entries $L_{ij} = 1$ if $i = j$, $L_{ij} = \ell_{ij}$ if $1 \leq j \leq k$ and $i > j$, and $L_{ij} = 0$ otherwise.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume the indicated elimination completes without breakdown. The operation count of [[#^gaussian-elimination|Gaussian Elimination]] is $\sim \frac{2}{3}n^{3}$.
:::

::: definition:Permutation Matrix
Let $P \in \mathbb{R}^{n, n}$. The matrix $P$ is a permutation matrix if it is obtained from the identity by permuting rows or columns.
:::

::: theorem:LU Factorization with Partial Pivoting
Let $A \in \mathbb{C}^{n, n}$. There exist a permutation matrix $P \in \mathbb{R}^{n, n}$, a unit lower-triangular matrix $L \in \mathbb{C}^{n, n}$ with $|\ell_{ij}| \le 1$, and an upper-triangular matrix $U \in \mathbb{C}^{n, n}$ s.t. $PA = LU$.
::: ^lu-partial-pivoting

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume the indicated elimination completes without breakdown. The operation count of [[#^lu-partial-pivoting|LU Factorization with Partial Pivoting]] is $\sim \frac{2}{3}n^{3}$.
:::

::: definition:Growth Factor
Let $A \in \mathbb{C}^{n, n}$. Assume $A \neq 0$ and Gaussian elimination completes. Set $U$ to be its upper-triangular factor. The growth factor for $A$ is $\rho = \frac{\underset{i, j}{\max} |u_{ij}|}{\underset{i, j}{\max} |a_{ij}|}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume $A$ is nonsingular and the factorization $A = LU$ is computed by Gaussian elimination without pivoting on a computer satisfying the axioms of floating point arithmetic. If $A$ has an LU factorization and the factorization completes successfully in floating point arithmetic, then the computed matrices $\tilde{L}$ and $\tilde{U}$ satisfy $\tilde{L}\tilde{U} = A + \delta A$ and $\frac{\|\delta A\|}{\|L\|\|U\|} = O(\varepsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume the factorization $PA = LU$ is computed by Gaussian elimination with partial pivoting on a computer satisfying the axioms of floating point arithmetic. The computed matrices $\tilde{P}$, $\tilde{L}$, and $\tilde{U}$ satisfy $\tilde{L}\tilde{U} = \tilde{P}A + \delta A$ and $\frac{\|\delta A\|}{\|A\|} = O(\rho \varepsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$, where $\rho$ is the growth factor for $A$. If $|\ell_{ij}| < 1$ for each $i > j$, implying that there are no ties in the selection of pivots in exact arithmetic, then $\tilde{P} = P$ for all sufficiently small $\varepsilon_{\text{machine}}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. For Gaussian elimination with partial pivoting applied to $A$, the growth factor satisfies $\rho \le 2^{n - 1}$.
:::

::: proposition
Gaussian elimination with partial pivoting is backward stable.
:::

::: note
For the above, backward stability holds in the sense that for each fixed dimension $n$, the bound $\frac{\|\delta A\|}{\|A\|} = O(\varepsilon_{\text{machine}})$ applies uniformly to all matrices of that dimension, but the constant involves $2^{n - 1}$. In practice, large growth factors are exponentially rare among random matrices, and Gaussian elimination with partial pivoting is utterly stable in practice.
:::

### Cholesky Factorizations
::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A$ is symmetric positive definite. The operation count of [[Matrix#^cholesky-factorization|Cholesky Factorization]] is $\sim \frac{1}{3}n^{3}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A$ is symmetric positive definite and [[Matrix#^cholesky-factorization|Cholesky factorization]] is computed on a computer satisfying the axioms of floating point arithmetic. For all sufficiently small $\varepsilon_{\text{machine}}$, the algorithm completes and its computed factor $\tilde R$ satisfies $\tilde R^T \tilde R = A + \delta A$ with $\frac{\|\delta A\|_2}{\|A\|_2} = O(\varepsilon_{\text{machine}})$ for some $\delta A \in \mathbb{R}^{n, n}$.
:::

### QR Factorization
::: theorem:Classical Gram–Schmidt Process
Let $a_1, a_2, \ldots, a_k \in \mathbb{R}^n$. If $a_1, a_2, \ldots, a_k$ are linearly independent, then there exists an orthonormal set $v_1, v_2, \ldots, v_k$ given by
$$
\begin{align*}
v_1 & = \frac{a_1}{\|a_1\|}, \\
v_i & = \frac{\bigl(I - v_1 v_1^T - \cdots - v_{i - 1} v_{i - 1}^T\bigr)a_i}
{\left\|\bigl(I - v_1 v_1^T - \cdots - v_{i - 1} v_{i - 1}^T\bigr)a_i\right\|}, \qquad i = 2, \dots, k.
\end{align*}
$$
::: ^classical-gram-schmidt-process

::: theorem:Gram–Schmidt QR Factorization
Let $A = [a_1\; a_2\; \cdots\; a_k] \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. Set $v_1, v_2, \ldots, v_k$ to be the orthonormal set constructed from $a_1, a_2, \ldots, a_k$ via the classical Gram–Schmidt process. $a_1 = \|a_1\|v_1$ and $a_i = \sum_{j = 1}^{i - 1}\langle a_i, v_j\rangle v_j + \left\|\bigl(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\bigr)a_i\right\|v_i$ for $i = 2, \ldots, k$. That is, $A = QR := [v_1\; v_2\; \cdots\; v_k] \begin{pmatrix} \|a_1\| & \langle a_2, v_1\rangle & \cdots & \langle a_k, v_1\rangle \\ 0 & \left\|\bigl(I - v_1 v_1^T\bigr)a_2\right\| & \cdots & \langle a_k, v_2\rangle \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \left\|\bigl(I - v_1 v_1^T - \cdots - v_{k - 1} v_{k - 1}^T\bigr)a_k\right\| \end{pmatrix}$.
::: ^gram-schmidt-qr

::: note
For [[#^gram-schmidt-qr|Gram–Schmidt QR Factorization]], it can also be formed as $AR_{1}R_{2}\cdots R_{k} = Q$, where $R_i = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\ \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\ 0 & 0 & \cdots & 0 & \frac{1}{\left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\|} & -\frac{\left\langle \left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i, a_{i + 1}\right\rangle}{\left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\|^{2}} & \cdots & -\frac{\left\langle \left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i, a_{k}\right\rangle}{\left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\|^{2}} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\ \vdots & \vdots &  & \vdots & \vdots &  & \ddots \end{pmatrix}$. The vector $v_{j}$ is the $j$-th column of $AR_{1}R_{2}\cdots R_{i - 1}$ for $j < i$. Its inverse is $R_{i}^{-1} = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0\\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0\\ \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots\\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0\\ 0 & 0 & \cdots & 0 & \left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\| & \frac{\left\langle \left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i, a_{i + 1}\right\rangle}{\left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\|} & \cdots & \frac{\left\langle \left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i, a_{k}\right\rangle}{\left\|\left(I - v_1v_1^T - \cdots - v_{i - 1}v_{i - 1}^T\right)a_i\right\|} \\ 0 & 0 & \cdots & 0 & 0 & 1 & \cdots\\ \vdots & \vdots &  & \vdots & \vdots &  & \ddots \end{pmatrix}$. Thus $R = R_{k}^{-1}R_{k - 1}^{-1}\cdots R_{1}^{-1}$ is an upper triangular matrix.
:::

::: theorem:Modified Gram–Schmidt Process
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. Set $z_j = A_{:,j}$ for $1 \le j \le k$ and $R = 0 \in \mathbb{R}^{k, k}$. For $i = 1,\ldots,k$, compute
$$
\begin{aligned}
r_{ii} &\leftarrow \|z_i\|_2,\qquad q_i \leftarrow \frac{z_i}{r_{ii}},\\
r_{ij} &\leftarrow q_i^Tz_j,\qquad z_j \leftarrow z_j - r_{ij}q_i\quad(j = i + 1,\ldots,k).
\end{aligned}
$$
The output $Q = (q_1\ \cdots\ q_k)$ satisfies $A = QR$ and $Q^TQ = I$ in exact arithmetic.
::: ^modified-gram-schmidt

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. The operation count of [[#^modified-gram-schmidt|Modified Gram–Schmidt Process]] is $\sim 2nk^{2}$.
:::

::: definition:Householder Reflection Matrix
Let $v \in \mathbb{R}^n$. Assume $\|v\|_2 = 1$. The Householder reflection matrix associated with $v$ is $H := I - 2vv^T$.
::: ^householder-reflection

::: note
Let $a, b \in \mathbb{R}^n$. Assume $a \neq b$ and $\|a\|_2 = \|b\|_2$. Set $v = \frac{a - b}{\|a - b\|_2}$ and $H = I - 2vv^T$. $Ha = b$ and $Hb = a$.
:::

::: note
For [[#^householder-reflection|Householder Reflection Matrix]], the Householder reflection matrix is an orthogonal matrix.
:::

::: theorem:Householder QR Factorization
Let $A = [a_1, a_2, \cdots, a_k] \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. Set $A_0 = A$ and, at the $i$-th step, use $\mathrm{sign}(0) = 1$ and compute in order
$$
\begin{align*}
\hat{a}_{i}& = (A_{i - 1})_{i:n,i} \in \mathbb{R}^{n - i + 1}\\
e_i& = (1, 0, \dots, 0)^T \in \mathbb{R}^{n - i + 1}\\
b_{i}& = -\mathrm{sign}((\hat a_i)_1)\|\hat a_i\|e_i \in \mathbb{R}^{n - i + 1}\\
v_{i}& = \frac{\hat a_i - b_i}{\|\hat a_i - b_i\|} \in \mathbb{R}^{n - i + 1}\\
\hat H_i& = I - 2v_{i}v_{i}^T \in \mathbb{R}^{n - i + 1, n - i + 1}\\
H_{i} & = \begin{bmatrix} I_{i - 1} & 0 \\ 0 & \hat H_{i} \end{bmatrix} \in \mathbb{R}^{n, n}\\
A_{i}& = H_iA_{i - 1}
\end{align*}
$$
Set $R = A_k$ and $Q = H_1H_2\cdots H_k$. $R$ is upper trapezoidal, $Q$ is orthogonal, and $A = QR$.
::: ^householder-qr

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $A$ has full column rank. The operation count of [[#^householder-qr|Householder QR Factorization]] is approximately $\sum_{j = 1}^{k}4(n - j + 1)(k - j + 1) \sim 2nk^{2} - \frac{2}{3}k^{3}$.
:::

::: proposition
[[#^householder-qr|Householder QR Factorization]] is backward stable.
::: ^householder-qr-backward-stability

### Least Squares
::: definition:Least Square via Normal Equations
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank. Form $A^T A$ and $A^T b$, compute the Cholesky factorization $A^T A = R^T R$, solve $R^T w = A^T b$ for $w$, and solve $R x = w$ for $x$. The resulting $x$ is the unique minimizer of $\|b - Ax\|_2$.
::: ^least-square-normal-equations

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank and real arithmetic is used. The computation of $A^T A$ is $n k^2$ and the computation of the Cholesky factorization is $\frac{1}{3} k^3$. The computation of [[#^least-square-normal-equations|Least Square via Normal Equations]] is approximately $n k^2 + \frac{1}{3} k^3$.
:::

::: definition:Least Square via QR Factorization
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank. Compute the reduced QR factorization $A = \hat{Q} \hat{R}$, compute the vector $\hat{Q}^T b$, and solve the upper-triangular system $\hat{R} x = \hat{Q}^T b$ for $x$. The resulting $x$ is the unique minimizer of $\|b - Ax\|_2$.
::: ^least-square-qr

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank and real arithmetic is used. The computation of [[#^least-square-qr|Least Square via QR Factorization]] is approximately $2 n k^2 - \frac{2}{3} k^3$.
:::

::: definition:Least Square via SVD
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank. Compute the reduced SVD $A = \hat{U} \hat{\Sigma} V^T$, compute the vector $\hat{U}^T b$, solve the diagonal system $\hat{\Sigma} w = \hat{U}^T b$ for $w$, and set $x = V w$. The resulting $x$ is the unique minimizer of $\|b - Ax\|_2$.
::: ^least-square-svd

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank and real arithmetic is used. The computation of [[#^least-square-svd|Least Square via SVD]] is approximately $2 n k^2 + 11 k^3$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^n$. Assume $A$ has full column rank and [[#^least-square-qr|least squares via QR factorization]] is implemented using Householder reflections on a computer satisfying the axioms of floating point arithmetic. The algorithm is backward stable: its computed solution $\tilde x$ minimizes $\|b - (A + \delta A)x\|_2$ for some $\delta A \in \mathbb{R}^{n, k}$ satisfying $\frac{\|\delta A\|_2}{\|A\|_2} = O(\varepsilon_{\text{machine}})$.
:::

::: proposition
Let $A, \Delta A \in \mathbb{R}^{n, k}$, $b, \Delta b \in \mathbb{R}^n$, $x, y \in \mathbb{R}^k$, and $\varepsilon > 0$. Assume $A$ has full column rank, $x \neq 0$, and $\varepsilon \kappa_2(A) < 1$. If $x$ minimizes $\|b - Ax\|_2$, $y$ minimizes $\|b + \Delta b - (A + \Delta A) y\|_2$, $\|\Delta A\|_2 < \varepsilon \|A\|_2$ and $\|\Delta b\|_2 < \varepsilon \|b\|_2$, then $\frac{\|y - x\|_2}{\|x\|_2} \le \frac{2 \varepsilon \kappa_2(A)}{1 - \varepsilon \kappa_2(A)} + \frac{\varepsilon \kappa_2(A)(\kappa_2(A) + 1)}{1 - \varepsilon \kappa_2(A)} \frac{\|b - Ax\|_2}{\|A\|_2 \|x\|_2}$.
:::

## Eigenvalue and SVD Algorithms
### Eigenvalue Algorithms
::: definition:Upper-Hessenberg Matrix
Let $H \in \mathbb{C}^{n, n}$. The matrix $H$ is an upper-Hessenberg matrix if $h_{ij} = 0$ for any $i > j + 1$.
:::

::: definition:Tridiagonal Matrix
Let $T \in \mathbb{C}^{n, n}$. The matrix $T$ is a tridiagonal matrix if $t_{ij} = 0$ for any $|i - j| > 1$.
:::

::: theorem:Hessenberg Reduction
Let $A \in \mathbb{C}^{n, n}$. Set $H = A$ and $\operatorname{phase}(z) = \frac{z}{|z|}$ for $z \neq 0$, with $\operatorname{phase}(0) = 1$. For $i = 1,\ldots,n - 2$, set $x = H_{i + 1:n,i}$. If $x = 0$, set $Q_i = I$ and skip the updates. Otherwise, compute
$$
\begin{aligned}
v &\leftarrow x + \operatorname{phase}(x_1)\|x\|_2e_1,\qquad v \leftarrow \frac{v}{\|v\|_2},\\
H_{i + 1:n,i:n} &\leftarrow H_{i + 1:n,i:n} - 2v(v^HH_{i + 1:n,i:n}),\\
H_{:,i + 1:n} &\leftarrow H_{:,i + 1:n} - 2(H_{:,i + 1:n}v)v^H,\\
Q_i &\leftarrow \operatorname{diag}(I_i,I - 2vv^H).
\end{aligned}
$$
Store the reflection vectors. In exact arithmetic, $Q = Q_1\cdots Q_{n - 2}$ satisfies $Q^HAQ = H$, and $H$ is upper-Hessenberg. If $A = A^H$, then $H$ is tridiagonal. For $n \le 2$, take $Q = I$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Householder Hessenberg reduction costs $\sim \frac{10}{3}n^3$ operations. If $A$ is Hermitian, then tridiagonal reduction exploiting Hermitian symmetry costs $\sim \frac{4}{3}n^3$ operations.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume $A \neq 0$ and Householder Hessenberg reduction is performed in the standard floating point model. Set $\tilde H$ to be the computed factor and $\tilde Q$ the exact unitary product represented by the computed reflectors. There exists $\delta A$ s.t. $\tilde Q\tilde H\tilde Q^H = A + \delta A$ and $\frac{\|\delta A\|_2}{\|A\|_2} = O(\varepsilon_{\text{machine}})$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $v_0 \in \mathbb{R}^n$. Assume $n \geq 2$, $A$ is symmetric with orthonormal eigenpairs $(\lambda_j, q_j)$ ordered by $|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|$, $\|v_0\|_2 = 1$, and $q_1^T v_0 \neq 0$. Set $c = \left|\frac{\lambda_2}{\lambda_1}\right|$, $v_k = \frac{Av_{k - 1}}{\|Av_{k - 1}\|_2}$, and $\rho_k = r(v_k)$. Power iteration satisfies $\|v_k - (\pm q_1)\|_2 = O(c^k)$ and $|\rho_k - \lambda_1| = O(c^{2k})$ as $k \to \infty$, with signs chosen at each step.
:::

::: proof
$v_{0} = a_1q_1 + a_2q_2 + \cdots + a_nq_n$. Since $v_{k}$ is a multiple of $A^kv_{0}$, $v_{k} = c_k\lambda_1^k(a_1q_1 + a_2(\frac{\lambda_2}{\lambda_1})^kq_2 + \cdots + a_n(\frac{\lambda_n}{\lambda_1})^kq_n)$. Since $a_1 = q_1^{T}v_{0} \neq 0$, the first equation follows. The second follows from this and $r(q_1) - r(x) = O(\|x - q_1\|_2^2)$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$, $\mu \in \mathbb{R}$, and $v_0 \in \mathbb{R}^n$. Assume $n \geq 2$, $A$ is symmetric with orthonormal eigenpairs $(\lambda_j, q_j)$, $\mu$ is not an eigenvalue, $\|v_0\|_2 = 1$, and $q_J^T v_0 \neq 0$, where $\lambda_J$ is simple and uniquely closest to $\mu$ and $\lambda_K$ is second closest. Set $c = \left|\frac{\mu - \lambda_J}{\mu - \lambda_K}\right|$, $(A - \mu I)w_k = v_{k - 1}$, $v_k = \frac{w_k}{\|w_k\|_2}$, and $\rho_k = r(v_k)$. Inverse iteration satisfies $\|v_k - (\pm q_J)\|_2 = O(c^k)$ and $|\rho_k - \lambda_J| = O(c^{2k})$ as $k \to \infty$, with signs chosen at each step.
::: ^inverse-iteration-convergence

::: definition:Rayleigh Quotient Iteration
Let $A \in \mathbb{R}^{n, n}$ and $v_0 \in \mathbb{R}^n$. Assume $A = A^T$ and $\|v_0\|_2 = 1$. Set $\rho_0 = r(v_0)$. Rayleigh quotient iteration uses
$$
(A - \rho_k I)w_{k + 1} = v_k,\qquad
v_{k + 1} = \frac{w_{k + 1}}{\|w_{k + 1}\|_2},\qquad
\rho_{k + 1} = r(v_{k + 1})
$$
for $k \geq 0$. The iteration stops if $Av_k = \rho_k v_k$. Otherwise, the next step requires $A - \rho_k I$ to be nonsingular.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $v_0 \in \mathbb{R}^n$. Assume $A = A^T$ and $\|v_0\|_2 = 1$. Set $v_k$ and $\rho_k$ to be the Rayleigh quotient iterates. The iteration converges to an eigenpair for almost every starting unit vector. If $\lambda_J$ is a simple eigenvalue with unit eigenvector $q_J$ and $v_0$ is sufficiently close to $q_J$, then convergence is ultimately cubic: $\|v_{k + 1} - (\pm q_J)\|_2 = O(\|v_k - (\pm q_J)\|_2^3)$ and $|\rho_{k + 1} - \lambda_J| = O(|\rho_k - \lambda_J|^3)$ as $k \to \infty$, with signs chosen at each step. Finite termination is included.
:::

::: proof
For a simple $\lambda_J$, if $\|v_{k} - q_J\| \le \epsilon$ for sufficiently small $\epsilon$, the Rayleigh quotient satisfies $|\rho_k - \lambda_J| = O(\epsilon^2)$ by the quadratic accuracy of the Rayleigh quotient. By the inverse-iteration estimate in [[#^inverse-iteration-convergence|inverse iteration]], one step of inverse iteration with shift $\mu = \rho_k$ gives $\|v_{k + 1} - ( \pm q_J)\| = O(|\rho_k - \lambda_J| \cdot \|v_{k} - ( \pm q_J)\|) = O(\epsilon^3)$. The constants are uniform near $\lambda_J$ and $q_J$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $V_0 \in \mathbb{R}^{n, m}$. Assume $1 \leq m < n$, $A$ is symmetric with orthonormal eigenpairs $(\lambda_j, q_j)$ ordered by $|\lambda_1| > \cdots > |\lambda_m| > |\lambda_{m + 1}| \geq \cdots \geq |\lambda_n|$, and all leading principal minors of $[q_1\;\cdots\;q_m]^T V_0$ are nonzero. Set $V_0 = \hat Q_0R_0$, $A\hat Q_{t - 1} = \hat Q_tR_t$ by reduced QR factorization, $q_{j,t} = (\hat Q_t)_{:,j}$, and $c = \underset{1 \leq j \leq m}{\max}\left|\frac{\lambda_{j + 1}}{\lambda_j}\right|$. Simultaneous iteration satisfies $\|q_{j,t} - q_j\|_2 = O(c^t)$ for $1 \leq j \leq m$ as $t \to \infty$, after adjusting column signs.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Set $A_0 = A$, $A_{k - 1} = U_kR_k$ by QR factorization, $A_k = R_kU_k$, $\bar Q_k = U_1\cdots U_k$, and $\bar R_k = R_k\cdots R_1$, with $\bar Q_0 = \bar R_0 = I$. Pure QR iteration is equivalent to simultaneous iteration starting from $I$, with $A^k = \bar Q_k\bar R_k$ and $A_k = \bar Q_k^T A\bar Q_k$.
:::

::: proof
By induction on $k$. For $k = 0$, $A^0 = I = \bar Q_0\bar R_0$ and $A_0 = A$. For $k \ge 1$, $A\bar Q_{k - 1} = \bar Q_{k - 1}A_{k - 1} = \bar Q_{k - 1}U_kR_k = \bar Q_kR_k$. Thus $A^k = A\bar Q_{k - 1}\bar R_{k - 1} = \bar Q_kR_k\bar R_{k - 1} = \bar Q_k\bar R_k$, which is also the factorization generated by simultaneous iteration. Finally, $A_k = U_k^T A_{k - 1}U_k = \bar Q_k^T A\bar Q_k$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$, the eigenvalues satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$, and the eigenvector matrix $Q$ of $A$ has all nonzero leading principal minors. Set $A_k$ and $\bar Q_k$ to be the pure QR iterates and accumulated orthogonal factors starting from $A_0 = A$. $A_{k}$ converges linearly with constant $\underset{1 \le j < n}{\max} \frac{|\lambda_{j + 1}|}{|\lambda_j|}$ to $\mathrm{diag}(\lambda_1, \ldots, \lambda_n)$, and $\bar Q_k$ (with the signs of its columns adjusted as necessary) converges at the same rate to $Q$.
:::

::: definition:Shifted QR Algorithm
Let $T \in \mathbb{R}^{n, n}$ and $\tau > 0$. Assume $T = T^T$ and $T$ is tridiagonal. Set $A_0 = T$ and $Q_0 = I$. On each active block, choose a real shift $\mu_k$ and compute
$$
\begin{aligned}
A_{k - 1} - \mu_kI &= U_kR_k,\\
A_k &\leftarrow R_kU_k + \mu_kI,\\
Q_k &\leftarrow Q_{k - 1}U_k.
\end{aligned}
$$
Here $U_kR_k$ is a QR factorization, and each block transformation is embedded in the identity when updating $Q_k$. Set $(A_k)_{j + 1,j} = (A_k)_{j,j + 1} = 0$ if $|(A_k)_{j + 1,j}| \le \tau(|(A_k)_{jj}| + |(A_k)_{j + 1,j + 1}|)$, and split at these entries. Stop when all blocks have size one. The diagonal entries and columns of $Q_k$ approximate the eigenvalues and eigenvectors of $T$. If $T = Q_H^TAQ_H$, the eigenvectors of $A$ are approximated by the columns of $Q_HQ_k$.
:::

::: definition:Wilkinson Shift
Let $A_k \in \mathbb{R}^{n, n}$. Assume $n \geq 2$ and $A_k = A_k^T$. Set $B = \begin{pmatrix} a & b \\ b & d \end{pmatrix}$ to be the trailing principal submatrix of order two and $\delta = \frac{a - d}{2}$. The Wilkinson shift is the eigenvalue of $B$ nearest to $d$, choosing either eigenvalue in a tie. If $b \neq 0$, then it is given by $\mu = d - \frac{\operatorname{sign}(\delta)b^2}{|\delta| + \sqrt{\delta^2 + b^2}}$, with $\operatorname{sign}(0) = 1$. If $b = 0$, then $\mu = d$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and $A$ is tridiagonal. In exact arithmetic, shifted QR iteration with the Wilkinson shift and deflation converges. For each unreduced active block, convergence of its trailing subdiagonal entry to zero is at least quadratic and is generically cubic.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A \neq 0$ is symmetric tridiagonal and shifted QR diagonalization is performed in the standard floating point model with deflation tolerance $\tau = O(\varepsilon_{\text{machine}})$. Set $\tilde\Lambda$ to be the computed diagonal factor and $\tilde Q$ the exact orthogonal product represented by the computed rotations or reflectors. There exists $\delta A$ s.t. $\tilde Q\tilde\Lambda\tilde Q^T = A + \delta A$ and $\frac{\|\delta A\|_2}{\|A\|_2} = O(\varepsilon_{\text{machine}})$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A \neq 0$ is symmetric and tridiagonal reduction followed by shifted QR is performed in the standard floating point model with deflation tolerance $\tau = O(\varepsilon_{\text{machine}})$. Its exact and computed eigenvalues, ordered increasingly, satisfy $\frac{|\tilde\lambda_j - \lambda_j|}{\|A\|_2} = O(\varepsilon_{\text{machine}})$ for $j = 1, \ldots, n$.
:::

::: definition:Jacobi Algorithm
Let $A \in \mathbb{R}^{n, n}$ and $\tau > 0$. Assume $A = A^T$. Set $B = A$ and $Q = I$. Sweep cyclically through $(p,q) = (1,2),(1,3),\ldots,(n - 1,n)$. For each pair, set $a = B_{pp}$, $b = B_{qq}$, $d = B_{pq}$, and choose $\theta \in [-\frac{\pi}{4},\frac{\pi}{4}]$ satisfying $(b - a)\sin(2\theta) = 2d\cos(2\theta)$, with $\theta = 0$ if $d = 0$. The Jacobi rotation $J$ equals the identity except for $J_{\{p,q\},\{p,q\}} = \begin{pmatrix}\cos\theta & \sin\theta\\-\sin\theta & \cos\theta\end{pmatrix}$. Update
$$
B \leftarrow J^TBJ,\qquad Q \leftarrow QJ.
$$
Stop when $\bigl(\sum_{p \neq q}|B_{pq}|^2\bigr)^{\frac{1}{2}} \le \tau\|A\|_F$. The diagonal entries of $B$ and columns of $Q$ approximate the eigenvalues and eigenvectors of $A$.
:::

::: definition:Irreducible Tridiagonal Matrix
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and $A$ is tridiagonal. The matrix $A$ is an irreducible tridiagonal matrix if $A_{i + 1, i} \neq 0$ for any $i \in \{1, \ldots, n - 1\}$.
:::

::: theorem:Eigenvalue Interlacing
Let $A \in \mathbb{R}^{n, n}$. Assume $A$ is symmetric, tridiagonal, and irreducible. Set $\lambda_{1,k} < \cdots < \lambda_{k,k}$ to be the eigenvalues of its leading principal submatrix of order $k$. The eigenvalues satisfy $\lambda_{j,k + 1} < \lambda_{j,k} < \lambda_{j + 1,k + 1}$ for any $1 \leq j \leq k < n$.
:::

::: definition:Sturm Sequence
Let $A \in \mathbb{R}^{n, n}$ and $t \in \mathbb{R}$. Assume $A = A^T$ and $A$ is tridiagonal. Set $a_i = A_{ii}$, $b_i = A_{i, i + 1}$, and $A_i$ to be the leading principal submatrix of order $i$. The Sturm sequence at $t$ is $p_0(t), p_1(t), \ldots, p_n(t)$, where $p_0(t) = 1$ and $p_i(t) = \det(A_i - tI)$. It is computed by
$$
p_1(t) = a_1 - t,\qquad
p_i(t) = (a_i - t)p_{i - 1}(t) - b_{i - 1}^2p_{i - 2}(t),\qquad i = 2, \ldots, n.
$$
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $t \in \mathbb{R}$. Assume $A$ is symmetric tridiagonal. Split $A$ at zero subdiagonal entries. The number of eigenvalues below $t$ is the sum of the Sturm sign-change counts of the resulting blocks, deleting zero terms before counting.
:::

::: definition:Sturm Bisection
Let $A \in \mathbb{R}^{n, n}$, $j \in \{1, \ldots, n\}$, $\ell, u \in \mathbb{R}$, and $\tau > 0$. Assume $A = A^T$ and $A$ is tridiagonal. Set $N(t)$ to be the number of eigenvalues strictly less than $t$, computed by Sturm sign counts, and choose $\ell < u$ s.t. $N(\ell) < j \leq N(u)$. Sturm bisection for the $j$th smallest eigenvalue repeatedly sets $m = \frac{\ell + u}{2}$ and replaces $\ell$ by $m$ if $N(m) < j$, or $u$ by $m$ otherwise. It stops when $u - \ell \leq \tau$ and returns $\frac{\ell + u}{2}$.
:::

### Singular Value Algorithms
::: definition:Upper Bidiagonal Matrix
Let $B \in \mathbb{R}^{n, k}$. The matrix $B$ is an upper bidiagonal matrix if $b_{ij} = 0$ for any $(i, j)$ with $j \neq i$ and $j \neq i + 1$.
:::

::: theorem:Golub-Kahan Bidiagonalization
Let $A \in \mathbb{R}^{n, k}$. Set $B = A$ and $F(x) = I - 2vv^T$, where $v = \frac{x + \operatorname{sign}(x_1)\|x\|_2e_1}{\|x + \operatorname{sign}(x_1)\|x\|_2e_1\|_2}$ for $x \neq 0$, with $\operatorname{sign}(0) = 1$ and $F(0) = I$. For $i = 1,\ldots,\min(n,k)$, compute
$$
\begin{aligned}
L_i &\leftarrow \operatorname{diag}(I_{i - 1},F(B_{i:n,i})),\\
B &\leftarrow L_iB,\\
R_i &\leftarrow \operatorname{diag}(I_i,F(B_{i,i + 1:k}^T))\quad(i < k),\\
B &\leftarrow BR_i\quad(i < k).
\end{aligned}
$$
Apply the reflectors to the active submatrices by rank-one updates and store their vectors. In exact arithmetic, $U = L_1\cdots L_{\min(n,k)}$ and $V = R_1\cdots R_{\min(n,k - 1)}$ satisfy $U^TAV = B$, with $B$ upper bidiagonal and $U,V$ orthogonal.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $n \geq k$. The operation count of Golub-Kahan bidiagonalization is $\sim 4nk^{2} - \frac{4}{3}k^{3}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $n \ge k$. Compute its SVD in two stages:
$$
\begin{aligned}
U_0^TAV_0 &= B\quad\text{by Golub--Kahan bidiagonalization},\\
B &= P\Sigma Q^T\quad\text{by bidiagonal SVD QR iteration},\\
U &\leftarrow U_0P,\qquad V \leftarrow V_0Q.
\end{aligned}
$$
The output is $A = U\Sigma V^T$, with the nonnegative diagonal entries of $\Sigma$ and corresponding columns of $U,V$ ordered by decreasing singular value. For a wide matrix, apply the procedure to $A^T$ and interchange the left and right factors.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$. Assume $A \neq 0$ and a backward stable SVD algorithm is used. Its computed singular values satisfy $\tilde\sigma_j = \sigma_j(A + \delta A)$ for some common perturbation $\delta A$ with $\frac{\|\delta A\|_2}{\|A\|_2} = O(\varepsilon_{\text{machine}})$. Consequently, $\frac{|\tilde\sigma_j - \sigma_j(A)|}{\|A\|_2} = O(\varepsilon_{\text{machine}})$ for $j = 1, \ldots, \min(n, k)$.
:::

## Iterative Methods
### Arnoldi and Lanczos
::: definition:Krylov Sequence
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. The Krylov sequence generated by $A$ and $b$ is $b, Ab, A^2b, \ldots$.
:::

::: definition:Krylov Subspace
Let $A \in \mathbb{C}^{n, n}$, $b \in \mathbb{C}^n$, and $k \ge 1$ be an integer. The $k$th Krylov subspace is $\mathcal{K}_k(A,b) = \operatorname{span}\{b, Ab, \ldots, A^{k - 1}b\}$.
:::

::: definition:Krylov Matrix
Let $A \in \mathbb{C}^{n, n}$, $b \in \mathbb{C}^n$, and $k \ge 1$ be an integer. The Krylov matrix is $K_k = \begin{pmatrix} b & Ab & \cdots & A^{k - 1}b \end{pmatrix} \in \mathbb{C}^{n, k}$.
:::

::: definition:Arnoldi Iteration
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $b \neq 0$. Set $q_1 = \frac{b}{\|b\|_2}$. Arnoldi performs the following operations for $k = 1,2,\ldots$:
$$
\begin{aligned}
v &\leftarrow Aq_k,\\
h_{jk} &\leftarrow q_j^Hv,\quad v \leftarrow v - h_{jk}q_j\quad (j = 1,\ldots,k),\\
h_{k + 1,k} &\leftarrow \|v\|_2,\\
q_{k + 1} &\leftarrow \frac{v}{h_{k + 1,k}}\quad\text{if }h_{k + 1,k} > 0.
\end{aligned}
$$
The iteration stops if $h_{k + 1,k} = 0$. The Hessenberg matrix $H_k = (h_{ij})_{i,j = 1}^k$ has $h_{ij} = 0$ for $i > j + 1$.
:::

::: definition:Ritz Value
Let $A \in \mathbb{C}^{n, n}$ and $Q_k \in \mathbb{C}^{n, k}$. Assume $Q_k^HQ_k = I$. The Ritz values of $A$ on $\operatorname{range}(Q_k)$ are the eigenvalues of $Q_k^HAQ_k$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume Arnoldi reaches step $k$ in exact arithmetic. Set $Q_k = (q_1\ \cdots\ q_k)$ and $v_k = Aq_k - Q_k(h_{1k},\ldots,h_{kk})^T$. $K_k = Q_kR_k$ is a reduced QR factorization, $H_k = Q_k^HAQ_k$, and $AQ_k = Q_kH_k + v_ke_k^T$. If $v_k \neq 0$, then $AQ_k = Q_{k + 1}\tilde H_k$, where $\tilde H_k = \begin{pmatrix}H_k\\h_{k + 1,k}e_k^T\end{pmatrix}$. If $v_k = 0$, then $\mathcal K_k(A,b)$ is $A$-invariant.
:::

::: definition:Arnoldi Approximation Problem
Let $A \in \mathbb{C}^{n, n}$, $b \in \mathbb{C}^n$, and $k \ge 1$ be an integer. Set $\mathcal M_k = \{p \in \mathbb{C}[z] : \deg p = k,\ p\text{ is monic}\}$. The Arnoldi approximation problem is to minimize $\|p(A)b\|_2$ over $p \in \mathcal M_k$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $K_k$ has full column rank and Arnoldi is performed in exact arithmetic. The unique solution of the Arnoldi approximation problem is $\pi_k(z) = \det(zI - H_k)$.
::: ^arnoldi-polynomial-characterization

::: proof
The minimization is a least squares problem with residual $A^kb + z$, $z \in \mathcal K_k(A,b)$, so optimality is equivalent to $Q_k^Hp(A)b = 0$. The Arnoldi relation gives $Q_k^HA^jb = \|b\|_2H_k^je_1$ for $0 \le j \le k$. Cayley–Hamilton therefore gives $Q_k^H\pi_k(A)b = 0$. Two minimizing monic polynomials would differ by a polynomial $d$ of degree at most $k - 1$ with $d(A)b = 0$. Full column rank of $K_k$ implies $d = 0$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$, $b \in \mathbb{C}^n$, $\sigma \in \mathbb{C}$, and $U \in \mathbb{C}^{n, n}$. Assume $U$ is unitary and Arnoldi reaches step $k$ in exact arithmetic. Set $\{\theta_j\}$ to be its Ritz values. Replacing $(A,b)$ by $(A + \sigma I,b)$ gives Ritz values $\{\theta_j + \sigma\}$. Replacing it by $(\sigma A,b)$ with $\sigma \neq 0$ gives $\{\sigma\theta_j\}$. Replacing it by $(UAU^H,Ub)$ leaves the Ritz values unchanged.
:::

::: definition:Lanczos Iteration
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A = A^H$ and $b \neq 0$. Set $q_0 = 0$, $\beta_0 = 0$, and $q_1 = \frac{b}{\|b\|_2}$. Lanczos performs the following operations for $k = 1,2,\ldots$:
$$
\begin{aligned}
v &\leftarrow Aq_k - \beta_{k - 1}q_{k - 1},\\
\alpha_k &\leftarrow q_k^Hv,\\
v &\leftarrow v - \alpha_kq_k,\\
\beta_k &\leftarrow \|v\|_2,\\
q_{k + 1} &\leftarrow \frac{v}{\beta_k}\quad\text{if }\beta_k > 0.
\end{aligned}
$$
The iteration stops if $\beta_k = 0$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A = A^H$ and Lanczos reaches step $k$ in exact arithmetic. Set $Q_k = (q_1\ \cdots\ q_k)$ and $v_k = Aq_k - \beta_{k - 1}q_{k - 1} - \alpha_kq_k$. $T_k = Q_k^HAQ_k$ is real symmetric tridiagonal with diagonal $\alpha_1,\ldots,\alpha_k$ and off-diagonal $\beta_1,\ldots,\beta_{k - 1}$. The relation $AQ_k = Q_kT_k + v_ke_k^T$ holds.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume $A = A^H$. Each Lanczos step without reorthogonalization requires one matrix-vector product and $O(n)$ additional operations. In floating point arithmetic, the generated vectors need not remain mutually orthogonal.
:::

::: definition:Jacobi Matrix
Let $T \in \mathbb{R}^{k, k}$. A Jacobi matrix is a symmetric tridiagonal matrix $T$ with positive subdiagonal entries.
:::

::: proposition
Let $w \in L^1([-1,1])$. Assume $w > 0$ almost everywhere. Set $\langle f,g\rangle_w = \int_{-1}^1 f(x)g(x)w(x)\,dx$, $\|f\|_w = \sqrt{\langle f,f\rangle_w}$, $q_0 = 0$, $\beta_0 = 0$, and $q_1 = \frac{1}{\sqrt{\int_{-1}^1w(x)\,dx}}$. For $j = 1,2,\ldots$, compute
$$
\begin{aligned}
v &\leftarrow xq_j - \beta_{j - 1}q_{j - 1},\\
\alpha_j &\leftarrow \langle q_j,v\rangle_w,\qquad v \leftarrow v - \alpha_jq_j,\\
\beta_j &\leftarrow \|v\|_w,\qquad q_{j + 1} \leftarrow \frac{v}{\beta_j}.
\end{aligned}
$$
The polynomials are orthonormal with $\deg q_j = j - 1$. The Jacobi matrix $T_k$ with diagonal $\alpha_1,\ldots,\alpha_k$ and off-diagonal $\beta_1,\ldots,\beta_{k - 1}$ satisfies $\det(xI - T_k) = C_kq_{k + 1}(x)$, where $C_k$ is the reciprocal leading coefficient of $q_{k + 1}$. Its zeros are distinct and lie in $(-1,1)$.
:::

::: proof
For $i \le j - 2$, $\langle xq_j,q_i\rangle_w = \langle q_j,xq_i\rangle_w = 0$, which gives the three-term recurrence. The monic polynomials $C_kq_{k + 1}$ and determinants $\det(xI - T_k)$ satisfy the same recurrence $d_k = (x - \alpha_k)d_{k - 1} - \beta_{k - 1}^2d_{k - 2}$, with $d_0 = 1$ and $d_1 = x - \alpha_1$. If $q_{k + 1}$ had fewer than $k$ sign changes in $(-1,1)$, multiplying by the product of its sign-change factors would give a nonzero integral against $w$, contradicting orthogonality to polynomials of degree below $k$.
:::

::: proposition
Let $x_1,\ldots,x_k \in [-1,1]$ be distinct. There exist unique weights $w_1,\ldots,w_k$ s.t. $\int_{-1}^1 f(x)\,dx = \sum_{j = 1}^k w_jf(x_j)$ for every polynomial $f$ of degree at most $k - 1$.
::: ^quadrature-interpolation

::: proposition
Let $k \ge 1$ be an integer. The quadrature rule with nodes at the zeros of the degree-$k$ Legendre polynomial and weights from [[#^quadrature-interpolation|quadrature interpolation]] is the Gauss–Legendre rule. Its degree of exactness is $2k - 1$, the largest possible for a $k$-node rule on $[-1,1]$.
:::

::: proof
Write $I(f) = \int_{-1}^1 f(x)\,dx$ and $I_k(f) = \sum_{j = 1}^k w_jf(x_j)$. For any nodes, $f(x) = \prod_{j = 1}^k(x - x_j)^2$ satisfies $I(f) > 0 = I_k(f)$, so exactness cannot reach degree $2k$. Let $L_k$ be the degree-$k$ Legendre polynomial. For $\deg f \le 2k - 1$, polynomial division gives $f = gL_k + r$ with $\deg g,\deg r \le k - 1$. Legendre orthogonality with weight $1$ gives $I(gL_k) = 0$, and its zeros give $I_k(gL_k) = 0$. Thus $I(f) = I(r) = I_k(r) = I_k(f)$.
:::

::: proposition
Let $k \ge 1$ be an integer. Set $T_k \in \mathbb{R}^{k, k}$ to be tridiagonal with $(T_k)_{jj} = 0$ for $1 \le j \le k$ and $(T_k)_{j,j + 1} = (T_k)_{j + 1,j} = \frac{j}{\sqrt{4j^2 - 1}}$ for $1 \le j < k$. Compute $T_k = V\operatorname{diag}(\lambda_1,\ldots,\lambda_k)V^T$ with $V = (v_1\ \cdots\ v_k)$ orthogonal. The Gauss–Legendre nodes and weights are $x_j = \lambda_j$ and $w_j = 2(v_j)_1^2$ for $1 \le j \le k$.
:::

### Krylov Solvers
::: definition:GMRES
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular and $b \neq 0$. Set $x_0 = 0$ and $\beta = \|b\|_2$. GMRES chooses $x_k \in \mathcal K_k(A,b)$ minimizing $\|b - Ax_k\|_2$. At step $k$, it extends Arnoldi and solves
$$
\begin{aligned}
\tilde H_k &\leftarrow \begin{pmatrix}H_k\\h_{k + 1,k}e_k^T\end{pmatrix},\\
y_k &\leftarrow \underset{y \in \mathbb{C}^k}{\operatorname{argmin}}\|\beta e_1 - \tilde H_ky\|_2,\\
x_k &\leftarrow Q_ky_k.
\end{aligned}
$$
It stops when the residual is zero and keeps subsequent iterates fixed. The least squares problem remains valid at Arnoldi termination, with $h_{k + 1,k} = 0$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular. In exact arithmetic, GMRES from $x_0 = 0$ reaches $A^{-1}b$ in at most $n$ steps. Step $k$ of unrestarted GMRES uses one matrix-vector product, $O(nk)$ additional operations, and $O(nk)$ storage.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular, $b \neq 0$, and GMRES is performed in exact arithmetic from $x_0 = 0$. Set $r_k = b - Ax_k$ and $P_k = \{p \in \mathbb{C}[z] : \deg p \le k,\ p(0) = 1\}$. $\|r_k\|_2 = \underset{p \in P_k}{\min}\|p(A)b\|_2$ and $\frac{\|r_k\|_2}{\|b\|_2} \le \underset{p \in P_k}{\inf}\|p(A)\|_2$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$, $b \in \mathbb{C}^n$, $\sigma \in \mathbb{C}\setminus\{0\}$, and $U \in \mathbb{C}^{n, n}$. Assume $A$ is nonsingular and $U$ is unitary. Set $r_k$ to be the exact-arithmetic GMRES residual from $x_0 = 0$. Replacing $(A,b)$ by $(\sigma A,\sigma b)$ gives residual $\sigma r_k$. Replacing it by $(UAU^H,Ub)$ gives $Ur_k$. GMRES is not generally invariant under shifts $A \mapsto A + \tau I$ with $\tau \in \mathbb{C}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular and diagonalizable, $b \neq 0$, and GMRES is performed in exact arithmetic from $x_0 = 0$. Set $A = X\Lambda X^{-1}$, $r_k = b - Ax_k$, and $P_k = \{p \in \mathbb{C}[z] : \deg p \le k,\ p(0) = 1\}$. $\frac{\|r_k\|_2}{\|b\|_2} \le \kappa_2(X)\underset{p \in P_k}{\inf}\underset{\lambda \in \sigma(A)}{\max}|p(\lambda)|$.
:::

::: proof
For $p \in P_k$, $\|p(A)\|_2 = \|Xp(\Lambda)X^{-1}\|_2 \le \kappa_2(X)\underset{\lambda \in \sigma(A)}{\max}|p(\lambda)|$. Apply the GMRES polynomial bound.
:::

::: definition:Conjugate Gradient Method
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is Hermitian positive definite. Set $x_0 = 0$ and $r_0 = p_0 = b$. CG performs the following operations while $r_{k - 1} \neq 0$:
$$
\begin{aligned}
v_k &\leftarrow Ap_{k - 1},\\
\alpha_k &\leftarrow \frac{r_{k - 1}^Hr_{k - 1}}{p_{k - 1}^Hv_k},\\
x_k &\leftarrow x_{k - 1} + \alpha_kp_{k - 1},\\
r_k &\leftarrow r_{k - 1} - \alpha_kv_k,\\
\beta_k &\leftarrow \frac{r_k^Hr_k}{r_{k - 1}^Hr_{k - 1}},\\
p_k &\leftarrow r_k + \beta_kp_{k - 1}.
\end{aligned}
$$
After termination, subsequent iterates remain fixed.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A$ is symmetric positive definite and CG is performed in exact arithmetic from $x_0 = 0$. If $r_{k - 1} \neq 0$, then $\mathcal K_k(A,b) = \operatorname{span}\{x_1,\ldots,x_k\} = \operatorname{span}\{p_0,\ldots,p_{k - 1}\} = \operatorname{span}\{r_0,\ldots,r_{k - 1}\}$. Moreover, $r_k^Tr_j = 0$ and $p_k^TAp_j = 0$ for $0 \le j < k$.
::: ^cg-orthogonality

::: proof
Induct on $k$. The recurrences place $r_j,p_j$ in $\mathcal K_{j + 1}(A,b)$. Suppose the preceding nonzero residuals are orthogonal and the preceding directions are $A$-conjugate. For $j < k - 1$, $r_j \in \operatorname{span}\{p_0,\ldots,p_j\}$ gives $r_k^Tr_j = 0$. Since $p_{k - 1} - r_{k - 1}$ is a multiple of $p_{k - 2}$, $p_{k - 1}^TAr_{k - 1} = p_{k - 1}^TAp_{k - 1}$, so the choice of $\alpha_k$ gives $r_k^Tr_{k - 1} = 0$.
For $j < k - 1$, $Ap_j = \frac{r_j - r_{j + 1}}{\alpha_{j + 1}}$ gives $p_k^TAp_j = 0$. For $j = k - 1$, $r_k^TAp_{k - 1} = -\frac{\|r_k\|_2^2}{\alpha_k}$, so the choice of $\beta_k$ gives $p_k^TAp_{k - 1} = 0$. The nonzero orthogonal residuals form a basis of $\mathcal K_k(A,b)$. The triangular recurrences for $p_j$ and $x_j$, with $\alpha_j > 0$, give the other span identities. At $k = 1$, use $p_0 = r_0$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A$ is symmetric positive definite and CG is performed in exact arithmetic from $x_0 = 0$. Set $x = A^{-1}b$ and $\|z\|_A = \sqrt{z^TAz}$. The iterate $x_k$ uniquely minimizes $\|x - z\|_A$ over $z \in \mathcal K_k(A,b)$. The errors satisfy $\|x - x_k\|_A \le \|x - x_{k - 1}\|_A$, and CG terminates in at most $n$ steps.
::: ^cg-minimization

::: proof
For $z = x_k - d \in \mathcal K_k(A,b)$, [[#^cg-orthogonality|CG orthogonality]] gives $r_k^Td = 0$. Hence $\|x - z\|_A^2 = \|x - x_k\|_A^2 + \|d\|_A^2$, with equality to the minimum iff $d = 0$. Nested Krylov spaces give monotonicity. More than $n$ nonzero mutually orthogonal residuals in $\mathbb{R}^n$ are impossible, so $r_k = 0$ for some $k \le n$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A$ is symmetric positive definite, $b \neq 0$, and CG is performed in exact arithmetic from $x_0 = 0$. Set $e_k = A^{-1}b - x_k$ and $P_k = \{p \in \mathbb{R}[z] : \deg p \le k,\ p(0) = 1\}$. $\|e_k\|_A = \underset{p \in P_k}{\min}\|p(A)e_0\|_A$ and $\frac{\|e_k\|_A}{\|e_0\|_A} \le \underset{p \in P_k}{\inf}\underset{\lambda \in \sigma(A)}{\max}|p(\lambda)|$.
::: ^cg-polynomial-error

::: proof
The errors attainable in $\mathcal K_k(A,b)$ are exactly $p(A)e_0$ with $p \in P_k$. Apply [[#^cg-minimization|CG minimization]]. In an orthonormal eigenbasis, write $e_0 = \sum_j a_jv_j$. Then $\|p(A)e_0\|_A^2 = \sum_j a_j^2\lambda_jp(\lambda_j)^2 \le \underset{\lambda \in \sigma(A)}{\max}|p(\lambda)|^2\|e_0\|_A^2$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A$ is symmetric positive definite. If $A$ has $m$ distinct eigenvalues, then exact-arithmetic CG from $x_0 = 0$ terminates in at most $m$ steps.
:::

::: proof
If $b = 0$, the initial iterate solves the system. Otherwise, for the distinct eigenvalues $\mu_1,\ldots,\mu_m$, the polynomial $p(z) = \prod_{j = 1}^m(1 - \frac{z}{\mu_j})$ satisfies $p(0) = 1$ and vanishes on $\sigma(A)$. Apply [[#^cg-polynomial-error|CG polynomial error bound]].
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A$ is symmetric positive definite, $b \neq 0$, and CG is performed in exact arithmetic from $x_0 = 0$. Set $e_k = A^{-1}b - x_k$ and $\kappa = \kappa_2(A) = \frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}$. $\frac{\|e_k\|_A}{\|e_0\|_A} \le 2\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^k$ for $k \ge 1$.
:::

::: proof
If $\kappa = 1$, then $A = cI$ with $c > 0$, and CG terminates in one step. Otherwise, set $a = \lambda_{\min}(A)$, $d = \lambda_{\max}(A)$, $\gamma = \frac{d + a}{d - a}$, and $p(z) = \frac{T_k(\frac{d + a - 2z}{d - a})}{T_k(\gamma)}$, where $T_k$ is the Chebyshev polynomial. Since $p(0) = 1$ and $|T_k(t)| \le 1$ on $[-1,1]$, [[#^cg-polynomial-error|CG polynomial error bound]] is at most $\frac{1}{T_k(\gamma)}$. The identity $T_k(\gamma) = \frac{s^k + s^{-k}}{2}$ with $s = \gamma + \sqrt{\gamma^2 - 1} = \frac{\sqrt\kappa + 1}{\sqrt\kappa - 1}$ gives the bound.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume $A$ is Hermitian positive definite. Each CG step requires one matrix-vector product and $O(n)$ additional operations.
:::

::: definition:Biorthogonal Vectors
Let $V,W \in \mathbb{C}^{n, k}$. Their columns are biorthogonal if $W^HV = I$.
:::

::: definition:Tridiagonal Biorthogonalization
Let $A,V \in \mathbb{C}^{n, n}$. Assume $V$ is nonsingular. A tridiagonal biorthogonalization is a factorization $A = VTV^{-1}$ with $T$ tridiagonal. The associated dual basis is $W = V^{-H}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $v_1,w_1 \in \mathbb{C}^n$. Assume $w_1^Hv_1 = 1$. Set $v_0 = w_0 = 0$ and $\beta_0 = \gamma_0 = 0$. Two-sided Lanczos performs
$$
\begin{aligned}
\alpha_j &\leftarrow w_j^HAv_j,\\
u &\leftarrow Av_j - \alpha_jv_j - \gamma_{j - 1}v_{j - 1},\\
z &\leftarrow A^Hw_j - \overline{\alpha_j}w_j - \overline{\beta_{j - 1}}w_{j - 1},\\
\beta_j &\leftarrow \|u\|_2,\qquad \gamma_j \leftarrow \frac{z^Hu}{\beta_j},\\
v_{j + 1} &\leftarrow \frac{u}{\beta_j},\qquad w_{j + 1} \leftarrow \frac{z}{\overline{\gamma_j}}
\end{aligned}
$$
for $j = 1,2,\ldots$, stopping before division if $u = 0$, $z = 0$, or $z^Hu = 0$. In exact arithmetic before breakdown, $V_k = (v_1\ \cdots\ v_k)$ and $W_k = (w_1\ \cdots\ w_k)$ satisfy $W_k^HV_k = I$ and $W_k^HAV_k = T_k$, where $T_k$ has diagonal $\alpha_j$, subdiagonal $\beta_j$, and superdiagonal $\gamma_j$. Moreover, $AV_k = V_kT_k + \beta_kv_{k + 1}e_k^T$, $A^HW_k = W_kT_k^H + \overline{\gamma_k}w_{k + 1}e_k^T$, $v_j \in \mathcal K_j(A,v_1)$, and $w_j \in \mathcal K_j(A^H,w_1)$.
:::

::: definition:CGN
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular. CGN applies CG to $A^HAx = A^Hb$, evaluating products as $A^H(Av)$ without forming $A^HA$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ is nonsingular, $b \neq 0$, and CGN is performed in exact arithmetic from $x_0 = 0$. Set $\kappa = \kappa_2(A)$ and $r_k = b - Ax_k$. $\frac{\|r_k\|_2}{\|r_0\|_2} \le 2\left(\frac{\kappa - 1}{\kappa + 1}\right)^k$ for $k \ge 1$.
:::

::: definition:BCG
Let $A \in \mathbb{C}^{n, n}$ and $b,s_0 \in \mathbb{C}^n$. Assume $A$ is nonsingular and $s_0^Hb \neq 0$. Set $x_0 = 0$, $r_0 = p_0 = b$, $q_0 = s_0$, and $\rho_0 = s_0^Hr_0$. BCG performs
$$
\begin{aligned}
v_k &\leftarrow Ap_{k - 1},\qquad u_k \leftarrow A^Hq_{k - 1},\\
\alpha_k &\leftarrow \frac{\rho_{k - 1}}{q_{k - 1}^Hv_k},\\
x_k &\leftarrow x_{k - 1} + \alpha_kp_{k - 1},\\
r_k &\leftarrow r_{k - 1} - \alpha_kv_k,\qquad s_k \leftarrow s_{k - 1} - \overline{\alpha_k}u_k,\\
\rho_k &\leftarrow s_k^Hr_k,\qquad \beta_k \leftarrow \frac{\rho_k}{\rho_{k - 1}},\\
p_k &\leftarrow r_k + \beta_kp_{k - 1},\qquad q_k \leftarrow s_k + \overline{\beta_k}q_{k - 1}
\end{aligned}
$$
for $k = 1,2,\ldots$, stopping if $r_k = 0$. A zero $\rho_{k - 1}$ or $q_{k - 1}^Hv_k$ causes breakdown before division. In exact arithmetic without breakdown, $r_k = b - Ax_k$, $x_k \in \mathcal K_k(A,b)$, and $r_k \perp \mathcal K_k(A^H,s_0)$.
:::

::: definition:Preconditioner
Let $A,M \in \mathbb{C}^{n, n}$ and $b \in \mathbb{C}^n$. Assume $A$ and $M$ are nonsingular. Left preconditioning by $M$ gives $M^{-1}Ax = M^{-1}b$. Right preconditioning gives $AM^{-1}y = b$ with $x = M^{-1}y$.
:::

::: proposition
Let $A,M \in \mathbb{R}^{n, n}$ and $b \in \mathbb{R}^n$. Assume $A,M$ are symmetric positive definite and $b \neq 0$. Set $M = C^TC$, $B = C^{-T}AC^{-1}$, $\kappa = \kappa_2(B) = \frac{\lambda_{\max}(M^{-1}A)}{\lambda_{\min}(M^{-1}A)}$, $y_k$ to be the exact-arithmetic CG iterates for $By = C^{-T}b$ from $y_0 = 0$, $x_k = C^{-1}y_k$, and $e_k = A^{-1}b - x_k$. The preconditioned CG error satisfies $\frac{\|e_k\|_A}{\|e_0\|_A} \le 2\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^k$ for $k \ge 1$.
:::
