from proxyPattern.aiCoder import AiCoder
from proxyPattern.aiCoderProxy import AiCoderProxy

"""
  代理模式demo
"""
if __name__ == "__main__":
    coder = AiCoder()
    proxy = AiCoderProxy(coder)
    proxy.programming()
