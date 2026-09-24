# STE / QAT 论文索引

整理日期：2026-09-23。按**实际分析的更新规则和结论**分类，不以标题中的 STE、QAT 或 PTQ 字样判断。前三类围绕训练动力学；第四类保留能帮助理解量化损失的 PTQ 分析。`Note.md` 是阅读笔记。

## 阅读顺序：标准权重 STE 的收敛理论

判断标准：保留全精度变量 W，在硬量化点 Q(W) 计算梯度，再用该梯度更新 W；核对定理证明的是否正是这个更新，以及结论控制的是 W、Q(W)、平均迭代点、驻点还是固定点。作者提出的软量化、重建、剪枝等新方法的收敛定理不计入。仅能把通用定理代入 Q 的论文单列为参考，不冒充原文证明了标准 QAT。

直接给原始更新提供收敛或误差界的论文，未读部分按下表排序；排序兼顾定理的普遍性和与权重硬舍入的相关度。

| 顺序 | 论文 | 读法 | 原始 STE 的定理与限制 |
| --- | --- | --- | --- |
| 已读 | Training Quantized Nets: A Deeper Understanding | §4.2、附录 | Eq. (7) 是原始 BinaryConnect；定理 3、4 在凸性等假设下控制平均全精度 W 的目标值，留有量化误差底，不证明部署点 Q(W) 收敛。确定性最近邻舍入对应的证明缺口见 `Note.md`。 |
| 1 | BinaryRelax | §2.5、§4、定理 4.10 证明 | 第 4 节明确只分析第二阶段，它恰是原始 BinaryConnect；非凸 L-smooth 下，在量化集合为若干直线并集及额外几何条件下，得到相邻量化点差趋零和近似驻点界。不是一般固定格点舍入的无条件收敛。 |
| 2 | Unified Scaling Laws for Compressed Representations | §3、定理 1 证明 | 直接设定“在 C(W) 取梯度、更新 W”的 STE–Adam 型更新，而非新的量化训练方法；非凸 L-smooth 下控制压缩点的期望梯度范数，界中保留压缩误差。优化器含最大二阶矩操作，压缩器 C 很一般，并未利用格点结构。 |
| 3 | Beyond Discreteness | §3–5、相关证明 | 原始潜在 W 加硬量化权重的 STE 更新；在特定二层高斯教师、一位权重和激活模型中，证明量化后的时间平均状态可恢复最优值，最后的量化状态可反复访问最优值。这不是一般多级舍入的收敛定理。 |

直接研究原始 STE，但结论不是上述意义的正面收敛界：ProxQuant §5.3 给二值 BinaryConnect 的固定点存在条件，并允许不收敛；Recurrence of Optimum 证明特殊教师模型中的反复访问和振荡；Understanding Quantization-Aware Training（已读）证明量化点有限时间进入低损失盆地，而非整个轨迹收敛；High-Dimensional Learning Dynamics 给特殊线性模型的高维极限动力学；Custom Gradient Estimators 比较代理导数与 identity STE 的量化状态轨迹。Understanding STE in Training Activation Quantized Neural Nets 仅分析激活量化，不属于这里的权重舍入问题。

不列入标准 STE 收敛优先顺序：QUASAR 的定理针对其选择的重建点，虽可通过单候选点作形式特化，却未单列原始 QAT 保证；Dynamic Model Pruning with Feedback 的定理针对剪枝，虽明确讨论推广到量化，仍须另核硬舍入是否满足压缩误差条件；Demystifying and Generalizing BinaryConnect 的收敛推论需要凸正则项，离散量化集合的指示函数不满足该条件。PARQ、CAGE、PV-Tuning、Mirror Descent View、Forward and Backward Proximal Quantizers 分析各自改进的算法；Gradient Descent with Compressed Iterates 更新的是已压缩点；Scheduling Weight Transitions 和 Overcoming Oscillations 主要分析机制而无原始 STE 的一般收敛定理；两篇 PTQ 论文不分析 STE 训练。

## 1. 原始 STE 的动力学与理论（`ste-dynamics/`）

- **Training Quantized Nets - A Deeper Understanding**：直接分析 BinaryConnect/STE 更新；用强凸性和 Hessian 正则性控制平均潜在权重的损失，并留下量化误差项。其消去一阶误差的证明需要无偏舍入，确定性最近邻舍入不能直接沿用，详见 `Note.md`。
- **Recurrence of Optimum for Training Weight and Activation Quantized Networks**：分析保留全精度权重、在量化权重处取粗梯度、再投影到二值/三值权重的更新；在特定高斯教师模型中证明量化状态反复到达最优点，也证明它一般未必收敛到一个固定量化状态。
- **Custom Gradient Estimators are Straight-Through Estimators in Disguise**：对均匀最近邻舍入，证明正的代理导数与 identity STE 经步长和初始化变换后可有近似相同的格点轨迹；研究的是 STE 的性质，不是目标函数收敛。
- **Unified Scaling Laws for Compressed Representations**：虽然主题是压缩表示的 scaling law，但其中的定理在非凸 L-smooth 假设下直接分析在压缩点取梯度、更新全精度权重的 STE–Adam，界中保留量化误差项；不能据此推出固定粗格点下梯度趋零。
- **Understanding Straight-Through Estimator in Training Activation Quantized Neural Nets**：在特定激活量化模型中证明 STE 方向的有效性及收敛，不能直接推广到任意网络。
- **High-Dimensional Learning Dynamics of Quantized Models with Straight-Through Estimator**：推导特定高维模型的 STE 极限动力学与稳定性。
- **Beyond Discreteness - Sample Complexity Analysis of Straight-Through Estimator for 1-bit Quantization**：在二层、一位权重和激活量化的特定模型中，给出 STE 到量化全局最优的样本复杂度与收敛分析；有标签噪声时转为反复返回最优状态。
- **Understanding Quantization-Aware Training - Gradients at Quantized Weights Bias to the Low-Loss Basin**：直接研究梯度取在量化点的更新，证明量化点有限时间进入低损失盆地；这不是整个训练过程的渐近收敛定理。
- **Dynamic Model Pruning with Feedback**：定理 4.1、4.2 针对剪枝模型；正文指出可把剪枝器换成一般压缩器，包括量化。它提供可迁移的证明模板，但不能未经核对相对压缩误差条件就当作硬舍入 QAT 定理。

## 2. 改进或替代更新的分析（`ste-variants/`）

- **Gradient Descent with Compressed Iterates**：压缩后的迭代点继续更新；无偏随机压缩及强凸假设下得到收敛到误差邻域的界。它与保留全精度潜在权重的确定性舍入 STE 不同，是有用的理论对照。
- **PARQ - Piecewise-Affine Regularized Quantization**：证明凸损失下 AProx 的收敛；软量化渐近趋向硬量化，但不是原始 STE 的收敛证明。
- **Mirror Descent View for Neural Network Quantization**：用镜像下降解释并设计量化训练更新；其保证对应新算法。
- **Understanding Neural Network Binarization with Forward and Backward Proximal Quantizers**：研究前向和反向近端量化器及其优化性质。
- **CAGE - Curvature-Aware Gradient Estimation for Accurate Quantization-Aware Training**：改变梯度估计，并在简化条件下分析新方向。
- **PV-Tuning - Beyond Straight-Through Estimation for Extreme LLM Compression**：交替离散更新方法及其理想化目标值收敛分析。

## 3. 分析 STE 缺陷并提出改进（`ste-analysis-and-improvements/`）

- **BinaryRelax - A Relaxation Approach for Training Deep Neural Networks with Quantized Weights**：提出松弛法；第 4 节单独分析与 BinaryConnect 完全相同的硬投影阶段，但量化集合及几何条件很特殊。
- **Demystifying and Generalizing BinaryConnect**：把 BinaryConnect 纳入 ProxConnect 框架；可消失的收敛误差界要求凸正则项，不能直接用于离散量化集合的指示函数。
- **ProxQuant - Quantized Neural Networks via Proximal Operators**：§5.3 分析二值 BinaryConnect 的固定点条件；§5.2 给出软近端延迟更新的振荡反例，另证明近端替代算法的收敛。
- **QUASAR - Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction**：在非凸 L-smooth 目标下分析其选择的重建点上的 STE–SGD 梯度偏差与损失感知误差。把候选集限制为标准硬量化点可形式特化其界，但原文没有先单列标准 QAT 的收敛定理，且仍需检查 Hessian 控制假设。
- **Overcoming Oscillations in Quantization-Aware Training**：分析 STE 量化状态振荡并提出缓解方法；主要是机制分析，没有一般收敛定理。
- **Scheduling Weight Transitions for Quantization-Aware Training**：分析权重跨量化格点的转换并调整更新；主要是机制分析，没有一般收敛定理。

## 4. 与 QAT 相关的 PTQ 损失分析（`ptq-loss-analysis/`）

- **Loss Aware Post-Training Quantization**：用 Taylor 展开和实验研究量化误差增大时的层间耦合、非可分性与曲率，再提出联合优化。分析有助于理解 QAT 为何可能需要跨层调整，但不研究 STE 训练轨迹。
- **Up or Down - Adaptive Rounding for Post-Training Quantization**：用二阶损失近似说明最近邻舍入可因 Hessian 非对角项而次优，并把舍入写成离散优化问题。可作为 PTQ 与 QAT 的损失比较基线；不证明 STE 收敛。

其余 PTQ 论文（GPTQ、APHQ-ViT、PTQ4ViT、4-bit rapid-deployment）主要贡献是校准、重建、舍入或高效部署方法；局部 Hessian/MSE 代理服务于方法设计，因此未收入本目录。普通损失景观、一般梯度下降和梯度通信压缩论文也未收入；它们没有直接分析这里关心的量化训练更新。
