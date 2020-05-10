'''
7.1.3.6 パターンの特殊文字列
'''
import string
import re
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

#数字だけPickup
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
m = re.findall('\d', printable)
print(m)

#数字、英字、アンダースコア
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
m1 = re.findall('\w', printable)
print(m1)

#空白文字
#[' ', '\t', '\n', '\r', '\x0b', '\x0c']
m2 = re.findall('\s', printable)
print(m2)

#マッチングはUnicode文字列にも適用される

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

#英字とマッチング（アクセント記号も）
#['a', 'b', 'c', 'ê', 'ĕ']
m3 = re.findall('\w', x)
print(m3)

