'''
デコレータ

デコレータは複数持てる
'''

def documentIt(func):
    def newFunction(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args )
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs )
        print('Result:', result)
        return result
    return newFunction

@documentIt
def addInts(a,b):
    return a + b

addInts(3, 5)

