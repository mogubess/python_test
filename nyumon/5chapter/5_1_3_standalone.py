'''
スタンドアローンプログラム
コマンドライン引数
モジュールとimport文
5.1 - 5.3
'''

import sys
print('Program arguments:', sys.argv)

import report
description = report.getDescription()
print("Todays Wheather:", description)

#別名によるモジュールのインポート
import report as wr
description2 = wr.getDescription()
print("Todays Wheather2:", description2)

#必要なものだけをインポートする方法
from report import getDescription
description3 = getDescription()
print("Todays Wheather3:", description3)

#必要なものを別名でインポートする方法
from report import getDescription as doIt
description4 = doIt()
print("Todays Wheather4:", description4)

#モジュールのサーチパス
import sys
for place in sys.path:
    print(place)