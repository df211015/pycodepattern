from adapterPattern.adaptee import Adaptee
from adapterPattern.adapter import Adapter

if __name__ == "__main__":
    adaptee = Adaptee()
    adaptee.dosomething()

    target = Adapter()
    target.iAdaptee = adaptee
    target.convert()
