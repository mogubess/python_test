'''
名前付きタプル
'''
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide ornge', 'long')

print(duck)

print(duck.bill)

print(duck.tail)

'''
辞書からも作れる
**parts のキーワード引数であることに注意
'''
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
#同じ意味
#duck2 = Duck(bill = 'wide orange', tail = 'long')

print(duck2)

'''
名前付きタプルはイミュータブルだが、１個以上のフィールドを交換した別の名前付きタプルを返すことはできる
'''
duck3 = duck2._replace(tail='magnificient', bill='crushing')

print(duck3)

'''
duckは辞書として定義することもできただろう
辞書にはフィールドを追加できる
しかし名前付きタプルには追加できない
'''
'''
イミュータプルなオブジェクトのようにふるまう
オブジェクトよりも空間的、時間的に効率がよい。
辞書スタイルの角かっこではなく、ドット記法で属性にアクセスできる
辞書のキーとして使える。
'''



