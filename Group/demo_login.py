import requests
import json
from lxml import html

HEADERS = {
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36';
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3761.400 QQBrowser/10.6.4116.400',
}
sign_data='{"ck":"","name":"%s","password":"%s","remenber":"false","ticket":""}'
SIGNIN_HEADERS={
    'Host': 'accounts.douban.com',
    'Connection': 'keep-alive',
    # 'Content-Length: 69',
    'Accept': 'application/json',
    'Origin': 'https://accounts.douban.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

s=requests.Session()
resp_1=s.get("https://www.douban.com",headers=HEADERS)
sign_datas=json.loads(sign_data % ("1339456879@qq.com","weippp5551994526"))
resp_2=s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_datas, headers=SIGNIN_HEADERS,)
# print(resp_2.text)
resp_3=s.get("https://www.douban.com/group/blabla/",headers=HEADERS)
# print(resp_3.text)
etree=html.etree
HTML=etree.HTML(resp_3.text)
check=HTML.xpath("//div[@class='group-misc']/a/span/text()")[0]
print(check)

resp_4=s.get("https://www.douban.com/group/pudongzufang/",headers=HEADERS)
# print(resp_3.text)
etree=html.etree
HTML=etree.HTML(resp_4.text)
check=HTML.xpath("//div[@class='group-misc']/a/span/text()")[0]
print(check)
# resp=requests.get("https://www.douban.com",headers=HEADERS)
# print(resp.status_code)
