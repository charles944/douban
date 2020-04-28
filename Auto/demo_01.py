
import json
import demjson
import requests

# try:
#     resq=requests.get("https://www.douban.com")
# except:
#     print("连接错误")
# # print(resq)
# i = 0
# def test_01():
#     print("我是你爸爸")
#     global i
#     if i<4:
#         i=i+1
#         print("i的值：",i)
#         test_01()
    # if i<4:
    #     print("i的值：", i)
    #     test_01()
    #     i+=1

# def test_02(i):
#     print("我是你爸爸")
#     if i<4:
#         i+=1
#         print("i的值：",i)

for i in list(range(10)):
    # if i/2==0:
    #     print(i)
    # else:
    #     continue
    # print(i)
    if i%2==0:
        continue
    print(i)


# x = 1
# print(x)
# def fun():
#     global x
#     if x < 20:
#         x = x+2
#         print(x)
#     else:
#         exit()
#     fun()
# fun()


# if __name__ == '__main__':
#     test_01()
# user_info = '{"name" : "john", "gender" : "male", "age": 28}'
# user_dict = eval(user_info)
# print(type(user_dict))

# js_json = "{x:1, y:2, z:3}"
#
# py_json1 = "{'x':1, 'y':2, 'z':3}"
#
# py_json2 = '{"x":1, "y":2, "z":3}'
#
# data = demjson.decode(js_json)
# print(type(data),data)
# # {'y': 2, 'x': 1, 'z': 3}
#
# data = demjson.decode(py_json1)
# print(type(data),data)
# # {'y': 2, 'x': 1, 'z': 3}
#
# data = demjson.decode(py_json2)
# print(type(data),data)
# {'y': 2, 'x': 1, 'z': 3}

# # javascript中的对象
# js_json = "{x:1, y:2, z:3}"
#
# # python打印出来的字典
# py_json1 = "{'x':1, 'y':2, 'z':3}"
#
# # 解析不规则的json会报错
# json.loads(js_json)
# json.loads(py_json1)
# # ValueError: Expecting property name: line 1 column 2 (char 1)
#
# # 解析规则的json
# py_json2 = '{"x":1, "y":2, "z":3}'
#
# data = json.loads(py_json2)
# print(data)
# {'y': 2, 'x': 1, 'z': 3}

# json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#
# text = demjson.decode(json)
# print(type(text))

# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# jsonData_02='["1","2","3","4","5","6"]'
# jsonData_03='100'
#
# text = json.loads(jsonData)
# text_02=json.loads(jsonData_02)
# text_03=json.loads(jsonData_03)
# print(type(text),text)
# print(type(text_02),text_02)
# print(type(text_03),text_03)

import time

# now = int(time.time())  # 1533952277
# timeArray = time.localtime(now)
# print(timeArray)
# otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
# print(otherStyleTime)

# sign_data={
#     'ck':'',
#     'name':'%s',
#     'password':'%s',
#     'remenber':'false',
#     'ticket':''
# }
# usaername="charles"
# password="1004526succeed"
# sign_data='{"ck":"","name":"%s","password":"%s","remenber":"false","ticket":""}'
# sign_data=sign_data%(usaername,password)
# sign_data=json.loads(sign_data)
# # print(sign_data%(usaername,password))
# print(type(sign_data),sign_data)
