from abc import abstractmethod

from builderPattern.superStar import SuperStar


class AbsBuilder:
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def favorite(self):
        return self._favorite

    def buildName(self, name):
        """
        构建对像name属性
        :param name:
        :return:
        """
        self._name = name
        return self

    def buildAge(self, age):
        """
        构建对像age属性
        :param age:
        :return:
        """
        self._age = age
        return self

    def buildFavorite(self, favorite):
        """
        构建对像favorite属性
        :param favorite:
        :return:
        """
        self._favorite = favorite
        return self

    @abstractmethod
    def build(self):
        """
        抽象方法
        :return: AbsBuilder
        """
        pass
