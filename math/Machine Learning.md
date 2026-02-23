#Application
Prerequisite knowledge: [[Real Vector]]
## Percepton
> [!theorem|] Novikov's Analysis
> Assume that the training data are linearly separable. That is, there exists a vector $w_N$ with $\|w_N\| = 1$ s.t. for all training samples $(x_i, y_i)$, $y_i \, w_N^\top x_i \ge \varepsilon > 0.$ Assume further that the input vectors are bounded, i.e., $\|x_i\| \le R \text{ for all } i.$ Then the perceptron algorithm makes only finitely many classification mistakes.

`\begin{proof}`
If there is no misclassification, $w_{j}^{\top}w_{j}=w_{j-1}^{\top}w_{j-1}$ and if there is misclassification, $w_{j}^{\top}w_{j}=(w_{j-1}+x_{j}y_{j})^{\top}(w_{j-1}+x_{j}y_{j}) = w_{j-1}^{\top}w_{j-1}+ y_{j}^{2}x_{j}^{\top}x_{j}+2y_{j}w_{j-1}^{\top}x_{j}$, implying $w_{j}^{\top}w_{j}\leqslant w_{j-1}^{\top}w_{j-1}+ x_{j}^{\top}x_{j}$. Since $x_{j}^{\top}x_{j}$ is bounded, then $\|w_{j}\|\leqslant \sqrt{m_{j}}R$. Besides, if there's no misclassification, $w_{N}^{\top}w_{j}=w_{N}^{\top}w_{j-1}$ and if there is misclassification, $w_{N}^{\top}w_{j}=w_{N}^{\top}(w_{j-1}+x_{i}y_{j})=w_{N}^{\top}w_{j-1} + y_i \, w_N^\top x_i$, implying $w_{N}^{\top}w_{j}\geq y_i \, w_N^\top x_i$. Since $\|w_{N}\|\|w_{j}\|\geq |w_{N}^{\top}w_{j}|$, then $\|w_{j}\|\geq m_{j}\varepsilon$. Therefore, $m_{j}\leqslant(\frac{R}{\varepsilon})^{2}$ 
`\end{proof}`
