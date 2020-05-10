'''
multiprocessingによるプロセスの作成]
ひとつのプログラムの中で複数の独立したプロセスを実行することができる。
'''
import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
        args=("I7m function %s" % n,))
        p.start()


#Process()関数は、新しいプロセスを起動し、そのなかでdo_this()を実行
#して終了する新プロセスを４個作っている


