from factoryPattern.domain.pickCar import PickCar
from factoryPattern.factory.absCarFactory import AbsCarFactory


class PickCarFactory(AbsCarFactory):
    def createCarFactory(self):
        return PickCar("pick")