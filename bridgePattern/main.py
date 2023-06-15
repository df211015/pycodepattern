from bridgePattern.concreteImplement import ConcreteImplement
from bridgePattern.concreteService import ConcreteService

"""
桥梁模式demo
将实现和抽象分离开来,各自有自己的开发维护空间
"""
if __name__ == "__main__":
    implement = ConcreteImplement()
    service = ConcreteService(implement)
    service.process("bridge")
