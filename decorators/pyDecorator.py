# level 4 way to use decorator
def test_decorator(func):
    print('before')
    func()
    print('after')

#
@test_decorator
def do_something():
    print('Doing something')
print('-------------------')
# lever 30 way to use decorator
def makeBold(func):
    def inner():
        print('before')
        func()
        print('after')
    return inner

@makeBold
def printName():
    print('ok your name')

printName()

print('------------')
print('Decorator with params')

def numCheck(func):
    def checkInt(a):
        if isinstance(a,int):
            if a == 0:
                print('Can not divide by zero')
                return False
            return True
        print(f'{a} is not a number')
        return False
    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numCheck
def divide(a,b):
    print(a/b)

divide(2,0)


#-------------------
print('--------------')
print('decorator with *args and **kwargs')

def outline(func):
    def inner(*args,**kwargs):
        print('`'*20)
        func(*args,**kwargs)
        print('`'*20)
    return inner

def list_items(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        print(f'args = {args}')
        print(f'kargs = {kwargs}')

        for x in args:
            print(f'args ={x}')
        
        for k,v in kwargs.items():
            print(f'{k} = {v}')
    return inner


@outline
@list_items
def display(msg):
    print(msg)

display('oi oi')



@outline
@list_items
def birthday(name='',age=0):
    print(f'Happy Birthday {name} , you are {age} years old')

birthday(name='nill',age=20)