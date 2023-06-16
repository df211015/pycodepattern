from abc import ABCMeta


class AbsCommand(metaclass=ABCMeta):
    def excute(self):
        pass
