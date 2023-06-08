class SuperStar:
    def __init__(self, builder):
        self._name = builder.name
        self._age = builder.age
        self._favorite = builder.favorite

    def toLocalString(self):
        print(f"name={self._name},age={self._age},favorite={self._favorite}")
