#inheritance
from animal import WildAnimal

class Lion(WildAnimal):
    def sleep(self):
        print(f'{self.name} is sleeping')


lions = WildAnimal('lion')
lions.roar()

############
x = Lion('phebe')
x.sleep()
x.roar()
# x.setName('on')

