from interpretedPattern.expression import Expression


class AndExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        self._expression1 = expression1
        self._expression2 = expression2

    def interpret(self, context):
        return self._expression1.interpret(context) and self._expression2.interpret(context)
