from statusPattern.absStatus import AbsStatus


class StatusOfEnd(AbsStatus):
    def handle(self, p):
        print(f"StatusOfEnd -> handle,p={super().toJson(p)}")
