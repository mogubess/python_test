'''
Property
'''


class Duck():
    def __init__(self, inputName):
        self.hiddenName = inputName
    def getName(self):
        print('inside the getter')
        return self.hiddenName
    def setName(self, inputName):
        print('inside the setter')
        self.hiddenName = inputName
    #変数のGetterとSetterを定義できる
    name = property(getName,setName)

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Daffy'

print(fowl.name)