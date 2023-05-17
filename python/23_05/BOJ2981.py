# 검문

import sys
from math import gcd
from math import sqrt

input = sys.stdin.readline
n = int(input().strip())
nList = sorted([int(input().strip()) for _ in range(n)])
interval = [nList[i + 1] - nList[i] for i in range(n - 1)]
res = set()

greatestCD = interval[-1]
for i in range(n - 2):
    greatestCD = gcd(greatestCD, interval[i])
for div in range(1, int(sqrt(greatestCD)) + 1):
    q, r = divmod(greatestCD, div)
    if r == 0:
        res.add(q)
        res.add(div)
res.remove(1)
print(*sorted(res))

# https://www.acmicpc.net/problem/2981