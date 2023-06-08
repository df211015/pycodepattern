class AbsCar:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"{self._name}Car"

    @name.setter
    def name(self, name):
        self._name = name

    def getCar(self):
        """
        抽象基类
        :return: AbsCar
        """
        pass
