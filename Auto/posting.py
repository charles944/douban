import re
from lxml import etree
import time

class Posting(object):
    def __init__(self,uid,s):
        self.s=s
        self.uid=uid

    # 选取某个小组进行发帖
    def post(self,group,uid,s):
        pass

    # 获取已经发的帖子
    def readyPosts(self,uid,s):
        pass

    # 顶贴
    def topPost(self):
        pass