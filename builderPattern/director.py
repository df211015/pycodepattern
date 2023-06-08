from builderPattern.builderOne import BuilderOne
from builderPattern.superStar import SuperStar


class Director:
    def __init__(self):
        pass

    def getSuperStar(self):
        # 构建者
        builder = BuilderOne()
        builder.buildName("zhangshang")
        builder.buildAge(30)
        builder.buildFavorite("coffee")

        # 通过构建者类创建对象的实例
        superStar = SuperStar(builder)
        return superStar
