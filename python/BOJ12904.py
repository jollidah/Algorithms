# 저울

import sys

a = int(sys.stdin.readline().strip())
wList = list(map(int, sys.stdin.readline().split()))
wList.sort()
n = 1
p = 0
while p < a:
    if n >= wList[p]:
        n += wList[p]
        p += 1
    else:
        break
print(n)

# https://www.acmicpc.net/problem/2437