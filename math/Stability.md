#NumericalLinearAlgebra
Prerequisite knowledge: [[Floating Point Arithmetic]], [[Condition Number]]
## Accuracy
> [!definition|] Absolute Error
> Let $F_{X}$ and $F_{Y}$ be idealized floating point system of $X$ and $Y$, $f:X\to Y$, $\tilde f:F_{X}\to F_{Y}$, and $x\in F_{X}$. The absolute error of $\tilde{f}$ at $x$ is $\|\tilde f(x)-f(x)\|$.

> [!definition|] Relative Error
> Let $F_{X}$ and $F_{Y}$ be idealized floating point system of $X$ and $Y$, $f:X\to Y$, $\tilde f:F_{X}\to F_{Y}$, and $x\in F_{X}$. The relative error of $\tilde{f}$ at $x$ is $\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}$.

> [!definition|] $O(\epsilon_{\text{machine}})$
> Let $\{F\}_{X}$ be the set of all idealized floating point system of $X$ and $\tilde{f}:\{F\}_{X}\times X\to F$. $\tilde{f}(F,x)=O(\epsilon_{\text{machine}})$ iff there exist $C>0$ and $\epsilon_0>0$ s.t. for all $F$ satisfying $\epsilon_{\text{machine}}<\epsilon_0$ and all $x\in F$, $\|\tilde{f}(F,x)\|\le C\epsilon_{\text{machine}}$.

> [!definition|] Accuracy
> Let $F_{X}$ and $F_{Y}$ be idealized floating point system of $X$ and $Y$, $f:X\to Y$, $\tilde f:F_{X}\to F_{Y}$. $\tilde f$ is accurate for $f$ if $\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}=O(\epsilon_{\text{machine}})$.

^babbb2

## Stability
> [!definition|] Stability
> Let $F_{X}$ and $F_{Y}$ be idealized floating point system of $X$ and $Y$, $f:X\to Y$ and $\tilde f:F_{X}\to F_{Y}$. $\tilde f$ is stable for $f$ if there exists $\tilde x\in F_{X}$ s.t. $\frac{\|\tilde x-x\|}{\|x\|}=O(\epsilon_{\text{machine}})$ and $\frac{\|\tilde f(x)-f(\tilde x)\|}{\|f(\tilde x)\|}=O(\epsilon_{\text{machine}})$.

^7e80c6

> [!definition|] Backward Stability
> Let $F_{X}$ and $F_{Y}$ be idealized floating point system of $X$ and $Y$, $f:X\to Y$ and $\tilde f:F_{X}\to F_{Y}$. $\tilde f$ is backward stable for $f$ if there exists $\tilde x\in F_{X}$ s.t. $\frac{\|\tilde x-x\|}{\|x\|}=O(\epsilon_{\text{machine}})$ and $\tilde f(x)=f(\tilde x)$.

> [!remark|]
> For [[#^babbb2]] and [[#^7e80c6]], if $\|x\|=0$, $\tilde{x}=x$ and if $f(x)=0$, $\tilde{f}(x)=f(x)$.

> [!remark|]
> For [[#^babbb2]] and [[#^7e80c6]], in finite dimensional space, since all kinds of norms are equivalent, they are regardless of the norm.

> [!proposition|]
> $\circledast \in\{+,-,\times,\div\}$ is backward stable.

> [!Theorem|]
> Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f:X\to Y$, $\tilde f:F_X\to F_Y$ and $\kappa(x)$ be the condition number of $f$ at $x$. If $\tilde f$ is backward stable for $f$, $\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}=O(\kappa(x)\epsilon_{\text{machine}})$.

`\begin{proof}`
By the definition of backward stability, we have $\tilde f(x)=f(\tilde x)$ for some $\tilde x\in X$ satisfying $\frac{\|\tilde x-x\|}{\|x\|}=O(\epsilon_{\text{machine}})$. And by the definition of $\kappa(x)$, this implies $\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}\le (\kappa(x)+o(1))\frac{\|\tilde x-x\|}{\|x\|},\tag{15.2}$ where $o(1)$ denotes a quantity that converges to zero as $\|\tilde{x}-x\|\to 0$. Combining these gives the proof.
`\end{proof}`
