class Leaf:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def getChildItems(self):
        pass

    def display(self, level):
        pass
