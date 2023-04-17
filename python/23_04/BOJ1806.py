# 부분합

import sys

input = sys.stdin.readline
n, target = map(int, input().split())
l = list(map(int, input().split()))
minL = 1e9
lp, rp = 0, 0
s = l[0]
while rp < n - 1:
    if s >= target:
        minL = min(minL, rp - lp + 1)
        s -= l[lp]
        if lp == rp:
             print(1)
             exit(0)
        lp += 1

    else:
        rp += 1
        s += l[rp]
while s >= target:
        minL = min(minL, rp - lp + 1)
        s -= l[lp]
        lp += 1
print(minL if minL != 1e9 else 0)

# https://www.acmicpc.net/problem/1806