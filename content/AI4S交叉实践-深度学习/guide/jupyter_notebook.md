# Jupyter Notebook 快捷入门教程

> 用于 AI4S 交叉实践课程实验（AutoDL 平台 + PyTorch）

---

## 1. 什么是 Jupyter Notebook

Jupyter Notebook 是一个**交互式 Python 编程环境**，以 `.ipynb` 文件保存。它将代码、运行结果、图表、笔记文字整合在一个文档中，特别适合做实验和数据分析。

---

## 2. 核心概念：Cell（单元格）

一个 Notebook 由若干 **Cell** 组成，每个 Cell 可以是两种类型之一：

| 类型 | 用途 | 快捷键切换 |
|------|------|-----------|
| **Code** | 写 Python 代码，按运行后会显示输出 | `Y` |
| **Markdown** | 写文字说明、数学公式、标题 | `M` |

- 选中一个 Cell 后，按 `Enter` 进入编辑模式，按 `Shift + Enter` 运行。
- 运行 Code Cell → 显示输出结果（打印、图表、tensor shape 等）。
- 运行 Markdown Cell → 渲染为格式化文本。

---

## 3. 常用快捷键

### 命令模式（按 `Esc` 进入，蓝色边框）

| 快捷键 | 作用 |
|--------|------|
| `A` | 在当前 Cell **上方**插入新 Cell |
| `B` | 在当前 Cell **下方**插入新 Cell |
| `DD` | 删除当前 Cell |
| `X` | 剪切当前 Cell |
| `C` + `V` | 复制 / 粘贴 Cell |
| `M` | 切换为 Markdown Cell |
| `Y` | 切换为 Code Cell |
| `Shift + ↑/↓` | 选中多个 Cell |
| `0` + `0` | 重启 Kernel（重要） |
| `I` + `I` | 中断运行中的代码 |

### 编辑模式（按 `Enter` 进入，绿色边框）

| 快捷键 | 作用 |
|--------|------|
| `Shift + Enter` | 运行当前 Cell 并选中下一个 |
| `Ctrl + Enter` | 运行当前 Cell |
| `Tab` | 自动补全 |
| `Shift + Tab` | 查看函数文档（光标放在函数名上） |

> **最重要的三个快捷键**：`Shift + Enter`（运行）、`B`（新建）、`DD`（删除）。

---

## 4. 在 AutoDL 上的基本操作（对应作业环境）

### 启动 Notebook

在 AutoDL 实例的 JupyterLab 中：
1. 左侧文件浏览器找到 `hw2_step1.ipynb` 或 `hw2_step2.ipynb`
2. 双击打开
3. 选择 Kernel（Python 3.8 / 3.10）

### 运行顺序

**从上到下依次运行**，因为后面的 Cell 依赖前面定义的变量（模型、数据等）。

```python
# Cell 1: 导入库
import torch
import torch.nn as nn
import torchvision
# ...

# Cell 2: 加载数据
train_loader = ...

# Cell 3: 定义模型
class Net(nn.Module): ...

# Cell 4: 训练循环
for epoch in range(epochs):
    ...
```

### 如果出错了

1. 查看错误信息（红色字体）
2. 修改代码
3. 重新运行出错的 Cell（以及它之后依赖它的 Cell）
4. 如果变量状态乱掉了 → **Kernel → Restart Kernel and Clear All Outputs**（`0` + `0`），然后从头开始运行

---

## 5. 在 Notebook 中画图

```python
%matplotlib inline          # 让图表直接显示在 Notebook 中
import matplotlib.pyplot as plt

plt.plot(train_losses, label='train')
plt.plot(test_accs, label='test')
plt.legend()
plt.show()                  # 显示图表
```

> `%matplotlib inline` 只需在 Notebook 中运行一次（通常在第一个 Cell 中）。

### 记录训练过程的常用写法

```python
train_losses = []
test_accs = []

for epoch in range(epochs):
    loss = train_one_epoch(model, loader)
    acc = evaluate(model, test_loader)

    train_losses.append(loss)
    test_accs.append(acc)

    print(f'Epoch {epoch}: loss={loss:.4f}, acc={acc:.2f}%')
```

最后用一个 Cell 统一画图，避免每步都画。

---

## 6. 常见问题

### Cell 一直 `[*]` 不动？

表示代码正在运行。等它跑完即可。如果卡死：
- 工具栏点 **Stop** 按钮（■）
- 或快捷键 `I` + `I`

### 跑了一半想改代码？

- 先 **中断** 当前运行（`I` + `I`）
- 修改代码
- **重启 Kernel**（`0` + `0`）并重新运行前面的 Cell，确保变量状态一致
- 改完后继续运行

> 部分修改后**不重启直接跑**可能导致变量不匹配的错误。

### 上一次运行的结果还在吗？

- **输出（print、图表）**：保存，刷新页面仍在
- **变量（模型参数、loss 值）**：存储在内存中，Kernel 重启后消失
- **代码本身**：保存在 `.ipynb` 文件中，下次打开还在

所以训练好的模型参数如果不想重训，需要保存：

```python
torch.save(model.state_dict(), 'model.pth')
```

---

## 7. Notebook 与 `.py` 文件的转换

| 方向 | 方法 |
|------|------|
| `.ipynb` → `.py` | `File → Export Notebook As → Python` |
| `.py` → `.ipynb` | 不太方便，建议直接在 Notebook 中写代码 |

> 交作业时通常提交 `.ipynb` 文件。

---

## 8. 作业中的典型 Notebook 结构

```
Cell 1:  导入库（torch, torchvision, matplotlib, etc.）
Cell 2:  加载 CIFAR-100 数据集（DataLoader）
Cell 3:  定义模型（MLP / CNN）
Cell 4:  定义训练函数
Cell 5:  定义评估函数
Cell 6:  训练循环（for epoch in range(epochs)）
Cell 7:  画图（loss 曲线 + accuracy 曲线）
Cell 8:  测试集评估，打印最终准确率
```

---

## 参考快捷键速查表

| 操作 | 快捷键 |
|------|--------|
| 运行当前 Cell | `Shift + Enter` |
| 上方插入 | `A` |
| 下方插入 | `B` |
| 删除 | `DD` |
| 中断运行 | `I I` |
| 重启 Kernel | `0 0` |
| 查看文档 | `Shift + Tab` |

> 熟练使用这几个就够了，不需要一次记住所有快捷键。
