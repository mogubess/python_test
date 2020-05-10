'''
スクレイピング
'''

import requests
from bs4 import BeautifulSoup

#res = requests.get('https://www.google.com')
res = requests.get('https://torina.top')
#print(type(res))
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
for h2 in soup.find_all('h2'):
    print(h2.text)
