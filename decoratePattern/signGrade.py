from decoratePattern.absGrade import AbsGrade
from decoratePattern.iGrade import IGrade


class SignGrade(AbsGrade):
    def __init__(self, iGrade: IGrade):
        super().__init__(iGrade)

    def signGrade(self):
        print("sign grade")

    def printfGrade(self):
        self.signGrade()
        super().printfGrade()