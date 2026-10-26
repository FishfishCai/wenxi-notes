::: theorem:Taylor
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$.
$$f(x + p) = f(x) + \int_0^1 \nabla f(x + t p)^T p \, dt$$
and
$$f(x + p) = f(x) + \nabla f(x + t p)^T p \text{ for some } t \in (0, 1).$$
Assume $f \in \mathcal{C}^2$.
$$\nabla f(x + p) = \nabla f(x) + \int_0^1 \nabla^2 f(x + t p) p \, dt,$$
$$f(x + p) = f(x) + \nabla f(x)^T p + \frac{1}{2} p^T \nabla^2 f(x + t p) p \text{ for some } t \in (0, 1)$$
and
$$f(x + p) = f(x) + \nabla f(x)^T p + \int_0^1 (1 - t)p^T \nabla^2 f(x + tp)p \, dt.$$
:::

::: corollary
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x, p \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$.  
$$f(x + p) = f(x) + \nabla f(x)^T p + o(\| p \|).$$
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^1$. If $x^*$ is a local minimizer of $f$, then $\nabla f(x^*) = 0$. Assume $f \in \mathcal{C}^2$, then $\nabla^2 f(x^*) \succeq 0$.
:::

::: proposition
Let $f : \mathbb{R}^n \to \mathbb{R}$ and $x^* \in \mathbb{R}^n$. Assume $f \in \mathcal{C}^2$. If $\nabla f(x^*) = 0$ and $\nabla^2 f(x^*) \succ 0$, then $x^*$ is a strict local minimizer of $f$.
:::
