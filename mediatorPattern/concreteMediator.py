from mediatorPattern.absMediator import AbsMediator


class ConcreteMediator(AbsMediator):
    def doOfColleagueFirst(self, param):
        super().colleagueFirst.otherMethod(param)

    def doOfColleagueSecond(self, param):
        super().colleagueSecond.otherMethod(param)
