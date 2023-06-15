from bridgePattern.concreteImpliment import ConcreteImpliment
from bridgePattern.concreteService import ConcreteService

"""
桥接模式demo
将实现和抽象分离开来,各自有自己的开发维护空间
"""
if __name__ == "__main__":
    impliment = ConcreteImpliment()
    service = ConcreteService(impliment)
    service.process("bridge")
