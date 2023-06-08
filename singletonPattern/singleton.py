class Singleton:
    def __init__(self, name):
        self._name = name

    def dosomething(self):
        return "singleton --> dosomething"

singleton = Singleton("singleton")
