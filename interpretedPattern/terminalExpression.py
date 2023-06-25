import string

from interpretedPattern.expression import Expression


class TerminalExpression(Expression):
    def interpret(self, context: string):
        if self._data in context:
            return True
        else:
            return False

    def __init__(self, data):
        self._data = data
