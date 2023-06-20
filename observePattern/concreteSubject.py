from observePattern.absObservable import AbsObservable


class ConcreteSubject(AbsObservable):

    def dosomething(self, p):
        print(f"ConcreteSubject -> dosomething,p={p}")

    def change(self, p):
        self.dosomething(p)
        super().notify(p)
