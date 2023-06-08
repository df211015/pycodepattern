from factoryPattern.abstractFactory.absFactory import AbsFactory
from factoryPattern.domain.solarpanel import Solarpanel
from factoryPattern.domain.suvCar import SUVCar


class WestFactory(AbsFactory):
    def createCar(self):
        return SUVCar("suv")

    def createEnergy(self):
        return Solarpanel("solar")
