from Auto2.Task import Task

class Post(Task):
    def __init__(self,groups,title,content,account):
        self.groups=groups
        self.content=content
        self.title=title
        self.accont=account

    def send(self):
        for group in self.groups:
            # 访问小组页面，开始发帖
            pass