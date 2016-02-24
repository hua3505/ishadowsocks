import urllib
import urllib.request
from lxml import etree

def fetch():
    url = "http://www.ishadowsocks.com/"
    content = urllib.request.urlopen(url).read() 
    selector=etree.HTML(content)
    divs = selector.xpath('//div[@class="col-lg-4 text-center"]')

    result = [];
    for i in range(0, 4):
        text = divs[0][i].text
        text = text[text.find(':')+1:]
        result.append(text)
    return tuple(result)
