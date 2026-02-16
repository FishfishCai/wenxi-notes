### Probability

#### 1. Definition

- $\mathbb{P}(E)=\underset{\omega \in E}{\sum}p(\omega)$, where $p:\Omega \to [0,1]$ satisfying that $\Omega$ is countable and $\underset{\omega \in \Omega}{\sum}p(\omega)$.
  - 可以看作$\int_E dp$
- Random variable $X:\Omega \to \mathbb{R}$
- Law of $X$: $\mathcal{L}_X(E)=\mathbb{P}(\{\omega \in \Omega:X(\omega)\in E\})=\mathbb{P}(X^{-1}(E))$, where $E \subset X(\Omega)$

#### 2. Equations

- $\mathbb{P}(A,B) = \mathbb{P}(A)\mathbb{P}(B)$ if $A$ and $B$ are independent
- $\mathbb{P}(A,B|C) = \mathbb{P}(A|C)\mathbb{P}(B|C)$ if $A$ and $B$ are conditionally independent

- $\mathbb{P}(A)=\mathbb{P}(A\mid B)\mathbb{P}(B)$ if $A\subset B$
  - $\mathbb{P}(A)=\sum_i\mathbb{P}(A\mid E_i)\mathbb{P}(E_i)$

- $\mathbb{P}(A,B) = \mathbb{P}(A|B)\mathbb{P}(B)$
  - $\mathbb{P}(A,B,C,D)=\mathbb{P}(A\mid B,C,D)\mathbb{P}(B\mid C,D)\mathbb{P}(C\mid D)\mathbb{P}(D)$

- $\mathbb{P}(A \mid B)=\frac{\sum_{i}\mathbb{P}(A \mid E_i)\mathbb{P}(E_i)}{\mathbb{P}(B)}$

#### 3. Expectation

- $\mathbb{E}[X]=\underset{\omega \in \Omega}{\sum}X(\omega)\mathbb{P}(\omega)=\underset{x \in X(\Omega)}{\sum}x \mathcal{L}_X(x)$
  - 可以看作$\int_\Omega X(\omega)dp$ 和$\int_{R_X}xdl$

- $\mathbb{E}[X]=\sum_i\mathbb{E}[X|B_i]\mathbb{P}(B_i)$
- 计数随机变量: $X = \sum_{k\geq1}1_{X\geq k}$

  - $E(X)=\sum_{k\geq1}\mathbb{P}(X\geq k)$



### Total Variation Distance

#### 1. Definition

- Total variation distance for probability $\mu$, $\nu$ over state space $S$: $d_{TV}(\mu, \nu) = \underset{A \subseteq \mathcal{S}}{\max}|\mu(A) - \nu(A)|$
- Coupling of $\mu$ and $\nu$: distribution $\delta:S\times S\to [0,1]$ such that $\delta(x,S)=\mu(x)$ and $\delta(S,x)=\nu(x)$

#### 2. Theorem

- $d_{TV}(\mu, \nu) = \frac{1}{2} \underset{x \in S}{\sum} |\mu(x) - \nu(x)|$
- $d_{TV}(\mu, \nu) = \frac{1}{2} \underset{}{\sup} \left\{ \underset{x \in S}{\sum} f(x) \mu(x) - \underset{x \in S}{\sum} f(x) \nu(x) \; : \; \underset{x \in S}{\max} |f(x)| = 1 \right\}$

- $d_{TV}(\mu, \nu) = \underset{(X,Y) \text{ is a coupling of } \mu \text{ and } \nu}{\inf} \mathbb{P}(X \neq Y)$



### Markov Chains

#### 1. Definition:

- Stochastic process: $\{X_n\}_{n\in \mathbb{N}}$ with state space $\mathcal{S}$, i.e. $X_n \in \mathcal{S}$
- Path $X$: $n\mapsto X_n$

- Temporally homogeneous discrete Markov Chain with transition matrix $p:S\times S\to[0,1]$: $\mathbb{P}(X_{n+1}=y|X_n=x,X_{n-1}=x_{n-1},...,X_1=x_1)=\mathbb{P}(X_{n+1}=y|X_n=x)=p(x,y)$

- $p^m(x,y)=\mathbb{P}(X_{n+m}=y|X_n=x)$
  - $p^{m+n}(x,y)=\underset{k\in S}{\sum}p^m(x,k)p^n(k,y)$


#### 2. Strong Markov Property

- Stopping time with respect to $X_n$: $T:\Omega \to \mathbb{N}\bigcup{\infty}$ s.t. ${T=n}$ is determined by ${X_0,...,X_n}$.

- Strong Markov property: For Markov chain $X_n$, for any $k\in \mathbb{N}$, $x\in \mathcal{S}$, given $\{X_T=x,T<\infty\}$, $X_{T+k}$ is independent of $\{X_0 ,\cdots, X_T\}$. Moreover, $\mathbb{P}(X_{T+k} =y \mid T< \infty ,X_T = x) =p^k(x,y)$

  - $$
    \begin{align*}
    &\mathbb{P}(X_{T+k} = y \mid T < \infty, X_T = x) \\
    &=\frac{1}{\mathbb{P}(T < \infty, X_T = x)} \sum_{n \geq 1} \sum_{\omega \in S(n,x)} \mathbb{P}\big(X_{T+k} = y \mid \omega = s\big) \mathbb{P}(\omega = s) \\
    &=p^k(x,y)\sum_{n \geq 1} \sum_{\omega \in S(n,x)}\frac{\mathbb{P}(\omega = s)}{\mathbb{P}(T < \infty, X_T = x)}\\
    &=p^k(x,y)
    \end{align*}
    $$
    
  - $\mathbb{P}(X_{T+k} =y \mid T = n ,X_T = x) =p^k(x,y)$

#### 3. Classification of States

- Definition:
  
  - $\mathbb{P}_x(A)=\mathbb{P}(A\mid X_0=x)$
  - $T_y=min\{ n\geq1:X_n=y\}=T_y^1$
  - $T_y^n=min\{n>T_y^{n-1}:X_n=y\}$
  - $\rho_{xy}=\mathbb{P}_x(T_y<\infty)$
  - $N_y = \sum_{n\geq 1}1_{\{X_n=y\}}$
  - $N_y^{T_x}=\sum_{1 \leq n\leq T_x}1_{\{X_n=y\}}$
  - Transient state $x$: $\rho_{xx}<1$
  - Recurrent state $x$: $\rho_{xx}=1$
  - $x$ communicate $y$ ($x\to y$): $\rho_{xy}>0$
    - $\exist m \ s.t.\ p^m(x,y)>0$ 
  - Closed state set $A$: $\forall x\in A,y\notin A, p(x,y)=0$
  - Irreducible state set $A$: $\forall x,y\in A, x\to y$
  
- $\mathbb{P}_x(T_y^k<\infty)=\rho_{xy}\rho_{yy}^{k-1}$

- If $\mathbb{P}_x(T_y\leq k)\geq a>0$ for $\forall x$, then $\mathbb{P}_x(T_y>mk)\leq(1-a)^m$.

- $\mathbb{E}_x(N_y)=\sum_{n \geq1}p^n(x,y)=\frac{\rho_{xy}}{1-\rho_{yy}}$

- $\mathbb{E}_x(N_y^{T_x})=\sum_{n \geq1}\mathbb{P}(X_n= y,n \leq T_x)$

- $\sum_{y\in S}\mathbb{E}_x(N_y^{T_x})=\mathbb{E}_x(T_x)$

- If $\rho_{xy}>0$ and $\rho_{yx}<1$, then $x$ is transient.

- If $\rho_{xy}>1$ and $x$ is recurrent, then $\rho_{yx}=1$.

- If $x\to y$ and $y\to z$, then $x\to z$.

- If the state space $S$ is finite, then it can be written as a disjoint union $S=T\bigcup R_1\bigcup ...\bigcup R_n$ where $T$ is the set of transient states, and $R_i$ is closed irreducable set of recurrent states.

  - If $x$ is recurrent, $x\to y$, then $y$ is recurrent.
  
  
    - If a finite set $A \subset S$ is closed, then there exists at least one recurrent state.
  
      - If $S$ is finite and irreducible, then all the states are recurrent.
  

#### 4. Stationary Distribution

- Definition:

  - Doubly stochastic matrix $P$: $\sum_x P(x, y) = 1$ for all $y\in S$
  - Stationary distribution $\pi$: $\pi(x)=\sum_{y\in S}\pi(y)p(y,x)$ for all $x\in S$

  - Detailed balance condition: $\pi(x) p(x,y) = \pi(y) p(y,x)$

- If $S$ is finite with doubly stochastic matrix, then $\pi(x) = \frac{1}{N}$ is a stationary distribution.

- If $S$ is finite and $x\in S$ is recurrent (or $S$ is countable and $x$ is positively recurrent), then $\pi(y)=\frac{\mathbb{E}_x(N_y^{T_x})}{\mathbb{E}_x(T_x)}$ is a stationary distribution.
- If $S$ is irreducible and has a stationary distribution, then the stationary distribution is unique and is $\pi(x)=\frac{1}{\mathbb{E}_x(T_x)}$.

- If the distribution of $X_0$ is stationary distribution $\pi$, let $\hat{X}_m=X_{n-m}$, then $\hat{X}$ is a MC with $\hat{p}(x,y)=\frac{\pi(y)p(y,x)}{\pi(x)}$.
  - If $\pi$ is detailed balanced or uniform, than $\hat{p}(x,y)=p(x,y)$

- For irreducible $S$, there is a detailed balanced stationary distribution iff for any cycle $x_0,\ x_1\ ,...,\ x_n=x_0$, $\Pi_{i=1}^np(x_{i-1},x_i)=\Pi_{i=1}^np(x_{i},x_{i-1})$

#### 5. Limit Behavior

- Definition:
  - Period: the greatest common divisor of $I_x=\{n\geq1:p^n(n,n)>0\}$, where $x$ is recurrent
  - Aperiodic $x$: a state whose period is $1$
- If $x\to y$ and $y\to x$, then $x$ and $y$ have the same period.
- If $p(x,x)>0$, then $x$ has period $1$.
- If the peroid of $x$ is 1, then there exists $n_0$ such that for all $n\geq n_0$, $n\in I_x$.
- If $S$ is irreducibel, aperiodic and has a stationary distribution $\pi$, then $p^n(x,y)\to \pi(y)$.

#### 6. Exit Distributions and Exit Times

- $A, B \subset S$ s.t. $C = S \setminus (A \cup B)$ is finite and $h:S \to [0,1]$ s.t. $h(a) = 1$ for $a \in A$, $h(b) = 0$ for $b \in B$, and $ h(c) = \sum_{y \in S} p(c, y) h(y)$ for $c \in C$. If $\mathbb{P}_c(V_A \wedge V_B < \infty) > 0$ for all $c \in C$, then $h(x) = \mathbb{P}_x(V_A < V_B)$.
- $A \subset S$ s.t. $C = S \setminus A$ is finite and bounded $g : S \to \mathbb{R}$ s.t. $g(a) = 0$ for $a \in A$ and for $c \in C$, $g(c) = \sum_{y \in S} p(c, y) f(c, y) + \sum_{y \in S} p(c, y) g(y) $ where $f : S \times S \to \mathbb{R}$ is non-negative. If $\mathbb{P}_c(V_A < \infty) > 0$ for $c \in C$, then $ g(x) = \mathbb{E}_x \left[ \sum_{m=1}^{\infty} f(X_{m-1}, X_m) \mathbf{1}_{\{V_A \geq m\}} \right]$.In particular, if $f = 1$, then $g(x) = \mathbb{E}_x[V_A]$.

#### 7. Ergodic Theorem

- If $S$ is irreducible and has a stationary distribution $\pi$ and $f : \mathcal{S} \to\mathbb{R}$ satisfy $\sum_{z \in S} |f(z)| \pi(z) < \infty$, then $\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n} f(X_k) = \mathbb{E}_\pi f := \sum_{x \in \mathcal{S}} f(x) \pi(x)$.
  - If $S$ is irreducible and has a stationary distribution, then $\underset{n\to \infty}{\lim}\frac{N_x^n}{n}=\frac{1}{\mathbb{E}_x(T_x)}=\pi(x)$.

- If $S$ is irreducible and recurrent, then $\underset{n\to \infty}{\lim}\frac{N_x^n}{n}=\frac{1}{\mathbb{E}_x(T_x)}$.
  - If $S$ is irreducible and recurrent, $\underset{n\to \infty}{\lim}\frac{1}{n}\sum_{i=1}^{n}p^i(x,y)\to \pi(y)$.


#### 8. Existence and Uniqueness in Countable State Space

- If $S$ has a stationary distribution, then state $x$ s.t. $\pi(x)>0$ is recurrent.
  - If $S$ is irreducible and transient, then it doesn't have a stationary distribution.



### Poisson Processes

#### 1. Exponential Distribution

- Exponential distribution:

  - $\mathbb{P}(X \leq t) = \left[1 - e^{-\lambda t}\right]\mathbf{1}_{\{t \geq 0\}}$

  - $f_X(t) = \lambda e^{-\lambda t} \mathbf{1}_{\{t \geq 0\}}$

  - $\mathbb{E}(X)=\frac{1}{\lambda}$

  - $\text{Var}(X)=\frac{1}{\lambda^2}$

- $\mathbb{P}(X > t + s \mid X > t) = \mathbb{P}(X > s)$
- $\mathbb{P}\left( \underset{i}{\min} X_i > t \right) =  e^{-(\lambda_1 + \cdots + \lambda_n)t}$
- $\mathbb{P}(\text{argmin }X_i = i) = \frac{\lambda_i}{\lambda_1 + \cdots + \lambda_n}$
- $f_{T_n}(t) = \lambda e^{-\lambda t} \frac{(\lambda t)^{n-1}}{(n-1)!} \mathbf{1}_{\{t \geq 0\}}$ where $T_N = X_1 + ... + X_n$

#### 2. Poisson Process

- Poisson process with intensity $\lambda>0$: $N(t) := \sum_{n \geq 1} \mathbf{1}_{\{T_n \leq t\}} = \max\{n \geq 1 : T_n \leq t\}$
- Poisson distribution:
  - $\mathbb{P}(X = k) = e^{-\lambda} \frac{\lambda^k}{k!},k \geq 0$
  - $\mathbb{E}(X)=\text{Var}(X)=\frac{1}{\lambda}$
- $\sum_{k=1}^{n} X_i \sim \text{Poi}\left( \sum_{k=1}^{n} \lambda_i \right)$
- If $N_t$ is a Poisson process with intensity $\lambda$, then $N_t \sim Poi(\lambda t)$.
- If $N_t$ is a Poisson process with intensity $\lambda$, then $\lim_{t \to \infty} \frac{N_t}{t} = \lambda$ almost surely.
- Let $N_t$ be a Poisson process and fix $s\geq0$. $\tilde{N_t}=N_{t+s}-N_s$ is also a Poisson process with same intensity and is independent of $N_r$ for $0\leq r\leq s$.
  - $N_{t_1}-N_{t_0}$, ..., $N_{t_n}-N_{t_{n-1}}$ are all independent.
- A stochastic process $N_t$ is a Poisson process with intensity $\lambda$ iff. $N_0 = 0$, $N_t-N_s \sim Poi(\lambda(t-s))$ and $N_t$ has independent increments. 
- A stochastic process $N_t$ is a non-homogeneous Poisson process with intensity function $\lambda: \mathbb{R^+}\to\mathbb{R}^+$ if $N_0 = 0$, $N_t-N_s \sim Poi(\int_s^t\lambda(r)dr)$ and $N_t$ has independent increments. 

- $N_t$ is Poisson process and $Y_n$s are i.d.d. random variables. A stochastic process $S_t$ is a compound Poisson process if $S_t = Y_1 + ... + Y_{N(t)}$.
- $Y_i$s are i.d.d. random variables, $N$ is an independent non-negative integer valued random variable and when $N=0$, $S = Y_1+...+ Y_N$. If $\mathbb{E}|Y_1| < \infty$ and $\mathbb{E}|N| < \infty$, then $\mathbb{E}[S] = \mathbb{E}[Y_1] \mathbb{E}[N]$. If $\mathbb{E}|Y_1|^2 < \infty$ and $\mathbb{E}|N|^2 < \infty$, then $Var[S] = Var(Y_1) \mathbb{E}[N] + Var(N) \mathbb{E}[Y_1]^2$. If $N \sim Poi(\lambda)$, then $Var(S) = \lambda \mathbb{E}[Y_1^2]$.
- If $N_t^y=\sum_{n=1}^{N_t}\mathbf{1}_{Y_n=y},y\in S$, then $\{N_t^y\}_{y\in S}$s are independent Poisson process with rate $\lambda\mathbb{P}(Y_1=y)$.
-  If $N_t^i$ are independent Poisson processes with rate $\lambda_i$, then $\sum_{i=1}^nN_t^i$ is a Poisson process with rate $\lambda_1+...+\lambda_n$.
- $N_t^i$s are Poisson processes with rate $\lambda_i$ and $N_t = \sum_{i=1}^nN_t^i$ . Let$\{\tau_k^i\}_{k=1}^\infty$ be independent exponential radom variables with rate $\lambda_i$. Then, $X_i=\underset{1\leq j \leq n}{\text{argmin}}\tau_i^j$ are independent and $\mathbb{P}(X_i=j)=\frac{\lambda_j}{\lambda_1+...+\lambda_n}$. Moreover, $N_t^j$ has the same distribution as $\sum_{k=1}^{N_t}\mathbf{1}_{X_k=j}$.
- If $N_t$ is a Poisson process, for all $0\leq s\leq t$ and $0\leq m \leq n$, $\mathbb{P}(N_s = m|N_t=n)=C(n,m)(\frac{s}{t})^m(1-\frac{s}{t})^{n-m}$
- For a given Poisson process $N_t$, let $\tau_k=\inf\{t > 0 : N(\tau_{n-1} + t) - N(\tau) \geq 1\}$ and $T_k = \tau_1 + \cdots + \tau_k$. Consider independent uniform distributions $U_1, \cdots, U_n$ on $[0, t]$ and their ordered version $U_{(1)}, \cdots, U_{(n)}$. On the set $\{N_t = n\}$, distribution of $T_1, \cdots, T_n$ is equal to $U_{(1)}, \cdots, U_{(n)}$.



### Continuous Time Markov Chains

#### 1. Continuous Time Markov Chains

- Continuous Time Markov Chains: a stochastic process $X_t$ over a countable state space $S$ such that $\mathbb{P}(X_{t+s} = y \mid X_s = x, X_{s_n} = x_n, \cdots, X_{s_0} = x_0) = \mathbb{P}(X_t = y \mid X_0 = x)$.

  - Transition probability: $p_t(x,y) = \mathbb{P}(X_t = y \mid X_0 = x) = \mathbb{P}_x(X_t = y)$
  - jump rate: $q(x,y) := \lim_{t \to 0} \frac{p_t(x,y) - p_0(x,y)}{t} = \lim_{t \to 0} \frac{p_t(x,y) - \mathbf{1}_{\{x=y\}}}{t}$

- Basic assumptions:

  - 1.Markov chain is almost surely right continuous: $\mathbb{P}\left( \lim_{h \downarrow 0} X_{t+h} = X_t \right) = 1$

  - 2a. Markov chain admits jump rate $q(x,y)$ where $-q(x,x)<\infty$ and $\sum_{y\in S}q(x,y)=0$.
  - 2b. Markov chain admits jump rate where $-\inf_{x\in S}q(x,y)<\infty$ and $\sum_{y\in S}q(x,y)=0$.
  - If a CTMC satisfies 2a, and jumps finitely many on any interval almost surely, then it satisfies 2b.

- If CTMC satisfies the 2b, and let $\lambda_x = -q(x,x) < \infty$, then the first time Markov chain leaves the state $x$ has exponential distribution with rate $\lambda_x$. If $\lambda_x=0$, then Markov chain never leaves $x$. And if $\lambda_x>0$, then Markov chain jumps to the state $y\neq x$ with probability $q(x,y)/\lambda_x$.

- If jump rate $q:S\times S \to R$ is given, where $\sum_{y\neq x}q(x,y)<\infty$ for all $x$, then there exists a CTMC with this jump rate.

- Let $T$ be a stopping time with respect to CTMC $X_t$ with transition probabilities $p_t$. For any $t>0$, given $\{T<\infty, X_T = x\}$, $X_{T+t}$ is independent of $X_{[0,T]}$ and $\mathbb{P}(X_{T+t} = y \mid T < \infty, X_T = x) = p_t(x,y)$

#### 2. Kolmogorov’s Equations

- For CTMC, $p_{t+s} = p_t p_s, \text{that is, }p_ {t+s}(x,y) = \sum_{z \in \mathcal{S}} p_t(x,z) p_s(z,y)$.
- For CTMC, $p_t' = Q p_t \text{ and } p_t' = p_t Q$.

- $e^M = \exp(M) = \sum_{k \geq 0} \frac{M^k}{k!} = \lim_{k \to \infty} \left( I + \frac{M}{k} \right)^k$
- For CTMC, $p_t = \exp(tQ)$.

#### 3. Limiting Behaviour

- Irreducible: for any states $x,y \in S$, there

  exists $x=x_0, x_1,...,x_n=y$ such that $q(x_{k},x_{k+1})>0$ for all $0\leq k<n$.

- If CTMC is irreducible, then $p_t(x,y)>0$ for all $x,y\in S$ and $t>0$.
- If CTMC satisfies 1 and 2b, then the following are equivalent:
  - CTMC is irreducible.
  - Embedded MC is irreducible.
  - $p_t(x,y)>0$ for all $x,y\in S$ and for some $t>0$.
- Stationary: $\sum_{y \in \mathcal{S}} \pi(y) p_t(y,x) = \pi(x),\ \forall t > 0$.
- If CTMC is irreducible, then $\pi$ is a stationary distribution iff $\sum_{y \in \mathcal{S}} \pi(y) Q(y,x) = 0$.
- If CTMC is irreducible, then $\pi$ is a stationary distribution iff $\pi(x) = \frac{1}{Z} \frac{\tilde{\pi}(x)}{\lambda_x}$ where $\tilde{\pi}$ is a stationary distribution.
- For CTMC with stationary distribution $\pi$, $\lim_{t \to \infty} p_t(x,y) = \pi(y)\text{ and }\lim_{t \to \infty} \frac{1}{t} \int_0^t \mathbf{1}_{\{X_s = y\}} \, ds = \pi(y)$

#### 4. Detailed Balance Condition

- Detailed balance condition: $\pi(x) Q(x,y) = \pi(y) Q(y,x)$
- Define $N_t^x := \sum_{k \geq 1} \mathbf{1}_{\{T_k \leq t\}} \mathbf{1}_{\{X_{T_k-} = x\}}$ counting the number of times that chain is in state $x$ immediately before arrivals. Then for CTMC, $\lim_{t \to \infty} \frac{N_t^x}{ \lambda t} =  \lim_{t \to \infty} \frac{N_t^x}{N_t} = \pi(x)$.
- $C = S - (A \cup B)$ is finite. If $P_C(V_A \wedge V_B)>0$, then $h(x) = P_X(V_A<V_B)$ is the unique bounded solution to $h(a) = 1, \ \forall a \in A, \ h(b) = 0,\  \forall b \in B, \ \text{and} \ \sum_{y \in \mathcal{S}} Q(c,y) h(y) = 0$.
- $C= S -A $ is finite and $f:S \times S \to R$ where $f(x,y)\geq 0, f(x,x)=0$. If $P_C(V_A<\infty)>0$, then $g(x) := \mathbb{E}_x\left[ \sum_{k=1}^{\infty} f(X_{T_{k-1}}, X_{T_k}) \mathbf{1}_{\{T_k \leq V_A\}} \right]$ is the unique bounded solution to $g(a) = 0, \ \forall a \in A, \ \text{and} \ \sum_{y \in \mathcal{S}} Q(c,y) g(y) + \sum_{y \in \mathcal{S}} Q(c,y) f(c,y) = 0$. In particular, if $f(x,y) = \frac{1}{\lambda_x} \mathbf{1}_{\{x \neq y\}}$, then $g(x) = \mathbb{E}_x[V_A]$ and the equations are $g(a) = 0, \ \forall a \in A, \ \text{and} \ \sum_{y \in \mathcal{S}} Q(c,y) g(y) + 1 = 0$.



### Martingales

#### 1. Basic Concept

- (Doob-Dynkin) Let $X,Y$ be random variables. Then $Y$ is measurable with respect to $\sigma(X)$ iff $Y=h(X)$ for some (Borel) measurable $h:R\to R$.
- $\mathbb{E}[aX + Y \mid \mathcal{H}] = a \mathbb{E}[X \mid \mathcal{H}] + \mathbb{E}[Y \mid \mathcal{H}]$
- If $X \leq Y$ (almost surely, then $\mathbb{E}[X \mid \mathcal{H}] \leq \mathbb{E}[Y \mid \mathcal{H}]$.
- (Jensen's inequality) If $\varphi$ is convex,  $\mathbb{E}[|X|]<\infty$ and $ \mathbb{E}[|\varphi(X)|] < \infty,$ then $\varphi(\mathbb{E}[X \mid \mathcal{H}]) \leq \mathbb{E}[\varphi(X) \mid \mathcal{H}]$.
- (Tower property) If $\mathcal{H} \subseteq \mathcal{G}$, then $\mathbb{E}[\mathbb{E}[X \mid \mathcal{H}] \mid \mathcal{G}] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}]$.
- If $X \in \mathcal{H}$ and $\mathbb{E}[|Y|] < \infty$, \, \mathbb{E}[|XY|] < \infty, then $\mathbb{E}[XY \mid \mathcal{H}] = X \mathbb{E}[Y \mid \mathcal{H}]$.

#### 2. Martingales

- $(F,P)-$martingale: a stochastic process $M_t$ satisfies that $M$ is adapted to $F$, $E[M_t]<\infty$ for all t and $E[M_t|F_S] = M_S$ for all $s<t$.
  - submartingale or supermartingale.
- Let $\xi_i$ be 1 with probability p and be -1 with probability q and $Z_n = \sum_{k=1}^{n} \xi_k$ , then $M_n = Z_n - (p-q)n$ is a martingale.
- Let $\xi_i$ be i.i.d with mean 0 and variance $\sigma^2$, then $Z_n = \sum_{k=1}^{n} \xi_k$ and $Z_n^2 - n\sigma^2$ are both martingales.
- If $M_n$ is a martingale, and $\phi$ is a convex function where $E[\phi(M_n)]<\infty$, then $\phi(M_n)$ is a submartingale. In particular, $\phi = x^2$.
-  If $M_n$ is a submartingale, and $\phi$ is a non-decreasing convex function where $E[\phi(M_n)]<\infty$, then $\phi(M_n)$ is a submartingale.
- If $M_n$ is a martinglae where $E[M_n^2]<\infty$, then $M_n^2 - \sum_{k=1}^{n} \mathbb{E}[(M_k - M_{k-1})^2 \mid \mathcal{F}_{k-1}]$ is a martingale.
- If $M_n$ is a martinglae where $E[M_n^2]<\infty$, then for any $0\leq l \leq k \leq m \leq n$, $\mathbb{E}[(M_n - M_m) M_k] = 0 \ \text{and} \ \mathbb{E}[(M_n - M_m)(M_k - M_\ell)] = 0$.
- $X_n$ is a discrete MC and $f:N\times S \to R$. If $f$ satisfies $\sum_{y \in \mathcal{S}} p^n(x,y) \lvert f(n,y) \rvert < \infty$ and $\sum_{y \in \mathcal{S}} p(x,y) f(n+1,y) = f(n,x)$, then $M_n = f(n,X_n)$ is a martingale.

#### 3. Optional Stopping

- If $M_n$ is a martingale and $\rho$ and $\tau$ are stopping times s.t. $\rho < \tau$ and $\lim_{R \to \infty} \sup_{n \in \mathbb{N}} \mathbb{E} \left| M_{\tau \wedge n} \mathbf{1}_{\{ |M_{\tau \wedge n}| \geq R \}} \right| = 0$ (umiformly integrable), then $\mathbb{E}[M_\tau \mid \mathcal{F}_\rho]= M_\rho$.
  - $M_n$ is bounded.
  - $\tau$ is bounded.
  - $E[|M_{n+1}-M_N||F_n]$ is bounded and $E[\tau]<\infty$.
- Let $X_K$ be i.i.d. random variables the mean $\mu$ and variance $\sigma^2$ and $S_n = \sum_{k=1}^nX_k$. If $E[\tau]<\infty$, then $\mathbb{E}[S_\tau] = \mu \mathbb{E}[\tau]$ and $\mathbb{E}[(S_\tau - \mu \tau)^2] = \sigma^2 \mathbb{E}[\tau]$.
- If $X_n$ is a martingale s.t. $X_n >0$ and $\lambda>0$, then $\mathbb{P}\left( \sup_n X_n > \lambda \right) \leq \frac{1}{\lambda} \mathbb{E}X_0$.

- If $X_n$ is a submartingale, then there exists unique martingale $M_n$ and a predictable increasing process $H_n$ with $H_0 = 0$ s.t. $X_n = M_n +H_n$.
- If $M_n$ is a martingale and $H_n$ is a predictable bounded process, then $X_n = M_n + H_n$ is a martingale.
