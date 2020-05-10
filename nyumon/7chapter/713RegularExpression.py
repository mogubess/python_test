'''
正規表現
'''

import re
source = 'Young Frankenstein'
m = re.match('You', source) # matchはsourceの先頭がパターンに一致するかどうかを見る
if m: #matchはオブジェクトを返す。　マッチした部分を確かめる
    print(m.group())

#先頭からのマッチング
m2 = re.match('^You', source)
if m2:
    print(m2.group())

m3 = re.match('Frank', source)
if m3:
    print(m3.group())
else:
    print('none')

#最初に見つけた文字列をそのまま返す
m4 = re.search('Frank', source)
if m4:
    print(m4.group())

#.は任意の一文字
#*は任意の個数の直前
#.*は任意の個数を任意の文字という意味
m5 = re.match('.*Frank',source)
if m5:
    print(m5.group())

#findall()
#文字列全体から、一致するものをすべてリスト化して返す
m6 = re.findall('n', source)
#split()
print(m6)

m7 = re.findall('n.', source)
print(m7)

#最後nで終わっているのもを検索するときは、?でnの後はオプションであることを明示する
m8 = re.findall('n.?', source)
print(m8)

#split()
#検索文字列で分割して、リストを作成している
m9 = re.split('n', source)
print(m9)

#sub()
#検索文字列に代わりを別の文字列で置き換える
#stringのreplaceに置き換える
m10 = re.sub('n', '?', source)
print(m10)

