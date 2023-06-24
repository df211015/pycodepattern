from iteratorPattern.iterator import Iterator


class ConcreteIterator(Iterator):
    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            return None

    def __init__(self, collection):
        self._collection = collection
        self._index = 0
