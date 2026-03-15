#Optimization 
Prerequisite knowledge: [[Vector Space]]
## Affine Subspace
> [!definition|] Affine Subsapce
> Let $M\subset \mathbb{R}^{n}$ and $x\in R^{n}$.  

## Convex Set
> [!definition|] Convex
> Let $M\subset \mathbb{R}^{n}$. $M$ is convex if for any $x,y\in M$, $[x,y]\subset M$.

> [!proposition|]
> Let $A\in \mathbb{R}^{n,k}$ and $b\in \mathbb{R}^{n}$. $n$ can be infinite. The set of solution $x$ of $Ax\leqslant b$ is convex.

^654f9c

> [!remark|]
> If we replace some of  $\leqslant$ in [[#^654f9c]] with $<$, the statement still holds. 

> [!definition|] Convex Combination
> Let $y_{1},\cdots ,y_{k} \in \mathbb{R}^{n}$. The convex combinition of $y_{1},\cdots , y_{n}$ is $y=\sum_{i=1}^{k}\lambda_{i}y_{i}$, where  $\lambda_{1}, \cdots , \lambda_{k}>0$ and $\sum_{i=1}^{k}\lambda_{i}=1$.

> [!proposition|]
> Let $M \subset \mathbb{R}^{n}$. $M$ is convex iff every convex combinition of of vectors from $M$ again is a vector from $M$.

> [!proposition|]
> Let $\{M_{\alpha}\}_{\alpha}$ be a family of convex sets in $\mathbb{R}^{n}$. $M=\cap_{\alpha}M_{\alpha}$ is convex.

> [!proposition|]
> Let $M_{1} \subset \mathbb{R}^{n_{1}}$ and $M_{2}\subset \mathbb{R}^{n_{2}}$. If $M_{1}$ and $M_{2}$ are convex, $M_{1}\times M_{2}=\{y=(y_{1},y_{2})\in \mathbb{R}^{n_{n_{1}+n_{2}}}:y_{1}\in M_{1}, y_{2}\in M_{2}\}$ is convex.

> [!proposition|]
> Let $M_{1}, \cdots , M_{k} \subset \mathbb{R}^{n}$. If $M_{1}, \cdots , M_{k}$ are convex, $\lambda_{1}M_{1}+\cdots +\lambda_{k}M_{k}=\{\sum_{i=1}^{k}\lambda_{i}x_{i}:x_{i}\in M_{i}, \lambda_{i}\in \mathbb{R}, i=1,\cdots ,k\}$is convex.

> [!proposition|]
> Let $M\in \mathbb{R}^{n}$, $A\in \mathbb{R}^{m,n}$ and $b\in\mathbb{R}^{m}$. If $M$ is convex, $A(M)=\{y=Ax+b:x\in M\}$ is convex.


> [!proposition|]
> Let $M\in \mathbb{R}^{n}$, $A\in \mathbb{R}^{n,m}$ and $b\in\mathbb{R}^{n}$. If $M$ is convex, $A^{-1}(M)=\{y\in \mathbb{R}^{m}:A(y)\in M\}$ is convex.
> 

> [!definition|] Convex Hull
> Let $M\in \mathbb{R}^{n}$. $M\neq \emptyset$. $\text{Conv}(M)$ is the convex hull of $M$ if $M$ is the intersection of all convex sets containing $M$.

> [!proposition|]
> Let $M\in \mathbb{R}^{n}$. $M\neq \emptyset$. $\text{Conv}(M)=\{\text{all convex combinations of vectors from }M\}$.

## Conic Set
> [!definition|] Conic
> Let $M \subset \mathbb{R}^{n}$. $M \neq \emptyset$. $M$ is conic if for any $x$ in $M$, the ray $Rx=\{tx:t\geq 0\} \subset M$.

> [!definition|] Cone
> Let $M\subset R^{n}$. $M$ is a cone if it is convex and conic.

> [!proposition|] 
> Let $M\subset \mathbb{R}^{n}$. $M\neq \emptyset$. $M$ is a cone iff $M$ is conic and for any $x,y\in M$, $x+y\in M$.

> [!proposition|]
> Let $A\in \mathbb{R}^{n,k}$ and $b\in \mathbb{R}^{n}$. $n$ can be infinite. The set of solution $x$ of $Ax\leqslant 0$ a cone.

> [!definition|] Conic Combination
> Let $y_{1},\cdots ,y_{k} \in \mathbb{R}^{n}$. The conic combinition of $y_{1},\cdots , y_{n}$ is $y=\sum_{i=1}^{k}\lambda_{i}y_{i}$, where  $\lambda_{1}, \cdots , \lambda_{k}>0$.

> [!proposition|]
> Let $M \subset \mathbb{R}^{n}$. $M$ is a cone iff $M\neq\emptyset$ and every conic combinition of of vectors from $M$ again is a vector from $M$.

> [!proposition|]
> Let $\{M_{\alpha}\}_{\alpha}$ be a family of cones in $\mathbb{R}^{n}$. $M=\cap_{\alpha}M_{\alpha}$ is a cone.

> [!definition|] Conic Hull
> Let $M\in \mathbb{R}^{n}$. $M\neq \emptyset$. $\text{Cone}(M)$ is the conic hull of $M$ if $M$ is the intersection of all cones containing $M$.

> [!proposition|]
> Let $M\in \mathbb{R}^{n}$. $M\neq \emptyset$. $\text{Cone}(M)=\{\text{all conic combinations of vectors from }M\}$.

