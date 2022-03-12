animals = ['cat','dog','tiger','lion']

#old way to count word 
print('old way-----------')
counts = [len(x) for x in animals]
print(counts)

#moder way
print('new way-----------')
newcount = list(map(len,animals))
print(newcount)

#------------------
print('----------------------')
firstname = ('a','b','c','d')
lastname = ('1','2','3')

def mergeFunc(a,b):
    return a + ' ' + b

x = map(mergeFunc,firstname,lastname)
print(x)
print(list(x))

#----------- mapping multiple function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def doAll(func,num):
    return func(num[0],num[1])

f = (add,subtract,multiply,divide)
v = [[5,3],[2,3],[3,3],] 
n = list(v) * len(f) #will last 3 elements

print(n)

m = map(doAll,f,n)
print(list(m))
