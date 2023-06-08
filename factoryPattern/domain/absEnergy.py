class AbsEnergy:
    """
    能源抽象类
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"energy={self._name}"

    @name.setter
    def name(self, name):
        self._name = name

    def getEnergy(self):
        pass
