'''
デコレータ
'''

# def decorator(function):
#     print('decorator')
#     return function

# @decorator
# def sayHello2(textH):
#     print(textH)

# sayHello2('文字列テスト')

#debug
#既存の関数に処理を追加するのに使う
def debug(function):
    def _debug(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__, args, kwargs, result)
        return result
    return _debug

@debug
def sayHello(test22,name2='デフォ',**kwargs):
    print(test22, name2)
    for key in kwargs:
        print(key,kwargs[key] )

sayHello('ふがふが','うわ',a=1,b=2)
