'''
Ｐython入門 ジェネレータ
'''

def myrange(first=0, last=10, step=2):
    number = first
    while number < last:
        yield number
        number += step

range = myrange(1,10)

for x in range:
    print(x)
