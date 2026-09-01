## Least Square
::: theorem:Least Square
Let $A \in \mathbb{R}^{n, k}$, $b \in \mathbb{R}^n$ and $x \in \mathbb{R}^k$. $x$ minimizes $\|b - Ax\|$ iff $A^T A x = A^T b$.
::: ^least-square

::: proof
Let $P$ be the projection matrix onto $\mathrm{range}(A)$. $\|b - b'\|^2 = \|b - Pb\|^2 + \|Pb - b'\|^2 \geq \|b - Pb\|^2$, implying $b'$ minimizes $\|b - b'\|$ iff $b' = Pb$. Since $Ax \in \mathrm{range}(A)$, $x$ minimizes $\|b - Ax\|$ iff $Ax = b'$. $Ax = b'$ is equivalent to $A^T(b - Ax) = 0$.
:::

::: note
For [[#^least-square|Least Square]], if $A$ is full-rank, $x = A^{+} b$.
:::

::: theorem:Least Square via Normal Equations
Let $x$ be the solution of [[#^least-square|Least Square]]. Form $A^T A$ and $A^T b$, compute the Cholesky factorization $A^T A = R^T R$, solve $R^T w = A^T b$ for $w$, and solve $R x = w$ for $x$.
::: ^least-square-normal-equations

::: proposition
The computation of $A^T A$ is $n k^2$ and the computation of the Cholesky factorization is $\frac{1}{3} k^3$. The computation of [[#^least-square-normal-equations|Least Square via Normal Equations]] is approximately $n k^2 + \frac{1}{3} k^3$.
:::

::: theorem:Least Square via QR Factorization
Let $x$ be the solution of [[#^least-square|Least Square]]. Compute the reduced QR factorization $A = \hat{Q} \hat{R}$, compute the vector $\hat{Q}^* b$, and solve the upper-triangular system $\hat{R} x = \hat{Q}^* b$ for $x$.
::: ^least-square-qr

::: proposition
The computation of [[#^least-square-qr|Least Square via QR Factorization]] is approximately $2 n k^2 - \frac{2}{3} k^3$.
:::

::: theorem:Least Square via SVD
Let $x$ be the solution of [[#^least-square|Least Square]]. Compute the reduced SVD $A = \hat{U} \hat{\Sigma} V^*$, compute the vector $\hat{U}^* b$, solve the diagonal system $\hat{\Sigma} w = \hat{U}^* b$ for $w$, and set $x = V w$.
::: ^least-square-svd

::: proposition
The computation of [[#^least-square-svd|Least Square via SVD]] is approximately $2 n k^2 + 11 k^3$.
:::

::: proposition
[[#^least-square-qr|Least Square via QR Factorization]] is backward stable.
:::

::: proof
$b = (\tilde{Q} + \delta Q)(\tilde{R} + \delta R) \tilde{x} = \bigl[\tilde{Q} \tilde{R} + (\delta Q) \tilde{R} + \tilde{Q}(\delta R) + (\delta Q)(\delta R)\bigr] \tilde{x}$. By [[Matrix Factorization#^householder-qr-backward-stability|the backward stability of Householder QR]], $b = \bigl[A + \delta A + (\delta Q) \tilde{R} + \tilde{Q}(\delta R) + (\delta Q)(\delta R)\bigr] \tilde{x}$. Since $\tilde{Q} \tilde{R} = A + \delta A$ and $\tilde{Q}$ is unitary, we have $\frac{\|\tilde{R}\|}{\|A\|} \le \|\tilde{Q}^*\| \frac{\|A + \delta A\|}{\|A\|} = O(1)$ as $\epsilon_{\text{machine}} \to 0$. This gives us $\frac{\|(\delta Q) \tilde{R}\|}{\|A\|} \le \|\delta Q\| \frac{\|\tilde{R}\|}{\|A\|} = O(\epsilon_{\text{machine}})$ and $\frac{\|\tilde{Q}(\delta R)\|}{\|A\|} \le \|\tilde{Q}\| \frac{\|\delta R\|}{\|\tilde{R}\|} \frac{\|\tilde{R}\|}{\|A\|} = O(\epsilon_{\text{machine}})$. Finally, $\frac{\|(\delta Q)(\delta R)\|}{\|A\|} \le \|\delta Q\| \frac{\|\delta R\|}{\|A\|} = O(\epsilon_{\text{machine}}^2)$. The total perturbation $\Delta A$ thus satisfies $\frac{\|\Delta A\|}{\|A\|} \le \frac{\|\delta A\|}{\|A\|} + \frac{\|(\delta Q) \tilde{R}\|}{\|A\|} + \frac{\|\tilde{Q}(\delta R)\|}{\|A\|} + \frac{\|(\delta Q)(\delta R)\|}{\|A\|} = O(\epsilon_{\text{machine}})$.
:::

::: proposition
Let $A, \Delta A \in \mathbb{R}^{n, n}$, $x, y, b, \Delta b \in \mathbb{R}^n$ and $\varepsilon > 0$. If $x$ minimizes $\|b - Ax\|$, $y$ minimizes $\|b + \Delta b - (A + \Delta A) y\|$, $\|\Delta A\| < \varepsilon \|A\|$ and $\|\Delta b\| < \varepsilon \|b\|$, then $\frac{\|y - x\|}{\|x\|} \le \frac{2 \varepsilon \kappa(A)}{1 - \varepsilon \kappa(A)} + \frac{\varepsilon \kappa(A)(\kappa(A) + 1)}{1 - \varepsilon \kappa(A)} \frac{\|b - Ax\|}{\|A\| \|x\|}$.
:::
