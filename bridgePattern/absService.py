from bridgePattern.absImpliment import AbsImpliment


class AbsService:
    def __init__(self, handle: AbsImpliment):
        self._handle = handle

    @property
    def handle(self):
        return self._handle

    def process(self, param):
        pass
