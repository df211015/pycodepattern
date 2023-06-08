from builderPattern.absBuilder import AbsBuilder
from builderPattern.superStar import SuperStar


class BuilderOne(AbsBuilder):
    def build(self):
        return SuperStar(self)
