from statusPattern.absStatus import AbsStatus
from statusPattern.eStatus import EStatus
from statusPattern.statusOfEnd import StatusOfEnd
from statusPattern.statusOfReady import StatusOfReady
from statusPattern.statusOfRun import StatusOfRun
from statusPattern.statusOfStart import StatusOfStart


class Context:
    def __init__(self):
        self._indexOfStatus = None
        self._dicStatus = {EStatus.Ready.index: StatusOfReady(),
                           EStatus.Start.index: StatusOfStart(),
                           EStatus.Run.index: StatusOfRun(),
                           EStatus.End.index: StatusOfEnd()}

    @property
    def indexOfStatus(self):
        return self._indexOfStatus

    @indexOfStatus.setter
    def indexOfStatus(self, indexOfstatus):
        self._indexOfStatus = indexOfstatus
        self._statusHandle = self._dicStatus[indexOfstatus]
        if self._statusHandle is not None:
            self._statusHandle.context = self

    @property
    def statusHandle(self) -> AbsStatus:
        return self._statusHandle

    def process(self, p):
        self.statusHandle.handle(p)
