## 前期准备

配环境

conda create -n dl_hw1 python=3.11 -y

conda activate dl_hw1

pip install torch torchvision matplotlib

conda install -n dl_hw1 ipykernel --update-deps --force-reinstall


## 函数编写

已经放在笔记中

## 训练模型

初始 learning_rate=0.01，步长过大导致参数全部变成了 nan，后面把步长设为 1e-6 之后模型正常。acc 为 0.95

learning_rate=1e-5 之后 test_acc 达到了 0.973

Epoch 9 | Total Time: 19s, Test Loss: 0.024, Test Acc: 0.975（3e-3，MSELoss）

step2 learning_rate=0.01 best_acc 达到 0.965（CrossEntropyLoss）

Epoch 19 | Total Time: 10s, Test Loss: 0.117, Test Acc: 0.967

同样配置换成 MSELoss test_acc 0.971, test_loss 0.104

Step 3：Epoch 19 | Total Time: 10s, Test Loss: 0.121, Test Acc: 0.966

Step 4：Epoch 19 | Total Time: 10s, Test Loss: 0.118, Test Acc: 0.966

Step 4 实验时花费了大量时间在对

```
    'width': [64, 128, 256],

    'depth': [1, 2],

    'batchsize': [64, 128, 256],

    'lr': [0.001, 0.01, 0.1],

    'epoch': 20,
```

的不同配置进行枚举实验，事实上上面的数据设置是不合理的，应该先手动进行几组预实验，再进行参数设置

设置 batchsize=64, width=512, depth=2, lr=[0.05,0.1,0.2,0.35,0.5] 进行实验

实验之后发现 acc 在 0.2 到 0.5 之间最优，继续实验发现在 0.2 到 0.5 之间震荡的不太规则，tmd，白做了。

然后发现 loss 在 0.2 到 0.5 是递减的，tmd

做了一下 width=64, depth=2，好像挺对劲的，因为 lr 小的时候 loss 才低

0.07313079815357923 0.9764


512 0.1 512 2 20 0.0634115420281887 0.9799

妈的，弄了一坨数据，根本没分析出来结果。下次先分析简单问题然后框框画图算了。


- 我跑了 width = [128, 256, 512], depth = [1, 2], lr = [0.001, 0.01, 0.1], batchsize=[128, 256, 512] 的 acc 和 loss，没有看出任何趋势
- 我接着对 batchsize=64，width=512, depth=2, lr=lr=[0.05,0.1,0.2,0.35,0.5]，的不同 lr 做了实验，发现最优 acc 在 [0.1, 0.35] 之间, loss 在区间是递减的。
- 我做了一下 width=64, depth=2，好像挺对劲的，因为 lr 小的时候 loss 才低。
- 我补了 128, 256 的数据，发现宽度越大的模型 lr 好像越高
- 我补了 depth=1 的数据，没有认真分析。
- 我尝试探索 batchsize 的规律，先做了 width=512, depth=2, lr=0.1，batchsize=[64, 128, 256, 512] 的数据，发现最优在 [128, 512] 之间
- 我接着跑了[128, 192, 256, 384, 512] 的数据梯度，最优（loss）是 batchsize=256
- 我跑了 128, 256 的数据，发现它们最优的 batchsize 是 192（loss）
- acc 均随 batchsize 递减，batchsize=32 的时候它们的 acc 是最优的。

在 Step 1\sim 3 中，我记录数据的习惯不好，记录了 accuracy 之后才发现作业需要记录 Loss，导致重复跑了好几次实验

### Step 1

Epoch 9 | Total Time: 25s, Test Loss: 0.089, Test Acc: 0.973 BCE Loss