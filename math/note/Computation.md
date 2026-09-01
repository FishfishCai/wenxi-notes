## Vector
::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a^T b$ is $2n - 1$.
::: ^1
::: proof
$n$ multiplication and $n - 1$ addition.
:::

::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a - b$ is $n$.
::: ^2

::: proposition
Let $\alpha \in \mathbb{R}$ and $a \in \mathbb{R}^n$. The operation count for $\alpha a$ is $n$.
::: ^3

::: proposition
Let $q, x \in \mathbb{R}^n$. Assume $P = qq^T$. The operation count for computing $(I - P)x$ is $4n - 1$.
:::
::: proof
$(I - P)x = x - q(q^T x)$, which combines the [[#^1|Proposition 1]], [[#^2|Proposition 2]] and [[#^3|Proposition 3]].
:::

## Matrix
::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $B \in \mathbb{R}^{k, m}$. The operation count for $AB$ is $nm(2k - 1)$.
:::
