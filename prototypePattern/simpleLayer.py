from copy import copy, deepcopy


class SimpleLayer:
    """
    原型模式用于创建复杂的或者耗时的实例：复制一个已经存在的实例使程序运行更高效。
    """

    def getContent(self):
        return self.content

    def getBackground(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)
