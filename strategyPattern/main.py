from strategyPattern.strategyOfTxt import StrategyOfTxt

"""
策略模式demo
基于抽象类或接口的策略实现,调用方可以方便的更新不同的策略
"""
if __name__ == "__main__":
    strategy = StrategyOfTxt()
    # strategy = StrategyOfWord()
    strategy.openFile("myFilePath")