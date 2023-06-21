from abc import abstractmethod

from visitorPattern.student import Student


class IVisitor:
    @abstractmethod
    def visit(self, student: Student):
        pass
