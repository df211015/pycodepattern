class A:
    def say(self):
        print("A")

class B(A):
    def say(self):
        super().say()


class C(A):
    def say(self):
        print("C")


class D(B):
    """
    super 是一个类，其中第二个参数是个 class 或者 object，决定了使用怎样的 mro。
    第一个参数是个 class，决定了从 mro 哪个 class 后面的 class 开始寻找，并将函数绑定到第二个参数上。两个参数都是可选的。
    这时 super 会将他所在的类当作第一个参数，将所在函数的第一个参数当作自己的第二个参数。
    显然，这样省略参数的 super 不能在类之外直接使用。
    """
    def say(self):
        super().say()

d = D()
d.say() # C
