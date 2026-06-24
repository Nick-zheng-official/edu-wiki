import re
import markdown
from xml.etree import ElementTree as etree

class BilibiliExtension(markdown.extensions.Extension):

    def extendMarkdown(self, md):
        pattern = r'!bilibili\[([A-Za-z0-9]+)\]'
        processor = BilibiliProcessor(pattern, md)
        md.inlinePatterns.register(processor, 'bilibili', 175)

class BilibiliProcessor(markdown.inlinepatterns.InlineProcessor):
    def handleMatch(self, match, data):
        bvid = match.group(1)
        iframe = etree.Element('iframe')
        iframe.set('src', f'//player.bilibili.com/player.html?bvid={bvid}&page=1')
        iframe.set('scrolling', 'no')
        iframe.set('border', '0')
        iframe.set('frameborder', 'no')
        iframe.set('framespacing', '0')
        iframe.set('allowfullscreen', 'true')
        iframe.set('style', 'width:100%;height:500px;margin:0 auto;display:block;')
        return iframe, match.start(0), match.end(0)

def makeExtension():
    return BilibiliExtension()
