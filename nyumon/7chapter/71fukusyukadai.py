'''
7.3 7-1 復習課題
'''

import unicodedata

#Unicode文字列を作り、値を代入して表示してみる
mystery = '\U0001f4a9'

print(mystery)
name = unicodedata.name(mystery)

print(name)

'''
7-2 復習問題
'''

pop_bytes = mystery.encode('utf-8')

print(pop_bytes)

pop_string = pop_bytes.decode('utf-8')

print(pop_string)

#7-4

print('My kitty cat likes %s' % 'roast beef')

#7-5

