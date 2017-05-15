from bisect import bisect_left
from itertools import combinations_with_replacement as cwr

def hoge(tpl):
    return tpl[0] * tpl[1]

(m, n) = map(int, input().split())
ms = [int(input()) for _ in range(m)]
ns = sorted(set(map(hoge, cwr([int(input()) for _ in range(n)], 2))))
for i in ms:
    print(ns[bisect_left(ns, i)] - i)

