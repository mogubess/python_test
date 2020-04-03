'''
ジェネレータ関数
yieldを使ったものを指している
'''
def makeSquare(n):
    for i in range(1,n+1):
        yield i**2

squares = makeSquare(10)
for i in squares:
    print(i)

def myRange(start,end,step):
    curNumber = start
    while curNumber < end:
        yield curNumber
        curNumber += step

for i in myRange(1,100,1):
    print(i)