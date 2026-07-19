# LaTeX 快速入门

> 用于撰写实验报告（数学公式、表格、图片、代码）

---

## 1. 推荐编辑器与下载

| 工具 | 平台 | 说明 |
|------|------|------|
| **Overleaf**（网页版） | 任何浏览器 | 在线编辑，免安装，自动编译，推荐初学者使用 |
| **TeX Live**（完整发行版） | Windows / Linux | 离线编译，完整安装约 5GB |
| **MiKTeX**（轻量发行版） | Windows | 按需下载宏包，比 TeX Live 小 |
| **VS Code + LaTeX Workshop** | 任何平台 | 若你已用 VS Code，装插件即可 |

### 下载方式

- **Overleaf**：打开浏览器访问 [overleaf.com](https://www.overleaf.com)，注册即可使用
- **TeX Live**：https://tug.org/texlive/，下载 install-tl-windows.exe
- **MiKTeX**：https://miktex.org/，下载 Windows 安装包

### 推荐方案

**初学者 → Overleaf**。注册即用，不需要装任何东西。实验报告这种短文档 Overleaf 完全够用。

---

## 2. 基本结构

```latex
\documentclass{article}              % 文档类型（article, report, book）
\usepackage[UTF8]{ctex}              % 中文支持
\usepackage{graphicx}                % 插入图片
\usepackage{booktabs}                % 三线表
\usepackage{amsmath}                 % 数学公式
\usepackage{setspace}                % 行距控制
\usepackage{enumitem}                % 列表间距控制

\title{Homework 1: MNIST Classification}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle                           % 显示标题
\tableofcontents                     % 显示目录（需编译两次）

\section{Introduction}               % 一级标题
这是实验报告的内容。

\subsection{Experimental Setup}      % 二级标题
这里写实验设置。

\end{document}
```

---

## 3. 布局控制

### 3.1 行距

```latex
\usepackage{setspace}

\singlespacing      % 单倍行距（默认）
\onehalfspacing     % 1.5 倍行距（推荐，宽松易读）
\doublespacing      % 双倍行距
```

### 3.2 列表间距

去除 `itemize` / `enumerate` 中 item 之间的额外空白，使之与正文行距一致：

```latex
\usepackage{enumitem}
\setlist{nosep}      % 全局设置：列表无额外间距
```

### 3.3 文档目录

```latex
\tableofcontents    % 在 \maketitle 之后使用，自动生成目录
```

需要编译两次才能正确显示。

---

## 4. 常用语法

### 4.1 标题层级

```latex
\section{一级标题}
\subsection{二级标题}
\subsubsection{三级标题}
```

### 4.2 文本格式

```latex
\textbf{粗体}    \textit{斜体}    \underline{下划线}
```

### 4.3 列表

```latex
\begin{itemize}
    \item 第一项
    \item 第二项
\end{itemize}

\begin{enumerate}
    \item 第一项
    \item 第二项
\end{enumerate}
```

### 4.4 数学公式

```latex
% 行内公式
$y = wx + b$

% 行间公式（不带编号）
$$
\hat{y} = \sigma(\mathbf{x}^\top \mathbf{w} + b)
$$

% 行间公式（带编号）
\begin{equation}
\text{MSE} = \frac{1}{n}\sum_{i=1}^{n} (\hat{y}_i - y_i)^2
\end{equation}

% 多行对齐
\begin{align}
\mathbf{Z} &= \mathbf{H}\mathbf{W} + \mathbf{1}\mathbf{b}^\top \\
\mathbf{H} &= \text{ReLU}(\mathbf{Z})
\end{align}

% 分段函数
f(x) = \begin{cases}
x^2, & x \ge 0 \\
0,   & x < 0
\end{cases}
```

---

## 5. 插入图片

```latex
% 单张图
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.6\textwidth]{lr_vs_acc.png}
    \caption{Learning Rate vs Test Accuracy}
    \label{fig:lr_acc}
\end{figure}
```

```latex
% 两张图并排
\begin{figure}[htbp]
    \centering
    \begin{minipage}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{loss_curve.png}
        \caption{Training Loss}
    \end{minipage}
    \hfill
    \begin{minipage}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{acc_curve.png}
        \caption{Test Accuracy}
    \end{minipage}
\end{figure}
```

参数说明：
- `[htbp]`：浮动位置（here, top, bottom, page）
- `width=0.6\textwidth`：宽度为页宽的 60%

---

## 6. 插入表格

```latex
\begin{table}[htbp]
    \centering
    \caption{不同超参数下的 test accuracy}
    \begin{tabular}{cccc}           % 4 列居中
        \toprule
        Learning Rate & Batch Size & Width & Accuracy \\
        \midrule
        0.01 & 64  & 256 & 0.9749 \\
        0.05 & 64  & 256 & 0.9832 \\
        0.10 & 64  & 256 & 0.9834 \\
        0.35 & 64  & 256 & \textbf{0.9862} \\
        \bottomrule
    \end{tabular}
    \label{tab:hyperparam}
\end{table}
```

`tabular` 列格式：`l`（左对齐）、`c`（居中）、`r`（右对齐）、`p{3cm}`（固定宽度）

---

## 7. 插入代码

```latex
\usepackage{listings}                % 在导言区添加

\begin{lstlisting}[language=Python, caption=MLP 定义]
class MLP(nn.Module):
    def __init__(self, input_dim, num_classes, hidden_dims):
        super().__init__()
        layers = []
        D = input_dim
        for C in hidden_dims:
            layers.append(nn.Linear(D, C))
            layers.append(nn.ReLU())
            D = C
        layers.append(nn.Linear(D, num_classes))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)
\end{lstlisting}
```

---

## 8. 实验报告模板

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[UTF8]{ctex}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{listings}
\usepackage[colorlinks=true,linkcolor=black]{hyperref}

% 代码样式
\lstset{
    basicstyle=\small\ttfamily,
    numbers=left,
    frame=single,
    breaklines=true,
}

\title{Homework 1: MNIST 图像分类实验报告}
\author{姓名 \\ 学号}
\date{2026 年 7 月}

\begin{document}
\maketitle

\section{实验目的}
本次实验的目标是...
(简要说明实验目标)

\section{实验设置}
\subsection{数据集}
MNIST 手写数字数据集，包含 60000 张训练图像和 10000 张测试图像，每张大小为 28×28。

\subsection{模型结构}
采用单隐藏层 MLP，结构为：\\
Linear(784, 300) → ReLU → Linear(300, 10)

\subsection{超参数}
\begin{itemize}
    \item 优化器：SGD
    \item 学习率：0.01
    \item Batch size：64
    \item Epochs：20
    \item 损失函数：CrossEntropyLoss
\end{itemize}

\section{实验结果}

\subsection{训练曲线}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.7\textwidth]{training_curves.png}
    \caption{训练过程中的 Loss 和 Accuracy 曲线}
    \label{fig:curves}
\end{figure}

\subsection{超参数对比}
表 \ref{tab:lr} 展示了不同学习率下的测试准确率。

\begin{table}[htbp]
    \centering
    \caption{学习率对比（width=256, depth=2, bs=64）}
    \begin{tabular}{cc}
        \toprule
        Learning Rate & Test Accuracy \\
        \midrule
        0.001 & 0.9256 \\
        0.01  & 0.9770 \\
        0.1   & 0.9834 \\
        0.35  & \textbf{0.9862} \\
        0.5   & 0.9726 \\
        \bottomrule
    \end{tabular}
    \label{tab:lr}
\end{table}

\subsection{结果分析}
从实验结果可以看出：
\begin{itemize}
    \item 学习率对模型性能影响最大，最优值为 0.35
    \item 宽度从 256 增加到 512 时性能提升不显著
    \item depth=2 略优于 depth=1，但差距在 0.3\% 以内
\end{itemize}

\section{结论}
本实验通过 MNIST 分类任务，验证了 MLP 在不同超参数下的表现。最优配置为 width=512, depth=2, lr=0.35, bs=64，最终测试准确率达到 98.71\%。

\end{document}
```

---

## 9. 编译方法

### Overleaf

直接点 "Recompile" 按钮，自动编译。

### 本地编译

```bash
# 用 pdflatex 编译两次（确保交叉引用正确）
pdflatex report.tex
pdflatex report.tex

# 或用 xelatex（推荐中文文档）
xelatex report.tex
```

---

## 模板

```tex
\documentclass[12pt,a4paper]{article}
\usepackage[UTF8]{ctex}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{listings}
\usepackage{float}
\usepackage[colorlinks=true,linkcolor=black]{hyperref}
\usepackage{setspace}
\usepackage{enumitem}
\setlist{nosep}
\onehalfspacing

% 代码样式
\lstset{
    basicstyle=\small\ttfamily,
    numbers=left,
    frame=single,
    breaklines=true,
}

\title{TITLE}
\author{YOUR NAME}
\date{DATE}


\begin{document}

\maketitle
\tableofcontents

\end{document}
```

---

## 9. 常见问题

| 问题 | 解决方法 |
|------|---------|
| 中文乱码 | 使用 `\usepackage[UTF8]{ctex}`，用 xelatex 编译 |
| 图片找不到 | 图片和 .tex 文件在同一目录，或用相对路径 |
| 编译报错 | 看第一个报错行，通常是漏了 `\end{...}` 或 `}` |
| 表格对不齐 | 检查 `tabular` 的列数是否匹配 |
| 公式编号不对 | 用 `\label{}` 和 `\ref{}`，编译两次 |
