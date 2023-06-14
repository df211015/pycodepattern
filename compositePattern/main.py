from compositePattern.func import Func
from compositePattern.menu import Menu

if __name__ == "__main__":
    root = Menu("大学")

    college01 = Menu("理学院")
    root.add(college01)
    func01 = Func("理化1班")
    func02 = Func("理化2班")
    college01.add(func01)
    college01.add(func02)

    college02 = Menu("文学院")
    root.add(college02)

    root.display(0)