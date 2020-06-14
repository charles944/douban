import requests
from lxml import etree
import re
from urllib import parse
import pymysql
import time


db=pymysql.connect(host='localhost',user='root',password='1994526succeed',port=3306,db="douban_xiaozu")
cursor=db.cursor()

URL_SEARCH="https://www.douban.com/search?cat=1019&q="
URL_GROUP="https://www.douban.com/group/"
HEADERS = {
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36';
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3761.400 QQBrowser/10.6.4116.400',
}

def getproxy():
    # resq=requests.get('http://http.9vps.com/getip.asp?username=charles&pwd=c3477e5847fd1d43acf1bcebba0be86d&geshi=1&fenge=1&fengefu=&getnum=0')
    resq=requests.get('http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2')
    print('现在使用的代理ip是%s'%resq.text.strip())
    proxies = {
        "https": resq.text.strip()
    }
    return proxies
proxies=getproxy()

def visit_html(url):
    global proxies
    try:
        resq=requests.get(url,headers=HEADERS,proxies=proxies,timeout=1)
    except:
        print('访问失败，更换代理')
        # time.sleep(10)
        proxies=getproxy()
        try:
            resq = requests.get(url, headers=HEADERS, proxies=proxies,timeout=1)
        except:
            # time.sleep(10)
            print("这个代理不行，换一个代理")
            resq=visit_html(url)

    if resq.status_code==200:
        # print("resq的状态是200")
        pass
    else:
        print("resq的状态是%d"%(resq.status_code),'需要重新申请代理')
        proxies=getproxy()
        try:
            resq = requests.get(url, headers=HEADERS, proxies=proxies,timeout=1)
        except:
            print("这个代理不行，换一个代理")
            resq=visit_html(url)
    return resq

def active_score(data_list):
    INIT_TIMESTAMP = 1577808000
    SCORE_LIST = []
    # start_time='2020-1-1 00:00:00'
    # timeArray=time.strptime(start_time,"%Y-%m-%d %H:%M:%S")
    # timeStamp=int(time.mktime(timeArray))
    # print('2020-1-1 00:00:00:',timeStamp)
    # print(int(time.time()))
    # start_time='04-20 02:04'
    # timeArray=time.strptime(start_time,"%m-%d %H:%M")
    # print(timeArray)
    for start_time in data_list:
        if "2019" in start_time or "2018" in start_time or "2017" in start_time or "2016" in start_time or "2015" in start_time or "2014" in start_time or "2013" in start_time or "2012" in start_time or "2011" in start_time or "2010" in start_time  or "2009" in start_time or "2008" in start_time or "2007" in start_time or "2006" in start_time or "2005" in start_time or "2004" in start_time or "2003" in start_time :
            timeArray = time.strptime(start_time, "%Y-%m-%d")
        else:
            start_time = '-'.join(["2020", start_time])
            timeArray = time.strptime(start_time, "%Y-%m-%d %H:%M")
        timeStamp = int(time.mktime(timeArray))
        # print(start_time, ':', timeStamp)
        diff_timeStamp = timeStamp - INIT_TIMESTAMP
        score = diff_timeStamp / (int(time.time()) - INIT_TIMESTAMP)
        SCORE_LIST.append(score)
    sum = 0
    for a in SCORE_LIST:
        sum = sum + a
    try:
        act_score=int((sum/len(SCORE_LIST))*100)
        return act_score
    except:
        print("遇到了除0错误")
        return 0
    # return act_score

def save_groupinfo(param, number_group, param1,act_score):
    sql="INSERT INTO xiaozu VALUES ('%s','%s','%s','%s')"%(param, number_group, param1,act_score)
    print(param, number_group, param1,act_score)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('sql语句有非法字符')


def get_score(url):
    resq=visit_html(url)
    HTML=etree.HTML(resq.text)
    data_list=HTML.xpath("//tr/td[contains(@class,'time')]/text()")
    top=HTML.xpath("//img[@alt='[置顶]']")
    print("首页有%d条帖子，其中%d置顶帖"%(len(data_list),len(top)))
    act_score=active_score(data_list[len(top):])
    return act_score

def reflash_page(keywords,j):
    # 首先将i值归零，如果该方法调用结束，i依然为0，那就停止循环，开始下一个词语
    i=0
    url="https://www.douban.com/j/search?q=%s&start=%s&cat=1019"%(keywords,str(j*20))
    resq_json=visit_html(url)
    resq_json=resq_json.text
    url_list = re.findall("url=(.*?)query", resq_json)
    title_list = re.findall(r'title=\\"(.*?)\\">', resq_json)
    number_list = re.findall(r'<div class=\\"info\\">\\n(.*?)\\n', resq_json)
    for a in range(len(url_list)):
        url=url_list[a]
        url = parse.unquote(url)
        url_list[a]=url[:-6]
    print(url_list)
    for b in range(len(number_list)):
        number=number_list[b]
        number=number.strip()
        number=number[:-3]
        number_list[b]=number
        if int(number)>5000:
            i+=1
            act_score=get_score(url_list[2*b])
            save_groupinfo(title_list[b], number, url_list[2*b],act_score)
        # print(number)
        # print(number_list)
    return i

# print(number_group_list,title_group_list)
# print(number_groups)
# for i in range(number_groups):
#     title_group=html.xpath("//h3/a/text()[%s]"%(str(i+1)))
#     print(title_group)
#     number_group=html.xpath("//div[@class='info']/text()[%s]"%(str(i+1)))
#     print(number_group)
# # "https://www.douban.com/link2/?url=http%3A%2F%2Fwww.douban.com%2Fgroup%2Ffendoucheng%2F&query=%E5%A5%8B%E6%96%97&cat_id=1019&type=search&pos=19"


def get_info(url,keywords):
    resq=visit_html(url)
    html = etree.HTML(resq.text)
    # number_groups=len(html.xpath("//div[@class='info']/text()"))
    # 获取页面的小组名称、小组链接和小组人数
    number_group_list = html.xpath("//div[@class='info']/text()")
    title_group_list = html.xpath("//h3/a/text()")
    url_group_list = html.xpath("//h3/a/@href")
    # print(len(number_group_list))
    # print(len(title_group_list))
    # print(len(url_group_list))
    top_number = len(re.findall("置顶", resq.text))
    number_group_list = number_group_list[top_number:]
    title_group_list=title_group_list[top_number:]
    url_group_list=url_group_list[top_number:]
    # 提取出各个小组的链接，格式化后存入数组中
    for i in range(len(url_group_list)):
        url_group = url_group_list[i]
        url_group = re.search('url=(.*?)query', url_group)
        # print(url_group.group(1))
        url_group = parse.unquote(url_group.group(1))
        url_group_list[i] = url_group[:-2]
    # print(number_group_list)
    i = 0
    # 判断小组人数是否大于5000，如果是，就将小组信息存入数据库
    for i in range(len(number_group_list)):
        number_group = number_group_list[i]
        number_group = number_group.strip()
        number_group = number_group[:-3]
        if int(number_group) > 5000:
            # print(title_group_list[i], number_group, url_group_list[i])
            act_score = get_score(url_group_list[i])
            save_groupinfo(title_group_list[i], number_group, url_group_list[i],act_score)
            i += 1
    # 如果i的值大于0，说明该页存在人数大于5000的小组，那么就用ajax继续查询该关键词
    j = 0
    while i > 0:
        j+=1
        i=reflash_page(keywords,j)

if __name__ == '__main__':
    with open("keywords.txt", "r", encoding='utf-8-sig') as f_1:
        keywords = f_1.read()
        keywords = keywords.split(" ")
        keywords_arr = []
        for word in keywords:
            word = word.strip()
            if len(word) != 0:
                keywords_arr.append(word)
        print(keywords_arr)
        # print(len(keywords_arr))
    with open("test_02.txt", "a+", encoding="utf-8") as f_2:
        f_2.seek(0)
        word_list_02 = f_2.read()
        word_list_02 = word_list_02.split("\n")
        print(word_list_02)
        update_word=word_list_02[len(word_list_02) - 1]
        # if ("\ufeff" in update_word):
        #     update_word=update_word.replace("\ufeff","")
        print("update_word是%s"%update_word)
        index = keywords_arr.index(update_word)
        # print(index)
        loop_count = len(keywords_arr) - index-1
        for i in range(loop_count):
            word = keywords_arr[index + i+1]
            # for word in keywords:
            #     word=word.strip()
            #     if len(word)!=0:
            time.sleep(1)
            # print(word)
            print("f_2.tell()的值是%d"%f_2.tell())
            url = URL_SEARCH + word
            print("现在查询的词是%s" % word)
            get_info(url, word)
            f_2.write("\n"+word)
    # code_list = code.split(" ")
    # print(len(code_list))
    # # keyswords_list=[]
    # for i in range(len(code_list)):
    #     keywords = code_list[i].strip()
    #     if keywords != "":
    #
    #         print("现在来查询的关键词是：", keywords)
    #         # keyswords_list.append(keywords)
