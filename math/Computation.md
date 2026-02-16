## Vector
> [!lemma|] 
> Operation count for $a^{\top}b$ is $2n-1$.

`\begin{proof}`
$n$ multiplication and $n-1$ addition.
`\end{proof}`

> [!lemma|] 
> Operation count for $a-b$ is $n$.

^ed7e9f

> [!lemma|] 
> Operation count for $\alpha a$ is $n$.

^592ada

> [!lemma|] 
> Operation count for $(I-P)x$ where $P=qq^{\top}$ is $4n-1$.

^dd24b3

`\begin{proof}`
$(I-P)x=x-q(q^{\top}x)$, which is the combinition of [[#^ed7e9f]], [[#^592ada]] and [[#^dd24b3]].
`\end{proof}`
