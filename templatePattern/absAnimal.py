from abc import abstractmethod


class AbsAnimal:
    def run(self):
        self.ready()
        self.hunt()

    @abstractmethod
    def ready(self):
        pass

    @abstractmethod
    def hunt(self):
        pass