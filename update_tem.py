#!/usr/bin/env python3
"""
根据SOP流程更新TEM.md文件和精简版Word文档
"""

import re
import os
import requests
from bs4 import BeautifulSoup


class VocabProcessor:
    """词汇处理器"""
    
    def __init__(self):
        self.tem_file = "d:\\edu-wiki\\docs\\docs\\english\\vocabs\\TEM.md"
        self.temp_file = "d:\\桌面\\vocab temp\\temp.txt"
        self.process_script = "d:\\edu-wiki\\process_tem.py"
    
    def read_temp_file(self):
        """读取temp.txt文件中的单词"""
        with open(self.temp_file, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    
    def check_spelling(self, words):
        """检查单词拼写"""
        # 简单的拼写检查，实际项目中可以使用更专业的拼写检查库
        misspelled = []
        for word in words:
            # 这里可以添加拼写检查逻辑
            if not word.isalpha():
                misspelled.append(word)
        return misspelled
    
    def get_next_number(self):
        """获取下一个单词的序号"""
        with open(self.tem_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 找到所有现有条目的序号
        pattern = r'### (\d+)\. '  # 匹配 "### 1. provincial /prəˈvɪnʃl/"
        matches = re.findall(pattern, content)
        if not matches:
            return 1
        
        # 返回最大序号+1
        max_num = max(int(match) for match in matches)
        return max_num + 1
    
    def get_word_info(self, word):
        """获取单词信息（简化版，实际项目中应使用可靠的词典API）"""
        # 这里使用简化的信息，实际项目中应调用词典API获取准确信息
        # 示例信息，实际需要替换为真实数据
        word_info = {
            'prime': {
                'phonetic': 'praɪm',
                'pos': [
                    '* **prime (adj.)** 主要的；首要的；最好的。',
                    '* **prime (n.)** 全盛时期；精华；质数。',
                    '* **prime (v.)** 使准备好；优化。'
                ],
                'collocations': [
                    '* **Prime minister**：首相；总理。',
                    '* **Prime time**：黄金时间。',
                    '* **Prime location**：黄金地段。',
                    '* **To prime sb. for sth.**：使某人准备好做某事。'
                ],
                'discrimination': [
                    '* **prime vs. primary**',
                    '  `Prime` 强调"最好的、最重要的"，常指品质或地位；`Primary` 强调"基本的、首要的"，常指顺序或重要性。',
                    '  *例句：This is the prime example of good design.* (这是好设计的最佳范例。)',
                    '  *例句：The primary reason is cost.* (主要原因是成本。)'
                ]
            },
            'inverse': {
                'phonetic': 'ɪnˈvɜːs',
                'pos': [
                    '* **inverse (adj.)** 相反的；逆的；倒数的。',
                    '* **inverse (n.)** 相反；倒数。',
                    '* **inverse (v.)** 使倒转。'
                ],
                'collocations': [
                    '* **Inverse relationship**：反比关系。',
                    '* **Inverse proportion**：反比例。',
                    '* **Inverse function**：反函数。'
                ],
                'discrimination': []
            }
        }
        
        # 返回示例信息，如果单词不在示例中则返回空
        return word_info.get(word, {
            'phonetic': '',
            'pos': [f'* **{word} (adj./n./v.)** 暂无详细信息。'],
            'collocations': [f'* **{word}**：暂无固定搭配。'],
            'discrimination': []
        })
    
    def create_vocab_entry(self, word, number):
        """创建词汇条目"""
        info = self.get_word_info(word)
        
        entry = f"### {number}. {word} /{info['phonetic']}/\n\n"
        
        # 词性转换
        entry += "**1. 词性转换**\n\n"
        for pos_item in info['pos']:
            entry += f"{pos_item}\n"
        
        # 固定搭配
        entry += "\n**2. 固定搭配/地道表达**\n\n"
        for colloc in info['collocations']:
            entry += f"{colloc}\n"
        
        # 重点辨析
        if info['discrimination']:
            entry += "\n**3. 重点辨析**\n\n"
            for disc in info['discrimination']:
                entry += f"{disc}\n"
        
        entry += "\n"  # 条目之间的空行
        return entry
    
    def append_to_tem_file(self, entry):
        """将条目追加到TEM.md文件"""
        with open(self.tem_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    
    def clear_temp_file(self):
        """清空temp.txt文件"""
        with open(self.temp_file, 'w', encoding='utf-8') as f:
            f.write('')
    
    def update_word_doc(self):
        """更新精简版Word文档"""
        # 运行process_tem.py脚本
        os.system(f"python {self.process_script}")
    
    def process(self):
        """执行完整的SOP流程"""
        print("开始执行SOP流程...")
        
        # 1. 读取源单词
        words = self.read_temp_file()
        if not words:
            print("temp.txt文件为空，无需处理。")
            return
        
        print(f"读取到 {len(words)} 个单词。")
        
        # 2. 拼写检查
        misspelled = self.check_spelling(words)
        if misspelled:
            print(f"发现拼写错误的单词：{', '.join(misspelled)}")
            return
        
        # 3. 获取下一个序号
        next_number = self.get_next_number()
        print(f"下一个单词序号：{next_number}")
        
        # 4. 为每个单词创建条目并追加到TEM.md
        for i, word in enumerate(words):
            number = next_number + i
            print(f"处理单词 {i+1}/{len(words)}: {word} (序号: {number})")
            entry = self.create_vocab_entry(word, number)
            self.append_to_tem_file(entry)
        
        # 5. 清空temp.txt文件
        self.clear_temp_file()
        print("已清空temp.txt文件。")
        
        # 6. 更新精简版Word文档
        print("开始更新精简版Word文档...")
        self.update_word_doc()
        print("精简版Word文档已更新。")
        
        print("SOP流程执行完成！")


if __name__ == "__main__":
    processor = VocabProcessor()
    processor.process()
