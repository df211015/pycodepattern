from decoratePattern.signGrade import SignGrade
from decoratePattern.sortGrade import SortGrade
from decoratePattern.studentGrade import StudentGrade

if __name__ == "__main__":
    grade = StudentGrade("zhangshang", 90)
    grade = SortGrade(grade)
    grade = SignGrade(grade)
    grade.printfGrade()
