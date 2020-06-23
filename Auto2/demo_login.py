import requests

cookies='ll="108088"; bid=z6iyTKjIRjE; __utmz=30149280.1592363338.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __yadk_uid=4N4xw8uYrNDTNpp7do68BdLkH0K506Ba; push_noty_num=0; push_doumail_num=0; __utmv=30149280.6388; __gads=ID=1293dca59012bcf8:T=1592363958:S=ALNI_MbW6EO_mIrpjgV11xUXHdOxQ3-cfw; douban-profile-remind=1; _pk_ses.100001.8cb4=*; __utma=30149280.1782810489.1592363338.1592363338.1592369089.2; dbcl2="63880601:+h/vEQ8JLsU"; _pk_id.100001.8cb4=b7c62ca65e6678ff.1592363335.2.1592370246.1592364056.; __utmt=1; __utmb=30149280.8.10.1592369089'
HEADERS={
    'Host': 'www.douban.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Cookie':cookies,
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

s=requests.session()
resp_1=s.get("https://www.douban.com",headers=HEADERS)
# print(resp_1.status_code)
# print(resp_1.text)
resp_2=s.get("https://www.douban.com/gallery/topic/148562/?from=discussing",headers=HEADERS)
print(resp_2.status_code)
print(resp_2.text)
