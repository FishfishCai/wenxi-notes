#LinearAlgebra 
Prerequisite knowledge: [[Structure]], [[Real Vector]]
## Complex Vector
> [!definition|] Inner Product in $\mathbb{C}^{n}$
> Let $a,b\in\mathbb{C}^n$. The inner product  in $\mathbb{C}^{n}$ is $\langle a, b \rangle := b^{*}a$.

> [!definition|] Norm in $\mathbb{C}^{n}$
> Let $a,b\in\mathbb{C}^n$.  The norm in $\mathbb{C}^{n}$ is $\|a\| := \sqrt{\langle a,a \rangle} = \sqrt{a^{*}a}$.
 
> [!lemma|] 
> Let $a,b \in \mathbb{C}^n$. If $\langle a, b \rangle$, then  $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$.

^6241d2

> [!remark|]
> The reverse of [[#^6241d2]] is incorrect. If $\|a+b\|^{2}=\|a\|^{2}+\|b\|^{2}$, then $\Re(a^{*}b)=\Re(b^{*}a)=0$.

> [!remark|]
> [[Real Vector#^9fece5]] is incorrect in $\mathbb{C}^{n}$. If $\|a\|=\|b\|$, $\langle a+b , a-b \rangle = 0$ not always holds.
