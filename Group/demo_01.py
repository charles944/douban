import requests
from lxml import etree
import time

# HEADERS = {
#     'Host': 'www.douban.com',
#     'Referer': 'https://www.douban.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
# resq=requests.get("https://www.douban.com/group/shanghaizufang/",headers=HEADERS)
# HTML=etree.HTML(resq.text)
# uptime=HTML.xpath("//tr/td[contains(@class,'time')]/text()")
# print(len(uptime))


with open("keywords.txt",'r',encoding="utf-8") as f_1:
    keywords=f_1.read()
    keywords=keywords.split(" ")
    keywords_arr=[]
    for word in keywords:
        word=word.strip()
        if len(word)!=0:
            keywords_arr.append(word)
    print(keywords_arr)
with open("test_01.txt","a+",encoding="utf-8") as f_2:
    f_2.seek(0)
    word_list_02=f_2.read()
    word_list_02=word_list_02.split(" ")
    index=keywords_arr.index(word_list_02[len(word_list_02)-1])
    print(index)
    loop_count=len(keywords_arr)-index
    for i in range(loop_count):
        word=keywords_arr[index+i]
    # for word in keywords:
    #     word=word.strip()
    #     if len(word)!=0:
        time.sleep(1)
        print(word)
        print(f_2.tell())
        f_2.write(word+" ")

# with open("test_01.txt","r",encoding="utf-8") as f_3:
#     words=f_3.read()
#     word_list=words.split(" ")
#     print(len(word_list))