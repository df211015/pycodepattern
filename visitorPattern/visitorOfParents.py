from visitorPattern.iVisitor import IVisitor
from visitorPattern.student import Student


class VisitorOfParents(IVisitor):
    """
    家长视角访问者, 家长的视角侧重学生成绩
    """

    def visit(self, student: Student):
        print(f"studentinfo,name:{student.name},grade:{student.grade}")
