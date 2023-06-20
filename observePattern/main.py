"""
观察者模式demo
"""
from observePattern.concreteSubject import ConcreteSubject
from observePattern.observerOfAPP import ObserverOfAPP
from observePattern.observerOfPC import ObserverOfPC

"""
观察者模式demo
同一个主题被多个观察者订阅,一旦主题发生变化,观察者列表均会被通知变化
"""
if __name__ == "__main__":
    pc = ObserverOfPC()
    app = ObserverOfAPP()
    subject = ConcreteSubject()
    subject.addObserver(pc)
    subject.addObserver(app)
    subject.change("主题出现变化")
