'''
error catch

try exceptでしよう
'''

yourInput = input('input >')

try:
    number = int(yourInput)
    print(10/number)
except ValueError:
    print('文字列が入力されました ')
except ZeroDivisionError:
    print('ZeroDivision')
except:
    print('OtherError')

yourInput2 = input('10/nの nにあたる数を好きに入れてください>')
if not yourInput2.isnumeric():
    print('文字が入力されました')
elif yourInput2 == '0':
    print('０で割ったらいけません')
else:
    number2 = int(yourInput2)
    print(10/number2)
    
