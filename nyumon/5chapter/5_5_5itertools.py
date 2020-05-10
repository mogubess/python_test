'''
5.5.5 itertoolsによるコード構造の反復処理
'''

#chain
import itertools
for item in itertools.chain([1,2],['a','b']):
    print(item)


#cycle(無限反復子)
# for item in itertools.cycle([1,2]):
#     print(item)

#accumulate(要素をひとつにまとめた値を計算する　デフォルトでは和を計算する)
for item in itertools.accumulate([1,2,3,4]):
    print(item)

#accumlate()は第２引数として関数を受付ることができる
#この関数は２個の引数を受付、１個の結果を返すものでなければならない。
def multiply(a,b):
    return a * b

for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)
