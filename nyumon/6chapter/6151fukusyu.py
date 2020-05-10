'''
6-15 復習問題 6-1
'''

class Thing():
    pass

print(Thing)

example = Thing()
print(example)

#6-2(クラス属性)
class Things2():
    letters = 'abc'

print(Things2.letters)

#6-3（インスタンス属性）
class Things3():
    def __init__(self):
        self.letters = 'xyz'

example3 = Things3()

print(example3.letters)

#6-4
class Element():
    def __init__(self):
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.number = 1
    
    def dump(self):
        print('one ' +self.name)
        print(self.symbol)
        print(self.number)

    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))


example4 = Element()

print(Element)

#6-5

dict2 = {'name':'Hydrogen','symbol':'H','number':1}

class Element2():
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.symbol = kwargs['symbol']
        self.number = kwargs['number']


example5 = Element2(**dict2)
print(example5)

print(example5.name)
print(example5.symbol)
print(example5.number)

#6-6

example4.dump()

#6-7
print(example4)

#6-8
#各属性を非公開にして、ゲッターを用意する
class Element3():
    def __init__(self,**kwargs):
        self.__name = kwargs['name']
        self.__symbol = kwargs['symbol']
        self.__number = kwargs['number']

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


example5 = Element3(**dict2)

print(example5.name)

print(example5.symbol)


#6-9


