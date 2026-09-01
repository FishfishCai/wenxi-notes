---
id: y2kmwhs2j1s20rq2
title: Eigenvalue Algorithm
tags: []
refs: []
backrefs: []
---
## Fundamental Difficulty
::: definition:Companion Matrix
Let $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0$ be a monic polynomial of degree $n$. The companion matrix of $p$ is $A \in \mathbb{R}^{n, n}$ given by $A = \begin{pmatrix} 0 & & & -a_0 \\ 1 & 0 & & -a_1 \\ & 1 & \ddots & \vdots \\ & & 1 & -a_{n-1} \end{pmatrix}$.
:::

::: proposition
For any integer $n \geq 5$, there exists a polynomial $p(z)$ of degree $n$ with rational coefficients that has a real root $r$ with $p(r) = 0$ s.t. $r$ cannot be written using any expression involving rational numbers, addition, subtraction, multiplication, division, and $k$th roots.
:::

## Two Phases of Eigenvalue Computations

::: definition:Upper-Hessenberg Matrix
Let $H \in \mathbb{C}^{n, n}$. The matrix $H$ is an upper-Hessenberg matrix if $h_{ij} = 0$ for any $i > j + 1$.
:::

::: definition:Tridiagonal Matrix
Let $T \in \mathbb{C}^{n, n}$. The matrix $T$ is a tridiagonal matrix if $t_{ij} = 0$ for any $|i - j| > 1$.
:::

::: note
If $A$ is Hermitian, then the upper-Hessenberg form is tridiagonal.
:::

## Reduction to Hessenberg or Tridiagonal Form

::: theorem:Hessenberg Reduction
Let $A \in \mathbb{C}^{n, n}$. There exists a unitary matrix $Q \in \mathbb{C}^{n, n}$ s.t. $Q^{*}AQ = H$, where $H$ is upper-Hessenberg. If $A$ is Hermitian, then $H$ is tridiagonal.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. The operation count of the Hessenberg reduction of $A$ is $\sim \frac{10}{3}n^{3}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume $A$ is Hermitian. The operation count of the tridiagonal reduction of $A$ is $\sim \frac{4}{3}n^{3}$.
:::

::: proposition
Let $A \in \mathbb{C}^{n, n}$. Assume the Hessenberg reduction $A = QHQ^{*}$ is computed on a computer satisfying the axioms of floating point arithmetic. There exists $\delta A \in \mathbb{C}^{n, n}$ s.t. the computed factors $\tilde{Q}$ and $\tilde{H}$ satisfy $\tilde{Q}\tilde{H}\tilde{Q}^{*} = A + \delta A$ and $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$.
:::

## Rayleigh Quotient, Inverse Iteration

::: definition:Rayleigh Quotient
Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. Assume $A = A^T$. The Rayleigh quotient of $x$ is $r(x) = \frac{x^T A x}{x^T x}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. Assume $A = A^T$. If $x$ is an eigenvector of $A$, then $r(x)$ is the corresponding eigenvalue.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $x \in \mathbb{R}^{n}$. Assume $A = A^T$. Then $\nabla r(x) = \frac{2}{x^T x}(Ax - r(x)x)$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$, $x, q_J \in \mathbb{R}^{n}$, and $\lambda_J \in \mathbb{R}$. Assume $A = A^T$ and $q_J$ is an eigenvector of $A$ corresponding to the eigenvalue $\lambda_J$. Then $r(q_J) - r(x) = O(\|x - q_J\|^{2})$ as $x \to q_J$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$, $v^{(0)} \in \mathbb{R}^{n}$, and $q_1, \ldots, q_n \in \mathbb{R}^{n}$. Assume $A = A^T$, $\|v^{(0)}\| = 1$, $q_1, \ldots, q_n$ are orthonormal eigenvectors of $A$ corresponding to eigenvalues $\lambda_1, \ldots, \lambda_n$ with $|\lambda_1| > |\lambda_2| \ge \cdots \ge |\lambda_n| \ge 0$, and $q_1^T v^{(0)} \neq 0$. Then the iterates of power iteration satisfy $\|v^{(k)} - (\pm q_1)\| = O\left(\left|\frac{\lambda_2}{\lambda_1}\right|^{k}\right)$ and $|\lambda^{(k)} - \lambda_1| = O\left(\left|\frac{\lambda_2}{\lambda_1}\right|^{2k}\right)$ as $k \to \infty$.
:::

::: proof
$v^{(0)} = a_1q_1 + a_2q_2 + \cdots + a_nq_n$. Since $v^{(k)}$ is a multiple of $A^kv^{(0)}$, $v^{(k)} = c_k\lambda_1^k(a_1q_1 + a_2(\frac{\lambda_2}{\lambda_1})^kq_2 + \cdots + a_n(\frac{\lambda_n}{\lambda_1})^kq_n)$. Since $a_1 = q_1^{T}v^{(0)} \neq 0$, the first equation follows. The second follows from this and $r(q_J) - r(x) = O(\|x - q_J\|^2)$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$, $\mu \in \mathbb{R}$, $v^{(0)} \in \mathbb{R}^{n}$, and $q_1, \ldots, q_n \in \mathbb{R}^{n}$. Assume $A = A^T$, $\|v^{(0)}\| = 1$, $q_1, \ldots, q_n$ are orthonormal eigenvectors of $A$ corresponding to eigenvalues $\lambda_1, \ldots, \lambda_n$, $\lambda_J$ is the closest eigenvalue to $\mu$ and $\lambda_K$ the second closest with $|\mu - \lambda_J| < |\mu - \lambda_K| \le |\mu - \lambda_j|$ for any $j \neq J$, and $q_J^T v^{(0)} \neq 0$. Then the iterates of inverse iteration satisfy $\|v^{(k)} - (\pm q_J)\| = O\left(\left|\frac{\mu - \lambda_J}{\mu - \lambda_K}\right|^{k}\right)$ and $|\lambda^{(k)} - \lambda_J| = O\left(\left|\frac{\mu - \lambda_J}{\mu - \lambda_K}\right|^{2k}\right)$ as $k \to \infty$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$ and $v^{(0)} \in \mathbb{R}^{n}$. Assume $A = A^T$. Then Rayleigh quotient iteration converges to an eigenvalue/eigenvector pair for all starting vectors $v^{(0)}$ except a set of measure zero, and when it converges the convergence is ultimately cubic: if $\lambda_J$ is an eigenvalue of $A$ and $v^{(0)}$ is sufficiently close to the eigenvector $q_J$, then $\|v^{(k+1)} - (\pm q_J)\| = O(\|v^{(k)} - (\pm q_J)\|^{3})$ and $|\lambda^{(k+1)} - \lambda_J| = O(|\lambda^{(k)} - \lambda_J|^{3})$ as $k \to \infty$.
:::

::: proof
We prove cubic convergence when convergence occurs. Assume $\lambda_J$ is simple. If $\|v^{(k)} - q_J\| \le \epsilon$ for sufficiently small $\epsilon$, the Rayleigh quotient satisfies $|\lambda^{(k)} - \lambda_J| = O(\epsilon^2)$ by the quadratic accuracy of the Rayleigh quotient. By Theorem 27.2, one step of inverse iteration with shift $\mu = \lambda^{(k)}$ gives $\|v^{(k+1)} - (\pm q_J)\| = O(|\lambda^{(k)} - \lambda_J| \cdot \|v^{(k)} - (\pm q_J)\|) = O(\epsilon^3)$. The constants in the $O$ symbols are uniform in sufficiently small neighborhoods of $\lambda_J$ and $q_J$, giving the cubic convergence pattern: $\epsilon \to O(\epsilon^3) \to O(\epsilon^9) \to \cdots$.
:::

## QR Algorithm without Shifts

::: proposition
Let $A \in \mathbb{R}^{n, n}$, $V^{(0)} \in \mathbb{R}^{n, k}$, and $\hat{Q}^{(0)} \in \mathbb{R}^{n, k}$. Assume $A = A^T$, the eigenvalues of $A$ satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_k| > |\lambda_{k+1}| \ge \cdots \ge |\lambda_n|$, and all leading principal minors of $\hat{Q}^T V^{(0)}$ are nonsingular. Then the columns of the matrices $\hat{Q}^{(k)}$ from simultaneous iteration converge linearly to the eigenvectors of $A$: $\|q_j^{(k)} - (\pm q_j)\| = O(C^k)$ for any $j$ with $1 \le j \le k$, where $C = \underset{1 \le k \le n}{\max} \frac{|\lambda_{k+1}|}{|\lambda_k|} < 1$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$, the eigenvalues satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$, and the eigenvector matrix $Q$ of $A$ has all nonsingular leading principal minors. Then the pure QR algorithm applied to $A$ is equivalent to simultaneous iteration, and $A^k = Q^{(k)}\underline{R}^{(k)}$ and $A^{(k)} = (Q^{(k)})^T A Q^{(k)}$, where $Q^{(k)} = Q^{(1)}Q^{(2)}\cdots Q^{(k)}$ and $\underline{R}^{(k)} = R^{(k)}R^{(k-1)}\cdots R^{(1)}$.
:::

::: proof
By induction on $k$. The base case $k = 0$ is trivial: $A^0 = I = Q^{(0)}\underline{R}^{(0)}$ and $A^{(0)} = A$. For $k \ge 1$, for simultaneous iteration, $A^k = AQ^{(k-1)}\underline{R}^{(k-1)} = Q^{(k)}R^{(k)}\underline{R}^{(k-1)} = Q^{(k)}\underline{R}^{(k)}$, using the QR factorization $AQ^{(k-1)} = Q^{(k)}R^{(k)}$. For the QR algorithm, $A^k = AQ^{(k-1)}\underline{R}^{(k-1)} = Q^{(k-1)}A^{(k-1)}\underline{R}^{(k-1)} = Q^{(k-1)}Q^{(k)}R^{(k)}\underline{R}^{(k-1)} = Q^{(k)}\underline{R}^{(k)}$. Both produce the same $Q^{(k)}$ and $\underline{R}^{(k)}$. Finally, $A^{(k)} = (Q^{(k)})^{T}A^{(k-1)}Q^{(k)} = (Q^{(k)})^{T}AQ^{(k)}$ follows from the inductive hypothesis.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$, the eigenvalues satisfy $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$, and the eigenvector matrix $Q$ of $A$ has all nonsingular leading principal minors. Then $A^{(k)}$ converges linearly with constant $\underset{k}{\max} \frac{|\lambda_{k+1}|}{|\lambda_k|}$ to $\mathrm{diag}(\lambda_1, \ldots, \lambda_n)$, and $Q^{(k)}$ (with the signs of its columns adjusted as necessary) converges at the same rate to $Q$.
:::

## QR Algorithm with Shifts

::: definition:Wilkinson Shift
Let $A^{(k)} \in \mathbb{R}^{n, n}$. Set $B \in \mathbb{R}^{2, 2}$ to be the lower-rightmost $2 \times 2$ submatrix of $A^{(k)}$, $B = \begin{pmatrix} a_{n-1} & b_{n-1} \\ b_{n-1} & a_n \end{pmatrix}$, and $\delta = \frac{a_{n-1} - a_n}{2}$. The Wilkinson shift is the eigenvalue of $B$ closer to $a_n$, given by $\mu = a_n - \frac{\mathrm{sign}(\delta) b_{n-1}^2}{|\delta| + \sqrt{\delta^2 + b_{n-1}^2}}$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$. Then the shifted QR algorithm with the Wilkinson shift converges at least quadratically, and in practice cubically.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$, $A$ is tridiagonal, and the diagonalization of $A$ is computed by the QR algorithm on a computer satisfying the axioms of floating point arithmetic, with computed factors $\tilde{\Lambda}$ and $\tilde{Q}$. There exists $\delta A \in \mathbb{C}^{n, n}$ s.t. $\tilde{Q}\tilde{\Lambda}\tilde{Q}^{*} = A + \delta A$ and $\frac{\|\delta A\|}{\|A\|} = O(\epsilon_{\text{machine}})$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$. Then the computed eigenvalues $\tilde{\lambda}_j$ of $A$ obtained by tridiagonal reduction followed by the QR algorithm satisfy $\frac{|\tilde{\lambda}_j - \lambda_j|}{\|A\|} = O(\epsilon_{\text{machine}})$ for any $j$.
:::

## Other Eigenvalue Algorithms

::: definition:Jacobi Rotation
Let $J, A \in \mathbb{R}^{n, n}$. The matrix $J$ is a Jacobi rotation if it has the form of a Givens rotation $\begin{pmatrix} c & s \\ -s & c \end{pmatrix}$ embedded in the identity, where $c = \cos\theta$ and $s = \sin\theta$ for some $\theta$ satisfying $\tan(2\theta) = \frac{2d}{b - a}$, and $a, b, d$ are the entries of a $2 \times 2$ symmetric submatrix $\begin{pmatrix} a & d \\ d & b \end{pmatrix}$ of $A$.
:::

::: definition:Irreducible Tridiagonal Matrix
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and $A$ is tridiagonal. The matrix $A$ is an irreducible tridiagonal matrix if all its off-diagonal entries are nonzero.
:::

::: theorem:Eigenvalue Interlacing
Let $A \in \mathbb{R}^{n, n}$ and $A^{(k)} \in \mathbb{R}^{k, k}$ for $k = 1, \ldots, n$. Assume $A = A^T$, $A$ is an irreducible tridiagonal matrix, and $A^{(k)}$ is the upper-left $k \times k$ principal submatrix of $A$ with eigenvalues $\lambda_1^{(k)} < \lambda_2^{(k)} < \cdots < \lambda_k^{(k)}$. Then the eigenvalues strictly interlace: $\lambda_j^{(k+1)} < \lambda_j^{(k)} < \lambda_{j+1}^{(k+1)}$ for $k = 1, 2, \ldots, n-1$ and $j = 1, 2, \ldots, k$.
:::

::: definition:Sturm Sequence
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and $A$ is tridiagonal. The Sturm sequence of $A$ is $1, \det(A^{(1)}), \det(A^{(2)}), \ldots, \det(A^{(n)})$, where $A^{(k)}$ is the upper-left $k \times k$ principal submatrix of $A$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, n}$. Assume $A = A^T$ and $A$ is tridiagonal. Then the number of negative eigenvalues of $A$ equals the number of sign changes in the Sturm sequence of $A$.
:::
