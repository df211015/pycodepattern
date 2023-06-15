from bridgePattern.absImpliment import AbsImpliment


class ConcreteImpliment(AbsImpliment):
    def dosomething(self, param):
        print(f"ConcreteImpliment -> dosomething:{param}")
