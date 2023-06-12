from adapterPattern.iAdaptee import IAdaptee


class Adaptee(IAdaptee):
    def dosomething(self):
        print("Adaptee->dosomething")
