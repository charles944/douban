import re
import time
import pymysql


# 该类作为数据日志，用来详细记录程序运行情况，作为数据分析和挖掘的基础
class History(object):
    def __init__(self,uid):
        self.uid=uid