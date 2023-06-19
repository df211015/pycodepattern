from statusPattern.absStatus import AbsStatus
from statusPattern.eStatus import EStatus


class StatusOfReady(AbsStatus):
    def handle(self, p):
        print(f"StatusOfReady -> handle,p={super().toJson(p)}")
        super().context.indexOfStatus = EStatus.Start.index
