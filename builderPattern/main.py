from builderPattern.director import Director

# 通过Director管理类获取对像实例
superStar = Director().getSuperStar()
superStar.toLocalString()