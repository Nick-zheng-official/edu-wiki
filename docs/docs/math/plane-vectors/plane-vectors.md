# 平面向量

向量有大小, 有方向, 可以使用几何表示(箭头, 画图)或代数表示(写下起点与终点, 上标箭头表示方向), 如 $\overrightarrow{AB}, \vec{a}, \vec{0}$. 在印刷体中, 向量也可使用粗体表示, 如 $\bm{a}, \bm{0}$ 等.

注意起点与终点不能调换, 如$\overrightarrow{AB} = - \overrightarrow{BA} = \overleftarrow{BA}$ ( $\overleftarrow{BA}$ 是有向线段的表示方法之一, 不建议向量如此表示). $\overrightarrow{AB}$ 与 $\overrightarrow{BA}$ 互为相反向量, 大小相等, 方向相反.

向量相等等价于其大小与方向均相等, 与位置无关. 故向量可以随意平移, 且向量共线等价于向量平行($\vec{a} \parallel \vec{b}$). 但在直线模块要严格区分平行与共线, 很多时候要特殊排除共线的情况.

注意区分线段, 向量与有向线段的概念. 线段有两个端点, 不能移动, 没有方向, $AB = BA$. 有向线段在线段的基础上增加方向, 但不能移动.

向量的大小称为其模(长), 如 $|\vec{a}|, |\overrightarrow{AB}|$ . 模长为 $1$ 的向量称为单位向量, $|\vec{e}| = 1$ ; 模长为 $0$ 的向量称为零向量, $|\vec{0}| = 0$ . 单位向量不唯一, 因为其方向不唯一. 零向量的方向任意, 其与任意向量均平行, 故向量平行不具有传递性(但若明确说明无零向量则有传递性).

向量垂直用 $\vec{a} \perp \vec{b}$ 表示, 平行(共线) 用 $\vec{a} \parallel \vec{b}$ 表示. 注意, 平行不等于方向相同, 可能相反.

## 线性运算

向量的加法符合平行四边形法则(共起点)与三角形法则(首尾相连). 遇见很多向量的加法一般考虑首尾相连看起点与终点, 即$\overrightarrow{AB} + \overrightarrow{BC} + \dots + \overrightarrow{YZ} = \overrightarrow{AZ}$ .

向量减法可以通过相反向量转化为向量加法, 先平移至共起点, $\overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{OA} + \overrightarrow{BO} = \overrightarrow{BA}$ , 得到的向量为连接两个终点, 方向由后一个向量终点指向前一个向量终点.

向量的数乘运算即 $\lambda\vec{a}$ , 一个数乘一个向量, 表示向量长度伸缩. 若 $\lambda < 0$ 则向量会反向.

向量线性运算得到的结果为向量, 故 $0 \cdot \vec{a} = \vec{0}, \lambda \cdot \vec{0} = \vec{0}$ .

解决平面向量题目画图很方便, 因为向量可以联系几何与代数. 一般将向量共起点放置(小心锐角与钝角的区别, 不能主观臆断为锐角)或首尾相接放置. 需要掌握几种常见的代数语言转化几何图形的方法, 如 $|\vec{a} - \vec{b}| = m, m$ 为定值, 即代表图形为一个圆; $|\vec{a} - \lambda\vec{b}|_{min}$ ( $|\vec{a} + \lambda\vec{b}|_{min}$ 同理, $\lambda$ 取负值即可)表示一个点到一条直线之间的距离, 当 $\vec{a} \pm \lambda\vec{b}$ 图像为直角三角形时取得最小值.

### 三点共线定理

![](../images/三点共线定理.png){ width=500px }

$$\overrightarrow{OC} = \mu\overrightarrow{OA} + \lambda\overrightarrow{OB}, \mu + \lambda = 1 \Leftrightarrow A, B, C 三点共线$$

对于系数 $\mu, \lambda$ 没有正负要求, 可以为负数. 但当二者均为正数时, $C$ 在 $AB$ 之间, 否则 $C$ 在 $AB$ 外侧, 此时一般首先移项将系数全部变为正数(自己写也是先写正数再移项). 确定 $\mu, \lambda$ 的取值可以通过找对边所占整条线段 $AB$ 的比例, 如 $\mu$ 为 $\frac{BC}{AB}$ , $\lambda$ 为 $\frac{AC}{AB}$ . 可以发现, 此定理与 $AB$ 边上的等分点(比例)关系密切.

特殊地, 中线的向量式可以用三点共线表示, 即若 $AC = BC$ , 有 $\overrightarrow{OC} = \frac{1}{2}\overrightarrow{OA} + \frac{1}{2}\overrightarrow{OB}$ .

由于图形很像鸡爪子, 所以也可成为鸡爪子模型(但我并不能看出来).

若三点不共线, 可以由向量伸缩(一般可以算出倍数关系)变为共线.

等和线是三点共线的推论.

![](../images/等和线.png){ width=500px }

确定等和线 $\mu + \lambda$ 的值就看 $O$ 到等和线距离是初始距离( $O$ 到 $AB$ )的几倍即可.

等和线可以由 $\overrightarrow{OA}, \overrightarrow{OB}$ 同时延长 $\mu + \lambda$ 倍后确定, 或者根据 $O$ 到等和线的距离确定, 或 $AB$ 上任意一点 $C$ 延长 $\overrightarrow{OC}$ $\mu + \lambda$ 倍后过点 $C'$ 做 $AB$ 的平行线得到.

一般出现鸡爪子模型, 问 $\mu + \lambda$ 最值时就需要使用等和线, 在几何图形中找边界情况. 求最值时注意两平行线(等和线)之间的垂线段可以平移, 一般平移到合适的位置计算更方便. 若所求的 $\mu + \lambda$ 带有系数, 如 $2\mu + \lambda$ , 就要找 $\frac{1}{2}\overrightarrow{OA}$ 的等效向量( $2\mu \cdot \frac{1}{2}\overrightarrow{OA}$ 转化后才能用等和线).

## 数量积

数量积(内积)是向量点乘, 得到一个数字; 外积是向量叉乘, 得到一个新的向量.
