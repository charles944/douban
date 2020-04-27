import re
import requests
from Auto.Settings import *
import json
import sys

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

    # 判断账号是否登陆成功。如果成功，返回uid；如果密码错误，就提示密码错误；如果没有是其他情况，就重试5次，不行就换号。
    # 不对，账号登陆的第一步实际上只有三种状态：登陆成功、需要过滑块验证、连接超时。
    # 如果是过滑块验证，那么通过验证后又有两种状态：密码正确或者密码错误。
    # 如果是链接超时，那访问5遍，还是不行的话，就放弃这个ip
    # 算了，把滑动验证码过掉，现在直接来写三种情况：登陆成功；出现滑动验证码，说明密码错误；连接超时，重新连接5次
    def signIn(self):
        s = requests.Session()
        # 任何网络访问都必须考虑到网络不好的情况，所以必须先把网络不好这种异常给捕获了
        resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
        print(resq_1)
        # if resq_1==<Response [200]> :
        sign_datas=json.loads(sign_data%(self.username,self.password))
        resq_2 = s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_datas, headers=SIGNIN_HEADERS,
                        verify=False)
        # 这里要加上换IP和过验证码的功能
        # print(resq_2.text)
        uid = re.search('id":"(.*?)"', resq_2.text)
        count_recursion=0
        if uid.group(1):
            # 如果成功获取UID，则登陆成功
            uid=uid.group(1)
            return uid
        elif re.search("需要图形验证码",resq_2.text):
            # 如果出现“需要图形验证码”，则密码错误
            return "密码错误"
        else:
            print("连接超时，再连4次")
            if count_recursion<4:
                self.signIn()
            else:
                sys.exit(0)
            # 这里需要函数调用自身，就是需要函数的递归调用吧，翻翻教材去

if __name__ == '__main__':
    # s = requests.Session()
    # resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
    # print(resq_1)
    account=Account("15000950339","weippp5551994526")
    account.signIn()