'''
プロのようにデータを操る

文字列
  Unicode文字列のシーケンス　テキストデータで扱われる
バイトとバイト列
  ８ビット整数のシーケンス　バイナリデータで扱われる
'''


def unicodeTest(value):
  import unicodedata
  name = unicodedata.name(value)
  value2 = unicodedata.lookup(name)
  print('value="%s", name="%s", value2="%s"' % (value, name, value2) )

unicodeTest('A')

unicodeTest('$')

unicodeTest('\u00a2')

unicodeTest('\u20ac')

unicodeTest('\u2603')

unicodeTest('\u00e9')

print('caf\u00e9')

print('caf\N{LATIN SMALL LETTER E WITH ACUTE}')
