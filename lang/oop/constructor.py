class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return 'color: {}, flavor: {}'.format(self.color, self.flavor)

apple = Apple('red', 'sweet')
print(apple.color)
print(apple.flavor)

print(str(apple))
