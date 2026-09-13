# 其他旧推荐：为什么移出主要清单

整理日期：2026-09-09。以下保留本次对话中的分类理由，并增加完整标题和本地 PDF 链接。本文件夹用于存档，不表示这些论文满足当前研究要求。

当前目标是多级量化下的

$$
q_t=Q(W_t),\qquad W_{t+1}=W_t-\eta_t\nabla f(q_t),
$$

以及最终量化模型的损失 $f(q_T)$。

PDF 来自 arXiv；PV-Tuning 保留此前分析所用的 v2，其余具体版本见 PDF 首页。

## 1. ProxQuant

完整标题：**ProxQuant: Quantized Neural Networks via Proximal Operators**。

[本地 PDF](01_ProxQuant_2019_1810.00861.pdf) · [论文原文](https://arxiv.org/html/1810.00861)

**本次处理理由：**自身方法的收敛定理针对另一个优化器；直接研究原始 STE 固定点的 §5.3 又是二值情形。

## 2. PARQ

完整标题：**PARQ: Piecewise-Affine Regularized Quantization**。

[本地 PDF](02_PARQ_2025_2503.15748.pdf) · [论文原文](https://arxiv.org/html/2503.15748)

**本次处理理由：**虽有 last-iterate 定理，但针对 AProx 的凸正则化目标，不能转用于你的固定硬量化 STE。

## 3. CAGE

完整标题：**CAGE: Curvature-Aware Gradient Estimation For Accurate Quantization-Aware Training**。

[本地 PDF](03_CAGE_2026_2510.18784.pdf) · [论文原文](https://arxiv.org/html/2510.18784)

**本次处理理由：**STE 的 error-feedback 改写值得参考，但它自己的理论算法和指标不能当成原始 STE 的 $f(q_T)$ 保证。

## 4. PV-Tuning

完整标题：**PV-Tuning: Beyond Straight-Through Estimation for Extreme LLM Compression**。

[本地 PDF](04_PV_Tuning_2024_2405.14852v2.pdf) · [论文原文（v2）](https://arxiv.org/html/2405.14852v2)

**本次处理理由：**量化损失下降分析有价值，但采用交替离散优化，改变了更新规则。

## 5. SEA

完整标题：**Straight-Through meets Sparse Recovery: the Support Exploration Algorithm**。

[本地 PDF](05_SEA_2023_2301.13584.pdf) · [论文原文](https://arxiv.org/html/2301.13584)

**本次处理理由：**属于稀疏恢复，不是你的多级 rounding 问题。

## 6. HDA

完整标题：**A network of spiking neurons for computing sparse representations in an energy efficient way**。

[本地 PDF](06_HDA_2012_1210.1530.pdf) · [论文原文](https://arxiv.org/abs/1210.1530)

**本次处理理由：**属于稀疏编码，不是你的多级 rounding 问题。

## 7. Gradient Descent with Compressed Iterates

[本地 PDF](07_Gradient_Descent_with_Compressed_Iterates_2019_1909.04716.pdf) · [论文原文](https://arxiv.org/html/1909.04716)

**本次处理理由：**从压缩点而非连续 latent 点出发更新，算法锚点不同。

## 8. Bengio 2013

完整标题：**Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation**。

[本地 PDF](08_Bengio_STE_2013_1308.3432.pdf) · [论文原文](https://arxiv.org/abs/1308.3432)

**本次处理理由：**STE 的历史和机制背景，你已经读过；不是多级量化终点损失理论。

## 不另行下载的纯二值相关工作

此前提到的 BinaryConnect、BNN、Yin 的二值激活理论、随机二值网络 STE 理论，以及 **Beyond Discreteness、1-bit scaling** 等，按你现在的要求从主阅读清单中删除，本次不另行下载。

这里排除的是**相关理论仅处理二值的工作**，不是看到标题出现 Binary 就一律删除。ProxConnect 的理论框架包含多级量化，因此仍在主要阅读文件夹中；ProxQuant 则仅作为其他旧推荐存档。

## 其他类别

- [主要阅读顺序与适用范围](../01_主要阅读/README.md)
- [补充阅读](../02_补充阅读/README.md)
