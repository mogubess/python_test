'''
5.5.3 OrderedDict()によるキー順のソート
辞書のキーの順序
'''

quotes = {
    'Moe':'A wise quy ], huh?',
    'Larry':'Qw!',
    'Curly':'Nyuk nyuk!',
}

for stooge in quotes:
    print(stooge)

from collections import OrderedDict
quotes2  = OrderedDict([
    ('Moe','A wise quy ], huh?'),
    ('Larry','Qw!'),
    ('Curly','Nyuk nyuk!'),
])

for stooge in quotes2:
    print(stooge)