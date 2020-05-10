'''
closer
関数内関数は、ループやコードの重複を避けるために役立つ、複数回の実行される複雑な
処理をほかの関数で実行するのである。

親関数が受け取った値を、参照したり、編集したりすることができる。
'''
def knights(saying):
    def inner():
        return "We are the knights who say: '%s'" % saying
    return inner

a = knights('Ni!')

print(type(a)) #aは関数オブジェクト <class 'function'>
print(a())

