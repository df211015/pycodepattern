from chainPattern.eType import EType
from chainPattern.handleOfFirst import HandleOfFirst
from chainPattern.handleOfSecond import HandleOfSecond
from chainPattern.handleOfThird import HandleOfThird
from chainPattern.param import Param

"""
职责链模式demo
"""
if __name__ == "__main__":
    param = Param("aaa", EType.seconde)
    first = HandleOfFirst()
    second = HandleOfSecond()
    third = HandleOfThird()
    first.nextHandle = second
    second.nextHandle = third
    third.nextHandle = None
    first.process(param)
