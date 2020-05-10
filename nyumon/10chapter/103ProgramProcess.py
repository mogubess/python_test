'''
10.3 プログラムとプロセス
'''
import os

#プロセス
print(os.getpid())

#カレントディレクトリ
print(os.getcwd())


#ユーザID
print(os.getuid())

#グループID
print(os.getgid())

'''
サブプロセス
'''
#プログラムが出力した結果を取得したいときはgetoutput()を使えばいい
#時間がかかる外部プロセスを
import subprocess
ret = subprocess.getoutput('date')
print(ret)

#協定標準時
ret2 = subprocess.getoutput('date -u')
print(ret2)

ret3 = subprocess.getoutput('date -u | wc')
print(ret3)

#check_output()という関連メソッドは、コマンドと引数のリストを受け付ける
#デフォルトでは文字列ではなくbyte形式で標準出力だけが返される。
ret4 = subprocess.check_output(['date', '-u'])
print(ret4)

#他のプログラムの終了ステータスを見たいときには、ステータスコードと出力のタプルが返される。
ret5 = subprocess.getstatusoutput('date')
print(ret5)

#出力を受け取って処理する必要はなく、ただ終了ステータスだけを知りたいときに、call()を使えばよい
ret6 = subprocess.call('date')

print(ret6)

#subprocess.call('date -u', shell=True)
#コマンドとオプションを分けて認識させるには、shell=Trueがいる

ret7 = subprocess.call(['date','-u'])






