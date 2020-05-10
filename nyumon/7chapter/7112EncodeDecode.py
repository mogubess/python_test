'''
7.1.1.2 UTF8によるエンコード、デコード

文字列をバイト列に[エンコード]する手段
バイト列を文字列にデコードする手段

ウェブページなどの他のソースからコピーアンドペーストでPython文字列を作る時は
ソースがUTF-8形式でエンコードされていることを確かめること
Latin-1 Windows 1252でエンコードされたテキストをPython文字列にコピーしている
例は非常によく見かける
あとで無効なバイトシーケンスだとして例外を引き起こすことになる。
'''
#
#
#7.1.1.3 エンコーディング
#
#
#ascii
#utf-8
#latin-1
#cp-1252
#unicode-escape

snowman = '\u2603'

print(len(snowman))

ds = snowman.encode('utf-8') #byte変数のため文字サイズは３となる

print(len(ds))

print(ds)

#例外は発生させずに、データを捨てる（空)
ds2 = snowman.encode('ascii', 'ignore')
print(ds2)

#エンコードできない文字を？に置き換える
ds3 = snowman.encode('ascii', 'replace')
print(ds3)

#unicode-escape形式のPython Unicode文字列を生成する
#Unicodeエスケープシーケンスの表示可能バージョンが必要なら、これを使うことになるだろう
ds4 = snowman.encode('ascii', 'backslashreplace')
print(ds4)

#ウェブページで使えるエンティティの文字列を生成する
ds5 = snowman.encode('ascii', 'xmlcharrefreplace')
print(ds5)

#
#
#デコーディング
#
#
#なんらかの外部ソース（ファイル、データベース、ウェブサイト、ネットワークＡＰＩ）
#からテキストを取り出したとき、そのテキストはバイト文字列としてエンコードされている
#難しいのは、実際にどのエンコーディングが使われているのかを知ることだ

place = 'caf\u00e9'
print(place)
print(type(place))

placeBytes = place.encode('utf-8')
print(placeBytes)
print(type(placeBytes))

place2 = placeBytes.decode('utf-8')
print(place2)
print(type(place2))

#違う文字コードでデコードすると例外が発生することもある
#今回は0xc3がASCIIの文字コードに当てはまらないので
#place3 = placeBytes.decode('ascii')
#print(place3)
#print(type(place3))

place4 = placeBytes.decode('latin-1')#windows-1252
print(place4)
print(type(place4))

