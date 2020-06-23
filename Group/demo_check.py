import pymysql
import requests
from lxml import html
import json
import random
import time

db=pymysql.connect(host='localhost',user='root',password='1994526succeed',port=3306,db="douban")
cursor=db.cursor()
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
sql_init='select * from xiaozu where id="%d"'
sql_update='update xiaozu set check="%d" where url="%s"'

def update(group):
    sql=sql_update%(group[5],group[3])
    cursor.execute(sql)
    db.commit()

def getCheck(url,s):
    resq=s.get(url,headers=HEADERS)
    etree=html.etree
    HTML=etree.HTML(resq.text)
    check=HTML.xpath("//div[@class='group-misc']/a/span/text()")[0]
    # if check=='申请加入小组':
    #     return 1
    # elif check=='加入小组':
    #     return 0
    # else:
    #     return -1
    # # -1表示这个小组我正在申请中,但是出现这个也表示这个小组是需要审核的啊
    if check=='加入小组':
        return 0
    else:
        return 1

if __name__ == '__main__':
    s = requests.Session()
    resp_1 = s.get("https://www.douban.com", headers=HEADERS)
    sign_datas = json.loads(sign_data % ("1339456879@qq.com", "weippp5551994526"))
    resp_2 = s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_datas, headers=SIGNIN_HEADERS, )
    for x in range(5776):
        sql=sql_init%(x+1)
        cursor.execute(sql)
        group=cursor.fetchone()
        group[5]=getCheck(group[3],s)
        update(group)
        time.sleep(random.randint(1000, 5000) / 1000)