import compositePattern.leaf
from compositePattern.leaf import Leaf


class Func(Leaf):
    def __init__(self, name):
        super().__init__(name)

    def add(self, item: compositePattern.leaf.Leaf):
        pass

    def remove(self, item: compositePattern.leaf.Leaf):
        pass

    def getChildItems(self):
        pass

    def display(self, level):
        str = "-" * level
        print(f"{str}name:{super().name}")
