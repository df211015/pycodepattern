from compositePattern.leaf import Leaf


class Menu(Leaf):
    def __init__(self, name):
        super().__init__(name)
        # 初始化子结点
        self._childNodes = []

    def add(self, item):
        self._childNodes.append(item)

    def remove(self, item):
        self._childNodes.remove(item)

    def getChildItems(self):
        return self._childNodes

    def display(self, level):
        str = ""
        for i in range(level):
            str += "-"
        print(f"{str}name:{self.name}")
        for item in self._childNodes:
            item.display(level + 1)
