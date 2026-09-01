## Topological Structure
::: definition:Topology
Let $X$ be a set and $\mathcal{T}$ be a set of subsets of $X$. $\mathcal{T}$ is a topology on $X$ if:
- $\emptyset \in \mathcal{T}$ and $X \in \mathcal{T}$.
- $\bigcap_{i=1}^{n} U_i \in \mathcal{T}$.
- $\bigcup_{\alpha \in A} U_\alpha \in \mathcal{T}$.
:::

::: definition:$\sigma$-algebra
Let $X$ be a set and $\mathcal{M}$ be a set of subsets of $X$. $\mathcal{M}$ is a $\sigma$-algebra on $X$ if:
- $X \in \mathcal{M}$.
- If $A \in \mathcal{M}$, then $A^c \in \mathcal{M}$.
- $\bigcup_{i=1}^{\infty} A_i \in \mathcal{M}$.
:::

::: definition:Measure
Let $X$ be a set and $\mathcal{M}$ be a $\sigma$-algebra on $X$. $\mu : \mathcal{M} \to [0, \infty]$ is a measure on $(X, \mathcal{M})$ if:
- $\mu(\emptyset) = 0$.
- $\mu(A) \geq 0$.
- $\mu\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mu(A_i)$ if $A_i \cap A_j = \emptyset$ for $i \neq j$.
:::

::: definition:Metric
Let $X$ be a set and $x, y, z \in X$. $\rho : X \times X \to \mathbb{R}$ is a metric if:
- $0 \leq \rho(x, y) < \infty$.
- $\rho(x, y) = 0$ iff $x = y$.
- $\rho(x, y) = \rho(y, x)$.
- $\rho(x, y) \leq \rho(x, z) + \rho(z, y)$.
:::

## Vector Space
::: definition:Vector Space
Let $\mathbb{F}$ be a field and $V$ be a set. $V$ is a vector space over $\mathbb{F}$ if there are operations $+ : V \times V \to V$ and $\cdot : \mathbb{F} \times V \to V$ s.t. for any $a, b, c \in V$ and $\lambda, \mu \in \mathbb{F}$:
- $a + b = b + a$.
- $(a + b) + c = a + (b + c)$.
- There exists $0 \in V$ s.t. $a + 0 = a$.
- If $a \in V$, then there exists $-a \in V$ s.t. $a + (-a) = 0$.
- $\lambda(a + b) = \lambda a + \lambda b$.
- $(\lambda + \mu)a = \lambda a + \mu a$.
- $(\lambda\mu)a = \lambda(\mu a)$.
- $1a = a$.
:::

::: definition:Inner Product
Let $V$ be a vector space over a field $\mathbb{F}$, $\lambda \in \mathbb{F}$, and $a, b, c \in V$. $\langle a, b \rangle$ is an inner product if:
- $\langle a, b \rangle = \langle b, a \rangle$.
- $\langle a, a \rangle \geq 0$ and the equality holds when $a = 0$.
- $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$.
:::

::: definition:Norm
Let $V$ be a vector space over a field $\mathbb{F}$, $\lambda \in \mathbb{F}$, and $a, b \in V$. $\|a\|$ is a norm if:
- $\|a\| \geq 0$ and the equality holds when $a = 0$.
- $\|\lambda a\| = |\lambda| \|a\|$.
- $\|a + b\| \leq \|a\| + \|b\|$.
:::
