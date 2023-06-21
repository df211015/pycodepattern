class Student:
    def __init__(self, name, gender, grade, remark):
        self._name = name
        self._gender = gender
        self._grade = grade
        self._remark = remark

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def grade(self):
        return self._grade
    @property
    def remark(self):
        return self._remark
