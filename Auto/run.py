import  requests
from Auto.Settings import *
import re
from Auto.account import Account



# 这里访问url肯定得带着cookie和session
# s=requests.Session()
# resq_1=s.get(URL_HOST,headers=HEADERS,verify=False)
# print(resq_1)
# resq_2=s.post("https://accounts.douban.com/j/mobile/login/basic",data=sign_data,headers=SIGNIN_HEADERS,verify=False)
# # 这里要加上换IP和过验证码的功能
# # print(resq_2.text)
# uid=re.search('id":"(.*?)"',resq_2.text)
# uid=uid.group(1)
# # print(uid.group(1))




if __name__ == '__main__':
    with open("demo.txt","r",encoding="utf-8") as f:
        contents=f.readlines()
        print(len(contents))
        for content in contents:
            content_list=content.split("----")
            username=content_list[0].strip()
            password=content_list[1].strip()
            print("账号：",username,"密码：",password)
            account=Account(username,password)
            # 发送登陆包，获取登陆包的返回值
            resq=account.signIn()
            # 登录成功，接下来判断账号是否被封。如果该账号被封，停止运行接下来的代码，直接开始下一个账号
            if not account.isClose():
                continue
            # 接下来获取系统信息和用户信息。如果有小组申请最近消息、用户回信、帖子被删等信息，都保存到日志中，以便后续数据分析用
            massage=account.getMassage()
            # 此时还需要加一个日志类，把所有的动作记录都保存到日志中，方便后面查看
            # 接下来获取账号信息，包括账号发帖条数、顶贴次数、加入小组数、收到的私信数、被用户回复数，要让每一条记录都是可以追溯的。
            # 这样是不是有点太理想化了，实际上的日志能做到这么详细么？不管了，我先把功能的位置写在这里，看后面是否真的要实现出来。
            accountInfo=account.getInfo()
            # 获取账号信息后的下一步，是选择到底使用什么功能，使用这些功能的顺序是怎样的。我希望程序以一种什么方式被操作起来呢？
            # 怎么计划工作流呢
