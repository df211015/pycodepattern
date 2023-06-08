from factoryPattern.domain.absCar import AbsCar


class NormalCar(AbsCar):
    def __init__(self, name):
        # super(NormalCar, self).__init__(name)
        super().__init__(name)

    def getCar(self):
        return self
