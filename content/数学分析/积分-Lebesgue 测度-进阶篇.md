# Lebesgue 测度（进阶篇）
> [[数学分析/README|← 返回索引]]

**Df 8.3.8（Borel $\sigma$-代数）** $\mathbb{R}^n$ 中所有**开集**生成的 $\sigma$-代数称为 **Borel $\sigma$-代数**（或 Borel 代数），记为：

$$
\mathcal{B} \equiv \mathcal{B}(\mathbb{R}^n)
$$

其内部的元素称为 **Borel 集**。

**Rmk 8.3.2** Borel 集族与 Lebesgue 可测集族 $\mathcal{L}(\mathbb{R}^n)$ 之间满足严格包含关系：

$$
\mathcal{B}(\mathbb{R}^n) \subsetneqq \mathcal{L}(\mathbb{R}^n)
$$

即所有 Borel 集都是 Lebesgue 可测的，但存在 Lebesgue 可测集不是 Borel 集。

**Df 8.3.9（二进方块 Dyadic Cube）** 对于固定的尺度 $k \in \mathbb{Z}$，定义二进方块族 $\mathcal{G}_{Dk}$ 为：

$$
\mathcal{G}_{Dk} = \left\{ 2^{-k} \left( (j_1, \dots, j_n)^T + [0, 1)^n \right) : j_1, \dots, j_n \in \mathbb{Z} \right\}
$$

通过改变 $k$ 的值，可以得到不同大小（边长为 $2^{-k}$）的网格结构。

全体二进方块的集合记为 $\displaystyle \mathcal{F}_{DQ} = \bigcup_{k\in\mathbb{Z}} \mathcal{G}_{Dk}$。

**Df 8.3.10（$G_\delta$ 集与 $F_\sigma$ 集）**
- $G_\delta$ 集：可数个开集的交集。
- $F_\sigma$ 集：可数个闭集的并集。

两类集合均为 Borel 集（因 $\sigma$-代数对可数交与可数并封闭）。

**Lemma 8.3.1（二进方块的三歧性）** 对于任意两个二进方块 $A, B \in \mathcal{G}_{Dk}$（可跨尺度），它们的关系必定满足以下三者之一：

$$
A \cap B = \emptyset \quad \text{或} \quad A \subset B \quad \text{或} \quad B \subset A
$$

即两个二进方块要么完全不相交，要么其中一个完全包含另一个，绝不可能出现部分重叠。

**Df 8.3.11（极大二进方块）** 令 $V \subseteq \mathbb{R}^n$ 为非空开集。对 $\forall x \in V$，定义包含点 $x$ 且包含在 $V$ 内部的**极大二进方块** $A(x)$ 为：

$$
A(x) \triangleq \{ A \in \mathcal{F}_{DQ} : x \in A \text{ 且 } A \text{ 在 } \mathcal{F}_{DQ} \text{ 中关于包含关系是极大的} \}
$$

**Thm 8.3.11（开集的二进分解）** $\mathbb{R}^n$ 中的任一开集可表为**至多可数个两两不交**的二进方块的并。

*证明*：设 $G \subseteq \mathbb{R}^n$ 为一开集。考虑包含在 $G$ 内部的所有二进方块的子族 $\{ Q \in \mathcal{F}_{DQ} : Q \subset G \}$。

由于开集的拓扑性质（内部任意点都有邻域包含在开集内），这些方块足以填满整个开集，即 $\bigcup_{A \in \mathcal{F}_{DQ}} A = G$。但此时的并集中存在大量重叠，尚未实现"两两不交"。

对 $\forall x \in G$，考虑包含 $x$ 且含于 $G$ 的极大二进方块 $A(x)$（见 Df 8.3.11）。由二进方块的三歧性（Lemma 8.3.1），$A(x)$ **唯一存在**，且对任意 $x, y \in G$，要么 $A(x) = A(y)$，要么 $A(x) \cap A(y) = \emptyset$（若相交则必有一个包含另一个，与极大性矛盾）。于是 $\{ A(x) : x \in G \}$ 即为 $G$ 的一个两两不交的二进方块覆盖，且至多可数（每个方块包含一个有理点）。$\square$

**Thm 8.3.12（外测度的开集与 $G_\delta$ 逼近）** 设 $E \subseteq \mathbb{R}^n$ 为任意子集，则它的 Lebesgue 外测度 $m^*(E)$ 满足：

$$
m^*(E) = \inf_{\substack{E \subseteq A \\ A \in G_\delta}} m(A) = \inf_{\substack{E \subseteq V \\ V \text{ 为开集}}} m(V)
$$

*证明*：先证 $m^*(E)=\inf_{E\subseteq V,\,V\text{开}}m(V)$。

对 $\forall\varepsilon>0$，由外测度定义存在方体列 $\{R_k\}$ 覆盖 $E$ 且 $\sum|R_k|<m^*(E)+\varepsilon$。将每个 $R_k$ 的边向外略扩为开方体 $\mathring{R}_k$ 使 $|\mathring{R}_k|\le|R_k|+\varepsilon/2^k$。令 $V=\bigcup\mathring{R}_k$，则 $V$ 为开集，$E\subseteq V$，且

$$
m(V)\le\sum|\mathring{R}_k|\le\sum|R_k|+\varepsilon<m^*(E)+2\varepsilon
$$

故 $\inf_{E\subseteq V}m(V)\le m(V)<m^*(E)+2\varepsilon$，由 $\varepsilon$ 任意性得 $m^*(E)\ge\inf_{E\subseteq V}m(V)$。

反之，对任意开集 $V\supseteq E$，由单调性 $m^*(E)\le m(V)$，取下确界得 $m^*(E)\le\inf_{E\subseteq V}m(V)$。因此 $m^*(E)=\inf_{E\subseteq V}m(V)$。

再证 $m^*(E)=\inf_{E\subseteq A,\,A\in G_\delta}m(A)$。一方面，开集是 $G_\delta$ 集，故

$$
\inf_{E\subseteq A}m(A)\le\inf_{E\subseteq V}m(V)=m^*(E)
$$

另一方面，对任意 $G_\delta$ 集 $A\supseteq E$，$A$ 可测且 $m(A)\ge m^*(E)$，取下确界得 $m^*(E)\le\inf_{E\subseteq A}m(A)$。两边夹即得等式。$\square$


**Rmk 8.3.3（外正则性的含义）** 这一定理揭示了 Lebesgue 外测度的一个重要特征：外测度本质上是一个**"由外向内"**的逼近工具。虽然外测度的原始定义依赖于生硬的方体覆盖，但它和 $\mathbb{R}^n$ 的拓扑结构有着深刻的联系——开集和 $G_\delta$ 集也能达到相同的逼近效果。这一性质称为**外正则性**，在后文证明可测函数的可积性、Fubini 定理等结论时将频繁出现。

**Rmk 8.3.4（为何引入 $G_\delta$ 集）** 开集逼近本身已足以刻画外测度，$G_\delta$ 集看似多余。但 $G_\delta$ 集在后续理论中扮演了独特角色：$G_\delta$ 集是 Borel 集，结构更精细（可测集可表示为 $G_\delta$ 集与零测集的差，这给出了可测性的更精细刻画——见 Lusin 定理等相关结论）。

**Rmk 8.3.5（内测度的闭集与 $F_\sigma$ 逼近）** 与 Thm 8.3.12 对偶，内测度 $m_*(E)$ 可从内部用闭集或 $F_\sigma$ 集逼近：

$$
m_*(E) = \sup_{\substack{A \subseteq E \\ A \in F_\sigma}} m(A) = \sup_{\substack{F \subseteq E \\ F \text{ 闭}}} m(F)
$$

**Thm 8.3.13（Lebesgue 可测性的拓扑等价条件）** 设 $E \subseteq \mathbb{R}^n$，则以下条件等价：

1. $E$ 是 Lebesgue 可测的。
2. (开集外部逼近) $\forall \varepsilon > 0,\ \exists\ \text{开集 } G \supseteq E \text{ 使得 } m^*(G \setminus E) < \varepsilon$。
3. (闭集内部逼近) $\forall \varepsilon > 0,\ \exists\ \text{闭集 } F \subseteq E \text{ 使得 } m^*(E \setminus F) < \varepsilon$。
4. ($G_\delta$ 外包) $\exists\ G_\delta \text{ 集 } G_0 \supseteq E \text{ 使得 } m^*(G_0 \setminus E) = 0$。
5. ($F_\sigma$ 内填) $\exists\ F_\sigma \text{ 集 } F_0 \subseteq E \text{ 使得 } m^*(E \setminus F_0) = 0$。

*证明*：(1) $\Rightarrow$ (2) 先考虑 $m(E) < \infty$ 的情形。由 Thm 8.3.12，存在开集 $G \supseteq E$ 使得 $m(G) < m(E) + \varepsilon$，从而 $m(G\setminus E) = m(G) - m(E) < \varepsilon$。

若 $m(E) = \infty$，将 $\mathbb{R}^n$ 分解为可数个两两不交的有界方体 $I_i^*$，令 $E_i = E \cap I_i^*$，则 $m(E_i) < \infty$。对每个 $E_i$ 取开集 $G_i \supseteq E_i$ 满足 $m(G_i) < m(E_i) + \varepsilon/2^i$。令 $G = \bigcup_{i=1}^\infty G_i$，则 $G$ 为开集，$E \subseteq G$，且

$$
m(G \setminus E) \le \sum_{i=1}^\infty m(G_i \setminus E_i) \le \sum_{i=1}^\infty \frac{\varepsilon}{2^i} = \varepsilon
$$

>[!info]
>为什么要分 $m(E)=\infty$ 的情况讨论？因为 $\infty$ 是不能做减法的，对有限集的证明失效了。

故 (1) $\Rightarrow$ (2) 得证。

(2) $\Rightarrow$ (1) 对 $\forall\varepsilon>0$，取开集 $G\supseteq E$ 使 $m^*(G\setminus E)<\varepsilon$。由 $G$ 可测及 Carathéodory 条件（Thm 8.3.2），对任意 $F\subseteq\mathbb{R}^n$ 有

$$
m^*(F)=m^*(F\cap G)+m^*(F\setminus G)
$$

由 $E\subseteq G$ 知 $F\cap E\subseteq F\cap G$，故 $m^*(F\cap G)\ge m^*(F\cap E)$。又 $F\setminus G\subseteq F\setminus E$，由次可加性得

$$
m^*(F\setminus E)\le m^*(F\setminus G)+m^*(F\cap(G\setminus E))< m^*(F\setminus G)+\varepsilon
$$

即 $m^*(F\setminus G)>m^*(F\setminus E)-\varepsilon$。代入 Carathéodory 分解：

$$
m^*(F) > m^*(F\cap E) + \big(m^*(F\setminus E)-\varepsilon\big)
$$

由 $\varepsilon$ 任意性得 $m^*(F)\ge m^*(F\cap E)+m^*(F\setminus E)$；反向不等式由次可加性自然成立。故 $E$ 可测。

>[!info]
>关键是对 $F\setminus G$ 的处理，它实际上是一个大集合减去一个零测集，所以要把 $m^*(F\setminus E)$ 用次可加性展开。

(1) $\Leftrightarrow$ (4) 若 $E$ 可测，由 (1)$\Rightarrow$(2) 知对每个 $k\in\mathbb{N}$ 存在开集 $G_k\supseteq E$ 使 $m^*(G_k\setminus E)<1/k$。令 $G_0=\bigcap_{k=1}^\infty G_k$，则 $G_0$ 为 $G_\delta$ 集，$E\subseteq G_0$，且 $G_0\setminus E\subseteq G_k\setminus E$ 对每个 $k$ 成立，故 $m^*(G_0\setminus E)=0$，即 (4) 成立。

反之，若 (4) 成立，则 $E=G_0\setminus(G_0\setminus E)$。$G_0$ 为 Borel 集（从而可测），$G_0\setminus E$ 为零测集（从而可测），故 $E$ 作为可测集的差也可测。

其余等价的证明类似。(1)$\Leftrightarrow$(3) 与 (1)$\Leftrightarrow$(2) 对偶；(1)$\Leftrightarrow$(5) 与 (1)$\Leftrightarrow$(4) 对偶。$\square$

**Thm 8.3.14（Jordan 可测 $\Rightarrow$ Lebesgue 可测）** 设 $E \subset \mathbb{R}^n$ 为有界 Jordan 可测集，则 $E$ 为 Lebesgue 可测集，且 $m(E) = |E|$，其中 $|E|$ 为 $E$ 的 Jordan 测度。

*证明*：由 Jordan 可测的定义，Jordan 外测度 $|E|^*$ 与内测度 $|E|_*$ 相等，记此公共值为 $|E|$。由于 Lebesgue 外测度 $m^*(E)$ 是使用可数矩形覆盖定义的 inf，而 Jordan 外测度 $|E|^*$ 仅使用有限矩形覆盖，故 $m^*(E) \le |E|^*$。类似地，Lebesgue 内测度满足 $m_*(E) \ge |E|_*$。于是：

$$
m^*(E) \le |E|^* = |E|_* \le m_*(E)
$$

但总有 $m_*(E) \le m^*(E)$，故 $m_*(E) = m^*(E) = |E|$。因此 $E$ 为 Lebesgue 可测，且 $m(E) = |E|$。$\square$

**Lemma 8.3.2（正测度集的稠密方体引理）** 设 $E \subseteq \mathbb{R}^n$ 满足 $m(E) > 0$，则对任意 $\lambda \in (0, 1)$，存在方体 $I$ 使得 $E$ 在 $I$ 内的密度超过 $\lambda$：

$$
\frac{m(E \cap I)}{|I|} > \lambda
$$

*证明*：由 Thm 8.3.13，存在开集 $G \supseteq E$ 使得 $m(G) < m(E)/\lambda$。将 $G$ 分解为可数个两两不交的二进方体之并（Thm 8.3.11）：$G = \bigcup_{k=1}^\infty I_k$。则：

$$
\sum_{k=1}^\infty m(E \cap I_k) = m(E) > \lambda \sum_{k=1}^\infty |I_k| = \lambda m(G)
$$

故必存在某个 $I_k$ 使得 $m(E \cap I_k) > \lambda |I_k|$。$\square$

**Thm 8.3.15（Steinhaus 定理）** 设 $E \subseteq \mathbb{R}^n$ 满足 $m(E) > 0$，记 $E \ominus E = \{ x - y : x, y \in E \}$，则存在 $\delta > 0$ 使得 $B_\delta(0) \subseteq E \ominus E$。即正测度集的差集包含一个以原点为中心的开球。

*证明*：取 $\lambda \in (1-1/2^{n+1}, 1)$，由 Lemma 8.3.2，存在方体 $I$（设边长为 $\delta$）使得 $\displaystyle \frac{m(E\cap I)}{|I|} > \lambda$，即 $m(E\cap I) > \lambda |I|$。令 $J = [-\delta/2,\ \delta/2]^n$（即以原点为中心、边长为 $\delta$ 的方体）。下证 $J \subseteq E \ominus E$。

对任意 $x_0 \in J$，记 $I_{x_0}=I+x_0$（即 $I$ 平移 $x_0$）。先看**一维情况**：$I=[a,a+\delta]$，平移后 $I_{x_0}=[a+x_0,a+x_0+\delta]$。两区间重叠部分的长度为

$$
\delta - |x_0|
$$

当 $|x_0|\le\delta/2$ 时，重叠长度 $\ge \delta/2$。

推广到 $n$ 维：$I$ 是边长为 $\delta$ 的方体，$I_{x_0}$ 在每个坐标 $i$ 上平移了 $x_{0,i}$。由于 $x_0\in J=[-\delta/2,\delta/2]^n$，每个坐标满足 $|x_{0,i}|\le\delta/2$，故第 $i$ 维上两区间重叠长度 $\ge\delta/2$。$n$ 个维度相乘即得交集体积的下界：

$$
m(I\cap I_{x_0}) \ge \prod_{i=1}^n \frac{\delta}{2} = \left(\frac{\delta}{2}\right)^n = \frac{|I|}{2^n}
$$

从而由容斥原理：

$$
m(I\cup I_{x_0})=|I|+|I|-m(I\cap I_{x_0})<2|I|-\frac{|I|}{2^n}=\Big(2-\frac1{2^n}\Big)|I|
$$

由 $\lambda>1-1/2^{n+1}$ 得 $2\lambda>2-1/2^n$，故 $m(I\cup I_{x_0})<2\lambda|I|$。

若 $(E\cap I)\cap(E\cap I_{x_0})=\emptyset$，则

$$
m\big((E\cap I)\cup(E\cap I_{x_0})\big)=m(E\cap I)+m(E\cap I_{x_0})>2\lambda|I|
$$

但 $(E\cap I)\cup(E\cap I_{x_0})\subseteq I\cup I_{x_0}$，故 $m(I\cup I_{x_0})\ge2\lambda|I|$，矛盾。因此 $(E\cap I)\cap(E\cap I_{x_0})\neq\emptyset$，存在 $x\in E\cap I$，$y\in E\cap I$ 使得 $x_0=x-y$，从而 $x_0\in E\ominus E$。$\square$


>[!info] 证明思路简述
>相当于证明存在开球，使得对于任意开球内的点 $x_0$，使得 $E\cap E+x_{0}\neq \varnothing$。
>如果能将 $E, E+x_{0}$ 框到一个集合 $K$ 内，使得 $E \cup E+x_{0}\subseteq K$ 且 $2m(E)>m(K)$，那么就可以证明交集非空了。
>但是 $E$ 的形状不好控制，不妨用一个方体来拟合，并保证 $E$ 在方体内的占比较大。那么假设 $E$ 就是方体 $I$，此时 $\left\lvert  I\cup I+\frac{\delta}{2}  \right\rvert=\left( 2-\frac{1}{2^n} \right)\lvert I \rvert$。
>此时只要让 $2m(E\cap I)>\left( 2-\frac{1}{2^n} \right)\lvert I \rvert$ 即可，这就回到了 Lemma 8.3.2。