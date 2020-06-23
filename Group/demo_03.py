
import requests
# from lxml import html
from lxml import etree
import re

HEADERS = {
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
# url_1='https://www.douban.com/group/18976/'
url_2='https://www.douban.com/group/blabla/'
resp=requests.get(url_2,headers=HEADERS)
# resq=resq.text
print(resp.status_code)
print(resp.text)
# resq_re=re.findall("置顶",resq)
# print(len(resq_re))
# etree=html.etree
HTML=etree.HTML(resp.text)
check=HTML.xpath("//a[contains(@class,'bn-join-group')]/span/text()")
print(type(check),len(check))
print(check)
# test=HTML.xpath("//a")
# print(len(test))
# print(test)