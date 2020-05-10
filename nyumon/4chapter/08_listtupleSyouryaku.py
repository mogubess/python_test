'''
リストやタプルに＊をつけて展開
要素数と引数の数が一致していないとエラー
'''

def func(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)

l = ['one', 'two', 'three']

func(*l)

func(*['one', 'two', 'three'])