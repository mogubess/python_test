'''
クラス
'''
print(type([1]))

class Student:
    def __init__(self,name):
        self.name = name
        self.score = {}
    
    def add_score(self,subject_name,point):
        self.score[subject_name] = point

    def get_score(self,subject_name):
        return self.score.get(subject_name,'その教科はまだ')

#
a = Student('takeda')
a.add_score('math',50)

b = Student('tokita')
b.add_score('math',100)

print(a.name)


'''
継承
'''
class Character:
    def __init__(self,name):
        self.name = name
        print('Character')

class Monster(Character):
    def __init__(self,name):
        super().__init__(name)
        print('Monster')


char_a = Monster('キャラA')
print(char_a.name)



'''
クラスの属性 インスタンスの属性
'''
class AAA:
    name = 10

class BBB:
    def __init__(self,name):
        self.name = name

a = AAA
b = BBB(10)

print(a.name)

print(b.name)

'''
プライベートな属性
Pythonではアンダースコアで示せるが、実際にはアクセスできる
開発マナーみたいなもの
'''

'''
アンダースコアが２つは通常アクセスできない
self.__value

a = A
a._A__value
'''


'''
property
'''
class Person:

    def __init__(self,n):
        self.name = n # name.setterのnameメソッド呼び出し、dataに格納される

    @property
    def name(self):
        '''self.nameやperson.nameとアクセスすると、このメソッドが呼び出されます'''
        return self.data

    @name.setter
    def name(self,value):
        '''self.name = ''やperson.name=''で呼び出される。dataに格納します'''
        if not value:
            value = '名無しの権瓶'
        self.data = value

person = Person('AAA')
print(person.name)


'''
特殊メソッド
'''
#__init__など

#def __len__(self)
#a = A()
#print(len(a))

#def __iter__ forで呼び出される
#def __next__ forで呼び出される

#def __getitem__(self,key):
#   return key

#a = A()
#print(a[0])

class A:
    def __init__(self,data):
        self.name = data
    def __str__(self):     #オブジェクト事の文字列
#        self.name = 'attr'
        return self.name

a = A('dddd')
print(a)
