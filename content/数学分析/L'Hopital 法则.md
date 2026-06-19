# L'Hopital 法则
> [[数学分析/README|← 返回索引]]

洛必达的证明都是固定一个点然后用 Cauchy 中值。

**Thm 7.0（基本型 $\frac{0}{0}$）**：设 $f,g$ 在 $x_0$ 附近可导（$x_0$ 处可除外），$g'(x)\neq0$，且 $\lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0$。若 $\lim_{x\to x_0}\frac{f'(x)}{g'(x)}$ 存在，则

$$
\lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}\frac{f'(x)}{g'(x)}
$$

证明：补充定义 $f(x_0)=g(x_0)=0$（可去间断点不影响极限），对任意 $x>x_0$，在 $[x_0,x]$ 上用 Cauchy 中值定理，存在 $\xi_x\in(x_0,x)$ 使 $\frac{f(x)}{g(x)}=\frac{f'(\xi_x)}{g'(\xi_x)}$。令 $x\to x_0^+$，$\xi_x\to x_0^+$，取极限即得。$\frac{\infty}{\infty}$ 型同理可证。

**常见的等价**：$\sin x,\tan x,\arcsin x,\arctan x\sim x$；$\cos x\sim 1-\frac{1}{2}x^2$；$\sin x\sim x-\frac{1}{6}x^3$，$\tan x\sim x+\frac{1}{3}x^3$。$e^x-1\sim x,\ln (1+x)\sim x$。$(1+x)^{\alpha}\sim 1+\alpha x$。

**Thm 7.1**（去核）：若 $F(x)\sim cx^{\alpha}$，$\varphi(x)\sim x$，则 $F(\varphi(x))\sim \varphi(x)$

**Thm 7.2**（去皮）：若 $\varphi(x),\psi(x)\to 0(x\to 0)$ 且 $F'(0)=A$，则 $F(\varphi(x))-F(\psi(x))\sim A(\varphi(x)-\psi(x))$。（用 Lagrange 中值定理）

推论：若 $f(x),g(x)\sim x$ 且 $f(x)-g(x)\sim cx^n$。则 $f(x)-g(x)\sim g^{-1}(x)-f^{-1}(x)$。

$$
\lim_{x\to 0} \frac{g^{-1}(x)-f^{-1}(x)}{x-g(f^{-1}(x))}=\lim_{x\to 0} \frac{g^{-1}(x)-g^{-1}(g(f^{-1}(x)))}{x-g(f^{-1}(x))}=1
$$
$$
\lim_{x\to 0}\frac{x-g(f^{-1}(x))}{f(x)-g(x)}=\lim_{x\to 0}\frac{f(f^{-1}(x))-g(f^{-1}(x))}{f(x)-g(x)}=1
$$