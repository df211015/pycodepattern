from abc import abstractmethod

from chainPattern.param import Param


class AbsHandle:

    def __init__(self):
        self._nextHandle = None

    @property
    def nextHandle(self):
        return self._nextHandle

    @nextHandle.setter
    def nextHandle(self, handle):
        self._nextHandle = handle

    def process(self, param: Param):
        myType = param.type
        if self.getType(myType):
            self.response(param)
        else:
            if self.nextHandle is not None:
                self.nextHandle.process(param)
            else:
                print("未找到合适的处理类")

    @abstractmethod
    def getType(self, type):
        pass

    def response(self, param: Param):
        pass
