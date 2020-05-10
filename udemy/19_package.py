#from calc.add import execute
import calc
result = calc.execute(1,39)
print(result)

result2 = calc.execute2(5,3)
print(result2)

'''
init.pyが先に読み込まれる

importの相対パス指定

import calc

result = calc.execute(1,3)
'''