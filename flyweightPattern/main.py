from flyweightPattern.flyweightFactory import FlyweightFactory
from flyweightPattern.iFlyweight import IFlyweight
from flyweightPattern.unsharedConcreteFlyweight import UnsharedConcreteFlyweight

if __name__ == "__main__":
    factory = FlyweightFactory()
    obj: IFlyweight = factory.getFlyweight("one")
    unshareObj1 = UnsharedConcreteFlyweight("unshareObj1")
    unshareObj2 = UnsharedConcreteFlyweight("unshareObj2")
    obj.operate(unshareObj1)
    obj.operate(unshareObj2)

    objsecond: IFlyweight = factory.getFlyweight("second")
    unshareObj3 = UnsharedConcreteFlyweight("unshareObj3")
    objsecond.operate(unshareObj3)
