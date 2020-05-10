'''
6.13 コンポジション
'''

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print(self.bill.description, self.tail.length)

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill,tail)
duck.about()

'''
6.14クラスの継承よりオブジェクトを渡して、新しいオブジェクトを生成する
・動作は同じだが、内部状態は異なる複数のインスタンスを必要とするときには、
　オブジェクトがもっとも役に立つ。
・クラスは継承をサポートするが、モジュールはサポートしない
・何かをひとつだけ必要とするときには、モジュールがよい。Pythonモジュールは、
　プログラムに何度参照されても、１個のコピーしかロードされない
　Pythonモジュールはシングルトンとして使える
・複数の値を持つ変数があり、これらを複数の関数に引数として渡せるときには、それ
　をクラスとして定義したほうがよい場合がある。
・問題にとってもっとも単純な方法を使う。辞書、リスト、タプルは、モジュールよりも単純で小さく高速
'''


