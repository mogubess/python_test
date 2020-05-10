'''
7.1.2 書式指定
'''

#7.1.2.1 %を使った古いスタイルの形式

print('われは %x' % 42)


#{}を使った新しいスタイル

n = 42
f = 7.03
s = 'string cheese'

print('{}{}{}'.format(n,f,s))

#引数の順序指定

print('{2}{0}{1}'.format(n,f,s))

#引数は辞書やキーワード引数でもよい
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))

#辞書
d = {'n':42, 'f':7.03, 's': 'string chees'}

print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))


#型指定子を指定する場合
print('{0:d} {1:f} {2:s}'.format(n, f, s))

#フィールド幅下限　文字数の上限　位置合わせ 右揃え
print('{0:10d} {1:10f} {2:10s}'.format(n,f,s))

#＞右揃え　＜左揃えにもできる
print('{0:<10d} {1:<10f} {2:<10s}'.format(n,f,s))

#中央揃え　^
print('{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s))

#パディング
print('{0:!^20s}'.format('BIG SALE'))


