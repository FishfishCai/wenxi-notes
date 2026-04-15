---
tags:
---
#NumericalLinearAlgebra 
Prerequisite knowledge: [[Matrix]], [[Matrix Factorization]], [[Stability]]
## Fundamental Difficulty

> [!definition|] Companion Matrix
> Let $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_1z + a_0$ be a monic polynomial of degree $n$, and $A \in \mathbb{R}^{n, n}$. The companion matrix of $p$ is $A = \begin{pmatrix} 0 & & & -a_0 \\ 1 & 0 & & -a_1 \\ & 1 & \ddots & \vdots \\ & & 1 & -a_{n-1} \end{pmatrix}$.

> [!theorem|]
> For any $n \ge 5$, there is a polynomial $p(z)$ of degree $n$ with rational coefficients that has a real root $p(r) = 0$ with the property that $r$ cannot be written using any expression involving rational numbers, addition, subtraction, multiplication, division, and $k$th roots.

## Two Phases of Eigenvalue Computations

> [!definition|] Upper-Hessenberg Matrix
> Let $H \in \mathbb{C}^{n, n}$. The matrix $H$ is an upper-Hessenberg matrix if $h_{ij} = 0$ for $i > j + 1$.

> [!definition|] Tridiagonal Matrix
> Let $T \in \mathbb{C}^{n, n}$. The matrix $T$ is a tridiagonal matrix if $t_{ij} = 0$ for $|i - j| > 1$.

> [!remark|]
> If $A$ is Hermitian, the upper-Hessenberg form is tridiagonal.

## Reduction to Hessenberg or Tridiagonal Form

> [!theorem|] Hessenberg Reduction
> Let $A \in \mathbb{C}^{n, n}$. There exists a unitary matrix $Q \in \mathbb{C}^{n, n}$ s.t. $Q^{*}AQ = H$, where $H$ is upper-Hessenberg. If $A$ is Hermitian, $H$ is tridiagonal.

> [!theorem|]
> The operation count of the Hessenberg reduction is $\sim \frac{10}{3}n^{3}$.

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$. Assume $A$ is Hermitian. The operation count of the tridiagonal reduction is $\sim \frac{4}{3}n^{3}$.

> [!theorem|]
> Let $A \in \mathbb{C}^{n, n}$. Assume the Hessenberg reduction $A = QHQ^{*}$ is computed by Algorithm 26.1 on a computer satisfying the axioms of floating point arithmetic. The computed factors $\tilde{Q}$ and $\tilde{H}$ satisfy $\tilde{Q}\tilde{H}\tilde{Q}^{*} = A + \delta A$, $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$.

## Rayleigh Quotient, Inverse Iteration

> [!definition|] Rayleigh Quotient
> Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. $A = A^{\top}$. The Rayleigh quotient of $x$ is $r(x) = \frac{x^{\top}Ax}{x^{\top}x}$.

> [!proposition|]
> Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. $A = A^{\top}$. If $x$ is an eigenvector of $A$, $r(x)$ is the corresponding eigenvalue.

> [!proposition|]
> Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. $A = A^{\top}$. $\nabla r(x) = \frac{2}{x^{\top}x}(Ax - r(x)x)$.

> [!proposition|]
> Let $A \in \mathbb{R}^{n, n}$, $q_J \in \mathbb{R}^{n}$, and $\lambda_J \in \mathbb{R}$. $A = A^{\top}$. $q_J$ is an eigenvector of $A$ corresponding to eigenvalue $\lambda_J$. $r(q_J) - r(x) = O(\|x - q_J\|^{2})$ as $x \to q_J$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$, $v^{(0)} \in \mathbb{R}^{n}$, and $q_1, \ldots, q_n \in \mathbb{R}^{n}$. $A = A^{\top}$. $\|v^{(0)}\| = 1$. $q_1, \ldots, q_n$ are orthonormal eigenvectors of $A$ corresponding to eigenvalues $\lambda_1, \ldots, \lambda_n$ with $|\lambda_1| > |\lambda_2| \ge \cdots \ge |\lambda_n| \ge 0$. Assume $q_1^{\top}v^{(0)} \neq 0$. The iterates of power iteration satisfy $\|v^{(k)} - (\pm q_1)\| = O\left(\left|\frac{\lambda_2}{\lambda_1}\right|^{k}\right)$ and $|\lambda^{(k)} - \lambda_1| = O\left(\left|\frac{\lambda_2}{\lambda_1}\right|^{2k}\right)$ as $k \to \infty$.

`\begin{proof}`
$v^{(0)} = a_1q_1 + a_2q_2 + \cdots + a_nq_n$. Since $v^{(k)}$ is a multiple of $A^kv^{(0)}$, $v^{(k)} = c_k\lambda_1^k(a_1q_1 + a_2(\frac{\lambda_2}{\lambda_1})^kq_2 + \cdots + a_n(\frac{\lambda_n}{\lambda_1})^kq_n)$. Since $a_1 = q_1^{\top}v^{(0)} \neq 0$, the first equation follows. The second follows from this and $r(q_J) - r(x) = O(\|x - q_J\|^2)$.
`\end{proof}`

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$, $\mu \in \mathbb{R}$, $v^{(0)} \in \mathbb{R}^{n}$, and $q_1, \ldots, q_n \in \mathbb{R}^{n}$. $A = A^{\top}$. $\|v^{(0)}\| = 1$. $q_1, \ldots, q_n$ are orthonormal eigenvectors of $A$ corresponding to eigenvalues $\lambda_1, \ldots, \lambda_n$. Assume $\lambda_J$ is the closest eigenvalue to $\mu$ and $\lambda_K$ is the second closest, $|\mu - \lambda_J| < |\mu - \lambda_K| \le |\mu - \lambda_j|$ for each $j \neq J$, and $q_J^{\top}v^{(0)} \neq 0$. The iterates of inverse iteration satisfy $\|v^{(k)} - (\pm q_J)\| = O\left(\left|\frac{\mu - \lambda_J}{\mu - \lambda_K}\right|^{k}\right)$ and $|\lambda^{(k)} - \lambda_J| = O\left(\left|\frac{\mu - \lambda_J}{\mu - \lambda_K}\right|^{2k}\right)$ as $k \to \infty$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$ and $v^{(0)} \in \mathbb{R}^{n}$. $A = A^{\top}$. Rayleigh quotient iteration converges to an eigenvalue/eigenvector pair for all except a set of measure zero of starting vectors $v^{(0)}$. When it converges, the convergence is ultimately cubic in the sense that if $\lambda_J$ is an eigenvalue of $A$ and $v^{(0)}$ is sufficiently close to the eigenvector $q_J$, $\|v^{(k+1)} - (\pm q_J)\| = O(\|v^{(k)} - (\pm q_J)\|^{3})$ and $|\lambda^{(k+1)} - \lambda_J| = O(|\lambda^{(k)} - \lambda_J|^{3})$ as $k \to \infty$.

`\begin{proof}`
We prove cubic convergence when convergence occurs. Assume $\lambda_J$ is simple. If $\|v^{(k)} - q_J\| \le \epsilon$ for sufficiently small $\epsilon$, the Rayleigh quotient satisfies $|\lambda^{(k)} - \lambda_J| = O(\epsilon^2)$ by the quadratic accuracy of the Rayleigh quotient. By Theorem 27.2, one step of inverse iteration with shift $\mu = \lambda^{(k)}$ gives $\|v^{(k+1)} - (\pm q_J)\| = O(|\lambda^{(k)} - \lambda_J| \cdot \|v^{(k)} - (\pm q_J)\|) = O(\epsilon^3)$. The constants in the $O$ symbols are uniform in sufficiently small neighborhoods of $\lambda_J$ and $q_J$, giving the cubic convergence pattern: $\epsilon \to O(\epsilon^3) \to O(\epsilon^9) \to \cdots$.
`\end{proof}`

## QR Algorithm without Shifts

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$, $V^{(0)} \in \mathbb{R}^{n, k}$, and $\hat{Q}^{(0)} \in \mathbb{R}^{n, k}$. $A = A^{\top}$. Assume the eigenvalues of $A$ satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_k| > |\lambda_{k+1}| \ge \cdots \ge |\lambda_n|$, and all leading principal minors of $\hat{Q}^{\top}V^{(0)}$ are nonsingular. The columns of the matrices $\hat{Q}^{(k)}$ from the simultaneous iteration converge linearly to the eigenvectors of $A$: $\|q_j^{(k)} - \pm q_j\| = O(C^k)$ for each $j$ with $1 \le j \le k$, where $C < 1$ is the constant $\underset{1 \le k \le n}{\max} |\lambda_{k+1}| / |\lambda_k|$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. Assume the eigenvalues satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$ and $Q$ has all nonsingular leading principal minors. The pure QR algorithm (Algorithm 28.1) applied to $A$ is equivalent to simultaneous iteration. $A^k = Q^{(k)}\underline{R}^{(k)}$ and $A^{(k)} = (Q^{(k)})^{\top}AQ^{(k)}$, where $Q^{(k)} = Q^{(1)}Q^{(2)}\cdots Q^{(k)}$ and $\underline{R}^{(k)} = R^{(k)}R^{(k-1)}\cdots R^{(1)}$.

`\begin{proof}`
By induction on $k$. The base case $k = 0$ is trivial: $A^0 = I = Q^{(0)}\underline{R}^{(0)}$ and $A^{(0)} = A$. For $k \ge 1$, for simultaneous iteration, $A^k = AQ^{(k-1)}\underline{R}^{(k-1)} = Q^{(k)}R^{(k)}\underline{R}^{(k-1)} = Q^{(k)}\underline{R}^{(k)}$, using the QR factorization $AQ^{(k-1)} = Q^{(k)}R^{(k)}$. For the QR algorithm, $A^k = AQ^{(k-1)}\underline{R}^{(k-1)} = Q^{(k-1)}A^{(k-1)}\underline{R}^{(k-1)} = Q^{(k-1)}Q^{(k)}R^{(k)}\underline{R}^{(k-1)} = Q^{(k)}\underline{R}^{(k)}$. Both produce the same $Q^{(k)}$ and $\underline{R}^{(k)}$. Finally, $A^{(k)} = (Q^{(k)})^{\top}A^{(k-1)}Q^{(k)} = (Q^{(k)})^{\top}AQ^{(k)}$ follows from the inductive hypothesis.
`\end{proof}`

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. Assume the eigenvalues satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$ and $Q$ has all nonsingular leading principal minors. $A^{(k)}$ converges linearly with constant $\underset{k}{\max} |\lambda_{k+1}|/|\lambda_k|$ to $\mathrm{diag}(\lambda_1, \ldots, \lambda_n)$, and $Q^{(k)}$ (with the signs of its columns adjusted as necessary) converges at the same rate to $Q$.

## QR Algorithm with Shifts

> [!definition|] Wilkinson Shift
> Let $A^{(k)} \in \mathbb{R}^{n, n}$ and $B \in \mathbb{R}^{2, 2}$. $B$ is the lower-rightmost $2 \times 2$ submatrix of $A^{(k)}$, i.e., $B = \begin{pmatrix} a_{n-1} & b_{n-1} \\ b_{n-1} & a_n \end{pmatrix}$. The Wilkinson shift is the eigenvalue of $B$ that is closer to $a_n$, given by $\mu = a_n - \frac{\mathrm{sign}(\delta) b_{n-1}^2}{|\delta| + \sqrt{\delta^2 + b_{n-1}^2}}$, where $\delta = \frac{a_{n-1} - a_n}{2}$.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. The shifted QR algorithm with the Wilkinson shift converges at least quadratically and in practice cubically.

> [!theorem|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. $A$ is tridiagonal. Assume the diagonalization of $A$ is computed by the QR algorithm (Algorithm 28.2) on a computer satisfying the axioms of floating point arithmetic, and let $\tilde{\Lambda}$ and $\tilde{Q}$ be defined as indicated. $\tilde{Q}\tilde{\Lambda}\tilde{Q}^{*} = A + \delta A$, $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$ for some $\delta A \in \mathbb{C}^{n, n}$.

> [!proposition|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. The computed eigenvalues $\tilde{\lambda}_j$ of $A$ via tridiagonal reduction followed by the QR algorithm satisfy $\frac{|\tilde{\lambda}_j - \lambda_j|}{\|A\|} = O(\epsilon_{\text{machine}})$.

## Other Eigenvalue Algorithms

> [!definition|] Jacobi Rotation
> Let $J \in \mathbb{R}^{n, n}$. The matrix $J$ is a Jacobi rotation if it has the form of a Givens rotation $J = \begin{pmatrix} c & s \\ -s & c \end{pmatrix}$ embedded in the identity, where $c = \cos\theta$ and $s = \sin\theta$ for some $\theta$ satisfying $\tan(2\theta) = \frac{2d}{b - a}$, and $a, b, d$ are entries of a $2 \times 2$ symmetric submatrix $\begin{pmatrix} a & d \\ d & b \end{pmatrix}$ of $A$.

> [!definition|] Irreducible Tridiagonal Matrix
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. $A$ is tridiagonal. The matrix $A$ is an irreducible tridiagonal matrix if all its off-diagonal entries are nonzero.

> [!theorem|] Eigenvalue Interlacing
> Let $A \in \mathbb{R}^{n, n}$ and $A^{(1)}, \ldots, A^{(n)} \in \mathbb{R}^{k, k}$ for $k = 1, \ldots, n$. $A = A^{\top}$. $A$ is an irreducible tridiagonal matrix. $A^{(k)}$ is the upper-left $k \times k$ principal submatrix of $A$ with eigenvalues $\lambda_1^{(k)} < \lambda_2^{(k)} < \cdots < \lambda_k^{(k)}$. The eigenvalues strictly interlace: $\lambda_j^{(k+1)} < \lambda_j^{(k)} < \lambda_{j+1}^{(k+1)}$ for $k = 1, 2, \ldots, n-1$ and $j = 1, 2, \ldots, k$.

> [!definition|] Sturm Sequence
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. $A$ is tridiagonal. The Sturm sequence of $A$ is $1, \det(A^{(1)}), \det(A^{(2)}), \ldots, \det(A^{(n)})$, where $A^{(k)}$ is the upper-left $k \times k$ principal submatrix.

> [!proposition|]
> Let $A \in \mathbb{R}^{n, n}$. $A = A^{\top}$. $A$ is a symmetric tridiagonal matrix. The number of negative eigenvalues of $A$ is equal to the number of sign changes in the Sturm sequence.

