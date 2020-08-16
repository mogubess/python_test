# -*- coding: utf-8 -*-

mystr = 'hello World'
strlen = len(mystr)

print("Len:{0}".format(strlen))

#print("mystr:{0}".format(dir(mystr)))

#print("dir:{0}".format(dir()))
print("mystr.title:{0}".format(mystr.title()))

print("mystr.__add__:{0}".format(mystr.__add__))

fmt = '私の名前は{}です。{}'
name = '太郎'

print(fmt.format(name,'なんてね'))

fmt2='{0}{1}{0}'

print(fmt2.format('佐藤','太郎'))

#fmt3 = '{lastname} {firstname}'

#print(fmt3.format(lastname='佐藤',firstname='太郎'))

lastname='佐藤'
firstname='太郎'

print(f'{lastname} {firstname}')

name = 'takada'
print('私の名前は%sです。' % name)

languages='Python,Ruby,PHP,Perl'
listA = languages.split(',')
listA.append('Test')
print(type(listA))
print(dir(listA))

separ = ','

print(separ.join(listA))

print('+'.join(listA))

poem='今日はとてもいい天気'

print(poem.replace('今日','昨日'))

name2 = 'takada'

print(name2.startswith('taka'))

print(name2.startswith('da'))

print(name2.endswith('da'))

print(name2.endswith('ka'))


print(name2.find('d'))

print(name2.index('a'))#findに似ている

#in関数

#strip

#rstrip

#lstrip

#スライス処理