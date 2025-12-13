import markdown

# 测试默认配置
text = "这是第一行  \n这是第二行"
html = markdown.markdown(text)
print("默认配置:")
print(html)
print()

# 测试启用 hard_wrap
html = markdown.markdown(text, extensions=[], extension_configs={})
print("无扩展:")
print(html)
print()

# 测试使用 extra 扩展
html = markdown.markdown(text, extensions=['extra'])
print("使用 extra 扩展:")
print(html)

# 测试使用 breaks 扩展
html = markdown.markdown(text, extensions=['markdown.extensions.breaks'])
print("使用 breaks 扩展:")
print(html)
