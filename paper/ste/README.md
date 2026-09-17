# STE / QAT 论文分类

整理日期：2026-09-17。

本目录围绕固定量化器下的 STE/QAT 更新、量化模型损失、损失景观几何，以及代表性 PTQ 局部代理方法，分为五类。PDF 文件名统一使用论文题目，不再保留下载编号或 arXiv 编号。

## 1. Optimization Interpretations

- ProxQuant: Quantized Neural Networks via Proximal Operators
- Demystifying and Generalizing BinaryConnect
- Mirror Descent View for Neural Network Quantization
- PARQ: Piecewise-Affine Regularized Quantization

## 2. STE and QAT Theory

- Beyond Discreteness: Sample Complexity Analysis of Straight-Through Estimator for 1-bit Quantization
- CAGE: Curvature-Aware Gradient Estimation for Accurate Quantization-Aware Training
- Dynamic Model Pruning with Feedback
- Gradient Descent with Compressed Iterates
- High-Dimensional Learning Dynamics of Quantized Models with Straight-Through Estimator
- PV-Tuning: Beyond Straight-Through Estimation for Extreme LLM Compression
- QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction
- Quantized Adam with Error Feedback
- Scheduling Weight Transitions for Quantization-Aware Training
- Training Quantized Nets: A Deeper Understanding
- Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin
- Understanding Straight-Through Estimator in Training Activation Quantized Neural Nets

这一类中的部分论文修改了优化器、梯度估计或离散更新规则，因此不能把其收敛结论直接当作原始 fixed-rounding identity-STE 的保证。

## 3. Loss Landscape and Geometry

- Beyond the Quadratic Approximation: The Multiscale Structure of Neural Network Loss Landscapes
- Gradient Extremals, Talwegs, Valleys, and Directional Alignment for Generic Gradient Descent
- Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape Perspective
- Unveiling the Basin-Like Loss Landscape in Large Language Models

## 4. Geometric Convergence

- Gradient Descent with Adaptive Stepsize Converges (Nearly) Linearly under Fourth-Order Growth

## 5. PTQ Algorithms

- APHQ-ViT: Post-Training Quantization with Average Perturbation Hessian Based Reconstruction for Vision Transformers
- GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers
- Loss Aware Post-Training Quantization
- PTQ4ViT: Post-Training Quantization for Vision Transformers with Twin Uniform Quantization
- Post Training 4-bit Quantization of Convolutional Networks for Rapid-Deployment
- Up or Down? Adaptive Rounding for Post-Training Quantization

## 已移除

以下四篇不属于当前五条主线，已从论文目录删除：

- Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation
- Straight-Through Meets Sparse Recovery: The Support Exploration Algorithm
- A Network of Spiking Neurons for Computing Sparse Representations in an Energy Efficient Way
- Unified Scaling Laws for Compressed Representations
