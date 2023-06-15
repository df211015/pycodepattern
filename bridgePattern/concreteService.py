from bridgePattern.absImpliment import AbsImpliment
from bridgePattern.absService import AbsService


class ConcreteService(AbsService):
    def __init__(self, handle: AbsImpliment):
        super().__init__(handle)

    def process(self, param):
        obj = super().handle
        if obj is not None:
            print(f"ConcreteService -> process,param:{param}")
            obj.dosomething(param)
