from statusPattern.context import Context
from statusPattern.eStatus import EStatus
from statusPattern.person import Person

"""
状态模式demo
"""
if __name__ == "__main__":
    ctx = Context()
    person = Person('Tom', 18, 'Beijing')
    ctx.indexOfStatus = EStatus.Ready.index
    ctx.process(person)
    ctx.process(person)
    ctx.process(person)
    ctx.process(person)
