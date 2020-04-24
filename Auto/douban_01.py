import  requests
from Auto.Settings import *
import re




# 这里访问url肯定得带着cookie和session
s=requests.Session()
resq_1=s.get(URL_HOST,headers=HEADERS,verify=False)
print(resq_1)
resq_2=s.post("https://accounts.douban.com/j/mobile/login/basic",data=sign_data,headers=SIGNIN_HEADERS,verify=False)
# 这里要加上换IP和过验证码的功能
# print(resq_2.text)
uid=re.search('id":"(.*?)"',resq_2.text)
uid=uid.group(1)
# print(uid.group(1))

# 接下来要写的功能有:
# 1.自动加入和退出小组;
# 2.选择小组进行发言;
# 3.选择帖子进行顶贴
