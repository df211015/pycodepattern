import enum


class EStatus(enum.Enum):
    Ready = 1, "开始"
    Start = 2, "起步"
    Run = 3, "运行"
    End = 4, "结束"

    def __init__(self, index, description):
        self._index = index
        self._description = description

    @property
    def index(self):
        return self._index

    @property
    def description(self):
        return self._description
