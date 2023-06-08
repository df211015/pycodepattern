from factoryPattern.simpleFactory.carFactory import CarFactory

# 简单工厂模式
carFactory = CarFactory()
car = carFactory.getInstanceCar("pick")
print(f"carInfo={car.getCar().name}")