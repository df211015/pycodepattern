from flyweightPattern.concreteFlyweight import ConcreteFlyweight


class FlyweightFactory:
    def __init__(self):
        # 声明一个字典
        self._keyMap = dict()

    @property
    def keyMap(self):
        return self._keyMap

    def getFlyweight(self, key):
        obj = self.keyMap.get(key)
        if obj is None:
            obj = ConcreteFlyweight(key)
            self.keyMap[key] = obj

        return obj
