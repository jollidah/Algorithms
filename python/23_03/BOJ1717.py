# 집합의 표현

import sys

def getParent(a) -> int:
        while a != p[a]:
            a = p[a]
        return a

def union(a, b) -> None:
    pa = getParent(a)
    pb = getParent(b)  
    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb

def compareParent(a, b) -> bool:
    if a == b: return True
    return getParent(a) == getParent(b)

n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]
for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    if t == 0:
        union(a, b)
    else:
         print("YES" if compareParent(a, b) else "NO")

# https://www.acmicpc.net/problem/1717