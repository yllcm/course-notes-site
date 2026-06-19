
> [[数学分析|← 返回索引]]

**Df 8.3.1（Lebesgue 外测度）**设 $E$ 是 $\mathbb{R}^n$ 空间中的任意子集（即 $E \subset \mathbb{R}^n$），则 $E$ 的**勒贝格外测度**记为 $m^*(E)$，其定义为：

$$
m^*(E) = \inf \left\{ \sum_{k \ge 1} |R_k| \ \bigg| \ E \subset \bigcup_{k \ge 1} R_k, \ R_k \text{ 为方体} \right\}
$$

**Thm 8.3.1（Lebesugue 外测度的性质）**

1. 单调性： $E \subset F$，则 $m^*(E) \le m^*(F)$。
2. $\sigma$-次可加性：对任意可数个集合序列 $\{E_k\}_{k=1}^{\infty}$，有：

$$
m^*\left( \bigcup_{k \ge 1} E_k \right) \le \sum_{k=1}^{\infty} m^*(E_k)
$$

证明：对每一个集合 $E_k$，都存在一列方体 $\{R_{k,j}\}_{j=1}^{\infty}$ 能够覆盖 $E_k$，即：

$$
E_k \subset \bigcup_{j=1}^{\infty} R_{k,j}
$$

并且这些方体的体积之和满足以下不等式（放大一个级数项）：

$$
\sum_{j=1}^{\infty} |R_{k,j}| < m^*(E_k) + \frac{\varepsilon}{2^k}
$$

求和可得

$$
m^*\left( \bigcup_{k=1}^{\infty} E_k \right) \le \sum_{k=1}^{\infty} m^*(E_k) + \varepsilon
$$

**Df 8.3.2（Lebesgue 内测度）** 对集合 $E\in \mathbb{R}^n$，设矩形 $R$ 满足 $E\subset R$，则 $E$ 的 Lebesgue 内测度定义为 $m_{*}(E)=\lvert R \rvert-m^*(R\setminus E)$。

**Df 8.3.3（Lebesgue 可测）** $E\in \mathbb{R}^n$ 有界，则 $E$ 称为 L-可测，如果 $m^*(E)=m_{*}(E)$，即 $\lvert R \rvert=m^*(E)+m^*(R\setminus E)$。

**Thm 8.3.2（Carathéodory 定理）** $E\in \mathbb{R}^n$ 有界，则 $E$ 是 L-可测 $\iff$ 对任意 $F\in \mathbb{R}^n$，$m^*(F)=m^*(F\cap E)+m^*(F\setminus E)$。

*证明*：($\Leftarrow$) 取 $F$ 为包含 $E$ 的矩形即得 Df 8.3.3。

($\Rightarrow$) 先设 $F=r$ 为矩形。取矩形 $r_0\supseteq E\cup r$。对 $\forall\varepsilon>0$，由外测度定义存在矩形列 $\{R_k\},\{\tilde R_k\}$ 使得

$$
E\subset\bigcup R_k,\quad r_0\setminus E\subset\bigcup\tilde R_k,\quad
\sum|R_k|<m^*(E)+\frac\varepsilon2,\quad\sum|\tilde R_k|<m^*(r_0\setminus E)+\frac\varepsilon2
$$

>[!info] 
>这一步的目的是把 L-可测的 $E$ 打碎成矩形，方便后面的逼近分析

则 $\{R_k\}\cup\{\tilde R_k\}$ 覆盖 $r_0$，故

$$
\sum|R_k|+\sum|\tilde R_k|<m^*(E)+m^*(r_0\setminus E)+\varepsilon=|r_0|+\varepsilon
$$

注意 $r\cap E\subset\bigcup(R_k\cap r)$，$r\setminus E\subset\bigcup(\tilde R_k\cap r)$（因 $r\setminus E\subset r_0\setminus E$），所以

$$
\begin{aligned}
m^*(r\cap E)+m^*(r\setminus E) &\le \sum|R_k\cap r|+\sum|\tilde R_k\cap r| \\
&= \big(\sum|R_k|-\sum|R_k\setminus r|\big)+\big(\sum|\tilde R_k|-\sum|\tilde R_k\setminus r|\big) \\
&< (|r_0|+\varepsilon)-(\sum|R_k\setminus r|+\sum|\tilde R_k\setminus r|)
\end{aligned}
$$

>[!info]
>注意这里利用了 Jordan 测度的可加性（由 $\chi_{R_{k}}=\chi_{R_{k}\cap r}+\chi_{R_{k}\setminus r}$ 导出）

由于 $\{R_k\}\cup\{\tilde R_k\}$ 覆盖 $r_0$，在 $r_0\setminus r$（即 $r_0$ 在 $r$ 外的部分）上的覆盖体积至少为 $|r_0\setminus r|$，故 $\sum|R_k\setminus r|+\sum|\tilde R_k\setminus r|\ge|r_0\setminus r|$。代入得

$$
m^*(r\cap E)+m^*(r\setminus E)<|r_0|+\varepsilon-|r_0\setminus r|=|r|+\varepsilon
$$

由 $\varepsilon$ 任意性得 $m^*(r\cap E)+m^*(r\setminus E)\le|r|$；反向不等式由次可加性成立。故对矩形 $r$ 结论成立。

对一般 $F$，取矩形覆盖 $\{R_k\}$ 使 $F\subset\bigcup R_k$。由已证结论及次可加性：

$$
\sum|R_k|=\sum\big(m^*(R_k\cap E)+m^*(R_k\setminus E)\big)\ge m^*(F\cap E)+m^*(F\setminus E)
$$

两边取下确界得 $m^*(F)\ge m^*(F\cap E)+m^*(F\setminus E)$，再结合次可加性即得等式。$\square$

**Thm 8.3.3（内测度与矩形 $R$ 的取法无关）** $\lvert R \rvert-m^*(R\setminus E)=\lvert r \rvert-m^*(r\setminus E)$。

取 $r\subseteq R$，则 

$$
\begin{align}

m^*(R\setminus E) & =m^*((R\setminus E)\cap r)+m^*((R\setminus E)\setminus r) \\
 & =m^*(r\setminus E)+m^*(R\setminus r) \\
 & =m^*(r\setminus E)+\lvert R \rvert-\lvert r \rvert

\end{align}
$$

等式成立。

对一般 $r,R$，$E\subset r, E\subset R$，则 $r\cap R$ 为矩形，$r\cap R\subset r,R$。则 $\lvert R \rvert-m^*(R\setminus E)=\lvert R\setminus r \rvert-m^*((R\cap r)\setminus E),\lvert r \rvert-m^*(r\setminus E)=\lvert R\cap r \rvert-m^*((R\cap r)\setminus E)$。所以结论成立。

**Df 8.3.4（任意集合的 Lebesgue 可测）** 对任意 $E\subset \mathbb{R}^n$，$m^*(E)=\lim_{ s \to \infty }m^*(E\cap Q_{s}(0))$，$E$ 称为 L-可测，等价于对任意 $s$，$E\cap Q_{s}(0)$ 为 L-可测。

**Df 8.3.5** $\mathcal{L}(\mathbb{R}^n)=\left\{ A:A\subset \mathbb{R}^n,A\text{为 }L\text{ -可测} \right\}$。


**Thm 8.3.4（Lebesgue 测度的更多性质）**

(P1) $m(E+x_{0})=m(E)$，$E+x_{0}=\left\{ x+x_{0}:\forall x\in E \right\}$。

**Df 8.3.6（$\sigma$ 代数）**$\mathcal{M}=\left\{ A:A\subset X\neq\varnothing \right\}$ 称为 $X$ 上的 $\sigma$ 代数，如果

1. $\varnothing,X\in \mathcal{M}$。
2. $E\in \mathcal{M}\implies X\setminus E\in \mathcal{M}$。
3. $E_{k}\in \mathcal{M},k=1,2,\dots\implies \bigcup_{k=1}^{\infty}\in \mathcal{M}$。

**Rmk 8.3.1** $\mathcal{M}$ 为 $X$ 上的 $\sigma$-代数，则

$$
E_{k}\in \mathcal{M}\implies\bigcap_{k=1}^{\infty} E_{k}\in \mathcal{M}
$$

**Thm 8.3.5（Lebesgue 可测集是 $\sigma$-代数）** $\mathcal{L}(\mathbb{R}^n)$ 为 $\mathbb{R}^n$ 上的 $\sigma$-代数，且若 $\left\{ E_{k} \right\}$ 为一列 $L$-可测的互不相交的集合，则 


$$
m\left( \bigcup_{k=1}^\infty E_{k} \right)=\sum_{k=1}^{\infty} m(E_{k})
$$

1. $\varnothing,\mathbb{R}^n\in \mathcal{L}(\mathbb{R}^n)$
2. 对于任意 $E,F\in \mathcal{L}(\mathbb{R}^n)$，任意 $W\in \mathbb{R}^n$

$$
\begin{align}
m^*(W)&=m^*(W\cap E)+m^*(W\setminus E) \\
 & =m^*(W\cap E\setminus F)+m^*(W\cap E\cap F)+m^*(W\setminus E) \\
 &  \geq m^*(W\cap( E\setminus F))+m(W\setminus(E\setminus F))
\end{align}
$$


![[Pasted image 20260616140350.png]]

>[!info]
>上面的不等式相当于用 Caratheodory 条件不断细分区域，分开的区域的并一定是大集合 $W$，此时再把除目标区域之外的区域合并，用大于等于号连接。

所以 $E\setminus F$ 是可测的，$E\cup F=\mathbb{R}^n\setminus (\mathbb{R}^n\setminus E)\setminus F\in \mathcal{L}(\mathbb{R}^n)$。

3. 先设 $\{E_k\}\subset\mathcal{L}(\mathbb{R}^n)$ 两两不交，令 $E=\bigcup_{k=1}^\infty E_k$。对任意 $F\subset\mathbb{R}^n$，利用 Carathéodory 条件（Thm 8.3.2）迭代可得：

$$
m^*(F)=\sum_{k=1}^N m^*(F\cap E_k)+m^*\Big(F\setminus\bigcup_{k=1}^N E_k\Big)
$$

取 $F=E$ 即得 $m(E)=\sum_{k=1}^\infty m(E_k)$。令 $N\to\infty$，由 $F\setminus E\subset F\setminus\bigcup_{k=1}^N E_k$ 得：

$$
m^*(F)\ge\sum_{k=1}^\infty m^*(F\cap E_k)+m^*(F\setminus E)\ge m^*(F\cap E)+m^*(F\setminus E)
$$

结合次可加性 $m^*(F)\le m^*(F\cap E)+m^*(F\setminus E)$ 即得 $m^*(F)=m^*(F\cap E)+m^*(F\setminus E)$，故 $E$ 可测。

对一般的 $\{E_k\}\subset\mathcal{L}(\mathbb{R}^n)$，令 $F_k=E_k\setminus\bigcup_{j<k}E_j$，则 $F_k$ 可测且两两不交，$\bigcup E_k=\bigcup F_k$，由已证结论知 $\bigcup E_k$ 可测。

**Thm 8.3.6** 若 $\left\{ E_{k} \right\}_{k=1}^{+\infty }$ 单增，即 $E_{1}\subset E_{2}\subset E_{3}\dots$，则

$$
\varlimsup_{ k \to \infty } E_{k}=\varliminf_{ k \to \infty } E_{k}\triangleq \lim_{ n \to \infty } E_{k}=\bigcup_{k=1}^{\infty}E_{k}=E
$$

且 $m(E)=\lim_{ k \to \infty }m(E_{k})$。

*证明*：将 $E$ 分解为不交并：

$$
E = E_1 \cup \bigcup_{k=2}^{\infty} (E_k \setminus E_{k-1})
$$

由可数可加性：

$$
m(E) = m(E_1) + \sum_{k=2}^{\infty} m(E_k \setminus E_{k-1}) = \lim_{N\to\infty} \Big[ m(E_1) + \sum_{k=2}^{N} m(E_k \setminus E_{k-1}) \Big]
$$

而 $E_N = E_1 \cup \bigcup_{k=2}^{N} (E_k \setminus E_{k-1})$，故 $m(E_N) = m(E_1) + \sum_{k=2}^{N} m(E_k \setminus E_{k-1})$。因此 $m(E) = \lim_{N\to\infty} m(E_N)$。$\square$

**Df 8.3.7（集合列的上下极限）**

$$
\bigcap_{k=1}^{\infty}\bigcup_{j=k}^{\infty}E_{j}=\varlimsup_{ k \to \infty } E_{k}
$$

$$
\bigcup_{k=1}^{\infty}\bigcap_{j=k}^{\infty}E_{j}\triangleq \varliminf_{ k \to \infty } E_{k}
$$

**Thm 8.3.7** 若 $\left\{ E_{k} \right\}_{k=1}^{\infty}$ 为 $L$-可测列，则 $\varlimsup_{ k \to \infty }E_{k}$ 与 $\varliminf_{ k \to \infty }E_{k}$ 均为 $L$-可测。

*证明*：由定义 $\varliminf_{k\to\infty} E_k = \bigcup_{k=1}^{\infty} \bigcap_{j=k}^{\infty} E_j$。每个 $\bigcap_{j=k}^{\infty} E_j$ 是可测集的可数交，由 Thm 8.3.5 知可测；可数并仍可测。$\varlimsup$ 同理（交换交与并的顺序）。$\square$

**Thm 8.3.8** $\left\{ E_{k} \right\}$ 单减可测，则 $E=\bigcap_{j=1}^{+\infty} E_{j}$ 可测。$\varlimsup_{ k \to \infty }E_{k}=\varliminf_{ k \to \infty }E_{k}\triangleq \lim_{ k \to \infty }E_{k}$。当 $m(E_{k})$ 不恒为 $+\infty$ 时有 $m(E)=\lim_{ k \to \infty }m(E_{k})$。

*证明*：可测性由 Thm 8.3.5 直接得到（可数交封闭）。下证测度收敛。

由条件存在 $N$ 使 $m(E_N) < \infty$。考虑 $k \ge N$ 时的子列，令 $F_k = E_N \setminus E_k$，则 $\{F_k\}_{k=N}^{\infty}$ 单增且 $F_k \subseteq E_N$。由 Thm 8.3.6：

$$
m\Big(\bigcup_{k=N}^{\infty} F_k\Big) = \lim_{k\to\infty} m(F_k)
$$

而 $\bigcup_{k=N}^{\infty} F_k = E_N \setminus \bigcap_{k=N}^{\infty} E_k = E_N \setminus E$，且 $m(F_k) = m(E_N) - m(E_k)$（因 $E_k \subseteq E_N$ 且测度有限）。代入得：

$$
m(E_N) - m(E) = m(E_N) - \lim_{k\to\infty} m(E_k)
$$

两边消去 $m(E_N)$（有限）即得 $m(E) = \lim_{k\to\infty} m(E_k)$。$\square$

