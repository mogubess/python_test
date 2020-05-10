'''
ローカル変数とグローバル変数
'''
#num = 1

def test():
    global num 
    num = 200
    print(num)


test()
print(num)