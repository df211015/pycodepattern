from memoPattern.memo import Memo


class Originator:
    @property
    def propdata(self):
        return self._propdata

    @propdata.setter
    def propdata(self, data):
        self._propdata = data

    def createMemo(self):
        """
        生成一个备忘录
        :return:
        """
        return Memo(self.propdata)

    def restoreMemo(self, memo):
        """
        获取备忘录恢复
        :param memo:
        :return:
        """
        self.propdata = memo.data
