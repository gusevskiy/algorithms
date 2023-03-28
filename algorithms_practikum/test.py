from typing import List, Tuple


a = 1, 8, 9
b = 2, 3, 1

def zz(a, b):
    n3 = sum([[a[i],b[i]] for i in range(len(a))],[])
    return n3

print(*zz(a, b))