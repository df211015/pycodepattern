class Param:
    """
    定义dto
    """
    __slots__ = ["_name", "_type"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    def __init__(self, name, type):
        self._name = name
        self._type = type
