import re
import requests
from Auto.Settings import *

class Account(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        # self.nicknam=nickname
        # self.uid=uid

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

    def signIn(self):
        s = requests.Session()
        resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
        print(resq_1)
        # if resq_1==<Response [200]> :

        resq_2 = s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_data, headers=SIGNIN_HEADERS,
                        verify=False)
        # 这里要加上换IP和过验证码的功能
        # print(resq_2.text)
        uid = re.search('id":"(.*?)"', resq_2.text)
        uid = uid.group(1)
        # print(uid.group(1))

if __name__ == '__main__':
    s = requests.Session()
    resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
    print(resq_1)