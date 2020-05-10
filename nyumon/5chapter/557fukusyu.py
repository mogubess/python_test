'''
5.7.7 復習課題
'''
from collections import defaultdict

dictOfLists = defaultdict(list)

#リストの、末尾に要素を追加する
dictOfLists['a'].append('something for a')

#末尾に別のリストやタプルを結合
#extend()

#指定位置に要素を追加（挿入
#insert

#指定位置に別のリストやタプルを追加（挿入）: スライスを使う
#

print(dictOfLists['a'])
