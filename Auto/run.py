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

def getUsername():
    pass


def getPassword():
    pass


if __name__ == '__main__':
    username=getUsername()
    password=getPassword()
    account=Account(username,password)
    resq=account.signIn()
