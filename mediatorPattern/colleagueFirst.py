from mediatorPattern.absColleague import AbsColleague


class ColleagueFirst(AbsColleague):

    def selfMethod(self, param):
        print(f"ColleagueFirst -> selfMethod,param={param}")
        super().mediator.colleagueSecond.otherMethod(param)

    def otherMethod(self, param):
        print(f"ColleagueFirst -> otherMethod,param={param}")
