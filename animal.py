#This is human class
class Animal:
    name    =   ''
    age     =   0
    gender  =   ''

    def __init__(self,name,age=0,gender='male'):
        self.name   =   name
        self.age    =   age
        self.gender =   gender
        print(f'Constructor for {self.name}')
    
    def talk(self):
        print(f'{self.name} talking')
    #---
    def sleep(self):
        print(f'{self.name} sleeping')
    #--
    def hungry(self):
        for x in range(5):
            self.talk()
    #--
    def eat(self):
        print(f'{self.name} eating')
    #-
    def description(self):
        print(f'{self.name} is a {self.gender} and {self.age} years old')

###########################
class WildAnimal:
    def __init__(self,name):
        self.name = name
        print('WildAnimal class')
    
    ##
    def roar(self):
        print(f'{self.name} roaring')
    
    def setName(self,name):
        print(f'{self} the name is {name}')
        self.name = name


