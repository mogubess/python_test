'''
Bottleテスト

bottleのrunには以下の機能がある
 debug=True HTTPエラーが返されたときにデバッグべーじが作られる
 reload=True Pythonコードに変更を加えたときにブラウザにページが再ロードされる
 開発者サイト(http://bottlepy.org/docs/dev/)
'''
from bottle import route, run


#URLと直後の関数を紐づけるため
@route('/')
def home():
    return "It ins't fancy, but it's my home page"

#run関数は、bottleに組み込まれているPythonによるテストウェブサーバーを実行する。
run(host='localhost', port=9999)

