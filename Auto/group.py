
import requests
from Auto.Settings import *
from lxml import etree
import re
import time


def time_refuse(name_group):
    pass


def send_words():
    pass


print(time.time())

class Group(object):
    def __init__(self,s,uid):
        # self.username=username
        # self.password=password
        # self.nickname=nickname
        self.uid=uid
        self.s=s

    # 获取所有该账号已加入的小组
    def getGroups(s,uid):
        url='https://www.douban.com/group/people/%s/joins'%uid
        resq=s.get(url,headers=HEADERS)
        HTML=etree.HTML(resq.text)
        group_titles=HTML.xpath("//li/div[@class='info']/div/a/text()")
        group_urls=HTML.xpath("//li/div[@class='info']/div/a/@href")
        number_group=len(group_titles)
        return (group_titles,group_urls,number_group)

    # 申请加入小组
    def joinGroups(name_groups,url_groups,words,s,uid):
        # url='https://www.douban.com/group/596337/?action=join&ck=DGtU'
        for i in len(name_groups):
            name_group=name_groups[i]
            url_group=url_groups[i]
            resq=s.get(url_group+"?action=join&ck=DGtU",headers=HEADERS)
            now = int(time.time())  # 1533952277
            timeArray = time.localtime(now)
            otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
            if re.search("小组管理员需要验证你的身份，请输入你的请求信息",resq.text):
                print("该小组需要验证")
                send_words()
                state="已申请"
            elif re.search("",resq.text):
                print("该小组已申请过且被拒绝了")
                time=time_refuse(name_group)
                state="已被拒"
                return time
            else:
                print("该小组不需要验证")
                state="已加入"
            return (name_group, otherStyleTime, state)

    # 获取所有已拒绝的小组
    def refuseGroups(s,uid):
        refuseUrl=""
        resq=s.get(refuseUrl,headers=HEADERS)
        HTML=etree.HTML(resq.text)
        refuseGroup=HTML.xpath("")
        return refuseGroup

if __name__ == '__main__':
    pass