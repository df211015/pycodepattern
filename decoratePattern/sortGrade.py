from decoratePattern.absGrade import AbsGrade
from decoratePattern.iGrade import IGrade


class SortGrade(AbsGrade):
    def __init__(self, iGrade: IGrade):
        super().__init__(iGrade)

    def sortGrade(self):
        print("sort grade")

    def printfGrade(self):
        self.sortGrade()
        super().printfGrade()
