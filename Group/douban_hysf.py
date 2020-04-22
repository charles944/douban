import time


INIT_TIMESTAMP=1577808000
SCORE_LIST=[]
data_list=['04-20 02:04','04-22 13:20','04-22 13:20','2014-09-05']
# start_time='2020-1-1 00:00:00'
# timeArray=time.strptime(start_time,"%Y-%m-%d %H:%M:%S")
# timeStamp=int(time.mktime(timeArray))
# print('2020-1-1 00:00:00:',timeStamp)
# print(int(time.time()))

# start_time='04-20 02:04'
# timeArray=time.strptime(start_time,"%m-%d %H:%M")
# print(timeArray)
for start_time in data_list:
    if "2019" in start_time or "2018" in start_time or "2017" in start_time or "2016" in start_time or "2015" in start_time or "2014" in start_time or "2013" in start_time or "2012" in start_time or "2011" in start_time or "2010" in start_time:
        timeArray=time.strptime(start_time,"%Y-%m-%d")
    else:
        start_time='-'.join(["2020",start_time])
        timeArray = time.strptime(start_time, "%Y-%m-%d %H:%M")
    timeStamp=int(time.mktime(timeArray))
    print(start_time,':',timeStamp)
    diff_timeStamp=timeStamp-INIT_TIMESTAMP
    score=diff_timeStamp/(int(time.time())-INIT_TIMESTAMP)
    SCORE_LIST.append(score)
# print(diff_timeStamp,score)

print(SCORE_LIST)