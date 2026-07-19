# TensorBoard 快速入门

> 用于可视化训练过程中的 loss、accuracy、模型图、梯度分布等。


## 1. 安装与启动

```bash
pip install tensorboard
```

在 notebook 中启动：

```python
%load_ext tensorboard
%tensorboard --logdir runs
```

或在终端启动：

```bash
tensorboard --logdir runs --port 6006
```

然后浏览器打开 `http://localhost:6006`。


## 2. 记录标量（Loss / Accuracy）

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('runs/experiment_1')

for epoch in range(epochs):
    train_loss = train(...)
    test_acc = test(...)

    writer.add_scalar('Loss/train', train_loss, epoch)
    writer.add_scalar('Loss/test', test_loss, epoch)
    writer.add_scalar('Accuracy/test', test_acc, epoch)

writer.close()
```

`Loss/train` 中的 `/` 会在 TensorBoard 中自动分组为 `Loss` 下的 `train` 和 `test` 子条目。


## 3. 记录多个实验对比

不同实验用不同的 `logdir`，TensorBoard 会自动叠加在同一张图上：

```python
# 实验 1
writer1 = SummaryWriter('runs/lr_0.01')
writer1.add_scalar('Loss/train', loss, epoch)

# 实验 2
writer2 = SummaryWriter('runs/lr_0.1')
writer2.add_scalar('Loss/train', loss, epoch)
```

启动 TensorBoard 时指定父目录：

```bash
tensorboard --logdir runs
```

所有 `runs/` 下的子目录会自动列在左侧，可勾选对比。


## 4. 记录超参数（HParams）

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('runs/hparam_tuning')

config = {
    'lr': 0.01,
    'batchsize': 64,
    'width': 256,
    'depth': 2,
}
metrics = {
    'hparam/accuracy': 0.9862,
    'hparam/loss': 0.065,
}

writer.add_hparams(config, metrics)
writer.close()
```

TensorBoard 的 HPARAMS 面板会生成超参数与性能指标的表格和散点图，便于分析哪些超参数影响最大。


## 5. 记录模型结构（Graph）

```python
dummy_input = torch.randn(1, 784)
writer.add_graph(model, dummy_input)
```

TensorBoard 的 GRAPHS 面板会显示模型的计算图，每个节点代表一层或一个算子。


## 6. 记录梯度与权值分布（Histogram）

```python
for name, param in model.named_parameters():
    writer.add_histogram(f'weights/{name}', param, epoch)
    if param.grad is not None:
        writer.add_histogram(f'grads/{name}', param.grad, epoch)
```

TensorBoard 的 HISTOGRAMS 面板会随时间展示权值和梯度的分布变化——梯度消失时分布会越来越窄，梯度爆炸时会发散。


## 7. 记录图像

```python
# 记录单张图像
writer.add_image('input', img_tensor, step)

# 记录多张图像（网格）
writer.add_images('batch', imgs_tensor, step)
```


## 8. 完整的训练模板

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('runs/mnist_mlp')

for epoch in range(20):
    train_loss, train_acc = train_one_epoch(...)
    test_loss, test_acc = evaluate(...)

    # 标量
    writer.add_scalar('Loss/train', train_loss, epoch)
    writer.add_scalar('Loss/test', test_loss, epoch)
    writer.add_scalar('Accuracy/train', train_acc, epoch)
    writer.add_scalar('Accuracy/test', test_acc, epoch)

    # 超参数（最后一轮记录即可）
    if epoch == 0:
        writer.add_hparams(
            {'lr': 0.01, 'batchsize': 64},
            {'final_accuracy': test_acc}
        )

    # 梯度分布（每几轮记录一次）
    if epoch % 5 == 0:
        for name, param in model.named_parameters():
            writer.add_histogram(f'grad/{name}', param.grad, epoch)

writer.close()
```


## 9. 常见问题

| 问题 | 解决方法 |
|------|---------|
| TensorBoard 页面空白 | 确认 `--logdir` 指向了正确的目录 |
| 曲线不更新 | 确保调用了 `writer.flush()` 或 `writer.close()` |
| 多个实验的曲线颜色相同 | 用不同的 `run` 名称区分 |
| `add_hparams` 报错 | 确保 `metric_dict` 的值是标量（Python float） |

![[Pasted image 20260713204958.png]]