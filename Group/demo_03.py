
import requests
from lxml import etree
import re

HEADERS = {
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
resq=requests.get("https://www.douban.com/group/lacai/",headers=HEADERS)
resq=resq.text
resq_re=re.findall("置顶",resq)
print(len(resq_re))