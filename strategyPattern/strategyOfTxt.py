from strategyPattern.iStrategy import IStrategy


class StrategyOfTxt(IStrategy):
    def openFile(self, path):
        print(f"使用txt打开文件,filePath:{path}")
