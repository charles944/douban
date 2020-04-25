
import time

now = int(time.time())  # 1533952277
timeArray = time.localtime(now)
print(timeArray)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print(otherStyleTime)