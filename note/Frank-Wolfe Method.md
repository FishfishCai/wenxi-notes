::: definition:Frank-Wolfe method
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, and $\gamma_k \in [0, 1]$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, compact, and convex, and $f \in \mathcal{C}^1$. The Frank-Wolfe method generates the iterates $v_k \in \underset{v \in \mathcal{X}}{\arg\min}\nabla f(x_k)^T v$ and $x_{k + 1} = x_k + \gamma_k(v_k - x_k)$.
:::

::: lemma
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x^*, x_0 \in \mathcal{X}$, and $\gamma_k \in [0, 1]$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, compact, and convex, $f$ is convex and $L$-smooth, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $D = \underset{x, y \in \mathcal{X}}{\max}\|x - y\|$ and $\{x_k\}$ as the Frank-Wolfe iterates with steplengths $\gamma_k$. $f(x_{k + 1}) - f(x^*) \leq (1 - \gamma_k)(f(x_k) - f(x^*)) + \frac{LD^2}{2}\gamma_k^2$ for any integer $k \geq 0$.
::: ^frank-wolfe-recurrence

*Proof.*
Smoothness and $\|v_k - x_k\| \leq D$ give
$$
f(x_{k + 1}) \leq f(x_k) + \gamma_k\nabla f(x_k)^T(v_k - x_k) + \frac{L\gamma_k^2}{2}\|v_k - x_k\|^2 \leq f(x_k) + \gamma_k\nabla f(x_k)^T(v_k - x_k) + \frac{LD^2}{2}\gamma_k^2.
$$
Since $v_k$ minimizes $\nabla f(x_k)^T v$ over $\mathcal{X}$, convexity gives
$$
\nabla f(x_k)^T(v_k - x_k) \leq \nabla f(x_k)^T(x^* - x_k) \leq f(x^*) - f(x_k).
$$
Substituting this bound and subtracting $f(x^*)$ gives
$$
f(x_{k + 1}) - f(x^*) \leq f(x_k) - f(x^*) - \gamma_k(f(x_k) - f(x^*)) + \frac{LD^2}{2}\gamma_k^2 = (1 - \gamma_k)(f(x_k) - f(x^*)) + \frac{LD^2}{2}\gamma_k^2.
$$

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, compact, and convex, $f$ is convex and $L$-smooth, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $D = \underset{x, y \in \mathcal{X}}{\max}\|x - y\|$ and $\{x_k\}$ as the Frank-Wolfe iterates with $\gamma_k = \frac{2}{k + 2}$. $f(x_k) - f(x^*) \leq \frac{2LD^2}{k + 2}$ for any integer $k \geq 1$.
:::

*Proof.*
This follows by induction on $k$ from [[#^frank-wolfe-recurrence|Lemma 2]], since $\gamma_0 = 1$ gives $f(x_1) - f(x^*) \leq \frac{LD^2}{2}$.

::: lemma
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, $x_0 \in \mathcal{X}$, and $a_k > 0$ for $k \geq 0$. Assume $\mathcal{X}$ is nonempty, compact, and convex, and $f$ is $L$-smooth. Set $D = \underset{x, y \in \mathcal{X}}{\max}\|x - y\|$, $A_k = \sum_{i = 0}^{k} a_i$, $\{x_k\}$ and $\{v_k\}$ as the Frank-Wolfe iterates with $\gamma_k = \frac{a_k}{A_k}$, $\ell_k = f(x_k) + \nabla f(x_k)^T(v_k - x_k)$, $B_k = \frac{1}{A_k}\sum_{i = 0}^{k} a_i\ell_i$, and $H_k = f(x_{k + 1}) - B_k$. $H_k \leq \frac{LD^2}{2A_k}\sum_{i = 0}^{k}\frac{a_i^2}{A_i}$ for any integer $k \geq 0$.
::: ^weighted-gap-bound

*Proof.*
For $k \geq 1$, $A_k = A_{k - 1} + a_k$ gives
$$
A_kH_k - A_{k - 1}H_{k - 1} = A_k(f(x_{k + 1}) - f(x_k)) - a_k\nabla f(x_k)^T(v_k - x_k).
$$
Smoothness, $x_{k + 1} - x_k = \frac{a_k}{A_k}(v_k - x_k)$, and $\|v_k - x_k\| \leq D$ give
$$
A_k(f(x_{k + 1}) - f(x_k)) \leq a_k\nabla f(x_k)^T(v_k - x_k) + \frac{La_k^2}{2A_k}D^2,
$$
so $A_kH_k - A_{k - 1}H_{k - 1} \leq \frac{La_k^2}{2A_k}D^2$. For $k = 0$, $x_1 = v_0$ and the same argument give $A_0H_0 \leq \frac{La_0^2}{2A_0}D^2$. Summing these inequalities gives the claim.

::: proposition
Let $\mathcal{X} \subseteq \mathbb{R}^n$, $f : \mathbb{R}^n \to \mathbb{R}$, and $x^*, x_0 \in \mathcal{X}$. Assume $\mathcal{X}$ is nonempty, compact, and convex, $f$ is convex and $L$-smooth, and $x^*$ solves $\underset{x \in \mathcal{X}}{\min} f(x)$. Set $D = \underset{x, y \in \mathcal{X}}{\max}\|x - y\|$, $a_k = k + 1$, $A_k = \sum_{i = 0}^{k} a_i$, $\{x_k\}$ and $\{v_k\}$ as the Frank-Wolfe iterates with $\gamma_k = \frac{2}{k + 2}$, $\ell_k = f(x_k) + \nabla f(x_k)^T(v_k - x_k)$, $B_k = \frac{1}{A_k}\sum_{i = 0}^{k} a_i\ell_i$, and $H_k = f(x_{k + 1}) - B_k$. $0 \leq f(x_{k + 1}) - f(x^*) \leq H_k \leq \frac{2LD^2}{k + 2}$ for any integer $k \geq 0$.
:::

*Proof.*
Since $v_i$ minimizes $\nabla f(x_i)^T v$ over $\mathcal{X}$, convexity gives
$$
\ell_i \leq f(x_i) + \nabla f(x_i)^T(x^* - x_i) \leq f(x^*)
$$
for any $0 \leq i \leq k$. Averaging these lower bounds with weights $\frac{a_i}{A_k}$ gives $B_k \leq f(x^*)$, so $0 \leq f(x_{k + 1}) - f(x^*) \leq H_k$ since $x_{k + 1} \in \mathcal{X}$. Since $A_i = \frac{(i + 1)(i + 2)}{2}$, $\gamma_i = \frac{a_i}{A_i}$ and $\frac{a_i^2}{A_i} = \frac{2(i + 1)}{i + 2} \leq 2$, so [[#^weighted-gap-bound|Lemma 4]] gives
$$
H_k \leq \frac{LD^2(k + 1)}{A_k} = \frac{2LD^2}{k + 2}.
$$

::: note
The Frank-Wolfe iterates are sparse: $x_k \in \operatorname{conv}(\{x_0, v_0, \ldots, v_{k - 1}\})$, so when each $v_i$ is an extreme point of $\mathcal{X}$, $x_k$ combines at most $k + 1$ extreme points. On the probability simplex with $x_0$ a vertex, $x_k$ has at most $k + 1$ nonzero entries.
:::
