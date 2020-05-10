'''
9.2.5 Flask
'''
from flask import Flask

app = Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return thing

#runを呼び出し時に、debugをTrueをセットすることには、別のメリットがある。
#サーバーコードで例外が発生すると、Flaskはどこで何が問題を起こしたかについての
#役に立つ詳細情報を特別な書式で表示したページを返してくる。
#コマンドを入力すると、サーバプログラムの変数の値を見ることができる。

#本番稼働サーバではdebug=True(自動再ロードも有効)をしてはいけない
app.run(port=9999, debug=True)

