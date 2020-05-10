'''
ウェブを解きほぐす
'''
import urllib.request as ur
url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
conn = ur.urlopen(url)
#connはいくつかのメソッドを持ちHTTPResponseオブジェクトです
print(conn)

data = conn.read()

print(data)

#HTTPステータスコード
#200=OK
print(conn.status)

#ステータスコード

#1xx(情報)
#サーバーは要求を受け取ったが、クライアントに対して知らせるべき追加情報がある。

#2xx(成功)
#要求は正しく機能した、200以外の成功コードには、追加情報が含まれている。

#3xx(リダイレクト)
#リソースが移動しているので、応答はクライアントに対して新しいＵＲＬを返す。

#4xx(クライアントエラー)
#クライアントサイドに問題がある、有名な404などがある

#5xx(サーバーエラー)
#500は汎用のエラーコードである。502(不正なゲートウェイ)は、ウェブサーバーと
#バックエンドアプリケーションサーバーの間に接続に問題があるときに返される。

#MIMEタイプの確認
print(conn.getheader('Content-Type'))

#text/plain テキスト文字列
#text/html  ＨＴＭＬ

for key, value in conn.getheaders():
    print(key, value)


#その他のＨＴＴＰヘッダー

# Connection close
# Content-Length 99
# Content-Type text/plain; charset=utf-8
# Cache-Control max-age=300
# Content-Security-Policy default-src 'none'; style-src 'unsafe-inline'; sandbox
# ETag W/"9f5651c47de1d25d4c531d22c98b96ea61d10d7e4f5c6eb6cbeecd9e01cdfbf8"
# Strict-Transport-Security max-age=31536000
# X-Content-Type-Options nosniff
# X-Frame-Options deny
# X-XSS-Protection 1; mode=block
# Via 1.1 varnish (Varnish/6.0)
# X-GitHub-Request-Id DE38:7449:3544D:3CDCD:5EB1A67E
# Accept-Ranges bytes
# Date Tue, 05 May 2020 18:06:45 GMT
# Via 1.1 varnish
# X-Served-By cache-hnd18743-HND
# X-Cache HFM, MISS
# X-Cache-Hits 0, 0
# X-Timer S1588702005.854104,VS0,VE240
# Vary Authorization,Accept-Encoding
# Access-Control-Allow-Origin *
# X-Fastly-Request-ID b5961fa64d790d5bb2eb8f8207864237fda66042
# Expires Tue, 05 May 2020 18:11:45 GMT
# Source-Age 0
