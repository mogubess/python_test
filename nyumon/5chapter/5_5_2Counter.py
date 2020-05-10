'''
5.5.2 Counter()による要素の計算
'''

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfastCounter = Counter(breakfast)
print(breakfastCounter)

#most_common()は、すべての要素を降順で返す
print(breakfastCounter.most_common())

#引数として整数を指定する　最上位から数えてその個数分だけを表示する
print(breakfastCounter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunchCounter = Counter(lunch)

print(breakfastCounter + lunchCounter)

print(breakfastCounter - lunchCounter)

print(lunchCounter - breakfastCounter)


print(breakfastCounter & lunchCounter)

print(breakfastCounter | lunchCounter)
