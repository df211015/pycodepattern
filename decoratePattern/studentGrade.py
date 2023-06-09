from decoratePattern.iGrade import IGrade


class StudentGrade(IGrade):
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    @property
    def name(self):
        return self._name

    @property
    def grade(self):
        return self._grade

    def printfGrade(self):
        print(f"name:{self._name},grade:{self._grade}")
