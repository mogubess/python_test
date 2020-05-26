'''
コードデバッグ
'''


def func(*arg, **kwargs):
    "varsによる引数表示"
    print(vars())
    first = 1
    second = 2
    third = 3
    print(first)
    print(second)
    print(third)


if __name__ == '__main__':
    func(3,2,1,'wait!', 'uh...',wine='merlot', entree='mutton', dessert='macaroon')
