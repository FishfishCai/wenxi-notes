#NumericalLinearAlgebra 
## Floating Point Number System
> [!definition|] Idealized Floating Point Number System
> Let base (or radix) $\beta\ge 2$ and precision $t\ge 1$. The idealized floating point system $F$ is $\{0\}\ \cup\ \Bigl\{\,x\in\mathbb{R}:\ x=\pm (m/\beta^t)\beta^e,\ \beta^{t-1}\le m\le \beta^t-1,\ e,m \in\mathbb{Z}\Bigr\}$. $\pm(m/\beta^t)$ is called the fraction (or mantissa) of $x$, and $e$ is the exponent.

> [!definition|] Machine Epsilon
> Let $F$ be an idealized floating point system. The machine epsilon is $\epsilon = \frac{1}{2}\beta^{1-t}$.

> [!Theorem|]
> Let $F$ be an idealized floating point system. For any $x\in \mathbb{R}$, there exists $x’\in F$ s.t. $|x-x’|\le \epsilon_{\text{machine}}|x|$ .

> [!definition|] Rounding Map
> Let $F$ be an idealized floating point system. Rounding map $\mathrm{fl}:\mathbb{R}\to F$ sends each $x\in\mathbb{R}$ to the closest element in $F$.

> [!definition|] Floating Point Operation
> Let $F$ be an idealized floating point system, $x,y\in F$, and $\circledast \in\{+,-,\times,\div\}$. $x\circledast y:=\mathrm{fl}(x*y)$.

> [!Theorem|] Fundamental Axiom of Floating Point Arithmetic
> Let $F$ be an idealized floating point system and $x,y\in F$. There exists $\epsilon$ with $|\epsilon|\le \epsilon_{\text{machine}}$ s.t. $x\circledast y=(x*y)(1+\epsilon)$.
