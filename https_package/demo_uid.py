import re

with open("uid.txt",'r',encoding='utf-8') as f:
    resq=f.read()

print(resq)
uid=re.search('id":"(.*?)"',resq)
print(uid.group(1))