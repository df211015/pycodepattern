from factoryPattern.abstractFactory.eastFactory import EastFactory
from factoryPattern.abstractFactory.westFactory import WestFactory

# 抽象工厂模式

# 定义工厂1
factory = EastFactory()
car = factory.createCar()
energy = factory.createEnergy()
print(car.getCar().name)
print(energy.getEnergy().name)

# 定义工厂2
factory = WestFactory()
car = factory.createCar()
energy = factory.createEnergy()
print(car.getCar().name)
print(energy.getEnergy().name)