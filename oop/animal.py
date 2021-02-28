class Animal:
    name = ''
    sound = ''

    def __init__(self, name):
        self.name = name

    def speak(self):
        print('{}! i\'m {}! {}!'.format(self.sound, self.name, self.sound))

class Piglet(Animal):
    sound = 'Oink!'

class Cow(Animal):
    sound = 'Mooo'


hamlet = Piglet('hamlet')
hamlet.speak()

milky = Cow('Milky White')
milky.speak()
