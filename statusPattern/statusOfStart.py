from statusPattern.absStatus import AbsStatus
from statusPattern.eStatus import EStatus


class StatusOfStart(AbsStatus):
    def handle(self, p):
        print(f"StatusOfStart -> handle,p={super().toJson(p)}")
        super().context.indexOfStatus = EStatus.Run.index
