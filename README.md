<div align="center">

<a href="https://edu-wiki.pages.dev/" target="_blank"><img src="docs/docs/static/img/logo.png" width="128" height="128"></a>

# Edu-Wiki

<p align="center">

高中知识，自由共享。

[![](https://img.shields.io/github/stars/Nick-zheng-official/edu-wiki?style=for-the-badge&color=black&label=Stars&logo=github&logoColor=white)](https://github.com/Nick-zheng-official/edu-wiki/stargazers) [![](https://img.shields.io/github/actions/workflow/status/Nick-zheng-official/edu-wiki/cloudflare-pages.yml?style=for-the-badge&branch=master&label=Build)](https://github.com/Nick-zheng-official/edu-wiki/actions) [![](https://img.shields.io/website?style=for-the-badge&url=https://edu-wiki.pages.dev/&label=Site)](https://edu-wiki.pages.dev/)

</p>

</div>

## 内容

高中学习任务繁重，知识点多且杂，网上资料大都零散琐碎，同学们往往不知道该如何系统地整理和复习各科知识。

为了方便高中生更好地学习和复习，**Edu-Wiki** 诞生了。这是一个基于 MkDocs 的高中知识维基百科，致力于整理和分享高中各科知识点，帮助大家更高效地学习。

目前，**Edu-Wiki** 涵盖以下学科：

- 语文
- 数学
- 英语
- 物理
- 化学
- 生物

**Edu-Wiki** 源于社区，提倡**知识自由**，在未来也绝不会商业化，将始终保持独立自由的性质。

---

## 部署

本项目采用 [MkDocs](https://github.com/mkdocs/mkdocs) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主题，部署在 [Cloudflare Pages](https://edu-wiki.pages.dev/)。

### 本地预览

```bash
# 1. clone
git clone https://github.com/Nick-zheng-official/edu-wiki.git
cd edu-wiki

# 2. 安装依赖
pip install -r requirements.txt

# 3. 本地预览，访问 http://127.0.0.1:8000/
python -m mkdocs serve -f docs/mkdocs.yml
```

**mkdocs 本地部署的网站是动态更新的，即当你修改并保存 md 文件后，刷新页面就能随之动态更新。**

### 构建静态文件

```bash
python -m mkdocs build -f docs/mkdocs.yml
```

构建后的静态文件会生成在 `docs/site` 目录。

---

## 如何参与完善 Edu-Wiki

我们非常欢迎你为 **Edu-Wiki** 编写内容，将自己的所学所得与大家分享。

### 添加新文档

1. 在对应学科目录下创建 Markdown 文件（如 `docs/docs/physics/optics.md`）
2. 图片文件放到对应学科的 `images/` 文件夹中
3. 在 `docs/mkdocs.yml` 中添加导航配置
4. 本地测试构建无误后提交

### 修改现有文档

1. 直接修改对应的 Markdown 文件
2. 本地测试构建
3. 提交代码到 GitHub

> 文件夹和 Markdown 文件请使用英文命名

---

## 配置说明

| 文件                   | 说明                                        |
| ---------------------- | ------------------------------------------- |
| `docs/mkdocs.yml`    | MkDocs 主配置文件（主题、导航、插件、扩展） |
| `requirements.txt`   | Python 依赖                                 |
| `.github/workflows/` | GitHub Actions 自动部署到 Cloudflare Pages  |

---

## 版权声明

`<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />``</a><br />`本作品采用`<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh">`知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议 (CC BY-NC-SA 4.0)`</a>`进行许可。

换言之，使用过程中您可以自由地共享、演绎，但是必须署名、以相同方式共享，且不得用于商业目的。

---

## 鸣谢

本项目受 [OI Wiki](https://oi-wiki.org/) 和 [CTF Wiki](https://ctf-wiki.org/) 的启发，在编写过程中参考了诸多资料，在此一并致谢。


<div align="center">

<a href="https://ctf-wiki.org/static/img/logo.png" target="_blank"><img src="https://ctf-wiki.org/static/img/logo.png" width="128" height="128"></a>

# CTF Wiki

<p align="center">

Come and join us, we need you!

[![](https://img.shields.io/discord/1115906685450596435?style=for-the-badge&color=%237289DA&label=Discord&logo=discord&logoColor=white")](https://discord.gg/ekv7WDa9pq)  [![](https://img.shields.io/github/stars/CTF-Wiki/CTF-Wiki?style=for-the-badge&color=black&label=Stars&logo=github&logoColor=white")](https://github.com/CTF-Wiki/CTF-Wiki/stargazers)

</p>

</div>

## Introduction

[中文](./README-zh_CN.md)  [English](./README.md)

欢迎来到 **CTF Wiki**。

**CTF**（Capture The Flag，夺旗赛）起源于 1996 年 **DEFCON** 全球黑客大会，是网络安全爱好者之间的竞技游戏。

**CTF** 竞赛涉及众多领域，内容繁杂。与此同时，安全技术的发展速度越来越快，**CTF** 题目的难度越来越高，初学者面对的门槛越来越高。而网上资料大都零散琐碎，初学者往往并不知道该如何系统性地学习 **CTF** 相关领域的知识，常需要花费大量时间，苦不堪言。

为了使得热爱 **CTF** 的小伙伴们更好地入门 **CTF**，2016 年 10 月份，**CTF Wiki** 在 Github 有了第一次 commit。随着内容不断完善，**CTF Wiki** 受到了越来越多安全爱好者的喜爱，也渐渐有素未谋面的小伙伴们参与其中。 

作为一个自由的站点，围绕 **CTF** 近几年赛题，**CTF Wiki** 对 **CTF** 中的各个方向的知识进行介绍，以便于初学者更好地学习 **CTF** 相关的知识。

目前，**CTF Wiki** 主要包含 **CTF** 各大方向的基础知识，正在着力完善以下内容

- CTF 竞赛中的进阶知识
- CTF 竞赛中的优质题目

关于上述部分待完善内容，请参见 CTF Wiki 的 [Projects](https://github.com/ctf-wiki/ctf-wiki/projects)，详细列举了正在做的事情以及待做事项。

虽然 **CTF Wiki** 基于 **CTF**，却不会局限于 **CTF**。在未来，**CTF Wiki** 将会

- 介绍安全研究中的工具
- 更多地与安全实战结合

此外，鉴于以下两点

- 技术应该以开放的方式分享
- 安全攻防技术在快速迭代更新，在面对新的防御技术时，旧的攻击技术随时可能失效

因此，**CTF Wiki** 永远不会出版书籍。

最后，**CTF Wiki** 源于社区，作为**独立的组织**，提倡**知识自由**，在未来也绝不会商业化，将始终保持**独立自由**的性质。

## How to build？

本文档目前采用 [mkdocs](https://github.com/mkdocs/mkdocs) 部署在 [https://ctf-wiki.org](https://ctf-wiki.org)。

本项目可以直接部署在本地，具体方式如下：

```shell
# 1. clone
git clone https://github.com/ctf-wiki/ctf-wiki.git
# 2. requirements
pip install -r requirements.txt
# generate static file in site/
python3 scripts/docs.py build-all
# deploy at http://127.0.0.1:8008
python3 scripts/docs.py serve
```

**mkdocs 本地部署的网站是动态更新的，即当你修改并保存 md 文件后，刷新页面就能随之动态更新。**


你只是想本地浏览，并不想修改文档？试试 Docker 吧！

```
docker run -d --name=ctf-wiki -p 4100:80 ctfwiki/ctf-wiki
```
随后即可在浏览器中访问 [http://localhost:4100/](http://localhost:4100/) 阅读 CTF Wiki 。

## How to practice？

首先，通过在线阅读来学习一些基本的安全知识。

其次，CTF Wiki 还有两个姊妹项目

- CTF Wiki 中涉及的题目在 [ctf-challenges](https://github.com/ctf-wiki/ctf-challenges) 仓库中，请根据对应的分类自行寻找。
- CTF Wiki 中涉及的工具会不断补充到 [ctf-tools](https://github.com/ctf-wiki/ctf-tools) 仓库中。

## How to make CTF Wiki Better？

我们非常欢迎你为 Wiki 编写内容，将自己的所学所得与大家分享。我们期待着你的加入！

**在你决定要贡献内容之前，请你务必看完 [CONTRIBUTING](https://ctf-wiki.org/en/contribute/before-contributing/)**。其中包含了详细的贡献方式。 

非常感谢一起完善 CTF Wiki 的小伙伴们

<a href="https://github.com/ctf-wiki/ctf-wiki/graphs/contributors"><img src="https://contrib.rocks/image?repo=ctf-wiki/ctf-wiki" /></a>

## What can you get?

- 快速学习新事物的能力
- 不一样的思考方式
- 乐于解决问题的心
- 有趣的安全技术
- 充实奋斗的时光

在阅读 Wiki 之前，我们希望能给予你几点建议：

- 学习 [提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)
- 善用 Google 搜索能帮助你更好地提升自己
- 至少掌握一门编程语言，比如 Python
- 动手实践比什么都要管用
- 保持对技术的好奇与渴望并坚持下去

> 世界很大，互联网让世界变小，真的黑客们应该去思考并创造，无论当下是在破坏还是在创造，记住，未来，那条主线是创造的就对了。 ——by 余弦

安全圈很小，安全的海洋很深。安全之路的探险，不如就从 **CTF Wiki** 开始！

## Copyleft
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

