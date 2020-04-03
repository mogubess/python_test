"""Fizz Buzz

1～n回まで繰り返し
３の倍数はFizz
５の倍数はBuzz
１５の倍数はFizz　Buzz
それ以外は数字の出力をする

"""


n = 100
for i in range(1,n+1):
    if 0 == i % 15:
        print('Fizz Buzz',end='')
    elif 0 ==  i % 3:
        print('Fizz',end='')
    elif 0 == i % 5:
        print('Buzz',end='')
    else:
        print(i,end='')


for i in range(1,101):
    message = ""
    if i % 3 == 0:
        message += 'Fizz'
    if i % 5 == 0:
        message += 'Buzz'
    
    print(message or i, end=' ')
