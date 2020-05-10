'''
ポリモーフィズムの緩やかな実装を持っている
クラスの種類に関わらず、異なるオブジェクトに対して、同じ操作を適用する
'''

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elemer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bug Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'


brook = BabblingBrook()

print(brook.says())
print(brook.who())


def whoSays(obj):
    print(obj.who(), 'says', obj.says())

whoSays(hunter)
whoSays(hunted1)
whoSays(hunted2)
whoSays(brook)
