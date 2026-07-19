# Pandas 快速入门

> 用于实验数据处理（读 CSV、筛选、分组、画图）


## 1. 读取 CSV

```python
import pandas as pd

df = pd.read_csv('experiment_data_all.csv')
print(df.head())          # 前 5 行
print(df.shape)           # (行数, 列数)
print(df.columns)         # 列名列表
```


## 2. 筛选数据

### 2.1 筛选行（按条件）

```python
# 单条件
df[df['width'] == 256]                            # width=256 的所有行

# 浮点数筛选（注意精度！）
df[df['lr'] == 0.1]                               # ❌ 可能因浮点精度漏掉数据
df[abs(df['lr'] - 0.1) < 1e-4]                   # ✅ 用绝对值容差比较
df[df['lr'].round(4) == 0.1]                      # ✅ 四舍五入后比较
```

> ⚠️ **浮点数不能用 `==` 直接比**。你的 CSV 里 lr 可能是 `0.350000000001` 而不是精确的 `0.35`。用 `abs(df['lr'] - 0.35) < 1e-4` 或 `.round(4) == 0.35` 更保险。

# 多条件：用 &（且）、|（或）
df[(df['width'] == 256) & (df['depth'] == 2)]     # width=256, depth=2
df[(df['lr'] == 0.1) | (df['lr'] == 0.01)]        # lr=0.1 或 0.01

# 多个值用 isin
df[df['lr'].isin([0.001, 0.01, 0.05])]            # lr 是这三个之一

# 比较
df[df['test_acc'] > 0.98]                         # acc>0.98
df[df['test_loss'] < 0.1]                         # loss<0.1
```

> ⚠️ 多条件时每个条件必须用**括号**括起来，`&` 不能用 `and`。

### 2.2 筛选列

```python
# 方式一：按列名取单列（返回 Series）
df['test_acc']                # 一列，形状 (N,)

# 方式二：取多列（返回 DataFrame）
df[['width', 'lr', 'test_acc']]   # 注意是双层方括号

# 方式三：按列名包含的关键字
df.filter(like='acc')               # 列名包含 'acc' → test_acc
df.filter(like='loss')              # 列名包含 'loss' → test_loss

# 方式四：按数据类型
df.select_dtypes(include=['float64', 'int64'])  # 只取数值列
```

### 筛选行 + 筛选列同时做

```python
# 先选行，再选列
df[df['width'] == 256][['lr', 'test_acc']]

# 或用 .loc（更推荐）
df.loc[df['width'] == 256, ['lr', 'test_acc']]
```

`.loc` 的语法：`.loc[行条件, 列条件]`

```python
# .loc 详解
df.loc[0:5]                              # 取前 5 行（按索引）
df.loc[:, ['lr', 'test_acc']]            # 所有行，只取 lr 和 test_acc
df.loc[df['width'] == 256, 'lr':'test_acc']  # 行筛选 + 列范围
```


## 3. 排序：sort_values

```python
df.sort_values('test_acc')                        # 按 test_acc 升序（小→大）
df.sort_values('test_acc', ascending=False)       # 降序（大→小）
df.sort_values(['width', 'lr'])                   # 先按 width，再按 lr 排序
df.sort_values(['width', 'lr'], ascending=[True, False])  # width 升序，lr 降序
```

画图前通常要排序，否则折线会乱：

```python
# ❌ 乱序：lr=[0.1, 0.001, 0.01]，折线来回交叉
subset = df[df['width'] == 256]
plt.plot(subset['lr'], subset['test_acc'])  # 图是乱的

# ✅ 先排序再画
subset = df[df['width'] == 256].sort_values('lr')
plt.plot(subset['lr'], subset['test_acc'])  # 平滑曲线
```

`sort_values` 默认返回**新 DataFrame**，不修改原数据。如果想原地修改：

```python
df.sort_values('test_acc', inplace=True)   # 直接修改 df 本身
```

## 4. 找最优配置

```python
# 找 test_acc 最高的行
best = df.loc[df['test_acc'].idxmax()]
print(best)

# 按 width 分组，每组找最优
best_per_width = df.loc[df.groupby('width')['test_acc'].idxmax()]
print(best_per_width[['width', 'lr', 'test_acc']])
```


## 4. 分组统计

```python
# 按 lr 分组，计算 acc 的均值
df.groupby('lr')['test_acc'].mean()

# 按 (width, depth) 分组，找每组的 acc 最大值
df.groupby(['width', 'depth'])['test_acc'].max()

# 分组后多列统计
df.groupby('lr').agg({'test_acc': ['mean', 'max', 'std'],
                      'test_loss': 'mean'})
```


## 5. 画图（pandas + matplotlib）

```python
import matplotlib.pyplot as plt

# 固定 width=256, depth=2，画 lr vs acc
subset = df[(df['width'] == 256) & (df['depth'] == 2)]
subset = subset.sort_values('lr')
plt.plot(subset['lr'], subset['test_acc'], 'o-')
plt.xscale('log')
plt.xlabel('Learning Rate')
plt.ylabel('Test Accuracy')
plt.grid(True, alpha=0.3)
plt.show()
```

```python
# 多条线对比：不同 width 的 lr vs acc
for w in [64, 128, 256, 512]:
    subset = df[(df['width'] == w) & (df['depth'] == 2) & (df['batchsize'] == 64)]
    subset = subset.sort_values('lr')
    plt.plot(subset['lr'], subset['test_acc'], 'o-', label=f'w={w}')
plt.xscale('log')
plt.xlabel('Learning Rate')
plt.ylabel('Test Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```


## 6. 数据透视表

```python
# 行=lr，列=width，值=test_acc
pivot = df.pivot_table(index='lr', columns='width', values='test_acc', aggfunc='mean')
print(pivot)

# 画热力图
import seaborn as sns
sns.heatmap(pivot, annot=True, fmt='.3f')
plt.show()
```


## 7. 导出

```python
df.to_csv('output.csv', index=False)          # 导出为 CSV
df.to_excel('output.xlsx', index=False)       # 导出为 Excel
```


## 完整示例

```python
import pandas as pd
import matplotlib.pyplot as plt

# 读数据
df = pd.read_csv('experiment_data_all.csv')

# 筛选：bs=64, depth=2
data = df[(df['batchsize'] == 64) & (df['depth'] == 2)]

# 画图：不同 width 的 lr vs acc
for w in sorted(data['width'].unique()):
    sub = data[data['width'] == w].sort_values('lr')
    plt.plot(sub['lr'], sub['test_acc'], 'o-', label=f'width={w}')

plt.xscale('log')
plt.xlabel('Learning Rate')
plt.ylabel('Test Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('lr_vs_acc.png', dpi=150)
plt.show()

# 打印最优配置
best = df.loc[df['test_acc'].idxmax()]
print('全局最优:')
print(f"  width={int(best['width'])}, depth={int(best['depth'])}, "
      f"bs={int(best['batchsize'])}, lr={best['lr']:.4f}, "
      f"acc={best['test_acc']:.4f}")
```
