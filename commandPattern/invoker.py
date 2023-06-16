from commandPattern.absCommand import AbsCommand


class Invoker:
    def __init__(self, absCmd: AbsCommand):
        self._absCmd = absCmd

    def excute(self):
        return self._absCmd.excute();