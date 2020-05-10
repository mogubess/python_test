'''
復習問題 4-10
'''

def decoTest(function):
    def _debug(*args, **kwargs):
        print('start')
        result = function(*args, **kwargs)
        print(function.__name__, args, kwargs, result)
        print('end')
        return result
    return _debug

@decoTest
def sayHell():
    print('sayHell')

sayHell()