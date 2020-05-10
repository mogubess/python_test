'''
8.2.2 YAML
'''

import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text)
print(data['name']['first'])

