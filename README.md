# EDU Wiki

![](./docs/static/img/logo.png){ width=128px }

欢迎来到 EDU Wiki！

[![Stars](https://img.shields.io/github/stars/Nick-zheng-official/edu-wiki?style=for-the-badge&color=black&label=Stars&logo=github&logoColor=white)](https://github.com/Nick-zheng-official/edu-wiki/stargazers)

[![Site](https://img.shields.io/website?style=for-the-badge&url=https://edu-wiki.pages.dev/&label=Site)](https://edu-wiki.pages.dev/)

[![QQ](https://img.shields.io/badge/QQ%E7%BE%A4-2181927847-blue?style=for-the-badge&logo=tencent-qq&logoColor=white)](https://qm.qq.com/q/2181927847)

## 关于我们

随着越来越多的教育资源被公开, 我们开始思考是否有一种方式, 能够将这些资源汇总起来, 形成一个统一的平台, 以便于学生学习, 并方便学生在任何地方任何时间进行复习。

因此，**EDU Wiki** 被创建了。

**EDU Wiki** 致力于成为高中文化课知识的一个免费开放的开源知识整合站点. 我们为大家准备了高中范围内特定学科的基础知识, 常见题型, 解题思路等内容, 希望可以帮助大家更快速深入地学习这些学科. 

目前, **EDU Wiki** 已整合了高中语文, 数学, 生物, 物理, 化学的知识. 其余学科的知识正在编写中. 你可以使用顶部导航栏选择学科, 在左侧边栏浏览具体章节, 从右侧目录中跳转到具体知识点. 你也可以使用上方搜索功能查找特定内容. 

请 **注意** , **EDU Wiki** 中不提供任何由 AI 生成的文章, 段落或语句. 我们将致力于避免 AIGC 对知识质量的影响, 严格监控文章的质量, 并在必要时进行调整. 我们也欢迎任何关于知识质量的反馈, 并会及时处理.

目前, **EDU Wiki** 处于 **试运行** 阶段, 请 **谨慎** 对待其中的内容。 在 **EDU Wiki** 完成第一轮迭代后, 我们会将 **EDU Wiki** 正式上线。当然, 在此过程中, 我们也会不断更新 **Wiki** 协作系统, 以便更好的维护与更新. 

**请注意** , **试运行** 阶段, **Wiki** 内容由本人学习笔记改编, 其内容与技巧基于 [@一数](https://space.bilibili.com/14229967), [@HuangFuRen](https://space.bilibili.com/23630128), [@学过石油的语文老师](https://space.bilibili.com/39737405) , [@一化儿](https://space.bilibili.com/1526560679) , [@一生儿](https://space.bilibili.com/2036187097) 的免费优质的公开课程, 排名不分先后, 按照 UID 大小排序, 请谨慎对待 Wiki 中的内容。

**EDU Wiki** 还有许多内容没有完善, 例如评论系统, **Docker** 部署, 更方便的 **PR** 预览, 以及许多空白页面等. 未来, 我们也会提供个性化功能, 帮助你免费创建独属于你自己的, 独特的 **Wiki** 网站, 用于记笔记及分享自己的学习动态. 我们期待有更多小伙伴加入我们的项目, 一起完善 **EDU Wiki** !

此外，鉴于以下两点

- 教育资源应该以开放的方式分享
- 解题技巧在快速迭代更新，在面对新的题目时，旧的技巧也随时可能失效

**EDU Wiki** 将永久免费开源开放且持续更新. **EDU Wiki** 源于社区，作为**独立的组织**，提倡**知识自由**，因此在未来也绝不会商业化, 亦 **不会** 出版任何 **书籍** ，将始终保持**独立自由**的性质。

换言之, 如果你在市面上发现所谓 "**EDU Wiki** 文章全收录" 等书籍, 一定 **非** **EDU Wiki** 官方出版. 

在阅读 **EDU Wiki** 之前，我们希望能给予你几点建议：

- 学习 [提问的智慧](http://www.catb.org/~esr/faqs/smart-questions.html) .
- 善用 AI 与浏览器搜索能帮助你更好地提升自己. 
- 结合优质课程使用, 不论校内还是线上免费课程. 
- 动手练习比什么都要管用. 
- 保持对芝士的好奇与渴望并坚持下去. 芝士, 与你分享(>_<)!

## 部署

本项目目前采用 [mkdocs](https://github.com/mkdocs/mkdocs) 部署在 [https://edu-wiki.pages.dev/](https://edu-wiki.pages.dev/).

 本项目可以直接部署在本地, 具体方式如下:

```bash
# 克隆仓库
git clone https://github.com/Nick-zheng-official/edu-wiki.git
cd edu-wiki

# 安装依赖
pip install -r requirements.txt

# 启动本地预览
mkdocs serve
```

启动后访问 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 即可查看网站。mkdocs 本地部署的网站是动态更新的，即当你修改并保存 md 文件后，刷新页面就能随之动态更新。

## 贡献指南

我们非常欢迎你为 **EDU Wiki** 编写内容，将自己的所学所得与大家分享。我们期待着你的加入！

在你决定要贡献内容之前，请你务必看完 [贡献指南](https://edu-wiki.pages.dev/home/contrib/contrib/)。其中包含了详细的贡献方式。

非常感谢一起完善 **EDU Wiki** 的小伙伴们: 

![Contributors](https://edu-wiki.pages.dev/static/img/contributors.png)

## 许可证

[![知识共享许可协议](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

除特别注明外, 项目中除代码部分外均采用[(Creative Commons BY-SA 4.0)知识共享署名-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-sa/4.0/)进行许可。

换言之，使用过程中您可以自由地共享、演绎，但是必须署名、以相同方式共享。

如果你想要引用这个 **Github** 仓库, 可以使用如下的 **bibtex** :

```bibtex
@misc{eduwiki,
  author = {EDU Wiki Team},
  title = {EDU Wiki},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/Nick-zheng-official/edu-wiki}},
}
```

## 鸣谢

本项目受 [CTF Wiki](https://github.com/ctf-wiki/ctf-wiki) 与 [OI Wiki](https://github.com/OI-wiki/OI-wiki/) 的启发，在编写过程中参考了诸多资料，在此一并致谢。

非常感谢一起完善 EDU Wiki 的 小伙伴们！

![](https://github.com/Nick-zheng-official/edu-wiki/blob/main/docs/static/img/contributors.png)

特别感谢 [@一数](https://space.bilibili.com/14229967), [@HuangFuRen](https://space.bilibili.com/23630128), [@学过石油的语文老师](https://space.bilibili.com/39737405) , [@一化儿](https://space.bilibili.com/1526560679) , [@一生儿](https://space.bilibili.com/2036187097) 老师在 Bilibili 平台上优质的课程, 本网站引用了部分视频截图及方法技巧. 排名不分先后, 按照 UID 大小排序. 注意, 不建议直接通过本网站学习, 而是建议学生在学习时, 参考 Bilibili 上的视频, 结合本网站的内容, 以获得更好的学习效果。
