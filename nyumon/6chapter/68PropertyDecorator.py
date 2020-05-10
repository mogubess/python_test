'''
Property Decorator
'''

class Duck():
    def __init__(self, inputName):
        self.hiddenName = inputName
    
    #ゲッターメソッドの前につけるデコレーター
    @property
    def name(self):
        print('inside the getter')
        return self.hiddenName

    #セッターメソッドの前につけるデコレーター
    @name.setter
    def name(self, inputName):
        print('inside the setter')
        self.hiddenName = inputName

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Daffy'

print(fowl.name)


class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 10
print(c.diameter)

