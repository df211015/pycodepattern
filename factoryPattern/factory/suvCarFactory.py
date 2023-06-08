from factoryPattern.domain.suvCar import SUVCar
from factoryPattern.factory.absCarFactory import AbsCarFactory


class SuvCarFactory(AbsCarFactory):
    def createCarFactory(self):
        return SUVCar("suv")
