---
id: abr19znvvmbhgbw1
title: Condition Number
tags: []
refs: []
backrefs: []
---
## Condition Number
::: definition:Condition Number
Let $X$ and $Y$ be normed vector spaces, $f : X \to Y$ and $x \in X$. Assume $f$ is continuous. The condition number of $f$ at $x$ is $\hat{\kappa}(x) := \underset{\delta \to 0}{\lim} \underset{\|\delta x\| \leq \delta}{\sup} \frac{\|\delta f\|}{\|\delta x\|}$.
:::

::: note
For [[:1]], if $f$ is differentiable, then $\hat{\kappa} = \|J(x)\|$.
:::

::: definition:Relative Condition Number
Let $X$ and $Y$ be normed vector spaces, $f : X \to Y$ and $x \in X$. Assume $f$ is continuous. The relative condition number of $f$ at $x$ is $\kappa(x) := \underset{\delta \to 0}{\lim} \underset{\|\delta x\| \leq \delta}{\sup} \frac{\frac{\|\delta f\|}{\|f(x)\|}}{\frac{\|\delta x\|}{\|x\|}}$.
:::

::: note
For [[:2]], if $f$ is differentiable, then $\kappa = \frac{\|J(x)\|\|x\|}{\|f(x)\|}$.
:::

## Condition Number of Matrix
::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $x, b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $A$, the condition number of computing $b$ with $Ax = b$ is $\kappa(x) = \|A\|\frac{\|x\|}{\|b\|} \leq \|A\|\|A^{-1}\|$. If $\|\cdot\| = \|\cdot\|_2$, then equality holds for any $x$ that is a multiple of a right singular vector of $A$ corresponding to the minimal singular value $\sigma_n$.
:::

::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $x, b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $A$, the condition number of computing $x$ with $Ax = b$ is $\kappa(b) = \|A^{-1}\|\frac{\|b\|}{\|x\|} \leq \|A\|\|A^{-1}\|$. If $\|\cdot\| = \|\cdot\|_2$, then equality holds for any $b$ that is a multiple of a left singular vector of $A$ corresponding to the maximal singular value $\sigma_1$.
:::

::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $x, b \in \mathbb{R}^m$. Assume $A$ is nonsingular. Given $b$, the condition number of computing $x$ with $x = A^{-1}b$ is $\kappa(A) = \|A\|\|A^{-1}\|$.
:::

::: definition:Condition Number of Matrix
Let $A \in \mathbb{R}^{n,k}$. Assume $A$ is full-rank. The condition number of $A$ is $\kappa(A) := \|A\|\|A^{+}\|$.
:::

::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $\|\cdot\| = \|\cdot\|_2$. $\kappa(A) = \frac{\sigma_1}{\sigma_n}$, where $\sigma_1$ is the maximal eigenvalue of $A$ and $\sigma_n$ is the minimal eigenvalue of $A$.
:::

::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $\|\cdot\| = \|\cdot\|_2$. $\kappa(A) = 1$ iff $A$ is orthogonal.
:::

::: proposition
Let $A \in \mathbb{R}^{n,n}$ and $\|\cdot\| = \|\cdot\|_2$. If each entry of $A$ is i.i.d. normal with $\mu = 0$ and $\sigma^2 = 1$, then $\log \kappa(A) \sim \log n$.
:::
