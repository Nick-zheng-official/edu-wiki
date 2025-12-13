# Edu-Wiki

## 项目简介

Edu-Wiki 是一个基于 MkDocs 的高中知识维基百科，用于整理和分享高中各科知识点。

## 技术栈

- **构建工具**：MkDocs
- **主题**：Material for MkDocs
- **部署平台**：Cloudflare Pages
- **CI/CD**：GitHub Actions

## 目录结构

```
eduwiki/
├── docs/                      # 文档目录
│   ├── docs/                  # Markdown文档存放目录
│   │   ├── index.md           # 网站首页
│   │   ├── chinese/           # 语文学科
│   │   ├── math/              # 数学学科
│   │   ├── english/           # 英语学科
│   │   ├── physics/           # 物理学科
│   │   ├── chemistry/         # 化学学科
│   │   ├── biology/           # 生物学科
│   │   └── static/            # 静态资源
│   └── mkdocs.yml             # MkDocs配置文件
├── .github/                   # GitHub配置
│   └── workflows/             # GitHub Actions工作流
│       └── cloudflare-pages.yml # Cloudflare Pages部署配置
├── requirements.txt           # Python依赖
└── README.md                  # 项目说明
```

## 安装和使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 本地预览

```bash
python -m mkdocs serve -f docs/mkdocs.yml
```

访问 http://127.0.0.1:8000/ 查看网站。

### 3. 构建网站

```bash
python -m mkdocs build -f docs/mkdocs.yml
```

构建后的静态文件会生成在 `docs/site` 目录。

## 部署

### 1. 自动部署

项目配置了 GitHub Actions 自动部署，当代码推送到 `master` 分支时，会自动触发部署流程。

部署流程：
1. 检查代码仓库
2. 设置 Python 环境
3. 安装依赖
4. 构建网站
5. 部署到 Cloudflare Pages

### 2. 手动部署

将 `docs/site` 目录下的所有文件上传到静态网站托管服务即可。

## 贡献指南

### 1. 添加新文档

1. 在对应学科目录下创建 Markdown 文件
2. 在 `docs/mkdocs.yml` 中添加导航配置
3. 测试本地构建
4. 提交代码到 GitHub

### 2. 修改现有文档

1. 直接修改对应的 Markdown 文件
2. 测试本地构建
3. 提交代码到 GitHub

## 配置文件说明

### mkdocs.yml

主要配置项：
- `site_name`：网站名称
- `site_description`：网站描述
- `theme`：主题配置
- `nav`：导航配置
- `plugins`：插件配置
- `markdown_extensions`：Markdown 扩展配置

### cloudflare-pages.yml

GitHub Actions 部署配置，包含：
- 触发条件：推送代码到 `master` 分支
- 构建命令：`python -m mkdocs build -f docs/mkdocs.yml`
- 部署目录：`docs/site`

## 许可证

ISC
