from adapterPattern.iAdaptee import IAdaptee
from adapterPattern.iTarget import ITarget


class Adapter(ITarget):

    @property
    def iAdaptee(self):
        return self._iAdaptee

    @iAdaptee.setter
    def iAdaptee(self, adaptee: IAdaptee):
        self._iAdaptee = adaptee

    def convert(self):
        print("通过适配器转化为ITarget对像")
        self._iAdaptee.dosomething()
