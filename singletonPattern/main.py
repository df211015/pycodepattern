from singletonPattern.singleton import singleton

"""
    1.模块天然就是单例的，因为模块只会被加载一次，加载之后，
      其他脚本里如果使用import二次加载这个模块时，
      会从sys.modules里找到已经加载好的模块，模块里的对象天然就是单例的，即使是在多线程环境下也是如此
    2.在任何引用singleton的脚本里，singleton都是同一个对象，这就确保了系统中只有一个Singleton的实例。
"""
print(singleton.dosomething())