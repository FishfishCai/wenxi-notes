#### 1. Form of constraint problem: 
- $\underset{x\in \mathbb{R^n}}{min}f(x) \ \text{s.t. } c_l(x) \leq 0, c_E(x)=0$
- Decision varibale: $x\in \mathbb{R}^n$ 
- Objective Function: $f:\mathbb{R}^n \to \mathbb{R}$
- Constraint Functions: $c_I:\mathbb{R}^n \to \mathbb{R}^{m_I}$ and $c_E:\mathbb{R}^n \to \mathbb{R}^{m_E}$
- $f$, $c_I$ and $c_E$ are $C^1$ functions.
- Gradient and Hessian: $\nabla f:\mathbb{R}^n \to \mathbb{R}^n$ and $\nabla^2f:\mathbb{R}^n\to \mathbb{R}^{n\times n}$
- Jacobian: $\nabla c_I:\mathbb{R}^{n} \to \mathbb{R}^{n\times m_I}$ and $\nabla c_E:\mathbb{R}^{n} \to \mathbb{R}^{n\times m_E}$
#### 2. Linear algebra:

- $\text{trace}(A)=\sum\lambda_i$
- $\text{det}(A)=\Pi\lambda_i$
- $\text{Null}(A)\bigoplus\text{Range}(A^T)=\mathbb{R}^n$ and $\text{Null}(A^T)\bigoplus\text{Range}(A)=\mathbb{R}^m$
- positive semi-definite: square matrix A s.t. $x^TAx\geq0$, for all $x\in \mathbb{R}^n$
- positive definite: square matrix A s.t. $\exists\mu>0 \ and \  x^TAx\geq \mu\|x\|^2_2$, for all $x\in \mathbb{R}^n$
  - If all the eigenvalues are positive, the matrix is positive definite.

#### 3. Norm:

- Definition:
  - $\|x\|\geq0$ for all $x\in \mathbb{R}^n$
  - $\|\alpha x\|=|\alpha|\|x\|$ for all $\alpha\in\mathbb{R}$ and $x\in \mathbb{R}^n$
  - $\|x\|=0$ iff $x=0$
  - $\|x+y\|\leq\|x\|+\|y\|$ for all $\{x,y\}\in \mathbb{R}^n$

- Cauchy-Schwartz inequality: $|x^Ty|\leq\|x\|_2\|y\|_2$
- Holder Inequality: $|x^Ty|\leq\|x\|_p\|y\|_q$
- Pythagorean theorem: $\|x+y\|^2_2=\|x\|_2^2+2x^Ty+\|y\|_2^2$
- Equivalent: $a\|x\|_\alpha\leq\|x\|_\beta\leq b\|x\|_\alpha$
- All norms in $\mathbb{R}^n$ are equivalent.	

- Condition number: $K(A)=\|A\|\|A^{-1}\|=\frac{\lambda_{max}(A)}{\lambda_{min}(A)}$

#### 4. Rate of convergence:

- Q-sublinear: $\underset{k\to \infty}{lim}\frac{\|x_{k+1}-x\|}{\|x_k-x\|}=1$
- Q-linear: $\frac{\|x_{k+1}-x\|}{\|x_k-x\|}\leq c$ for $c\in(0,1)$ and sufficient big $k$
- Q-superlinear: $\underset{k\to \infty}{lim}\frac{\|x_{k+1}-x\|}{\|x_k-x\|}=0$
- Q-quadratic: $\frac{\|x_{k+1}-x\|}{\|x_k-x\|^2}\leq c$ for $c>0$ and sufficient big $k$
- R-sth.: there exists $\{\epsilon_k\}$ s.t. $\|x_k-x\|\leq\epsilon_k$ and $\{\epsilon_k\}$ is Q-sth.



### Theorem of multi-dimensional function:

#### 1. Basic Definition

- Global minimum: $f(x^*)\leq f(x)$ for all $x\in \mathbb{R}^n$

- Local minimum: there exists $\epsilon>0$ s.t. $f(x^*)\leq f(x)$ for $x\in B(x^*,\epsilon)$

- Strict: the inequality holds for $x\neq x^*$.

- Isolated: for a $B(x^*,\epsilon)$, the minimum is unique.

- Descent direction $v$: $v\in \mathbb{R}^n$ s.t. $\nabla f(x)^Tv<0$

#### 2. Theorems

- If $f\in C^1$ and $x$ is a local minimum, then $\nabla f(x)=0$.
- If $f\in C^2$ and $x$ is a local minimum, then $\nabla^2 f(x) \succ 0$.
- If $f\in C^2$, $\nabla f(x)=0$ and $\nabla^2 f(x) \succ 0$, then $x$ is a strict local minimum.

- If $f\in C^1$, then there exists $\alpha\in[0,1]$ s.t. $f(x+d)=f(x)+\nabla f(x+\alpha d)^Td$
- If $f\in C^2$, then there exists $\alpha\in[0,1]$ s.t. $f(x + d) = f(x)+\nabla f(x)^Td+\frac{1}{2}d^T\nabla^2f(x+\alpha d)d$
- If $f\in C^1$, then $f(x+d)=f(x)+\int_0^1\nabla f(x+\alpha d)^Td \ d\alpha$
- If $f\in C^2$, then $f(x + d) = f(x)+\nabla f(x)^Td+\int_0^1\frac{1}{2}d^T\nabla^2f(x+\alpha d)d\ d\alpha$
- Taylor's theorem: If $f\in C^{k+1}$, then there exists $\alpha\in[0,1]$ s.t. $f(x + d) = \sum_{|\beta| \leq k} \frac{1}{\beta!} \partial^\beta f(x) d^\beta + \sum_{|\beta| = k+1} \frac{1}{\beta!} \partial^\beta f(x + \alpha d) d^\beta$

- Taylor's theorem: If $f\in C^{k+1}$, then $f(x + d) = \sum_{|\beta| \leq k} \frac{1}{\beta!} \partial^\beta f(x) d^\beta + \sum_{|\beta| = k+1}\int_0^1 \frac{1}{\beta!} \partial^\beta f(x + \alpha d) d^\beta\ d\alpha$

- If $f\in C^2$, then $\nabla f(x+d)=\nabla f(x)+\int_0^1\nabla^2f(x+\alpha d)d d\alpha$

#### 3. Additional conditions:

- Convexity: $f(\alpha x+(1-\alpha)y)\leq\alpha f(x)+(1-\alpha)f(y)$ for $\alpha\in [0,1]$
  - Sum and composition of convex functions is convex. 


- $\mu$-strongly convexity: $f(\alpha x + (1 - \alpha)y) \leq \alpha f(x) + (1 - \alpha) f(y) - \frac{\mu}{2} \alpha (1 - \alpha) \| x - y \|_2^2$ for $\alpha\in [0,1]$
- L-Lipschitz continuous gradient: $\|\nabla f(\mathbf{y}) - \nabla f(\mathbf{x})\|_2 \leq L \|\mathbf{y} - \mathbf{x}\|_2$
- If $f$ is convex, then the local minimum is a global minimum.
- If $f$ is strictly convex, then there's at most one local minimum.
- If $f$ is $\mu$-strongly convex, then there's at most one local minimum.

- $f\in C^1$ is convex iff $f(y) \geq f(x) + \nabla f(x)^T (y - x)$.
- $f\in C^2$ is convex iff $\nabla^2 f(x) \succeq 0$.

- $f\in C^1$ is $\mu$-strongly convex iff $f(y) \geq f(x) + \nabla f(x)^T (y - x) + \frac{\mu}{2} \| y - x \|_2^2$.
- $f\in C^2$ is $\mu$-strongly convex iff $\nabla^2 f(x) \succeq \mu I$.

- If $f \in C^1$ is convex and has L-Lipschitz continuous gradient, then $f(y) \leq f(x) + \nabla f(x)^T (y - x) + \frac{L}{2} \|y - x\|_2^2$
- If $f\in C^2$ is convex and has L-Lipschitz continuous gradient, then $\nabla^2 f(x) \preceq L I$

#### 4. Constrained function Analysis

- Linear independence constraint qualification (LICQ): $\{\nabla c(x)_i:i\in \mathcal{E} \cup \mathcal{A}(x)\}$ are linearly independent.
- If $x^*$ is a local solution s.t. LICQ holds, then there exists Lagrange multipliers $\lambda^*$ s.t. $\nabla_x L(x, \lambda) = \nabla f(x) + \nabla c(x) \lambda = 0$,  $c_i(x) = 0 \text{ for } i \in \mathcal{E}$, $c_i(x) \leq 0 \text{ for }i \in \mathcal{I}$, $\lambda_i \geq 0 \text{ for }i \in \mathcal{I}$ and $\lambda_i c_i(x) = 0 \text{ for }i \in \mathcal{I}$.

- If $x^*$ is a local solution s.t. LICQ holds and $\lambda^*$ is the corresponding multipliers s.t. $(x^*, \lambda^*)$ is a KKT point, then $d^T \nabla^2 L(x^*, \lambda^*) d \geq 0\text{ for all } d \in C(x^*, \lambda^*)$​, where $C(x^*, \lambda^*) = \left\{\begin{array}{ll}\nabla c_i(x)^T d = 0; & i \in \mathcal{E} \\\nabla c_i(x)^T d = 0; & i \in A(x) \text{ with } \lambda_i > 0 \\\nabla c_i(x)^T d \leq 0; & i \in A(x) \text{ with } \lambda_i = 0\end{array}\right.$

- If $x^*$ is a feasible point, $\lambda^*$ is a Lagrange multiplier vector s.t. the KKT conditions hold and $d^T \nabla^2 L(x^*, \lambda^*) d > 0\text{ for all } d \in C(x^*, \lambda^*) \setminus \{0\}$, then $x^*$ is a strict local solution.

#### 5. Gradient Descent Analysis

- If $f\in C^1$ has L-Lipschitz continuous gradient and is bounded below, let $x_{k+1}=x_k-\alpha\nabla f(x_k)$ where $0<\alpha\leq\frac{1}{L}$, then $f(x_{k+1})\leq f(x_k) - \frac{1}{2} \alpha \|\nabla f(x_k)\|_2^2$, implying $\sum_{j=0}^{\infty} \|\nabla f(x_k)\|_2^2 < \infty$ and $\nabla f(x_k) \to 0$.
- If $f\in C^1$ has L-Lipschitz continuous gradient and is convex, let $x_{k+1}=x_k-\alpha\nabla f(x_k)$ where $0<\alpha\leq\frac{1}{L}$, then $f(x_k) - f(x^*) \leq \frac{\|x_0 - x^*\|_2^2}{2 \alpha k}$.

- If $f\in C^1$ has L-Lipschitz continuous gradient and is $\mu$-strongly convex, let $x_{k+1}=x_k-\alpha\nabla f(x_k)$ where $0<\alpha\leq\frac{1}{L}$, then $f(x_k) - f(x^*) \leq (1 - \alpha \mu)^k ( f(x_0) - f(x^*) )$.

#### 6. Newton's Method Analysis

- If $f\in C^2$, and in $B(x^*,r)$, $\|\nabla^2f(x^*)^{-1}\|\leq M$ and $\nabla^2f(x^*)$  is L-Lipschitz continuous, let $\|x_0-x^*\|\leq\min\{r,\frac{1}{2ML}\}$ and $x_{k+1} = x_k -[\nabla^2f(x_k)]^{-1}\nabla f(x_k)$, then $\|x_{k+1}-x^*\|\leq ML\|x_k-x^*\|^2$ and $\|x_{k+1}-x^*\|\leq \frac{1}{2}\|x_k-x^*\|$. 

#### 7. Line Search Method Analysis

- Sufficient decrease condition: $f(x_k + \alpha_k d_k) \leq f(x_k) + c_1 \alpha_k \nabla f(x_k)^T d_k$
- Curvature condition: $\nabla f(x_k + \alpha_k d_k)^T d_k \geq c_2 \nabla f(x_k)^T d_k$
- Wolfe conditions: $f(x_k + \alpha_k d_k) \leq f(x_k) + c_1 \alpha_k \nabla f(x_k)^T d_k$ and $\nabla f(x_k + \alpha_k d_k)^T d_k \geq c_2 \nabla f(x_k)^T d_k$ where $0 < c_1 < c_2 < 1$

- Suppose $f : \mathbb{R}^n \to \mathbb{R}$. Let $d_k$ be a descent direction at $x_k$ and assume that $f$ is bounded below along the ray $\{x_k + \alpha d_k \mid \alpha > 0\}$. Then if $0 < c_1 < c_2 < 1$, there exist intervals of step lengths satisfying the Wolfe conditions.
- If $f\in C^1$ has L-Lipschitz continuous gradient and is bounded below, let $x_{k+1}=x_k+\alpha_kd_k$ where $d_k$ is a descent direction and $\alpha_k$ satisfies wolfe condition, then $\sum_{j=0}^{\infty}\cos^2\theta_k \|\nabla f(x_k)\|_2^2 < \infty$ and $\cos^2\theta_k\nabla f(x_k) \to 0$.

#### 8. BFGS Analysis

- If $f\in C^2$ and there exists $\mu$ and $L$ s.t. $\mu\|d\|^2_2\leq d^T\nabla^2f(x)d\leq L\|d\|^2_2$ for all $d$ and $x\in \mathbb{R}^n$,  then for any $x_0$ and $H_0$, the sequence generated by the BFGS method with a Wolfe line search converges to the minimizer of $f$.
- If $f\in C^2$, BFGS converges to a minimizer at which $\nabla^2f$ is Lipschitz continuous and $\sum_{n=1}^\infty\|x_k-x^*\|<\infty$, then $x_k\to x^*$ at a superlinear rate.

#### 9. SGD Analysis

- 

#### 10. Convergence–Quadratic Penalty Algorithm Analysis

- If $\nu_k \to \infty$ and each $x_k$ is the exact global minimizer of $\phi(x, \nu_k)$, then every limit point of $\{x_k\}$ is a global solution of the original problem.

- If $\nu_k \to \infty$,  $\xi_k \to 0$ and $x^*$ be any limit point of $\{x_k\}$, then if $x^*$ is infeasible, then it is a stationary point of $\frac{1}{2} \|c(x)\|_2^2$ and if $x^*$ is feasible and the LICQ hold, then $x^*$ is a KKT point for the original problem. Moreover, for such points, we have that for any infinite subsequence $\mathcal{K}$ s.t. $\lim_{k \in \mathcal{K}} x_k = x^*$, $\lim_{k \in \mathcal{K}} \nu_k c_i(x_k) = \lambda_i^*$.



### Algorithm

#### 1. Line Search Algorithm

- Steps:

  - Algorithm chooses a direction $d_k$

  - Searches along $d_k$ from the current $x_k$ for a new iterate $x_{k+1}$

  - $x_{k+1} = x_k + \alpha d_k$

- Determine the direction first, then determine the step size.

- Step size:
  - Predetermined sequence: Constant, diminishing...
  - Adaptive: backtracking (Armijo), Armijo-Wolfe...

#### 2. Trust Region Algorithm

- Steps:

  - Algorithm constructs a model $m_k$ of $f$ at $x_k$

  - Minimizes the model $m_k$ (instead of $f$) at $x_k$ to compute the step $d$, i.e. $d = \underset{d}{\text{arg min}}m_k(x_k+d)$

  - New iterate: $x_{k+1} = x_k+d$

- Fix the trust region radius first, then determine the step size with direction.

#### 3. N-th Order Model

- First-order model: $\mathit{m}_k (\mathbf{x}_k + \mathbf{d}) = f(\mathbf{x}_k) + \nabla f(\mathbf{x}_k)^T \mathbf{d}$
- Second-order model: $\mathit{m}_k (\mathbf{x}_k + \mathbf{d}) = f(\mathbf{x}_k) + \nabla f(\mathbf{x}_k)^T \mathbf{d} + \frac{1}{2} \mathbf{d}^T \mathbf{I} \mathbf{d}$

#### 4.Convergence Algorithm

  - Globally convergent algorithm: For any initial iterate $x_0$, the iterate sequence $\{x_k\}$ generated by the algorithm has a subsequence that converges to a stationary point.

  - Locally convergent algorithm: If, from any initial iterate $x_0$ in a neighborhood of a point $x^*$, the iterate sequence $\{x_k\}$ generated by the algorithm has a subsequence that converges to $x^*$, then the algorithm is said to be locally convergent to $x^*$.
    - A globally convergent algorithm is locally convergent to the points converged by itself.

#### 5. Gradient Descent Algorithm

- $x_{k+1} = x_k -\alpha\nabla f(x_k)$
- Termination conditions:
  - Patience level: $k \leq k_{\text{max}}$ or $\text{time} \leq x \text{ seconds}$
  - First-Order optimality:  $\|\nabla f(x_k)\|_{\infty} \leq \epsilon \max \{ 1, \|\nabla f(x_0)\|_{\infty} \}$ where $\epsilon \in (0,1)$

#### 6. Newton's Method

- For $F:\mathbb{R}^n\to \mathbb{R}^n$, in order to achieve $F(x)=0$,  $\nabla F(x_k)^T d = -F(x_k)$
- For $f:\mathbb{R}^n\to \mathbb{R}$, in order to achieve $\min f(x)$,  $\nabla^2 f(x_k) d = -\nabla f(x_k)$
  - $d = -(\nabla^2 f(x_k))^{-1}\nabla f(x_k)$
- $x_{k+1}=x_k+d_k$

#### 7. Gradient Descent with Wolfe Line Search

- $x_{k+1} = x_k -\alpha_k\nabla f(x_k)$
- $\alpha_k$ satisfies the Wolfe conditions.

#### 8.Modified Newton’s Method with Line Search

- $x_{k+1}=x_k+\alpha_kd_k$
- $d_k = -(\nabla^2 f(x_k)+\eta_kI)^{-1}\nabla f(x_k)$ where $\eta_kI$ is positively definite.
- $\alpha_k$ satisfies Armijo condition.

#### 9. Symmetric Rank-1/2 Updating

- Secant equation: $B_{k+1}s_k = y_k$
- $B_{k+1} = B_k+\sigma vv^T$
  - $B_{k+1} = B_k + \frac{(y_k - B_k s_k)(y_k - B_k s_k)^T}{(y_k - B_k s_k)^T s_k}$
  - $H_{k+1} = H_k + \frac{(s_k - H_k y_k)(s_k - H_k y_k)^T}{(s_k - H_k y_k)^T y_k}$


- $B_{k+1} = B_k+\sigma_1 v_1v_1^T+\sigma_2 v_2v_2^T$

  - DFP: $\min\limits_{B \in \mathbb{R}^{n \times n}} \| B - B_k \|$ s.t. $B = B^T$ and $B s_k = y_k$
    - $B_{k+1} = ( I - \frac{y_k s_k^T}{s_k^T y_k}) B_k ( I - \frac{s_k y_k^T}{s_k^T y_k}) + \frac{y_k y_k^T}{s_k^T y_k}$
    - $H_{k+1} = H_k - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k} + \frac{s_k s_k^T}{s_k^T y_k}$
  - BFGS: $\min\limits_{H \in \mathbb{R}^{n \times n}} \| H - H_k \|$ s.t. $H = H^T$ and $H s_k = y_k$
    - $H_{k+1} = ( I - \frac{y_k s_k^T}{s_k^T y_k}) H_k ( I - \frac{s_k y_k^T}{s_k^T y_k}) + \frac{s_k s_k^T}{s_k^T y_k}$
    - $B_{k+1} = B_k - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k} + \frac{y_k y_k^T}{s_k^T y_k}$
  
  - Broyden Class: $B_{k+1} = (1-\phi_k)B_{k+1}^{BFGS}+\phi_kB_{k+1}^{DFP}$

#### 10. TR Subproblem

- Conditions:
  - $(B_k +\lambda I)d_k =−\nabla f(x_k) $
  - $(B_k +\lambda I)\geq0$
  - $\lambda(\Delta_k −\|d_k\|)=0$

- Let $\lambda=0$ first, otherwise, find $\lambda>0 \ s.t. \ B_k +\lambda I \geq0$ and $d(\lambda)=−(B_k +λI)\nabla f(x_k)$

#### 11. Quadratic Penalty Algorithm

- Find solutions $\{x_k\}$ for $\min_{x \in \mathbb{R}^n} \phi(x, \nu_k) = f(x) + \frac{\nu_k}{2} \|c(x)\|_2^2$, with increasing $x_k$.
- 
