'''
ラムダ関数
'''
# def func():
#     pass

# def mySort(string):
#     return string[-1]

# mylist = ['python','django','tkinter','requests','kivy']

# mylist.sort(key=mySort)
# print(mylist)

mylistA = [('natou',78),('yoguruto',90),('coffe',120),('cola',120),('saba',100)]
mylistA.sort(key=lambda tpl:tpl[1],reverse=True)
print(mylistA)

#map関数 filter関数
numbers = [1,2,3,4,5]
for num in map(lambda num:num**2,numbers):
    print(num)

for num in filter(lambda num:num%2,numbers):
    print(num)

