'''
ラムダ関数
'''

def editStory(words,func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def envien(word):
    return word.capitalize() + '!'

#editStory(stairs, envien)

editStory(stairs, lambda word: word.capitalize() + '!')


 