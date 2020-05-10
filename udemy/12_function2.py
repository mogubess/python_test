'''
デフォルト引数とミュータブル
'''
#引数のデフォルト値は使いまわされる
def createlist(numbers=None):
    if numbers is None:
        numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers

numbers = createlist([1,2,3])
print(numbers)

numbers2 = createlist()
print(numbers2)

numbers3 = createlist()
print(numbers3)



