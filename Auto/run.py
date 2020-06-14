import  requests
from Auto.Settings import *
import re
from Auto.account import Account
import json



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
    # 这里是用的读取txt文件的方式来获取账号，后面得改成从json、xml等配置文件中获取账号，后面别忘了改
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
            resq=account.signIn(4)
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
            # 工作流的配置就用json来写啊，后面考虑用cfg、XML或者ini来替换，现在就这样，先把主程序给写出来。
            # 现在来读取json文件配置的工作流
            setUp=json.loads("setUp.json")
            taskFlow=setUp["选择功能"]
            # 现在问题来了：1.难道每个账号发的帖子内容都一样吗？肯定不是啊；2.难道每个账号要加入的小组都是一样的吗？肯定不是啊
            for task in taskFlow:
                if task=="1":
                    # 如果为“1”，那么开始发帖
                    # 问题：用什么机制来发帖呢？为每个账号如何分配要发帖的小组和发帖的内容呢？
                    # 1.小组的选择：随机选择一个小组吗？肯定不行啊，得选择一个已经加入、并且目前最适合最营销的小组啊
                    # 2.内容的选择：随机从json配置文件中选取一个内容来发，同时记录下来这次发帖，看看怎么能监测这条帖子的内容，并且在后续把内容选择优化下，尽量选择效果最好的帖子
                    account.posting()
                elif task=="2":
                    # 如果为“2,”，那么开始顶贴
                    account.topPost()
                elif task=="3":
                    # 如果为“3”，那么加入某个小组
                    account.joinGroups()
                else:
                    # 如果以上都不是，那说明写错了，记录运行错误，但是不停止程序运行
                    print("运行配置错啦")

    # 接下来还需要做的任务：
    # 1.设计好mysql的数据库；
    # 2.埋点，将数据保存到mysql数据库中。先来设计mysql的数据库。
    # ps：面对网络请求的延时，有直接的参数可以设置的。还可以检测状态码是否是200，没必要特地写一个递归函数，增加了代码的复杂性。