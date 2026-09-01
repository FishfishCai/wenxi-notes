## Floating Point Number System
::: definition:Idealized Floating Point Number System
Let base (or radix) $\beta \geq 2$ and precision $t \geq 1$. The idealized floating point system is $F = \{0\} \cup \left\{ x \in \mathbb{R} : x = \pm \frac{m}{\beta^t} \beta^e, \ \beta^{t-1} \leq m \leq \beta^t - 1, \ e, m \in \mathbb{Z} \right\}$. The fraction (or mantissa) of $x$ is $\pm \frac{m}{\beta^t}$, and $e$ is the exponent.
:::

::: definition:Machine Epsilon
Let $F$ be an idealized floating point system. The machine epsilon is $\epsilon_{\text{machine}} = \frac{1}{2} \beta^{1-t}$.
:::

::: proposition
Let $F$ be an idealized floating point system. For any $x \in \mathbb{R}$, there exists $x' \in F$ s.t. $|x - x'| \leq \epsilon_{\text{machine}} |x|$.
:::

::: definition:Rounding Map
Let $F$ be an idealized floating point system. The rounding map $\mathrm{fl} : \mathbb{R} \to F$ sends each $x \in \mathbb{R}$ to the closest element of $F$.
:::

::: definition:Floating Point Operation
Let $F$ be an idealized floating point system, $x, y \in F$, and $* \in \{+, -, \times, \div\}$. The floating point operation is $x \circledast y := \mathrm{fl}(x * y)$.
:::

::: theorem:Fundamental Axiom of Floating Point Arithmetic
Let $F$ be an idealized floating point system, $x, y \in F$, and $* \in \{+, -, \times, \div\}$. There exists $\epsilon \in \mathbb{R}$ with $|\epsilon| \leq \epsilon_{\text{machine}}$ s.t. $x \circledast y = (x * y)(1 + \epsilon)$.
:::
