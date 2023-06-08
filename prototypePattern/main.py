from prototypePattern.simpleLayer import SimpleLayer

if __name__ == "__main__":
    # 正常构建对像
    dog_layer = SimpleLayer()
    dog_layer.paint("dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print(f"background:{dog_layer.getBackground()}")
    print(f"painting:{dog_layer.getContent()}")
    another_dog_layer = dog_layer.clone()
    # 通过复制获取实例
    print(f"background:{another_dog_layer.getBackground()}")
    print(f"painting:{another_dog_layer.getContent()}")
