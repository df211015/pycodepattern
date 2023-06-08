from factoryPattern.domain.absCar import AbsCar


class PickCar(AbsCar):
    def __init__(self, name):
        # super(PickCar, self).__init__(name)
        super().__init__(name)
        
    def getCar(self):
        return self
