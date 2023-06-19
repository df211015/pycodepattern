from statusPattern.absStatus import AbsStatus
from statusPattern.eStatus import EStatus


class StatusOfRun(AbsStatus):
    def handle(self, p):
        print(f"StatusOfRun -> handle,p={super().toJson(p)}")
        super().context.indexOfStatus = EStatus.End.index
