from bridgePattern.absImplement import AbsImplement


class ConcreteImplement(AbsImplement):
    def dosomething(self, param):
        print(f"ConcreteImplement -> dosomething:{param}")
