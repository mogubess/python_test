'''
復習問題 4-9
'''

def testAA():
    for i in range(10):
        if i % 2 == 1:
            yield i

gene = testAA()

for x in gene:
    print(x)

