## Vector
::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a^T b$ is $2n - 1$.
::: ^dot-product-operation-count
::: proof
$n$ multiplication and $n - 1$ addition.
:::

::: proposition
Let $a, b \in \mathbb{R}^n$. The operation count for $a - b$ is $n$.
::: ^vector-subtraction-operation-count

::: proposition
Let $\alpha \in \mathbb{R}$ and $a \in \mathbb{R}^n$. The operation count for $\alpha a$ is $n$.
::: ^scalar-vector-operation-count

::: proposition
Let $q, x \in \mathbb{R}^n$. Assume $P = qq^T$. The operation count for computing $(I - P)x$ is $4n - 1$.
:::
::: proof
$(I - P)x = x - q(q^T x)$, which combines [[#^dot-product-operation-count|the dot-product operation count]], [[#^scalar-vector-operation-count|the scalar–vector operation count]], and [[#^vector-subtraction-operation-count|the vector subtraction operation count]].
:::

## Matrix
::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $B \in \mathbb{R}^{k, m}$. The operation count for $AB$ is $nm(2k - 1)$.
:::
