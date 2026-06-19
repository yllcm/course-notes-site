# Taylor 定理
> [[数学分析|← 返回索引]]

## 一元函数的 Taylor 展开

**Df 2.1（泰勒多项式）**设 $f(x)$ 在 $x_0$ 处有 $n$ 阶导数，定义 **$n$ 次泰勒多项式** 为：

$$
T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k

$$

**Thm 2.1（带 Peano 余项的泰勒定理）**若 $f(x)$ 在 $x_0$ 处有 $n$ 阶导数，则存在 $x \to x_0$ 时的高阶无穷小，使得：

$$
f(x) = T_n(x) + o((x-x_0)^n)
$$

设余项为 $R_n(x) = f(x) - T_n(x)$，分母为 $Q_n(x) = (x-x_0)^n$。

由于 $f$ 在 $x_0$ 邻域内有 $n-1$ 阶导数，我们可以连续使用 $n-1$ 次洛必达法则：

$$
\lim_{x \to x_0} \frac{R_n(x)}{Q_n(x)} = \lim_{x \to x_0} \frac{R_n'(x)}{Q_n'(x)} = \dots = \lim_{x \to x_0} \frac{R_n^{(n-1)}(x)}{Q_n^{(n-1)}(x)}
$$

其中 $Q_n^{(n-1)}(x) = n \cdot (n-1) \dots 2 \cdot (x-x_0) = n!(x-x_0)$，$R_n^{(n-1)}(x) = f^{(n-1)}(x) - T_n^{(n-1)}(x)$。

此时原式为

$$
\begin{aligned} &\lim_{x \to x_0} \frac{f^{(n-1)}(x) - [f^{(n-1)}(x_0) + f^{(n)}(x_0)(x-x_0)]}{n!(x-x_0)} \\ &= \frac{1}{n!} \left[ \lim_{x \to x_0} \frac{f^{(n-1)}(x) - f^{(n-1)}(x_0)}{x-x_0} - f^{(n)}(x_0) \right]\\&=0 \end{aligned}
$$

**Thm 2.2（带 Lagrange 余项的泰勒定理）**设函数 $f(x)$ 在闭区间 $[a, b]$ 上有 $n$ 阶导数，在开区间 $(a, b)$ 内有 $n+1$ 阶导数。对于任意 $x, x_0 \in [a, b]$，至少存在一点 $\xi$（在 $x$ 与 $x_0$ 之间），使得：

$$
f(x) = f(x_0) + \frac{f'(x_0)}{1!}(x-x_0) + \dots + \frac{f^{(n)}(x_0)}{n!}(x-x_0)^n + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
$$

令

$$
F(t) = f(x) - \left[ f(t) + \frac{f'(t)}{1!}(x-t) + \dots + \frac{f^{(n)}(t)}{n!}(x-t)^n \right]
$$

$$
Q(t) = (x-t)^{n+1}
$$

运用 Cauchy 中值定理

$$
\frac{F(x_0)}{Q(x_0)} = \frac{F(x_0) - F(x)}{Q(x_0) - Q(x)} = \frac{F'(\xi)}{Q'(\xi)}= \frac{-\frac{f^{(n+1)}(\xi)}{n!}(x-\xi)^n}{-(n+1)(x-\xi)^n} = \frac{f^{(n+1)}(\xi)}{(n+1)!}
$$

也可以用习题里面的待定常数法求 $n$ 次导。

## 多元函数的 Taylor 展开

**Df 2.2（记号）**

- **多重指标 $\alpha$**: 定义为 $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_n)$，其中每个分量 $\alpha_i \ge 0$ 且 $\alpha_i \in \mathbb{N}$。
    
- **阶乘符号**: $\alpha! \triangleq \alpha_1! \alpha_2! \dots \alpha_n!$
    
- **绝对值 (阶数)**: $|\alpha| \triangleq \alpha_1 + \dots + \alpha_n$
- **幂符号**: $x^\alpha \triangleq x_1^{\alpha_1} x_2^{\alpha_2} \dots x_n^{\alpha_n}$
	- **偏导数算子**: 记 $D^\alpha f(x_0)$ 为在点 $x_0 = (x_1^0, \dots, x_n^0)$ 处计算的偏导数：
    
    $$
    \left. \frac{\partial^{|\alpha|} f(x)}{\partial x_1^{\alpha_1} \partial x_2^{\alpha_2} \dots \partial x_n^{\alpha_n}} \right|_{x=x_0} \triangleq \frac{\partial^{|\alpha|} f(x_0)}{\partial x^\alpha}
    $$
- 若函数 $f(x)$ 在点 $x_0$ 处拥有直到 $m$ 阶的连续偏导数，则其 $m$ 阶 Taylor 多项式 $T_m(x)$ 定义为：

$$
T_m(x) \triangleq T_m(x, f) \triangleq \sum_{k=0}^{m} \left( \sum_{|\alpha|=k} \frac{1}{\alpha!} \frac{\partial^k f(x_0)}{\partial x^\alpha} (x - x_0)^\alpha \right)
$$

**Thm 2.3（多变量函数的 Taylor 定理）**设 $D \subseteq \mathbb{R}^n$ 为凸区域，$f:D\to \mathbb{R}$ 且 $f \in C^{m+1}(D)$。对于任意 $a_0 \in D$ 及 $x \in D$，存在 $\theta \in (0, 1)$，使得：

$$
f(x) = \sum_{k=0}^{m} \sum_{|\alpha|=k} \frac{D^\alpha f(a_0)}{\alpha!} (x - a_0)^\alpha + \sum_{|\alpha|=m+1} \frac{D^\alpha f(a_0 + \theta(x - a_0))}{\alpha!} (x - a_0)^\alpha
$$

令 $\varphi(t) = f(a_0 + t(x - a_0))$，其中 $t \in [0, 1]$，则

$$
\varphi(1) = \varphi(0) + \frac{\varphi'(0)}{1!} + \dots + \frac{\varphi^{(m)}(0)}{m!} + \frac{\varphi^{(m+1)}(\theta)}{(m+1)!}
$$

设 $h=x-a_0$，我们有：

$$
\begin{align*}\left(\frac{\text{d}}{\text{d}t}\right)^k\varphi(t)&=\left(\frac{\text{d}}{\text{d}t}\right)^k f(a_0+th)\\&=\left(\frac{\text{d}}{\text{d}t}\right)^{k-1}\left(\frac{\text{d}}{\text{d}(a_0+th)}f(a_0+th)\right)h\\&=\left(\frac{\text{d}}{\text{d}t}\right)^{k-1}\left(\sum_{i=1}^n \frac{\partial f}{\partial x_i}(a_0+th)e_i^T\right)h\\&=\left(\frac{\text{d}}{\text{d}t}\right)^{k-1}\left(\sum_{i=1}^n h_i\frac{\partial f}{\partial x_i}(a_0+th)\right)\\&=\left(\sum_{i=1}^n h_i\frac{\partial }{\partial x_i}\right)^k f(a_0+th)\end{align*}
$$

而：

$$
\left( \sum_{i=1}^{n} h_i \frac{\partial}{\partial x_i} \right)^k = \sum_{|\alpha|=k} \frac{k!}{\alpha!} h^\alpha D^\alpha
$$

故 

$$
\varphi^{(k)}(t) = \sum_{|\alpha|=k} \frac{k!}{\alpha!} D^\alpha f(a_0 + th) (x - a_0)^\alpha
$$

代入即可。

分析余项

$$
f(x) = \sum_{k=0}^{m} \sum_{|\alpha|=k} \frac{D^\alpha f(a_0)}{\alpha!} (x - a_0)^\alpha + \underbrace{\sum_{|\alpha|=m} \left( \frac{D^\alpha f(a_0 + \theta(x - a_0))}{\alpha!} - \frac{D^\alpha f(a_0)}{\alpha!} \right) (x - a_0)^\alpha}_{R_m(x)}
$$

则

$$
\lim_{x \to a_0} \frac{R_m(x)}{\|x - a_0\|^m} = \lim_{x \to a_0} \sum_{|\alpha|=m} \left( \frac{D^\alpha f(a_0 + \theta(x - a_0))}{\alpha!} - \frac{D^\alpha f(a_0)}{\alpha!} \right) \cdot \frac{(x - a_0)^\alpha}{\|x - a_0\|^m}
$$

故

$$
f(x) = \sum_{k=0}^{m} \sum_{|\alpha|=k} \frac{D^\alpha f(a_0)}{\alpha!} (x - a_0)^\alpha +o(||x-x_0||^m)
$$

**Thm 2.4（凸函数的等价判定条件）**

- **条件 1 (一阶条件)**：若 $f$ 在 $\Omega$ 上可微，则 $f$ 为凸函数 $\iff \forall x, y \in \Omega, f(y) \ge f(x) + \nabla f(x) \cdot (y - x)$。
    
- **条件 2 (二阶条件)**：若 $f \in C^2(\Omega)$，则 $f$ 为凸函数 $\iff \nabla^2 f(x) = Hf(x)$（Hessian 矩阵）是**半正定**的。

条件 1 必要性只需要列出式子 $tf(y)+(1-t)f(x)\geq f(ty+(1-t)x)$，然后 Taylor 展开即可。充分性只要列两个式子然后把它们线性组合即可，不再赘述。

条件 2 可以考虑使用条件 1 证明。

（充分性）利用二阶 Taylor 展开，若 Hessian 矩阵半正定，则 $(y-x)^T Hf(\xi) (y-x) \ge 0$。由展开式可知 $f(y) \ge f(x) + \nabla f(x)(y-x)$，即满足一阶凸性条件，故函数为凸。

（必要性）假设存在 $h \neq 0$ 使得 $h^T Hf(x) h < 0$。根据凸性，有 $f(x+th) - [f(x) + \nabla f(x) \cdot th] \ge 0$。对其进行二阶 Taylor 展开并除以 $t^2$：

$$
\frac{f(x+th) - f(x) - \nabla f(x) \cdot th}{t^2} = \frac{1}{2}h^T Hf(x) h + \frac{o(\|th\|^2)}{t^2}
$$

令 $t\to 0^+$ 可得矛盾。

类比一维情况，一阶导数保证存在支撑线（面），二阶导数为正（半正定）
