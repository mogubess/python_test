'''
ファイルの読み込み
'''
with open('hello.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line,end='')

with open('hello.txt', 'r') as f:
    print(f.read())

with open('hello.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

#chunk ごと
with open('hello.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        print(f.tell())
        if not line:
            break

#f.tell(現在位置)
#f.seek(検索位置(ファイルの先頭からに絶対位置))



