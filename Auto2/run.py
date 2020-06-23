import json
import threading
import requests
from Auto2.Account import *
from Auto2.Join import Join
from Auto2.Post import Post
from Auto2.Top import Top

def readjson(plan):
    # 1.账号登录；
    account=Account(plan["账号"]["username"],plan["账号"]["password"],plan["账号"]["cookie"])
    account.login()
    # 2.账号初始化
    account.init()
    # 3.执行加入小组任务；
    join=Join(plan["加入小组"],account)
    join.joingroup()
    # 4.执行发帖任务；
    post=Post(plan['发帖']['发帖小组'],plan['发帖']['发帖标题'],plan['发帖']['发帖内容'],account)
    post.send()
    # 5.执行顶贴任务
    top=Top(plan['顶贴']['顶贴帖子'],plan['顶贴']['顶贴内容'],plan['顶贴']['顶贴轮次'],account)
    top.sendtop()

if __name__ == '__main__':
    with open("demo_json.json",'r',encoding="utf-8") as f:
        content=f.read()
    resp=json.loads(content)
    for i in range(len(resp)):
        t=threading.Thread(target=readjson,name="thread_%d"%(i+1),args=(content["计划%d"%i],))
        t.start()