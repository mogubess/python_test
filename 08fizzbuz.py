'''
Fizz Buzzを一行で作成する
'''

print(''.join(['Fizz'*(num%3==0)+'Buzz'*(num%5==0) or str(num) for num in range(1,101)]))

