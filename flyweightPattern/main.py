from flyweightPattern.flyweightFactory import FlyweightFactory
from flyweightPattern.iFlyweight import IFlyweight
from flyweightPattern.unsharedConcreteFlyweight import UnsharedConcreteFlyweight

"""
享元模式demo
该模式建议将一个大对像拆解为若干组合的小对像,在设计时需要区分外部状态和内部状态,通过外部状态的共享从而实现其中部分属性的重用
"""
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
