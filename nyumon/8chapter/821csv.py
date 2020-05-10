'''
8.2.1 CSV
'''
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa','Klebb'],
    ['Mister','Big'],
    ['Auric','Goldfinger'],
    ['Ernst','Blofeld'],
]

with open('villais','wt') as fout: #コンテキストマネージャ
    csvout = csv.writer(fout)
    csvout.writerows(villains)


# with open('villais','rt') as fin: #コンテキストマネージャ
#     cin = csv.reader(fin) #cinオブジェクトの中にforループで抽出できる行を作ってくれる
#     villains2 = [row for row in cin] #リスト内包表記

with open('villais','rt') as fin:
    #fieldnames引数を省略するとファイルの第一行の値(first,last)を列ラベル、辞書キーとして使えという意味になる
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains2 = [row for row in cin]

print(villains2)

with open('villais2', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains2)


