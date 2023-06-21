"""
访问者模式demo
"""
from visitorPattern.student import Student
from visitorPattern.studentService import StudentService
from visitorPattern.visitorOfParents import VisitorOfParents

if __name__ == "__main__":
    student = Student("王大海", "男", "A", "学生介绍")
    studentService = StudentService(student)
    visitor = VisitorOfParents()
    studentService.accept(visitor)
