import requests
import re

# resq=requests.get("http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=0&specialTxt=3&specialJson=&usertype=1")
# text=resq.text
# print(text)
# # text='{"code":0,"success":true,"msg":"","data":[{"IP":"0.0.0.0","Port":8080,"ExpireTime":"2018-01-01 08:08:08","IpAddress":"湖南省益阳市 电信","ISP":"电信"},{"IP":"0.0.0.0","Port":8080,"ExpireTime":"2018-01-01 08:08:08","IpAddress":"湖南省益阳市 电信","ISP":"电信"}]}'
# status_code=re.search('code":(.*?),"success"',text)
# status_success=re.search('success":(.*?),"msg"',text)
# ip=re.search('IP":"(.*?)","Port"',text)
# port=re.search('"Port":(.*?),"ExpireTime',text)
# proxy='https://%s:%s'%(ip.group(1),port.group(1))
# print('status_code:%s'%status_code.group(1),'status_succeee:%s'%status_success.group(1),'ip:%s'%ip.group(1),'prot:%s'%port.group(1))
# if status_code.group(1)=='0':
#     if status_success.group(1)=='true':
#         print(proxy)
#     else:
#         print("获取代理失败")
# else:
#     print("获取代理失败")

HEADERS = {
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36';
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3761.400 QQBrowser/10.6.4116.400',
}

resq=requests.get('http://http.9vps.com/getip.asp?username=charles&pwd=c3477e5847fd1d43acf1bcebba0be86d&geshi=1&fenge=1&fengefu=&getnum=0')
# resq=requests.get('http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=0&specialTxt=3&specialJson=&usertype=2')
# print(resq.text)
proxies={
    "https":resq.text.strip()
}
resq_douban=requests.get("https://www.douban.com/",headers=HEADERS,proxies=proxies)
print(resq_douban.status_code)

# print(proxies)