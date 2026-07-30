# 文章撰写

在文章开始之前，**EDU Wiki** 项目组全体成员十分欢迎您为本项目贡献页面．

本页面将列出在 **EDU Wiki** 编写过程时推荐使用的格式规范与编辑方针．请您在撰稿或者修正 Wiki 页面以前，仔细阅读以下内容，以帮助您完成更高质量的内容．

## 基础的写作技巧

本项目中几乎所有文档都结合使用 Markdown 与 LaTeX 来撰写．下面对这两种语言进行简单的介绍．

### Markdown

**Markdown** 是一种轻量级文档排版系统, 它允许你使用一些符号来表示排版布局, 并通过特定方式渲染出文档结构. 它简单易学, 其基础用法如下: 

- 标题. 你可以在标题前添加若干 `#` 来表示这是几级标题, 几个 `#` 就代表几级标题, 如本文的一级标题为 `# 文章撰写` , 此段所在的三级标题为 `### Markdown`.
- 粗体与斜体. 你可以使用左右各一个 `*` 括起你想写为斜体的文字, 如 *斜体* ( `*斜体*` ); 类似地你可以使用左右各两个 `*` 括起你想写为粗体的文字, 如 **粗体** ( `**粗体**` ); 当然, 你也可以使用左右各三个 `*` 括起你想写为粗斜体的文字, 如 ***粗斜体*** ( `***粗斜体***` ). 实际上, `*` 也可被替代为 `_` , 但为统一格式建议写作 `*` . 
- 删除线. 我们不建议你在本 **Wiki** 中使用删除线语法. ~~删除线~~ 可以使用 `~~删除线~~` 得到. 
- 列表. 列表分为有序列表与无序列表. 无序列表可以使用并列的, 统一缩进的 `-` 来表示, 如 `- 无序列表项`; 有序列表可以使用并列的, 统一缩进的数字加点号, 如 `1. 有序列表项` . 注意, `-` 或 `1.` 与列表项间应有空格; 列表项若为句子, 需要在末尾添加标点符号, 除最后一项使用 `;` , 最后一项使用 `.` . 实际上, 无序列表中的 `-` 可以使用 `*` 或 `+` 来替代, 但为统一格式建议写作 `-` . 
- 链接与图片. 你可以使用 `[链接文字](链接地址)` 来添加链接, 如 `[EDU Wiki](https://edu-wiki.pages.dev/)`. 对于图片, 你需要使用 `![图片描述](图片地址)` (增加一个 `!` )才能保证其正常渲染, 如 `![EDU Wiki Logo](/docs/static/img/logo.png)`. 特殊地, 你被建议使用如 `<https://edu-wiki.pages.dev/>` 等此类格式来代替 `[https://edu-wiki.pages.dev/](https://edu-wiki.pages.dev/)` 以实现 [https://edu-wiki.pages.dev/](https://edu-wiki.pages.dev/) 的效果. 对于其中涉及到的地址的写法, 下文会介绍. 
- 下载: 下载文件需要使用 **html** 格式, 如 `<a href="https://raw.githubusercontent.com/Nick-zheng-official/edu-wiki/main/docs/static/img/logo.psd" download="logo.psd">下载 logo.psd</a>` , 其中 `href` 是文件的 URL, `download` 是文件的下载名, `<a>` 与 `</a>` 间的内容为链接显示的文字. 对于其中涉及到的地址的写法, 下文会介绍. 
- 引用. `>` 被用于表示引用, 其后为引用的文字. 如 `> 这是一个引用` . 当然, 你可以使用多个 `>` , 辅以适当的缩进, 来表示引用的层级. 或者, 你也可以连续多行使用 `>` 来表示连续引用. 
- 代码. 行内代码使用 ` ` ` 括起, 如 ` `这是一个行内代码` ` . 对于代码块, 你需要在上下均使用 ` ``` ` 来包裹代码块, 且上方 ` ``` ` 后可以选择声明代码块语言(如 `md` , `latex` , `plain` 等, 或不添加也可), 以获得对应语言的高亮显示. 下文有具体实例. 需要注意的是, 如果行间代码块内需要出现 ` ``` ` , 则考虑将外层包裹的 ` ``` ` 改为 ` `` `` ` . 
- 数学公式. 在本项目中, 针对行内公式, 你可以使用两个 `$` 括起你使用 **LaTeX** 编写的数学公式, 如 `$1 + 1 = 2$` . 对于行间公式, 你需要在上下均使用 `$$` 来包裹 **LaTeX** 数学公式, 下文有具体实例. 
- 分割线. 你可以使用 `---` 来添加分割线, 注意其上下各一行内 **不能** 有 **任何** 内容, 否则会出现格式问题. 同样地, 你也可以使用 `***` 来表示分割线, 但因格式统一问题不建议使用. 
- 表格. 你可以使用 `|` 与 `---` 来绘制表格, 但更建议你通过编辑器的可视化工具来绘制表格. 对齐方式有以下三种: `:---` 左对齐; `:---:` 居中; `---:` 右对齐. 
- 任务清单. `- [ ] 代办任务` 与 `- [x] 已完成任务` . 
- 脚注. `[^1]` 等可以用于添加注释. 显然, 你需要在文档末尾添加对应的注释, 通过再次使用 `[^1]: 这是注释内容 1` 来实现. 如此, 你可以在注释的"定义"与"应用"间进行跳转. 实际上, `1` 可以被替换为任意文本. 
- 注释. 这里特指仅在文本模式下可见, 不被渲染的注释. 我们通过 `html` 的方式实现, 如 `<!-- 这是一个注释 -->` . 当然, 也可以实现多行注释, 只需类似行间公式般, `<!--` 与 `-->` 包裹即可. 

注意, 特殊地排版效果, 如居中或改变颜色等不被 Markdown 所支持, 需要使用 **html** 格式来实现. 如 `<div style="text-align: center;">居中文字</div>` 与 
`<span style="color: red;">红色文字</span>`. 

需要注意的是, 文章会自动换行. 若你确需要手动换行, 可以在行末使用两个连续的空格. 若你想另起一段, 请在段落间留出一行或多行空行. 多行空行仅会被当作一行空行; 多个连续的空格实现的间距也仅为一个空格间距. 

对于代码块, 行间公式, 列表, 表格, 多行注释等占用多行的内容, 你需要在其上下各留出一行 **空白行**, 否则会出现格式问题. 如:

````plain

```plain
这是一个代码块. 
```

$$
1 + 1 = 2
$$

- 无序列表项 1
- 无序列表项 2
- 无序列表项 3

1. 有序列表项 1
2. 有序列表项 2
3. 有序列表项 3

| A | B | C |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

<!--
这是多行注释第一行
这是多行注释第二行
-->

````

Markdown 文档的后缀为 `.md` . 此类文件的编辑, 我们一般使用特殊地编辑器, 如 "所见即所得" 的 `Typora` , `Obsidian` ; 当然, 如果你喜欢同时查看源文本与预览效果, 你可以选择万能的 `VS Code` 及其插件. 

随着你的使用, Markdown 纯文本的优势会愈发突出. 当然, 掌握 Markdown 的最好方式是实践. 所以, 不妨多写一些 Markdown 文档, 来熟悉其语法.

### LaTeX

LaTeX（读作/ˈlɑːtɛx/或/ˈleɪtɛx/）是一个让你的文档看起来更专业的排版系统，而不是文字处理器．它尤其适合处理篇幅较长、结构严谨的文档，并且十分擅长处理公式表达．它是免费的软件，对大多数操作系统都适用．

LaTeX 基于 TeX（Donald Knuth 在 1978 年为数字化排版设计的排版系统）．TeX 是一种电脑能够处理的低级语言，但大多数人发现它很难使用．LaTeX 正是为了让它变得更加易用而设计的．目前 LaTeX 的版本是 LaTeX 2e．

如果你习惯于使用微软的 Office Word 处理文档，那么你会觉得 LaTeX 的工作方式让你很不习惯．Word 是典型的「所见即所得」的编辑器，你可以在编排文档的时候查看到最终的排版效果．但使用 LaTeX 时你并不能方便地查看最终效果，这使得你专注于内容而不是外观的调整．

一个 LaTeX 文档是一个以 `.tex` 结尾的文本文件，可以使用任意的文本编辑器编辑，当然, 本文不会介绍如何编辑 LaTeX 文档, 因为本项目主要使用其数学模式的公式功能．正如前文所述, 我们使用 `$` 与 `$$` 来包裹 `LaTeX` 数学公式, 启用数学模式. 

如果是生成带标号的公式，可以使用 `\begin{equation}...\end{equation}`．例如：

```latex
\begin{equation}
1 + 1 = 2
\end{equation}
```

生成的效果为：

$$
\begin{equation}
1 + 1 = 2
\end{equation}
$$

使用 `\begin{align}...\end{align}` 来撰写多行公式．例如：

```tex
\begin{align}
  a & = b + c \\
    & = y - z
\end{align}
```

生成的效果为

$$
\begin{eqnarray}
  a & = b + c \\
    & = y - z
\end{eqnarray}
$$

要撰写不标号的公式就在环境标志的后面添加 `*` 字符，如 `{equation*}`，`{eqnarray*}`．

??? warning "Warning"
    可以发现，使用 `eqnarray` 时，会出现等号周围的空隙过大之类的问题．

    可以使用`amsmath` 宏包中的 `align` 环境：

    ``tex     \usepackage{amsmath}     ...     \begin{align}       a & = b + c \\         & = y - z     \end{align}     ``

    或在行间公式中使用`aligned` 环境．它们的名字后面加上星号后，公式就不带标号了．

    详见[更多阅读](#更多阅读) 中第一篇资料的「4.4 多行公式」．

#### 常用数学符号

尽管一些基础的符号可以直接键入，但大多数特殊符号需要使用命令来显示．

本书只是数学符号使用的入门教程，LaTeX Wikibook 的数学符号章节是另一个更好更完整的教程．如果想要了解更多关于数学符号的内容请移步．如果你想找到一个特定的符号，可以使用 [Detexfiy](http://detexify.kirelabs.org)，它可以识别手写字符．当然, 也可查阅 [数学符号表](https://edu-wiki.pages.dev/home/contrib/symbols/) 来获取更多符号的命令．

在写作中, 难免会需要输入一些不熟悉的数学符号. 这时, 询问 AI 来获取符号的命令是可取的. 当然, 使用上述两个工具也可以获取符号的命令．以下介绍最基础的数学符号的命令．

##### 调整间距与换行

我们可以键入空格或使用 `\, , \; , \quad, \qquad` 等命令来调整间距, 间距大小递增. 多个空格连续使用时, 仅识别为一个空格, 但其余命令可以叠加．你可以自行尝试不同的命令以找到合适的间距. 

在 LaTeX 环境下, 我们使用 `\\` 来换行. 同时, 由于 LaTeX 行间公式默认居中, 故对于不同行的对齐, 考虑使用 `$`. 例如:

```latex
\begin{align}
  原式 & = 1 + 1 \\
    & = 2
\end{align}
```

效果为:

$$
\begin{align}
  原式 & = 1 + 1 \\
    & = 2
\end{align}
$$

##### 上标和下标

上标（Powers）使用 `^` 来表示，比如 `$n^2$` 生成的效果为 $n^2$．

下标（Indices）使用 `_` 表示，比如 `$2_a$` 生成的效果为 $2_a$．

如果上标或下标的内容包含多个字符，请使用花括号包裹起来．比如 `$b_{a-2}$` 的效果为 $b_{a-2}$．

##### 分数

分数使用 `\frac{分子}{分母}` 命令插入．比如 `$$\frac{a}{3}$$` 的生成效果为

$$
\frac{a}{3}
$$

分数可以嵌套．比如 `$$\frac{y}{\frac{3}{x}+b}$$` 的生成效果为

$$
\frac{y}{\frac{3}{x}+b}
$$

##### 根号

我们使用 `\sqrt{...}` 命令插入根号．省略号的内容由被开根的内容替代．如果需要添加开根的次数，使用方括号括起来即可．

例如 `$$\sqrt{n^2}$$` 的生成效果为

$$
\sqrt{n^2}
$$

而 `$$\sqrt[3]{n^2}$$` 的生成效果为

$$
\sqrt[3]{n^2}
$$

##### 运算符

对于键盘可键入的运算符，直接键入即可．需要注意的是, 一些特殊符号, 如 `%`, `&`, `^`, `_` 等, 需要使用反斜杠来转义, 才能正常显示．例如 `1 + [0 + (1 - 1)] = 1, 0.1\% > 0` . 对于部分运算符, 我们需要通过命令来表示, 如 `\times` 或 `\cdot` , `\div`, `\pm`, `\mp` , `\approx` , `\ne` , `\ge` , `\le` , `\dots` , `\bmod` , `\pmod` (请注意不要使用已弃用的 `\mod` ), `\log` , `\lim` , `\sin` , `\to` , `\in` , `\max` , `\min` 等, 分别显示为 $\times, \cdot, \div, \pm, \mp, \approx, \ne, \ge, \le, \dots, \bmod, \pmod, \log, \lim, \sin, \to, \in, \max, \min$ ．

使用 `\sum` 和 `\prod` 来插入求和式与求积式．对于两种符号，上限使用 `^` 来表示，而下限使用 `_` 表示．

`$$\sum_{i = 1}^n 2^i$$` 的生成效果为

$$
\sum_{i = 1}^n 2^i
$$

而 `$$\prod_{i = 1}^n 2^i$$` 的生成效果为

$$
\prod_{i = 1}^n 2^i
$$

##### 希腊字母

我们可以使用反斜杠加希腊字母的名称来表示一个希腊字母．名称的首字母的大小写决定希腊字母的大小写．例如: 

- `$\alpha, \Alpha$`=$\alpha, \Alpha$
- `$\beta, \Beta$`=$\beta, \Beta$
- `$\delta, \Delta$`=$\delta, \Delta$
- `$\pi, \Pi$`=$\pi, \Pi$
- `$\sigma, \Sigma$`=$\sigma, \Sigma$
- `$\phi, \Phi, \varphi$`=$\phi, \Phi, \varphi$
- `$\theta, \Theta$`=$\theta, \Theta$
- `$\omega, \Omega$`=$\omega, \Omega$
- `$\mu, \Mu$`=$\mu, \Mu$
- `$\nu, \Nu$`=$\nu, \Nu$
- `$\epsilon, \Epsilon$`=$\epsilon, \Epsilon$

## 格式手册

在格式方面, **EDU Wiki** 与 **OI Wiki** 基本保持一致. 下文节选自 **OI Wiki** 的 [格式手册](https://oi-wiki.org//intro/format/) , 有部分修改.

### 太长不看版

为方便初次阅读本文档的用户，本节列举该手册中的若干重点事项：

- 文件存储：

  - 使用小写文件名，以 `-` 代替空格．详见 [SAVE-1](#SAVE-1)．
  - 不要插入外链图片．详见 [SAVE-2](#SAVE-2)．
  - 图片尽可能使用 SVG 格式，只应使用 SVG 1.1 标准．详见 [SAVE-3](#SAVE-3)．
  - 动图应使用 SVG 或 APNG 格式．详见 [SAVE-4](#SAVE-4)．
  - 有源文件的图片建议同时提交源文件．详见 [SAVE-5](#SAVE-5)．
  - 插入外链时建议同时插入快照链接．详见 [SAVE-6](#SAVE-6)．
  - 不要以插入外链的方式插入内链．详见 [SAVE-7](#SAVE-7)．
- 标点符号：

  - 规范使用标点符号．在每句话的末尾添加 **句号**．详见 [PUNC-1](#PUNC-1) 至 [PUNC-7](#PUNC-7)．
  - 注意区分连接号（hyphen、en dash、em dash）．详见 [PUNC-8](#PUNC-8)．
- Markdown 语法与主题扩展语法：

  - 不要使用标题替代加粗．不要在标题写 LaTeX 公式．详见 [LINT-1](#LINT-1)、[MDFM-1](#MDFM-1)、[CONT-4](#CONT-4)、[CONT-9](#CONT-9)．
  - 使用折叠框[^note3]语法和选项卡[^note6]语法时，须保持内部缩进一致，**对空行也是如此**．**不要漏掉** 空行的空格缩进．详见 [LINT-6](#LINT-6)、[MDFM-6](#MDFM-6)．
  - 不要使用删除线 `~~foo~~` 语法．详见 [LINT-3](#LINT-3)．
  - 行间公式应写作

    ```text
    $$
    a^{2}=b^{2}+c^{2}
    $$
    ```

    而不是 `$$a^{2}=b^{2}+c^{2}$$`．详见 [LINT-5](#LINT-5)．
  - 使用折叠框而不是块引用（Blockquotes）．详见 [MDFM-5](#MDFM-5)．
  - 代码块只应使用 ` ``` ` 语法，且须标注语言．详见 [LINT-7](#LINT-7)、[MDFM-3](#MDFM-3)．
- LaTeX 公式：

  - 不应与 [数学符号表](./symbols.md) 相冲突．详见 [MATH-1.1](#MATH-1.1)．
  - 注意字体的使用，详见 [MATH-1.2](#MATH-1.2)、[MATH-1.15](#MATH-1.15)、[MATH-2.6](#MATH-2.6)、[MATH-2.7](#MATH-2.7)．
  - 不要滥用 LaTeX 公式．详见 [MATH-1.14](#MATH-1.14)．

### 对本文档的格式要求

- <a id="FREQ-1"></a>FREQ-1：修订格式手册的条目时需同时补充 Changelog．若只是修正格式，则无需补充 Changelog．
- <a id="FREQ-2"></a>FREQ-2：除 [太长不看版](#太长不看版) 一节外，格式手册的条目都需要有不重复的编号，编号需要匹配正则表达式 `(?<category>[A-Z]{4})-(?<id>[1-9][0-9]*(?:\.[1-9][0-9]*)*)`，其中 `category` 应具有直观的含义．说明文字不需要有编号．
- <a id="FREQ-3"></a>FREQ-3：[太长不看版](#太长不看版) 的条目必须来自格式手册其他章节的内容，且需在末尾引用对应的条目编号．
- <a id="FREQ-4"></a>FREQ-4：条目的编号一旦确定就不应更改．如果确需更改（如删除、合并条目），则应用类似「已废止」、「迁移至 XXXX-id」的文字注明．

### 贡献文档要求

当你打算贡献某部分的内容时，你应该尽量熟悉以下三部分：

- 文档存储的格式
- 文档的合理性
- remark-lint 和 $\rm{\LaTeX}$ 公式的格式要求

#### 文档引用与存储的格式

- <a id="SAVE-1"></a>SAVE-1：**文件名请务必都小写，以 `-` 分割．** 例如：`file-name.md`．
- <a id="SAVE-2"></a>SAVE-2：请务必确保文档中引用的 **外链** 图片已经全部转存到了 **本库内** 对应的 `images` 文件夹中（防止触发某些网站的防盗链），建议处理成 `MD 文档名称 + 编号` 的形式（可参考已有文档中图片的处理方式）．例如：本篇文档的文件名称为 format，则文档中引用的第一张图片的名字为 `format1.png`．
- <a id="SAVE-3"></a>SAVE-3：推荐使用 SVG 格式的图片[^ref4]，以获取较好的清晰度和缩放效果．由于 **OI Wiki** 各组件对 SVG 标准的兼容性不同，所以您的图片应基于 [SVG 1.1](http://www.w3.org/TR/SVG11/) 标准．
- <a id="SAVE-4"></a>SAVE-4：动图如果无法或者不会制作 SVG 格式的，则推荐使用 APNG 格式[^apng]的文件．Windows 用户可使用 [ScreenToGif](https://www.screentogif.com) 录制，Linux 用户可使用 [Peek](https://github.com/phw/peek) 录制，注意需要在设置里调整为录制 APNG．其他情况则推荐先制作为 MP4 等视频文件再转换为 APNG，如果使用 ffmpeg 则可以使用 `ffmpeg -i filename.mp4 -f apng filename.apng -plays 0` 转换．[^intro-apng]
- <a id="SAVE-5"></a>SAVE-5：同时具有源文件和导出图像的图片（例如 JPG 文件与 PSD 文件或者 SVG 图像与 TikZ TeX 源代码），建议将源文件以与图片相同的文件名保存于同一目录下．
- <a id="SAVE-6"></a>SAVE-6：请确保您的文档中的引用链接的稳定性．**不推荐** 引用 **自建** 服务中的资源（如自建 OJ 里的题目）．建议在添加时同时将该外链存于互联网档案馆[^webarchive]，以防无法替代的链接失效．
- <a id="SAVE-7"></a>SAVE-7：站内链接请去掉网站域名，并且使用相对路径链接对应 `.md` 文件．例如，在本页面（`intro/format`）中链接杂项简介（`misc`），应使用 `[杂项简介](../misc/index.md)`．可以在链接中添加 hash 来链接到某一节，例如 [`[Pull Request 信息格式规范](./contrib.md#pull-request-信息格式规范)`](./contrib.md#pull-request-信息格式规范)，hash 的值可以通过位于每个标题右侧的按钮或者位于网页右侧的目录中的链接得到．

#### 文档的合理性

**合理性**，指所编写的 **内容** 必须具有如下的特性：

- <a id="STRC-1"></a>STRC-1：由浅入深，内容的难度应该具有渐进性．
- <a id="STRC-2"></a>STRC-2：逻辑性．

  - <a id="STRC-2.1"></a>STRC-2.1：对于算法或数学概念类内容的撰写应该尽量包含以下的内容：

    1. 原理：说明该内容对应的原理；
    2. 例子：给出 1 \~ 2 个典型的例子；
    3. 题目：在该标题下，**只需要给出题目名字和题目链接**．对于算法类题目，题目链接 OJ 的优先级为：原 OJ（国外 OJ 要求国内可流畅访问）> UOJ > LOJ > 洛谷．

    示例页面：[IDA\*](../search/idastar.md)
  - <a id="STRC-2.2"></a>STRC-2.2：对于工具类内容的撰写应该尽量包含以下的内容：

    1. 简介：阐明该工具的背景与用途．
    2. 配置方式：详细给出配置环境与使用的过程，下载与安装方法建议尽量引用官方文档．

    示例页面：[WSL (Windows 10)](../tools/wsl.md)

除现有内容质量较低的情况外，建议尽量从 **补充** 的角度来做贡献，而非采取直接覆盖的方式．如果拿不准主意，可以参考 [关于本项目的交流方式](./discuss.md) 一节，与 **OI Wiki** 项目组联系．

#### 文档的基本格式要求

##### Remark-lint 的格式要求

[remark-lint](https://github.com/remarkjs/remark-lint) 可以自动给项目内文件统一风格．**OI Wiki** 现在启用的配置文件托管在 [.remarkrc](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc)．

在配置过程中 **OI Wiki** 项目组也遇到了一些 remark-lint 不能很好处理的问题，所以请严格按照下列要求编辑文档：

- <a id="LINT-1"></a>LINT-1：不要使用如 `<h1>` 或者 `# 标题` 的一级标题．
- <a id="LINT-2"></a>LINT-2：标题要空一个英文半角空格，例如：`## 简介`．
- <a id="LINT-3"></a>LINT-3：由于 remark-lint 不能很好地处理删除线，因此请不要使用删除线语法（不使用删除线语法的另外一个原因是，删除线划去的内容大多为「抖机灵」性质，对读者理解帮助不大，不符合下面的「文本内容的格式要求」中 [对内容表述的要求](#CONT-5)）．
- <a id="LINT-4"></a>LINT-4：列表：

  - <a id="LINT-4.1"></a>LINT-4.1：列表前要有空行，新开一段．
  - <a id="LINT-4.2"></a>LINT-4.2：使用有序列表（如 `1. 例子`）时，点号后要有空格．
- <a id="LINT-5"></a>LINT-5：行间公式前后各要有一行空行，否则会被当做是行内公式．
- <a id="LINT-6"></a>LINT-6：使用 `???` 或 `!!!` 开头的 Details 语法时，每一行要包括在 Details 语法的文本框的文本，开头必须至少有 4 个空格．

  **即使是空行，也必须保持与其他行一致的缩进．请不要使用编辑器的自动裁剪行末空格功能．**

  ???+ success "示例"
  下面的代码中用 `␣` 表示空格 ．

  ``text ???+ warning ␣␣␣␣请记得在文本前面添加 4 个空格．其他的语法还是与 Markdown 语法一致． ␣␣␣␣ ␣␣␣␣不添加 4 个空格的话，文本就不会出现在 Details 文本框里了． ␣␣␣␣ ␣␣␣␣这个`???`是什么的问题会在 [下文](#MDFM-5) 解答． ``

  ???+ warning "Warning"
  请记得在文本前面添加 4 个空格．其他的语法还是与 Markdown 语法一致．

  不添加 4 个空格的话，文本就不会出现在 Details 文本框里了．

  这个 `???` 是什么的问题会在 [下文](#MDFM-5) 解答．
- <a id="LINT-7"></a>LINT-7：代码样式的纯文本块请使用 ` ```text`．直接使用 ` ``` ` 而不指定纯文本块里的语言，可能会导致内容被错误地缩进．

##### 标点符号的使用

- <a id="PUNC-1"></a>PUNC-1：请在每句话的末尾添加 **句号**．

<!-- scripts.linter.postprocess.fix_full_stop off -->

- <a id="PUNC-2"></a>PUNC-2：请正确使用 **全角** 标点符号与 **半角** 标点符号．汉语请使用全角符号，英语请使用半角符号．中文中夹用英文时，请参考 [中文出版物夹用英文的编辑规范](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html)．特别地，请用全角句点「．」替代中文句号「。」．

<!-- scripts.linter.postprocess.fix_full_stop on -->

<!-- scripts.linter.postprocess.fix_quotation off -->

- <a id="PUNC-3"></a>PUNC-3：由于 `“……”` 和 `‘……’` 未区分全半角，请使用 `「……」` 作为全角双引号，`"..."` 作为半角双引号，`『……』` 作为全角单引号，`'...'` 作为半角单引号．

<!-- scripts.linter.postprocess.fix_quotation on -->

- <a id="PUNC-4"></a>PUNC-4：注意区分 **顿号** 与 **逗号** 的使用．
- <a id="PUNC-5"></a>PUNC-5：注意 **括号** 的位置．句内括号与句外括号的位置不同．
- <a id="PUNC-6"></a>PUNC-6：通常使用 **分号** 来表示列表环境中各复句之间的关系．
- <a id="PUNC-7"></a>PUNC-7：对于有序列表，推荐在每一项的后面添加 **分号**，在列表最后一项的后面添加 **句号**；对于无序列表，推荐在每一项的后面添加 **句号**．
- <a id="PUNC-8"></a>PUNC-8：注意区分各种不同的连接号，如 hyphen（一般使用 U+002D hyphen-minus（-），即键盘上的「减号」代替），U+2013 en dash（–）和 U+2014 em dash（—）．（英文中连接多个人名时，须用 en dash，但是极常误用为 hyphen．其他误用较为罕见，基本上只需记住这一点即可．）详见 [连接号 - 维基百科](https://zh.wikipedia.org/wiki/%E8%BF%9E%E6%8E%A5%E5%8F%B7)．

  ???+ success "示例"
  -   中学生学科竞赛主要包括信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛和信息学奥林匹克竞赛（谁写的这个示例，建议抬走）．
  -   「你吃了吗？」李四问张三．
  -   我想对你说：「我真是太喜欢你了．」
  -   「苟利国家生死以，岂因祸福避趋之！」
  -   张华考上了大学；李萍进了技校；我当了工人：我们都有美好的前途．[^note1]
  -   以下是这个算法的基本流程：
  1.  初始化到各点的距离为无穷大，将所有点设置为未被访问过，初始化一个队列；
  2.  将起点放入队列，将起点设置为已被访问过，更新到起点的距离为 $0$；
  3.  取出队首元素，将该元素设置为未被访问过；
  4.  遍历所有与此元素相连的边，若到这个点存在更短的距离，则进行松弛操作；
  5.  若这个点未被访问过，则将这个点放入队列，且设置这个点为已经访问过；
  6.  回到第三步，直到队列为空．
  -   KMP 算法（Knuth–Morris–Pratt algorithm, KMP algorithm）由 Knuth、Pratt 和 Morris 在 1977 年共同发布．[^note2]

##### Markdown 格式与主题扩展格式要求

- <a id="MDFM-1"></a>MDFM-1：表示强调时请使用 `**SOMETHING**` 和 `「」`，而非某级标题，因为使用标题会导致文章结构层次混乱和（或）目录出现问题．
- <a id="MDFM-2"></a>MDFM-2：当需要引用题目链接时，应尽可能使用原 OJ 题库中的链接而不是镜像链接．
- <a id="MDFM-3"></a>MDFM-3：请正确使用 Markdown 的区块功能．插入行内代码请使用一对反引号包围代码区块；行间代码请使用一对 ` ``` ` 包围代码区块，其中反引号就是键盘左上角波浪线下面那个符号，行间代码请在第一个 ` ``` ` 的后面加上语言名称（如：` ```cpp`）．

  ???+ success "示例"
  ``text ```cpp // #include<stdio.h>    //不好的写法 #include <cstdio>  //好的写法 ``` ``

  ``cpp // #include<stdio.h>    //不好的写法 #include <cstdio>  //好的写法 ``
- <a id="MDFM-4"></a>MDFM-4：「参考资料与注释」使用 Markdown 的脚注功能进行编写．格式为：

  ```markdown
  文本内容．[^脚注名]
  [^脚注名]: 参考资料内容．注意：冒号是英文冒号，冒号后面跟着一个空格．
  ```

  脚注名既可以使用数字也可以使用文本．脚注名摆放的位置与括号的用法一致．为美观起见，建议同一个页面内的脚注名遵循统一的命名规律，如：ref1、ref2、note1……

  脚注的内容统一放在 `## 参考资料与注释` 二级标题下．

  ???+ success "示例"
  ```markdown
  当 `#include <cxxxx>` 可以替代 `#include <xxxx.h>` 时，应使用前者．[^ref1]

  2020年1月21日，CCF宣布恢复NOIP．[^ref2]

##### 参考资料与注释

  [^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)

  ```

  当 `#include <cxxxx>` 可以替代 `#include <xxxx.h>` 时，应使用前者．[^ref1]

  2020 年 1 月 21 日，CCF 宣布恢复 NOIP．[^ref2]
- <a id="MDFM-5"></a>MDFM-5：建议使用主题扩展的 `???+note` 格式（即 [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks)）来描述题面和参考代码．也可以用这种格式来展示其他需要补充介绍的内容．

  示例代码（下面的代码中用 `␣` 表示空格 ）：

  ```text
  ??? note "标题"
  ␣␣␣␣这个文本框会被默认折叠．
  ␣␣␣␣
  ␣␣␣␣推荐将 **解题代码** 放在折叠文本框内．

  ???+note "[HDOJ 的「A + B Problem」](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
  ␣␣␣␣标题也可以使用 Markdown 的超链接．这里的超链接是 HDOJ 的「A + B Problem」．
  ␣␣␣␣
  ␣␣␣␣而且推荐以这种方式**标注原题链接**．
  ␣␣␣␣
  ␣␣␣␣注意双引号的位置．
  ```

  效果：

  ??? note "标题"
  这个文本框会被默认折叠．

  推荐将 **解题代码** 放在折叠文本框内．

  ???+ note "[HDOJ 的「A + B Problem」](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
  标题也可以使用 Markdown 的超链接．这里的超链接是 HDOJ 的「A + B Problem」．

  而且推荐以这种方式 **标注原题链接**．

  注意双引号的位置．

  两种格式的区别是，带 `+` 的会默认保持展开，而不带 `+` 的会默认保持折叠．

  折叠框的标题，即 `???+note` 中 `note` 后的内容应以 `"` 包裹起来．其中的内容支持 Markdown 语法．详见 [Admonition - Changing the title](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#changing-the-title)．（不具备折叠功能的为一般的 Admonitions，参考 [Admonitions - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions)）
- <a id="MDFM-6"></a>MDFM-6：当需要添加不同语言的代码时，推荐使用 Content tabs，可以实现不同语言代码的切换．Content tabs 还有其他的用法，详见 [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage)．其使用方法和效果如下．

  ???+ success "示例"
  注意需要在文本前面添加 4 个空格（下面用 `␣` 表示）．其他的语法还是与 Markdown 语法一致．

  ````text
  === "C"
  ␣␣␣␣``c ␣␣␣␣#include <stdio.h> ␣␣␣␣ ␣␣␣␣int main(void) { ␣␣␣␣  printf("Hello world!\n"); ␣␣␣␣  return 0; ␣␣␣␣} ␣␣␣␣``

  === "C++"
  ␣␣␣␣``cpp ␣␣␣␣#include <iostream> ␣␣␣␣ ␣␣␣␣int main(void) { ␣␣␣␣  std::cout << "Hello world!" << std::endl; ␣␣␣␣  return 0; ␣␣␣␣} ␣␣␣␣``
  ````

  === "C"
  ```c
  #include <stdio.h>

  int main(void) {
  printf("Hello world!\n");
  return 0;
  }
  ```

  === "C++"
  ```cpp
  #include <iostream></iostream>

  int main(void) {
  std::cout << "Hello world!" << std::endl;
  return 0;
  }
  ```

如果对 mkdocs-material（我们使用的这个主题）还有什么问题，还可以查阅 [MkDocs 使用说明](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)，其介绍了 mkdocs-material 主题的插件使用方式．

##### 文本内容的格式要求

- <a id="CONT-1"></a>CONT-1：所有的 **OI Wiki** 文本都应使用粗体标记．
- <a id="CONT-2"></a>CONT-2：在页面的开头应有一段简短的文字（如「本页面将介绍……」），用于概述页面内容．

  ???+ success "示例"
  本页面将列出在 **OI Wiki** 编写过程时推荐使用的格式规范与编辑方针．
- <a id="CONT-3"></a>CONT-3：涉及到「前置知识」的页面，请在开头添加一行 **前置知识：……**，放在页面概述前．格式如下：

  `前置知识：[站内页面1](url1)、[站内页面2](url2)和[站内页面3](url3)`

  ???+ success "示例"
  前置知识：[时间复杂度](../basic/complexity.md)

  本页面将介绍基础的计算理论的知识．
- <a id="CONT-4"></a>CONT-4：请注意文档结构．文档结构应当十分条理，层次清晰．请不要让诸如「五级标题」这种事情再次发生了，一篇正常的文章是用不到如此复杂的结构层次的．
- <a id="CONT-5"></a>CONT-5：请注意内容的表述．作为一个百科网站，**OI Wiki** 使用的语言应该是书面的，客观的．诸如「抖机灵」性质的，对读者理解帮助不大的内容，不应该出现在 **OI Wiki** 当中．
- <a id="CONT-6"></a>CONT-6：请尽量为链接提供完整的标题、或者可被识别的提示，避免使用裸地址和「这」、「此」之类的模糊不清的描述．每一个超链接都应尽量对其加以清楚明确的描述，方便读者明白该超链接将指向何处．

  建议使用源文章或者标签页的标题．

  ???+ failure "不推荐的写法"
  ```markdown
  请参考[这个页面](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

  请参考 [https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
  ```

  请参考 [这个页面](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

  请参考 [https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

  ???+ success "推荐的写法"
  ``markdown 请参考 GitHub 官方的帮助页面 [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) ``

  请参考 GitHub 官方的帮助页面 [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
- <a id="CONT-7"></a>CONT-7：受 Markdown 格式限制，`## 参考资料与注释` 二级标题必须放在文末．
- <a id="CONT-8"></a>CONT-8：所有用作序号的数字建议使用中文．示例：

  - 数列的第一项．
  - 输入文件的第一行．
- <a id="CONT-9"></a>CONT-9：请尽量避免在标题中使用 MathJax 公式，无论是几级标题．在标题中使用公式有可能会导致目录显示错误．[^ref3]

##### LaTeX 公式的格式要求

LaTeX 作为公式排版的首选，我们应当正确地使用它．因此对于 LaTeX 的使用我们有严格的要求．如果您想要快速上手，可以阅读本章节末给出的表格．

- <a id="MATH-1.1"></a>MATH-1.1：您使用的符号不应与 [数学符号表](./symbols.md) 规定的符号冲突．
- <a id="MATH-1.2"></a>MATH-1.2：使用 Roman 体表示数字、常量、算子和函数．使用 Italic 体表示变量、下标．LaTeX 已经预先定义好了一些常见的常量、函数、运算符等，我们可以直接调用，包括但不限于：

  ```latex
  \log, \ln, \lg, \sin, \cos, \tan, \sec, \csc, \cot, \gcd, \min, \max, \exp, \inf, \mod, \bmod, \pmod
  ```

  所以在输入常量、函数名、运算符等时，请先检查一下是否应该使用 Roman 体或其它字体．LaTeX 符号的书写可参考 [KaTeX 的 Supported Functions 页面](https://katex.org/docs/supported.html)（不是全部），也可以搜索求解, 或询问 AI 工具．

  由于 LaTeX 书写 Roman 体小写希腊字母较为困难，故小写希腊字母常量、算子和函数可以使用 Italic 体，如 $\pi$ 以及 $\delta x$ 中的 $\delta$.

  如果遇到没有预先定义好的需要使用 Roman 体的 **函数名**，我们可以使用 `$\operatorname{something}$` 来产生，如我们可以使用 `$\operatorname{lcm}$` 产生正体的最小公倍数（函数）符号．同理，产生 Roman 体的 **常量** 应用 `$\mathrm{}$`；产生 Roman 体粗体符号应用 `$\mathbf{}$`；产生 Italic 体粗体符号应用 `$\boldsymbol{}$`（如向量 $\boldsymbol{a}$）．对于多字母的变量，应当使用 `$\textit{}$`．其他非数学内容，包括英文、特殊符号等，一律使用 `$\text{}$`．中文我们则建议不放在 LaTeX 公式中．
- <a id="MATH-1.3"></a>MATH-1.3：如果表达式须折行（常见于较长的行间公式中），则应遵循如下换行规则：

  - <a id="MATH-1.3.1"></a>MATH-1.3.1：将换行符放在 $=$，$+$，$-$，$\pm$，$\mp$ 之前，如果有必要，也可放在 $\times$，$\cdot$，$/$ 之前，如：

    $$
    \begin{aligned}
        \mathrm{e}^x &= \sum\limits_{n=0}^{\infty} \frac{x^n}{n!} \\
        &= \phantom{+} 1 + x + \frac{x^2}{2} \\
        & \phantom{=} + \frac{x^3}{6} + \frac{x^4}{24} + \dots \\
    \end{aligned}
    $$
  - <a id="MATH-1.3.2"></a>MATH-1.3.2：同一运算符不应在换行符前后同时出现，
  - <a id="MATH-1.3.3"></a>MATH-1.3.3：换行符尽量不要出现在括号内的表达式中．
- <a id="MATH-1.4"></a>MATH-1.4：在行内使用分数的时候，请使用 `$\dfrac{}{}$`．比如 `$\dfrac{1}{2}$`，效果 $\dfrac{1}{2}$，而不是 `$\frac{1}{2}$`，效果 $\frac{1}{2}$．
- <a id="MATH-1.5"></a>MATH-1.5：组合数请使用 `\dbinom{n}{m}`，效果 $\dbinom{n}{m}$，而不是 `{n \choose m}`（在 LaTeX 中这种写法已不推荐）；与上一条关于分数的约定相似，请不要使用 `\binom{n}{m}`，效果 $\binom{n}{m}$．
- <a id="MATH-1.6"></a>MATH-1.6：尽可能避免在行内使用巨运算符（如 $\sum$，$\prod$，$\int$ 等）．
- <a id="MATH-1.7"></a>MATH-1.7：在不会引起歧义的情况下，请用 `$\times$` 代替星号，叉乘请使用 `$\times$`，点乘请使用 `$\cdot$`．如 $a\times b$，$a\cdot b$，而不是 $a\ast b$．
- <a id="MATH-1.8"></a>MATH-1.8：请用 `$\cdots$`（居于排版基线与顶线中间），`$\ldots$`（居于排版基线的位置），`$\vdots$`（竖着的省略号）代替 `$...$`．如 $a_1,a_2,\cdots a_n$，而不是 $a_1,a_2,... a_n$．
- <a id="MATH-1.9"></a>MATH-1.9：请注意，不要在非代码区域使用任何程序设计语言的表示方式，而是使用 LaTeX 公式．例如，使用 `$=$` 而不是 `$==$`（如 $a=b$，而不是 $a==b$）、使用 `` `a<<1` `` 或者 `$a\times 2$` 而不是 `$a<<1$`、使用 `$a\bmod b$` 代替 `$a\%b$`（如 $a\bmod b$，而不是 $a\%b$）等．
- <a id="MATH-1.10"></a>MATH-1.10：公式中不要使用中括号连缀（即 C++ 高维数组的表示方式）而多使用下标．即 $a_{i,j,k}$ 而不是 $a[i][j][k]$．在公式中下标较复杂的情况下建议改用多元函数（$f(i,j,k)$）或内联代码格式．对于一元简单函数使用 `$f_i$`、`$f(i)$` 或 `$f[i]$` 均可．
- <a id="MATH-1.11"></a>MATH-1.11：为了统一且书写方便，复杂度分析时大 $O$ 记号请直接使用 `$O()$` 而不是 `$\mathcal O()$`．
- <a id="MATH-1.12"></a>MATH-1.12：在表示等价关系时，请使用 `$\iff$`，效果 $\iff$，而不是 `$\Leftrightarrow$`，效果 $\Leftrightarrow$．
- <a id="MATH-1.13"></a>MATH-1.13：分段函数环境 `cases`  **只能有两列**（即一个 `&` 分隔符）．
- <a id="MATH-1.14"></a>MATH-1.14：请不要滥用 LaTeX 公式．这不仅会造成页面加载缓慢（因为 MathJax 的效率低是出了名的），同时也会导致页面的排版混乱．我们通常使用 LaTeX 公式字体表示变量名称．我们的建议是，如非必要，尽量减少公式与普通正文字体的 **大量** 混合使用，如非必要，尽量不要使用公式，如：

  ```LaTeX
  我们将要学习 $Network-flow$ 中的 $SPFA$ 最小费用流，需要使用 $Edmonds–Karp$ 算法进行增广．
  ```

  就是一个典型的 **滥用公式字体** 的例子．（在页面中使用斜体请用 `*文本*` 表示．）
- <a id="MATH-1.15"></a>MATH-1.15：请正确使用对应的 LaTeX 符号，尤其是公式中的希腊字母等特殊符号．如欧拉函数请使用 `$\varphi$`，圆的直径请使用 `$\Phi$`，黄金分割请使用 `$\phi$`．这些符号虽然同样表示希腊字母 Phi，但是在不同的环境下有不同的含义．切记 **不要使用输入法的插入特殊符号** 来插入这种符号．

  另外，由于 LaTeX 历史原因，空集的符号应为 `$\varnothing$` 而不是 `$\emptyset$`；其他的符号应参照 [数学符号表](./symbols.md) 书写．

我们可以使用一个表格来总结一下上述内容．注意本表格没有举出所有符号的用法，只给出常见的错误．类似的情况类比即可．

| 不符合规定的用法                       | 渲染效果               | 符合规定的用法                             | 渲染效果                                       |
| -------------------------------------- | ---------------------- | ------------------------------------------ | ---------------------------------------------- |
| `$log, ln, lg$`                      | $log, ln, lg$        | `$\log$, $\ln$, $\lg$`                   | $\log$，$\ln$，$\lg$                     |
| `$sin, cos, tan$`                    | $sin, cos, tan$      | `$\sin$, $\cos$, $\tan$`                 | $\sin$，$\cos$，$\tan$                   |
| `$gcd, lcm$`                         | $gcd, lcm$           | `$\gcd$, $\operatorname{lcm}$`           | $\gcd$，$\operatorname{lcm}$               |
| `$e$, $\text{e}$, e`（自然对数的底） | $e$，$\text{e}$, e | `$\mathrm{e}$`                           | $\mathrm{e}$                                 |
| `$i$, $\text{i}$, i`（虚数单位）     | $i$，$\text{i}$, i | `$\mathrm{i}$`                           | $\mathrm{i}$                                 |
| `$ 小于 a 的质数 $`                  | $小于 a 的质数$      | `小于 $a$ 的质数`                        | 小于$a$ 的质数                               |
| `$...$`                              | $...$                | `$\cdots$, $\ldots$, $\vdots$, $\ddots$` | $\cdots$，$\ldots$，$\vdots$，$\ddots$ |
| `$a*b$`（两个数相乘）                | $a*b$                | `$a\times b$, $a\cdot b$`                | $a\times b$，$a\cdot b$                    |
| `$SPFA$`（英文名称）                 | $SPFA$               | `SPFA`                                   | SPFA                                           |
| `$a==b$`                             | $a==b$               | `$a=b$`                                  | $a=b$                                        |
| `$f[i][j][k]$`                       | $f[i][j][k]$         | `$f_{i,j,k}$, $f(i,j,k)$`                | $f_{i,j,k}$，$f(i,j,k)$                    |
| `$R,N^*$`（集合）                    | $R,N^*$              | `$\mathbf{R}$, $\mathbf{N}^*$`           | $\mathbf{R}$，$\mathbf{N}^*$               |
| `$\emptyset$`                        | $\emptyset$          | `$\varnothing$`                          | $\varnothing$                                |
| `$size$`                             | $size$               | `$\textit{size}$`                        | $\textit{size}$                              |

##### 对数学公式的附加格式要求

请注意，尽管上述输入公式的语法和真正的 LaTeX 排版系统非常相似，但 **MathJax 和 LaTeX 是两个完全没有关系的东西**，MathJax 仅仅使用了一部分与 LaTeX 非常相似的语法而已．实际上，二者之间有不少细节差别，而这些差别经常导致写出来的公式在二者之间不通用．

考虑到 MathJax 和 LaTeX 之间的兼容性, **请各位在 Wiki 中书写数学公式时注意以下几点．**

这些规则已经向 MathJax 做了尽可能多的妥协．导出工具兼容了一部分原本仅能在 MathJax 中正常输出的写法．

- <a id="MATH-2.1"></a>MATH-2.1：请使用 `\begin{aligned} ... \end{aligned}` 表示多行对齐的公式；
- <a id="MATH-2.2"></a>MATH-2.2：如果这些多行对齐的公式需要 **编号**，请用 `align` 或 `equation` 环境；
- <a id="MATH-2.3"></a>MATH-2.3：不要使用 `split`、`eqnarray` 环境；
- <a id="MATH-2.4"></a>MATH-2.4：不要使用 `\lt`,`\gt` 来表示大于号和小于号，请直接使用 `<`，`>`；
- <a id="MATH-2.5"></a>MATH-2.5：不要直接用 `\\` 换行（需要换行的公式，请套在 `aligned` 或其他多行环境下）；
- <a id="MATH-2.6"></a>MATH-2.6：若要输出 LaTeX 符号 $\rm{\LaTeX}$，请用 `$\rm{\LaTeX}$`，而不是 `mathrm`；（`\LaTeX` 在 TeX 排版系统中是一个不能用于数学模式下的命令，而 `\mathrm` 又不能在普通模式下使用；另外，`\text` 命令虽然在 TeX 上正常输出，但是在 MathJax 中 `\text` 命令的参数会被原样输出，而不是按命令转义）；
- <a id="MATH-2.7"></a>MATH-2.7：数学公式中的中文文字 **必须置于 `\text{}` 命令之中**，而变量、数字、运算符、函数名称则必须置于 `\text{}` 命令之外．**请不要在 `\text{}` 命令中嵌套数学公式**；
- <a id="MATH-2.8"></a>MATH-2.8：使用 `array` 环境时请注意 **实际列数与对齐符号的数量保持一致**．例如下面的公式中，数据实际有 3 列（`&` 是列分隔符），因此需要 3 个对齐符号（`l`/`r`/`c` 分别表示左、右、居中对齐）．

  ```latex
  $$
  \begin{array}{lll}
  F_1=\{\frac{0}{1},&&\frac{1}{1}\}\\
  F_2=\{\frac{0}{1},&\frac{1}{2},&\frac{1}{1}\}\\
  \end{array}
  $$
  ```


### 外部链接

- [标点符号用法（GB/T 15834—2011）](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201001/W020190128580990138234.pdf)
- [维基百科：格式手册/标点符号](https://zh.wikipedia.org/wiki/Wikipedia:%E6%A0%BC%E5%BC%8F%E6%89%8B%E5%86%8C/%E6%A0%87%E7%82%B9%E7%AC%A6%E5%8F%B7)
- [中文文案排版指北（简体中文版）](https://mazhuang.org/wiki/chinese-copywriting-guidelines/)
- [中文文案风格指南 - PDFE GUIDELINE](https://pdfe.github.io/GUIDELINE/#/others/copywriter)
- [一份（不太）简短的 LATEX2ε 介绍或 106 分钟了解 LATEX2ε](https://github.com/CTeX-org/lshort-zh-cn/releases)
- [中文出版物夹用英文的编辑规范](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html)

### 参考资料与注释

[^ref2]: [CCF关于恢复NOIP竞赛的公告-中国计算机学会](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)
    
[^note1]: （冒号）表示总结上文．
    
[^note2]: 科学技术名称的英文全称与其缩略形式间，应使用英文逗号．中文句子内夹用了用以注释、补充或说明的英文句子或语段，该英文句子或语段用中文圆括号标示．
    
[^note3]: 折叠框：参见 [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks)，有时我们也用「Details 语法」指代该语法，因其从功能上与 HTML 中的 [`<details>` 元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) 功能一致．
    
[^note4]: 移至 [如何贡献](./contrib.md)．
    
[^note5]: 该规范写入了 [编辑前须知](../edit-landing.md) 并发布了公告，并未写入本文档．
    
[^note6]: 选项卡：参见 [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs)．
    
[^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)
    
[^ref2]: [CCF 关于恢复 NOIP 竞赛的公告 - 中国计算机学会](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)
    
[^ref3]: [我的公式为什么在目录里没有正常显示？好像双倍了](../faq.md)
    
[^ref4]: [SVG|MDN](https://developer.mozilla.org/zh-CN/docs/Web/SVG)
    
[^webarchive]: [Save Page in Internet Archive](https://web.archive.org/save/)
    
[^apng]: [APNG](https://en.wikipedia.org/wiki/APNG)
    
[^intro-apng]: [OI-wiki/OI-wiki#3422](https://github.com/OI-wiki/OI-wiki/issues/3422)
