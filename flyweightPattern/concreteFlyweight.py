from flyweightPattern.iFlyweight import IFlyweight
from flyweightPattern.unsharedConcreteFlyweight import UnsharedConcreteFlyweight


class ConcreteFlyweight(IFlyweight):
    def __init__(self, key):
        self._key = key
        print(f"具体享元被创建,key:{key}")

    def operate(self, unsharedConcreteFlyweight: UnsharedConcreteFlyweight):
        print(f"ConcreteFlyweight -> operate,享元key:{self._key},非享元对象:{unsharedConcreteFlyweight.toString()}")
