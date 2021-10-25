
a = (1,23,4)

for i in a:
    print(i)

print('--------------')
animals = ['cow','cat','rat']
i = iter(animals)
print(i)
print(next(i))
print(next(i))
print(next(i))
#-----------------
print('-'*20)
import random
class Lottery:
    def __init__(self):
        self._max = 5

    def __iter__(self):
        for _ in range(self._max):
            yield random.randrange(0,100)

    def setMax(self,value):
        self._max = value

print('-'*10)
lotto = Lottery()
lotto.setMax(10)
for x in lotto:
    print(x)
print('-'*10)
