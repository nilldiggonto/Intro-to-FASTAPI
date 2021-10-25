#skipping
for _ in range(5):
    print('oiii')

#-------------
#single underscore
from testClass import *
p = Person()
p.setName('oni')
#weak private scope
p._name = 'yo'
print(f'I changed your name to {p._name}')


#-----------
#Double underscore
print('--------------')
p = Person()
p.work()
# p.__think() #you can't access
# c = Child()
# c.testDouble()

#------------------
#After(Any)
#helps to avoid same name conflict
print('------------')
class_ = Person()
class_.work()

#__beforeAfter__
print('---------')
p = Person()
p.__call__()