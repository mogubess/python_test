'''
ファイルの書き込み
'''

text="おはよう"

#ファイルを開き、ファイルを扱うためのオブジェクト
#書き込みモードw 追記モードa ファイルがある時はエラーとするx
#wbはバイナリモードの書き込み
# file = open('hello.txt', '', encoding='utf-8')

#ファイルに書き込む
# file.write(text)

#ファイルを閉じる(プロセスが終了したら、勝手に閉じる)
# file.close()


with open('hello.txt', 'w', encoding='utf-8') as file:
    file.write(text)


#バイナリモードの書きこみ