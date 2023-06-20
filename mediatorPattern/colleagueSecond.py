from mediatorPattern.absColleague import AbsColleague


class ColleagueSecond(AbsColleague):

    def selfMethod(self, param):
        print(f"ColleagueSecond -> selfMethod,param={param}")
        super().mediator.colleagueFirst.otherMethod(param)

    def otherMethod(self, param):
        print(f"ColleagueSecond -> otherMethod,param={param}")
