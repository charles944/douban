import requests
import json

# cookie='ll="108088"; bid=z6iyTKjIRjE; _pk_ses.100001.8cb4=*; __utma=30149280.1782810489.1592363338.1592363338.1592363338.1; __utmc=30149280; __utmz=30149280.1592363338.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2="63880601:Ucoprdim0Nc"; ck=7D_G; _pk_id.100001.8cb4=b7c62ca65e6678ff.1592363335.1.1592363477.1592363335.; ap_v=0,6.0; __yadk_uid=4N4xw8uYrNDTNpp7do68BdLkH0K506Ba; push_noty_num=0; push_doumail_num=0; __utmv=30149280.6388; __utmb=30149280.3.10.1592363338'
cookie='ll="108088"; bid=z6iyTKjIRjE; __utma=30149280.1782810489.1592363338.1592363338.1592363338.1; __utmc=30149280; __utmz=30149280.1592363338.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2="63880601:Ucoprdim0Nc"; ck=7D_G; ap_v=0,6.0; __yadk_uid=4N4xw8uYrNDTNpp7do68BdLkH0K506Ba; push_noty_num=0; push_doumail_num=0; __utmv=30149280.6388; __gads=ID=1293dca59012bcf8:T=1592363958:S=ALNI_MbW6EO_mIrpjgV11xUXHdOxQ3-cfw; douban-profile-remind=1; _pk_id.100001.8cb4=b7c62ca65e6678ff.1592363335.1.1592364056.1592363335.'
HEADERS={
    'Host': 'www.douban.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Cookie':cookie,
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
sign_data='{"ck":"U-Sp","name":"%s","password":"%s","remenber":"false","ticket":""}'
HEADERS_2={
    'Host': 'www.douban.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
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
URL_HOST="https://www.douban.com/"
s=requests.session()
resp=s.get(URL_HOST,headers=HEADERS)
# print(resp.status_code)
# resp_2=s.get('https://www.douban.com/group/blabla/',headers=HEADERS_2,)
# print(resp_2.status_code)
sign_datas = json.loads(sign_data % ("1339456879@qq.com", "weippp5551994526"))
resp_2 = s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_datas, headers=SIGNIN_HEADERS)
print(resp_2.status_code)
print(resp_2.text)
# resp_3=s.get('https://www.douban.com/group/blabla/',headers=HEADERS_2)
# print(resp_3.text)