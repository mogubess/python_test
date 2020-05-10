'''
オリジナル例外
'''

class UppercaseException(Exception):
    pass

# words = ['eeenie', 'meenie', 'miny', 'MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)

try:
    raise UppercaseException('panic')
except UppercaseException as exc:
    print(exc)
