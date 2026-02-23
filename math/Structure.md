#Topology
## Topological Structure
> [!definition|] Topology
>  $\mathcal{T}$ is a topology on a set $X$ if:  
> - $\emptyset \in \mathcal{T}$ and $X \in \mathcal{T}$.  
> - $\bigcap_{i=1}^n U_i \in \mathcal{T}$.  
> - $\bigcup_{\alpha \in A} U_\alpha \in \mathcal{T}$.  

> [!definition|] $\sigma$-algebra
>  $\mathcal{M}$ is a $\sigma$-algebra on a set $X$ if:  
> - $X \in \mathcal{M}$.  
> - If $A \in \mathcal{M}$, then $A^c \in \mathcal{M}$.  
> - $\bigcup_{n=1}^\infty A_i \in \mathcal{M}$.  

> [!definition|] Measure
>  Let $X$ is a set and $\mathcal{M}$ is a $\sigma$-algebra on $X$. $\mu:X \to \mathbb{R}$ is a measure on $(X,\mathcal{M})$ if:  
> - $\mu(\emptyset)=0$.  
> - $\mu(A)\ge 0$.  
> - $\mu\!\left(\bigcup_{n=1}^\infty A_i\right)=\sum_{n=1}^\infty \mu(A_i)$.  

> [!definition|] Metric
>  Let $X$ be a set and $x,y\in X$. $\rho: X \times X \to \mathbb{R}$ is a metric if:  
> - $0 \le \rho(x,y) < \infty$.  
> - $\rho(x,y)=0$ iff. $x=y$.  
> - $\rho(x,y)=\rho(y,x)$.  
> - $\rho(x,y) \le \rho(x,z)+\rho(z,y)$.  

## Vector Space
> [!definition|] Vector Space
>  Let $\mathbb{F}$ be a field. A set $V$ is a vector space over $\mathbb{F}$ if there are operations $+: V \times V \to V$ and $\cdot: \mathbb{F} \times V \to V$ such that for all $a,b,c \in V$ and $\lambda,\mu \in \mathbb{F}$:  
> - $a+b=b+a$.  
> - $(a+b)+c=a+(b+c)$.  
> - There exists $0 \in V$ such that $a+0=a$.  
> - If $a \in V$, then there exists $-a \in V$ s.t. $a+(-a)=0$.  
> - $\lambda(a+b)=\lambda a+\lambda b$.  
> - $(\lambda+\mu)a=\lambda a+\mu a$.  
> - $(\lambda\mu)a=\lambda(\mu a)$.  
> - $1a=a$.  

> [!definition|] Inner Product
>  Let $V$ be a vector space over a field $\mathbb{F}$, $\lambda \in \mathbb{F}$, and $a,b,c \in V$. $\langle a, b \rangle$ is an inner products if:
> - $\langle a, b \rangle = \langle b, a \rangle$.
> - $\langle a , a \rangle \ge 0$ and the equality holds when $a=0$.
> - $\langle a, \lambda b + c \rangle = \lambda \langle a, b \rangle + \langle a, c \rangle$

> [!definition|] Norm
>  Let $V$ be a vector space over a field $\mathbb{F}$, $\lambda \in \mathbb{F}$, and $a,b \in V$. $\lVert a \rVert$ is a norm if:  
> - $\lVert a \rVert \ge 0$ and the equality holds when $a=0$.  
> - $\lVert \lambda a \rVert = |\lambda| \, \lVert a \rVert$.  
> - $\lVert a + b \rVert \le \lVert a \rVert + \lVert b \rVert$.  
