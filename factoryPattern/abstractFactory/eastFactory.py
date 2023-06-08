from factoryPattern.abstractFactory.absFactory import AbsFactory
from factoryPattern.domain.gasoline import Gasoline
from factoryPattern.domain.normalCar import NormalCar


class EastFactory(AbsFactory):
    def createCar(self):
        return NormalCar("normal")

    def createEnergy(self):
        return Gasoline("gas")
