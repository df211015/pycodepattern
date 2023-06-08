from factoryPattern.domain.absEnergy import AbsEnergy


class Solarpanel(AbsEnergy):
    def __init__(self, name):
        super().__init__(name)

    def getEnergy(self):
        return self
