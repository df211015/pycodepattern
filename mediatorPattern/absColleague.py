from abc import abstractmethod

from mediatorPattern.absMediator import AbsMediator


class AbsColleague:
    def __init__(self):
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, m: AbsMediator):
        self._mediator = m

    @abstractmethod
    def selfMethod(self, param):
        """
        处理自己范畴内的业务
        :param param:
        :return:
        """
        pass

    @abstractmethod
    def otherMethod(self, param):
        """
        处理需要中介者协调的业务
        :param param:
        :return:
        """
        pass
