import os
import re

# 定义要替换的数学函数列表
math_functions = ['lg', 'ln', 'log', 'sin', 'cos', 'tan', 'cot']

# 创建正则表达式模式，匹配前面没有反斜杠的数学函数
# 匹配前面可以是空白字符、数字、标点符号或行首的情况，确保我们只匹配独立的数学函数名
pattern = re.compile(r'(?<!\\)(?<![a-zA-Z])(' + '|'.join(math_functions) + r')(?![a-zA-Z])')

# 找到所有.md文件
md_files = []
for root, dirs, files in os.walk('d:\\edu-wiki'):
    # 排除 node_modules 目录
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    for file in files:
        if file.endswith('.md'):
            md_files.append(os.path.join(root, file))

print(f'找到 {len(md_files)} 个 .md 文件')

# 处理每个文件
modified_count = 0
for file_path in md_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 执行替换
        new_content = pattern.sub(r'\\\1', content)
        
        # 只有当内容发生变化时才写入
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'修改: {file_path}')
            modified_count += 1
    except Exception as e:
        print(f'处理文件失败 {file_path}: {e}')

print(f'完成！共修改了 {modified_count} 个文件')
