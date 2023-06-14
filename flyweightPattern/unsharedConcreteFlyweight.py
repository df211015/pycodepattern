class UnsharedConcreteFlyweight:
    def __init__(self, info):
        self._info = info

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

    def toString(self):
        return self.info
