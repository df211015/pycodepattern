from commandPattern.absCommand import AbsCommand

class ConcreteCommand(AbsCommand):
    def excute(self):
        print("ConcreteCommand -> excute")