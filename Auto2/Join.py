from Auto2.Task import Task

class Join(Task):
    def __init__(self,groups,account):
        self.groups=groups
        self.account=account

    def joingroup(self):
        for group in self.groups:
            # 访问小组页面，提出加入小组申请
            pass