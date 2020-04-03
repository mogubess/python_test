'''
ファイルの読み込み
'''
with open('hello.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line,end='')