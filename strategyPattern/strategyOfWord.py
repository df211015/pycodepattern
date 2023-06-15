from strategyPattern.iStrategy import IStrategy


class StrategyOfWord(IStrategy):
    def openFile(self, path):
        print(f"使用word打开文件,filePath:{path}")
