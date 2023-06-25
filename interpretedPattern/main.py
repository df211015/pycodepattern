from interpretedPattern.orExpression import OrExpression
from interpretedPattern.terminalExpression import TerminalExpression

"""
解释器模式demo
设计阶段,区分出哪些是终结符,哪些是非终结符
"""
if __name__ == "__main__":
    zhangshan = TerminalExpression("张三")
    lisi = TerminalExpression("李四")
    orExpression = OrExpression(zhangshan, lisi)
    mtach = orExpression.interpret("李四")
    print(f"李四在配置规则里吗?回答:{mtach}")
