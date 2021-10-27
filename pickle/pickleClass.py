import pickle

## decorators
def outline(func):
    def inner(*args,**kwargs):
        print('*'*20)
        print(f'function: {func.__name__}')
        func(*args,**kwargs)
        print('*'*20)
    return inner

######################
class Cat:
    def __init__(self,name,age,info):
        self._name  =   name
        self._age   =   age
        self._info  =   info

    @outline
    def display(self,msg=''):
        print(msg)
        print(f'{self._name} is {self._age} years old')
        for x,y in self._info.items():
            print(f'{x} = {y}')

yourcat = Cat('phebe',15,dict(color='white',weight=10,love='eating'))
yourcat.display('First test') 

######### serialize
#--------
print('------------')
sc = pickle.dumps(yourcat)
print(sc)

with open('pickle.txt','wb') as f:
    pickle.dump(yourcat,f)

# Deserialize
print('---------------- ')
print('deserialize from string')
mycat = pickle.loads(sc)
mycat.display('deserialize')

#deserialize from file
with open('pickle.txt','rb') as f:
    cats = pickle.load(f)
cats.display('from os file')

#-----------------------------