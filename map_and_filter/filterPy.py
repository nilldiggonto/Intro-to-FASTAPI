import random
v = [random.randrange(100) for x in range(10)]
print(v)

def lowerFunc(value):
    if value < 50:
        return True
    else:
        return False
print('----------------')
print('filter')
f = filter(lowerFunc,v)
print(list(f))


#FILTER TYPES
#------------
print('--------------')

class Animal:
    name = ''
    def __init__(self,name):
        self.name = name
    
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)


animals = []
for x in range(10):
    name = 'animal'+ str(x)
    if (x % 2) == 0:
        cat = name + ' cat'
        animals.append(Cat(cat))
    else:
        dog = name + ' dog'
        animals.append(Dog(dog))

for a in animals:
    print(f'Animal: {a.name}')

def onlyCat(value):
    return isinstance(value,Cat)


def onlyDog(value):
    return isinstance(value,Dog)

for c in list(filter(onlyCat,animals)):
    print(f'Cat: {c.name}')