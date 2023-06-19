import json
from abc import abstractmethod

from statusPattern.person import Person


class AbsStatus:
    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    def toJson(self, person: Person):
        """
        python对像转json
        :param person:
        :return:
        """
        person_dict = vars(person)
        return json.dumps(person_dict, indent=4)

    @abstractmethod
    def handle(self, p):
        pass
