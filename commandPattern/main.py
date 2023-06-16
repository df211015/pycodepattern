from commandPattern.concreteCommand import ConcreteCommand
from commandPattern.invoker import Invoker

"""
命令模式demo
"""
if __name__ == "__main__":
    cmd = ConcreteCommand()
    invoker = Invoker(cmd)
    invoker.excute()
