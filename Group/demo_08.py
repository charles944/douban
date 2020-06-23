import csv
import pymysql

db=pymysql.connect(host='localhost',user='root',password='1994526succeed',port=3306,db="douban")
cursor=db.cursor()

sql_one='select * from xiaozu where title="太原兼职"'
sql_all='select * from xiaozu where title like "%租房%"'

# cursor.execute(sql_one)
cursor.execute(sql_all)
one=cursor.fetchone()
cursor.execute(sql_all)
all=cursor.fetchall()
cursor.execute(sql_all)
many=cursor.fetchmany(20)
print('fetchone的返回值是',one)
print('fetchall的返回值是',all)
print('fetchmany的返回值是',many)