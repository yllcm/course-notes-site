---
title: AI4S 交叉实践 — 深度学习
---

# AI4S 交叉实践 — 深度学习

> AI for Science 交叉实践课程笔记。笔记按**组件 → 架构 → 前沿 → 理论 → 工程**的递进逻辑组织，实用工具作为第七模块并列。

---

## 笔记目录

### 一、数理基础与经典模型
[[01-数理基础与经典模型|→ 笔记]]
> 从线性模型到神经网络：线性回归 → 逻辑回归 → Softmax → 通用近似定理 → KL 散度 → 三个差距

### 二、深度学习核心组件
[[02-深度学习核心组件|→ 笔记]]
> 决定深层网络能否收敛的微观技术：激活函数 → Kaiming 初始化 → 残差连接 → BatchNorm/LayerNorm/RMSNorm → 正则化

### 三、经典网络架构
[[03-经典网络架构|→ 笔记]]
> CNN（稀疏连接/参数共享） → Standard Transformer（Attention 完整推导）

### 四、大语言模型与前沿演进
[[04-大语言模型与前沿演进|→ 笔记]]
> MoE（路由/负载均衡/专家并行） → 因果注意力（掩码/KV Cache/MQA/GQA） → 对齐训练 → In-Context Learning

### 五、优化理论与泛化界
[[05-优化理论与泛化界/README|→ 两个章节]]
> 连续优化（SGD 收敛 / 缩放规则 / Adam） + 统计学习理论（VC 维 / Rademacher 复杂度）

### 六、工程实践与底层实现
[[06-工程实践与底层实现|→ 笔记]]
> 矩阵微分法 → 前反向传播 → PyTorch 基础 → 自动求导 → 训练循环 → 模型评估

---

## 实用工具（七）

| 工具 | 说明 |
|------|------|
| [[guide/jupyter_notebook|Jupyter Notebook]] | 基本操作、快捷键、AutoDL 配置 |
| [[guide/python_slicing|Python Slicing]] | 切片语法、花式索引、整数数组索引 |
| [[guide/matplotlib_quickstart|Matplotlib]] | 折线图、子图、对数坐标、图例、样式控制 |
| [[guide/pandas_quickstart|Pandas]] | 数据读取、筛选、排序、分组、透视表、画图 |
| [[guide/latex_quickstart|LaTeX]] | 文档结构、数学公式、表格、实验报告模板 |
| [[guide/tensorboard_quickstart|TensorBoard]] | 标量/超参数/模型图/梯度分布的可视化 |

---

## 作业实践

- **HW1** — MNIST 手写数字分类（逻辑回归 → 手动 MLP → autograd → nn.Module → 超参数搜索）
- **HW2** — CIFAR-100 图像分类（MLP → CNN → 优化技巧 → BN 目标 68%+）

## 其他资料

- [[深度学习实验设计与分析流程|实验方法论]] — 从实验中总结的系统化流程
- [[hw1手记|HW1 实验手记]] — 操作记录与踩坑经验
