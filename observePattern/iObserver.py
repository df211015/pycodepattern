from abc import abstractmethod


class IObserver:
    @abstractmethod
    def update(self, p):
        pass
