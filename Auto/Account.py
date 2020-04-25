import re

class Account(object):
    def __init__(self,username,password,nickname,uid):
        self.username=username
        self.password=password
        self.nicknam=nickname
        self.uid=uid

    # 获取已加入的小组
    def getGroups(self):
        pass

    # 从历史记录中获取已发的帖子
    def getPosts(self):
        pass

    # 获取账号的安全状态
    def state(self):
        pass

    # 获取账号收到的私信
    def getMassage(self):
        pass