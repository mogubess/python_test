
#1+1を計算し、結果を表示する

result = 1 + 1
print(result)

names = ['tanaka','takeda','saitoh']

if 'takeda' in names:
    print('ok %s' % 'takeda')
    print('encho')
else:
    print('ng')
print('dotiramo')

#文字列比較
color = 'red'
if color == 'red':
    print('red')

elif color == 'blue':
    print('blue')
else:
    print('other')

numbers = [1,2,3,4,5]
if 1 in numbers and 2 in numbers:
    print('numbers ok')

namaes=['satoh','yoshida','takeda','suzuki']
syozoku=['daigaku','koukou','onngakku','hanahana']
if namaes:
    print(namaes[0])

for name in namaes:
    for char in name:
        print(char)

#for key,value in dict_instance.items():

#range
#for i in range(100):
for i in range(1,101,2):
    print(i)

my_list=list(range(1,101))
print(my_list)

#enumerate
for i,n in enumerate(namaes):
    mes = '{0} banme {1}'.format(i,n)
    print(mes)

#zip
for n,s in zip(namaes,syozoku):
    print(n,s)
