from chainPattern.absHandle import AbsHandle
from chainPattern.eType import EType
from chainPattern.param import Param


class HandleOfThird(AbsHandle):
    def getType(self, type):
        if EType.third == type:
            return True
        else:
            return False

    def response(self, param: Param):
        print("HandleOfThird -> response")
