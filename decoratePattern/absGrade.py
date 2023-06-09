from abc import abstractmethod

from decoratePattern.iGrade import IGrade


class AbsGrade(IGrade):
    def __init__(self, iGrade: IGrade):
        self._iGrade = iGrade

    def printfGrade(self):
        self._iGrade.printfGrade()
