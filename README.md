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
