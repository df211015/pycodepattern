from iteratorPattern.concreteAggregate import ConcreteAggregate

if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add("item_1")
    aggregate.add("item_2")
    aggregate.add("item_3")

    iterator = aggregate.create_iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)