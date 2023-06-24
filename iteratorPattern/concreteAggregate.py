from iteratorPattern.aggregate import Aggregate
from iteratorPattern.concreteIterator import ConcreteIterator


class ConcreteAggregate(Aggregate):
    def create_iterator(self):
        return ConcreteIterator(self._collection)

    def __init__(self):
        self._collection = []

    def add(self, item):
        self._collection.append(item)
