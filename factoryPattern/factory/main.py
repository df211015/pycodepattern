from factoryPattern.factory.normalCarFactory import NormalCarFactory
from factoryPattern.factory.pickCarFactory import PickCarFactory

# 工厂模式
carFactory = NormalCarFactory()
car = carFactory.createCarFactory()
print(f"car={car.getCar().name}")

carFactory = PickCarFactory()
car = carFactory.createCarFactory()
print(f"car={car.getCar().name}")