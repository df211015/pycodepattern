from factoryPattern.domain.normalCar import NormalCar
from factoryPattern.factory.absCarFactory import AbsCarFactory


class NormalCarFactory(AbsCarFactory):
    def createCarFactory(self):
        return NormalCar("normal")
