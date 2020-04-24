
import requests
from Auto.Settings import *
from lxml import etree
import re

class Group(object):
    def __init__(self,s,uid):
        # self.username=username
        # self.password=password
        # self.nickname=nickname
        self.uid=uid

    def getGroups(s,uid):
        url='https://www.douban.com/group/people/%s/joins'%uid
        resq=s.get(url,headers=HEADERS)
        HTML=etree.HTML(resq.text)
        group_titles=HTML.xpath("//li/div[@class='info']/div/a/text()")
        group_urls=HTML.xpath("//li/div[@class='info']/div/a/@href")
        number_group=len(group_titles)
        return (group_titles,group_urls,number_group)

    def jiaruGroups(name_groups,url_groups,words,s,uid):
        # url='https://www.douban.com/group/596337/?action=join&ck=DGtU'
        for i in len(name_groups):
            name_group=name_groups[i]
            url_group=url_groups[i]
            resq=s.get(url_group+"?action=join&ck=DGtU",headers=HEADERS)
            if re.search("小组管理员需要验证你的身份，请输入你的请求信息",resq.text):
                print("该小组需要验证")
            else:
                print("该小组不需要验证")