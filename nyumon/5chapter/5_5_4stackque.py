'''
5.5.4 スタック＋キュー
dequeは両端キュー
'''

def palindrome(word):
    from collections import deque
    dq  = deque(word)
    # while len(dq) > 1:
    #     if dq.popleft() != dq.pop():
    #         return False
    # return True

    print(dq.popleft())
    print(dq.pop())


# palindrome('a')
# palindrome('racecar')
# palindrome('radar')
# palindrome('halibut')


