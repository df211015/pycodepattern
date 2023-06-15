from bridgePattern.concreteImpliment import ConcreteImpliment
from bridgePattern.concreteService import ConcreteService

if __name__ == "__main__":
    impliment = ConcreteImpliment()
    service = ConcreteService(impliment)
    service.process("bridge")