import re
import pymysql

db=pymysql.connect(host='localhost',user='root',password='1994526succeed',port=3306,db="ximalaya")
cursor=db.cursor()

# 过验证码
def verificationCode():
    pass

