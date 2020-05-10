'''
モジュールのインポート(report.py)
リストからランダムに要素を選択して返す
関数単位でimportする　名前空間の制御
'''

def getDescription():
    """プロと同じようにランダムな天気を返す"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knosws']
    return choice(possibilities)
