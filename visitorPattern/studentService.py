from visitorPattern.iVisitor import IVisitor


class StudentService:
    def __init__(self, student):
        self._student = student

    @property
    def student(self):
        return self._student

    def accept(self, visitor: IVisitor):
        visitor.visit(self.student)
