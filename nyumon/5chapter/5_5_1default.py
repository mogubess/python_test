'''
5.5.1 setdefault() defaultdict()
存在しないキーで辞書にアクセスすると例外を発生する
'''

periodicTable = {'Hydrogen':1, 'Helium':2}
print(periodicTable)

#setdefault 存在しないキーと値は生成する
carbon = periodicTable.setdefault('Carbon',12)
print(periodicTable)

#すでにあるキーは上書きされない
helium = periodicTable.setdefault('Helium', 947)
print(periodicTable)

#defaultdictに辞書の初期値を渡すもしくはfunction intはint() 整数の0を返す
from collections import defaultdict
periodicTable = defaultdict(int)

periodicTable['Hydrogen'] = 1
print(periodicTable['Lead'])
print(periodicTable)

#functionをデフォルト値にした時の話
def noIdea():
    return 'Huh?'

bestiary = defaultdict(noIdea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilink'
print(bestiary['A'])
print(bestiary['C'])

#デフォルト値を省略すると defaultdict()はNoneになる

#lambdaを使うとdefaultdict内で関数を定義できる
bestiary2 = defaultdict(lambda : 'Huh?')

print(bestiary2['E'])

from collections import defaultdict
foodCounter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    foodCounter[food] += 1

for food, count in foodCounter.items():
    print(food, count)

