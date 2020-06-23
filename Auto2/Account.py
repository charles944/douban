import requests
from Auto2.settings import *
import json

class Account():
    def __init__(self,username,password,cookie):
        self.username=username
        self.password=password
        self.cookie=cookie
        self.s=requests.session()
        self.sign_datas=json.loads(sign_data%(self.username,self.password))

    # 账号登录
    def login(self):
        self.s.get(URL_HOST,headers=HEADERS)
        self.s.post("https://accounts.douban.com/j/mobile/login/basic", data=self.sign_datas, headers=SIGNIN_HEADERS)
        # 现在已经登录成功了

    # 账号初始化，更新账号信息和帖子信息
    def init(self):
        # 0.查看账号是否被封,如果被封，这个线程结束；否则继续。
        # 1.访问系统信息，查看被拒绝的小组，保存到数据库
        # 2.访问个人主页，查看已经成功加入的小组，保存到数据库。
        # 3.和数据库中申请加入小组记录和已加入小组记录对比，查看还没有通过审核的小组和已经移除的小组；
        # 4.查看已经发出的所有帖子，和数据库中已发出的帖子对比，查找到已经被删除的帖子；
        # 5.查看所有已经发出的顶贴，和数据库中已发出的顶贴对比，查找到已经被删除的顶贴
        pass