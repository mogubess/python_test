'''
else finaly
'''
#file = IOError
try:
    file = open('hello.txt', 'x', encoding='utf-8')
except FileExistsError:
    print('FileExist')
else:
    file.write('hello')
    file.close()
finally:
    print('Process End')

