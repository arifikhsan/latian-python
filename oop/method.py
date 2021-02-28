class Piglet:
    name = 'piglet'
    years = 0

    def speak(self):
        print('Oink! i\'m {}! Oink!'.format(self.name))

    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = 'Hamlet'
hamlet.speak()

petunia = Piglet()
petunia.name = 'Petunia'
petunia.speak()

hamlet.years = 2
print(hamlet.pig_years())
