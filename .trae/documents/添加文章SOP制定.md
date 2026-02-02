# 添加文章标准操作程序 (SOP)

## 1. 将中文名的md文件及文件夹改为对应的英文名

### 1.1 操作目的
将所有中文命名的文件夹和md文件转换为英文命名，保持项目结构的一致性和规范性。

### 1.2 操作步骤

#### 1.2.1 查看当前文件夹结构
```bash
# 使用PowerShell命令查看当前文档结构
Get-ChildItem -Path "D:/edu-wiki/docs/docs" -Recurse
```

#### 1.2.2 制定命名规则
- 学科文件夹保持不变（已为英文）
- 子文件夹：使用清晰、简洁的英文名称，如"导数" → "calculus"
- md文件：使用小写字母、连字符分隔，如"极值点偏移.md" → "extreme-point-offset.md"

#### 1.2.3 重命名文件夹
```powershell
# 使用Rename-Item命令重命名文件夹
Rename-Item -Path "原路径" -NewName "新名称"
```

#### 1.2.4 重命名md文件
```powershell
# 使用Rename-Item命令重命名md文件
Rename-Item -Path "原文件名.md" -NewName "新文件名.md"
```

### 1.3 注意事项
- 保持命名的一致性和可读性
- 确保文件名与文件内容相符
- 记录所有重命名操作，便于后续配置文件更新

## 2. 修改配置文件

### 2.1 操作目的
更新mkdocs.yml配置文件，确保导航路径与新的文件夹和文件名一致。

### 2.2 操作步骤

#### 2.2.1 查看当前配置文件
```bash
# 使用cat命令查看当前配置文件
cat "D:/edu-wiki/docs/mkdocs.yml"
```

#### 2.2.2 更新导航配置
- 打开mkdocs.yml文件
- 更新所有导航条目，将中文路径替换为英文路径
- 保持导航结构的逻辑性和层级关系

#### 2.2.3 添加新文件到导航
- 在对应学科下添加新文件的导航条目
- 确保导航条目名称与文件标题一致

### 2.3 注意事项
- 检查所有路径的正确性
- 保持导航结构的清晰性
- 确保所有md文件都已添加到导航中

## 3. 处理图片文件

### 3.1 操作目的
将桌面学科文件夹中的图片复制到项目对应的images文件夹，并清空桌面文件夹。

### 3.2 操作步骤

#### 3.2.1 复制图片到项目
```powershell
# 使用Copy-Item命令复制图片
Copy-Item -Path "D:/桌面/化学/*" -Destination "D:/edu-wiki/docs/docs/chemistry/images/"
Copy-Item -Path "D:/桌面/生物/*" -Destination "D:/edu-wiki/docs/docs/biology/images/"
Copy-Item -Path "D:/桌面/数学/*" -Destination "D:/edu-wiki/docs/docs/math/images/"
Copy-Item -Path "D:/桌面/物理/*" -Destination "D:/edu-wiki/docs/docs/physics/images/"
```

#### 3.2.2 验证图片复制
```powershell
# 检查目标文件夹中的图片
Get-ChildItem -Path "D:/edu-wiki/docs/docs/*/images/"
```

#### 3.2.3 清空桌面文件夹
```powershell
# 使用Remove-Item命令清空桌面文件夹
Remove-Item -Path "D:/桌面/化学/*" -Recurse -Force
Remove-Item -Path "D:/桌面/生物/*" -Recurse -Force
Remove-Item -Path "D:/桌面/数学/*" -Recurse -Force
Remove-Item -Path "D:/桌面/物理/*" -Recurse -Force
```

### 3.3 注意事项
- 确保所有图片都已成功复制
- 检查图片文件名的正确性
- 验证图片路径在md文件中的引用是否正确

## 4. 验证与测试

### 4.1 构建文档
```bash
# 在docs目录下运行构建命令
cd D:/edu-wiki/docs
mkdocs build
```

### 4.2 检查构建结果
- 查看构建过程中是否有错误
- 检查生成的site目录结构
- 本地预览网站，确保所有页面都能正常访问

## 5. 总结

### 5.1 完成情况检查
- [ ] 所有中文文件夹和md文件已改为英文
- [ ] 配置文件已更新
- [ ] 所有图片已复制到项目images文件夹
- [ ] 桌面学科文件夹已清空
- [ ] 文档构建成功
- [ ] 网站预览正常

### 5.2 文档更新记录
- 记录添加的文章标题和路径
- 记录修改的配置内容
- 记录处理的图片数量

## 6. 最佳实践

### 6.1 命名规范
- 文件夹名：使用小写字母，单词间用连字符分隔
- 文件名：使用小写字母，单词间用连字符分隔，避免使用特殊字符
- 导航名称：使用中文，保持良好的可读性

### 6.2 配置文件管理
- 保持导航结构的清晰性和逻辑性
- 定期检查配置文件的正确性
- 确保所有md文件都已添加到导航中

### 6.3 图片管理
- 图片文件使用清晰、描述性的名称
- 图片文件大小控制在合理范围内
- 定期清理无用的图片文件

### 6.4 文档质量
- 保持文档内容的准确性和完整性
- 遵循Markdown语法规范
- 添加适当的标题和目录结构

## 7. 常见问题及解决方案

### 7.1 图片路径错误
- 检查md文件中的图片引用路径
- 确保图片已正确复制到对应的images文件夹

### 7.2 配置文件格式错误
- 检查YAML语法的正确性
- 确保缩进和格式符合要求

### 7.3 文档构建失败
- 检查md文件的语法错误
- 检查配置文件的正确性
- 检查文件路径的正确性

# 结束

以上就是添加文章的完整SOP，按照这个流程操作可以确保文章添加的规范性和正确性。