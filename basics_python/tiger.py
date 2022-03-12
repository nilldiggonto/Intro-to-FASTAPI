from animal import WildAnimal

class Tiger(WildAnimal):
    def __init__(self):
        super().__init__('Main class name')
        print('creating a tiger constructor')
    
    def stalk(self):
        print(f'{self.name} is stalking me')

    def rename(self,name):
        super().setName(name)


x = Tiger()
x.stalk()
x.roar()
x.rename('test')
x.roar()
x.stalk()