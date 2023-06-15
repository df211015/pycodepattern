from bridgePattern.absImplement import AbsImplement


class AbsService:
    def __init__(self, handle: AbsImplement):
        self._handle = handle

    @property
    def handle(self):
        return self._handle

    def process(self, param):
        pass
