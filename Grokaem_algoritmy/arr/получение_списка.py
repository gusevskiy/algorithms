import re

rere = r'([A-z]{3,8})'

data = []
with open('list', 'r')as f:
    dat = f.read().split(' ')
    result = re.findall(rere, str(dat))
    print(result)
    print(result[197])
    print(len(result))
    print(sorted(result))
