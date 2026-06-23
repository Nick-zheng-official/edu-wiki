import re
import markdown

class BilibiliExtension(markdown.extensions.Extension):

    def extendMarkdown(self, md):
        pattern = r'!bilibili\[([A-Za-z0-9]+)\]'
        processor = BilibiliProcessor(md.registry)
        md.inlinePatterns.register(processor, 'bilibili', 175)

class BilibiliProcessor(markdown.inlinepatterns.Pattern):
    def handleMatch(self, match):
        bvid = match.group(1)
        iframe = f'''<iframe src="//player.bilibili.com/player.html?bvid={bvid}&page=1" 
                scrolling="no" border="0" frameborder="no" framespacing="0" 
                allowfullscreen="true" style="width:100%;height:500px;margin:0 auto;display:block;">
                </iframe>'''
        return markdown.html.StripTagProcessor().run(iframe)

def makeExtension():
    return BilibiliExtension()
