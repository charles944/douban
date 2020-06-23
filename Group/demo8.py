import csv
import pymysql

db=pymysql.connect(host='localhost',user='root',password='1994526succeed',port=3306,db="douban")
cursor=db.cursor()
save_sql='insert into xiaozu (title,number,url,score) values ("%s","%s","%s","%s")'
check_sql='select * from xiaozu where title="%s"'

def save(sql):
    cursor.execute(sql)
    db.commit()

def check(title):
    sql=check_sql%title
    cursor.execute(sql)
    resq=cursor.fetchall()
    if resq:
        return True
    else:
        return False

if __name__ == '__main__':
    with open("test.csv", "r", newline='') as f:
        groups = csv.reader(f)
        print(groups)
        a = 0
        for group in groups:
            a += 1
            # print(group)
            title=group[0]
            print('这是第%d个小组' % a)
            sql_check=check(title)
            if sql_check:
                print('小组已保存，不再保存')
            else:
                sql=save_sql%(group[0],group[1],group[2],group[3])
                save(sql)