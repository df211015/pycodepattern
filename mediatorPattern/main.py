from mediatorPattern.colleagueFirst import ColleagueFirst
from mediatorPattern.colleagueSecond import ColleagueSecond
from mediatorPattern.concreteMediator import ConcreteMediator

"""
中介者模式demo
当有多个对像进行交互时,避免出现各个对像的直接交互,而应该通过中介类与外对像进行交互
"""
if __name__ == "__main__":
    colleagueFirst = ColleagueFirst()
    colleagueSecond = ColleagueSecond()
    media = ConcreteMediator(colleagueFirst, colleagueSecond)
    colleagueFirst.mediator = media
    colleagueSecond.mediator = media
    colleagueFirst.selfMethod("入参dto")
