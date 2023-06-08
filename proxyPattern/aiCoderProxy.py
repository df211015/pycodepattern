from proxyPattern.iCoder import ICoder


class AiCoderProxy(ICoder):
    """
    对像代理
    """

    def __init__(self, proxy):
        self._proxy = proxy

    def begin(self):
        print("I am a proxy,programming start...")

    def end(self):
        print("I am a proxy,programming end")

    def programming(self):
        proxy: ICoder = self._proxy
        if proxy is not None:
            self.begin()
            proxy.programming()
            self.end()
        else:
            print("代理实例不存在!")
