class Person:
    #weak scope of function
    _name = 'Use internally only'

    def setName(self,name):
        self._name = name
        print(f'Did my name changed to {self._name}')

    #private
    def __think(self):
        print('Ok i am thinking')

    def work(self):
        self.__think()

    # __beforeAfter__
    def __init__(self):
        print('ok construcccccctor')
    
    def __call__(self):
        print('call someone')

######
# class Child(Person):
#     def testDouble(self):
#         self.__think(self) #will not work