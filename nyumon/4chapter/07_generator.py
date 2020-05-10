'''
ジェネレータ
Pythonのシーケンスを作るオブジェクト

ジェネレータはイテレータのデータソースとなることが多い
range()なども使われている
xrange() python2で使える

yieldを駆使して、処理を記載する
'''

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range()

print(type(ranger))

for x in ranger:
    print(x)

