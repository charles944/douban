import re
import requests
from Auto.Settings import *
import json
import sys
import time
from lxml import etree
import random
from Auto.utils import *

class Account(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        # self.nicknam=nickname
        # self.uid=uid

    def time_refuse(self):
        pass

    def send_words(self):
        pass

    # 判断是否被封号。等有了被封的账号再来写这个功能。
    def isClose(self):
        pass

    # 获取已加入的小组
    def getGroups(self):
        pass

    # 从历史记录中获取已发的帖子
    def getPosts(self):
        pass

    # 获取账号的安全状态
    def state(self):
        pass

    # 获取账号收到的系统信息和用户信息
    def getMassage(self):
        pass

    def getInfo(self):
        pass

    # 判断账号是否登陆成功。如果成功，返回uid；如果密码错误，就提示密码错误；如果没有是其他情况，就重试5次，不行就换号。
    # 不对，账号登陆的第一步实际上只有三种状态：登陆成功、需要过滑块验证、连接超时。
    # 如果是过滑块验证，那么通过验证后又有两种状态：密码正确或者密码错误。
    # 如果是链接超时，那访问5遍，还是不行的话，就放弃这个ip
    # 算了，把滑动验证码过掉，现在直接来写三种情况：登陆成功；出现滑动验证码，说明密码错误；连接超时，重新连接5次
    def signIn(self,count_recursion):
    # signIn()的参数count_recursion表示在网络不好的情况下，最多尝试的次数
        s = requests.Session()
        # 任何网络访问都必须考虑到网络不好的情况，所以必须先把网络不好这种异常给捕获了
        try:
            resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
        except:
            print("网络连接错误")
            sys.exit(0)
        else:
            print(resq_1)
            # if resq_1==<Response [200]> :
            sign_datas=json.loads(sign_data%(self.username,self.password))
            try:
                resq_2 = s.post("https://accounts.douban.com/j/mobile/login/basic", data=sign_datas, headers=SIGNIN_HEADERS,
                                verify=False)
            except:
                print("网络连接错误")
                sys.exit(0)
            else:
                # 这里要加上换IP和过验证码的功能
                # print(resq_2.text)
                uid = re.search('id":"(.*?)"', resq_2.text)
                count_recursion=0
                if uid.group(1):
                    # 如果成功获取UID，则登陆成功
                    uid=uid.group(1)
                    return (uid,s)
                elif re.search("需要图形验证码",resq_2.text):
                    # 如果出现“需要图形验证码”，则密码错误
                    return "密码错误"
                    sys.exit(0)
                else:
                    print("连接超时，再次连接")
                    if count_recursion>0:
                        # 递归调用本函数，调用次数就是在网络情况不好时访问网络的次数
                        return self.signIn(count_recursion-1)
                    else:
                        sys.exit(0)
                    # 这里需要函数调用自身，就是需要函数的递归调用吧，翻翻教材去



    def getGroups(s,uid):
        url='https://www.douban.com/group/people/%s/joins'%uid
        resq=s.get(url,headers=HEADERS)
        HTML=etree.HTML(resq.text)
        group_titles=HTML.xpath("//li/div[@class='info']/div/a/text()")
        group_urls=HTML.xpath("//li/div[@class='info']/div/a/@href")
        number_group=len(group_titles)
        return (group_titles,group_urls,number_group)

    # 申请加入小组
    def joinGroups(self, name_groups, url_groups, words, s, uid):
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
                self.send_words()
                state="已申请"
            elif re.search("",resq.text):
                print("该小组已申请过且被拒绝了")
                time=self.time_refuse(name_group)
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

    # 这个方法用于从该账号的所有已加入小组中选择一个最适合的小组来发帖
    # 先把demo写这里，后面再来补充详细写法。这里的返回值是一个元组
    def getGroup(self):
        group=("鹅组","https://www.douban.com/ezu")
        return group

    # 这个方法用于从json配置文件中随机选择一个作为发帖内容，这里返回值是一个字典
    def getContent(self):
        setUp=json.loads("setUp.json")
        content=setUp["发帖"][random.randint(0,len(setUp["发帖"])-1)]
        return content

    # 选取某个小组进行发帖
    def posting(self,s):
        # 第一步：选择合适的发帖小组
        get_group=self.getGroup()
        # 第二步：选择合适的发帖内容
        post_content=self.getContent()
        # 第三步：开始发帖，后面抓包了再来写


    # 获取已经发的帖子。
    # 从数据库的历史记录中获取，返回的是一个数组，数组的每个元素是帖子标题+url的二维元组
    def readyPosts(self,uid,s):
        post=("我是你爸爸，我真伟大","https://www.douban.com/921837")
        return post

    # 顶贴的方法
    # 问题1：该账号是只顶自己的帖子呢，还是其他账号的帖子也要顶呢？如何选择要顶的帖子呢？
    #     目前还是只顶自己的帖子吧，从自己以往发的帖子中随机选择一个帖子来
    # 问题2：顶贴的内容从哪儿来呢？
    #     从json文件中随机选择一个来顶吧
    # 问题3：顶贴的时间间隔是多少呢？是对一个帖子顶一次就换呢，还是一次就只顶一个帖子呢？
    #     时间间隔随机吧。对一个帖子顶一次就换。
    # 问题4：一组任务顶贴多少次呢？
    #     自己设置吧，作为参数传进去，顶完了就停了。
    def topPost(self,num):
        # 顶贴num次
        for i in range(num):
            # 第一步：选择目标帖子，post变量是元组类型
            post=self.readyPosts()
            # 第二步：选择合适的顶贴内容
            setUp=json.loads("setUp.json")
            content=setUp["顶贴"][random.randint(0,len(setUp["顶贴"])-1)]
            # 第三步：对目标帖子进行顶贴。等后面抓了包再来写


if __name__ == '__main__':
    # s = requests.Session()
    # resq_1 = s.get(URL_HOST, headers=HEADERS, verify=False)
    # print(resq_1)
    account=Account("15000950339","weippp5551994526")
    account.signIn()