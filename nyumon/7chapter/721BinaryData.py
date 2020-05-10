'''
7.2 バイナリデータ バイトとバイト列
'''

#bytesはイミュータブルで、バイトのタプルのようなものだ

#bytearrayはミュータブルで、バイトのリストのようなものだ

blist = [1,2,3,255]
theBytes = bytes(blist)
print(theBytes)

theByteArray = bytearray(blist)
print(theByteArray)

