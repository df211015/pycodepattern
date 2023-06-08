from factoryPattern.domain.normalCar import NormalCar
from factoryPattern.domain.pickCar import PickCar
from factoryPattern.domain.suvCar import SUVCar


class CarFactory:
    def getInstanceCar(self, name):
        """
        :param name:车类型
        :return:
        """
        if name == "normal":
            return NormalCar(name)
        elif name == "suv":
            return SUVCar(name)
        elif name == "pick":
            return PickCar(name)
        else:
            return None