## Accuracy
::: definition:Absolute Error
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, $\tilde{f} : F_X \to F_Y$, and $x \in F_X$. The absolute error of $\tilde{f}$ at $x$ is $\|\tilde{f}(x) - f(x)\|$.
:::

::: definition:Relative Error
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, $\tilde{f} : F_X \to F_Y$, and $x \in F_X$. The relative error of $\tilde{f}$ at $x$ is $\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|}$.
:::

::: definition:$O(\epsilon_{\text{machine}})$
Let $\mathcal{F}(X)$ be the set of all idealized floating point systems of $X$, $\tilde{f} : \mathcal{F}(X) \times X \to X$, and $\tilde{f}(F, x) \in F$. $\tilde{f} = O(\epsilon_{\text{machine}})$ if there exist $C > 0$ and $\epsilon_0 > 0$ s.t. for all $F$ satisfying $\epsilon_{\text{machine}} < \epsilon_0$ and all $x \in F$, $\|\tilde{f}(F, x)\| \le C \epsilon_{\text{machine}}$.
:::

::: definition:Accuracy
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, and $\tilde{f} : F_X \to F_Y$. $\tilde{f}$ is accurate for $f$ if $\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|} = O(\epsilon_{\text{machine}})$.
::: ^accuracy

## Stability
::: definition:Stability
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, and $\tilde{f} : F_X \to F_Y$. $\tilde{f}$ is stable for $f$ if there exists $\tilde{x} \in F_X$ s.t. $\frac{\|\tilde{x} - x\|}{\|x\|} = O(\epsilon_{\text{machine}})$ and $\frac{\|\tilde{f}(x) - f(\tilde{x})\|}{\|f(\tilde{x})\|} = O(\epsilon_{\text{machine}})$.
::: ^stability

::: definition:Backward Stability
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, and $\tilde{f} : F_X \to F_Y$. $\tilde{f}$ is backward stable for $f$ if there exists $\tilde{x} \in F_X$ s.t. $\frac{\|\tilde{x} - x\|}{\|x\|} = O(\epsilon_{\text{machine}})$ and $\tilde{f}(x) = f(\tilde{x})$.
:::

::: note
For [[#^accuracy|Definition 4 (Accuracy)]] and [[#^stability|Definition 5 (Stability)]], if $\|x\| = 0$, then $\tilde{x} = x$, and if $f(x) = 0$, then $\tilde{f}(x) = f(x)$.
:::

::: note
For [[#^accuracy|Definition 4 (Accuracy)]] and [[#^stability|Definition 5 (Stability)]], in a finite-dimensional space, since all norms are equivalent, they hold regardless of the norm.
:::

::: proposition
$\circledast$ is backward stable.
:::

::: proposition
Let $F_X$ and $F_Y$ be idealized floating point systems of $X$ and $Y$, $f : X \to Y$, $\tilde{f} : F_X \to F_Y$, and $\kappa(x)$ the condition number of $f$ at $x$. If $\tilde{f}$ is backward stable for $f$, then $\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|} = O(\kappa(x) \epsilon_{\text{machine}})$.
:::

::: proof
By the definition of backward stability, $\tilde{f}(x) = f(\tilde{x})$ for some $\tilde{x} \in X$ satisfying $\frac{\|\tilde{x} - x\|}{\|x\|} = O(\epsilon_{\text{machine}})$. By the definition of $\kappa(x)$, this implies $\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|} \le (\kappa(x) + o(1)) \frac{\|\tilde{x} - x\|}{\|x\|}$, where $o(1)$ denotes a quantity that converges to zero as $\|\tilde{x} - x\| \to 0$. Combining these gives the proof.
:::
