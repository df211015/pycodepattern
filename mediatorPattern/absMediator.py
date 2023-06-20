from abc import abstractmethod


class AbsMediator:
    def __init__(self, colleagueFirst, colleagueSecond):
        self._colleaguefirst = colleagueFirst
        self._colleagueSeond = colleagueSecond

    @property
    def colleagueFirst(self):
        return self._colleaguefirst

    @property
    def colleagueSecond(self):
        return self._colleagueSeond

    @abstractmethod
    def doOfColleagueFirst(self, param):
        pass

    @abstractmethod
    def doOfColleagueSecond(self, param):
        pass
