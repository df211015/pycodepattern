from abc import abstractmethod

from observePattern.iObserver import IObserver


class AbsObservable:
    def __init__(self):
        self._lstObservers = []

    @property
    def lstObservers(self):
        return self._lstObservers

    def addObserver(self, observer: IObserver):
        flag = self.checkNotIn(observer)
        if flag:
            self.lstObservers.append(observer)

    def removeObserver(self, observer: IObserver):
        flag = self.checkIn(observer)
        if flag:
            self.lstObservers.remove(observer)

    def checkNotIn(self, observer: IObserver):
        return self.lstObservers is not None and observer not in self.lstObservers

    def checkIn(self, observer: IObserver):
        return self.lstObservers is not None and observer in self.lstObservers

    def notify(self, p):
        """
        通知观察者
        :param p: 入参类型:IObserver
        :return:
        """
        for observer in self.lstObservers:
            observer.update(p)

    @abstractmethod
    def change(self, p):
        pass
