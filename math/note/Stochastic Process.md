### Probability

#### 1. Definition

::: definition:Probability
$\mathbb{P}(E) = \sum_{\omega \in E} p(\omega)$, where $p : \Omega \to [0, 1]$ satisfying that $\Omega$ is countable and $\sum_{\omega \in \Omega} p(\omega)$.
- 可以看作$\int_E dp$
:::

::: definition:Random variable
Random variable $X : \Omega \to \mathbb{R}$.
:::

::: definition:Law of a random variable
Let $E \subseteq X(\Omega)$. The law of $X$ is $\mathcal{L}_X(E) = \mathbb{P}(\{\omega \in \Omega : X(\omega) \in E\}) = \mathbb{P}(X^{-1}(E))$.
:::

#### 2. Equations

::: proposition
$\mathbb{P}(A, B) = \mathbb{P}(A)\mathbb{P}(B)$ if $A$ and $B$ are independent.
:::

::: proposition
$\mathbb{P}(A, B \mid C) = \mathbb{P}(A \mid C)\mathbb{P}(B \mid C)$ if $A$ and $B$ are conditionally independent.
:::

::: proposition
$\mathbb{P}(A) = \mathbb{P}(A \mid B)\mathbb{P}(B)$ if $A \subset B$.
- $\mathbb{P}(A) = \sum_i \mathbb{P}(A \mid E_i)\mathbb{P}(E_i)$
:::

::: proposition
$\mathbb{P}(A, B) = \mathbb{P}(A \mid B)\mathbb{P}(B)$.
- $\mathbb{P}(A, B, C, D) = \mathbb{P}(A \mid B, C, D)\mathbb{P}(B \mid C, D)\mathbb{P}(C \mid D)\mathbb{P}(D)$
:::

::: proposition
$\mathbb{P}(A \mid B) = \frac{\sum_i \mathbb{P}(A \mid E_i)\mathbb{P}(E_i)}{\mathbb{P}(B)}$
:::

#### 3. Expectation

::: definition:Expectation
$\mathbb{E}[X] = \sum_{\omega \in \Omega} X(\omega)\mathbb{P}(\omega) = \sum_{x \in X(\Omega)} x\,\mathcal{L}_X(x)$
- 可以看作$\int_\Omega X(\omega)dp$ 和$\int_{R_X}xdl$
:::

::: proposition
$\mathbb{E}[X] = \sum_i \mathbb{E}[X \mid B_i]\mathbb{P}(B_i)$
:::

::: proposition
计数随机变量: $X = \sum_{k \geq 1} \mathbf{1}_{\{X \geq k\}}$
- $\mathbb{E}(X) = \sum_{k \geq 1} \mathbb{P}(X \geq k)$
:::

### Total Variation Distance

#### 1. Definition

::: definition:Total variation distance
Let $\mu, \nu$ be probability distributions over a state space $S$. The total variation distance is $d_{TV}(\mu, \nu) = \underset{A \subseteq \mathcal{S}}{\max}|\mu(A) - \nu(A)|$.
:::

::: definition:Coupling
Let $\mu, \nu$ be distributions over $S$. A coupling of $\mu$ and $\nu$ is a distribution $\delta : S \times S \to [0, 1]$ s.t. $\delta(x, S) = \mu(x)$ and $\delta(S, x) = \nu(x)$.
:::

#### 2. Theorem

::: proposition
$d_{TV}(\mu, \nu) = \frac{1}{2}\sum_{x \in S}|\mu(x) - \nu(x)|$
:::

::: proposition
$d_{TV}(\mu, \nu) = \frac{1}{2}\sup\left\{\sum_{x \in S} f(x)\mu(x) - \sum_{x \in S} f(x)\nu(x) : \underset{x \in S}{\max}|f(x)| = 1\right\}$
:::

::: proposition
$d_{TV}(\mu, \nu) = \underset{(X, Y) \text{ is a coupling of } \mu \text{ and } \nu}{\inf}\mathbb{P}(X \neq Y)$
:::

### Markov Chains

#### 1. Definition:

::: definition:Stochastic process
Let $\mathcal{S}$ be a state space. A stochastic process is a family $\{X_n\}_{n \in \mathbb{N}}$ with $X_n \in \mathcal{S}$.
:::

::: definition:Path
The path of $X$ is the map $n \mapsto X_n$.
:::

::: definition:Temporally homogeneous discrete Markov chain
Let $p : S \times S \to [0, 1]$. A temporally homogeneous discrete Markov chain with transition matrix $p$ satisfies $\mathbb{P}(X_{n+1} = y \mid X_n = x, X_{n-1} = x_{n-1}, \ldots, X_1 = x_1) = \mathbb{P}(X_{n+1} = y \mid X_n = x) = p(x, y)$.
:::

::: definition:$m$-step transition probability
$p^m(x, y) = \mathbb{P}(X_{n+m} = y \mid X_n = x)$.
- $p^{m+n}(x, y) = \sum_{k \in S} p^m(x, k)p^n(k, y)$
:::

#### 2. Strong Markov Property

::: definition:Stopping time
Let $\{X_n\}$ be a stochastic process. A stopping time with respect to $X_n$ is a map $T : \Omega \to \mathbb{N} \cup \{\infty\}$ s.t. $\{T = n\}$ is determined by $\{X_0, \ldots, X_n\}$.
:::

::: theorem:Strong Markov property
Let $X_n$ be a Markov chain. For any $k \in \mathbb{N}$, $x \in \mathcal{S}$, given $\{X_T = x, T < \infty\}$, $X_{T+k}$ is independent of $\{X_0, \cdots, X_T\}$. Moreover, $\mathbb{P}(X_{T+k} = y \mid T < \infty, X_T = x) = p^k(x, y)$.

$$
\begin{align*}
&\mathbb{P}(X_{T+k} = y \mid T < \infty, X_T = x) \\
&=\frac{1}{\mathbb{P}(T < \infty, X_T = x)} \sum_{n \geq 1} \sum_{\omega \in S(n,x)} \mathbb{P}\big(X_{T+k} = y \mid \omega = s\big) \mathbb{P}(\omega = s) \\
&=p^k(x,y)\sum_{n \geq 1} \sum_{\omega \in S(n,x)}\frac{\mathbb{P}(\omega = s)}{\mathbb{P}(T < \infty, X_T = x)}\\
&=p^k(x,y)
\end{align*}
$$

- $\mathbb{P}(X_{T+k} = y \mid T = n, X_T = x) = p^k(x, y)$
:::

#### 3. Classification of States

::: definition:Classification of states
Let $X_n$ be a Markov chain on state space $S$.
- $\mathbb{P}_x(A) = \mathbb{P}(A \mid X_0 = x)$
- $T_y = \min\{n \geq 1 : X_n = y\} = T_y^1$
- $T_y^n = \min\{n > T_y^{n-1} : X_n = y\}$
- $\rho_{xy} = \mathbb{P}_x(T_y < \infty)$
- $N_y = \sum_{n \geq 1} \mathbf{1}_{\{X_n = y\}}$
- $N_y^{T_x} = \sum_{1 \leq n \leq T_x} \mathbf{1}_{\{X_n = y\}}$
- Transient state $x$: $\rho_{xx} < 1$
- Recurrent state $x$: $\rho_{xx} = 1$
- $x$ communicate $y$ ($x \to y$): $\rho_{xy} > 0$
    - $\exists m \text{ s.t. } p^m(x, y) > 0$
- Closed state set $A$: $\forall x \in A, y \notin A, p(x, y) = 0$
- Irreducible state set $A$: $\forall x, y \in A, x \to y$
:::

::: proposition
$\mathbb{P}_x(T_y^k < \infty) = \rho_{xy}\rho_{yy}^{k-1}$
:::

::: proposition
If $\mathbb{P}_x(T_y \leq k) \geq a > 0$ for any $x$, then $\mathbb{P}_x(T_y > mk) \leq (1 - a)^m$.
:::

::: proposition
$\mathbb{E}_x(N_y) = \sum_{n \geq 1} p^n(x, y) = \frac{\rho_{xy}}{1 - \rho_{yy}}$
:::

::: proposition
$\mathbb{E}_x(N_y^{T_x}) = \sum_{n \geq 1} \mathbb{P}(X_n = y, n \leq T_x)$
:::

::: proposition
$\sum_{y \in S} \mathbb{E}_x(N_y^{T_x}) = \mathbb{E}_x(T_x)$
:::

::: proposition
If $\rho_{xy} > 0$ and $\rho_{yx} < 1$, then $x$ is transient.
:::

::: proposition
If $\rho_{xy} > 1$ and $x$ is recurrent, then $\rho_{yx} = 1$.
:::

::: proposition
If $x \to y$ and $y \to z$, then $x \to z$.
:::

::: proposition
If the state space $S$ is finite, then it can be written as a disjoint union $S = T \cup R_1 \cup \ldots \cup R_n$ where $T$ is the set of transient states, and $R_i$ is a closed irreducible set of recurrent states.
- If $x$ is recurrent and $x \to y$, then $y$ is recurrent.
    - If a finite set $A \subset S$ is closed, then there exists at least one recurrent state.
        - If $S$ is finite and irreducible, then all the states are recurrent.
:::

#### 4. Stationary Distribution

::: definition:Stationary distribution
- Doubly stochastic matrix $P$: $\sum_x P(x, y) = 1$ for all $y \in S$
- Stationary distribution $\pi$: $\pi(x) = \sum_{y \in S} \pi(y)p(y, x)$ for all $x \in S$
- Detailed balance condition: $\pi(x)p(x, y) = \pi(y)p(y, x)$
:::

::: proposition
If $S$ is finite with a doubly stochastic matrix, then $\pi(x) = \frac{1}{N}$ is a stationary distribution.
:::

::: proposition
If $S$ is finite and $x \in S$ is recurrent (or $S$ is countable and $x$ is positively recurrent), then $\pi(y) = \frac{\mathbb{E}_x(N_y^{T_x})}{\mathbb{E}_x(T_x)}$ is a stationary distribution.
:::

::: proposition
If $S$ is irreducible and has a stationary distribution, then the stationary distribution is unique and is $\pi(x) = \frac{1}{\mathbb{E}_x(T_x)}$.
:::

::: proposition
If the distribution of $X_0$ is the stationary distribution $\pi$, let $\hat{X}_m = X_{n-m}$, then $\hat{X}$ is a Markov chain with $\hat{p}(x, y) = \frac{\pi(y)p(y, x)}{\pi(x)}$.
- If $\pi$ is detailed balanced or uniform, then $\hat{p}(x, y) = p(x, y)$.
:::

::: proposition
For irreducible $S$, there is a detailed balanced stationary distribution iff for any cycle $x_0, x_1, \ldots, x_n = x_0$, $\prod_{i=1}^n p(x_{i-1}, x_i) = \prod_{i=1}^n p(x_i, x_{i-1})$.
:::

#### 5. Limit Behavior

::: definition:Period
- Period: the greatest common divisor of $I_x = \{n \geq 1 : p^n(x, x) > 0\}$, where $x$ is recurrent
- Aperiodic $x$: a state whose period is $1$
:::

::: proposition
If $x \to y$ and $y \to x$, then $x$ and $y$ have the same period.
:::

::: proposition
If $p(x, x) > 0$, then $x$ has period $1$.
:::

::: proposition
If the period of $x$ is $1$, then there exists $n_0$ s.t. $n \in I_x$ for all $n \geq n_0$.
:::

::: proposition
If $S$ is irreducible, aperiodic and has a stationary distribution $\pi$, then $p^n(x, y) \to \pi(y)$.
:::

#### 6. Exit Distributions and Exit Times

::: proposition
Let $A, B \subset S$ s.t. $C = S \setminus (A \cup B)$ is finite, and $h : S \to [0, 1]$ s.t. $h(a) = 1$ for $a \in A$, $h(b) = 0$ for $b \in B$, and $h(c) = \sum_{y \in S} p(c, y)h(y)$ for $c \in C$. If $\mathbb{P}_c(V_A \wedge V_B < \infty) > 0$ for all $c \in C$, then $h(x) = \mathbb{P}_x(V_A < V_B)$.
:::

::: proposition
Let $A \subset S$ s.t. $C = S \setminus A$ is finite, and $g : S \to \mathbb{R}$ bounded s.t. $g(a) = 0$ for $a \in A$ and $g(c) = \sum_{y \in S} p(c, y)f(c, y) + \sum_{y \in S} p(c, y)g(y)$ for $c \in C$, where $f : S \times S \to \mathbb{R}$ is non-negative. If $\mathbb{P}_c(V_A < \infty) > 0$ for $c \in C$, then $g(x) = \mathbb{E}_x\left[\sum_{m=1}^{\infty} f(X_{m-1}, X_m)\mathbf{1}_{\{V_A \geq m\}}\right]$. In particular, if $f = 1$, then $g(x) = \mathbb{E}_x[V_A]$.
:::

#### 7. Ergodic Theorem

::: proposition
If $S$ is irreducible and has a stationary distribution $\pi$, and $f : \mathcal{S} \to \mathbb{R}$ satisfies $\sum_{z \in S} |f(z)|\pi(z) < \infty$, then $\underset{n \to \infty}{\lim} \frac{1}{n}\sum_{k=0}^{n} f(X_k) = \mathbb{E}_\pi f := \sum_{x \in \mathcal{S}} f(x)\pi(x)$.
- If $S$ is irreducible and has a stationary distribution, then $\underset{n \to \infty}{\lim} \frac{N_x^n}{n} = \frac{1}{\mathbb{E}_x(T_x)} = \pi(x)$.
:::

::: proposition
If $S$ is irreducible and recurrent, then $\underset{n \to \infty}{\lim} \frac{N_x^n}{n} = \frac{1}{\mathbb{E}_x(T_x)}$.
- If $S$ is irreducible and recurrent, then $\underset{n \to \infty}{\lim} \frac{1}{n}\sum_{i=1}^{n} p^i(x, y) \to \pi(y)$.
:::

#### 8. Existence and Uniqueness in Countable State Space

::: proposition
If $S$ has a stationary distribution, then a state $x$ s.t. $\pi(x) > 0$ is recurrent.
- If $S$ is irreducible and transient, then it does not have a stationary distribution.
:::

### Poisson Processes

#### 1. Exponential Distribution

::: definition:Exponential distribution
- $\mathbb{P}(X \leq t) = \left[1 - e^{-\lambda t}\right]\mathbf{1}_{\{t \geq 0\}}$
- $f_X(t) = \lambda e^{-\lambda t}\mathbf{1}_{\{t \geq 0\}}$
- $\mathbb{E}(X) = \frac{1}{\lambda}$
- $\text{Var}(X) = \frac{1}{\lambda^2}$
:::

::: proposition
$\mathbb{P}(X > t + s \mid X > t) = \mathbb{P}(X > s)$
:::

::: proposition
$\mathbb{P}\left(\underset{i}{\min} X_i > t\right) = e^{-(\lambda_1 + \cdots + \lambda_n)t}$
:::

::: proposition
$\mathbb{P}\left(\underset{i}{\arg\min} X_i = i\right) = \frac{\lambda_i}{\lambda_1 + \cdots + \lambda_n}$
:::

::: proposition
$f_{T_n}(t) = \lambda e^{-\lambda t}\frac{(\lambda t)^{n-1}}{(n-1)!}\mathbf{1}_{\{t \geq 0\}}$ where $T_n = X_1 + \cdots + X_n$.
:::

#### 2. Poisson Process

::: definition:Poisson process
Let $\lambda > 0$. A Poisson process with intensity $\lambda$ is $N(t) := \sum_{n \geq 1} \mathbf{1}_{\{T_n \leq t\}} = \max\{n \geq 1 : T_n \leq t\}$.
:::

::: definition:Poisson distribution
- $\mathbb{P}(X = k) = e^{-\lambda}\frac{\lambda^k}{k!}, k \geq 0$
- $\mathbb{E}(X) = \text{Var}(X) = \frac{1}{\lambda}$
:::

::: proposition
$\sum_{k=1}^{n} X_i \sim \text{Poi}\left(\sum_{k=1}^{n} \lambda_i\right)$
:::

::: proposition
If $N_t$ is a Poisson process with intensity $\lambda$, then $N_t \sim \text{Poi}(\lambda t)$.
:::

::: proposition
If $N_t$ is a Poisson process with intensity $\lambda$, then $\underset{t \to \infty}{\lim} \frac{N_t}{t} = \lambda$ almost surely.
:::

::: proposition
Let $N_t$ be a Poisson process and fix $s \geq 0$. $\tilde{N_t} = N_{t+s} - N_s$ is also a Poisson process with the same intensity and is independent of $N_r$ for $0 \leq r \leq s$.
- $N_{t_1} - N_{t_0}, \ldots, N_{t_n} - N_{t_{n-1}}$ are all independent.
:::

::: proposition
A stochastic process $N_t$ is a Poisson process with intensity $\lambda$ iff $N_0 = 0$, $N_t - N_s \sim \text{Poi}(\lambda(t - s))$ and $N_t$ has independent increments.
:::

::: definition:Non-homogeneous Poisson process
Let $\lambda : \mathbb{R}^+ \to \mathbb{R}^+$. A stochastic process $N_t$ is a non-homogeneous Poisson process with intensity function $\lambda$ if $N_0 = 0$, $N_t - N_s \sim \text{Poi}\left(\int_s^t \lambda(r)\,dr\right)$ and $N_t$ has independent increments.
:::

::: definition:Compound Poisson process
Let $N_t$ be a Poisson process and $Y_n$ be i.i.d. random variables. A stochastic process $S_t$ is a compound Poisson process if $S_t = Y_1 + \cdots + Y_{N(t)}$.
:::

::: proposition
Let $Y_i$ be i.i.d. random variables, $N$ an independent non-negative integer valued random variable, and when $N = 0$, $S = Y_1 + \cdots + Y_N$. If $\mathbb{E}|Y_1| < \infty$ and $\mathbb{E}|N| < \infty$, then $\mathbb{E}[S] = \mathbb{E}[Y_1]\mathbb{E}[N]$. If $\mathbb{E}|Y_1|^2 < \infty$ and $\mathbb{E}|N|^2 < \infty$, then $\text{Var}[S] = \text{Var}(Y_1)\mathbb{E}[N] + \text{Var}(N)\mathbb{E}[Y_1]^2$. If $N \sim \text{Poi}(\lambda)$, then $\text{Var}(S) = \lambda\mathbb{E}[Y_1^2]$.
:::

::: proposition
If $N_t^y = \sum_{n=1}^{N_t} \mathbf{1}_{\{Y_n = y\}}$ for $y \in S$, then $\{N_t^y\}_{y \in S}$ are independent Poisson processes with rate $\lambda\mathbb{P}(Y_1 = y)$.
:::

::: proposition
If $N_t^i$ are independent Poisson processes with rate $\lambda_i$, then $\sum_{i=1}^n N_t^i$ is a Poisson process with rate $\lambda_1 + \cdots + \lambda_n$.
:::

::: proposition
Let $N_t^i$ be Poisson processes with rate $\lambda_i$ and $N_t = \sum_{i=1}^n N_t^i$. Let $\{\tau_k^i\}_{k=1}^\infty$ be independent exponential random variables with rate $\lambda_i$. Then $X_i = \underset{1 \leq j \leq n}{\arg\min} \tau_i^j$ are independent and $\mathbb{P}(X_i = j) = \frac{\lambda_j}{\lambda_1 + \cdots + \lambda_n}$. Moreover, $N_t^j$ has the same distribution as $\sum_{k=1}^{N_t} \mathbf{1}_{\{X_k = j\}}$.
:::

::: proposition
If $N_t$ is a Poisson process, then for all $0 \leq s \leq t$ and $0 \leq m \leq n$, $\mathbb{P}(N_s = m \mid N_t = n) = \binom{n}{m}\left(\frac{s}{t}\right)^m\left(1 - \frac{s}{t}\right)^{n-m}$.
:::

::: proposition
For a given Poisson process $N_t$, let $\tau_k = \inf\{t > 0 : N(\tau_{n-1} + t) - N(\tau) \geq 1\}$ and $T_k = \tau_1 + \cdots + \tau_k$. Consider independent uniform distributions $U_1, \cdots, U_n$ on $[0, t]$ and their ordered version $U_{(1)}, \cdots, U_{(n)}$. On the set $\{N_t = n\}$, the distribution of $T_1, \cdots, T_n$ is equal to $U_{(1)}, \cdots, U_{(n)}$.
:::

### Continuous Time Markov Chains

#### 1. Continuous Time Markov Chains

::: definition:Continuous time Markov chain
Let $X_t$ be a stochastic process over a countable state space $S$. It is a continuous time Markov chain if $\mathbb{P}(X_{t+s} = y \mid X_s = x, X_{s_n} = x_n, \cdots, X_{s_0} = x_0) = \mathbb{P}(X_t = y \mid X_0 = x)$.
- Transition probability: $p_t(x, y) = \mathbb{P}(X_t = y \mid X_0 = x) = \mathbb{P}_x(X_t = y)$
- jump rate: $q(x, y) := \underset{t \to 0}{\lim} \frac{p_t(x, y) - p_0(x, y)}{t} = \underset{t \to 0}{\lim} \frac{p_t(x, y) - \mathbf{1}_{\{x = y\}}}{t}$
:::

::: definition:Basic assumptions
- 1. Markov chain is almost surely right continuous: $\mathbb{P}\left(\underset{h \downarrow 0}{\lim} X_{t+h} = X_t\right) = 1$
- 2a. Markov chain admits jump rate $q(x, y)$ where $-q(x, x) < \infty$ and $\sum_{y \in S} q(x, y) = 0$.
- 2b. Markov chain admits jump rate where $-\underset{x \in S}{\inf} q(x, y) < \infty$ and $\sum_{y \in S} q(x, y) = 0$.
- If a CTMC satisfies 2a, and jumps finitely many times on any interval almost surely, then it satisfies 2b.
:::

::: proposition
If a CTMC satisfies 2b, and let $\lambda_x = -q(x, x) < \infty$, then the first time the Markov chain leaves the state $x$ has exponential distribution with rate $\lambda_x$. If $\lambda_x = 0$, then the Markov chain never leaves $x$. If $\lambda_x > 0$, then the Markov chain jumps to the state $y \neq x$ with probability $\frac{q(x, y)}{\lambda_x}$.
:::

::: proposition
If a jump rate $q : S \times S \to \mathbb{R}$ is given, where $\sum_{y \neq x} q(x, y) < \infty$ for all $x$, then there exists a CTMC with this jump rate.
:::

::: proposition
Let $T$ be a stopping time with respect to a CTMC $X_t$ with transition probabilities $p_t$. For any $t > 0$, given $\{T < \infty, X_T = x\}$, $X_{T+t}$ is independent of $X_{[0, T]}$ and $\mathbb{P}(X_{T+t} = y \mid T < \infty, X_T = x) = p_t(x, y)$.
:::

#### 2. Kolmogorov’s Equations

::: proposition
For a CTMC, $p_{t+s} = p_t p_s$, that is, $p_{t+s}(x, y) = \sum_{z \in \mathcal{S}} p_t(x, z)p_s(z, y)$.
:::

::: proposition
For a CTMC, $p_t' = Q p_t$ and $p_t' = p_t Q$.
:::

::: definition:Matrix exponential
$e^M = \exp(M) = \sum_{k \geq 0} \frac{M^k}{k!} = \underset{k \to \infty}{\lim} \left(I + \frac{M}{k}\right)^k$
:::

::: proposition
For a CTMC, $p_t = \exp(tQ)$.
:::

#### 3. Limiting Behaviour

::: definition:Irreducible
A CTMC is irreducible if for any states $x, y \in S$, there exists $x = x_0, x_1, \ldots, x_n = y$ s.t. $q(x_k, x_{k+1}) > 0$ for all $0 \leq k < n$.
:::

::: proposition
If a CTMC is irreducible, then $p_t(x, y) > 0$ for all $x, y \in S$ and $t > 0$.
:::

::: proposition
If a CTMC satisfies 1 and 2b, then the following are equivalent:
- CTMC is irreducible.
- Embedded Markov chain is irreducible.
- $p_t(x, y) > 0$ for all $x, y \in S$ and for some $t > 0$.
:::

::: definition:Stationary distribution
$\sum_{y \in \mathcal{S}} \pi(y)p_t(y, x) = \pi(x)$ for all $t > 0$.
:::

::: proposition
If a CTMC is irreducible, then $\pi$ is a stationary distribution iff $\sum_{y \in \mathcal{S}} \pi(y)Q(y, x) = 0$.
:::

::: proposition
If a CTMC is irreducible, then $\pi$ is a stationary distribution iff $\pi(x) = \frac{1}{Z}\frac{\tilde{\pi}(x)}{\lambda_x}$ where $\tilde{\pi}$ is a stationary distribution.
:::

::: proposition
For a CTMC with stationary distribution $\pi$, $\underset{t \to \infty}{\lim} p_t(x, y) = \pi(y)$ and $\underset{t \to \infty}{\lim} \frac{1}{t}\int_0^t \mathbf{1}_{\{X_s = y\}}\,ds = \pi(y)$.
:::

#### 4. Detailed Balance Condition

::: definition:Detailed balance condition
$\pi(x)Q(x, y) = \pi(y)Q(y, x)$
:::

::: proposition
Define $N_t^x := \sum_{k \geq 1} \mathbf{1}_{\{T_k \leq t\}}\mathbf{1}_{\{X_{T_k-} = x\}}$ counting the number of times that the chain is in state $x$ immediately before arrivals. Then for a CTMC, $\underset{t \to \infty}{\lim} \frac{N_t^x}{\lambda t} = \underset{t \to \infty}{\lim} \frac{N_t^x}{N_t} = \pi(x)$.
:::

::: proposition
Let $C = S - (A \cup B)$ be finite. If $\mathbb{P}_C(V_A \wedge V_B) > 0$, then $h(x) = \mathbb{P}_X(V_A < V_B)$ is the unique bounded solution to $h(a) = 1$ for all $a \in A$, $h(b) = 0$ for all $b \in B$, and $\sum_{y \in \mathcal{S}} Q(c, y)h(y) = 0$.
:::

::: proposition
Let $C = S - A$ be finite and $f : S \times S \to \mathbb{R}$ where $f(x, y) \geq 0$, $f(x, x) = 0$. If $\mathbb{P}_C(V_A < \infty) > 0$, then $g(x) := \mathbb{E}_x\left[\sum_{k=1}^{\infty} f(X_{T_{k-1}}, X_{T_k})\mathbf{1}_{\{T_k \leq V_A\}}\right]$ is the unique bounded solution to $g(a) = 0$ for all $a \in A$, and $\sum_{y \in \mathcal{S}} Q(c, y)g(y) + \sum_{y \in \mathcal{S}} Q(c, y)f(c, y) = 0$. In particular, if $f(x, y) = \frac{1}{\lambda_x}\mathbf{1}_{\{x \neq y\}}$, then $g(x) = \mathbb{E}_x[V_A]$ and the equations are $g(a) = 0$ for all $a \in A$, and $\sum_{y \in \mathcal{S}} Q(c, y)g(y) + 1 = 0$.
:::

### Martingales

#### 1. Basic Concept

::: theorem:Doob-Dynkin
Let $X, Y$ be random variables. Then $Y$ is measurable with respect to $\sigma(X)$ iff $Y = h(X)$ for some (Borel) measurable $h : \mathbb{R} \to \mathbb{R}$.
:::

::: proposition
$\mathbb{E}[aX + Y \mid \mathcal{H}] = a\mathbb{E}[X \mid \mathcal{H}] + \mathbb{E}[Y \mid \mathcal{H}]$
:::

::: proposition
If $X \leq Y$ almost surely, then $\mathbb{E}[X \mid \mathcal{H}] \leq \mathbb{E}[Y \mid \mathcal{H}]$.
:::

::: theorem:Jensen's inequality
If $\varphi$ is convex, $\mathbb{E}[|X|] < \infty$ and $\mathbb{E}[|\varphi(X)|] < \infty$, then $\varphi(\mathbb{E}[X \mid \mathcal{H}]) \leq \mathbb{E}[\varphi(X) \mid \mathcal{H}]$.
:::

::: theorem:Tower property
If $\mathcal{H} \subseteq \mathcal{G}$, then $\mathbb{E}[\mathbb{E}[X \mid \mathcal{H}] \mid \mathcal{G}] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}]$.
:::

::: proposition
If $X \in \mathcal{H}$, $\mathbb{E}[|Y|] < \infty$ and $\mathbb{E}[|XY|] < \infty$, then $\mathbb{E}[XY \mid \mathcal{H}] = X\mathbb{E}[Y \mid \mathcal{H}]$.
:::

#### 2. Martingales

::: definition:Martingale
A $(\mathcal{F}, \mathbb{P})$-martingale is a stochastic process $M_t$ s.t. $M$ is adapted to $\mathcal{F}$, $\mathbb{E}[M_t] < \infty$ for all $t$ and $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for all $s < t$.
- submartingale or supermartingale.
:::

::: proposition
Let $\xi_i$ be $1$ with probability $p$ and $-1$ with probability $q$, and $Z_n = \sum_{k=1}^{n} \xi_k$. Then $M_n = Z_n - (p - q)n$ is a martingale.
:::

::: proposition
Let $\xi_i$ be i.i.d. with mean $0$ and variance $\sigma^2$. Then $Z_n = \sum_{k=1}^{n} \xi_k$ and $Z_n^2 - n\sigma^2$ are both martingales.
:::

::: proposition
If $M_n$ is a martingale, and $\phi$ is a convex function where $\mathbb{E}[\phi(M_n)] < \infty$, then $\phi(M_n)$ is a submartingale. In particular, $\phi = x^2$.
:::

::: proposition
If $M_n$ is a submartingale, and $\phi$ is a non-decreasing convex function where $\mathbb{E}[\phi(M_n)] < \infty$, then $\phi(M_n)$ is a submartingale.
:::

::: proposition
If $M_n$ is a martingale where $\mathbb{E}[M_n^2] < \infty$, then $M_n^2 - \sum_{k=1}^{n} \mathbb{E}[(M_k - M_{k-1})^2 \mid \mathcal{F}_{k-1}]$ is a martingale.
:::

::: proposition
If $M_n$ is a martingale where $\mathbb{E}[M_n^2] < \infty$, then for any $0 \leq l \leq k \leq m \leq n$, $\mathbb{E}[(M_n - M_m)M_k] = 0$ and $\mathbb{E}[(M_n - M_m)(M_k - M_\ell)] = 0$.
:::

::: proposition
Let $X_n$ be a discrete Markov chain and $f : \mathbb{N} \times S \to \mathbb{R}$. If $f$ satisfies $\sum_{y \in \mathcal{S}} p^n(x, y)\lvert f(n, y)\rvert < \infty$ and $\sum_{y \in \mathcal{S}} p(x, y)f(n+1, y) = f(n, x)$, then $M_n = f(n, X_n)$ is a martingale.
:::

#### 3. Optional Stopping

::: proposition
If $M_n$ is a martingale and $\rho$ and $\tau$ are stopping times s.t. $\rho < \tau$ and $\underset{R \to \infty}{\lim} \underset{n \in \mathbb{N}}{\sup} \mathbb{E}\left|M_{\tau \wedge n}\mathbf{1}_{\{|M_{\tau \wedge n}| \geq R\}}\right| = 0$ (uniformly integrable), then $\mathbb{E}[M_\tau \mid \mathcal{F}_\rho] = M_\rho$.
- $M_n$ is bounded.
- $\tau$ is bounded.
- $\mathbb{E}[|M_{n+1} - M_n| \mid \mathcal{F}_n]$ is bounded and $\mathbb{E}[\tau] < \infty$.
:::

::: proposition
Let $X_k$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2$ and $S_n = \sum_{k=1}^n X_k$. If $\mathbb{E}[\tau] < \infty$, then $\mathbb{E}[S_\tau] = \mu\mathbb{E}[\tau]$ and $\mathbb{E}[(S_\tau - \mu\tau)^2] = \sigma^2\mathbb{E}[\tau]$.
:::

::: proposition
If $X_n$ is a martingale s.t. $X_n > 0$ and $\lambda > 0$, then $\mathbb{P}\left(\underset{n}{\sup} X_n > \lambda\right) \leq \frac{1}{\lambda}\mathbb{E}X_0$.
:::

::: proposition
If $X_n$ is a submartingale, then there exists a unique martingale $M_n$ and a predictable increasing process $H_n$ with $H_0 = 0$ s.t. $X_n = M_n + H_n$.
:::

::: proposition
If $M_n$ is a martingale and $H_n$ is a predictable bounded process, then $X_n = M_n + H_n$ is a martingale.
:::
