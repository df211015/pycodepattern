from factoryPattern.domain.absCar import AbsCar


class SUVCar(AbsCar):
    def __init__(self, name):
        # super(SUVCar, self).__init__(name)
        super().__init__(name)

    def getCar(self):
        return self
