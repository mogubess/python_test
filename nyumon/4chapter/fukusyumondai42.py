'''
復習問題 4-2
'''

guess_me = 7
start = 1

while True:
    if start > guess_me:
        print('oops')
        break
    elif start == guess_me:
        print('foud it!')
    else:
        print('too low')
    start = start + 1
