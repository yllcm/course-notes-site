# Matplotlib 快速入门

> 用于实验画图（loss 曲线、accuracy 曲线、对比图）

---

## 1. 基本画图

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0.9, 0.92, 0.94, 0.955, 0.96, 0.965]

plt.plot(x, y)           # 折线图
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Test Accuracy')
plt.show()               # 显示
```

---

## 2. 画 loss 曲线

```python
# train_loss 和 test_loss 是列表，每个 epoch 一个值
plt.plot(train_loss, label='train', color='blue')
plt.plot(test_loss, label='test', color='red')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()              # 显示图例
plt.grid(True, alpha=0.3) # 显示网格线（透明度 30%，更淡雅）
plt.show()
```

---

## 3. 同时画 loss 和 acc（子图）

```python
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)                       # 1 行 2 列，第 1 个
plt.plot(train_loss, label='train')
plt.plot(test_loss, label='test')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)                       # 1 行 2 列，第 2 个
plt.plot(train_acc, label='train')
plt.plot(test_acc, label='test')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()                          # 自动调整间距
plt.savefig('training_curves.png', dpi=150) # 保存
plt.show()
```

---

## 4. 超参对比图

```python
# 不同 lr 的 acc 曲线画在一起
plt.figure(figsize=(8, 5))

# 每组数据是 (lr 列表, acc 列表)
for lr in [0.001, 0.01, 0.1]:
    plt.plot(lr_values[lr], acc_values[lr], 'o-', label=f'lr={lr}')

plt.xlabel('Learning Rate')
plt.ylabel('Test Accuracy')
plt.legend()
plt.xscale('log')          # lr 通常用对数坐标
plt.show()
```

---

## 5. 常用格式控制

```python
plt.plot(x, y,
    color='red',            # 颜色
    marker='o',             # 标记点样式
    linestyle='--',         # 线型（- 实线, -- 虚线, -. 点划线, : 点线）
    linewidth=2,            # 线宽
    markersize=6,           # 标记大小
    label='train')          # 图例标签
```

常用颜色：`'blue'` / `'red'` / `'green'` / `'orange'` / `'purple'` / `'#ff6600'`

---

## 6. 保存图片

```python
plt.savefig('filename.png', dpi=150, bbox_inches='tight')
# dpi=150：分辨率，越大越清晰
# bbox_inches='tight'：裁掉空白边
# 支持 .png, .pdf, .jpg
```

> **必须先 savefig 再 show**，否则 show 之后画布会清空，保存的是空白图。

---

## 7. 画多条线时自动配色

```python
colors = ['blue', 'red', 'green', 'orange', 'purple']
markers = ['o', 's', '^', 'D', 'v']

for i, bs in enumerate([64, 128, 256, 512, 1024]):
    plt.plot(x_data[bs], acc_data[bs], 
             color=colors[i], marker=markers[i], label=f'bs={bs}')
plt.legend()
plt.show()
```

---

## 完整示例

```python
import matplotlib.pyplot as plt

# 假设已有数据（实验结果的列表）
epochs = range(1, 21)
train_loss = [2.3, 1.8, 1.2, 0.8, 0.6, 0.5, ...]   # 20 个值
test_acc = [0.89, 0.91, 0.93, 0.94, ...]            # 20 个值

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, 'b-', label='Train Loss')
plt.plot(epochs, test_loss, 'r-', label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(epochs, train_acc, 'b-', label='Train Acc')
plt.plot(epochs, test_acc, 'r-', label='Test Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('experiment_results.png', dpi=150)
plt.show()
```

---

## 8. 网格线 plt.grid

```python
plt.grid(True)               # 显示网格
plt.grid(True, alpha=0.3)    # 透明度 30%（更淡雅）
plt.grid(True, axis='y')     # 只显示水平线
plt.grid(False)              # 隐藏网格
```

网格线能帮助你更准确地读出曲线在纵轴/横轴上的位置，适合放在实验报告中展示。

---

## 9. 自动调整布局 tight_layout

`plt.tight_layout()` 自动调整子图之间的间距，防止坐标轴标签重叠。

```python
plt.subplot(1, 2, 1)
plt.xlabel('Learning Rate')
plt.ylabel('Loss')

plt.subplot(1, 2, 2)
plt.xlabel('Learning Rate')
plt.ylabel('Accuracy')

plt.tight_layout()                # 自动拉开间距
plt.show()
```

没有 `tight_layout` 时，左边子图的 y 轴标签和右边子图的 x 轴标签可能会挤在一起。加上后自动留出空间。通常在 `savefig` 和 `show` 之前调一次。

---

## 10. 图例 legend

### 用法一：plot 时指定 label

```python
plt.plot(x, y1, label='train')      # plot 时指定标签
plt.plot(x, y2, label='test')
plt.legend()                         # 自动显示图例
```

`plt.legend()` 会收集所有带 `label` 参数的曲线，自动生成图例。

### 用法二：在子图里分别加图例

```python
plt.subplot(1, 2, 1)
plt.plot(x, y1, label='train')
plt.legend()                        # ← 第一个子图的图例

plt.subplot(1, 2, 2)
plt.plot(x, y2, label='test')
plt.legend()                        # ← 第二个子图的图例
```

> ⚠️ 如果只在子图外面调一次 `plt.legend()`，图例只会出现在**最后一个子图**上。每个子图都要单独调一次。

### 用法三：手动指定位置

```python
plt.legend(loc='best')              # 自动选最佳位置（默认）
plt.legend(loc='upper right')       # 右上角
plt.legend(loc='lower left')        # 左下角
plt.legend(loc='center')            # 正中央
```

常用 `loc` 值：`'best'`, `'upper right'`, `'upper left'`, `'lower right'`, `'lower left'`, `'center'`

```python
plt.grid(True)               # 显示网格
plt.grid(True, alpha=0.3)    # 透明度 30%（更淡雅）
plt.grid(True, axis='y')     # 只显示水平线
plt.grid(False)              # 隐藏网格
```

网格线能帮助你更准确地读出曲线在纵轴/横轴上的位置，适合放在实验报告中展示。
```
