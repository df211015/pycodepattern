from chainPattern.absHandle import AbsHandle
from chainPattern.eType import EType
from chainPattern.param import Param


class HandleOfSecond(AbsHandle):
    def getType(self, type):
        if EType.seconde == type:
            return True
        else:
            return False

    def response(self, param: Param):
        print("HandleOfSecond -> response")