class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny = Apple('gree', 'tart')
carnelian = Grape('purple', 'sweet')

print(granny.flavor)
print(carnelian.color)
