# Note
#### Smooth Manifold ([[Differential Topology.pdf#page=12&selection=0,0,7,4|Milnor, p.12]])
- Smooth: $U \subset R^k$ and $V\subset R^l$ are open sets. For $f: U \rightarrow V$, all partial derivatives exist and are continuous.
	- $M \subset R^k$ and $N\subset R^l$. For $f: M \rightarrow N$, for each $x\in X$, there exists an open set $U\subset R^k$ containing $x$ and a smooth mapping $F:U\rightarrow R^l$ that coincides with $f$ on $U \cap X$.
		- Extention: $F$.
	- The composition of smooth functions are smooth.
- Diffeomorphism: $M \subset R^k$ and $N\subset R^l$. For $f: M \rightarrow N$, $f$ is homeomorphism and both $f$ and $f^{-1}$ are smooth.
- Smooth manifold: For $M \subset R^k$, for each $x\in M$, there exits a neighborhood $W$ of $x$ such that $W\cap M$ is diffeomorphic to an open set $U$ of $R^m$.
	- Parametrization: the diffeomorphism $g: U \rightarrow W \cap M$.
	- Coordinate: the inverse diffeomorphism $g: W \cap M \rightarrow U$.
#### Tangent Space ([[Differential Topology.pdf#page=13&selection=236,0,242,11|Milnor, p.13]])
- Derivative: $U \subset R^k$ and $V\subset R^l$ are open sets. For smooth $f: U \rightarrow V$, $df_x:R^k\rightarrow R^l$, $df_x(h)=\lim_{t \to 0} \frac{f(x + t h) - f(x)}{t}$.
	- $df_x$ is a linear mapping.
	- Chain rule: $d(g\circ f)_x = dg_y\circ df_x$ with $f(x)=y$.
- $U \subset R^k$ and $V\subset R^l$ are open sets. If there exists a diffeomorphism $f$ between $U$ and $V$, then $k=l$ and $df_x$ is nonsingular.
	- Connected smooth manifold's dimension is invariant.
- Tangent space: For smooth manifold $M\subset R^k$ with dimension of $m$, $TM_x$ is $\text{Image}\,dg_u(R^m)$, where $g: U\rightarrow M\subset R^k$ is a parametrization.
	- The rank of $TM_x$ is $m$.
	- $TM_x$ is independent of $g$.
- Derivative: $M \subset R^k$ and $N\subset R^l$. For smooth $f: M \rightarrow N$, $df_x: TM_x \rightarrow TN_y$, $df_x=dF_x$, where $F_x$ is the extention of $f_x$.
	- $df_x$ is independent of $F$.
	- Chain rule: $d(g\circ f)_x = dg_y\circ df_x$ with $f(x)=y$.
	- $M \subset R^k$ and $N\subset R^l$. If there exists a diffeomorphism $f$ between $M$ and $N$, then $k=l$ and $df_x$ is an isomorphism.
#### Regular Value ([[Differential Topology.pdf#page=18&selection=159,0,161,6|Milnor, p.18]])
- $f:M\rightarrow N$ is a smooth map between manifolds.
	- Regular point:  $x\in M$ and $df_x$ is surjective.
	- Regular value: $y\in N$ and $f^{-1}(y)$ contains only regular points.
		- $M$ and $N$ has same dimension. If $M$ is compact and $y$ is a regular value, then $f^{-1}(y)$ is finite.
			- $\#f^{-1}(y)$: the number of points in $f^{-1}(y)$.
			- There exists a neighborhood $V \subset N$ of y such that $\#f^{-1}(y) = \#f^{-1}(y')$ for all $y' \in V$.
	- Critical point: $x\in M$ and $df_x$ is not surjective.
	- Critical value: $y\in N$ and one of $f^{-1}(y)$ is critical point.