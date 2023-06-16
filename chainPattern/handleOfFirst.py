from chainPattern.absHandle import AbsHandle
from chainPattern.eType import EType
from chainPattern.param import Param


class HandleOfFirst(AbsHandle):
    def getType(self, type):
        if EType.first == type:
            return True
        else:
            return False

    def response(self, param: Param):
        print("HandleOfFirst -> response")
