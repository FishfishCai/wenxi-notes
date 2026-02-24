#NumericalLinearAlgebra 
## Vector
> [!lemma|] 
> Let $a,b\in \mathbb{R}^{n}$. The operation count for $a^{\top}b$ is $2n-1$.

`\begin{proof}`
$n$ multiplication and $n-1$ addition.
`\end{proof}`

> [!lemma|] 
>  Let $a,b\in \mathbb{R}^{n}$. The operation count for $a-b$ is $n$.

^ed7e9f

> [!lemma|] 
>  Let $\alpha \in \mathbb{R}$ and $a\in \mathbb{R}^{n}$. The operation count for $\alpha a$ is $n$.

^592ada

> [!Lemma|]
> Let $q,x \in \mathbb{R}^{n}$. Assume $P = qq^{\top}$. The operation count for computing $(I-P)x$ is $4n-1$.

^dd24b3

`\begin{proof}`
$(I-P)x=x-q(q^{\top}x)$, which is the combinition of [[#^ed7e9f]], [[#^592ada]] and [[#^dd24b3]].
`\end{proof}`

## Matrix
> [!Lemma|]
> Let $A \in \mathbb{R}^{n,k}$ and $B \in \mathbb{R}^{k,m}$. The operation count for $AB$ is $nm(2k-1)$.
