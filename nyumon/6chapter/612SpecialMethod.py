'''
6.12 特殊メソッド
一覧は以下リンクに記載
http://bit.ly/pydocs-smn
'''

class Word():
    def __init__(self, text):
        self.text = text
    #self == other
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    #self != other
    def __ne__(self,word2):
        pass

    def __str__(self):
        return self.text
    #対話型インタプリタで使う（通常はいらない？）
    def __repr__(self):
        return 'Word("' + self.text + '")'


first = Word('ha')
second = Word('HA')
third = Word('eh')

if first == second:
    print('True')

if first == third:
    print('True 2')

print(first)

###############################################################
    #self < other
    #def __lt__

    #self > other
    #def __gt__

    #self <= other
    #def __le__

    #self >= other
    #def __ge__

    #self + other
    #def __add__

    #self - other
    #def __sub__

    #self * other
    #def __mul__

    #self // other
    #def __floordiv__

    #self / other
    #def __truediv__

    #self % other
    #def __mod__

    #self ** pow
    #def __pow__
