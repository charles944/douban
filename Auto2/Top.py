from Auto2.Task import Task

class Top(Task):
    def __init__(self,posts,content,number,account):
        self.posts=posts
        self.content=content
        self.number=number
        self.account=account

    def sendtop(self):
        for post in self.posts:
            # 接下来为每一个帖子顶贴
            pass