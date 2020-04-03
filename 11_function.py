'''
関数
'''
def hello(data):
    print('{0}'.format(data))
    if(len(data) <= 3):
        return True

#argsはタプルになる
def hello2(*args):
    print(args)
    for ag in args:
        print(ag)

#キーワード引数
def hello3(*args, **kwargs):
    print(args,kwargs)

#キーワード引数
def hello4(text, *, name='narito'):
    print(text,name)

ret = hello('tekitoudata')

print(ret)

hello2('hello2data','testtest')

hello3('hello3data','testtest','iiopu',a=1,z=2,d=3)

hello4('こんにちわ',name='太郎')



