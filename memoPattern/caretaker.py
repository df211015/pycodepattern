class Caretaker:
    def __init__(self):
        self._lstMemo = []

    @property
    def lstMemo(self):
        return self._lstMemo

    def addMemo(self, memo):
        self.lstMemo.append(memo)

    def getMemo(self):
        """
        此处可以有加入获取策略
        :return:
        """
        return self.lstMemo[0]
