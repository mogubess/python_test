'''
関数　位置引数　キーワード引数　デフォルト引数値の指定
'''

#位置引数
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

menuA = menu('chardonnay', 'chicken', 'cake')

print(menuA)


#キーワード引数
menuB = menu(entree='beef', dessert='bage1',wine='bordeaux')

print(menuB)

#キーワード引数と位置引数の混在は可能

#*による位置引数のタプル化
def printArgs(*args):
    print('Positional argument tuple:',args)

def printMore(req1, req2, *args):
    print('Need req1:', req1)
    print('Need req2:', req2)
    print('Positional argument tuple:',args)

printArgs(3,2,1,'wait!', 'uh...')

printMore(3,2,1,'wait!', 'uh...')

#**によるキーワード引数の辞書化
def printKwargs(**kwargs):
    print('Keyword arguments:', kwargs)

printKwargs(wine='merlot', entree='mutton', dessert='macaroon')

#*argsと**kwargsを併用する場合は、*argが先


