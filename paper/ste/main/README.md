# 主要阅读：阅读顺序与适用范围

整理日期：2026-09-09。以下内容保留本次对话中的概括，并增加本地 PDF 链接。文件名前的编号即建议阅读顺序；PDF 来自 arXiv，具体版本见 PDF 首页。

## 我们的研究标准

$$
q_t=Q(W_t),\qquad W_{t+1}=W_t-\eta_t\nabla f(q_t),
$$

其中 $Q$ 是多级量化，最终关心 $f(q_T)$。不能把连续权重损失、平均迭代点、随机迭代点的保证，直接当作最后一步保证。

如果严格要求“上述更新＋多级量化＋预先指定终点 $T$ 的量化损失界”，目前核实到的论文中，QUASAR 最直接。其他值得读的论文各有明确缺口，不能把它们算成同等级的结果。

建议顺序：**QUASAR → Understanding QAT → DPF → ProxConnect → High-Dimensional Dynamics**。

这五篇是合并筛选后的主要阅读路线，不代表“五篇都已证明你的最终目标”，更不代表文献只有五篇。其中 QUASAR 最直接；其他四篇分别补充首次到达、随机输出、一般优化框架和特殊模型动力学。

## 1. QUASAR — 2026：先看与你的最终目标最接近的保证

完整标题：**QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction**。

[本地 PDF](01_QUASAR_2026_2608.13966.pdf) · [论文原文](https://arxiv.org/html/2608.13966)

- **更新式关系：**理论使用在重构权重 $r_t$ 处计算梯度、更新连续权重的 SGD。将候选重构集合取为单元素 $\{Q(W_t)\}$，即可对应你的固定量化器。这是对其理论框架的特化，不是说 QUASAR 的实际方法就是普通 STE。
- **结论对象：**Corollary 1 明确控制最后的 $\mathbb E[f(r_T)-f^\star]$，不是随机挑选某次迭代。
- **主要假设：**光滑性、梯度噪声控制、重构误差对应的梯度偏差控制，以及额外的 PL 条件。
- **局限：**结论通常是“衰减项＋量化误差项＋随机噪声项”，不等于固定精度下收敛到离散最优解。

**阅读位置：§5，尤其 §5.3、Corollary 1，以及对应证明。**

你首先需要知道：已有论文为了得到你想要的最终保证，究竟使用了什么假设、付出了什么误差项。

## 2. Understanding Quantization-Aware Training — 2026：同一个更新式，但终点是特殊时刻

完整标题：**Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin**。

[本地 PDF](02_Understanding_QAT_2026_2606.09012.pdf) · [论文原文](https://arxiv.org/html/2606.09012)

- **更新式：**与你的确定性更新直接一致。
- **结论对象：**确实控制 $f(Q(W_T))$。
- **关键区别：**这里的 $T$ 是量化轨迹**第一次进入低损失区域的时刻**，不是任意预先指定的训练终点。
- **主要假设：**低损失区域具有特定几何结构、梯度指向该区域、量化误差相对区域宽度足够小，以及合适的预训练初始化。

**阅读位置：§2 的几何假设 → §3.2 → Theorem 1 → Corollaries 1–2。**

它适合回答“STE 为什么能把量化后的坏模型拉回低损失区域”，但不能自动回答“之后训练到任意 $T$ 都好吗”。

## 3. Dynamic Model Pruning with Feedback — 2020：保留，不能仅因标题是剪枝而排除

完整标题：**Dynamic Model Pruning with Feedback**。

[本地 PDF](03_Dynamic_Model_Pruning_with_Feedback_2020_2006.07253.pdf) · [论文原文](https://arxiv.org/html/2006.07253)

这里需要修正此前过于简单的分类：**论文 §4 明确说明，分析可以扩展到一般压缩算子，包括量化器。** 因而它不只是一个剪枝类比。

- **更新式：**

  $$
  W_{t+1}=W_t-\eta_t g(\mathcal C(W_t)),
  $$

  取 $\mathcal C=Q$，就是你的 SGD 版本。
- **主要假设：**光滑目标、无偏随机梯度及有界二阶矩、压缩误差控制；函数值保证另外使用强凸性。
- **结论对象：**Theorem 4.1 控制**随机选取的压缩迭代点的损失**；非凸结果控制随机压缩点的梯度范数。
- **缺口：**不是最后 $q_T$ 的损失保证。

**阅读位置：§3 更新式 → §4 Theorems 4.1–4.2 → “Extension to Other Compression Schemes” → 附录证明。**

这篇的证明相对直接，适合作为你自己推导多级量化损失界的基础。

## 4. ProxConnect — NeurIPS 2021：恢复到清单，但不要误用其收敛结论

完整标题：**Demystifying and Generalizing BinaryConnect**。

[本地 PDF](04_ProxConnect_2021_2110.13220.pdf) · [论文原文](https://arxiv.org/html/2110.13220)

**标题包含 BinaryConnect，但理论框架并不限于正负二值量化。**

- **更新式：**原文公式 (2)–(3) 与你的更新对应；一般框架可以包含多级离散集合上的硬投影。
- **价值：**解释连续权重的梯度累积、量化点的选择，以及它们与 dual averaging 的关系。
- **结论边界：**Theorem 5.1 给出一般不等式；损失凸时，Corollary 5.2 给出涉及量化迭代点的 best-iterate 界。
- **必须注意：**更简洁的收敛界还要求正则项凸；多点离散集合的指示函数不满足这一条件。因此不能直接宣称一般硬 rounding 的最终损失收敛。

**阅读位置：§2 → §4.2 → §5 的 Theorem 5.1、Corollary 5.2。**

对于你希望从 coordinate descent 角度分析的问题，它的重要性在于：先弄清楚“历史梯度累积＋离散点选择”已有怎样的数学解释。

## 5. High-Dimensional Learning Dynamics… — 2025：看多级量化轨迹如何演化

完整标题：**High-Dimensional Learning Dynamics of Quantized Models with Straight-Through Estimator**。

[本地 PDF](05_High_Dimensional_Learning_Dynamics_2025_2510.10693.pdf) · [论文原文](https://arxiv.org/html/2510.10693)

- **不是仅二值：**包含多 bit 量化和位宽影响。
- **更新式：**在其线性回归模型下，是量化权重处计算梯度、更新连续权重的在线 SGD。
- **研究对象：**量化模型的预测误差及训练动力学，不只是连续权重的损失。
- **主要假设：**高斯数据、teacher–student 线性模型、新鲜独立样本；简化动力学还使用额外的各向同性假设。
- **缺口：**主要是高维极限、有限缩放时间内的动力学近似与固定点分析，不是一般有限维问题的最后一步损失界。

**阅读位置：模型定义与更新式 → §V 的假设和 Theorem V.3 → §VI-A 的 weight-only quantization。**

这篇放后面，因为模型假设较强，但它能帮助你理解量化轨迹的停滞、跳变和误差平台。

## 其他类别

- [补充阅读](../02_补充阅读/README.md)
- [其他旧推荐：不纳入主线的原因](../03_其他旧推荐_不纳入主线/README.md)
