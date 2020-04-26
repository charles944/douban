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

