
def outline(func):
    def inner(*args,**kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args,**kwargs)
        print('_'*20)
    return inner

@outline
def test_one(x,y):
    try:
        z  = x/y
        print(f'Result:{z}')
    except:
        print(f'something went wrong x:{x} ,y:{y}')
    finally:
        print('complete')

test_one(2,0)

print('two----------------------------')
@outline
def test_two(x,y):
    try:
        assert(x>0)
        assert(y>0)
        # z  = x/y
        # print(f'Result:{z}')
    except AssertionError:
        print(f'Assert Error {x} , {y}')
    except Exception as e:
        print(f'something went wrong x:{x} ,y:{y}, issue:{e}')
    else:
        z = x/y
        print(f'Result is: {z}')
    finally:
        print('complete')

test_two(2,0)

#----------------
print('--------------------')
class CatError(RuntimeError):
    def __init__(self,*args):
        self.args = args

@outline
def test_three(qty):
    try:
        if not isinstance(qty,int):
            raise TypeError('Must be integer')
        if qty < 9:
            raise CatError('Must have more than 9 cats')
        print(f'you have some cats')
    except Exception as e:
        print(f'errors: {e.args}')
    finally:
        print('done')

test_three(12)