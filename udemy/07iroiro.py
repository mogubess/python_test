"""
いろいろ
forにつくelse
forが中断されなければ、最後にたどり着く
for elseは嫌われる
"""

names=['satoh','yoshida','takeda','suzuki']

for name in names:
    if name.endswith('zuki'):
        print('ok')
        break
else:
    print('ng')


'''
リスト内包表記 ネットで色々調べてみる
'''

numbers = [1,5,6,11,3,5,7,3]
squares = [num**2 for num in numbers]
print(squares)

'''
文字列を大文字にする
'''

words = ['python','django','tkinter']
upperWords = [word.upper() for word in words]
print(upperWords)

'''
文字列を取り出して小文字にする
'''
oneWords = [char for word in words for char in word]
print(oneWords)

'''
偶数を求める　ifのサンプ
'''
evenNum = [x for x in range(1,11) if x % 2 == 0]
print(evenNum)

table = [ [] for _ in range(1,10)]
print(table)

'''
'''
table2 = [[None for  x in range(1,10)] for y in range(1,10)]
print(table2)

'''
setsの内包表記
'''
sets = {x for x in range(10)}
print(sets)

'''
dictionary
'''
dicts = {x:'デフォルト値' for x in range(10)}
print(dicts)

'''
辞書逆転
'''
score = {'math':80,'eng':20}
newScore = {value:key for key, value in score.items()}
print(newScore)

'''
タプルはできない　ジェネレータ式になる
リスト内包表記とジェネレータ内包表記の違いについて理解すること
'''
numbers = [1,5,6,11,3,5,7,3]
square_gen = (num**2 for num in numbers)
for num in square_gen:
    print(num)

print(type(square_gen))
print(dir(square_gen))


