## 一、收敛定理：潜在权重与量化点的上界
以下论文都用一般（general）的手段研究 STE：《QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction》《Unified Scaling Laws for Compressed Representations》《Dynamic Model Pruning with Feedback》《Training Quantized Nets: A Deeper Understanding》。我们根据其中的思路推导出下列结论。各篇提供的思路：QUASAR 先控制潜在权重，用极化恒等式处理梯度失配；Unified Scaling Laws 加减量化点梯度后用 Cauchy–Schwarz 和梯度界处理失配；Dynamic Model Pruning with Feedback 先控制量化点（距离势函数），再用对称过渡不等式换到潜在权重，其中 1.2(a) 对应原文定理 4.1 与附录式 (4)，原文另有非凸情形只控制量化点的梯度范数，原文的剪枝掩码换成 RTN 不影响证明，因为证明只用到梯度取样点和误差 $\|Q(w_t)-w_t\|$；Training Quantized Nets 给出随机舍入下平均潜在权重的界（1.4）。除 1.2(a) 与 1.4 外均为我们的推导。

### 共同设定
- 更新：$w_{t+1}=w_t-\eta_tg_t$，$\mathbb E_t[g_t]=\nabla\mathcal L(Q(w_t))$（GD 时 $g_t=\nabla\mathcal L(Q(w_t))$），$w_t\in\mathbb R^d$。
- 量化：$Q$ 为间距 $\Delta$ 的均匀格点逐坐标最近舍入，不截断，因此 $\|Q(w)-w\|^2\le d\Delta^2/4$。
- $L$-光滑：$\|\nabla\mathcal L(x)-\nabla\mathcal L(y)\|\le L\|x-y\|$，且 $\mathcal L^\star=\inf_x\mathcal L(x)>-\infty$。
- PL：$\|\nabla\mathcal L(x)\|^2\ge2\mu\big(\mathcal L(x)-\mathcal L^\star\big)$。
- $\mu$-强凸：$\mathcal L(y)\ge\mathcal L(x)+\langle\nabla\mathcal L(x),y-x\rangle+\frac\mu2\|y-x\|^2$，最优点 $w^\star$；凸即 $\mu=0$。强凸蕴含 PL。
- 噪声模型 A（相对方差）：$g_t=\nabla\mathcal L(Q(w_t))+\xi_t$，$\mathbb E_t\xi_t=0$，$\mathbb E_t\|\xi_t\|^2\le M\|\nabla\mathcal L(Q(w_t))\|^2+\sigma^2$。GD 即 $M=\sigma=0$。
- 噪声模型 B（二阶矩有界）：$\mathbb E_t\|g_t\|^2\le G^2$。GD 时即量化点梯度有界 $\|\nabla\mathcal L(Q(w_t))\|\le G$。
- 过渡不等式（对任意 $x,y$）：对称过渡 $\mathcal L(y)-\mathcal L^\star\le2\big(\mathcal L(x)-\mathcal L^\star\big)+L\|x-y\|^2$；PL 过渡 $\mathcal L(Q(w))-\mathcal L^\star\le\frac{2L}{\mu}\big(\mathcal L(w)-\mathcal L^\star\big)+\frac{L^2}{\mu}\|Q(w)-w\|^2$。

### 1.1 PL（强凸蕴含 PL，本节结论对强凸同样成立）
#### (a) 噪声模型 A，先控制潜在权重
- 常数步长：$0<\eta<1/[L(1+M)]$。
- 潜在权重：
  $$
  \mathbb E\big[\mathcal L(w_T)-\mathcal L^\star\big]
  \le(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{L\eta\sigma^2}{2\mu}+\frac{L^2d\Delta^2}{8\mu}.
  $$
- 量化模型（PL 过渡）：
  $$
  \mathbb E\big[\mathcal L(Q(w_T))-\mathcal L^\star\big]
  \le\frac{2L}{\mu}(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{L^2\eta\sigma^2}{\mu^2}+\frac{L^3d\Delta^2}{4\mu^2}+\frac{L^2d\Delta^2}{4\mu}.
  $$
- 量化模型（对称过渡）：
  $$
  \mathbb E\big[\mathcal L(Q(w_T))-\mathcal L^\star\big]
  \le2(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{L\eta\sigma^2}{\mu}+\frac{L^2d\Delta^2}{4\mu}+\frac{Ld\Delta^2}{4}.
  $$

#### (b) 噪声模型 B，先控制潜在权重
- 常数步长：$0<\eta\le1/L$。
- 潜在权重：
  $$
  \mathbb E\big[\mathcal L(w_T)-\mathcal L^\star\big]
  \le(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{L\eta G^2}{2\mu}+\frac{L^2d\Delta^2}{8\mu}.
  $$
- 量化模型（对称过渡）：
  $$
  \mathbb E\big[\mathcal L(Q(w_T))-\mathcal L^\star\big]
  \le2(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{L\eta G^2}{\mu}+\frac{L^2d\Delta^2}{4\mu}+\frac{Ld\Delta^2}{4}.
  $$

#### (c) GD + 梯度有界，先控制潜在权重（Cauchy–Schwarz 处理失配）
- 量化点梯度有界：$\|\nabla\mathcal L(Q(w_t))\|_2\le G$；常数步长：$0<\eta\le1/(2L)$。
- 潜在权重：
  $$
  \mathcal L(w_T)-\mathcal L^\star
  \le(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{LG\sqrt d\,\Delta}{2\mu}+\frac{3L^2d\Delta^2}{8\mu}.
  $$
- 量化模型：
  $$
  \mathcal L(Q(w_T))-\mathcal L^\star
  \le(1-\eta\mu)^T\big(\mathcal L(w_0)-\mathcal L^\star\big)+\frac{LG\sqrt d\,\Delta}{2\mu}+\frac{3L^2d\Delta^2}{8\mu}+\frac{G\sqrt d\,\Delta}{2}+\frac{3Ld\Delta^2}{8}.
  $$

#### (d) 噪声模型 A，先控制量化点（在量化点用 PL）
- 常数步长：$0<\eta\le1/[2L(1+M)]$。
- 量化模型：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{2\big(\mathcal L(w_0)-\mathcal L^\star\big)}{\eta\mu T}+\frac{L\eta\sigma^2}{\mu}+\frac{L^2d\Delta^2}{4\mu},
  $$
- 潜在权重：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{4\big(\mathcal L(w_0)-\mathcal L^\star\big)}{\eta\mu T}+\frac{2L\eta\sigma^2}{\mu}+\frac{L^2d\Delta^2}{2\mu}+\frac{Ld\Delta^2}{4}.
  $$

#### (e) 噪声模型 B，先控制量化点（在量化点用 PL）
- 步长：$\eta=\sqrt{\frac{2(\mathcal L(w_0)-\mathcal L^\star)}{LG^2T}}$。
- 量化模型：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{G\sqrt{2L\big(\mathcal L(w_0)-\mathcal L^\star\big)}}{\mu\sqrt T}+\frac{L^2d\Delta^2}{8\mu},
  $$
- 潜在权重：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{2G\sqrt{2L\big(\mathcal L(w_0)-\mathcal L^\star\big)}}{\mu\sqrt T}+\frac{L^2d\Delta^2}{4\mu}+\frac{Ld\Delta^2}{4}.
  $$

### 1.2 强凸（先控制量化点，距离势函数）
#### (a) 噪声模型 B
- 步长：$\eta_t=\frac{4}{\mu(t+2)}$。
- 量化模型与潜在权重：
  $$
  \sum_{t=0}^T\frac{2(t+1)}{(T+1)(T+2)}\,\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{8G^2}{\mu(T+2)}+\frac{3Ld\Delta^2}{4},
  $$
  $$
  \sum_{t=0}^T\frac{2(t+1)}{(T+1)(T+2)}\,\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{16G^2}{\mu(T+2)}+\frac{7Ld\Delta^2}{4}.
  $$

#### (b) 噪声模型 A（GD 取 $M=\sigma=0$）
- 常数步长：$0<\eta\le1/[4L(1+M)]$；权重 $p_t=\frac{(1-\mu\eta/2)^{-(t+1)}}{\sum_{s=0}^{T-1}(1-\mu\eta/2)^{-(s+1)}}$，$t=0,\dots,T-1$。
- 量化模型与潜在权重：
  $$
  \sum_{t=0}^{T-1}p_t\,\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{\mu\|w_0-w^\star\|^2(1-\mu\eta/2)^T}{1-(1-\mu\eta/2)^T}+2\eta\sigma^2+\frac{3Ld\Delta^2}{2},
  $$
  $$
  \sum_{t=0}^{T-1}p_t\,\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{2\mu\|w_0-w^\star\|^2(1-\mu\eta/2)^T}{1-(1-\mu\eta/2)^T}+4\eta\sigma^2+\frac{13Ld\Delta^2}{4}.
  $$

### 1.3 凸（先控制量化点，距离势函数）
凸函数没有 PL，先控制潜在权重的路线得不到损失界，因此只列先控制量化点的结论。
#### (a) 噪声模型 B
- 步长：$\eta=\frac{\|w_0-w^\star\|}{G\sqrt T}$。
- 量化模型与潜在权重：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{2\|w_0-w^\star\|\,G}{\sqrt T}+\frac{Ld\Delta^2}{2},
  $$
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{4\|w_0-w^\star\|\,G}{\sqrt T}+\frac{5Ld\Delta^2}{4}.
  $$

#### (b) 噪声模型 A
- 常数步长：$0<\eta\le1/[4L(1+M)]$。
- 量化模型与潜在权重：
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(Q(w_t))-\mathcal L^\star\big]\le\frac{2\|w_0-w^\star\|^2}{\eta T}+2\eta\sigma^2+Ld\Delta^2,
  $$
  $$
  \frac1T\sum_{t=0}^{T-1}\mathbb E\big[\mathcal L(w_t)-\mathcal L^\star\big]\le\frac{4\|w_0-w^\star\|^2}{\eta T}+4\eta\sigma^2+\frac{9Ld\Delta^2}{4}.
  $$
- GD（$M=\sigma=0$，$\eta=\frac1{4L}$）：量化模型为 $\frac{8L\|w_0-w^\star\|^2}{T}+Ld\Delta^2$，潜在权重为 $\frac{16L\|w_0-w^\star\|^2}{T}+\frac{9Ld\Delta^2}{4}$。

### 1.4 随机舍入下的平均潜在权重（Training Quantized Nets 原文结论）
- 记 $r_t=Q(w_t)-w_t$，$R_T=T^{-1}\sum_{t=1}^T\mathbb E\|r_t\|^2$。Hessian 的 $L_2$-Lipschitz 性给出梯度展开：$\nabla\tilde f(Q(w_t))=\nabla\tilde f(w_t)+\nabla^2\tilde f(w_t)r_t+e_t$，其中 $\|e_t\|\le (L_2/2)\|r_t\|^2$。
- 关键前提是舍入误差条件均值为零，且舍入随机性独立于样本抽取。此时一阶项在取期望后消失；余项使潜在权重到最优点的平方距离递推每步多出至多 $\eta_tDL_2\mathbb E\|r_t\|^2$，其中 $D$ 是定义域直径。用强凸性、梯度二阶矩界 $G^2$、$\eta_t=1/[\mu(t+1)]$ 和望远镜求和，再除以 $T$，得到
  $$
  \mathbb E[F(\bar w_T)-F(w^*)]
  \le \frac{(1+\log(T+1))G^2}{2\mu T}+\frac{DL_2}{2}R_T,
  \qquad \bar w_T=\frac1T\sum_{t=1}^T w_t.
  $$
  因此只要平均平方舍入误差 $R_T$ 不随训练消失，第二项就形成与 $T$ 无关的误差底。原文定理 4 将它写成 $DL_2\sqrt d\,\Delta/2$，但附录从 $\|r_t\|\le\sqrt d\,\Delta$ 推出对 $\|r_t\|^2$ 的同阶界，这一步一般不成立。对间距 $\Delta$ 的逐坐标无偏随机舍入，可直接用 $R_T\le d\Delta^2/4$。上式是按平方误差重新写出的界，并非原文原式。
- 适用范围：原文称定理也覆盖确定性最近邻舍入，但这种舍入通常没有 $\mathbb E[r_t\mid w_t]=0$，一阶项不能按附录的做法消去；即使 $L_2=0$，也不能据此断言确定性 rounding 的误差底为零。结论针对平均潜在权重 $\bar w_T$ 的损失，没有控制最终量化点 $Q(w_T)$ 的损失。

### 1.5 说明
- 随 $T\to\infty$ 趋于 0 的是含 $(1-\eta\mu)^T$、$(1-\mu\eta/2)^T$、$1/T$、$1/\sqrt T$ 的项。含 $\Delta$ 的项与 $T$ 无关，始终保留，因此只能收敛到 $\mathcal L^\star$ 附近的邻域；常数步长下正比于 $\eta$ 的噪声项（含 $\sigma^2$ 或 $G^2$）也保留；取 $\eta\propto1/\sqrt T$ 或递减步长时（1.1(e)、1.2(a)、1.3(a)），噪声并入衰减项。
- 含 $\Delta$ 的项只能靠减小 $\Delta$（增加位宽）降低；噪声项正比于步长 $\eta$，衰减项的速度也由步长决定。
- 先控制哪个点，哪个点的上界更小：1.1(a)(b)(c) 中 $\mathcal L(w)$ 的上界更小，1.1(d)(e)、1.2、1.3 中 $\mathcal L(Q(w))$ 的上界更小。比较的是上界，不是真实损失。
- 较大的上界 $=$ 放大系数 $\times$ 较小的上界 $+$ 只含 $\Delta$ 的过渡项：对称过渡为 $\times2$，另加 $\frac{Ld\Delta^2}{4}$；PL 过渡（1.1(a) 第一个量化式）为 $\times\frac{2L}{\mu}$，另加 $\frac{L^2d\Delta^2}{4\mu}$；1.1(c) 为 $\times1$，另加 $\frac{G\sqrt d\,\Delta}{2}+\frac{3Ld\Delta^2}{8}$。
- 量化下限的量级：用极化恒等式或 Young 不等式处理失配时为 $O(d\Delta^2)$；1.1(c) 用 Cauchy–Schwarz，多出 $O(\sqrt d\,\Delta)$ 的一次项，$\Delta$ 小时占主导；PL 下的下限带因子 $L^2/\mu$，强凸和凸用距离势函数时只带因子 $L$。

## 二、量化点的离散动力学：固定状态、振荡、跳变与转换率

### 《ProxQuant: Quantized Neural Networks via Proximal Operators》
#### 固定量化状态
- 定理 5.3：二值 BinaryConnect 在正步长且 $\sum_t\eta_t=\infty$ 时，量化符号 $s$ 能持续不变，当且仅当每个非零梯度坐标都满足 $\operatorname{sign}(\nabla_iL(s))=-s_i$。固定的是量化符号，潜在权重仍可移动。
- 推广到 rounding（我们的推导）：若固定量化点 $q$，潜在权重会沿 $-\nabla L(q)$ 不断移动。无截断均匀格点的每个舍入区间都有界，因此量化状态最终固定要求 $\nabla L(q)=0$；有限截断格点在边界还允许梯度指向格点外侧。
#### Critical thinking
- 不存在固定量化状态不等于证明振荡；还需分析跳变方向与驻留时间。进一步可尝试为量化点的损失建立带加性余项的长期界，而定理 5.3 本身没有给出这样的界。

### 《Recurrence of Optimum for Training Weight and Activation Quantized Networks》
- 在高斯输入、单隐层、二值激活和二值或三值权重的具体模型中，若目标全精度权重 $W^*$ 不可量化，$Q(W_t)$ 一般不会稳定收敛；论文还构造了始终避开最优量化状态的周期振荡例子。
- 若 $W^*$ 足够接近其最优量化方向，$Q(W_t)$ 会无限次达到最优量化损失，但这只是反复回访，不是最终停在最优状态。深层网络实验观察到量化权重符号振荡，未证明一般 rounding STE 也具有这种最优回访性质。对我们的研究，它主要提供振荡现象和反例，读结论与反例即可。

### 《BinaryRelax: A Relaxation Approach for Training Deep Neural Networks with Quantized Weights》
论文的理论分析无法直接迁移到标准 STE 的分析上，但可以借此得到关于跳变的一些结论。
#### 跳变引起的量化点损失变化（我们的推导）
- 设定：量化点 $x_k=Q(w_k)$，$Q$ 为间距 $\Delta$ 的均匀格点逐坐标最近舍入。第 $k$ 步跳变的坐标集合为 $J$，坐标 $i$ 跳 $m_i\in\mathbb Z\setminus\{0\}$ 格，$x_{k+1}-x_k=\Delta\sum_{i\in J}m_ie_i$，$m_J=(m_i)_{i\in J}$。$\mathcal L$ 二阶连续可微，$H_{JJ}(y)$ 为 $\nabla^2\mathcal L(y)$ 在 $J$ 上的主子矩阵，$y_u=x_k+u(x_{k+1}-x_k)$，
  $$
  \Lambda_J=\max_{u\in[0,1]}\lambda_{\max}\big(H_{JJ}(y_u)\big),\qquad
  \lambda_J=\min_{u\in[0,1]}\lambda_{\min}\big(H_{JJ}(y_u)\big).
  $$
- 一般情形：
  $$
  \Delta\sum_{i\in J}m_i\,\partial_i\mathcal L(x_k)+\frac{\lambda_J}{2}\Delta^2\|m_J\|^2
  \le\mathcal L(x_{k+1})-\mathcal L(x_k)
  \le\Delta\sum_{i\in J}m_i\,\partial_i\mathcal L(x_k)+\frac{\Lambda_J}{2}\Delta^2\|m_J\|^2.
  $$
- 无噪声（$m_i\,\partial_i\mathcal L(x_k)=-|m_i|\,|\partial_i\mathcal L(x_k)|$）且 $|m_i|=1$，记 $\bar g_J=\frac1{|J|}\sum_{i\in J}|\partial_i\mathcal L(x_k)|$：
  $$
  |J|\,\Delta\Big(\frac{\lambda_J\Delta}{2}-\bar g_J\Big)
  \le\mathcal L(x_{k+1})-\mathcal L(x_k)
  \le|J|\,\Delta\Big(\frac{\Lambda_J\Delta}{2}-\bar g_J\Big).
  $$
- Hessian 为 $L_2$-Lipschitz 时：
  $$
  \mathcal L(x_{k+1})-\mathcal L(x_k)
  \le\Delta\sum_{i\in J}m_i\,\partial_i\mathcal L(x_k)+\frac{\Delta^2}{2}\,m_J^\top H_{JJ}(x_k)\,m_J+\frac{L_2}{6}\Delta^3\|m_J\|^3.
  $$

### 《Scheduling Weight Transitions for Quantization-Aware Training》
- 转换率（transition rate）：第 $t$ 步改变格点的量化权重所占的比例，
  $$
  k_t=\frac1d\sum_{i=1}^d\mathbb 1\big[Q(w_t)_i\ne Q(w_{t-1})_i\big],
  $$
  即上文跳变记号中的 $|J|/d$。单步只越过一个转换点时，每个量化权重的变化量只能是 $0$ 或 $\Delta$，因此量化权重每步的平均变化量为 $\Delta\,k_t$。
- 方法：不调度学习率而调度目标转换率 $R_t$。用滑动平均 $K_t=mK_{t-1}+(1-m)k_t$ 估计当前转换率，令 $U_t=\max\big(0,\,U_{t-1}+\eta(R_t-K_t)\big)$，更新 $w_{t+1}=w_t-U_tg_t$。
- 没有理论分析，只有上述启发式推导和实验。

## 三、可借鉴的建模假设

### 《Beyond Discreteness: Sample Complexity Analysis of Straight-Through Estimator for 1-bit Quantization》《Understanding Straight-Through Estimator in Training Activation Quantized Neural Nets》《High-Dimensional Learning Dynamics of Quantized Models with Straight-Through Estimator》
三篇都基于特定模型（特定网络结构、高斯输入、teacher–student 标签、平方损失），结论不能直接推广到一般损失。基于这三篇文章，我们可能可以做出以下两个假设。
- 跳变解耦（来自第三篇的高维集中）：第 $k$ 步跳变 $x_{k+1}-x_k=\Delta\sum_{i\in J}m_ie_i$，$H=\nabla^2\mathcal L(x_k)$，同时跳变坐标之间的非对角耦合近似相消：
  $$
  \sum_{i\ne j\in J}H_{ij}m_im_j\approx0,\qquad\text{即}\qquad (x_{k+1}-x_k)^\top H\,(x_{k+1}-x_k)\approx\Delta^2\sum_{i\in J}H_{ii}m_i^2 .
  $$
  检验：取 Rademacher 随机符号 $s\in\{\pm1\}^d$，有 $\mathbb E_s\big[(s\odot d_k)^\top H(s\odot d_k)\big]=\Delta^2\sum_{i\in J}H_{ii}m_i^2$，其中 $d_k=x_{k+1}-x_k$。检验跳变步上
  $$
  R_k=\frac{d_k^\top H\,d_k}{\mathbb E_s\big[(s\odot d_k)^\top H\,(s\odot d_k)\big]}\approx1 .
  $$
- 输入各向同性（来自前两篇的数据假设，归一化层使之近似成立）：各量化层的输入近似各向同性（旋转不变）。检验：层输入协方差 $\Sigma$ 的有效秩 $\operatorname{tr}(\Sigma)^2/\operatorname{tr}(\Sigma^2)$ 接近输入维数。

## 四、其他理论分析

### 《Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin》
#### 定理与推论的证明思路
- 定理一：初始潜在权重在盆地内，量化点在盆地外。盆地外的法向梯度推动潜在权重靠近流形；量化误差界与小步长保证其加权平方距离在首次进入前每步下降固定量。潜在权重深入盆地后，量化点也必进入。
- 推论一、二：首次进入时的量化损失相对初始全精度损失，分为三类变化：1. 沿流形的两个潜在权重投影点之间的损失变化，近驻点时有上界，额外切向相关性下有下降项；2. 同一步量化点与潜在权重的投影错位；3. 起点和量化终点各自相对投影的盆地平坦性误差，共两次。结论只涉及首次进入时的损失，不证明长期收敛。
#### Critical thinking
1. 定理一只使用梯度取样点与潜在权重的距离界，未用格点结构；可推广到有界扰动的梯度取样，随机扰动是特例。
2. 待核实的现象：QAT 末期量化损失可能低于同一步潜在权重损失。这不违背论文给出的首次进入时、相对初始全精度点的损失上界；同一步损失差及首次进入后的行为仍待分析。

### 《Custom Gradient Estimators are Straight-Through Estimators in Disguise》
- 核心结论：各种自定义的权重梯度估计器与 STE 近似等价，差别只相当于换一个学习率和初始化。
- 设定：只考虑权重量化；均匀量化器间距 $\Delta$；估计器 $\hat Q'$ 在每个量化格子上形状相同，满足 $0<L_-\le\hat Q'\le L_+$，且 $\hat Q'$ 为 Lipschitz。
- SGD：用 $\hat Q'$、学习率 $\eta$、初始化 $w_0$ 训练，与用 STE、学习率 $\alpha\eta$、初始化 $M(w_0)$ 训练近似相同，每步对齐误差只增加 $O(\eta^2)$ 和一个仅依赖量化权重的梯度差项。其中 $[w_-,w_+]$ 为一个量化格子，$w_b$ 为任一格子边界：
  $$
  \alpha=\frac{\Delta}{\int_{w_-}^{w_+}\frac{ds}{\hat Q'(s)}},\qquad M(w)=w_b+\alpha\int_{w_b}^{w}\frac{ds}{\hat Q'(s)} .
  $$
  $M$ 单调且保持格子边界不动，因此两个网络越过边界的时刻几乎相同。
- Adam 等自适应优化器：无需调整学习率和初始化，$\hat Q'$ 与 STE 直接近似等价。
