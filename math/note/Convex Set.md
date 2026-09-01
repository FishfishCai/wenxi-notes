---
id: k6hy6ca2jqhnww7v
title: Convex Set
tags: []
refs: []
backrefs: []
---
## Affine Subspace
::: definition:Affine Subspace
Let $M \subset \mathbb{R}^{n}$ and $x \in \mathbb{R}^{n}$.
:::

## Convex Set
::: definition:Convex
Let $M \subset \mathbb{R}^{n}$. $M$ is convex if $[x, y] \subset M$ for any $x, y \in M$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^{n}$, where $n$ can be infinite. The set of solutions $x$ of $Ax \leqslant b$ is convex.
:::

::: note
If some of the $\leqslant$ in [[:3]] are replaced with $<$, then the statement still holds.
:::

::: definition:Convex Combination
Let $y_{1}, \cdots, y_{k} \in \mathbb{R}^{n}$. The convex combination of $y_{1}, \cdots, y_{k}$ is $y = \sum_{i=1}^{k} \lambda_{i} y_{i}$, where $\lambda_{1}, \cdots, \lambda_{k} > 0$ and $\sum_{i=1}^{k} \lambda_{i} = 1$.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$. $M$ is convex iff every convex combination of vectors from $M$ is again in $M$.
:::

::: proposition
Let $\{M_{\alpha}\}_{\alpha}$ be a family of convex sets in $\mathbb{R}^{n}$. Set $M = \bigcap_{\alpha} M_{\alpha}$. $M$ is convex.
:::

::: proposition
Let $M_{1} \subset \mathbb{R}^{n_{1}}$ and $M_{2} \subset \mathbb{R}^{n_{2}}$. Assume $M_{1}$ and $M_{2}$ are convex. Then $M_{1} \times M_{2} = \{y = (y_{1}, y_{2}) \in \mathbb{R}^{n_{1} + n_{2}} : y_{1} \in M_{1}, y_{2} \in M_{2}\}$ is convex.
:::

::: proposition
Let $M_{1}, \cdots, M_{k} \subset \mathbb{R}^{n}$. Assume $M_{1}, \cdots, M_{k}$ are convex. Then $\lambda_{1} M_{1} + \cdots + \lambda_{k} M_{k} = \{\sum_{i=1}^{k} \lambda_{i} x_{i} : x_{i} \in M_{i}, \lambda_{i} \in \mathbb{R}, i = 1, \cdots, k\}$ is convex.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$, $A \in \mathbb{R}^{m, n}$ and $b \in \mathbb{R}^{m}$. Assume $M$ is convex. Then $A(M) = \{y = Ax + b : x \in M\}$ is convex.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$, $A \in \mathbb{R}^{n, m}$ and $b \in \mathbb{R}^{n}$. Assume $M$ is convex. Then $A^{-1}(M) = \{y \in \mathbb{R}^{m} : A(y) \in M\}$ is convex.
:::

::: definition:Convex Hull
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $\text{Conv}(M)$ is the convex hull of $M$ if $\text{Conv}(M)$ is the intersection of all convex sets containing $M$.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $\text{Conv}(M) = \{\text{all convex combinations of vectors from } M\}$.
:::

## Conic Set
::: definition:Conic
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $M$ is conic if the ray $Rx = \{tx : t \geq 0\} \subset M$ for any $x \in M$.
:::

::: definition:Cone
Let $M \subset \mathbb{R}^{n}$. $M$ is a cone if it is convex and conic.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $M$ is a cone iff $M$ is conic and $x + y \in M$ for any $x, y \in M$.
:::

::: proposition
Let $A \in \mathbb{R}^{n, k}$ and $b \in \mathbb{R}^{n}$, where $n$ can be infinite. The set of solutions $x$ of $Ax \leqslant 0$ is a cone.
:::

::: definition:Conic Combination
Let $y_{1}, \cdots, y_{k} \in \mathbb{R}^{n}$. The conic combination of $y_{1}, \cdots, y_{k}$ is $y = \sum_{i=1}^{k} \lambda_{i} y_{i}$, where $\lambda_{1}, \cdots, \lambda_{k} > 0$.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$. $M$ is a cone iff $M \neq \emptyset$ and every conic combination of vectors from $M$ is again in $M$.
:::

::: proposition
Let $\{M_{\alpha}\}_{\alpha}$ be a family of cones in $\mathbb{R}^{n}$. Set $M = \bigcap_{\alpha} M_{\alpha}$. $M$ is a cone.
:::

::: definition:Conic Hull
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $\text{Cone}(M)$ is the conic hull of $M$ if $\text{Cone}(M)$ is the intersection of all cones containing $M$.
:::

::: proposition
Let $M \subset \mathbb{R}^{n}$. Assume $M \neq \emptyset$. $\text{Cone}(M) = \{\text{all conic combinations of vectors from } M\}$.
:::
