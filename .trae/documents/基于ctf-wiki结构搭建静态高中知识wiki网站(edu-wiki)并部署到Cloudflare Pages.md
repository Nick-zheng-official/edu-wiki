# 基于ctf-wiki结构搭建静态高中知识wiki网站(edu-wiki)并部署到Cloudflare Pages

## 1. 项目分析与目标

### 1.1 ctf-wiki结构分析
通过查看ctf-wiki的文件结构和配置，确认其核心技术栈：
- **静态站点生成器**：MkDocs
- **主题**：Material for MkDocs
- **配置文件**：`mkdocs.yml`（位于`docs/zh/`等语言目录下）
- **目录结构**：多语言支持，清晰的分类导航
- **插件**：search, minify等静态插件

### 1.2 项目目标
- 创建与ctf-wiki完全一致结构的高中知识wiki
- 保留静态功能，移除动态功能（留言/登录）
- 简化配置，专注于静态生成
- 部署到Cloudflare Pages

## 2. 项目初始化与配置

### 2.1 初始化项目
- 在`d:\edu-wiki`目录初始化MkDocs项目
- 安装核心依赖：
  ```
  mkdocs
  mkdocs-material
  mkdocs-minify-plugin
  ```
- 创建基础目录结构

### 2.2 配置文件设计
- 复制ctf-wiki的`mkdocs.yml`配置
- 移除不必要的动态配置
- 调整为高中知识相关的标题、描述和导航
- 保留核心插件：search, minify

## 3. 目录结构设计

### 3.1 核心目录结构
完全参考ctf-wiki的结构，调整为高中知识分类：
```
docs/
├── zh/                     # 中文版本
│   ├── docs/               # 文档内容
│   │   ├── index.md        # 首页
│   │   ├── 数学/           # 数学分类
│   │   │   ├── 代数.md
│   │   │   ├── 几何.md
│   │   │   └── ...
│   │   ├── 物理/           # 物理分类
│   │   ├── 化学/           # 化学分类
│   │   ├── 生物/           # 生物分类
│   │   ├── 语文/           # 语文分类
│   │   └── 英语/           # 英语分类
│   ├── static/             # 静态资源
│   │   ├── img/            # 图片
│   │   ├── css/            # 自定义CSS
│   │   └── js/             # 自定义JS
│   └── mkdocs.yml          # 中文配置
├── requirements.txt        # 依赖声明
└── .gitignore             # Git忽略配置
```

### 3.2 多语言支持（可选）
- 如需多语言，可参考ctf-wiki添加`en/`和`zh-tw/`目录
- 配置语言切换功能

## 4. 主题与样式定制

### 4.1 Material主题配置
- 复制ctf-wiki的Material主题配置
- 调整颜色方案（primary: white, accent: red）
- 配置logo和图标
- 启用核心功能：
  - navigation.tabs
  - navigation.tabs.sticky
  - search.suggest
  - search.highlight
  - search.share

### 4.2 自定义样式
- 复制ctf-wiki的自定义CSS和JS
- 调整为高中知识wiki的品牌元素
- 确保响应式设计正常工作

## 5. 内容创作与组织

### 5.1 内容结构规划
- 按高中学科分类组织内容
- 每个学科下按知识点细分
- 保持一致的Markdown格式
- 使用统一的标题层级

### 5.2 Markdown扩展支持
保留ctf-wiki使用的Markdown扩展：
- admonition
- codehilite
- toc
- pymdownx.arithmatex（数学公式）
- pymdownx.emoji（表情）
- pymdownx.superfences（代码块）
- 等

## 6. 本地开发与测试

### 6.1 本地开发环境
- 启动MkDocs开发服务器：`mkdocs serve -f docs/zh/mkdocs.yml`
- 访问本地预览：`http://localhost:8000`
- 实时查看修改效果

### 6.2 测试与验证
- 测试搜索功能
- 验证导航链接
- 检查响应式设计
- 确认Markdown扩展正常工作
- 测试静态生成：`mkdocs build -f docs/zh/mkdocs.yml`

## 7. 部署到Cloudflare Pages

### 7.1 Git仓库准备
- 初始化Git仓库
- 创建`.gitignore`文件
- 提交代码到GitHub

### 7.2 Cloudflare Pages配置
- 登录Cloudflare账号
- 创建新的Pages项目
- 连接GitHub仓库
- 配置构建命令：
  ```
  build command: mkdocs build -f docs/zh/mkdocs.yml
  build output directory: site
  ```
- 部署网站
- 配置自定义域名（可选）

## 8. 优化与简化

### 8.1 移除动态功能
- 确保不包含任何动态功能（留言/登录）
- 移除不必要的API调用和脚本
- 专注于静态内容生成

### 8.2 简化配置
- 移除不必要的插件和扩展
- 简化CI/CD配置（如需）
- 确保配置文件简洁明了

## 9. 维护与更新

### 9.1 内容更新流程
- 本地修改内容
- 测试预览
- 提交到Git仓库
- Cloudflare Pages自动部署

### 9.2 主题与插件更新
- 定期更新MkDocs和Material主题
- 测试兼容性
- 确保静态生成正常

## 实施步骤

1. 初始化MkDocs项目
2. 安装核心依赖
3. 创建目录结构
4. 配置mkdocs.yml文件
5. 复制ctf-wiki的主题和样式配置
6. 创建示例内容
7. 本地测试网站
8. 初始化Git仓库并推送到GitHub
9. 部署到Cloudflare Pages
10. 验证部署结果
11. 开始正式内容创作

这个计划将创建一个与ctf-wiki结构完全一致的静态高中知识wiki网站，专注于内容展示，去除动态功能，适合部署到Cloudflare Pages。