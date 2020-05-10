'''
復習問題 4-11
'''

class OopsException(Exception):
    pass

try:
    raise OopsException()
except OopsException as exc:
    print("Caught an oops " + OopsException.__name__)
