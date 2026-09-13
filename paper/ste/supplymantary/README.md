# 补充阅读：以前推荐的其他非二值论文

整理日期：2026-09-09。以下保留本次对话中的概括，并增加本地 PDF 链接。PDF 来自 arXiv，具体版本见 PDF 首页。

下面这些没有消失，但**不再计入满足你全部条件的主要清单**。我们的目标仍然是

$$
q_t=Q(W_t),\qquad W_{t+1}=W_t-\eta_t\nabla f(q_t),
$$

以及最终量化模型的损失 $f(q_T)$。

## 1. Training Quantized Nets: A Deeper Understanding — 2017

[本地 PDF](01_Training_Quantized_Nets_2017_1706.02379.pdf) · [论文原文](https://arxiv.org/html/1706.02379)

- **保留它的用途：**更新式直接匹配，包含多级 rounding；你已经在读，可以作为背景。
- **为什么不是你的目标定理：**§4.2 的主要函数值界控制连续权重的平均点 $f(\bar W_T)$，不是 $f(q_T)$。

## 2. Unified Scaling Laws for Compressed Representations — 2025

[本地 PDF](02_Unified_Scaling_Laws_2025_2506.01863.pdf) · [论文原文](https://arxiv.org/html/2506.01863)

- **保留它的用途：**若接受 Adam/AMSGrad 类更新，这是相关扩展。
- **为什么不是你的目标定理：**保证随机压缩点的梯度范数，不是最终量化损失。

## 3. Quantized Adam with Error Feedback — 2020

[本地 PDF](03_Quantized_Adam_with_Error_Feedback_2020_2004.14180.pdf) · [论文原文](https://arxiv.org/html/2004.14180)

- **保留它的用途：**同样适合研究自适应优化器的扩展。
- **为什么不是你的目标定理：**§3.1.2 控制随机量化点的梯度范数，且更新不是普通 SGD。

## 4. Scheduling Weight Transitions for Quantization-Aware Training — ICCV 2025

[本地 PDF](04_Scheduling_Weight_Transitions_2025_2404.19248.pdf) · [论文原文](https://arxiv.org/html/2404.19248)

- **保留它的用途：**与你“每步只有部分量化坐标发生跳变”的观察最贴近。
- **为什么不是你的目标定理：**主要提出 transition-rate 调度并做实验，没有证明原始 STE 的最终损失保证。

对于你当前的坐标下降思路，**Scheduling Weight Transitions 可以提前读它的机制分析部分**；但应把它当作现象和算法设计参考，不当作收敛理论依据。

## 其他类别

- [主要阅读顺序与适用范围](../01_主要阅读/README.md)
- [其他旧推荐：不纳入主线的原因](../03_其他旧推荐_不纳入主线/README.md)
