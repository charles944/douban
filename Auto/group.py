
import requests
from Auto.Settings import *
from lxml import etree

class Group(object):
    def __init__(self,username,password,nickname):
        self.username=username
        self.password=password
        self.nickname=nickname

    def getGroups(username,nickname):
        url=URL_HOST+nickname
        resq=requests.get(url,headers=HEADERS)
        HTML=etree.HTML(resq.text)
        group_titles=HTML.xpath("")
        group_urls=HTML.xpath("")
        number_groups=HTML.xpath("")
        return (number_groups,group_titles,group_urls)

    def jiaruGroups(name_groups,url_groups,words,nickname):
        for i in len(name_groups):
            resq=requests.get